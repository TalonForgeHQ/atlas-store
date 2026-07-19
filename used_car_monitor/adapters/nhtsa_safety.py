"""NHTSA SafetyRatings adapter — completely free, no key, official.

Endpoints used:
- `GET /SafetyRatings/modelyear/{year}/make/{make}/model/{model}` — list VehicleIds
- `GET /SafetyRatings/VehicleId/{id}` — full safety data: overall rating,
  front/side crash ratings, rollover rating, ESC/FCW/LDW standard,
  complaints count, recalls count, investigations count.

Why this matters:
- A model with many complaints = buyers will pay less = monitor's "discount"
  on that model can be more aggressive.
- An active investigation (e.g. NHTSA opened an engineering analysis) is a
  real risk signal that affects resale value.
- Standard ESC/FCW/LDW increases valuation on cars without those features.
- OverallRating 4-5 is a public safety record buyers care about.

Limitations:
- Not all year/make/model combos are rated. We degrade to `info` flag.
- Lookup requires make/model match — if listing has wrong make, returns nothing.
"""

from __future__ import annotations

import re
import time
import urllib.parse
import urllib.request
from typing import Any, Iterable, Optional

from .risk import Adapter, RiskFlag
from .valuation_types import USER_AGENT


def _http_get(url: str, timeout: int = 15) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT,
                                               "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode("utf-8", errors="replace")
    except Exception as e:
        return 0, f"{type(e).__name__}: {e}"


class NHTSASafetyRatingsAdapter(Adapter):
    """Lookup crash ratings + complaint counts via NHTSA SafetyRatings API.

    Two-step lookup:
      1. /SafetyRatings/modelyear/{year}/make/{make}/model/{model} -> VehicleId
      2. /SafetyRatings/VehicleId/{id} -> full safety data

    Both endpoints are free, no API key, no rate limit (NHTSA publishes them
    for public use). Verified July 2026.
    """
    name = "nhtsa_safety"

    def screen(self, listing: dict[str, Any]) -> Iterable[RiskFlag]:
        year = listing.get("year")
        make = listing.get("make")
        model = listing.get("model")
        if not (year and make and model):
            return
        url = (f"https://api.nhtsa.gov/SafetyRatings/modelyear/{year}"
               f"/make/{urllib.parse.quote(str(make))}"
               f"/model/{urllib.parse.quote(str(model))}")
        status, body = _http_get(url)
        if status != 200:
            return
        import json as _json
        try:
            data = _json.loads(body)
        except ValueError:
            return
        results = data.get("Results") or []
        if not results:
            # No NHTSA rating for this model year — silent info.
            yield RiskFlag("info", "nhtsa_no_rating",
                           f"NHTSA has no crash rating for {year} {make} {model}",
                           {"year": year, "make": make, "model": model})
            return
        # Pick the first match — operator can refine later if 4WD/2WD matters.
        vid = results[0].get("VehicleId")
        if not vid:
            return
        detail_url = f"https://api.nhtsa.gov/SafetyRatings/VehicleId/{vid}"
        status2, body2 = _http_get(detail_url)
        if status2 != 200:
            return
        try:
            d = _json.loads(body2).get("Results", [{}])[0]
        except (ValueError, IndexError):
            return

        overall = d.get("OverallRating")
        rollover = d.get("RolloverRating")
        complaints = int(d.get("ComplaintsCount") or 0)
        recalls = int(d.get("RecallsCount") or 0)
        investigations = int(d.get("InvestigationCount") or 0)

        # Hard stop on open NHTSA investigation (rare, but big news)
        if investigations >= 1:
            yield RiskFlag(
                "warn", "nhtsa_investigation_open",
                f"NHTSA has {investigations} open investigation(s) on this model",
                {"investigations": investigations, "VehicleId": vid},
            )

        # Warn on heavy complaint load (model reliability signal)
        if complaints >= 500:
            yield RiskFlag(
                "warn", "nhtsa_complaint_heavy",
                f"{complaints} complaints filed with NHTSA for {year} {make} {model} — high",
                {"complaints": complaints},
            )
        elif complaints >= 100:
            yield RiskFlag(
                "info", "nhtsa_complaint_present",
                f"{complaints} complaints on {year} {make} {model}",
                {"complaints": complaints},
            )

        # Recall cross-check (in case the make/model/year recall API missed it)
        if recalls >= 3:
            yield RiskFlag(
                "info", "nhtsa_recall_count",
                f"{recalls} recall campaigns on {year} {make} {model}",
                {"recalls": recalls},
            )

        # Overall safety rating — informational
        try:
            overall_n = int(overall)
        except (TypeError, ValueError):
            overall_n = None
        try:
            rollover_n = int(rollover)
        except (TypeError, ValueError):
            rollover_n = None
        if overall_n and overall_n <= 2:
            yield RiskFlag(
                "warn", "nhtsa_low_safety_rating",
                f"NHTSA overall crash rating {overall_n}/5 for {year} {make} {model}",
                {"overall": overall_n, "rollover": rollover_n},
            )
        elif overall_n:
            yield RiskFlag(
                "info", "nhtsa_safety_rating",
                f"NHTSA overall crash rating {overall_n}/5 for {year} {make} {model}",
                {"overall": overall_n, "rollover": rollover_n},
            )

        # Standard safety equipment — ups valuation a notch if listed car lacks them
        esc = (d.get("NHTSAElectronicStabilityControl") or "").strip()
        if esc and esc != "Standard":
            yield RiskFlag(
                "info", "nhtsa_no_esc",
                f"ESC is '{esc}' on {year} {make} {model} — modern cars have Standard",
                {"esc": esc},
            )
        time.sleep(0.2)  # be polite to the free NHTSA host


class NHTSAVPICSpecsAdapter(Adapter):
    """Pull make/model/trim/drivetrain/transmission/fuel type from NHTSA vPIC.

    Free, no key. Different shape from SafetyRatings — vPIC gives specs.
    Used by both valuation (trim-level matching) and risk (detect
    listing-vs-VIN mismatches).

    Returns info-level flags only — no hard-stops. Hard-stops for
    make/model mismatch are handled by NHTSAVinDecodeAdapter in risk.py.
    """
    name = "nhtsa_vpic_specs"

    def screen(self, listing: dict[str, Any]) -> Iterable[RiskFlag]:
        year = listing.get("year")
        make = listing.get("make")
        model = listing.get("model")
        if not (year and make and model):
            return
        url = (f"https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformakeyear/make/"
               f"{urllib.parse.quote(str(make))}/modelyear/{year}"
               f"?format=json")
        status, body = _http_get(url)
        if status != 200:
            return
        import json as _json
        try:
            data = _json.loads(body)
        except ValueError:
            return
        results = data.get("Results") or []
        # Confirm the listed model exists for this make+year (to catch typos)
        models = {(r.get("Model_Name") or "").lower() for r in results}
        listed_model = (str(model) or "").lower()
        if listed_model and listed_model not in models:
            yield RiskFlag(
                "warn", "model_not_in_vpic",
                f"NHTSA vPIC has no {year} {make} {model} — possible listing typo",
                {"year": year, "make": make, "model": model,
                 "vpic_models_count": len(models)},
            )
        else:
            yield RiskFlag(
                "info", "model_confirmed_vpic",
                f"NHTSA vPIC confirms {year} {make} {model} exists",
                {"models_count": len(models)},
            )
        time.sleep(0.2)