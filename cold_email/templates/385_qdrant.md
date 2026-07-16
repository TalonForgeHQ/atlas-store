# Qdrant — Open-Source Vector Database Audit-Prep Template

**To:** info@qdrant.com
**From:** Atlas Audit Prep — Talon Forge
**Subject:** $500 audit, no deck — Qdrant vector-write → HNSW → hybrid-search → RAG lineage

> **Inquiry channel:** `info@qdrant.com` — verified live 2026-07-16 from Qdrant's official homepage, `https://qdrant.tech/` (HTTP 200; Organization JSON-LD exposes `info@qdrant.com` and founders Andrey Vasnetsov + Andre Zayarni).

---

Hi Andrey, Andre, and the Qdrant team,

Qdrant is the open-source vector-search sibling in our `ai_vector_db` audit cohort: Apache-2.0 server, Qdrant Cloud, Hybrid Cloud, HNSW, sparse+dense hybrid search, BM25, payload filters, quantization, snapshots, replication, and downstream RAG/agent state. The question is not whether each component logs events. It is whether an enterprise buyer can reconstruct one regulated decision across those seams without hand-joining exports from Qdrant, the embedding provider, and the application layer.

For a $500 / 48h audit-prep sprint, we test five concrete joins:

1. Can one `vector_id` be joined to `collection_id`, `upsert_event_id`, `hnsw_graph_mutation_id`, `embedding_model_version_id`, `hybrid_search_query_id`, `retrieval_result_id`, `rag_chunk_id`, `llm_call_id`, and `downstream_agent_action_id`?
2. When dense, sparse, BM25, and payload-filter signals are blended, can the final ranking be explained with score components, filter allow/deny decisions, and ranking deltas?
3. Can an auditor separate Apache-2.0 Qdrant OSS provenance from Qdrant Cloud, Hybrid Cloud, customer plugins, and control-plane changes in one release lineage?
4. Can Qdrant prove tenant isolation across API keys, collections, payload filters, snapshots, replication, VPC peering, and customer-managed Kubernetes or on-prem deployments?
5. Can vector mutations, deletes, HNSW rebuilds, quantization jobs, snapshot exports, retrieval decisions, and downstream LLM calls be exported to WORM storage with retention and deletion evidence attached?

If one of those joins breaks, the buyer usually finds it during SOC 2 CC6.1, GDPR Art. 28, ISO 42001, or EU AI Act Art. 10/12 vendor diligence — after the architecture is already in procurement. We deliver the gap map, a 17-column provenance join-table stub, a hybrid-search score-explainability table, a tenant-isolation evidence checklist, and a 30-minute walkthrough. If the first sprint is useful, the follow-on is $497/mo for the recurring evidence-reconstruction loop, including a 15-minute monthly control check.

**Simple next step:** reply `AUDIT` and we will send the redacted join-table stub, or reply `NOPE` and we will close the thread.

— Atlas Audit Prep
Talon Forge LLC · https://talonforge.io/atlas-store
Unsubscribe: atlas@talonforge.io

## 17-column vector provenance join-table

<table>
<thead><tr><th>#</th><th>Lineage column</th><th>Evidence question</th></tr></thead>
<tbody>
<tr><td>1</td><td>vector_id</td><td>Which source record was embedded?</td></tr>
<tr><td>2</td><td>collection_id</td><td>Which collection and tenant owned the vector?</td></tr>
<tr><td>3</td><td>upsert_event_id</td><td>When was the vector written or replaced?</td></tr>
<tr><td>4</td><td>embedding_model_version_id</td><td>Which model and version produced the embedding?</td></tr>
<tr><td>5</td><td>hnsw_graph_mutation_id</td><td>Which index mutation made it searchable?</td></tr>
<tr><td>6</td><td>quantization_job_id</td><td>Which quantization or compression job changed retrieval?</td></tr>
<tr><td>7</td><td>payload_filter_decision_id</td><td>Which filter allowed or denied the candidate?</td></tr>
<tr><td>8</td><td>hybrid_search_query_id</td><td>Which dense, sparse, or BM25 query requested it?</td></tr>
<tr><td>9</td><td>retrieval_result_id</td><td>What score and rank did Qdrant return?</td></tr>
<tr><td>10</td><td>reranker_decision_id</td><td>Did a reranker change the final order?</td></tr>
<tr><td>11</td><td>rag_chunk_id</td><td>Which chunk entered the application context?</td></tr>
<tr><td>12</td><td>prompt_version_id</td><td>Which prompt consumed the retrieved context?</td></tr>
<tr><td>13</td><td>llm_call_id</td><td>Which model call generated the response?</td></tr>
<tr><td>14</td><td>downstream_agent_action_id</td><td>Which agent action followed the retrieval?</td></tr>
<tr><td>15</td><td>tenant_isolation_event_id</td><td>What proves cross-tenant separation?</td></tr>
<tr><td>16</td><td>worm_retention_record_id</td><td>Where is the immutable retention record?</td></tr>
<tr><td>17</td><td>deletion_propagation_event_id</td><td>Did deletion propagate through index and backup copies?</td></tr>
</tbody>
</table>
