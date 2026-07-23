Subject: Qdrant payload filter + named vector audit

Hi {{first_name}},

Following our note on the Rust-native Qdrant vector search engine —

The cohort-unique wedge for Qdrant vs Pinecone / Weaviate / Zilliz /
LanceDB is **payload filtering + named vectors + quantization
config**. Three questions before we sign a $500/48h scope:

1. **Named vectors** — does qdrant/qdrant 33,519★ ≥ 1.10 support
   multiple named vectors per point (text + image + code embeddings,
   one record) with per-vector index params? We need a verified recipe
   for the multi-modal agent-retrieval use case.

2. **Payload filter hits** — does qdrant support nested-key payload
   filters (`user.tenant_id == "X" AND chunk_id IN (...)`) with
   per-key indexes, and at what cardinality threshold does the
   payload index start to dominate query latency?

3. **Scalar / product / binary quantization** — does qdrant support
   per-vector quantization config, and what's the rerank-from-full-
   precision pattern recommended for ≥ 99% recall parity?

For one production agent-retrieval use case (tenant-scoped, multi-
modal, ~1M queries/day), we'll deliver a 22-column evidence-gap map
covering named_vector_id + payload_index_id + filter_condition_id +
quantization_config_id + hybrid_search_query_id + audit_export_id.

$500/48h fixed-scope, $497/mo quarterly refresh, $2,000 four-vendor
benchmark (Pinecone + Weaviate + Qdrant + Zilliz). Reply if useful.

— Atlas
Qdrant SIBLING #3/5 ai_agent_vector_memory
https://qdrant.tech/contact
