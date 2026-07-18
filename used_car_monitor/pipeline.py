"""Orchestrator: drive the 7-stage pipeline for one or more briefs.

`run_once(briefs, adapters)` returns a run report dict.

Each stage:
1. Discover (file feed + community MCP if enabled)
2. Normalize + dedupe (SQLite)
3. Value (heuristic + comps_local by default; pluggable KBB)
4. Risk screen (NHTSA VIN/recall + scarcity heuristics)
5. Compute all-in cost & max offer
6. Rank candidates; create alerts (idempotent)
7. Send to notifier(s) - never auto-message sellers

Only read-only stages are autonomous. Outbound contact, offers, and
purchases are ALWAYS human-gated.
"""

from __future__ import annotations

import json
import sqlite3
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Optional

from . import db
from .adapters import discovery as discovery_mod
from .adapters import notifier as notifier_mod
from .adapters import risk as risk_mod
from .adapters import valuation as valuation_mod


@dataclass
class PipelineAdapters:
    discoverers: list[discovery_mod.Adapter] = field(default_factory=list)
    valuators: list[valuation_mod.Adapter] = field(default_factory=list)
    risk_screeners: list[risk_mod.Adapter] = field(default_factory=list)
    notifiers: list[notifier_mod.Adapter] = field(default_factory=list)


def _now_iso() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def load_briefs(conn: sqlite3.Connection) -> list[dict[str, Any]]:
    rows = conn.execute("SELECT * FROM briefs WHERE active = 1 ORDER BY id").fetchall()
    out = []
    for r in rows:
        d = dict(r)
        d["target"] = json.loads(d.pop("target_json"))
        d["sources"] = json.loads(d.pop("sources_json"))
        out.append(d)
    return out


def all_in_cost(ask_price: float, brief_target: dict[str, Any]) -> dict[str, float]:
    """Estimate total landed cost so the user never sees a bare ask price."""
    tax_pct = brief_target.get("tax_pct", 0.0625)
    fees = brief_target.get("fees_flat", 350)
    transport = brief_target.get("transport", 0)
    inspection = brief_target.get("inspection", 200)
    immediate_repairs = brief_target.get("immediate_repairs", 0)
    contingency = brief_target.get("contingency_pct", 0.05)
    tax = ask_price * tax_pct
    base = ask_price + tax + fees + transport + inspection + immediate_repairs
    total = base * (1 + contingency)
    return {
        "ask_price": round(ask_price, 0),
        "tax": round(tax, 0),
        "fees": round(fees, 0),
        "transport": round(transport, 0),
        "inspection": round(inspection, 0),
        "immediate_repairs": round(immediate_repairs, 0),
        "contingency_pct": contingency,
        "all_in": round(total, 0),
    }


def max_offer(conservative_value: float, all_in: dict[str, float],
              margin_pct: float = 0.08) -> float:
    """Conservative market value minus non-price costs minus margin."""
    non_price = all_in["all_in"] - all_in["ask_price"]
    return round(conservative_value - non_price - conservative_value * margin_pct, 0)


def recommendation(listing_row: sqlite3.Row,
                   valuation: Optional[valuation_mod.Valuation],
                   cost: dict[str, float],
                   flags: list[risk_mod.RiskFlag],
                   brief: dict[str, Any]) -> dict[str, Any]:
    """Compose a recommendation payload that the notifier renders."""
    ask = listing_row["ask_price"] or 0
    mid = valuation.midpoint if valuation else None
    disc = ((mid - ask) / mid) if (mid and ask and mid > 0) else 0.0
    under_threshold = disc >= brief["min_discount"]

    if risk_mod.has_hard_stop(flags):
        return {"action": "ignore", "why": "hard_stop risk gate"}
    if not valuation or mid is None:
        return {"action": "ignore", "why": "no valuation; need comps"}
    if not under_threshold:
        return {"action": "ignore",
                "why": f"discount {disc:.1%} below {brief['min_discount']:.0%} threshold"}
    if cost["all_in"] > brief["max_all_in"]:
        return {"action": "ignore",
                "why": f"all-in ${cost['all_in']:,.0f} > budget ${brief['max_all_in']:,.0f}"}

    max_off = max_offer(valuation.low, cost)
    return {"action": "review",
            "why": "passes gates; needs human approval to contact",
            "discount_pct": round(disc * 100, 1),
            "max_offer": max_off,
            "all_in": cost["all_in"],
            "valuation_mid": mid,
            "valuation_low": valuation.low,
            "valuation_high": valuation.high,
            "valuation_confidence": valuation.confidence,
            "risk_score": risk_mod.risk_score(flags)}


def evaluate_listing(conn: sqlite3.Connection,
                     listing_id: int,
                     brief: dict[str, Any],
                     valuators: list[valuation_mod.Adapter],
                     risk_screeners: list[risk_mod.Adapter]) -> dict[str, Any]:
    """Value + risk + recommend one listing. Persists to DB. Returns the report dict."""
    row = conn.execute("SELECT * FROM listings WHERE id = ?", (listing_id,)).fetchone()
    if row is None:
        return {"error": f"listing_id={listing_id} not found"}

    listing_dict = dict(row)
    listing_dict["ask_price"] = row["ask_price"]

    now_iso = _now_iso()
    valuations = []
    for ad in valuators:
        if not ad.enabled:
            continue
        try:
            v = ad.value(listing_dict)
        except Exception as e:
            db.audit(conn, "valuation.error", listing_id, {"adapter": ad.name, "err": str(e)})
            continue
        if v is None:
            continue
        valuations.append(v)
        # Persist each source separately (no dedupe across runs).
        try:
            conn.execute(
                """INSERT OR IGNORE INTO valuations
                   (listing_id, source, lookup_at, low, midpoint, high, confidence, raw_json, notes)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (listing_id, v.source, now_iso, v.low, v.midpoint, v.high,
                 v.confidence, json.dumps(v.raw, default=str), v.notes),
            )
        except sqlite3.IntegrityError:
            pass

    blended = valuation_mod.merge(valuations) if valuations else None
    if blended is not None:
        try:
            conn.execute(
                """INSERT OR IGNORE INTO valuations
                   (listing_id, source, lookup_at, low, midpoint, high, confidence, raw_json, notes)
                   VALUES (?, 'blended', ?, ?, ?, ?, ?, ?, ?)""",
                (listing_id, now_iso, blended.low, blended.midpoint, blended.high,
                 blended.confidence, json.dumps(blended.raw, default=str), blended.notes),
            )
        except sqlite3.IntegrityError:
            pass

    flags = risk_mod.screen_all(listing_dict, risk_screeners)
    for f in flags:
        conn.execute(
            """INSERT INTO risk_flags(listing_id, severity, code, message, evidence_json)
               VALUES (?, ?, ?, ?, ?)""",
            (listing_id, f.severity, f.code, f.message, json.dumps(f.evidence, default=str)),
        )

    target = brief.get("target", {})
    cost = all_in_cost(row["ask_price"] or 0, target)
    rec = recommendation(row, blended, cost, flags, brief)

    # Status update
    new_status = "screened"
    if risk_mod.has_hard_stop(flags):
        new_status = "rejected"
    elif rec["action"] == "review":
        new_status = "flagged"
    conn.execute("UPDATE listings SET status = ? WHERE id = ?", (new_status, listing_id))
    db.audit(conn, "evaluation.done", listing_id, {
        "valuation_mid": blended.midpoint if blended else None,
        "valuation_confidence": blended.confidence if blended else None,
        "risk_score": risk_mod.risk_score(flags),
        "recommendation": rec.get("action"),
    })

    return {
        "listing_id": listing_id,
        "valuations": [asdict(v) for v in valuations],
        "blended": asdict(blended) if blended else None,
        "flags": [asdict(f) for f in flags],
        "cost": cost,
        "recommendation": rec,
        "status": new_status,
    }


def alert_payload(conn: sqlite3.Connection,
                  listing_id: int,
                  brief: dict[str, Any],
                  report: dict[str, Any]) -> Optional[dict[str, Any]]:
    """Compose the message we send to notifiers. None means no alert needed."""
    rec = report.get("recommendation") or {}
    if rec.get("action") != "review":
        return None
    row = conn.execute("SELECT * FROM listings WHERE id = ?", (listing_id,)).fetchone()
    if row is None:
        return None
    title = f"{row['year'] or ''} {row['make'] or ''} {row['model'] or ''} {row['trim'] or ''}".strip()
    payload = {
        "kind": "new_flag",
        "listing_id": listing_id,
        "brief_id": brief["id"],
        "vehicle": {"title": title,
                    "year": row["year"], "make": row["make"], "model": row["model"],
                    "trim": row["trim"], "vin": row["vin"],
                    "mileage": row["mileage"], "location": row["location"]},
        "ask_price": row["ask_price"],
        "url": row["url"],
        "valuation_mid": rec.get("valuation_mid"),
        "valuation_low": rec.get("valuation_low"),
        "valuation_high": rec.get("valuation_high"),
        "valuation_confidence": rec.get("valuation_confidence"),
        "discount_pct": rec.get("discount_pct"),
        "max_offer": rec.get("max_offer"),
        "all_in_cost": rec.get("all_in"),
        "risk_score": rec.get("risk_score"),
        "risk_flags": [{"severity": f["severity"], "code": f["code"],
                        "message": f["message"]}
                       for f in report.get("flags", [])],
        "recommendation": f"Review: {rec.get('why', '')}. "
                          f"Approve with:  used-car-monitor approve {listing_id}",
    }
    # Dedupe key: one alert per (listing, brief, kind) ever, unless the price
    # changes by >=5% OR valuation confidence changes OR a new risk flag.
    price_bucket = int(round((row["ask_price"] or 0) / 500))
    conf = rec.get("valuation_confidence", "low")
    flagset = ",".join(sorted(f["code"] for f in report.get("flags", [])))
    dedupe = f"listing={listing_id}|brief={brief['id']}|price={price_bucket}|conf={conf}|flags={flagset}"
    payload["dedupe_key"] = dedupe
    return payload


def run_once(conn: sqlite3.Connection,
             pipeline: PipelineAdapters,
             only_brief_id: Optional[int] = None) -> dict[str, Any]:
    """Drive the entire pipeline once. Returns a structured report."""
    started = _now_iso()
    briefs = load_briefs(conn)
    if only_brief_id is not None:
        briefs = [b for b in briefs if b["id"] == only_brief_id]

    report = {"started_at": started, "ended_at": None,
              "briefs_run": [b["id"] for b in briefs],
              "listings": {"discovered": 0, "ingested_new": 0, "ingested_updated": 0,
                           "flagged": 0, "rejected": 0, "alerts_sent": 0,
                           "alerts_suppressed": 0},
              "errors": [], "brief_reports": []}

    for brief in briefs:
        target = brief["target"]
        # 1. Discover
        try:
            raw = discovery_mod.discover(brief, pipeline.discoverers)
        except Exception as e:
            report["errors"].append({"brief": brief["id"], "stage": "discover", "err": str(e)})
            raw = []
        # Pull out adapter error notifications
        adapter_errs = [r for r in raw if "_adapter_errors" in r]
        if adapter_errs:
            report["errors"].extend([{"brief": brief["id"], "stage": "discover", "err": e}
                                     for e in adapter_errs[0]["_adapter_errors"]])
            raw = [r for r in raw if "_adapter_errors" not in r]
        report["listings"]["discovered"] += len(raw)

        # 2-3. Ingest + assign brief
        ingested = []
        for rec in raw:
            lid, inserted = db.upsert_listing(conn, rec)
            # Assign to this brief if no brief assigned yet
            cur = conn.execute("SELECT brief_id FROM listings WHERE id = ?", (lid,)).fetchone()
            if cur and cur["brief_id"] is None:
                conn.execute("UPDATE listings SET brief_id = ? WHERE id = ?",
                             (brief["id"], lid))
            if inserted:
                report["listings"]["ingested_new"] += 1
            else:
                report["listings"]["ingested_updated"] += 1
            ingested.append(lid)

        # 4. Evaluate each ingested listing
        brief_report = {"brief_id": brief["id"], "name": brief["name"],
                        "evaluated": [], "alerts": []}
        for lid in ingested:
            # Skip listings not assigned to this brief
            owner = conn.execute("SELECT brief_id FROM listings WHERE id = ?",
                                 (lid,)).fetchone()
            if owner and owner["brief_id"] != brief["id"]:
                continue
            eval_report = evaluate_listing(conn, lid, brief,
                                           pipeline.valuators,
                                           pipeline.risk_screeners)
            brief_report["evaluated"].append({
                "listing_id": lid,
                "status": eval_report["status"],
                "recommendation": eval_report["recommendation"].get("action"),
            })
            if eval_report["status"] == "rejected":
                report["listings"]["rejected"] += 1
            if eval_report["status"] == "flagged":
                report["listings"]["flagged"] += 1

            # 5-6. Compose alert + dedupe + send
            payload = alert_payload(conn, lid, brief, eval_report)
            if payload is None:
                continue
            try:
                conn.execute(
                    """INSERT INTO alerts(listing_id, brief_id, kind, dedupe_key, payload_json, delivered)
                       VALUES (?, ?, ?, ?, ?, 0)""",
                    (lid, brief["id"], payload["kind"], payload["dedupe_key"],
                     json.dumps(payload, default=str)),
                )
            except sqlite3.IntegrityError:
                report["listings"]["alerts_suppressed"] += 1
                continue
            delivered_any = False
            for n in pipeline.notifiers:
                if not n.enabled:
                    continue
                ok = n.send(payload)
                delivered_any = delivered_any or ok
            if delivered_any:
                conn.execute(
                    "UPDATE alerts SET delivered = 1 WHERE dedupe_key = ?",
                    (payload["dedupe_key"],),
                )
                report["listings"]["alerts_sent"] += 1
                brief_report["alerts"].append({"listing_id": lid,
                                               "dedupe_key": payload["dedupe_key"]})

        report["brief_reports"].append(brief_report)

    report["ended_at"] = _now_iso()
    return report