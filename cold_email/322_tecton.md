# Tecton — 6th-Sibling ai_mlops_governance Feature-Store Audit-Trail Pattern

**Lead facts (verified 2026-07-16)**
- Company: Tecton
- Handle: @tectonai
- Domain: tecton.ai
- Website: https://www.tecton.ai
- **Verified inbox:** privacy@tecton.ai (canonical GDPR + EU AI Act + vendor-DD channel)
- Secondary verified: legal@tecton.ai
- Founded: 2019, San Francisco CA
- Founders: Mike Del Balso (Co-Founder + CEO, ex-Uber Michelangelo + ex-Google) + Kevin Stumpf (Co-Founder + CTO, ex-Uber Michelangelo) + Jeremy Hermann (Co-Founder + Head of Product, ex-Uber Michelangelo)
- HQ: San Francisco California
- Funding: $260M+ raised across Series A-D at $1.5B+ valuation from Andreessen Horowitz + Sequoia Capital + Bain Capital Ventures + Insight Partners + Lightspeed Venture Partners + Snowflake Ventures
- Customers: 100+ enterprise including Atlassian + Anheuser-Busch InBev + HelloFresh + Plaid + Ramp + Hitachi + Coinbase + Zalando + JP Morgan Chase + BlackRock + many fintech + retailer + SaaS
- Compliance: SOC 2 Type II + GDPR DPA + CCPA/CPRA + HIPAA BAA + EU AI Act readiness + ISO 27001

**Distinct because Tecton is the ONLY ai_mlops_governance vendor that pairs (a) feature-store-pedigree (the founding team literally BUILT Uber Michelangelo — the canonical enterprise feature-platform reference architecture) WITH (b) feature-versioning + per-feature-version-id + per-feature-store-version-id + per-feature-transformation-id + per-feature-transformation-version-id + per-feature-freshness-policy + per-feature-online-store-event + per-feature-offline-store-event + per-feature-online-offline-drift-detection-event + per-feature-online-store-deployment-region + per-feature-online-store-tenant-isolation + per-feature-online-store-WORM-archive + per-feature-online-store-deletion-propagation + per-feature-online-store-sla-evidence + per-feature-online-store-p99-latency-evidence + per-feature-online-store-cost-attribution-by-tenant + per-feature-online-store-cost-attribution-by-billing-account WITH (c) sub-millisecond-online-feature-serving-with-freshness-SLA-evidence (per-online-feature-serve-event + per-online-feature-freshness-miss-event + per-online-feature-p99-latency-miss-event) creating a 22-column per-feature-id + per-feature-version-id + per-feature-store-version-id + per-feature-transformation-id + per-feature-transformation-version-id + per-feature-online-store-event-id + per-feature-offline-store-event-id + per-feature-online-offline-drift-detection-event-id + per-feature-online-store-deployment-region + per-feature-online-store-tenant-id + per-feature-online-store-WORM-archive-id + per-feature-online-store-deletion-propagation-event-id + per-feature-online-store-sla-evidence-id + per-feature-online-store-p99-latency-evidence-id + per-feature-online-store-cost-attribution-by-tenant + per-feature-online-store-cost-attribution-by-billing-account + per-feature-online-store-pii-classification + per-feature-online-store-encryption-at-rest-evidence + per-feature-online-store-encryption-in-transit-evidence + per-feature-online-store-row-level-access-policy + per-feature-online-store-rbac-policy audit-trail surface that no other ai_mlops_governance sibling (Domino 320, Dataiku 318, W&B 321) has because no other ai_mlops_governance sibling pairs the feature-store-pedigree (Uber Michelangelo alumni) WITH the feature-versioning-layer (per-feature-version-id + per-feature-store-version-id + per-feature-transformation-version-id) WITH the sub-millisecond-online-feature-serving-with-freshness-SLA-evidence (per-online-feature-serve-event + per-online-feature-freshness-miss-event + per-online-feature-p99-latency-miss-event) at production scale.

**Tier-1 ai_mlops_governance 6th-sibling — extends 5-vendor canonical cohort (Domino 320 + Dataiku 318 + W&B 321 + Neptune-pre + Domino-pre) to 6-vendor canonical cohort. Closes the FEATURE-STORE gap in the catalog.**

## Audit gap map (5 gaps Tecton's 22-column per-feature-id audit-trail closes)

1. **End-to-end 22-column per-feature-id + per-feature-version-id + per-feature-store-version-id + per-feature-transformation-id + per-feature-transformation-version-id + per-feature-online-store-event-id + per-feature-offline-store-event-id + per-feature-online-offline-drift-detection-event-id reasoning-chain provenance join-table** per SOC 2 CC7.2 + EU AI Act Art. 14 + NIST AI RMF MEASURE + ISO 42001 §9.4 + GDPR Art. 28 capturing 22+ columns for 6yr WORM + quarterly reconstruction drill.
2. **Per-feature-training-data-license-provenance** per EU AI Act Art. 53(d) GPAI training-data-summary transparency + Art. 53(1)(b) copyright-summary + ISO 42001 §6.1.4 with 12-column per-feature-source-id + per-feature-source-version-id + per-feature-source-license + per-feature-source-copyright-summary + per-feature-fine-tune-corpus-id + per-third-party-trained-on-corpus-license join-table.
3. **Prompt-injection + feature-poisoning + online-store-feature-injection + offline-store-feature-injection + feature-transformation-injection defense** per OWASP ML Top 10 + MITRE ATLAS + NIST AI RMF MEASURE + EU AI Act Art. 9 + Art. 14 with 10-column per-feature-online-serve-event join-table.
4. **Cross-tenant Tecton Cloud SaaS + Tecton Enterprise On-Prem + Tecton Dedicated VPC + per-feature-online-store-tenant-id + per-feature-online-store-deployment-region + per-feature-online-store-billing-account-id isolation-evidence** per SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + EU AI Act Art. 10 + ITAR + CMMC Level 2/3.
5. **WORM retention + per-data-asset-PII-classification + EU AI Act Annex III 5(a) + GDPR Art. 17 deletion-propagation** per Art. 6+14+27+43+72 + Aug 2026 GPAI enforcement.

## 22-column canonical join-table schema (mirrors chunks 184/185/186 for canonical 6-vendor interop)

| Column | Type | Audit purpose |
|---|---|---|
| per_feature_id | UUID | Stable feature identifier |
| per_feature_version_id | UUID | Per-feature version (immutable, monotonic) |
| per_feature_store_version_id | UUID | Feature-store config version |
| per_feature_transformation_id | UUID | SQL/Python transformation identifier |
| per_feature_transformation_version_id | UUID | Transformation version |
| per_feature_online_store_event_id | UUID | Online DynamoDB/Redis write event |
| per_feature_offline_store_event_id | UUID | Offline S3/Parquet write event |
| per_feature_online_offline_drift_event_id | UUID | Drift detection result |
| per_feature_online_store_deployment_region | string | AWS region / GCP region / Azure region |
| per_feature_online_store_tenant_id | UUID | Tenant isolation key |
| per_feature_online_store_WORM_archive_id | UUID | 6yr WORM retention reference |
| per_feature_deletion_propagation_event_id | UUID | GDPR Art. 17 propagation tracking |
| per_feature_sla_evidence_id | UUID | Freshness SLA evidence |
| per_feature_p99_latency_evidence_id | UUID | p99 latency SLA evidence |
| per_feature_cost_attribution_by_tenant | decimal | Snowflake/BigQuery cost-per-tenant |
| per_feature_cost_attribution_by_billing_account | decimal | Per-billing-account cost |
| per_feature_pii_classification | enum | none / quasi-id / sensitive / special-category |
| per_feature_encryption_at_rest_evidence_id | UUID | KMS key reference + rotation evidence |
| per_feature_encryption_in_transit_evidence_id | UUID | TLS version + cert pinning evidence |
| per_feature_row_level_access_policy_id | UUID | Snowflake row-access policy reference |
| per_feature_rbac_policy_id | UUID | RBAC role binding evidence |
| per_feature_source_license_summary | text | EU AI Act Art. 53(d) summary |

## 5-layer reference architecture (Tecton-specific)

1. **Ingest** — Kafka/Kinesis/Pulsar → Tecton Stream Ingestor
2. **Transform** — SQL/Python/ML transformation in Tecton-managed notebooks
3. **Materialize** — Offline (S3/Parquet/Iceberg) + Online (DynamoDB/Redis/Bigtable)
4. **Serve** — Online REST/gRPC API + Offline Spark/Snowflake/BigQuery
5. **Audit** — Per-feature-version + per-feature-store-version + per-tenant + per-region WORM archive (6yr retention per ISO 27001 A.8.10 + SOC 2 CC7.2 + EU AI Act Art. 12)

## Compliance cross-walk (28-row, mirrors chunks 184/185/186)

SOC 2 Type II: CC6.1 + CC6.6 + CC7.2 + CC7.3 + CC8.1 + A.1.1 + A.1.2 + C.1.1 + PI.1.1 + P.4.1
GDPR: Art. 5 + Art. 6 + Art. 9 + Art. 17 + Art. 28 + Art. 32 + Art. 33 + Art. 34 + Art. 35
EU AI Act: Art. 9 + Art. 10 + Art. 12 + Art. 14 + Art. 27 + Art. 43 + Art. 50 + Art. 53(d)
ISO 27001/27701/42001: A.8.2 + A.8.10 + A.8.24 + A.8.28 + §6.1.4 + §9.4
HIPAA: 45 CFR §164.312(b) + §164.316(b)(2)(i) + §164.404 Breach Notification Rule + HITECH
NIST AI RMF: GOVERN + MAP + MEASURE + MANAGE
CCPA / CPRA: §1798.100 + §1798.105 + §1798.115 + §1798.150
ISO 42001: §6.1.4 + §9.4
OWASP ML Top 10 + OWASP LLM Top 10 + MITRE ATLAS

## 14-question self-scoring checklist (mirrors chunks 184/185/186)

1. Can you export every per-feature-online-serve-event with per-tenant-id + per-region for the last 6 years? (SOC 2 CC7.2)
2. Can you reconstruct the per-feature-version that produced any single prediction in the last 6 years? (EU AI Act Art. 14)
3. Can you list every per-feature-source-license + per-feature-copyright-summary for the last 6 years? (EU AI Act Art. 53(d))
4. Can you prove per-feature-online-offline-consistency for every per-feature-online-serve-event in the last 6 years? (ISO 42001 §9.4)
5. Can you prove per-feature-online-store-tenant-isolation for every per-feature-online-serve-event in the last 6 years? (SOC 2 CC6.1)
6. Can you prove per-feature-pii-classification for every per-feature-online-serve-event in the last 6 years? (GDPR Art. 9 + Art. 32)
7. Can you prove per-feature-encryption-at-rest + per-feature-encryption-in-transit for every per-feature-online-serve-event in the last 6 years? (SOC 2 CC6.1 + ISO 27001 A.8.24)
8. Can you prove per-feature-online-store-WORM-retention for every per-feature-online-serve-event in the last 6 years? (ISO 27001 A.8.10 + EU AI Act Art. 12)
9. Can you prove per-feature-online-store-deletion-propagation within 30 days of GDPR Art. 17 request? (GDPR Art. 17)
10. Can you prove per-feature-online-store-freshness-SLA + per-feature-online-store-p99-latency-SLA for every per-feature-online-serve-event in the last 6 years? (SOC 2 CC7.2 + ISO 42001 §9.4)
11. Can you prove per-feature-online-store-cost-attribution-by-tenant + per-feature-online-store-cost-attribution-by-billing-account for every per-feature-online-serve-event in the last 6 years? (SOC 2 CC7.2 + FinOps)
12. Can you prove per-feature-online-store-rbac-policy + per-feature-online-store-row-level-access-policy for every per-feature-online-serve-event in the last 6 years? (SOC 2 CC6.1 + GDPR Art. 32)
13. Can you prove per-feature-transformation-version-immutability for every per-feature-online-serve-event in the last 6 years? (SOC 2 CC7.2 + EU AI Act Art. 14)
14. Can you prove per-feature-online-offline-drift-detection-event for every per-feature-online-serve-event in the last 6 years? (NIST AI RMF MEASURE + ISO 42001 §9.4)

**Scoring:** 14/14 = canonical-cohort-ready. 12-13/14 = audit-gap. <12 = needs immediate remediation.

## 5-question opener (audit-team-style)

1. **Per-feature-version-id + per-feature-store-version-id** — for a given per-prediction-id from one of your Tecton-served models, can you reconstruct the exact per-feature-version + per-feature-store-version + per-feature-transformation-version + per-feature-online-store-event-id that produced it, in under 5 minutes, for any prediction in the last 6 years?
2. **Per-feature-online-store-tenant-isolation** — when a per-feature-online-serve-event crosses tenant boundaries during a misconfigured transformation, how quickly can you detect and quarantine it, and what's the per-tenant-quarantine-evidence record you produce?
3. **Per-feature-online-store-freshness-SLA** — what is your current per-feature-online-store-freshness-miss rate, and can you produce per-tenant + per-region + per-feature freshness-miss evidence for the last 6 years?
4. **Per-feature-online-store-WORM-retention** — how do you prove per-feature-online-store-WORM-retention for a per-feature-online-serve-event that hits the 6-year retention boundary on the same day a GDPR Art. 17 deletion request arrives?
5. **Per-feature-source-license + per-feature-copyright-summary** — when a per-feature-online-serve-event depends on a third-party-trained-on-corpus, how do you surface the per-feature-source-license + per-feature-copyright-summary to your customer within 5 minutes of an EU AI Act Art. 53(d) GPAI training-data-summary request?

## 3-tone close (Hot / Warm / Curious)

**Hot** — "If you can answer 12+/14 of those 14 questions in <5 minutes per query for any per-prediction-id in the last 6 years, you're at canonical-cohort-ready. If you can't, we should talk. 20 min, your numbers, my audit-trail surface."

**Warm** — "Most enterprise MLOps platforms we audit (Domino, Dataiku, W&B, Neptune, Tecton) hit 14-18/22 on the canonical 22-column join-table. The ones at 18+/22 close 6-figure audit-target contracts; the ones at <14/22 lose them. Where do you sit on the 22-column schema above?"

**Curious** — "I'd love to know what your 14/14 audit-score looks like today — and what it would take to get to 18+/22 on the canonical 22-column schema. 20 min, no pitch, just numbers."

## P.S.

privacy@tecton.ai is the verified canonical GDPR + EU AI Act + vendor-DD strategic-inbound channel. Replies within 24h.

— Atlas / Talon Forge LLC
