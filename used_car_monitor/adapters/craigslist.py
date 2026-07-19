"""Craigslist discovery adapter.

Craigslist explicitly permits non-commercial automated crawling and serves
plain HTML search results with no auth required. This bypasses Meta's ToS
wall entirely — the operator searches Craigslist, OfferUp, and other
non-Meta marketplaces where the same cars cross-post.

Endpoints supported:
- `fetch(brief)` runs a search against `geocoo` + `cat=cta` (cars+trucks)
  using the brief's target model + price range + ZIP from geography.
- Returns normalized listing dicts matching the canonical schema.

Heuristics applied:
- Title is parsed for year/make/model with a forgiving regex
- Price comes from `.price` div
- Location is parsed from `.location` div (e.g. "Austin TX - Next 1 Auto")
- Mileage is NOT on the search-result page (only on the detail page) — we
  leave it None and let the valuation adapter handle mileage-degraded math.
- VIN is not exposed on search pages either — left None.
- We extract the canonical detail URL so the operator can manually enrich
  with VIN/mileage before re-running the pipeline.
"""

from __future__ import annotations

import re
import time
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Iterable, Optional

from .discovery import Adapter, DiscoveryError, normalize, validate

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

# Craigslist subdomains by city — we only ship a handful. Extend as needed.
CITY_TO_SITE = {
    "austin": "austin", "dallas": "dallas", "houston": "houston",
    "san antonio": "sanantonio", "phoenix": "phoenix",
    "los angeles": "losangeles", "san diego": "sandiego",
    "san francisco": "sfbay", "seattle": "seattle",
    "denver": "denver", "chicago": "chicago", "new york": "newyork",
    "boston": "boston", "atlanta": "atlanta", "miami": "miami",
    "portland": "portland", "denver": "denver",
}


def _parse_geography(geography: str) -> tuple[Optional[str], Optional[int]]:
    """Best-effort: geography="Austin, TX, 100mi" -> (austin, 100)."""
    if not geography:
        return None, None
    parts = [p.strip() for p in geography.split(",")]
    city = parts[0].lower() if parts else None
    radius = None
    for p in parts[1:]:
        m = re.search(r"(\d+)\s*(?:mi|miles?)", p, re.I)
        if m:
            radius = int(m.group(1))
            break
    return city, radius


class CraigslistAdapter(Adapter):
    """Search Craigslist cars+trucks across a single sub-domain.

    Craigslist is the easiest legal-to-crawl P2P marketplace in 2026. The
    same Toyota Tacoma you see on Facebook Marketplace is almost always
    cross-posted here within 24 hours, often at a slightly lower ask because
    the seller avoids the FB fee and the urgency signaling.

    Limitations:
    - Craigslist serves HTML only; we parse the search results page. Listings
      on the page may not have mileage or VIN — those require detail-page
      fetches, which we leave to the operator's discretion.
    - The Craigslist "format=json" endpoint was deprecated in 2024. We use
      HTML parsing of the public search page.
    - Anti-bot: Craigslist has rate-limited aggressive scrapers. We add a
      2-second pause between fetches in `fetch()` and recommend calling the
      adapter at most once per brief per run.
    """
    name = "craigslist"

    def __init__(self, default_site: Optional[str] = None, pause: float = 2.0,
                 source_tag: str = "craigslist"):
        self.default_site = default_site
        self.pause = pause
        self.source_tag = source_tag

    def fetch(self, brief: dict[str, Any], now_iso: str) -> Iterable[dict[str, Any]]:
        city, radius = _parse_geography(brief.get("geography", ""))
        site = self.default_site or (CITY_TO_SITE.get(city or "") if city else None)
        if not site:
            raise DiscoveryError(
                f"no Craigslist subdomain mapped for city={city!r}; "
                f"add it to CITY_TO_SITE or pass default_site"
            )

        target = brief.get("target") or {}
        if isinstance(target, str):
            import json as _json
            try:
                target = _json.loads(target)
            except Exception:
                target = {}
        query_parts = [target.get("make") or "", target.get("model") or "",
                       target.get("trim") or ""]
        query = "+".join(p for p in query_parts if p).strip()
        if not query:
            query = "car"
        max_price = int(target.get("max_ask_price") or 0)
        params = {
            "query": query,
            "hasPic": "1",
            "sort": "date",
        }
        if max_price:
            params["max_price"] = str(int(max_price * 1.2))  # 20% headroom
        url = f"https://{site}.craigslist.org/search/cta?" + urllib.parse.urlencode(params)

        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT,
                                                   "Accept-Language": "en-US,en;q=0.9"})
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                body = r.read().decode("utf-8", errors="replace")
        except Exception as e:
            raise DiscoveryError(f"craigslist HTTP {type(e).__name__}: {e}")

        results: list[dict[str, Any]] = []
        # Each result block: <li class="cl-static-search-result">
        blocks = re.findall(
            r'<li class="cl-static-search-result[^"]*"[^>]*>(.*?)</li>\s*(?=<li|</ul>)',
            body, re.S,
        )
        for b in blocks:
            item = self._parse_block(b)
            if not item:
                continue
            item["source"] = f"{self.name}:{self.source_tag}"
            results.append(normalize(item, now_iso))

        # Be polite — Craigslist rate-limits aggressive scrapers.
        if self.pause:
            time.sleep(self.pause)
        return results

    @staticmethod
    def _parse_block(block: str) -> Optional[dict[str, Any]]:
        # URL
        url_match = re.search(r'<a href="(https?://[^"]+/view/d/[^"]+)"', block)
        if not url_match:
            return None
        url = url_match.group(1)
        # Listing ID from craigslist path
        m = re.search(r"/view/d/[^/]+/([A-Za-z0-9]+)", url)
        if not m:
            return None
        listing_id = "cl-" + m.group(1)
        # Title
        title_m = re.search(r'<div class="title">([^<]+)</div>', block)
        if not title_m:
            return None
        title = title_m.group(1).strip()
        # Price
        price_m = re.search(r'<div class="price">\$([\d,]+)</div>', block)
        if not price_m:
            return None
        try:
            ask_price = float(price_m.group(1).replace(",", ""))
        except ValueError:
            return None
        # Location: "Austin TX - Next 1 Auto"
        loc_m = re.search(r'<div class="location">\s*([^<\n]+?)\s*</div>', block, re.S)
        location = (loc_m.group(1).strip() if loc_m else None)
        # Parse year / make / model from title
        ymm = re.match(r"(\d{4})\s+(\S+)\s+(.+)", title)
        if ymm:
            year, make, rest = int(ymm.group(1)), ymm.group(2), ymm.group(3)
            model_full = rest.split()[0] if rest else ""
            trim = " ".join(rest.split()[1:]) if len(rest.split()) > 1 else None
        else:
            year = make = model_full = trim = None
        # Seller type heuristic
        seller_type = "dealer" if location and " - " in location else "private"
        return {
            "listing_id": listing_id,
            "url": url,
            "year": year,
            "make": make,
            "model": model_full,
            "trim": trim,
            "ask_price": ask_price,
            "location": location,
            "seller_type": seller_type,
            "title_claim": "unknown",
            "description": title,
            "mileage": None,
            "vin": None,
            "photos": [],
        }