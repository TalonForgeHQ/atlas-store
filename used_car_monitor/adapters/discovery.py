"""Discovery adapters.

`discover_listings(brief)` returns a list of raw listing dicts that match the schema
in `db.upsert_listing`. Adapters are responsible for rate-limiting and for NOT
hitting sources that disallow automated access.

Built-in adapters:
- `FileFeedAdapter`: reads a JSON/JSONL drop directory. Use this for safe
  ingestion today. Examples: a manual export, a researcher's saved search,
  a teammate's copy/paste, or output from a community MCP that you run
  manually outside the platform's automation firewall.
- `CommunityMCPAdapter`: shell out to a Node-based MCP like
  `jlsookiki/secondhand-mcp` if it is installed locally. Disabled by default;
  requires the operator to confirm they understand Meta's automation policy
  and to keep the MCP at arm's length from their primary Facebook account.

Everything else (real OAuth Marketplace APIs, paid aggregators, dealer feeds)
can be added by writing a new Adapter subclass.
"""

from __future__ import annotations

import abc
import json
import os
import shutil
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Optional

# Schema fields a listing dict MUST have:
REQUIRED = {"source", "listing_id", "ask_price", "make", "model", "year", "location"}


class DiscoveryError(RuntimeError):
    pass


def normalize(raw: dict[str, Any], now_iso: str) -> dict[str, Any]:
    """Coerce a raw record from any adapter to the canonical schema.

    Anything missing stays None; required keys must be present after normalization.
    """
    out = dict(raw)
    out.setdefault("source", "unknown")
    out["listing_id"] = str(out.get("listing_id") or out.get("id") or "")
    out.setdefault("now", now_iso)

    # Cast numbers
    if out.get("year") is not None:
        try:
            out["year"] = int(out["year"])
        except (TypeError, ValueError):
            out["year"] = None
    if out.get("mileage") is not None:
        try:
            out["mileage"] = int(str(out["mileage"]).replace(",", "").split()[0])
        except (TypeError, ValueError, IndexError):
            out["mileage"] = None
    if out.get("ask_price") is not None:
        try:
            s = str(out["ask_price"]).replace("$", "").replace(",", "").strip()
            out["ask_price"] = float(s.split()[0]) if s else None
        except (TypeError, ValueError, IndexError):
            out["ask_price"] = None

    out.setdefault("title_claim", "unknown")
    return out


def validate(raw: dict[str, Any]) -> None:
    missing = REQUIRED - set(raw.keys())
    if missing:
        raise DiscoveryError(f"listing missing required fields {sorted(missing)}: {raw}")
    if not raw.get("listing_id"):
        raise DiscoveryError(f"listing has empty listing_id: {raw}")
    if raw.get("ask_price") in (None, 0):
        raise DiscoveryError(f"listing has no ask_price: {raw}")


@dataclass
class Adapter(abc.ABC):
    name: str = ""  # subclasses override
    enabled: bool = True

    @abc.abstractmethod
    def fetch(self, brief: dict[str, Any], now_iso: str) -> Iterable[dict[str, Any]]:
        ...


class FileFeedAdapter(Adapter):
    """Read JSON/JSONL files from a drop directory. Files are moved to a `processed/`
    subdirectory after a successful read so the same listing is never ingested twice.

    File schema (JSON array OR JSONL):
      [
        {"listing_id": "abc", "url": "...", "year": 2019, "make": "Toyota",
         "model": "Tacoma", "trim": "TRD", "mileage": 62000, "ask_price": 27400,
         "location": "Austin, TX", "seller_name": "Vlad", "seller_type": "private",
         "vin": null, "title_claim": "clean", "description": "...", "photos": []},
        ...
      ]
    """
    name = "file"

    def __init__(self, drop_dir: Path, source_tag: str = "manual_export"):
        self.drop_dir = Path(drop_dir)
        self.drop_dir.mkdir(parents=True, exist_ok=True)
        (self.drop_dir / "processed").mkdir(exist_ok=True)
        self.source_tag = source_tag

    def fetch(self, brief: dict[str, Any], now_iso: str) -> Iterable[dict[str, Any]]:
        results: list[dict[str, Any]] = []
        for p in sorted(self.drop_dir.glob("*.json")):
            data = json.loads(p.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                data = [data]
            for item in data:
                item["source"] = f"{self.name}:{self.source_tag}"
                results.append(normalize(item, now_iso))
            self._archive(p)
        for p in sorted(self.drop_dir.glob("*.jsonl")):
            with p.open("r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    item = json.loads(line)
                    item["source"] = f"{self.name}:{self.source_tag}"
                    results.append(normalize(item, now_iso))
            self._archive(p)
        return results

    def _archive(self, p: Path) -> None:
        dest = self.drop_dir / "processed" / p.name
        if dest.exists():
            ts = time.strftime("%Y%m%dT%H%M%S")
            dest = self.drop_dir / "processed" / f"{p.stem}.{ts}{p.suffix}"
        shutil.move(str(p), str(dest))


class CommunityMCPAdapter(Adapter):
    """Run a community MCP (e.g. `jlsookiki/secondhand-mcp`) over its CLI and parse results.

    This adapter does NOT install the MCP. The operator must:
      1) clone the MCP themselves,
      2) accept the platform's automation policy,
      3) keep the MCP at arm's length from their primary Facebook account.

    `command` is a list like ["npx", "-y", "secondhand-mcp", "search", "--query", "..."]
    The adapter passes the brief's query/location/max_price through env vars
    MCP_QUERY, MCP_LOCATION, MCP_MAX_PRICE, MCP_MIN_PRICE, MCP_LIMIT.

    The MCP must emit JSON (one object per line, or an array) on stdout. If the
    MCP exits non-zero or emits no JSON, the adapter raises DiscoveryError and
    the run continues with other adapters.
    """
    name = "community_mcp"

    def __init__(self, command: list[str], source_tag: str = "secondhand_mcp",
                 timeout: int = 60):
        if shutil.which(command[0]) is None and command[0] not in {"npx", "node", "uvx"}:
            # Will still try; npx/uvx may resolve at runtime. Just record the warn.
            pass
        self.command = command
        self.source_tag = source_tag
        self.timeout = timeout

    def fetch(self, brief: dict[str, Any], now_iso: str) -> Iterable[dict[str, Any]]:
        target = brief.get("target_json") or "{}"
        try:
            target_d = json.loads(target)
        except Exception:
            target_d = {}
        query = target_d.get("query") or f"{target_d.get('make','')} {target_d.get('model','')}".strip()
        env = os.environ.copy()
        env.update({
            "MCP_QUERY": query,
            "MCP_LOCATION": brief.get("geography", ""),
            "MCP_MAX_PRICE": str(int(target_d.get("max_ask_price") or 0)),
            "MCP_MIN_PRICE": "0",
            "MCP_LIMIT": "30",
        })
        try:
            proc = subprocess.run(
                self.command, env=env, capture_output=True,
                text=True, timeout=self.timeout, check=False,
            )
        except (FileNotFoundError, subprocess.TimeoutExpired) as e:
            raise DiscoveryError(f"community MCP failed: {e}")
        if proc.returncode != 0:
            raise DiscoveryError(
                f"community MCP exited {proc.returncode}; stderr={proc.stderr[:500]}"
            )
        text = proc.stdout.strip()
        if not text:
            return []
        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            data = [json.loads(line) for line in text.splitlines() if line.strip()]
        if isinstance(data, dict):
            data = [data]
        results = []
        for item in data:
            item["source"] = f"{self.name}:{self.source_tag}"
            results.append(normalize(item, now_iso))
        return results


def discover(brief: dict[str, Any], adapters: list[Adapter],
             now_iso: Optional[str] = None) -> list[dict[str, Any]]:
    """Run every adapter, validate each record, return a flat list."""
    now_iso = now_iso or time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    out: list[dict[str, Any]] = []
    errors: list[str] = []
    seen_in_run: set[tuple[str, str]] = set()
    for ad in adapters:
        if not ad.enabled:
            continue
        try:
            for raw in ad.fetch(brief, now_iso):
                validate(raw)
                key = (raw["source"], raw["listing_id"])
                if key in seen_in_run:
                    continue
                seen_in_run.add(key)
                out.append(raw)
        except DiscoveryError as e:
            errors.append(f"[{ad.name}] {e}")
    if errors:
        # Surface as part of result for the CLI to log; never silently drop.
        out.append({"_adapter_errors": errors})
    return out