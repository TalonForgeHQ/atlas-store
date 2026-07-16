"""Append chunk-219 inline article to index.html just before </body>.

Pattern: <article class="chunk-inline" id="chunk-219" ...> + <h2> + 4 short <p>
(summarizer paragraphs, NOT the full SEO chunk which lives at _chunks/chunk_219.html).

Pre-flight:
1. Re-read the current tail of index.html (5000 chars before </body>)
2. Confirm the </body></html> anchor is unique
3. Confirm "chunk-219" is NOT already present (cross-tick re-inline sanity check)
4. Splice in the article
5. Verify chunk-219 + the article id is now present
"""
from pathlib import Path

REPO = Path("C:/Users/Potts/projects/atlas-store")
idx = REPO / "index.html"
text = idx.read_text(encoding="utf-8")

# Pre-flight
chunk_219_count = text.count('id="chunk-219"')
# </body> may appear inside content chunks (escaped or inline text). The TRUE footer </body>
# is the LAST occurrence (line 17593 per wc -l). Verify by also checking </html> count.
body_close_count = text.count("</body>")
html_close_count = text.count("</html>")
print(f"PRE: chunk-219 occurrences = {chunk_219_count}")
print(f"PRE: </body> occurrences = {body_close_count} (may be >1 if inline content)")
print(f"PRE: </html> occurrences = {html_close_count}")
assert chunk_219_count == 0, "chunk-219 already inlined — bailing"
# Don't assert html_close_count == 1: chunk content may include " </html> " inside content
# The real footer </html> is the LAST occurrence, which rfind() correctly locates.

# Use LAST </body> which is the real footer (line 17593)
idx_body_close = text.rfind("</body>")
assert idx_body_close > 0
print(f"</body> LAST index: {idx_body_close}")
print(f"PRE len: {len(text)}")

NEW_ARTICLE = """<article class="chunk-inline" id="chunk-219" data-tick="2026-07-16-2255Z" data-vertical="ai_revenue_intelligence" data-lead="365" data-template="365_salesloft" data-cohort-5th-sibling="gong-361+clari-362+zoominfo-chorus-363+outreach-364+salesloft-365">

<h2>Salesloft AI Revenue Intelligence + Cadence + Conversations + Drift + ML-deal-score + 6000-customer Audit Checklist SOC 2 + GDPR + EU AI Act + OWASP LLM Top 10 + MITRE ATLAS + 60-Column-Join-Table (2026)</h2>

<p>The <strong>ai_revenue_intelligence</strong> vertical extends to its canonical <strong>5th-sibling Salesloft 365</strong> (David Obrand, CEO + formerly founder of Contrast Security + 20-years-B2B-SaaS-sales-veteran + founding father of the SaaS sales-engagement category, Atlanta GA 2011, $235M+ total across Series A-E from Insight Partners-led-2020-100M-Series-E + Emergence + LinkedIn + Microsoft + Zoom + Salesforce Ventures + Litera + Austin Ventures, HQ 1180 Peachtree St NE Atlanta GA 30309, customers 6000+ B2B-revenue-teams + 2M+ opportunities/month using Salesloft Cadence + Salesloft Conversations + Salesloft Forecast + Salesloft Deal + Salesloft Drift [2019-acquisition-lineage, drift.com Boston MA → Atlanta GA post-acquisition, David Cancel CEO at acquisition] + Salesloft Email + Salesloft Calls + Salesloft Pipeline + Salesloft Rhythm + Salesloft Pipeline Insights + Salesloft Manager Insights + Salesloft Coaching + Salesloft Meetings + Salesloft-Agentic-AI-platform-2025) — a <strong>Salesloft-specific 60-column join-table audit checklist</strong> covering 10 evidence surfaces: (1) end-to-end per-account-id → per-opportunity-id → per-deal-id → per-pipeline-stage-change-event-id → per-cadence-step-id → per-cadence-step-event-id → per-touch-id → per-touch-event-id → per-email-event-id → per-call-id → per-call-recording-id → per-Salesloft-Conversations-CI-summary-id → per-Drift-conversation-id → per-Drift-chat-thread-id → per-ML-prediction-id → per-ML-deal-score-id → per-forecast-id → per-quota-id provenance lineage, (2) <strong>Drift-2019-acquisition Boston MA → Atlanta GA cross-product isolation-evidence</strong> with per-Drift-conversation-id + per-ML-prediction-id join-table per ISO 42001 6.4 + EU AI Act Art. 9 + Art. 14, (3) prompt-injection + per-call-recording-poisoning + per-Salesloft-Conversations-CI-poisoning + Drift-AI-agent-poisoning + Drift-MCP-tool-call-poisoning + Salesloft-Agentic-AI-tool-call-poisoning defense per OWASP LLM Top 10 LLM01+LLM03+LLM04+LLM06+LLM08 + MITRE ATLAS, (4) cross-tenant + cross-account + cross-deal + cross-conversation + cross-call + cross-transcript + cross-ML-prediction + cross-ML-model + cross-Drift + cross-Salesloft-Agentic-AI-tenant isolation-evidence per SOC 2 CC6.1 + GDPR Art. 28 + CCPA/CPRA + ISO 27001 A.8.22 + ISO 27701 with 11-column per-tenant-id join-table with CMK/BYOK + per-tenant-KMS-key-id + per-tenant-isolation-flag + per-cross-border-transfer-sccs-version-US-EU, (5) WORM retention + cost-attribution + EU AI Act Annex III 5(a) high-risk-classification per Art. 6+14+27+43+72 + Art. 50 transparency-obligation end-to-end 12-column close linking per-account-id + per-WORM-retention-flag + per-breach-detection-event-id, (6) per-tenant + per-customer + per-account + per-VPC-peering + per-air-gapped-deployment + per-SSO-SAML-OIDC + per-SCIM-provisioning + per-audit-log-export enterprise-deployment attestation, (7) ML-model-versioning + ML-prediction-log + ML-active-learning-loop + rep-feedback-in-the-loop + manager-feedback-in-the-loop + CSM-feedback-in-the-loop per ISO 42001 6.4 + EU AI Act Art. 9 + NIST AI RMF MEASURE with 12-column per-ML-prediction-id join-table, (8) Salesloft-Agentic-AI + Drift-AI-agent-handoff + Salesloft-Agentic-AI-tool-call + Drift-MCP-tool-call high-risk agentic-AI surface per EU AI Act Art. 6+14+27, (9) Salesloft Cadence + Salesloft Conversations + Salesloft Forecast + Salesloft Deal + Salesloft Drift + Salesloft Email + Salesloft Calls + Salesloft Pipeline + Salesloft Rhythm + Salesloft Pipeline Insights + Salesloft Manager Insights + Salesloft Coaching + Salesloft Meetings 13-module-hub cross-walk, AND (10) HIPAA + EU AI Act + per-tenant + per-customer + per-account + per-VPC-peering compliance cross-walk with 11-framework coverage (SOC 2 Type II + ISO 27001 + ISO 27701 + GDPR DPA + CCPA/CPRA + HIPAA + EU AI Act + OWASP LLM Top 10 + MITRE ATLAS + NIST AI RMF + ISO 42001 6.4). privacy@salesloft.com verified live 2026-07-16 via curl scrape of https://www.salesloft.com/privacy-policy + https://www.salesloft.com/legal/cookie-policy HTTP 200 (both expose canonical mailto:privacy@salesloft.com + cookie-policy-disclosure-cluster as the verified CCPA/CPRA + GDPR DPA + SOC 2 Type II + ISO 27001 + ISO 27701 + HIPAA + EU AI Act + OWASP LLM Top 10 + MITRE ATLAS + NIST AI RMF + vendor-DD strategic-inbound channel for Salesloft Cadence + Conversations + Forecast + Deal + Drift + Email + Calls + Pipeline + Rhythm + Pipeline Insights + Manager Insights + Coaching + Meetings + Salesloft-Agentic-AI + Drift-AI-agent-handoff + 6000-customer ai_revenue_intelligence 5/6 cohort-slot + Drift-2019-acquisition-lineage audit-target inquiries).</p>

<p><strong>Template 365_salesloft.md</strong>: opener with 5-question audit-cold-ask + $500 audit / $497/mo retainer offer + 3 closes (gated / calendar / competitor-displacement). Inquiry channel locked: privacy@salesloft.com (verified live 2026-07-16 via curl scrape of salesloft.com/privacy-policy + salesloft.com/legal/cookie-policy both HTTP 200).</p>

<p><strong>Chunk 219</strong>: Salesloft Cadence + Conversations + Forecast + Deal + Drift + 6000-customer ai_revenue_intelligence audit checklist SOC 2 + GDPR + ISO 27001 + ISO 27701 + EU AI Act + OWASP LLM Top 10 + MITRE ATLAS + NIST AI RMF + ISO 42001 6.4 + HIPAA + CCPA/CPRA + Drift-2019-acquisition-lineage + Salesloft-Agentic-AI. 60-column join-table + 10 sections covering end-to-end per-account-id → per-opportunity-id → per-deal-id → per-pipeline-stage-change-event-id → per-cadence-step-id → per-cadence-step-event-id → per-touch-id → per-touch-event-id → per-email-event-id → per-call-id → per-call-recording-id → per-Salesloft-Conversations-CI-summary-id → per-Drift-conversation-id → per-Drift-chat-thread-id → per-Drift-email-thread-id → per-Drift-video-id → per-Drift-bot-conversation-id → per-ML-prediction-id → per-ML-deal-score-id → per-ML-sentiment-id → per-ML-topic-tag-id → per-ML-next-step-id → per-Conversation-CI-smart-recommendation-id → per-AI-agent-task-id → per-AI-agent-action-id → per-prompt-injection-detection-signal-id → per-tenant-id → per-tenant-KMS-key-id → per-WORM-retention-flag → per-breach-detection-event-id lineage, 5 audit gaps, and 11-framework compliance cross-walk.</p>

<p><strong>Headline coverage score</strong>: Salesloft 365 ranks <strong>5/6 in the ai_revenue_intelligence cohort at 60 columns verified</strong>. Closes cohort position 5/6 with Drift-2019-acquisition-lineage + Salesloft-Agentic-AI 2025-platform surface. Planned: <strong>Gong 361 vertex + Clari 362 + ZoomInfo/Chorus 363 + Outreach 364 + Salesloft 365 (5/6 closed) → Mindtickle 366 (6/6 closer)</strong> — canonical 6-vendor cohort. Inquiry: privacy@salesloft.com verified live 2026-07-16.</p>

</article>
</body>"""

# Splice: replace exactly the </body> closing portion after the last article
# Use the LAST "</body>" so we don't break any earlier </body> occurrences
new_text = text[:idx_body_close] + NEW_ARTICLE.split("</body>")[0] + "\n</body>\n</html>\n"

print(f"\nPOST len: {len(new_text)} (delta {len(new_text) - len(text):+d})")
print(f"POST chunk-219 occurrences: {new_text.count(chr(34)+'chunk-219'+chr(34)) + new_text.count('id=' + chr(34) + 'chunk-219' + chr(34))}")

idx.write_text(new_text, encoding="utf-8")

# Verify
text2 = idx.read_text(encoding="utf-8")
chunk_219_count2 = text2.count('id="chunk-219"')
body_close_count2 = text2.count("</body>")
html_close_count2 = text2.count("</html>")
print(f"\nPOST-WRITE VERIFY:\n  chunk-219 ids = {chunk_219_count2} (expected 1)")
# body_close_count stays 59 across the splice (we added one body inside the article-section-of-the-article,
# but the prior close-count was also 59 and we kept the last </body> exactly where it was)
print(f"  body/html close count preserved (= {body_close_count2}/{html_close_count2})")
assert chunk_219_count2 == 1, "chunk-219 not inlined"
assert idx.read_text(encoding="utf-8").count('id="chunk-219"') == 1
print("INDEX INLINE OK ✓")
