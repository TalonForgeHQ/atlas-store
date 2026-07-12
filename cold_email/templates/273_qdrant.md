# Qdrant — Open-Source Vector Database SOC 2 + EU AI Act Annex III 4 Audit

**To:** info@qdrant.com
**From:** Atlas Audit Prep — Talon Forge
**Subject:** Quick Qdrant SOC 2 + EU AI Act audit-prep question (5 min)

---

Hi Andrey / André / Qdrant team,

I've been mapping the vector-database audit surface that enterprise AI teams are about to get asked for in SOC 2 + ISO 42001 + EU AI Act Annex III 4 + Art. 12 + Art. 53(d) vendor-DD cycles. Qdrant is a different case from Pinecone because the surface spans open-source Apache-2.0 deployments, Qdrant Cloud, Qdrant Hybrid Cloud, Qdrant Enterprise, HNSW graph mutation, quantization, sparse vectors, BM25, hybrid search, payload filters, snapshots, replication, backup export and downstream RAG/agent state changes.

**5 audit gaps I'm seeing in the public artifacts** (each one maps to a real evidence table a regulated buyer will ask for):

1. **Vector write → HNSW graph mutation → downstream LLM action provenance.** A buyer needs one join-table from `vector_id` to `collection_id` to `hnsw_graph_mutation_id` to `payload_filter_decision_id` to `hybrid_search_query_id` to `embedding_call_id` to `llm_call_id` to `downstream_state_change_id` — not separate logs in Qdrant, the embedding provider and the app server.

2. **Sparse+dense hybrid-search score explainability.** When Qdrant blends dense vectors, sparse vectors and BM25/payload terms, the auditor will ask which signal actually drove the retrieval. The evidence needs per-query score components, ranking deltas, payload-filter allow/deny decisions and the final RAG chunk IDs.

3. **Apache-2.0 OSS + Qdrant Cloud license/provenance split.** The open-source repo is Apache-2.0, but an enterprise deployment often combines OSS server, Qdrant Cloud control plane, Qdrant Hybrid Cloud and customer plugins. EU AI Act Art. 53(d) + ISO 42001 buyers will ask for a clean OSS/proprietary/control-plane provenance map.

4. **Cross-tenant isolation in Cloud + Hybrid Cloud.** Collection-level ACLs, API keys, payload filters, VPC peering, snapshots, replication, backups and customer-managed Kubernetes/on-prem deployments all need per-tenant evidence. "We isolate tenants" is not enough for SOC 2 CC6.1 + GDPR Art. 28 + EU AI Act Art. 10.

5. **WORM retention for vector mutations and retrieval decisions.** SOC 2 and EU AI Act Art. 12 require record-keeping. Buyers will ask whether vector upserts/deletes, HNSW rebuilds, quantization jobs, snapshot exports and downstream LLM calls can be exported to S3 Object Lock / equivalent WORM storage for 7-year retention.

**Offer:** $500 / 48h audit-prep engagement that produces the Qdrant-specific 17-column vector provenance join-table, the 10-column hybrid-search score-explainability table, the 9-column Art. 53(d) OSS/proprietary provenance table, the 12-column per-tenant isolation-evidence export, and the 14-question buyer checklist for your next regulated enterprise vendor-DD cycle. Or a 30-min call if you'd rather see the gap map first.

— Atlas Audit Prep
Talon Forge · talonforge.io/atlas-store

P.S. I just mapped Pinecone as the managed-vector-db sibling; Qdrant is the open-source + hybrid-cloud sibling. The two gap maps are complementary, not interchangeable.
