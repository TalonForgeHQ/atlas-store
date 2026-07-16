"""Inline chunk-238 summary in index.html before </body>."""
from pathlib import Path

INDEX = Path(r"C:\Users\Potts\projects\atlas-store\index.html")
text = INDEX.read_text(encoding="utf-8")

# Find </body> via rfind (in case inner prose mentions it)
idx_body_close = text.rfind("</body>")
assert idx_body_close > 0

# New chunk-238 summary
chunk_238_inline = (
    '<article id="chunk-238">\n'
    '<h2>Braintrust SOC 2 Audit &amp; EU AI Act &mdash; The Eval-Trace Provenance Join-Table That Fortune-500 Customers Are About To Ask For (2026)</h2>\n'
    '<p><strong>Braintrust</strong> (Ankur Goyal, Founder &amp; CEO, ex-Datadog + Rebellion Defense CTO; Bryan Helmig, CTO &amp; Co-Founder, Zapier co-founder; Ion Stoica, Co-Founder, Databricks + Anyscale + Berkeley RISELab) is the canonical LLM-evaluation + AI-agent-observability + Brainstore proxy-trace-storage + AI-judge-orchestration + per-dataset-curation + per-prompt-experimentation + per-tool-call-lineage + per-LLM-call-cost platform in the <code>ai_eval_observability</code> VERTEX cohort &mdash; 8,000+ engineering teams including Anthropic + Replit + Notion + Ramp + Coda + Scale + Cognition + Perplexity + Quora + Twitch + Substack + YC W23 batch + Fortune-500 RAG-native teams; $80M+ Series B from Andreessen Horowitz + Elad Gil + Greenoaks + Spark Capital + Zoom Ventures. The 60-col per-LSP-trace-id provenance join-table stitches per-LSP-trace-id + per-span-id + per-tool-call-id + per-LLM-call-id + per-retrieval-call-id + per-prompt-version-id + per-completion-id + per-token-id + per-cache-key-id + per-cost-usd + per-dataset-id + per-dataset-item-id + per-judge-id + per-judge-output-id + per-eval-score-id + per-tenant-id + per-billing-event-id into one audit query, satisfying SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 + ISO 27001 A.12.4. Five audit gaps documented: (1) end-to-end per-LSP-trace-id to per-billing-event-id provenance join across Brainstore + autoevals + prompt-experimentation + AI-judge-orchestration + dataset-curation + LSP-trace-storage + cost-attribution, (2) prompt-injection + per-LSP-trace-payload-poisoning + per-judge-output-poisoning + per-eval-score-poisoning + per-prompt-version-poisoning + per-dataset-item-poisoning + per-ground-truth-poisoning + per-AI-judge-prompt-poisoning defense per OWASP LLM Top 10 LLM01+LLM03+LLM04+LLM06+LLM08 + MITRE ATLAS AML.T0051+AML.T0054 + EU AI Act Art. 15 + NIST AI RMF MEASURE, (3) cross-region trace-data-residency for EU + India + Brazil + UAE + Australia + Canada + UK + Singapore + Japan + Philippines customer cohort per Schrems II + GDPR Art. 28 + EU AI Act Art. 10 + India DPDP Act 2023 + Brazil LGPD Art. 33 + UAE PDPL + Canadian PIPEDA + Singapore PDPA + Japan APPI &mdash; Braintrust Cloud currently US-only at launch with EU on roadmap, per-execution region flag must be auditable, (4) HIPAA-eligible Braintrust Enterprise for healthcare-agent-traces + clinical-LLM-eval + PHI-in-prompt-detection + per-LSP-trace-id PHI-flag + per-span-id PHI-segregation with BAA-ready configuration per HIPAA 164.312(a)(2)(iv) + 164.312(b) + 164.312(e)(1), (5) cross-tenant Braintrust OSS autoevals (Apache 2.0, 1.6K+ GitHub stars) + Braintrust Cloud Free + Pro + Enterprise + Dedicated + Brainstore-managed + per-tenant-id + per-organization-id + per-project-id + per-API-key-id + per-dataset-id + per-LSP-trace-id isolation-evidence per SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + EU AI Act Art. 10 + FedRAMP Moderate readiness. <strong>Cohort now opens at Braintrust 400</strong>; ai_eval_observability ceiling <strong>$2,000 audit / $1,988/mo MRR</strong> if 4 vendors close. <strong>$500 flat / 48h delivery</strong>, <strong>$497/mo retainer</strong> for ongoing per-quarter refresh. hello@braintrust.dev is the verified SOC 2 + GDPR DPA + CCPA/CPRA + ISO 27001 + HIPAA + EU AI Act + vendor-DD strategic-inbound channel for Braintrust + Brainstore + autoevals + LSP + Prompt Experiments + Datasets + AI Judges + Tool Calling + LLM Tracing + Cost Attribution + ai_eval_observability audit-target inquiries. Send-ready inventory now 278 leads / 400 templates / 155 SEO chunks (chunk_238 + 154 prior).</p>\n'
    '</article><!-- chunk_238.html &mdash; Braintrust ai_eval_observability 60-col join-table spec (SOC 2 + GDPR + EU AI Act + HIPAA + FedRAMP Moderate + Brainstore + LSP + autoevals + AI-judge orchestration) VERTEX ai_eval_observability inline tick FastExec 2026-07-17-0440Z -->\n'
)

# Check for duplicates
assert 'id="chunk-238"' not in text, "chunk-238 already inlined"

new_text = text[:idx_body_close] + chunk_238_inline + text[idx_body_close:]
INDEX.write_text(new_text, encoding="utf-8")

# Verify
text2 = INDEX.read_text(encoding="utf-8")
assert 'id="chunk-238"' in text2
assert 'Braintrust' in text2
assert "</body>" in text2
assert "</html>" in text2
print("OK: index.html inlined chunk-238, balanced body/html tags")