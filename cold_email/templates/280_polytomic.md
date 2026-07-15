Subject: Polytomic ETL + Reverse ETL audit-trail — 4 questions on per-sync-run provenance

Ghalib — quick opener, not a deck.

We've been running vendor-DD audits on the 5-vendor reverse-ETL cohort (Census 276 + Hightouch 277 + Airbyte 278 + Hevo 279 + Polytomic) and Polytomic is the no-code + data-warehouse-native option in the cohort. The wedge we keep hitting: per-sync-run provenance, per-AI-mapping-suggestion audit trail, and per-tenant KMS BYOK + cross-tenant isolation evidence under SOC 2 CC7.2 + EU AI Act Annex IV §1-3 (Aug 2026 GPAI enforcement) + ISO 42001 §9.4.

Four questions we can't answer from the privacy page or the docs site — would take 15 min on a scope call to walk through:

1. **Per-sync-run provenance join-table.** When Polytomic moves a row from Snowflake/BigQuery/Postgres/Redshift into Salesforce/HubSpot/Zendesk/Marketo/Google Sheets/Postgres, can the per-sync-run record carry per-source-LSN + per-source-tx-id + per-warehouse-query-id + per-destination-API-call-id + per-retry-count + per-partial-failure-mode + per-schema-drift-event-id joinable per-tenant-key + per-pipeline-id + per-run-id? SOC 2 CC7.2 auditors are asking for this granularity for any reverse-ETL vendor whose syncs touch customer-PII or deal-state downstream.

2. **Per-AI-mapping-suggestion reasoning-chain.** Polytomic's no-code UI surfaces AI-assisted field-mapping suggestions when users wire up a new source-to-destination pair. What's the audit trail on each suggestion — the prompt, the retrieved-source-schema-id, the model-id, the temperature, the tool-call, the suggested-mapping, the human-accept-event-id, the reviewer-id, and the timestamp — joinable per-tenant-key + per-suggestion-id + per-downstream-sync-run-id? This is the EU AI Act Art. 12 risk-management + Annex IV §1(c) technical-documentation + ISO 42001 §9.4 AI-data-governance evidence chain.

3. **Per-tenant KMS BYOK + cross-tenant prompt-injection defense.** Polytomic is multi-tenant by definition. Is there per-tenant KMS-CMK-BYOK on the warehouse connection credentials + the destination API tokens + the per-sync queue state + the per-AI-mapping prompt cache? And what does the cross-tenant prompt-injection defense look like across the AI-field-mapping prompt-injection attack surface (per OWASP LLM Top 10 LLM01 + LLM03 + LLM06)?

4. **Per-destination-API-call attribution + per-recipient sync-evidence.** When Polytomic writes to a downstream Salesforce/HubSpot/Zendesk/Marketo record, can the customer pull a per-recipient attribution event — per-recipient-id + per-sync-run-id + per-API-call-id + per-record-id + per-old-value + per-new-value — joinable per-tenant-key + per-segment-id + per-recipient-id? This is the SOC 2 CC7.2 + GDPR Art. 28 + CCPA/CPRA evidence chain for downstream-state-change attribution.

The same five audit gaps propagate from every vendor in the cohort, so we've shipped a **free 5-vendor reverse-ETL compliance-overlap map** (Census + Hightouch + Airbyte + Hevo + Polytomic) — happy to send it if useful.

We do the audit in **48h for $500 flat**, deliverable is a 25-35 page report with the per-vendor compliance-framework cross-walk + the 5-audit-gap join-table filled in for your environment + the 5-layer reference architecture + the EU AI Act Aug 2026 GPAI technical-documentation draft. The Polytomic audit includes a free SOC 2 CC7.2 + ISO 42001 §9.4 + EU AI Act Annex IV evidence-export drill.

Worth 15 min next week? I'll send the free map if you reply yes.

— Atlas (Talon Forge LLC)
talonforge.io/atlas-store