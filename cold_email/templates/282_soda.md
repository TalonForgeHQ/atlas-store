# 282_soda.md — Soda Data Observability + Soda Agent + Soda Checks Audit Outreach

**Recipient tier:** 1 (high-conviction)
**Vertical:** data_quality_observability
**Inbox:** privacy@soda.io (cc: security@soda.io)
**Lead row:** 282
**Sibling:** Monte Carlo 281 (first data_quality_observability sibling — Soda is the natural complement)

---

**Subject:** The 5-question Soda data observability + Soda Agent audit prep your Fortune 500 auditor will send in Q4 — with a free compliance-overlap map

**Body:**

Hi Soda Trust + Privacy team,

We do 48h SOC 2 + EU AI Act + ISO 42001 vendor-DD audits for AI-data-infrastructure vendors, and the 5 questions below keep surfacing from CISO + CDAO joint buyers on every Soda evaluation we see. They mirror the same audit gaps from the Monte Carlo (281) sibling in data_quality_observability, plus the reverse-ETL cohort (Census 276 + Hightouch 277 + Airbyte 278 + Hevo 279 + Polytomic 280), but applied to data observability + data-quality + Soda Agent.

**1. Per-Soda-Check failure-event + per-data-source-query-id join-table.** When Soda Core / Soda Cloud fires a Check failure (freshness, volume, schema, validity, custom-Check) on a Snowflake/Databricks/BigQuery/Redshift/Postgres/dbt source, can the per-Check-event record carry per-Check-id + per-data-source-query-id + per-data-asset-id + per-freshness-check-id + per-schema-drift-event-id + per-incident-creation-event-id + per-recipient-notification-id — joinable per-tenant-key + per-data-asset-key for SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 §9.4?

**2. Per-Soda-Agent reasoning-chain audit trail.** The Soda Agent now drafts incident summaries + root-cause hypotheses + suggested remediation queries + suggested stakeholder notifications on the data-reliability surface. What's the per-Soda-Agent-suggestion audit trail — the prompt, the retrieved-Soda-Check-ids, the model-id, the temperature, the tool-call list, the suggested-query, the human-accept-event-id, the reviewer-id, the deployment-stage, the per-tenant-key — joinable per-suggestion-id + per-downstream-incident-id? This is the EU AI Act Art. 12 + Annex IV §1(c) technical-documentation + ISO 42001 §9.4 evidence chain.

**3. Per-data-source-query-id provenance + per-custom-Check reasoning-chain.** Soda Core runs SQL queries against customer warehouses (Snowflake/Databricks/BigQuery/Redshift/Postgres/Spark/Kafka) and supports custom Checks (SQL + YAML + Python). What's the per-data-source-query-id + per-custom-Check join-table — the per-query-id + per-query-result-id + per-Check-creation-event-id + per-Check-tuning-event-id + per-Check-firing-event-id + per-anomaly-classification-id + per-confidence-score — joinable per-tenant-key + per-data-asset-key + per-Check-key for SOC 2 CC7.2 + GDPR Art. 28?

**4. Per-tenant KMS CMK BYOK + cross-tenant data-warehouse isolation evidence.** Soda connects into customer warehouses with sensitive PII / PHI / financial data. Is there per-tenant KMS-CMK-BYOK on the warehouse-connection credentials + the per-Check query-state cache + the per-Soda-Agent prompt cache + the per-incident-response Slack/Jira/PagerDuty/ServiceNow webhook credentials? And what does the cross-tenant isolation evidence look like for the per-tenant Soda Checks + the per-tenant Soda Incidents + the per-tenant Soda Agent reasoning-chain history under SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + EU AI Act Art. 10?

**5. Per-incident-response auto-page + per-root-cause-analysis reasoning-chain WORM retention + cost-attribution join-table.** When the Soda Agent auto-pages an on-call + drafts a root-cause analysis + opens a downstream-Slack/Jira/PagerDuty/ServiceNow ticket, can the per-incident record carry per-paging-event-id + per-Soda-Agent-reasoning-chain-id + per-root-cause-hypothesis-id + per-remediation-query-id + per-downstream-ticket-id + per-cost-attribution-id + per-WORM-retention-flag for SOC 2 CC7.2 + SEC 17a-4 WORM + EU AI Act Annex III §4 + Aug 2026 GPAI enforcement? And how is the per-Soda-Agent reasoning-chain cost + per-Check-firewall cost + per-data-source-query cost + per-downstream-ticket-creation cost attributable per-tenant + per-data-asset + per-Check + per-incident?

We've shipped a **free 6-vendor data-ops compliance-overlap map** (Census + Hightouch + Airbyte + Hevo + Polytomic + Monte Carlo + Soda) mapping each of the 5 audit gaps to the per-vendor evidence surface — happy to send if useful.

We do the audit in **48h for $500 flat**, deliverable is a 25-35 page report with the per-vendor compliance-framework cross-walk + the 5-audit-gap join-table filled in for your environment + the 5-layer reference architecture + the EU AI Act Aug 2026 GPAI technical-documentation draft. The Soda audit includes a free SOC 2 CC7.2 + ISO 42001 §9.4 + EU AI Act Annex IV evidence-export drill.

Worth 15 min next week? I'll send the free 7-vendor overlap map if you reply yes.

— Atlas (Talon Forge LLC)
talonforge.io/atlas-store