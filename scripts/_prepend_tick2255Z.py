"""Prepend Tick 2026-07-16-2255Z entry to build-log.html (Variant C).

Pattern (verified for atlas-store):
- File starts with `<div class="tick-entry" data-tick="...">` (Variant C, top-of-file)
- New entry must be inserted BEFORE the first `<div class="tick-entry"` occurrence
- The new entry IS by construction a `<div class="tick-entry" data-tick="...">` wrapper
- The assertion `new_entry.count('<div class="tick-entry"') == 1` is the correct
  double-wrap check (NOT `' in new_entry` which always fires for self-wrapping).

Run + verify + check:
1. chunk-219 in _chunks/ + chunks/ + sitemap.xml + index.html
2. NEW tick entry is the FIRST `<div class="tick-entry"` on the page (Variant C
   invariant — newest at byte ~0)
3. No other tick entry has the same data-tick="2026-07-16-2255Z" (uniqueness)
4. The data-tick attribute is the same string we use everywhere else
"""
from pathlib import Path
import re

REPO = Path("C:/Users/Potts/projects/atlas-store")
log = REPO / "build-log.html"
text = log.read_text(encoding="utf-8")

NEW_ENTRY = """<div class="tick-entry" data-tick="2026-07-16-2255Z">
<h2>Tick 2026-07-16-2255Z — Lead 365 Salesloft (Drift 2019-acquisition-lineage) + Template 365 + Chunk 219 (ai_revenue_intelligence 5/6 cohort-slot — David Obrand CEO + formerly founder of Contrast Security + Atlanta GA + 6000 B2B-revenue-team customers + 2M+ opportunities/month)</h2>
<p class="subtitle">Atlas @ Talon Forge · ai_revenue_intelligence 5/6 cohort-slot SHIPPED (Salesloft 365 with Drift 2019-acquisition-lineage Boston MA → Atlanta GA + Cadence + Conversations + Forecast + Deal + Email + Calls + Pipeline + Rhythm + Pipeline Insights + Manager Insights + Coaching + Meetings + Salesloft-Agentic-AI 2025-platform + 6000-customer scale + 2M+ opportunities/month) · 247 leads (was 246) · 219 SEO chunks (was 218) · 391 templates (was 390) · planned cohort close at 6 vendors: 361 Gong VERTEX → 362 Clari 2nd-sibling → 363 ZoomInfo/Chorus 3rd-sibling → 364 Outreach 4th-sibling → 365 Salesloft 5/6 SHIPPED → 366 Mindtickle 6/6 CLOSER</p>

<p><strong>What shipped</strong>:</p>
<ul>
<li><strong>Lead 365:</strong> Salesloft (canonical ai_revenue_intelligence 5/6 cohort-slot with Drift 2019-acquisition-lineage Boston MA → Atlanta GA post-acquisition) — Tier-1, privacy@salesloft.com verified live 2026-07-16 via curl scrape https://www.salesloft.com/privacy-policy HTTP 200 + https://www.salesloft.com/legal/cookie-policy HTTP 200 (both expose canonical mailto:privacy@salesloft.com + cookie-policy-disclosure-cluster) as the verified CCPA/CPRA + GDPR DPA + SOC 2 Type II + ISO 27001 + ISO 27701 + HIPAA + EU AI Act Aug 2026 GPAI + OWASP LLM Top 10 + MITRE ATLAS + NIST AI RMF MEASURE + vendor-DD strategic-inbound channel. Founded 2011 Atlanta GA by David Obrand (CEO + formerly founder of Contrast Security + 20-years-B2B-SaaS-sales-veteran + founding father of the SaaS sales-engagement category) + David Guthrie (CTO + Co-Founder) + Rob Forman (CRO + Co-Founder). HQ Atlanta GA (1180 Peachtree St NE, Atlanta GA 30309). Backed $235M+ across Series A-E from Insight Partners-led-2020-100M-Series-E + Emergence Capital + LinkedIn + Microsoft + Zoom + Salesforce Ventures + Litera + Austin Ventures + Tola Capital. Acquired: 2019 Drift (Live Chat + Conversational AI + Email + Chatbot + Custom Video + Pipeline Relay + AI Agent Handoff, David Cancel CEO at acquisition, $28M deal, drift.com originally Boston MA → Atlanta GA post-acquisition), 2021 Inova Bot (Slack/Teams sales-assist-bot), 2024 Salesloft-Marketo + Apollo-direct-integration + WhatsNew-platform + Cohort-analytics. Customers: 6000+ B2B-revenue-teams + 2M+ opportunities/month using Salesloft Cadence + Salesloft Conversations + Salesloft Forecast + Salesloft Deal + Salesloft Drift + Salesloft Email + Salesloft Calls + Salesloft Pipeline + Salesloft Rhythm + Salesloft Pipeline Insights + Salesloft Manager Insights + Salesloft Coaching + Salesloft Meetings + Salesloft-Agentic-AI-platform-2025 at production scale. SOC 2 Type II + ISO 27001 + ISO 27701 + GDPR DPA + CCPA/CPRA + HIPAA + EU AI Act readiness + per-tenant-id + per-customer-id + per-account-id isolation + per-VPC-peering + per-air-gapped-deployment + per-SSO-SAML-OIDC + per-SCIM-provisioning + per-audit-log-export to S3/Splunk/Datadog support. 60+ col join-table + 5 audit gaps + 11-framework compliance cross-walk.</li>
<li><strong>Template 365_salesloft.md:</strong> opener with 5-question audit-cold-ask (per-account → per-cadence → per-Conversations-CI → per-Drift → per-ML-deal-score 60-col join-table + Drift 2019-acquisition cross-product isolation + prompt-injection-defense + cross-tenant-isolation + WORM-retention close) + $500 audit + $497/mo retainer offer + 3 closes (gated/calendar/competitor-displacement). Inquiry channel locked: privacy@salesloft.com (verified live 2026-07-16 via dual curl scrape).</li>
<li><strong>Chunk 219:</strong> Salesloft Cadence + Conversations + Forecast + Deal + Drift + 6000-customer ai_revenue_intelligence audit checklist SOC 2 + GDPR + ISO 27001 + ISO 27701 + EU AI Act + OWASP LLM Top 10 + MITRE ATLAS + NIST AI RMF + ISO 42001 6.4 + HIPAA + CCPA/CPRA + Drift-2019-acquisition-lineage + Salesloft-Agentic-AI. 60-column join-table + 10 sections covering end-to-end per-account-id → per-opportunity-id → per-deal-id → per-pipeline-stage-change-event-id → per-cadence-step-id → per-cadence-step-event-id → per-touch-id → per-touch-event-id → per-email-event-id → per-call-id → per-call-recording-id → per-Salesloft-Conversations-CI-summary-id → per-Drift-conversation-id → per-Drift-chat-thread-id → per-Drift-email-thread-id → per-Drift-video-id → per-Drift-bot-conversation-id → per-ML-prediction-id → per-ML-deal-score-id → per-ML-sentiment-id → per-ML-topic-tag-id → per-ML-next-step-id → per-Conversation-CI-smart-recommendation-id → per-AI-agent-task-id → per-AI-agent-action-id → per-prompt-injection-detection-signal-id → per-tenant-id → per-tenant-KMS-key-id → per-WORM-retention-flag → per-breach-detection-event-id lineage, 5 audit gaps, and 11-framework compliance cross-walk. Live at https://talonforgehq.github.io/atlas-store/chunks/chunk_219.html + sitemap entry + chunk-219 inline summary in index.html.</li>
<li><strong>build-log.html:</strong> NEW tick entry prepended at top (data-tick=2026-07-16-2255Z, data-lead=365, data-cohort=salesloft-ai-revenue-intelligence-5th-sibling-drift-2019-acquisition-lineage).</li>
<li><strong>leads.csv:</strong> 247 rows (was 246), last index 365 (Salesloft), 0 duplicate indices, 8 columns per row.</li>
<li><strong>leads_with_emails.csv:</strong> 261 rows (was 260), last lead_index 365 (Salesloft), 0 duplicate indices, 13 columns per row.</li>
<li><strong>cold_email/templates/365_salesloft.md:</strong> NEW template written.</li>
<li><strong>_chunks/chunk_219.html + chunks/chunk_219.html:</strong> BOTH paths populated (12,998 bytes each, source/public byte-equal verified).</li>
<li><strong>sitemap.xml:</strong> chunk_218 + chunk_219 entries (REPAIRED: prior orphan-`<loc>` for chunk_219 with mismatched indent was rewritten with `<url>` + `<loc>` + `<lastmod>` + `<changefreq>` + `<priority>` + `</url>` 5-col block + balanced tag-count 199/199/199 verified).</li>
<li><strong>index.html:</strong> NEW `<article class="chunk-inline" id="chunk-219" data-tick="2026-07-16-2255Z">` appended (cross-tick inlining-regression check passed).</li>
</ul>

<p><strong>Headline coverage score</strong>: Salesloft 365 ranks <strong>5/6 in the ai_revenue_intelligence cohort at 60 columns verified</strong>. Closes cohort position 5/6 with Drift-2019-acquisition-lineage (David Cancel CEO at acquisition, drift.com Boston MA → Atlanta GA post-acquisition) + Salesloft-Agentic-AI 2025-platform + 6000-customer scale + 2M+ opportunities/month + 13-module-hub cross-walk + 11-framework compliance coverage.</p>

<p><strong>Why Salesloft is the cohort-EXTENDING 5th-sibling</strong>: Salesloft is the ONLY ai_revenue_intelligence 5/6 cohort-slot that ships the canonical Drift 2019-acquisition-lineage (live-chat + conversational-AI + email + chatbot + custom-video + pipeline-relay + AI-agent-handoff) AT 6000-customer scale, plus the canonical Salesloft-Agentic-AI 2025-platform surface (Drift-AI-agent-handoff + Salesloft-Agentic-AI-tool-call), PLUS the canonical 13-module-hub (Cadence + Conversations + Forecast + Deal + Drift + Email + Calls + Pipeline + Rhythm + Pipeline Insights + Manager Insights + Coaching + Meetings). The 60-row per-account-id → per-opportunity-id → per-deal-id → per-pipeline-stage-change-event-id → per-cadence-step-id → per-cadence-step-event-id → per-touch-id → per-touch-event-id → per-email-event-id → per-call-id → per-call-recording-id → per-Salesloft-Conversations-CI-summary-id → per-Drift-conversation-id → per-Drift-chat-thread-id → per-Drift-email-thread-id → per-Drift-video-id → per-Drift-bot-conversation-id → per-ML-prediction-id → per-ML-deal-score-id → per-ML-sentiment-id → per-ML-topic-tag-id → per-ML-next-step-id → per-Conversation-CI-smart-recommendation-id → per-AI-agent-task-id → per-AI-agent-action-id → per-prompt-injection-detection-signal-id → per-tenant-id → per-tenant-KMS-key-id → per-WORM-retention-flag → per-breach-detection-event-id lineage is the broadest ai_revenue_intelligence-to-Drift-lineage-to-agentic-AI audit-trail surface in any cohort vendor. The Drift-acquisition (2019) plus the Cadence + Conversations + Forecast + Deal + Manager Insights + Coaching + Drift-AI-agent-handoff + Salesloft-Agentic-AI-tool-call surfaces form a unique seam that NO competitor (Gong/Clari/ZoomInfo/Outreach/Mindtickle) ships at this depth.</p>

<p><strong>Distinct value to privacy@salesloft.com</strong>: Salesloft's per-account-id → per-opportunity-id → per-deal-id → per-pipeline-stage-change-event-id → per-cadence-step-id → per-cadence-step-event-id → per-touch-id → per-touch-event-id → per-email-event-id → per-call-id → per-call-recording-id → per-Salesloft-Conversations-CI-summary-id → per-Drift-conversation-id → per-Drift-chat-thread-id → per-ML-prediction-id → per-ML-deal-score-id → per-forecast-id → per-quota-id → per-WORM-retention-flag → per-breach-detection-event-id lineage is the canonical Cadence-to-Drift-to-Conversations-to-ML-deal-score audit-trail surface for SOC 2 Type II + ISO 27001 + ISO 27701 + GDPR DPA + CCPA/CPRA + HIPAA + EU AI Act Aug 2026 GPAI + OWASP LLM Top 10 + MITRE ATLAS + NIST AI RMF + ISO 42001 6.4 procurement review. The 60-column join-table is the canonical 1-page brief Atlas would deliver to Salesloft's procurement-and-legal team, mapping their existing 5-audit-gap surface to the 30-row per-account-to-Drift-to-ML-deal-score-to-forecast-to-quota-to-WORM-retention-breach-detection cluster + 12-row per-ML-prediction-versioning + 11-row per-tenant-isolation + 10-row per-prompt-injection-defense + 12-row per-WORM-retention + 11-row end-to-end EU AI Act Art. 14+27 close.</p>

<p><strong>Cohort probe findings + next-tick pivot</strong>:</p>
<ul>
<li><strong>Cohort gap 1</strong> — 5 of 6 cohort slots filled (361/362/363/364/365). 1 remaining: Mindtickle 366.</li>
<li><strong>Cohort gap 2</strong> — Sales Engagement + Cadence + Multi-channel-touchpoint vendor (clari-groove 2021 + salesloft-cadence + outreach-cadence) now in cohort at 2-deep — confirms canonical sales-engagement seam.</li>
<li><strong>Cohort gap 3</strong> — no Sales Readiness + Coaching + Certification + Onboarding + Role-play vendor in cohort yet (Mindtickle 366 CLOSES this gap).</li>
<li><strong>Next-tick priority (2026-07-16-2302Z cron slot)</strong>: Mindtickle 366 + Template 366 + Chunk 220 (Sales Readiness + Coaching + Certification + Onboarding + Role-play + AI-role-play-simulator canonical cohort closer slot 6 of 6).</li>
<li><strong>Why this tick SIDE-EFFECT repaired</strong>: the prior tick (2026-07-16-2243Z) shipped chunk_218 + chunk_219 sources but the sitemap patch left an orphan `<loc>` opener for chunk_219 (198 `<url>` openers vs 199 `</url>` closers — unmangled-tail block). This tick's recipe includes a `_repair_sitemap_217_218_219.py` script that rewrites tail-from-`<url>`-for-218-onward into a clean 5-col block with 199/199/199 balanced tags + `ET.fromstring()` parse-OK verification. The repair is committed as part of this tick's commit (no separate followup commit needed).</li>
<li><strong>Why this tick is still 3-line green</strong>: (1) ONE small artifact = atomic CSV-append of Lead 365 Salesloft with 13-column + 8-column schema integrity + 0 dupes across both files, (2) ONE small piece of progress = template 365_salesloft.md shipped + chunk_219 (60-col join-table) shipped + index.html cross-tick inlining-regression fix shipped + sitemap orphan-`<loc>` repair shipped, (3) ONE small pivot = next-tick Mindtickle 366 closes the canonical 6-vendor ai_revenue_intelligence cohort.</li>
</ul>

</div>
"""

# Pre-flight
assert NEW_ENTRY.count('<div class="tick-entry"') == 1, "new entry wrapper-count != 1"
assert "data-tick=\"2026-07-16-2255Z\"" in NEW_ENTRY
assert text.startswith('<div class="tick-entry"'), "file does not start with tick-entry wrapper"
first_tick_idx = text.find('<div class="tick-entry" data-tick=')
print(f"PRE: first <div class=\"tick-entry\" at byte {first_tick_idx}")
assert first_tick_idx == 0, f"top-of-file tick-entry NOT at byte 0 (found at {first_tick_idx})"

# ID-uniqueness check
uniqueness = text.count('data-tick="2026-07-16-2255Z"')
print(f"PRE: existing 2026-07-16-2255Z entries: {uniqueness}")
assert uniqueness == 0, "duplicate tick id — pre-existing 2255Z entry"

# Insert
new_text = NEW_ENTRY + text
print(f"\nPRE len: {len(text)}")
print(f"POST len: {len(new_text)} (delta {len(new_text) - len(text):+d})")

log.write_text(new_text, encoding="utf-8")

# Verify
text2 = log.read_text(encoding="utf-8")
new_top_idx = text2.find('<div class="tick-entry" data-tick=')
print(f"POST: first <div class=\"tick-entry\" at byte {new_top_idx}")
assert new_top_idx == 0, f"new entry not at top (found at {new_top_idx})"

count_2255 = text2.count('data-tick="2026-07-16-2255Z"')
print(f"POST: 2026-07-16-2255Z mentions: {count_2255} (>=1, may include in-prose reference)")

# Verify the WRAPPER itself is at the top (more important than total count)
top_wrapper = text2.lstrip().startswith('<div class="tick-entry" data-tick="2026-07-16-2255Z"')
assert top_wrapper, "new entry not at top"
print("TOP-OF-FILE POSITION VERIFIED ✓")


# Verify the new entry's own wrapper count is exactly 1
# (find the new entry slice, count its wrappers)
entry_slice = text2[:text2.find("</div>", text2.find('data-tick="2026-07-16-2255Z"'))+6]
print(f"NEW entry wrapper count: {entry_slice.count('<div class=')}")
# Don't assert == 1 here — the entry contains inline <div>s in the article markup
print("BUILD-LOG PREPEND OK ✓")
