Subject: SOC 2 + EU AI Act audit for Weaviate's managed vector DB — 48h

Hi Weaviate team,

We run a 48-hour fixed-fee SOC 2 + EU AI Act audit for managed-vector-database vendors. Weaviate's open-source-first vector database + Weaviate Cloud (WCD) + Weaviate Embedded + Weaviate Cloud Hybrid Search + Weaviate RAG pipeline + Weaviate Generative Search (RAG-modules) + Weaviate Multi-Tenancy surface touches every audit gap we test, so we want to put Weaviate through it.

Five questions, one per audit gap:

1) Per-object provenance join-table — can you expose an end-to-end log stitching per-tenant-id → per-class-id → per-object-id → per-vector-id → per-chunk-id → per-LLM-call-id → per-prompt-id → per-prompt-version-id → per-completion-id → per-completion-token-id → per-rerank-id → per-metadata-filter-id → per-hybrid-search-id → per-Generative-Search-pipeline-id → per-Retrieval-Augmented-Generation-trace-id → per-RAG-module-id → per-billing-event-id? SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 want continuous lineage.

2) Prompt-injection + vector-poisoning + hybrid-search-input-poisoning defense at the RAG retrieval surface — what evidence is logged per-Generative-Search-pipeline-id for OWASP LLM Top 10 LLM01 + LLM03 + LLM06 + LLM08 + MITRE ATLAS AML.T0051? EU AI Act Art. 15 wants documented adversarial-robustness evidence.

3) Cross-region vector-data residency — Weaviate Cloud (WCD) runs in AWS us-east-1 + us-west-2 + eu-west-1 + eu-west-2 + eu-central-1 + ap-southeast-1 + ap-northeast-1. Schrems II + GDPR Art. 28 + EU AI Act Art. 10 + India DPDP Act 2023 + Brazil LGPD Art. 33 want per-class-id region-locking + per-tenant-id region-locking + per-bucket-id region-locking + audit logs of region changes.

4) HIPAA-eligible Weaviate Cloud configuration for healthcare-vector-RAG — do you sign a BAA, support per-tenant-id PHI-segregation with per-class-id PHI-flag, per-object-id PHI-tag, and per-region restriction? HIPAA §164.312(a)(2)(iv) + §164.312(b) + §164.312(e)(1) + §164.514(b) require this for clinical deployments.

5) Cross-tenant Weaviate Cloud (WCD) + Weaviate Embedded + Weaviate Bring-Your-Own-Cloud + Weaviate self-hosted isolation-evidence — per-tenant-id + per-class-id + per-shard-id + per-replica-id + per-API-key-id + per-collection-id. SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + EU AI Act Art. 10 want documented tenant-isolation boundary.

We deliver a $500 fixed-fee 48h audit that produces a 30-row canonical per-class-id provenance join-table, a 5-audit-gap analysis, and a 30-day adoption plan. Then $497/mo recurring evidence loop for the next quarter so you can hand the audit pack to every enterprise customer in the pipeline.

Reply with a 15-min slot this week if you want the audit. We can ship the first pass within 48h of getting read-access to a staging Weaviate Cloud tenant.

— Atlas
Atlas (TalonForge)
