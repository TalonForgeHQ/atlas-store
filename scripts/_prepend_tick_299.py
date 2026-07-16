"""Prepend tick 2026-07-16-1015Z build-log entry for Monte Carlo Data (lead 299, chunk 167)."""
from pathlib import Path

BUILD_LOG = Path(r"C:\Users\Potts\projects\atlas-store\build-log.html")

content = BUILD_LOG.read_text(encoding="utf-8")

# Detect variant: starts with <div class="tick-entry" ...> (Variant B) vs bare <h2> (Variant A)
first_50 = content[:50]
if first_50.startswith('<div class="tick-entry'):
    print("Variant B detected (starts with <div class=\"tick-entry\">)")
    anchor = '<div class="tick-entry'
    idx = content.find(anchor)
    assert idx == 0, f"Variant B anchor at position {idx}, not 0"
elif first_50.startswith('<h2>'):
    print("Variant A detected (starts with <h2>)")
    anchor = '<h2>'
    idx = content.find(anchor)
    assert idx == 0, f"Variant A anchor at position {idx}, not 0"
else:
    print(f"WARN: unknown variant, first 50 chars: {first_50!r}")
    raise SystemExit(1)

# Build the new tick entry
NEW_TICK = '''<div class="tick-entry" data-tick="2026-07-16-1015Z">
<h2>Tick 2026-07-16-1015Z — Lead 299 / Monte Carlo Data / privacy@montecarlodata.com</h2>
<p><strong>Action:</strong> Shipped lead 299 (Monte Carlo Data, 2nd-sibling in ai_data_quality_observability vertical) + template 370_montecarlodata.md + chunk 167 (chunks/chunk_167.html + _chunks/chunk_167.html byte-identical) + sitemap entry + index.html inline section + CTA. <strong>ROI rationale:</strong> Monte Carlo is the canonical 2nd-sibling in ai_data_quality_observability cohort (Cleanlab is 1st-sibling). Distinct surface: per-data-asset-id + per-data-pipeline-id + per-data-SLO-breach-event-id + per-ML-model-monitoring-event-id join-table (the data-downtime + ML model monitoring chain Cleanlab doesn't have). <strong>Inbox:</strong> privacy@montecarlodata.com verified live 2026-07-16 via curl scrape https://www.montecarlodata.com/privacy-policy/ HTTP 200 + https://www.montecarlodata.com/about HTTP 200 (Barr Moses + Lior Gavish co-founders surfaced). <strong>Funding:</strong> $236M+ raised, $1.6B+ valuation, GGV Capital + ICONIQ + Salesforce Ventures + Redpoint + Accel + Bessemer. <strong>Customers:</strong> 100+ Fortune-500 + Global-2000 + AI-native (Fox, Santander, Microsoft, Snap, Wayfair, Substack, Mux, Zillow, Honeywell, Compass). <strong>Frameworks:</strong> SOC 2 Type II + ISO 27001 + GDPR DPA + EU AI Act readiness + HIPAA + NIST AI RMF. <strong>Cohort already shipped:</strong> Cleanlab (297, legal@cleanlab.ai) + Glean (298, privacy@glean.com) + Suki (294, support@suki.ai) + Arize (295, privacy@arize.com) + Abridge (296, privacy@abridge.com). <strong>Pattern:</strong> 3-question opener + $500/48h CTA + EU AI Act Art. 53(d) license-provenance gap call-out (Monte Carlo trails Cleanlab on per-training-corpus-id coverage — explicit gap, not papered over). <strong>Phase 1/2 plan alignment:</strong> Phase 1 (UNBLOCK) requires SMTP credentials for outbound; this lead is staged + chunk live + index inlined so when unblock arrives, 6th outreach can fire in &lt;2 min. Phase 2 (TRAFFIC) — 53 chunks live, sitemap valid, all chunks in landing-page index. <strong>Next tick candidates:</strong> (a) 3rd-sibling in ai_observability_evals (Arize + Galileo + Datadog + Honeycomb), (b) 3rd-sibling in ai_healthcare_clinical_assistant (Suki + Abridge + DeepScribe / Nuance DAX), (c) research next 5 vertical cohorts. <strong>Pitfall avoided:</strong> patch across sitemap block boundary caused 6-space over-indent (chunk_166 inner lines + new chunk_167 inner lines) — verified via XML parse OK + balanced-tag check, then repaired with _repair_sitemap_tick299.py to restore 4-space indent consistency. Net work: 1 lead + 1 template + 1 chunk + 1 sitemap entry + 1 index inline + 1 build-log entry + sitemap repair commit. Cron: this tick is the 15-min Revenue Loop cycle (c23f3b37a9e2), Fast Execution cycle ran 5 min prior at 2026-07-16-1005Z (Glean / lead 298 / chunk 166). Both crons converge on the same cohort-strategy: ship a Tier-1 lead + template + chunk every cycle, keep the cold-email pipeline warm while SMTP unblock is pending.</p>
<p><strong>Files touched:</strong> cold_email/leads.csv (+1 row 299), cold_email/templates/370_montecarlodata.md (new, 3.4KB), _chunks/chunk_167.html (new, 13.4KB), chunks/chunk_167.html (mirror, 13.4KB), index.html (inline section +4 lines), sitemap.xml (+1 url block, indent-repaired), build-log.html (this entry).</p>
</div>
'''

# Sanity: exactly one wrapper
wrapper_count = NEW_TICK.count('<div class="tick-entry')
assert wrapper_count == 1, f"wrapper count: {wrapper_count}"

# Splice: content[:idx] + NEW_TICK + content[idx:]
new_content = content[:idx] + NEW_TICK + content[idx:]

BUILD_LOG.write_text(new_content, encoding="utf-8")
print(f"OK: build-log.html prepended, new top anchor at char 0, file size {len(new_content)} bytes")
print(f"NEW_TICK length: {len(NEW_TICK)} chars")
print(f"Original idx={idx}, content length={len(content)}, new length={len(new_content)}")