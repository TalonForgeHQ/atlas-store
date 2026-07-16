From: james@talonforge.io
To: info@qdrant.tech
Subject: Qdrant Rust-native vector search + Qdrant Cloud + HNSW — 5 questions before we route our vector-database audit cohort to you

Hi Qdrant team,

I'm James Potts, founder of Talon Forge. We run a 50-customer AI-agent audit practice (SOC 2 Type II + HIPAA + EU AI Act + OWASP LLM Top 10 + MITRE ATLAS coverage) and we're now sending our RAG-native + vector-database clients to Qdrant as the canonical Rust-native vector search engine + Qdrant Cloud managed-service surface — alongside Pinecone (managed-serverless) + Weaviate (open-source + WCD managed) + Chroma (open-source-embedded + AI-native) + Milvus (billion-scale distributed + GPU-accelerated). Three of our recent audit subjects — two RAG-native startups in healthcare + a Fortune-500 financial-services vector-search team — all evaluate Qdrant against competitive vector-database offerings (Pinecone + Weaviate + Chroma + Milvus + pgvector + Turbopuffer + LanceDB), and we want to make sure our enterprise audit-template lines up with your actual control surface before we send our first joint customer your way.

I have five vendor-DD questions I'd like to walk through with your security/GRC team (30-min Zoom, your time):

1. Per-collection + per-segment + per-shard + per-replica provenance — can you share the canonical join-table for per-collection-id → per-point-id → per-vector-id → per-payload-id → per-segment-id → per-shard-id → per-replica-id → per-peer-id → per-Raft-id → per-consensus-id → per-WAL-id → per-index-id → per-HNSW-index-id → per-quantization-id → per-distance-metric-id → per-filter-id → per-query-id → per-tenant-id → per-region-id lineage? Our audit-template uses 60+ columns and we want to make sure we're not missing Qdrant-specific events like Raft consensus log entries, WAL writes, or HNSW graph mutations per-shard.

2. Prompt-injection + adversarial-payload defense — Qdrant stores arbitrary third-party vector payloads and answers nearest-neighbor queries that flow downstream into RAG pipelines + LLM context windows. How do you defend against prompt injection in stored payloads, per-payload-poisoning, per-vector-poisoning (shifting the nearest-neighbor manifold toward attacker-controlled content), per-filter-poisoning, per-query-payload-poisoning, per-HNSW-graph-poisoning (mutating graph edges to redirect retrieval), per-quantization-poisoning (attacker exploits int8/binary quantization rounding errors), per-WAL-poisoning, per-Raft-consensus-poisoning, and per-replica-payload-poisoning (poisoning propagates via Raft replication)? We benchmark against OWASP LLM Top 10 LLM01+LLM03+LLM04+LLM06+LLM08 + MITRE ATLAS AML.T0051+AML.T0054 + EU AI Act Art. 15 + NIST AI RMF MEASURE.

3. Cross-region vector-data-residency — for EU + India + Brazil + UAE + Australia + Canada + UK + Singapore + Japan + Philippines customers, what's the per-customer-region selection mechanism for Qdrant Cloud + Qdrant Hybrid Cloud + Qdrant On-Premise + per-cluster-region + per-shard-region + per-replica-region, and is it auditable in your customer-facing logs? We're auditing against Schrems II + GDPR Art. 28 + EU AI Act Art. 10 + India DPDP Act 2023 + Brazil LGPD Art. 33 + UAE PDPL + Canadian PIPEDA + Singapore PDPA + Philippines DPA + Japan APPI.

4. HIPAA-eligible Qdrant Cloud Enterprise for healthcare-vector-RAG — if your healthcare customers want to use Qdrant Cloud for HIPAA-covered RAG pipelines (e.g. patient-record-vector-search, clinical-trial-retrieval, payer-portal-embedding-search), can you walk us through the BAA-ready configuration, per-collection-id PHI-flag handling, per-payload-id CMK/BYOK encryption, per-shard-id PHI-segregation, and per-tenant-id BAA-isolation? HIPAA §164.312(a)(2)(iv) + §164.312(b) + §164.312(e)(1) + §164.514(b) is the floor.

5. Cross-tenant isolation — for Qdrant Open-Source + Qdrant Cloud Free + Qdrant Cloud Standard + Qdrant Cloud Pro + Qdrant Cloud Enterprise + Qdrant Cloud Dedicated + Qdrant Hybrid Cloud + Qdrant On-Premise + per-tenant-id + per-cluster-id + per-database-id + per-collection-id + per-API-key-id + per-RBAC-role-id + per-TLS-cert-id + per-Audit-Log-event-id isolation evidence, can you share the most recent SOC 2 Type II report (CC6.1) + GDPR DPA (Art. 28) + ISO 27001 + EU AI Act readiness statement? Especially interested in how user-stored API keys (OpenAI + Cohere + Hugging Face inference API keys) + CMK/BYOK customer-managed-keys are isolated across tenants, and whether per-shard encryption keys are rotated per tenant or shared.

If a 30-min Zoom is too much friction, I'm also happy to do a written Q&A over email. Our standard vendor-DD SLA is 5 business days, and we won't share your answers outside our audit subject's GRC team.

If Qdrant isn't the right contact for any of these, I'd appreciate a redirect to your security/GRC lead. Either way, thanks for your time — looking forward to working together.

Best,
James Potts
Founder, Talon Forge LLC
james@talonforge.io
https://talonforge.io