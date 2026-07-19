"""Valuation adapters — CarsXE + CompsLocal + Heuristic, sharing types from
`valuation_types`. The shared `merge()` lives there to avoid circular imports.
"""

from __future__ import annotations

import abc
import json
import os
import statistics
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional

from .valuation_types import USER_AGENT, Valuation, merge

__all__ = ["Adapter", "Valuation", "merge",
           "CarsXEMarketValueAdapter", "HeuristicValuation",
           "CompsLocalAdapter"]


@dataclass
class Adapter(abc.ABC):
    name: str = ""
    enabled: bool = True

    @abc.abstractmethod
    def value(self, listing: dict[str, Any]) -> Optional[Valuation]:
        ...


def _http_get(url: str, headers: Optional[dict] = None, timeout: int = 20) -> tuple[int, str]:
    hdrs = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    if headers:
        hdrs.update(headers)
    req = urllib.request.Request(url, headers=hdrs)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode("utf-8", errors="replace")
    except Exception as e:
        return 0, f"{type(e).__name__}: {e}"


class CarsXEMarketValueAdapter(Adapter):
    """Live market value via CarsXE.

    Endpoint: GET https://api.carsxe.com/market-value
    Auth:     ?key=YOUR_KEY  (env var CARSXE_API_KEY)
    Pricing (carsxe.com/pricing, verified July 2026):
      Sandbox: $0/mo, 100 calls lifetime
      Starter: $40.83/mo, 2K calls/mo
      Pro:     $207.50/mo, 25K calls/mo
    """
    name = "carsxe"

    def __init__(self, api_key: Optional[str] = None, timeout: int = 20):
        self.api_key = api_key or os.environ.get("CARSXE_API_KEY")
        self.enabled = bool(self.api_key)
        self.timeout = timeout

    def value(self, listing: dict[str, Any]) -> Optional[Valuation]:
        if not self.api_key:
            return None
        params = {"key": self.api_key}
        if listing.get("vin"):
            params["vin"] = listing["vin"]
        else:
            for k in ("year", "make", "model", "trim", "mileage"):
                if listing.get(k) is not None:
                    params[k] = listing[k]
        url = "https://api.carsxe.com/market-value?" + urllib.parse.urlencode(params)
        status, body = _http_get(url, timeout=self.timeout)
        if status != 200:
            return None
        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            return None
        if not data.get("success"):
            return None
        # Two response shapes exist across API versions
        v = data.get("value") or {}
        low = v.get("min") or v.get("low") or data.get("range_low") or data.get("low")
        high = v.get("max") or v.get("high") or data.get("range_high") or data.get("high")
        mid = v.get("average") or data.get("average") or data.get("midpoint")
        if mid is None and low is not None and high is not None:
            mid = (low + high) / 2
        if mid is None:
            return None
        confidence = "high" if listing.get("vin") else "medium"
        return Valuation(
            source="carsxe",
            low=float(low) if low else float(mid) * 0.92,
            midpoint=float(mid),
            high=float(high) if high else float(mid) * 1.08,
            confidence=confidence,
            notes="CarsXE live market value API",
            raw={"carsxe_payload": data},
        )


class HeuristicValuation(Adapter):
    """Pure-math valuation. Used as the floor."""
    name = "heuristic"

    MSRP_TABLE = {
        ("Toyota", "Tacoma"): 36500,
        ("Toyota", "4Runner"): 41000,
        ("Toyota", "Camry"): 28000,
        ("Toyota", "Corolla"): 23000,
        ("Honda", "Civic"): 24000,
        ("Honda", "Accord"): 28500,
        ("Honda", "CR-V"): 32000,
        ("Mazda", "MX-5"): 30000,
        ("Mazda", "MX-5 Miata"): 30000,
        ("Mazda", "3"): 24000,
        ("Ford", "F-150"): 45000,
        ("Ford", "F150"): 45000,
        ("Subaru", "Outback"): 32000,
        ("Subaru", "WRX"): 34000,
    }

    def value(self, listing: dict[str, Any]) -> Optional[Valuation]:
        year = listing.get("year")
        make = (listing.get("make") or "").strip()
        model = (listing.get("model") or "").strip()
        if not (year and make and model):
            return None
        msrp = listing.get("msrp") or self.MSRP_TABLE.get((make, model))
        if not msrp:
            return None
        age = max(0, 2026 - int(year))
        if age <= 3:   retained = 0.78
        elif age <= 5: retained = 0.62
        elif age <= 8: retained = 0.48
        elif age <= 12: retained = 0.35
        elif age <= 18: retained = 0.22
        else:           retained = 0.13
        mid = msrp * retained
        mileage = listing.get("mileage")
        if mileage:
            expected = age * 12000
            delta = mileage - expected
            adj = max(-0.20, min(0.20, -delta * 0.00005))
            mid *= (1 + adj)
        spread = 0.08
        return Valuation(
            source="heuristic",
            low=round(mid * (1 - spread), 0),
            midpoint=round(mid, 0),
            high=round(mid * (1 + spread), 0),
            confidence="low",
            notes=f"age={age}, retained={retained:.2f}, msrp={msrp}",
            raw={"age": age, "msrp": msrp, "retained": retained},
        )


class CompsLocalAdapter(Adapter):
    """Median of recent comparable listings you maintain in a JSON file."""
    name = "comps_local"

    def __init__(self, comps_path: Path):
        self.comps_path = Path(comps_path)
        if not self.comps_path.exists():
            self.comps_path.parent.mkdir(parents=True, exist_ok=True)
            self.comps_path.write_text("[]", encoding="utf-8")

    def value(self, listing: dict[str, Any]) -> Optional[Valuation]:
        try:
            comps = json.loads(self.comps_path.read_text(encoding="utf-8"))
        except Exception:
            return None
        make = (listing.get("make") or "").lower()
        model = (listing.get("model") or "").lower()
        trim = (listing.get("trim") or "").lower()
        year = listing.get("year")
        mileage = listing.get("mileage")
        if not (make and model and year):
            return None
        weighted = []
        for c in comps:
            if (c.get("make", "").lower() != make or c.get("model", "").lower() != model):
                continue
            cy = c.get("year")
            if cy is None:
                continue
            w = 1.0
            dy = abs(int(cy) - int(year))
            if dy == 0: w *= 1.0
            elif dy == 1: w *= 0.6
            elif dy == 2: w *= 0.3
            else: continue
            if trim and (c.get("trim") or "").lower() == trim:
                w *= 1.25
            cm = c.get("mileage")
            if mileage and cm:
                if abs(cm - mileage) / max(mileage, 1) <= 0.15:
                    w *= 1.10
            p = c.get("ask_price")
            if p and p > 1000:
                weighted.append((float(p), w))
        if len(weighted) < 2:
            return None
        prices = [p for p, _ in weighted]
        median = statistics.median(prices)
        spread = 0.07
        confidence = "high" if len(weighted) >= 5 else "medium"
        return Valuation(
            source="comps_local",
            low=round(median * (1 - spread), 0),
            midpoint=round(median, 0),
            high=round(median * (1 + spread), 0),
            confidence=confidence,
            notes=f"median of {len(weighted)} weighted comps",
            raw={"weighted": weighted, "comps_count": len(weighted)},
        )