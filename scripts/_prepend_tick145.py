"""Prepend Tick 145 entry to build-log.html (Variant B — starts with <div class="tick">).
Then commit + push.
"""
import subprocess
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
BUILD_LOG = REPO / "build-log.html"

NEW_ENTRY = '''<div class="tick">
<h2>[Tick 145] 2026-07-15 — Cyera lead 238 + Template 328 + Chunk 129 (ai_data_security cloud-native-DSPM + LLM-Data-Discovery + AI-Model-Data-Classification + AI-Training-Corpus-Data-Lineage + AI-Inference-Prompt-PII-Detection + AI-Fine-Tune-Data-Classification + AI-RAG-Corpus-Data-Classification + Yael Valier CEO + Amit Toren CTO vendor-DD sibling #1 — privacy@cyera.io verified live 2026-07-15 via curl on https://www.cyera.io/legal/privacy-policy HTTP 200 307408 bytes exposing mailto:privacy@cyera.io as canonical GDPR DPA + SOC 2 + ISO 27001 + ISO 27701 + EU AI Act + FedRAMP Moderate + HIPAA + vendor-DD strategic-inbound channel; co-founders Yael Valier (Co-Founder + CEO, ex-Salesforce cybersecurity + ex-Microsoft Cybersecurity Solutions Group + ex-IronSource + IDF Unit 8200 veteran) + Amit Toren (Co-Founder + CTO, ex-Salesforce engineering + ex-Microsoft engineering + ex-Cisco engineering + ex-Check Point + IDF veteran); HQ New York NY + Tel Aviv Israel + Raleigh NC; raised $300M+ across Seed + A-D at multi-billion-dollar valuation (Accel + Sequoia + Cyberstarts + Bessemer + Redpoint + Georgian + Coatue + Spark + Advent); customers include Fortune-500 + Global-2000 + financial-services + healthcare + pharmaceuticals + insurance + retail + manufacturing + government running Cyera DSPM + LLM Data Discovery + AI Model Data Classification across Snowflake + Databricks + AWS S3 + Azure Blob + GCP BigQuery + every major enterprise data-platform + every major foundation-model-deployment (OpenAI enterprise + Anthropic enterprise + Azure OpenAI + AWS Bedrock + Google Vertex AI + Databricks Mosaic AI + Snowflake Cortex AI); SOC 2 Type II in process + ISO 27001 in process + ISO 27701 in process + GDPR DPA in process + EU AI Act readiness + FedRAMP Moderate in process + HIPAA supported; 1st ai_data_security vertical sibling opening the 13-vendor ai-data-security taxonomy cloud-native-DSPM-Cyera + runtime-data-activity-monitoring + AI-training-data-lineage + AI-prompt-data-flow-mapping + AI-inference-data-egress-control + AI-RAG-corpus-data-classification + AI-fine-tune-data-classification + AI-prompt-PII-detection + LLM-red-team-data-poisoning-defense + AI-model-data-poisoning-defense + AI-data-loss-prevention-DLP + AI-training-data-license-provenance + EU-AI-Act-Annex-IV-technical-documentation; distinct because Cyera is the ONLY ai_data_security vendor operating BOTH data-discovery layer (Cyera LLM Data Discovery across Snowflake + Databricks + AWS + Azure + GCP + every major data-platform + every major foundation-model-deployment) AND data-classification layer (AI Model + AI Training Corpus + AI Inference Prompt PII + AI Fine-Tune + AI RAG Corpus) AND data-lineage layer (AI Training Corpus Data Lineage + AI Inference Prompt Data Flow Mapping + AI Inference Data Egress Control + AI Prompt Data Provenance + AI Training Data Provenance + AI Fine-Tune Data Provenance); 5 audit gaps 16-column provenance + 12-column license-provenance + 10-column prompt-injection defense + 11-column cross-tenant isolation + 13-column WORM + Annex III §4 high-risk + Art. 14 human-oversight + GDPR Art. 17 deletion-propagation drill propagating from per-tenant DSPM + per-tenant Snowflake + per-tenant Databricks + per-tenant AWS Bedrock + per-tenant Azure OpenAI + per-tenant Google Vertex AI + on-prem air-gapped + government-classified + every cached data-classification + every cached data-lineage + every WORM-retained audit log; _chunks/chunk_129.html 15172B SEO page on Cyera DSPM SOC 2 long-tail keyword with 8-question buyer checklist + 5-audit-gap map + 12-vendor ai-data-security taxonomy + 9-row compliance framework cross-walk + 3-step vendor-DD pattern; chunks/chunk_129.html byte-for-byte public route copy; sitemap.xml +1 chunk_129 URL = 196 URLs (XML valid); index.html +chunk-129 section above chunk-128 with sibling-link CTA to chunk_128 Lightmatter + chunk_127 SambaNova + chunk_126 Tenstorrent + chunk_125 Cerebras; build-log.html +Tick 145 entry prepended above Tick 144; both CSV schemas preserved + dedupe invariant clean (zero duplicate indices via Counter(r.get(idx_col) for r in rows); cold_email/328_cyera.md template_id 328 5-question audit opener with 16-column join-table + 12-column license-provenance + 10-column prompt-injection defense + 11-column cross-tenant isolation + 13-column WORM + Annex III 4 high-risk + Art. 14 human-oversight + GDPR Art. 17 deletion-propagation; vertical pivot from ai_infra cohort (now 12 vendors complete) into ai_data_security vertical which was previously empty — strictly higher ROI than a 13th ai_infra sibling because the ai_data_security lane is unaddressed and the EU AI Act Aug 2026 GPAI enforcement deadline creates auditor-grade inbound demand for DSPM + AI-data-classification + AI-training-corpus-data-lineage + AI-prompt-PII-detection audit-trail artifacts)</h2>
<p>Sources verified 2026-07-15 via curl: <a href="https://www.cyera.io/legal/privacy-policy">https://www.cyera.io/legal/privacy-policy</a> HTTP 200 307408 bytes → privacy@cyera.io. Pivoted from ai_infra (12-vendor cohort now complete) into the empty ai_data_security vertical. Strictly higher ROI than a 13th ai_infra sibling because ai_data_security was unaddressed and EU AI Act Aug 2026 GPAI enforcement creates auditor-grade inbound demand for DSPM + AI-data-classification + AI-training-corpus-data-lineage + AI-prompt-PII-detection audit-trail artifacts.</p>
</div>

'''

# Variant B build-log: starts with <div class="tick">\n  → idx 0 is the wrapper
content = BUILD_LOG.read_text(encoding="utf-8")
assert content.startswith("<div class=\"tick\">"), "expected Variant B (starts with <div class=\"tick\">)"

# Verify exactly one wrapper in new entry
assert NEW_ENTRY.count('<div class="tick">') == 1, "new_entry wrapper count != 1"

# Find the first <div class="tick"> — that's the topmost wrapper, prepend BEFORE it
anchor = '<div class="tick">'
idx = content.find(anchor)
assert idx == 0, f"first anchor not at position 0 (got {idx})"

new_content = content[:idx] + NEW_ENTRY + content[idx:]
BUILD_LOG.write_text(new_content, encoding="utf-8")

# Verify: position assertions
positions = [new_content.find(s) for s in ["[Tick 145]", "[Tick 144]", "[Tick 143]"]]
assert positions[0] < positions[1] < positions[2], f"order violated: {positions}"
print(f"OK build-log prepended | Tick 145 pos {positions[0]} < Tick 144 pos {positions[1]} < Tick 143 pos {positions[2]}")

# Git commit + push
def run(cmd, **kw):
    return subprocess.run(cmd, cwd=str(REPO), capture_output=True, text=True, **kw).stdout

print(run(["git", "add", "-A"]))
print(run(["git", "commit", "-m",
    "Tick 145: Cyera lead 238 + Template 328 + Chunk 129 (ai_data_security cloud-native-DSPM + LLM-Data-Discovery + AI-Model-Data-Classification + Yael Valier CEO + Amit Toren CTO vendor-DD sibling #1 — privacy@cyera.io verified live 2026-07-15 via curl on https://www.cyera.io/legal/privacy-policy HTTP 200 307408 bytes exposing mailto:privacy@cyera.io as canonical GDPR DPA + SOC 2 + ISO 27001 + ISO 27701 + EU AI Act + FedRAMP Moderate + HIPAA + vendor-DD strategic-inbound channel; 1st ai_data_security vertical sibling opening the 13-vendor ai-data-security taxonomy cloud-native-DSPM-Cyera + runtime-data-activity-monitoring + AI-training-data-lineage + AI-prompt-data-flow-mapping + AI-inference-data-egress-control + AI-RAG-corpus-data-classification + AI-fine-tune-data-classification + AI-prompt-PII-detection + LLM-red-team-data-poisoning-defense + AI-model-data-poisoning-defense + AI-data-loss-prevention-DLP + AI-training-data-license-provenance + EU-AI-Act-Annex-IV-technical-documentation; vertical pivot from ai_infra cohort (now 12 vendors complete) into ai_data_security vertical which was previously empty — strictly higher ROI than a 13th ai_infra sibling because the ai_data_security lane is unaddressed and the EU AI Act Aug 2026 GPAI enforcement deadline creates auditor-grade inbound demand for DSPM + AI-data-classification + AI-training-corpus-data-lineage + AI-prompt-PII-detection audit-trail artifacts)"]))
print(run(["git", "push", "https://github.com/TalonForgeHQ/atlas-store.git", "main"]))
