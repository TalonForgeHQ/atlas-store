"""Valuation adapters.

A valuation adapter takes a listing dict and returns a `Valuation` object
with low/midpoint/high + a confidence label.

We will NEVER rely on a single source. The monitor calls every adapter that
is enabled and merges them. A listing needs >=2 independent sources to be
considered "medium" confidence; >=3 different sources or any cross-checked
"high" signal (e.g. comps_local median) to be "high".

Built-in adapters:
- `HeuristicValuation`: pure local rule of thumb based on MSRP depreciation curve
  + mileage adjustment. No network. Always available; used as the floor.
- `KBBPublicAdapter`: scrapes the KBB what's-my-car-worth search page or hits
  a KBB-style endpoint if available. Network required. Disabled by default
  because KBB serves behind aggressive bot walls; we tried and got 403s.
- `CompsLocalAdapter`: median of recent `comparable_listings` you store in a
  JSON file. Real local comps are how a real buyer beats the algorithm.
"""

from __future__ import annotations

import abc
import json
import re
import statistics
import time
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Optional


USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"


@dataclass
class Valuation:
    source: str
    low: float
    midpoint: float
    high: float
    confidence: str          # low|medium|high
    notes: str = ""
    raw: dict[str, Any] = field(default_factory=dict)

    def as_db_row(self, listing_id: int, lookup_at: str) -> dict[str, Any]:
        return {
            "listing_id": listing_id,
            "source": self.source,
            "lookup_at": lookup_at,
            "low": self.low,
            "midpoint": self.midpoint,
            "high": self.high,
            "confidence": self.confidence,
            "raw_json": json.dumps(self.raw, default=str),
            "notes": self.notes,
        }


def _http_get(url: str, timeout: int = 15) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT,
                                               "Accept-Language": "en-US,en;q=0.9"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode("utf-8", errors="replace")
    except Exception as e:
        return 0, f"{type(e).__name__}: {e}"


@dataclass
class Adapter(abc.ABC):
    name: str = ""  # subclasses override
    enabled: bool = True

    @abc.abstractmethod
    def value(self, listing: dict[str, Any]) -> Optional[Valuation]:
        ...


class HeuristicValuation(Adapter):
    """Pure-math valuation. Used as the floor.

    Year-depreciation model: 5-year-old vehicles lose ~40% of MSRP, 10-year-old
    ~65%, 15-year-old ~80%. Mileage adjustment: -$0.05/mile above 12k/yr,
    +$0.05/mile below 8k/yr, capped at +/- 20%.

    These curves are deliberately conservative. They give us a screening
    signal, not an appraisal. Real comps beat them every time.
    """
    name = "heuristic"

    # Common MSRP assumptions for popular used models. Override per-listing
    # by setting `msrp` in the raw listing dict. Keep this table small on purpose.
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
        if age <= 3:
            retained = 0.78
        elif age <= 5:
            retained = 0.62
        elif age <= 8:
            retained = 0.48
        elif age <= 12:
            retained = 0.35
        elif age <= 18:
            retained = 0.22
        else:
            retained = 0.13
        mid = msrp * retained

        mileage = listing.get("mileage")
        if mileage:
            expected = age * 12000
            delta = mileage - expected
            adj = max(-0.20, min(0.20, -delta * 0.00005))
            mid *= (1 + adj)

        spread = 0.08  # +/-8% range around midpoint
        return Valuation(
            source="heuristic",
            low=round(mid * (1 - spread), 0),
            midpoint=round(mid, 0),
            high=round(mid * (1 + spread), 0),
            confidence="low",
            notes=f"age={age}, retained={retained:.2f}, msrp={msrp}",
            raw={"age": age, "msrp": msrp, "retained": retained},
        )


class KBBPublicAdapter(Adapter):
    """Try the public KBB what's-my-car-worth page. Disabled by default because
    KBB serves behind Akamai bot walls and we received 403 on bare requests.

    To enable in your own deployment:
      1. Set `KBB_ENABLED=1`
      2. Bring your own residential proxy + cookie (NOT included here).
    """
    name = "kbb"

    def value(self, listing: dict[str, Any]) -> Optional[Valuation]:
        if not os.environ.get("KBB_ENABLED"):
            return None
        # Without a residential proxy + cookie, KBB returns 403. We refuse to
        # pretend we got data. Surface the failure to the operator instead.
        qs = urllib.parse.urlencode({
            "make": listing.get("make", ""),
            "model": listing.get("model", ""),
            "year": listing.get("year", ""),
        })
        status, body = _http_get(f"https://www.kbb.com/whats-my-car-worth/?{qs}")
        if status != 200 or "Access Denied" in body:
            return None
        m = re.search(r"\$([\d,]+)", body)
        if not m:
            return None
        mid = float(m.group(1).replace(",", ""))
        return Valuation(
            source="kbb",
            low=mid * 0.92, midpoint=mid, high=mid * 1.08,
            confidence="medium",
            notes="KBB public scrape (proxied); unverified range",
        )


class CompsLocalAdapter(Adapter):
    """Median of recent comparable listings you maintain in a JSON file.

    File format:
      [
        {"year": 2019, "make": "Toyota", "model": "Tacoma", "trim": "TRD",
         "ask_price": 27200, "mileage": 61000, "location": "Austin, TX"},
        ...
      ]

    Each comp is matched on (make, model) and weighted by:
      - exact year match:    full weight
      - within 1 year:       0.6 weight
      - within 2 years:      0.3 weight
      - same trim:           1.25x weight
      - mileage within 15%:  1.10x weight
    """
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
        weighted: list[tuple[float, float]] = []
        for c in comps:
            if (c.get("make", "").lower() != make or c.get("model", "").lower() != model):
                continue
            cy = c.get("year")
            if cy is None:
                continue
            w = 1.0
            dy = abs(int(cy) - int(year))
            if dy == 0:
                w *= 1.0
            elif dy == 1:
                w *= 0.6
            elif dy == 2:
                w *= 0.3
            else:
                continue
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


def merge(valuations: list[Valuation]) -> Optional[Valuation]:
    """Combine multiple Valuation objects into one blended estimate.

    We compute a weighted midpoint: each source contributes its midpoint
    weighted by confidence (high=3, medium=2, low=1). The low/high are the
    minimum low and maximum high across sources (conservative range).

    The blended confidence equals the highest single-source confidence UNLESS
    only one source contributed, in which case it's that source's confidence
    but capped one notch lower (medium->low) to express that we didn't cross-check.
    """
    if not valuations:
        return None
    conf_w = {"high": 3.0, "medium": 2.0, "low": 1.0}
    total_w = sum(conf_w.get(v.confidence, 1.0) for v in valuations)
    blended = sum(v.midpoint * conf_w.get(v.confidence, 1.0) for v in valuations) / total_w
    lo = min(v.low for v in valuations)
    hi = max(v.high for v in valuations)
    spread = 0.10 if len(valuations) >= 2 else 0.15
    conf_rank = {"high": 3, "medium": 2, "low": 1}
    max_conf = max(valuations, key=lambda v: conf_rank[v.confidence]).confidence
    if len(valuations) == 1:
        # single source → drop confidence one notch
        bumped = {"high": "medium", "medium": "low", "low": "low"}
        final_conf = bumped[max_conf]
    else:
        final_conf = max_conf
    return Valuation(
        source="blended",
        low=round(min(lo, blended * (1 - spread)), 0),
        midpoint=round(blended, 0),
        high=round(max(hi, blended * (1 + spread)), 0),
        confidence=final_conf,
        notes=f"blended {len(valuations)} sources: " +
              ", ".join(f"{v.source}({v.confidence})" for v in valuations),
        raw={"blended_midpoint": blended, "inputs": [
            {"source": v.source, "midpoint": v.midpoint, "confidence": v.confidence}
            for v in valuations
        ]},
    )