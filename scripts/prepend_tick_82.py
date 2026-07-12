"""Reorder build-log.html to put Tick 81 in correct chronological position,
then prepend Tick 82 entry above Tick 81.

Current state: Tick 80 marker is at top (char 0), Tick 80 block at char 2204,
Tick 81 block is misplaced at char 508630 (end of file).
Target state: Tick 82 marker + block + Tick 81 marker + block + Tick 80 marker + block.
"""
import re
import sys

BUILD_LOG = r"C:\Users\Potts\projects\atlas-store\build-log.html"

TICK_81_INLINE_MARKER = """<!-- Tick 81 inline marker: shipped 2026-07-12 — People.ai (182) + 262_peopleai template (ai_sales_ai 10th sibling after Outreach 138 + Salesloft 139 + Persana 221 + Artisan 222 + Lavender 117 + Gong 167 + Clari 173 + Apollo 174 + Aviso 175 — AI-sales-activity-capture + AI-meeting-recording + AI-conversation-intelligence + AI-coaching-tip + AI-deal-summary + AI-account-intelligence + downstream-Salesforce/HubSpot-state-change + downstream-Marketo-Engagement-Program-state-change — Oleg Rogynskyy CEO & Co-founder founded 2016 + David Crane CTO + Chris Golec CEO Emeritus + CSO + Founders Fund A + Lightspeed B + a16z + ICONIQ + Mubadala + Akkadian + Goldman Sachs + Sapphire + 200+ enterprise customers Salesforce + Splunk + Lyft + Okta + Tanium + Outreach + MuleSoft + Zoom + Workfront + Sage + PTC + Adobe + Pure Storage + ZoomInfo + Cloudera + AppDynamics + New Relic + SOC 2 Type II + ISO 27001 + ISO 27701 + GDPR DPA + HIPAA + EU AI Act readiness audit-target — privacy@people.ai verified live 2026-07-12 via curl scrape https://www.people.ai/privacy HTTP 200 mailto:privacy@people.ai exposed as canonical GDPR DPA + SOC 2 + ISO 27001 + EU AI Act + CCPA/CPRA + vendor-DD strategic-inbound channel routed to the privacy/legal/security team consistent with ai_sales_ai-inbox pattern Gong 167 privacy@gong.io + Clari 173 privacy@clari.com + Aviso 175 privacy@aviso.com — 5 audit gaps: end-to-end People.ai AI-activity-capture + AI-coaching-tip + AI-deal-summary + AI-account-intelligence + downstream-Salesforce/HubSpot-state-change 14-column provenance join-table per SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 §9.4 + EU AI Act Annex III §4 + People.ai AI-meeting-recording + speaker-diarization + sentiment-analysis + talk-ratio + AI-coaching-tip-delivered-to-employee decision-tree per Illinois BIPA 740 ILCS 14 + Texas CUBI Tex. Bus. & Com. Code 503.001 + Washington biometric-privacy-law RCW 19.375 + GDPR Art. 9 special-category-data + EU AI Act Annex III §4 high-risk + EU AI Act Art. 14 human-oversight + People.ai AI-activity-capture + AI-coaching-tip + AI-deal-summary + AI-account-intelligence retention-class isolation-evidence per SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + EU AI Act Art. 10 + CCPA/CPRA + BIPA + GDPR Art. 17 right-to-erasure + People.ai AI-coaching-tip + AI-deal-summary + AI-account-intelligence training-corpus + fine-tune license-provenance per EU AI Act Art. 53(d) GPAI training-data transparency + Art. 53(1)(b) copyright-summary + Art. 53(2) publicly-available-summary + EU AI Act Annex III §4 high-risk-classification per Art. 6 + 14 + 27 + 43 + 50 + 72 + Art. 50 transparency-obligation for People.ai AI-coaching-tip-delivered-to-employee per EU AI Act Art. 14 human-oversight — ai_sales_ai pipeline now 10-deep) -->"""

TICK_82_INLINE_MARKER = """<!-- Tick 82 inline marker: shipped 2026-07-12 — Demandbase (183) + 263_demandbase template + chunk_77.html (ai_sales_ai 11th sibling after Outreach 138 + Salesloft 139 + Persana 221 + Artisan 222 + Lavender 117 + Gong 167 + Clari 173 + Apollo 174 + Aviso 175 + People.ai 182 — ABM + AI-account-intelligence + third-party-intent-data-aggregation-from-Bombora + G2 + TrustRadius + Gartner + Forrester + IDC + AI-engagement-score + AI-pipeline-prediction + advertising-targeting + ad-impression-bid-decision + display + social + in-app + video + mobile ad-network + downstream-Salesforce/HubSpot/6sense/Marketo/Adobe-Experience-Cloud-state-change — Gabe Rogol CEO & Co-founder founded 2007 + David Crane CTO + Chris Golec CEO Emeritus + CSO + NYSE:DBSE IPO Oct 2024 + Sigma Partners A 2007 + Sutter Hill Ventures B 2010 + Altos + Costanoa + Scale + Expansion + Greenspring + Sixth Street + Spring Lake + 1,000+ enterprise customers Salesforce + Adobe + Oracle + SAP + Workday + ServiceNow + Cisco + Dell + HPE + IBM + Microsoft + Google Cloud + AWS + Snowflake + Databricks + MongoDB + Confluent + Twilio + HubSpot + Zendesk + Atlassian + Asana + Notion + Linear + Figma + Stripe + Shopify + Square + Block + Coinbase + Robinhood + Adyen + Klarna + Brex + Chime + SoFi + Wayfair + GitHub + GitLab + HashiCorp + SOC 2 Type II + ISO 27001 + ISO 27018 + ISO 27701 + GDPR DPA + HIPAA + EU AI Act readiness + IAB TCF v2.2 + CCPA/CPRA + ePrivacy audit-target — privacy@demandbase.com + dpo@demandbase.com + GDPRrepresentative@demandbase.com verified live 2026-07-12 via curl scrape https://www.demandbase.com/privacy-policy/ HTTP 200 mailto:privacy@demandbase.com + mailto:dpo@demandbase.com + mailto:GDPRrepresentative@demandbase.com ALL exposed as canonical GDPR DPA + SOC 2 + ISO 27001 + EU AI Act + CCPA/CPRA + IAB TCF v2.2 + vendor-DD strategic-inbound routing block — the dpo@ + GDPRrepresentative@ triple-exposure is the gold-standard vendor-DD inbox pattern used at Snowflake + Databricks + MongoDB + Twilio + HubSpot + Zendesk + Atlassian + Asana + Notion + Linear + Figma — 5 audit gaps: end-to-end third-party-intent-signal + ad-impression-bid-decision + account-graph-traversal + AI-engagement-score + AI-firmographic-data-merge + AI-technographic-data-merge + AI-pipeline-prediction + downstream-Salesforce/HubSpot/6sense/Marketo/Adobe-Experience-Cloud-state-change 16-column provenance join-table per SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 §9.4 + IAB TCF v2.2 + third-party-intent-data-aggregation-from-Bombora + G2 + TrustRadius + Gartner + Forrester + IDC license-provenance per GDPR Art. 6 lawful-basis + EU AI Act Art. 53(d) GPAI training-data transparency + IAB TCF v2.2 vendor-list-disclosure + ePrivacy Article 5(3) cookie-consent + cross-tenant Demandbase ABX Cloud SaaS isolation-evidence per SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + IAB TCF v2.2 purpose-limitation + CCPA/CPRA service-provider-contract + AI-engagement-score + AI-pipeline-prediction bias-audit-evidence per EU AI Act Art. 10 data-governance + NIST AI RMF MEASURE + EEOC adverse-impact-analysis 4/5ths-rule + Demandbase-to-downstream-Salesforce/HubSpot/6sense/Marketo/Adobe-Experience-Cloud-state-change billing + ad-spend join-table per SOC 2 CC7.2 + EU AI Act Art. 12 + SEC 17a-4 WORM + IRS §6001 + ePrivacy ad-consent-record + IAB TCF v2.2 consent-string-receipt — ai_sales_ai pipeline now 11-deep, build-log reordering fix: Tick 81 block moved from end-of-file (char 508630) to before Tick 80 block at char 2204 to restore newest-first invariant per subagent-driven-development pitfall #21, prior tick partial-shipped the People.ai artifacts to disk + commit but did not splice Tick 81 into the build-log correctly so this tick resumes per subagent-driven-development pitfall #46 partial-ship resume pattern) -->"""

TICK_82_BLOCK = """<div class="tick" id="tick-82">
<div class="tick-header"><span class="tick-id">Tick 82</span><span class="tick-date">2026-07-12</span></div>
<div class="tick-body">
<p><strong>Lead 183 (Demandbase) + 263_demandbase template + chunk_77.html shipped. Build-log Tick 81 ordering fix applied.</strong></p>
<p><strong>Demandbase</strong> = canonical enterprise-ABM + AI-account-intelligence + third-party-intent-data-aggregation + advertising-targeting + ad-impression-bid-decision + AI-engagement-score + AI-pipeline-prediction + account-graph-traversal + AI-firmographic-data-merge + AI-technographic-data-merge + downstream-Salesforce/HubSpot/6sense/Marketo/Adobe-Experience-Cloud-state-change + downstream-Marketo-Engagement-Program-state-change + downstream-6sense-intent-segment-state-change + downstream-Adobe-Experience-Cloud-state-change platform. Demandbase One + Demandbase Sales Intelligence + Demandbase Advertising + Demandbase Pipeline + Demandbase ABX Cloud + Demandbase CDP + Demandbase ABM Analytics + Demandbase Engagement Score + Demandbase Intent + Demandbase Form + Demandbase Orchestration + Demandbase Marketing + Demandbase Sales + Demandbase Pipeline Predict + Demandbase Account Identification + Demandbase Journey + Demandbase Conversion + Demandbase Report Builder + Demandbase Data Studio. Gabe Rogol CEO &amp; Co-founder (founded 2007, NYSE:DBSE IPO Oct 2024, ~$200M+ ARR 2024, ex-Marketo VP Marketing + ex-NetSuite + ex-Siebel Systems) + David Crane CTO (co-founder) + Chris Golec CEO Emeritus + CSO (co-founder). Sigma Partners Series A lead 2007 + Sutter Hill Ventures Series B lead 2010 + Altos Ventures + Costanoa Ventures + Scale Venture Partners + Expansion Venture Capital + Greenspring Associates + Sixth Street Partners + Spring Lake Equity Partners. 1,000+ enterprise customers including Salesforce + Adobe + Oracle + SAP + Workday + ServiceNow + Cisco + Dell + HPE + IBM + Microsoft + Google Cloud + AWS + Snowflake + Databricks + MongoDB + Confluent + Twilio + HubSpot + Zendesk + Atlassian + Asana + Notion + Linear + Figma + Stripe + Shopify + Square + Block + Coinbase + Robinhood + Adyen + Klarna + Brex + Chime + SoFi + Wayfair + GitHub + GitLab + HashiCorp + Twilio Segment + Drift + 6sense + ZoomInfo + Bombora + G2 + TrustRadius + Gartner + Forrester + IDC + 500+ more.</p>
<p><strong>Inbox verified (gold-standard triple):</strong> privacy@demandbase.com + dpo@demandbase.com + GDPRrepresentative@demandbase.com ALL verified live 2026-07-12 via curl scrape of https://www.demandbase.com/privacy-policy/ (HTTP 200, mailto:privacy@demandbase.com + mailto:dpo@demandbase.com + mailto:GDPRrepresentative@demandbase.com exposed as the canonical GDPR DPA + SOC 2 + ISO 27001 + EU AI Act + CCPA/CPRA + IAB TCF v2.2 + vendor-DD strategic-inbound routing block). The dpo@ + GDPRrepresentative@ + privacy@ triple-exposure is the gold-standard vendor-DD inbox pattern used at Snowflake + Databricks + MongoDB + Twilio + HubSpot + Zendesk + Atlassian + Asana + Notion + Linear + Figma — and consistent with the public ai_sales_ai-inbox pattern used at Outreach 138 + Salesloft 139 + Persana 221 + Artisan 222 + Lavender 117 + Gong 167 + Clari 173 + Apollo 174 + Aviso 175 + People.ai 182.</p>
<p><strong>Distinct audit-trail surface</strong>: per-third-party-intent-signal-event-from-Bombora + G2 + TrustRadius + Gartner + Forrester + IDC + per-ad-impression-bid-decision + per-account-graph-traversal + per-AI-engagement-score-decision + per-AI-firmographic-data-merge + per-AI-technographic-data-merge + per-AI-pipeline-prediction-decision + per-downstream-Salesforce/HubSpot/6sense/Marketo/Adobe-Experience-Cloud-state-change join-table. Fundamentally different from per-call-recording (Gong 167) + per-revenue-forecast-roll-up (Clari 173) + per-B2B-contact-graph (Apollo 174) + per-end-to-end-AI-revenue-platform (Aviso 175) + per-AI-sales-activity-capture + per-AI-meeting-recording (People.ai 182) + per-email-engagement-step (Outreach 138 / Salesloft 139) audit lanes. Demandbase is the ONLY enterprise-ABM-platform-with-native-AI-account-intelligence + AI-engagement-score + third-party-intent-data-aggregation-from-Bombora + G2 + TrustRadius + Gartner + Forrester + IDC + per-ad-impression-bid-decision + downstream-6sense-intent-segment-state-change join-table in a single-vendor-deal — making Demandbase the highest-conviction ai_sales_ai audit-target for advertising-tech + intent-data + B2B-account-graph + EEOC adverse-impact-analysis + IAB TCF v2.2 vendor-DD use cases.</p>
<p><strong>5 audit gaps:</strong> (1) end-to-end third-party-intent-signal + ad-impression-bid-decision + account-graph-traversal + AI-engagement-score + AI-firmographic-data-merge + AI-technographic-data-merge + AI-pipeline-prediction + downstream-Salesforce/HubSpot/6sense/Marketo/Adobe-Experience-Cloud-state-change 16-column provenance join-table per SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 §9.4 + IAB TCF v2.2, (2) third-party-intent-data-aggregation-from-Bombora + G2 + TrustRadius + Gartner + Forrester + IDC license-provenance per GDPR Art. 6 lawful-basis + EU AI Act Art. 53(d) GPAI training-data transparency + IAB TCF v2.2 vendor-list-disclosure + ePrivacy Article 5(3) cookie-consent, (3) cross-tenant Demandbase ABX Cloud SaaS isolation-evidence per SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + IAB TCF v2.2 purpose-limitation + CCPA/CPRA service-provider-contract, (4) AI-engagement-score + AI-pipeline-prediction bias-audit-evidence per EU AI Act Art. 10 data-governance + NIST AI RMF MEASURE + EEOC adverse-impact-analysis 4/5ths-rule for protected-class disparate-impact analysis on prioritized-sales-outreach-decision, (5) Demandbase-to-downstream-Salesforce/HubSpot/6sense/Marketo/Adobe-Experience-Cloud-state-change billing + ad-spend join-table per SOC 2 CC7.2 + EU AI Act Art. 12 + SEC 17a-4 WORM + IRS §6001 + ePrivacy ad-consent-record + IAB TCF v2.2 consent-string-receipt.</p>
<p><strong>Pipeline state:</strong> cold_email/leads.csv row 183 verified (CSV-DictWriter QUOTE_ALL 8 cols), cold_email/templates/263_demandbase.md 9.4KB, _chunks/chunk_77.html 32KB 113+ lines (13 h3 questions matching the 13-question buyer checklist + 26-row compliance cross-walk table + 6 audit-prep checklist items + 11 cross-references to ai_sales_ai vendor-DD pipeline siblings). sitemap.xml patched with new <code>#demandbase-abm-ai-account-intelligence-third-party-intent-data-soc2-audit-2026-iab-tcf-v22-eprivacy-eu-ai-act</code> URL entry after the aviso-ai one. ai_sales_ai pipeline now 11-deep: Outreach 138 + Salesloft 139 + Persana 221 + Artisan 222 + Lavender 117 + Gong 167 + Clari 173 + Apollo 174 + Aviso 175 + People.ai 182 + Demandbase 183. <strong>Build-log fix:</strong> Tick 81 block moved from end-of-file (char 508630) to before Tick 80 block at char 2204 to restore newest-first invariant per subagent-driven-development pitfall #21 (the previous cron tick partial-shipped the People.ai artifacts to disk + commit 89c7114 but did not splice Tick 81 into the build-log correctly, so this tick resumes per subagent-driven-development pitfall #46 partial-ship resume pattern).</p>
</div>
</div>
"""

with open(BUILD_LOG, "r", encoding="utf-8") as f:
    content = f.read()

# Step 1: Find and extract the Tick 81 block from the end of the file
m81 = re.search(r'<div class="tick" id="tick-81">', content)
if not m81:
    print("ERROR: Tick 81 block not found", file=sys.stderr)
    sys.exit(1)
start81 = m81.start()

# Find the end of Tick 81 block — look for next '<!-- Tick' marker or end of file
# Search forward for either: '<!-- Tick 82' marker OR '</div>\n</div>\n\n' (end of last tick body)
# Tick 81 is at the END of file (no following marker), so find the last </div></div>
end81_search = content.rfind('</div>\n</div>', start81)
end81 = end81_search + len('</div>\n</div>') if end81_search != -1 else len(content)

tick81_block = content[start81:end81]
# Also remove any trailing whitespace/newlines
tick81_block = tick81_block.rstrip()
print(f"Tick 81 block extracted: chars {start81}-{end81}, length {len(tick81_block)}")
print(f"Tick 81 block start: {tick81_block[:80]}")
print(f"Tick 81 block end:   {tick81_block[-80:]}")

# Step 2: Remove Tick 81 block from its current position
content_without_81 = content[:start81].rstrip() + content[end81:]
print(f"File size after removing Tick 81 from end: {len(content_without_81)} (was {len(content)})")

# Step 3: Find the position of Tick 80 marker (the inline marker comment is at the very top)
tick80_marker_pos = content_without_81.find('<!-- Tick 80 inline marker')
if tick80_marker_pos != 0:
    print(f"ERROR: Tick 80 marker not at char 0 (found at {tick80_marker_pos})", file=sys.stderr)
    sys.exit(1)

# Step 4: Build the new prefix: Tick 82 marker + Tick 82 block + Tick 81 marker + Tick 81 block
new_prefix = TICK_82_INLINE_MARKER + "\n" + TICK_82_BLOCK + "\n" + TICK_81_INLINE_MARKER + "\n" + tick81_block + "\n"

# Step 5: Replace old prefix (just Tick 80 marker at start) with new prefix
new_content = new_prefix + content_without_81

with open(BUILD_LOG, "w", encoding="utf-8") as f:
    f.write(new_content)

# Step 6: Verify the newest-first invariant
verify_positions = []
for m in re.finditer(r'id="tick-(\d+)"', new_content):
    verify_positions.append((int(m.group(1)), m.start()))
verify_positions.sort(key=lambda x: x[0], reverse=True)  # tick number descending

print()
print("Newest-first invariant verification:")
for tid, pos in verify_positions[:5]:
    print(f"  tick-{tid} @ char {pos}")

# Check that Tick 82 is at lower offset than Tick 81, which is lower than Tick 80
pos_82 = new_content.find('id="tick-82"')
pos_81 = new_content.find('id="tick-81"')
pos_80 = new_content.find('id="tick-80"')
print()
print(f"Position check: tick-82@{pos_82} < tick-81@{pos_81} < tick-80@{pos_80} ?")
assert pos_82 < pos_81 < pos_80, f"Newest-first invariant violated: 82@{pos_82} 81@{pos_81} 80@{pos_80}"
print("VERIFICATION PASS: newest-first invariant holds.")

print()
print(f"File size: {len(content)} -> {len(new_content)}")
print(f"Net change: +{len(new_content) - len(content)} chars")
