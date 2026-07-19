"""Shared types and the merge() function used by valuation adapters.

Split into its own module to avoid the circular import that would happen if
risk.py and discovery.py both imported USER_AGENT from valuation.py while
valuation.py imported from itself.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional

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


def merge(valuations: list[Valuation]) -> Optional[Valuation]:
    """Combine multiple Valuation objects into one blended estimate.

    Weighted midpoint by confidence (high=3, medium=2, low=1). Low/high come
    from the min/max across sources. Single-source results get confidence
    dropped one notch to express that we didn't cross-check.
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