# Weaviate — Open-Source Vector Database SOC 2 + EU AI Act Annex III 4 Audit

**To:** legal@weaviate.io
**From:** Atlas Audit Prep — Talon Forge
**Subject:** Quick Weaviate SOC 2 + EU AI Act audit-prep question (5 min)

---

Hi Bob / Etienne / Weaviate team,

I've been mapping the vector-database audit surface that enterprise AI teams are about to get asked for in SOC 2 + ISO 42001 + EU AI Act Annex III 4 + Art. 12 + Art. 53(d) vendor-DD cycles. Weaviate is a different case from Pinecone and Qdrant because the surface spans open-source BSD-3-Clause deployments, Weaviate Cloud (WCD), Weaviate Enterprise, Weaviate Embedded, hybrid search (BM25 + dense + sparse), named vectors (per-property vectorization), ref2vec, generative-search modules, modular vectorizer integrations, multi-tenant collections with per-tenant RBAC, backup, replication, quantization (PQ + BQ + SQ) and HNSW.

**5 audit gaps I'm seeing in the public artifacts** (each one maps to a real evidence table a regulated buyer will ask for):

1. **Vector write → hybrid-search score component → generative-search prompt → downstream LLM action provenance.** A buyer needs one join-table from `vector_id` to `collection_id` to `tenant_id` to `named_vector_property` to `bm25_score + dense_score + sparse_score` to `generative_search_prompt_id` to `rag_module_call_id` to `vectorizer_call_id` to `embedding_call_id` to `llm_call_id` to `downstream_state_change_id` — not separate logs in Weaviate, the embedding provider, the LLM provider and the app server.

2. **Per-tenant multi-tenant RBAC + collection isolation evidence.** Weaviate Cloud + Enterprise support per-tenant collections with RBAC. Buyers will ask for per-tenant isolation evidence: collection ACLs, named-vector isolation, RBAC role changes, backup export, replication topology, vectorizer module isolation and customer-operated Kubernetes/on-prem isolation evidence.

3. **BSD-3-Clause OSS + Weaviate Cloud proprietary control-plane + vectorizer modules license/provenance split.** The open-source repo is BSD-3-Clause, but an enterprise deployment often combines OSS server, Weaviate Cloud control plane, Weaviate Enterprise and modular vectorizer integrations (OpenAI/Anthropic/Cohere/OctoAI/open-source). EU AI Act Art. 53(d) + ISO 42001 buyers will ask for a clean OSS/proprietary/module-provenance map.

4. **Prompt-injection + retrieval-source-poisoning + hybrid-search-score-manipulation + generative-search-prompt-poisoning detection.** When Weaviate blends BM25, dense vectors and sparse vectors and then feeds a generative-search module, the auditor will ask which signal actually drove the retrieval, what the generative-search prompt contained and whether any prompt-injection or retrieval-poisoning attempt was detected across the per-payload detection log.

5. **WORM retention for vector mutations, hybrid-search scoring and generative-search decisions.** SOC 2 and EU AI Act Art. 12 require record-keeping. Buyers will ask whether vector upserts/deletes, BM25 + dense + sparse scoring, generative-search calls, RAG-module calls, vectorizer calls, backup exports, replication events and downstream LLM calls can be exported to S3 Object Lock / equivalent WORM storage for 7-year retention.

**Offer:** $500 / 48h audit-prep engagement that produces the Weaviate-specific 18-column vector + hybrid-search + generative-search + vectorizer + downstream LLM provenance join-table, the 11-column per-tenant multi-tenant RBAC isolation-evidence export, the 9-column Art. 53(d) OSS/proprietary/module-provenance table, the 12-column prompt-injection/retrieval-poisoning detection-log table, and the 14-question buyer checklist for your next regulated enterprise vendor-DD cycle. Or a 30-min call if you'd rather see the gap map first.

— Atlas Audit Prep
Talon Forge · talonforge.io/atlas-store

P.S. I just mapped Pinecone as the managed-vector-db sibling + Qdrant as the open-source + hybrid-cloud sibling. Weaviate is the open-source + hybrid-search + generative-search + multi-tenant-RBAC sibling. The three gap maps are complementary, not interchangeable.
