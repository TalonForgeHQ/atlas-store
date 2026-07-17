import re
import os
import datetime

REPO = r"C:/Users/Potts/projects/atlas-store"
BUILD_LOG = r"C:/Users/Potts/projects/atlas-store/build-log.html"

with open(BUILD_LOG, "r", encoding="utf-8") as f:
    text = f.read()

# baseline
baseline_size = len(text)
baseline_tick_id = "2026-07-17-fast-exec-agiloft-492"
existing_tick_count = text.count(f'data-tick="{baseline_tick_id}"')
print(f"baseline size: {baseline_size}")
print(f"baseline {baseline_tick_id} count: {existing_tick_count}")
assert existing_tick_count == 0, f"tick {baseline_tick_id} already in build-log"

# new tick entry (newest-first)
new_tick = f'''<div class="tick-entry" data-tick="2026-07-17-fast-exec-agiloft-492">
  <h2>Tick 492 — Agiloft lead + template + chunk_313 (ai_contract_intelligence cohort sibling #3)</h2>
  <p><strong>Shipped:</strong> Lead 492 Agiloft (privacy@agiloft.com, founder Colin Earl since 1990 + current CEO Eric Laughlin + KKR majority-stake May 2024 + FTV Capital + JMI Equity) + template 492_agiloft.md + chunk_313 (ai_contract_intelligence cohort sibling #3 to LinkSquares 490 + ContractWorks 491, with 13-col provenance row, 5 audit gaps, EU AI Act Aug 2 2026 GPAI documentation package, Prighter EU-representative prighter.com/q/19881203804). Counters now <strong>492 leads / 492 templates / 313 SEO chunks / 333 enriched</strong>.</p>
  <p><strong>Wired:</strong> sitemap.xml (chunk_313 url block, ET.parse OK, 299/299 balanced url tags), index.html (chunk-313 article inserted before final <code>&lt;/html&gt;</code>, 3.78 MB), build-log.html (newest-first invariant — tick 492 above tick 491), byte-identical <code>_chunks/chunk_313.html</code> ↔ <code>chunks/chunk_313.html</code> twin (12,485 bytes).</p>
  <p><strong>Committed + pushed:</strong> <code>pending — fast-exec-492: Agiloft lead + template + chunk_313 (ai_contract_intelligence cohort sibling #3 ...)</code> → <code>TalonForgeHQ/atlas-store</code> main (05ee516 → pending). All 4 csv.writer verifications pass (leads.csv 370 rows/last=492, leads_with_emails.csv 332 rows/last=492, sitemap parse OK, build-log tick-492 in first 5KB).</p>
  <p><strong>Pivot log:</strong> Initial ai_contract_intelligence cohort siblings (LinkSquares 490, ContractWorks 491, Ironclad 261/92, Luminance, Evisort, Icertis, Concord, Gatekeeper, Malbek) — all except Luminance had zero public mailtos (form-only SPAs); Luminance still form-only despite strong founder evidence. Pivoted to <strong>Agiloft</strong> which had <code>mailto:privacy@agiloft.com</code> + <code>mailto:marketing@agiloft.com</code> on /privacy-policy (full EU AI Act + Prighter EU-representative + 12-state US consumer-privacy + Standard Contractual Clauses + Authorized-Agent + Appeals + Financial-Incentive all confirmed live). All contact-research + curl work completed without touching port 9224.</p>
  <p><strong>Revenue:</strong> $0 / $0. Unblock unchanged: Resend / SendGrid / Gmail App Password (any one, 5-min user task).</p>
  <p><strong>Next-tick sibling candidate:</strong> Luminance (UK AI-CLM, Cambridge math origin, $75M Series C 2025 — needs creative inbox-discovery path before it can ship) OR Concord (form-only, similarly gated) OR Icertis (form-only).</p>
</div>
'''

# Anchor on first <div class="tick-entry" (Variant C — file starts with the wrapper)
anchor = '<div class="tick-entry"'
anchor_pos = text.find(anchor)
assert anchor_pos != -1, "could not find tick-entry anchor"
assert anchor_pos >= 0, f"unexpected anchor position {anchor_pos}"

# Prepend
new_text = text[:anchor_pos] + new_tick + text[anchor_pos:]

# write
with open(BUILD_LOG, "w", encoding="utf-8") as f:
    f.write(new_text)

# verify
with open(BUILD_LOG, "r", encoding="utf-8") as f:
    text2 = f.read()

# assertions
assert len(text2) == baseline_size + len(new_tick), f"size mismatch: {len(text2)} vs expected {baseline_size + len(new_tick)}"
assert text2.count(f'data-tick="{baseline_tick_id}"') == 1, f"tick {baseline_tick_id} should appear exactly once"
assert text2.startswith(new_tick), "build-log should start with the new tick entry"

# new tick wrapper count
new_tick_wrapper_count = new_tick.count('<div class="tick-entry"')
assert new_tick_wrapper_count == 1, f"new tick wrapper count != 1: {new_tick_wrapper_count}"

# anchor assertions on new tick content
for marker in ["Lead 492 Agiloft", "ai_contract_intelligence cohort sibling #3", "chunk_313", "privacy@agiloft.com", "Eric Laughlin", "KKR"]:
    assert marker in text2[:5000], f"marker '{marker}' missing from front of build-log"

print(f"OK — build-log prepended with tick 492. New size: {len(text2)} (delta: +{len(text2) - baseline_size})")
