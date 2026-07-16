#!/usr/bin/env python3
"""Prepend build-log entry for Tick 07:55Z (chunk_155 Tonic.ai SEO landing).
Use str.find + concat to splice BEFORE the existing first TICK comment."""
from pathlib import Path
from datetime import datetime, timezone

BUILD_LOG = Path("build-log.html")
text = BUILD_LOG.read_text(encoding="utf-8")

# Detect variant: starts with <div class="tick-entry"> (Variant B) or <h2> (Variant A)
first_chunk = text[:50]
if first_chunk.startswith('<div class="tick-entry"'):
    anchor = '<div class="tick-entry"'
    variant = "B (wrapped)"
elif first_chunk.startswith('<!-- TICK'):
    # Variant C: starts with the TICK comment — splice AFTER the comment but BEFORE first div
    # Look for the first <div class="tick-entry"> after the TICK comment
    tick_end = text.find('-->')
    if tick_end == -1:
        print("ERROR: TICK comment not closed"); raise SystemExit(1)
    after_tick = text[tick_end+3:]
    # Find first <div class="tick-entry"> in the post-comment text
    div_pos_in_after = after_tick.find('<div class="tick-entry"')
    if div_pos_in_after == -1:
        print("ERROR: no tick-entry div after TICK comment"); raise SystemExit(1)
    abs_anchor = tick_end + 3 + div_pos_in_after
    variant = "C (TICK-comment + tick-entry wrapper)"
else:
    # Variant A: <h2> at position 0
    if not text.startswith("<h2>"):
        print(f"ERROR: unknown variant, first 50 chars: {first_chunk!r}")
        raise SystemExit(1)
    abs_anchor = 0
    variant = "A (bare h2)"

print(f"Variant: {variant}")
print(f"Anchor position: {abs_anchor}")

# New entry: uses <div class="tick-entry" data-tick="2026-07-16T07:55Z"> wrapper with <h2> + <p>
ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
new_entry = f'''<!-- TICK {ts} -->
<div class="tick-entry" data-tick="{ts}">
<h2>Tick {ts} — chunk_155 Tonic.ai SEO landing (synthetic_data_privacy inaugural cohort)</h2>
<p>Shipped the inaugural <strong>synthetic_data_privacy</strong> landing-page chunk for lead 285 Tonic.ai:</p>
<ul>
<li>+ <strong>chunk_155.html</strong> (Tonic.ai + Tonic Structural + Tonic Textual + Tonic Clinical + Tonic Protect + Tonic Validate audit-trail SOC 2 + EU AI Act + HIPAA Safe Harbor + GDPR Anonymization + ISO 42001) — 16KB source + public, 14-column per-synthetic-record provenance join-table, 14-question buyer checklist, 5-layer reference architecture, 11-row SOC 2 / EU AI Act / ISO 42001 / HIPAA / GDPR cross-walk, $500 / 48h fixed-bid CTA → <code>285_tonic.md</code></li>
<li>+ <strong>leads.csv</strong> idx-285 Tonic.ai (privacy@tonic.ai, synthetic_data_privacy) — verified live 2026-07-16 via curl scrape <code>docs.tonic.ai/trust-center/privacy-notice.md</code> HTTP 200 (prior tick 07:40Z)</li>
<li>+ <strong>leads_with_emails.csv</strong> 13-col row with best_email <code>privacy@tonic.ai</code>, source_template <code>285_tonic.md</code></li>
<li>+ <strong>cold_email/templates/285_tonic.md</strong> — 4 audit-gap topics (per-synthetic-record provenance + per-membership-inference risk-scoring reasoning-chain + per-tenant KMS-CMK-BYOK + per-HIPAA-Safe-Harbor-identifier-category detection), $500 / 48h fixed-bid close, 15-min scope call CTA (prior tick 07:40Z)</li>
<li>+ <strong>sitemap.xml</strong> chunk_154 + chunk_155 entries added; balanced <url> tags (verified via ET.fromstring + balanced regex counts); recovered from patch-then-indent DOUBLE-BREAK on the chunk_153 sibling (Pitfall A from subagent-driven-development skill — script <code>scripts/_repair_sitemap_155.py</code> rewrote tail with literal multi-line <code>str.replace</code>)</li>
<li>+ <strong>index.html</strong> chunk-155 summary section inlined before <code></body></html></code> close (1 match for <code>id="chunk-155"</code>)</li>
</ul>
<p>Vertical status: <strong>synthetic_data_privacy</strong> = 1/5 (Tonic.ai inaugural). Research queue: MOSTLY AI (synthetic-data + differential-privacy), Gretel (LLM-fine-tuning-corpus + privacy-engineering), Synthesized (data-masking + test-data-generation), Ydata (tabular + time-series + statistical-fidelity), DataCebo/Synthetic-Data-Vault (open-source + enterprise). Audit-target ROI: HIPAA-vertical wedge + EU-public-sector + LLM-fine-tuning corpus + RAG-corpus replacement + EU AI Act Annex IV §1(c)+§1(d) automatic-logging are the four highest-leverage procurement signals in Q3-Q4 2026.</p>
<p>Prior commit <code>a5bd5f0</code> (Tick 07:40Z — Lead 285 Tonic.ai) shipped the lead + template pair. This tick completes the lead → template → chunk → sitemap → index → build-log cycle by adding chunk_155 + the sitemap/index inlines.</p>
</div>
'''

# Splice: prepend new_entry at the anchor position
new_text = text[:abs_anchor] + new_entry + text[abs_anchor:]

# Verify the new content structure
assert new_text.startswith('<!-- TICK') or new_text.startswith('<div class="tick-entry"') or new_text.startswith("<h2>"), "FAIL: startswith check"
assert new_text.count('<div class="tick-entry"') >= 1, "FAIL: no tick-entry div in new text"
tick_divs = new_entry.count('<div class="tick-entry"')
print(f"PASS: new entry has {tick_divs} tick-entry divs (want 1)")
assert tick_divs == 1
assert 'chunk_155' in new_text, "FAIL: chunk_155 missing"
assert 'Tonic.ai' in new_text, "FAIL: Tonic.ai missing"
assert "data-tick=" in new_entry, "FAIL: data-tick attr missing"

BUILD_LOG.write_text(new_text, encoding="utf-8")

print(f"PASS: build-log.html prepended ({len(new_entry)} bytes)")
print(f"PASS: total file size now {len(new_text)} bytes (was {len(text)})")
te_count = new_text.count('<div class="tick-entry"')
print(f"PASS: tick-entry count = {te_count}")