# Lead 1057 — LanceDB (lancedb.com — multimodal lakehouse for AI)

## First-party verification

- **Real vendor + product:** the first-party homepage title is “LanceDB | Multimodal Lakehouse for AI,” and its hero describes LanceDB as “the AI-native Multimodal Lakehouse.”
- **Founder:** the first-party Chang She author page identifies **Chang She — CEO and Co-Founder of LanceDB**. The June 24, 2025 Series A post says, verbatim, “Four years ago my co-founder Lei and I asked a simple question,” establishing the two-founder origin without inferring Lei’s surname or title.
- **Open-source foundation:** the first-party funding post calls Lance “the new open source standard for AI data” and states that open-source packages had been downloaded more than 20 million times as of June 2025. GitHub’s first-party repository API describes `lancedb/lancedb` as a “Developer-friendly OSS embedded retrieval library for multimodal AI” (Apache-2.0; 10,964 stars verified 2026-07-23) and `lance-format/lance` as an “Open Lakehouse Format for Multimodal AI” implemented in Rust (Apache-2.0; 6,838 stars).
- **Enterprise surface:** first-party docs say LanceDB Enterprise is a “petabyte-scale (and beyond), distributed multimodal lakehouse platform,” supports private deployment, and uses the same Lance format and table model as LanceDB OSS.
- **Commercial route:** first-party docs publish `contact@lancedb.com`; the homepage and `/contact` publish a Contact Sales form. Nothing was submitted.
- **Security posture:** first-party security docs state “LanceDB Enterprise maintains high security standards with SOC 2 Type II, HIPAA, and GDPR compliance.” The first-party Trust Center independently lists SOC 2 Type 2, HIPAA, and GDPR.

## 5-WEDGE non-overlap rubric vs Pinecone 1050 + Weaviate 1051 + Qdrant 1052 + Zilliz 1053

1. **Multimodal lakehouse, not vector-database-only:** LanceDB unifies curation, feature engineering, search/retrieval, and model training in one data layer. That is distinct from Pinecone’s managed-serverless retrieval plane, Weaviate’s AI-native vector infrastructure, Qdrant’s Rust-native vector engine, and Zilliz Cloud + Milvus.
2. **Lance open format + versioned table:** raw bytes, metadata, embeddings, features, and governance artifacts stay together in a versioned multimodal table with branching, tagging, rollback, and no duplicate data. The unique audit join is table-version-to-retrieval-to-training, not collection-only retrieval.
3. **Embedded OSS → private Enterprise continuity:** LanceDB OSS is an embedded retrieval library in Python, TypeScript, and Rust; LanceDB Enterprise scales the same Lance table model into distributed private deployments. This local-to-private continuity differs from the cohort’s managed-cloud and standalone-server patterns.
4. **Training-data plane:** homepage receipts include up to 70% MFU, 100B+ rows per table, and 100K+ QPS; first-party product copy explicitly joins retrieval to training-data curation and GPU feeding. No prior sibling owns training-data version provenance as its primary wedge.
5. **Multimodal production evidence + compliance:** the first-party Series A post names Runway, Midjourney, and Character.ai, “tens of billions of vectors,” and petabytes of training data; security docs add SOC 2 Type II, HIPAA, GDPR, strict account isolation, and encryption at rest.

## 22-column evidence-gap map

`tenant_id + lance_table_uri + table_version + branch_or_tag + source_blob_id + row_id + feature_version + embedding_model_version + vector_index_id + full_text_index_id + metadata_filter + query_id + reranker_id + candidate_rank + retrieved_context + prompt_version + tool_call_id + agent_action_id + training_dataset_version + human_override + deletion_state + audit_export_id`

## Cohort and commercial status

- **Role:** CLOSER #5/5 (`closer-5-of-5`) after Pinecone 1050, Weaviate 1051, Qdrant 1052, and Zilliz 1053.
- **Offer:** $500/48h fixed-scope evidence-gap map, $497/month refresh, or $2,000 five-vendor benchmark.
- **Route:** `mailto:contact@lancedb.com` or `FORM:https://www.lancedb.com/contact`.
- **Status:** queued_not_sent; SMTP/form gated; no email/form submitted; $0 sent / $0 received.

## Claim exclusions

No founding year, HQ city, Lei surname/title, current employee count, or certification beyond the exact first-party SOC 2 Type II/HIPAA/GDPR wording is asserted.
