"""Risk adapters.

Each adapter returns 0+ `RiskFlag` records per listing. Severity is one of
`info`, `warn`, or `hard_stop`. A hard_stop means the listing MUST NOT be
contacted until a human overrides.

Built-in adapters:
- `NHTSARecallAdapter`: live NHTSA recalls API (no key required). Hits
  https://api.nhtsa.gov/recalls/recallsByVehicle. Verifies the lookup works.
- `NHTSAVinDecodeAdapter`: live NHTSA vPIC VIN decoder. Catches obvious
  VIN format errors and confirm make/model.
- `ScarceSignalAdapter`: pure local heuristics — price too good to be true,
  zero mileage on an old vehicle, copy-paste description, etc.
"""

from __future__ import annotations

import abc
import json
import re
import time
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from typing import Any, Iterable, Optional

from .valuation import USER_AGENT

VIN_RE = re.compile(r"^[A-HJ-NPR-Z0-9]{11,17}$")  # exclude I, O, Q


@dataclass
class RiskFlag:
    severity: str   # info|warn|hard_stop
    code: str
    message: str
    evidence: dict[str, Any] = field(default_factory=dict)


@dataclass
class Adapter(abc.ABC):
    name: str = ""  # subclasses override
    enabled: bool = True

    @abc.abstractmethod
    def screen(self, listing: dict[str, Any]) -> Iterable[RiskFlag]:
        ...


def _http_get(url: str, timeout: int = 15) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode("utf-8", errors="replace")
    except Exception as e:
        return 0, f"{type(e).__name__}: {e}"


class NHTSAVinDecodeAdapter(Adapter):
    """Verify the VIN against NHTSA's vPIC decoder and cross-check year/make/model."""
    name = "nhtsa_vin"

    def screen(self, listing: dict[str, Any]) -> Iterable[RiskFlag]:
        vin = (listing.get("vin") or "").strip().upper()
        if not vin:
            return
        if not VIN_RE.match(vin):
            yield RiskFlag(
                "hard_stop", "vin_format_invalid",
                f"VIN {vin!r} does not match the 11-17 char no-I/O/Q format",
                {"vin": vin},
            )
            return
        status, body = _http_get(
            f"https://vpic.nhtsa.dot.gov/api/vehicles/decodevin/{vin}?format=json"
        )
        if status != 200:
            yield RiskFlag("warn", "vin_decode_unavailable",
                           f"NHTSA decode HTTP {status}", {"body_snippet": body[:200]})
            return
        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            return
        results = {r["Variable"]: r["Value"] for r in data.get("Results", [])}
        errors = [k for k, v in results.items() if k == "Error Code" and v not in ("0", "")]
        if results.get("Error Code") not in (None, "0"):
            yield RiskFlag(
                "hard_stop", "vin_decode_failed",
                f"NHTSA reports error code {results.get('Error Code')} for VIN {vin}",
                {"error_text": results.get("Error Text")},
            )
            return
        # Cross-check
        declared_year = str(listing.get("year") or "")
        declared_make = (listing.get("make") or "").upper()
        nhtsa_year = (results.get("Model Year") or "").strip()
        nhtsa_make = (results.get("Make") or "").strip().upper()
        if declared_year and nhtsa_year and declared_year != nhtsa_year:
            yield RiskFlag(
                "hard_stop", "vin_year_mismatch",
                f"Listing year={declared_year} but VIN decodes year={nhtsa_year}",
                {"listing_year": declared_year, "nhtsa_year": nhtsa_year},
            )
        if declared_make and nhtsa_make and declared_make != nhtsa_make:
            yield RiskFlag(
                "hard_stop", "vin_make_mismatch",
                f"Listing make={declared_make} but VIN decodes make={nhtsa_make}",
                {"listing_make": declared_make, "nhtsa_make": nhtsa_make},
            )
        yield RiskFlag("info", "vin_decode_ok",
                       f"VIN {vin} decoded year={nhtsa_year} make={nhtsa_make}",
                       {"results_subset": {k: results.get(k) for k in (
                           "Make", "Model", "Model Year", "Trim", "Drive Type",
                           "Transmission Style", "Fuel Type - Primary")},
                       })


class NHTSARecallAdapter(Adapter):
    """Look up open recalls on a listing's make/model/year."""
    name = "nhtsa_recall"

    def screen(self, listing: dict[str, Any]) -> Iterable[RiskFlag]:
        year = listing.get("year")
        make = listing.get("make")
        model = listing.get("model")
        if not (year and make and model):
            return
        qs = urllib.parse.urlencode({
            "make": make, "model": model, "modelYear": year,
        })
        status, body = _http_get(
            f"https://api.nhtsa.gov/recalls/recallsByVehicle?{qs}"
        )
        if status != 200:
            yield RiskFlag("warn", "recall_lookup_unavailable",
                           f"NHTSA recalls HTTP {status}", {"body_snippet": body[:200]})
            return
        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            return
        results = data.get("results") or []
        if not results:
            yield RiskFlag("info", "no_open_recalls",
                           f"No recalls for {year} {make} {model}")
            return
        # Open recalls exist. Not a dealbreaker, but warn.
        yield RiskFlag(
            "warn", "open_recalls_present",
            f"{len(results)} open recall(s) on {year} {make} {model}. " +
            "Verify each is remedied before purchase.",
            {"count": len(results),
             "first_three": [{"campaign": r.get("NHTSACampaignNumber"),
                              "component": r.get("Component"),
                              "summary": r.get("Summary")} for r in results[:3]]},
        )


class ScarcitySignalsAdapter(Adapter):
    """Pure-local heuristics for fraud and bad data."""
    name = "scarcity"

    SUSPICIOUS_KEYWORDS = (
        "paypal only", "western union", "gift card", "crypto only",
        "shipping only", "ebay gift card", "zelle only", "wire transfer",
        "outside of ebay", "outside of marketplace", "verification code",
    )

    def screen(self, listing: dict[str, Any]) -> Iterable[RiskFlag]:
        desc = (listing.get("description") or "").lower()
        ask = listing.get("ask_price") or 0
        mileage = listing.get("mileage")
        year = listing.get("year") or 0

        for kw in self.SUSPICIOUS_KEYWORDS:
            if kw in desc:
                yield RiskFlag(
                    "hard_stop", "payment_offplatform",
                    f"Suspicious keyword {kw!r} in description",
                    {"keyword": kw},
                )

        if mileage is not None and mileage < 100 and year and (2026 - int(year)) >= 2:
            yield RiskFlag(
                "hard_stop", "impossible_mileage",
                f"Year {year} listing claims {mileage} miles — likely a placeholder",
                {"year": year, "mileage": mileage},
            )

        if ask and ask < 500:
            yield RiskFlag(
                "warn", "price_suspiciously_low",
                f"Ask price ${ask:,.0f} is below the floor for any drivable vehicle",
                {"ask_price": ask},
            )

        # Empty description with seller asking real money
        if ask and ask > 5000 and len(desc.strip()) < 30:
            yield RiskFlag(
                "warn", "thin_description",
                f"Listing asks ${ask:,.0f} with <30 chars of description",
                {"desc_len": len(desc.strip())},
            )

        # Title claim is salvage/rebuilt — flag but not auto-stop (depends on brief)
        title = (listing.get("title_claim") or "").lower()
        if title in ("salvage", "rebuilt", "flood"):
            yield RiskFlag(
                "warn", "branded_title",
                f"Listing declares {title} title",
                {"title_claim": title},
            )


def screen_all(listing: dict[str, Any], adapters: list[Adapter]) -> list[RiskFlag]:
    flags: list[RiskFlag] = []
    for ad in adapters:
        if not ad.enabled:
            continue
        try:
            flags.extend(ad.screen(listing))
        except Exception as e:
            flags.append(RiskFlag(
                "warn", f"{ad.name}_adapter_error",
                f"Adapter {ad.name} raised {type(e).__name__}: {e}",
            ))
    return flags


def has_hard_stop(flags: list[RiskFlag]) -> bool:
    return any(f.severity == "hard_stop" for f in flags)


def risk_score(flags: list[RiskFlag]) -> int:
    """0-100. Lower = safer. Hard stop doesn't reduce score - it sets it to 100."""
    if has_hard_stop(flags):
        return 100
    return min(100, sum({"info": 2, "warn": 8}[f.severity] for f in flags))