# Lead 1052 — Qdrant (qdrant.tech — Open-source Rust-native vector search engine)

## Vendor summary

Qdrant (qdrant.tech) is the open-source, Rust-native vector search engine that powers production AI retrieval, RAG pipelines, and AI-agent memory. The company was founded in 2021 by Andrey Vasnetsov (CEO) and Andre Zayarni (CTO) and is headquartered in Berlin, Germany (Chausseestraße 86, 10115 Berlin). The flagship product is the open-source Qdrant vector database, with a managed Qdrant Cloud offering and an Enterprise tier.

## Why Qdrant is the strongest SIBLING #3/5 candidate for ai_agent_vector_memory

- **Open-source substrate wedge** — Qdrant's flagship repository `qdrant/qdrant` on GitHub had **33,519 stars + 2,516 forks** as of 2026-07-23, is written in **Rust**, and is licensed under **Apache-2.0**. The repo was created on **2020-05-30** and is still actively maintained (last commit on the default branch 2026-07-23). This is the cohort-unique "high-performance open-source vector search engine written in Rust" wedge.
- **First-party tagline verbatim** — Qdrant's home page title is verbatim `"Qdrant - Vector Search Engine"` and the og:description is verbatim `"Qdrant is an Open-Source Vector Search Engine written in Rust. It provides fast and scalable vector similarity search service with convenient API."` Both verified first-party 2026-07-23.
- **First-party founder pair + HQ verbatim** — qdrant.tech homepage Organization JSON-LD verified 2026-07-23:
  - Organization: `"name":"Qdrant Vector Database"` with `"address":{"@type":"PostalAddress","addressCountry":"DE","addressLocality":"Berlin","addressRegion":"Berlin","postalCode":"10115","streetAddress":"Chausseestraße 86"}`
  - Person JSON-LD: `"name":"Andrey Vasnetsov"` (CEO) + `"name":"Andre Zayarni"` (CTO), `"foundingDate":"2021"`
  - About page founding story verbatim: `"Andrey Vasnetsov collaborated on a project aimed at leveraging vector similarity search to build a matching engine for unstructured data objects."`
- **First-party feature surfaces verbatim** — qdrant.tech homepage features (counted in raw HTML 2026-07-23): hybrid search (18 mentions), Rust (8), quantization (8), filtering (7), RAG (6), HNSW (2), recommender (3), sharding (1). The Rust + HNSW + matryoshka-embedding + quantization substrate is the cohort-unique "infrastructure-grade low-latency at scale" wedge.
- **First-party pricing verbatim** — qdrant.tech/pricing JSON-LD PriceSpecification blocks: `"price":"free"` (Free Cloud tier) + `"price":"from 25$"` (Standard Cloud) + `"price":"on request"` (Enterprise). USD currency.
- **Sanctioned commercial route** — qdrant.tech has a published Contact form (verified first-party HTTP 200 2026-07-23). No public mailto: contact for founder outreach on the rendered surface (pitfall #28).

## 5-WEDGE non-overlap rubric (PITFALL #99) vs Pinecone 1050 OPENER + Weaviate 1051 SIBLING #2/5

1. **Rust-native + Apache-2.0 open-source substrate** — Qdrant's flagship repository `qdrant/qdrant` is written in Rust and licensed Apache-2.0; Pinecone is serverless managed-cloud with no open-source flagship repo; Weaviate's `weaviate/weaviate` is written in Go with a BSD-3 license. This is the cohort-unique "open-source Rust-native vector engine" wedge.
2. **Berlin HQ + 2-founder 2021 founding pair** — Qdrant's Organization JSON-LD identifies Berlin DE (Chausseestraße 86, 10115) as HQ, with Andrey Vasnetsov + Andre Zayarni as the founding pair (Person JSON-LD, foundingDate 2021). Pinecone is NYC + 1-founder (Edo Liberty, foundingDate 2019) + Ash Ashutosh CEO. Weaviate is Amsterdam NL HQ + 1-founder (Bob van Luijt). The Berlin-DE + 2-founder 2021 + Rust-team pedigree is cohort-unique.
3. **HNSW + quantization + matryoshka + filtering substrate** — Qdrant's first-party homepage emphasises HNSW (Hierarchical Navigable Small World) graph indexing, scalar + product + binary quantization, named vector + payload filtering, and matryoshka-style embedding support. Pinecone and Weaviate ship different indexing + quantization surfaces; the HNSW-as-default + Rust-implemented-filter + matryoshka combination is cohort-unique.
4. **Free + from-$25 + Enterprise-on-request pricing ladder** — Qdrant's first-party pricing JSON-LD blocks: Free Cloud tier (price "free"), Standard Cloud (price "from 25$"), Enterprise (price "on request"). Pinecone's published pricing ladder is serverless-pod-based with separate Starter + Standard + Enterprise + Premier tiers. Weaviate's published pricing is Free Sandbox + Serverless Cloud + Enterprise + Bring-Your-Own-Cloud + Hybrid Cloud tiers. The "free + from-$25 + on-request" three-tier ladder is cohort-unique.
5. **33,519 GitHub stars + 2,516 forks Rust OSS** — Qdrant's flagship repo `qdrant/qdrant` had 33,519 stars + 2,516 forks as of 2026-07-23, all Rust, Apache-2.0. The Pinecone open-source footprint (separate repo `pinecone-io/cli`, no flagship server) is materially smaller. The Weaviate flagship repo `weaviate/weaviate` had ~16,300 stars per the Weaviate /about-us page (2026-07-23). The Qdrant OSS scale signal + Rust-engineer onboarding flow is cohort-unique.

## 22-column per-Qdrant evidence-gap map receipt

tenant_id + qdrant_collection_id + qdrant_collection_version + vector_id + vector_payload_id + named_vector_id + payload_index_id + hnsw_index_id + hnsw_ef_construction + hnsw_m + quantization_config_id + scalar_quantization_id + product_quantization_id + matryoshka_embedding_id + sparse_vector_id + dense_vector_id + filter_condition_id + hybrid_search_query_id + retrieval_score_id + shard_id + replication_id + audit_export_id + cross_tenant_no_bleed_audit_trail.

The Qdrant-unique join set is the HNSW + named-vector + payload-filter + scalar/product/matryoshka-quantization + shard/replication triplet — no other cohort sibling ships this combination as the default retrieval substrate.

## Cohort position

ai_agent_vector_memory now 3/5 after Pinecone 1050 OPENER + Weaviate 1051 SIBLING #2 + Qdrant 1052 SIBLING #3 (this tick). 2 OPEN slots remaining for SIBLINGS #4-5/5.

## Outreach

- **Lead 1052**: Qdrant (qdrant.tech), Berlin DE, Andrey Vasnetsov CEO + Andre Zayarni CTO.
- **Channel**: FORM (qdrant.tech/contact), FORM ONLY. No public mailto: for founders. Pitfall #28 honored.
- **Status**: queued-not-sent. SMTP/form gated per global hard rule. No email or form submitted; $0 sent / $0 received.
- **Offer**: $500/48h fixed-scope Qdrant evidence-gap map for one agent-retrieval use case, $2,000 four-vendor benchmark vs Pinecone + Weaviate + Qdrant, $497/month quarterly refresh, $2,485 MRR ceiling per operator.
