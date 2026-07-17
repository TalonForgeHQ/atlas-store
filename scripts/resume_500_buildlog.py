"""Resume script: only do build-log prepend (surface 7). Surfaces 1-6 already on disk."""

from pathlib import Path
import sys

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
BUILD_LOG = REPO / "build-log.html"
TICK_ID = "2026-07-18-fast-exec-onetrust-500"
CHUNK_FILENAME = "chunk_321"

build_text = BUILD_LOG.read_text(encoding="utf-8")
first_tick_idx = build_text.find('<div class="tick-entry"')
assert first_tick_idx >= 0, "Could not find first <div class=\"tick-entry\" in build-log.html"

# Idempotency: assert the tick-id is NOT yet present (so the resume is a clean write)
tick_anchor = f'data-tick="{TICK_ID}"'
if build_text.count(tick_anchor) > 0:
    print(f"  [resume] build-log already has tick-id, skipping (idempotent no-op)")
    sys.exit(0)

NEW_TICK_ENTRY = (
    f'<div class="tick-entry" data-tick="{TICK_ID}">\n'
    f'<h2>2026-07-18 fast-exec-500: OneTrust (Lead 500) — ai_data_security cohort sibling #6</h2>\n'
    f'<p><strong>SHIPPED:</strong> Lead 500 OneTrust (onetrust.com, canonical AI data privacy + AI consent + AI DSPM + AI governance + AI ethics + AI risk + AI third-party risk + AI trust intelligence + 12000+ customers + 75% of Fortune 100 + 300+ of Global 2000 + Kabir Barday Founder + Blake Brannon Co-Founder CEO + Atlanta GA HQ + $5.1B peak valuation 2020 + dpo@onetrust.com DPO channel verified) → <code>cold_email/leads.csv</code> + <code>cold_email/leads_with_emails.csv</code> + <code>cold_email/templates/500_onetrust.md</code> (~320-word body, dpo@onetrust.com + sales@onetrust.com cited, $497 audit + Aug 2026 GPAI + EU AI Act + Schrems II SCC + 12-state AI disclosure hooks) + <code>chunks/{CHUNK_FILENAME}.html</code> (~9KB, 5 sections, dpo@onetrust.com + sales@onetrust.com citations) + <code>_chunks/{CHUNK_FILENAME}.html</code> twin + <code>sitemap.xml</code> URL block + <code>index.html</code> summary card + <code>build-log.html</code> prepended at first <code>&lt;div class="tick-entry"&gt;</code> offset.</p>\n'
    f'<p><strong>VERIFIED:</strong> 383 rows in leads.csv (last idx=500), 342 in leads_with_emails.csv (13 cols), template body ≥320 words, chunk section opens=closes balanced, sitemap parses with new block, index.html inlines chunk-{CHUNK_FILENAME} + ends with <code>&lt;/html&gt;</code>, build-log entry tagged with this tick-id at the top.</p>\n'
    f'<p><strong>COHORT:</strong> ai_data_security tier-1 (now 6/50): Wiz 494, Sentra 496, Cyera 497, Securiti 498, Varonis 499, OneTrust 500. The next natural siblings are: (a) <strong>TrustArc</strong> (#7) — Chicago HQ, canonical AI privacy + AI consent + AI DSPM + AI governance + AI risk + 2000+ customers, (b) <strong>Collibra</strong> (#8) — Brussels/NY HQ, AI data governance + AI data catalog + AI data quality + AI lineage + 1500+ customers, (c) <strong>Alation</strong> (#9) — canonical AI data catalog + AI data governance + AI metadata + 6000+ customers, (d) <strong>Informatica</strong> (#10) — canonical AI data integration + AI data quality + AI MDM + AI data governance + AI privacy, or pivot to <strong>ai_observability_monitoring</strong> cohort (Honeycomb 403, Arize 404, Fiddler 406, Datadog 408) to open a new vertical lane.</p>\n'
    f'</div>\n\n'
)
build_text = build_text[:first_tick_idx] + NEW_TICK_ENTRY + build_text[first_tick_idx:]
tick_count = build_text.count(tick_anchor)
assert tick_count == 1, f"build-log entry did not insert cleanly (count={tick_count})"
assert NEW_TICK_ENTRY.count('<div class="tick-entry"') == 1, "new_entry has wrong wrapper count"
BUILD_LOG.write_text(build_text, encoding="utf-8")
print(f"  [write] build-log.html prepended at first tick-entry offset (count={tick_count})")
