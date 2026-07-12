import re
from pathlib import Path

build_log = Path(r"C:\Users\Potts\projects\atlas-store\build-log.html")
new_tick_html = '''<div class="tick" id="tick-75">
<h3>Tick 75 (2026-07-12 01:19 UTC) — Retool (177) + 257_retool template</h3>
<p class="tick-meta">low_code_backend vertical · 2nd sibling after Rowy 176 · 5-min wall-clock</p>
<ul class="tick-tokens">
<li><strong>Lead:</strong> Retool (row 177) — low_code_backend #2 after Rowy 176</li>
<li><strong>Inbox:</strong> support@retool.com verified 2026-07-12 via curl scrape of retool.com/contact (HTTP 200, mailto exposed in canonical strategic-inbound routing block)</li>
<li><strong>Founder:</strong> David Hsu (CEO & Co-Founder, co-founded 2017 with Andrew Stojkovski + Justin OHarrow)</li>
<li><strong>Funding:</strong> ~$415M+ (Sequoia C-lead + Founders Fund B-lead + Coatue A-lead + IVP + Tiger Global + D1 Capital + Bain Capital Ventures + Work-Bench + Susa Ventures)</li>
<li><strong>Customers:</strong> 7,000+ enterprise (Amazon + Stripe + NBC + Verizon + Cisco + Plaid + Brex + Datadog + HubSpot + Atlassian + Wayfair + Doordash + Lyft + Snowflake)</li>
<li><strong>Compliance:</strong> SOC 2 Type II + ISO 27001 + HIPAA + GDPR DPA + CCPA/CPRA + EU AI Act readiness</li>
<li><strong>Distinct lane:</strong> enterprise-grade-low-code-internal-tools-builder-with-native-AI-agents + Workflows + Database + Mobile + Embed — audit-trail surface = per-retool-app-component + per-workflow-step + per-ai-agent-action-decision + per-database-query + per-mobile-action + per-embed-render + per-webhook-trigger + per-function-execution + downstream-Salesforce/Postgres/Stripe/Google-Sheets state change join-table</li>
<li><strong>5 audit gaps:</strong> (1) end-to-end provenance join-table SOC 2 CC7.2 + ISO 27001 A.12.4 + ISO 42001 §9.4 + EU AI Act Art. 12, (2) AI Agents + Functions training-corpus + fine-tune license-provenance EU AI Act Art. 53(d) + Art. 53(1)(b), (3) Database + Mobile + Embed cross-tenant isolation + downstream-data-source no-leakage SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + FedRAMP Mod + EU AI Act Art. 10, (4) AI Agents + Workflows human-oversight + risk-classification EU AI Act Annex III §4 + Art. 14, (5) AI Agents + Embed + Mobile customer-disclosure + Art. 50 transparency-obligation surface</li>
<li><strong>Sibling target:</strong> Rowy 176 (1st low_code_backend) + Internal + Budibase + Appsmith + Tooljet</li>
<li><strong>Template:</strong> cold_email/templates/257_retool.md — 11 audit-target tokens, $500/48h offer, founder-name greeting</li>
<li><strong>Pipeline:</strong> 173 leads (172 prior + Retool) · 154 templates (153 prior + 257_retool) · 73 SEO chunks · GRAND_PLAN.md Phase 1 + Phase 2 parallel</li>
<li><strong>CSV integrity:</strong> row 177 parsed cleanly 8 cols (csv.writer QUOTE_ALL, no nested-quote bug)</li>
<li><strong>Next:</strong> Phase 1 (UNBLOCK) needs SMTP creds from user + Chrome re-login; Phase 2 (TRAFFIC) push low_code_backend #3 = Internal</li>
</ul>
</div>
'''

content = build_log.read_text(encoding="utf-8")

tick_id_pattern = re.compile(r'<div class="tick" id="tick-(\d+)">')
matches = list(tick_id_pattern.finditer(content))
if not matches:
    raise SystemExit("no tick-id divs found")
newest = max(matches, key=lambda m: int(m.group(1)))
newest_n = int(newest.group(1))
newest_idx = newest.start()
print("Newest tick: id=tick-" + str(newest_n) + " at offset " + str(newest_idx))
assert newest_n == 74, "expected tick-74 newest, got tick-" + str(newest_n)

new_content = content[:newest_idx] + new_tick_html + "\n" + content[newest_idx:]
build_log.write_text(new_content, encoding="utf-8")

new_tick_idx = new_content.find('<div class="tick" id="tick-75">')
assert new_tick_idx < newest_idx, "tick-75 should appear before tick-74, but tick-75 at " + str(new_tick_idx) + " >= tick-74 at " + str(newest_idx)
print("OK: tick-75 spliced at offset " + str(new_tick_idx) + " (before tick-74 at " + str(newest_idx) + ")")

required_tokens = ["Retool", "support@retool.com", "David Hsu", "415M", "Sequoia", "7,000",
                   "low_code_backend", "Rowy 176", "257_retool.md", "173 leads",
                   "154 templates", "73 SEO chunks"]
missing = [t for t in required_tokens if t not in new_content]
assert not missing, "missing tokens: " + str(missing)
print("All " + str(len(required_tokens)) + " required tokens present")
print("Total ticks now: " + str(new_content.count('<div class="tick"')))
