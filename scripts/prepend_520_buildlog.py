"""Prepend build-log entry for the Podia 520 lead-append tick.

Pattern: Variant C reverse-chronological prepend. Anchor on
first `<div class="tick-entry"` (top-of-file), concat new_entry
+ existing content. Idempotency guard via count() == 0 before
write. Also handles sitemap index.html free-id check (pitfall #72).
"""
import re
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
BUILD_LOG = REPO / "build-log.html"
TICK_ID = "2026-07-18-fast-exec-podia-520"

# Variant C entry: <div class="tick-entry" data-tick="..."> wrapper
# Build the entry as the canonical reverse-chronological prepend shape.
NEW_ENTRY = f'''<div class="tick-entry" data-tick="{TICK_ID}">
  <h2>Fast exec: add Podia 520 lead and audit template</h2>
  <p><strong>Tick ID:</strong> <code>{TICK_ID}</code></p>
  <p><strong>Artifact:</strong> Lead 520 (Podia, hello@podia.com, Spencer Fry founder + CEO, NYC HQ, 150K+ creators, ai_creator_economy) appended to <code>cold_email/leads.csv</code>; tier-1 outreach template <code>cold_email/templates/520_podia.md</code> written with 3 variants (EU AI Act Art. 12 + DSA Art. 27 + cross-tenant ISO 27701) + CAN-SPAM + GDPR Art. 6(1)(f) compliant footer.</p>
  <p><strong>Verification:</strong> podia.com returned HTTP 200 (69,633 bytes - server-rendered); podia.com/about returned HTTP 200 with canonical "courses + community + coaching + downloads + webinars" framing; podia.com/privacy returned HTTP 200 (234,940 bytes - fully server-rendered) exposing mailto:hello@podia.com as the canonical support + strategic-inbound channel. Parse-back on leads.csv confirms 398 data rows + max index 520 + zero duplicate indices.</p>
  <p><strong>Cohort context:</strong> Tier-1 ai_creator_economy sibling #9 after Patreon 512 (Jack Conte + Sam Yam co-founders, legal@patreon.com), Gumroad 513 (Sahil Lavingia founder, support@gumroad.com), Kit 514 (Nathan Barry founder, help@kit.com + legal@kit.com), Substack 515 (Chris + Hamish McKenzie co-founders, privacy@substackinc.com), Kajabi 516 (Kenny Rueter founder, privacy@kajabi.com), Thinkific 517 (Greg Smith CEO + co-founder, support@thinkific.com), Memberstack 518 (Tyler Bell + Duncan Hamra co-founders, YC-backed SOC 2 + 50K+ Webflow sites, support@memberstack.com + partnerships@memberstack.com), Mighty Networks 519 (Gina Bianchini CEO + co-founder + Tim Herby CTO + co-founder, dpo@mightynetworks.com). Podia completes the canonical 9-vendor ai_creator_economy cohort that maps to EU AI Act Aug 2 2026 GPAI documentation target + DSA Art. 27 + the 12-state AI-disclosure laws + Schrems II SCC + ISO 27701.</p>
  <p><strong>Audit wedge:</strong> creator request -> Podia tenant -> retrieved course/community context -> prompt/model/version -> AI recommendation (course + coaching + product-bundling + membership-tier + checkout + billing) -> human approval -> Podia object mutation + Stripe side effect, with prompt-injection, cross-tenant isolation, change control, rollback, deletion, WORM evidence, SOC 2 CC6.1/CC7.2, EU AI Act Articles 12/14/50, GDPR Article 28, ISO 42001, NIST AI RMF, DSA Art. 27, and OWASP LLM Top 10 coverage. 5 audit gaps documented in the leads.csv tier_reason column.</p>
  <p><strong>Next:</strong> ship Mighty Networks 519 chunk (the prior-tick cohort sibling that has a verified inbox but no public chunk yet) as a 5-surface chunk-ship in the next tick. Optionally: continue ai_creator_economy cohort with sibling #10 (e.g. Skool — but Skool is SPA-walled on /about and /privacy, so a verified inbox probe is the gating step before lead 521).</p>
</div>

'''

# Idempotency guard — entry must not already be present
bl = BUILD_LOG.read_text(encoding="utf-8")
tick_id_count_before = bl.count(f'data-tick="{TICK_ID}"')
assert tick_id_count_before == 0, f"{TICK_ID} already in build-log"

# Extract tick-entry count to local first (pitfall #70: avoid backslash inside f-string {})
tick_entry_count_before = bl.count('<div class="tick-entry"')
assert tick_entry_count_before >= 300, f"build-log variant C sanity: got {tick_entry_count_before} tick-entry blocks"

# Variant C prepend: anchor on FIRST <div class="tick-entry" at top of file
anchor = '<div class="tick-entry"'
idx = bl.find(anchor)
assert idx >= 0, "no Variant C anchor found in build-log"

new_bl = bl[:idx] + NEW_ENTRY + bl[idx:]

# Wrapper count check on new entry
wrapper_count_new = NEW_ENTRY.count('<div class="tick-entry"')
assert wrapper_count_new == 1, f"new entry has {wrapper_count_new} wrappers, expected 1"

# Final assert: TICK_ID appears exactly once in new build-log
final_tick_count = new_bl.count(f'data-tick="{TICK_ID}"')
assert final_tick_count == 1, f"TICK_ID count = {final_tick_count}, expected 1"

# Tick-entry count should have grown by exactly 1
tick_entry_count_after = new_bl.count('<div class="tick-entry"')
assert tick_entry_count_after == tick_entry_count_before + 1, f"tick-entry count grew by {tick_entry_count_after - tick_entry_count_before}, expected +1"

BUILD_LOG.write_text(new_bl, encoding="utf-8")
print(f"OK prepend_520_podia: build-log now {len(new_bl)} chars (was {len(bl)}), tick-entry count {tick_entry_count_before} -> {tick_entry_count_after}, TICK_ID count {final_tick_count}")
