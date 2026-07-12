# Pinecone Systems — Managed Vector Database SOC 2 + EU AI Act Annex III 4 Audit

**To:** privacy@pinecone.io (cc: security@pinecone.io)
**From:** Atlas Audit Prep — Talon Forge
**Subject:** Quick Pinecone SOC 2 + EU AI Act Annex III 4 audit-prep question (5 min)

---

Hi Edo / Pinecone privacy team,

Congrats on the Pinecone serverless milestone — looking at your public trust page, the architecture (vector-upsert + vector-mutation + vector-delete + vector-namespace-isolation + vector-tenant-isolation + vector-API-key-rotation + vector-RBAC-role-change + vector-SSO/SAML-assertion + vector-audit-log-export + vector-BYOK-key-rotation + vector-CMEK-key-rotation + downstream-OpenAI/Anthropic/Cohere/Hugging-Face-embeddings-call + downstream-LLM-call + downstream-Snowflake/Databricks/BigQuery/Redshift/Postgres-state-change + downstream-S3/GCS/Azure-Blob-state-change) is the kind of system that lands in front of a SOC 2 + ISO 42001 + EU AI Act Annex III 4 + Art. 12 + Art. 14 + Art. 50 + Art. 53(d) + OWASP LLM Top 10 + HIPAA + GDPR DPA + CCPA/CPRA vendor-DD questionnaire.

**5 audit gaps I'm seeing in the public artifacts** (each one is a real downstream-state-change that an audit-prep buyer will ask for a 17-column provenance join-table for):

1. **End-to-end vector-mutation-to-downstream-state-change provenance** — per-vector-upsert + per-vector-mutation + per-vector-delete + per-vector-namespace-isolation-event + per-vector-tenant-isolation-event + per-vector-API-key-rotation + per-vector-RBAC-role-change + per-vector-SSO-SAML-assertion + per-vector-audit-log-export-event + per-vector-BYOK-key-rotation + per-vector-CMEK-key-rotation + per-downstream-OpenAI/Anthropic/Cohere/Hugging-Face-embeddings-call + per-downstream-LLM-call + per-downstream-Snowflake/Databricks/BigQuery/Redshift/Postgres-state-change + per-downstream-S3/GCS/Azure-Blob-state-change — SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4.

2. **Sparse-dense-index + hybrid-search + RAG-pipeline training-corpus license-provenance** — Pinecone sparse-dense-index + Pinecone metadata-filtering + Pinecone hybrid-search + Pinecone semantic-search + Pinecone RAG-pipeline + Pinecone AI-agent-memory training-corpus + fine-tune license-provenance per EU AI Act Art. 53(d) GPAI training-data transparency + Art. 53(1)(b) copyright-summary + Art. 53(2) publicly-available-summary + ISO 42001 6.1.4 + Apache-2.0 license provenance Annoy-library.

3. **Prompt-injection + jailbreak detection on vector ingest + metadata filter + RAG retrieval** — per OWASP LLM Top 10 LLM01 + LLM06 + NIST AI RMF MEASURE, vector-upsert-attributes + vector-mutation-attributes + vector-delete-attributes + metadata-filtering-input + sparse-dense-index-input + hybrid-search-input + semantic-search-input + RAG-pipeline-input are the canonical injection vectors.

4. **Cross-tenant Pinecone SaaS isolation-evidence** — per SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + EU AI Act Art. 10, the namespace-isolation + tenant-isolation + BYOK + CMEK + KMS + SSO/SAML + RBAC evidence chain is what enterprise vendor-DD teams will ask for in writing.

5. **Cost-attribution + WORM join-table** — per SOC 2 CC7.2 + EU AI Act Art. 12 + SEC 17a-4 WORM + IRS §6001 + EU AI Act Annex III 4 high-risk-classification per Art. 6 + 14 + 27 + 43 + 72 + Aug 2026 GPAI enforcement, the per-vector-upsert + per-vector-mutation + per-vector-delete + per-downstream-embeddings-call + per-downstream-LLM-call + per-downstream-warehouse-state-change billing + cost-attribution join-table is the audit-prep buyer's first ask.

**Offer:** $500 / 48h audit-prep engagement that produces the 17-column provenance join-table spec + the 9-column Art. 53(d) GPAI training-data-summary + the 10-column per-decision human-oversight log + the 12-column per-tenant cross-tenant isolation-evidence + the 11-column WORM billing join-table + the 14-question buyer checklist for your next vendor-DD cycle. Or a 30-min call if you'd rather see the gap map first.

— Atlas Audit Prep
Talon Forge · talonforge.io/atlas-store

P.S. If you'd like the ai_vector_db vertical cross-walk (Pinecone + Weaviate + Chroma + Qdrant + Milvus + LanceDB + Vespa), I can send that separately.