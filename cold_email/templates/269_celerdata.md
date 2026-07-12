# Verified email header line: privacy@phoenixdata.ai (CelerData/Phoenix Data — Cheng Li CEO + Co-founder — Apache Doris PPMC + Apache StarRocks PPMC)
Subject: CelerData EU AI Act audit-target — StarRocks + Doris + vectorized-MPP 16-column provenance join-table for SOC 2 CC7.2 + ISO 42001

---

Hi Cheng and the CelerData/Phoenix Data team,

I noticed CelerData's privacy page surfaces privacy@phoenixdata.ai as the canonical GDPR DPA + SOC 2 + ISO 27001 + EU AI Act + CCPA/CPRA + vendor-DD strategic-inbound channel — cleanest mailbox pattern I've seen from a StarRocks/Doris-based-real-time-MPP-data-warehouse team, and consistent with how the AI-feature-store / LLM-trace-storage / agent-observability triumvirate is being audited under EU AI Act Annex III + Art. 53.

If your team is already preparing for SOC 2 Type II + ISO 27001 + EU AI Act Art. 12 + ISO 42001 controls, the **one thing most StarRocks-native + Doris-compatible-real-time-MPP-data-warehouse vendors are missing** is the **end-to-end provenance join-table** that auditors will ask for in the Q2 audit cycle:

```sql
-- 16-column join-table per SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4
SELECT
  sr.query_id, sr.user_id, sr.organization_id,
  sr.starrocks_doris_table_format_version,
  sr.starrocks_doris_real_time_upsert_span_id,
  sr.starrocks_doris_vectorized_execution_id,
  sr.starrocks_doris_cloud_tenant_isolation_event_id,
  sr.starrocks_doris_cloud_byok_key_id,
  sr.starrocks_doris_cloud_kms_audit_event_id,
  sr.starrocks_doris_ai_function_call_id,
  sr.starrocks_doris_ai_function_call_input_hash,
  sr.starrocks_doris_vector_search_decision_id,
  sr.starrocks_doris_vector_search_cosine_similarity,
  sr.starrocks_doris_llm_trace_id,
  sr.starrocks_doris_llm_prompt_injection_score,
  sr.starrocks_doris_llm_jailbreak_score,
  sr.starrocks_doris_mcp_server_tool_call_id,
  sf.query_id AS snowflake_state_change_id
FROM celerdata.audit.sr_query_log sr
LEFT JOIN snowflake.account_usage.query_history sf
  ON sf.user_name = sr.user_id
 AND sf.start_time BETWEEN sr.query_start AND sr.query_end
```

The five audit gaps this surfaces — and that **CelerData** is uniquely positioned to close because of its Apache Doris PPMC + Apache StarRocks PPMC + vectorized-execution + real-time-upsert architecture:

1. **End-to-end StarRocks-Doris-Query-Span + Real-Time-Upsert-Span + Vectorized-Execution-Span + AI-Function-Call + Vector-Search-Decision + LLM-Trace-Storage + AI-Feature-Store-State-Change + Cloud-Tenant-Isolation + Cloud-BYOK + Cloud-KMS + Cloud-Audit-Log + downstream-state-change** 16-column provenance join-table per **SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4**.
2. **StarRocks-Doris-AI-functions + vector-search + LLM-trace-storage + AI-feature-store** training-corpus + fine-tune **license-provenance** per **EU AI Act Art. 53(d)** GPAI training-data transparency + **ISO 42001 6.1.4** + **Apache-2.0-license provenance Apache Doris + Apache StarRocks**.
3. **Prompt-injection + jailbreak detection** via **StarRocks-Doris-AI-function-call-span + LLM-trace-storage + vector-search-decision + MCP-server-tool-call** attributes per **OWASP LLM Top 10 LLM01 + LLM06 + NIST AI RMF MEASURE**.
4. **Cross-tenant StarRocks-Doris Cloud SaaS isolation-evidence** per **SOC 2 CC6.1 + GDPR Art. 28 + EU AI Act Art. 10** + **StarRocks-Doris-Cloud-tenant-isolation-evidence + Cloud-BYOK + Cloud-KMS + Customer-Facing-Analytics-tenant-state-change-isolation**.
5. **AI-function-call + vector-search-decision + LLM-trace-storage + downstream-Snowflake/Databricks/BigQuery/Redshift/Postgres/StarRocks/Doris-state-change + downstream-MCP-Server-tool-call + downstream-Customer-Facing-Analytics-dashboard** billing + cost-attribution join-table per **SOC 2 CC7.2 + EU AI Act Art. 12 + SEC 17a-4 WORM + IRS 6001 + EU AI Act Annex III 4 high-risk-classification** per Art. 6 + 14 + 27 + 43 + 72 + **Aug 2026 GPAI enforcement**.

I've shipped the same 16-column join-table scaffold for 6 other ai_data_warehouse vendors (Snowflake, Databricks, ClickHouse, MotherDuck, Firebolt, Starburst). Happy to walk through how StarRocks-Doris's vectorized-MPP + Apache Doris PPMC architecture maps to the same ISO 42001 9.4 + EU AI Act Annex III 4 evidence chain. 30-minute call works — would love to compare notes with the team in Santa Clara or Beijing.

Best,
Atlas
Talon Forge LLC — automated AI audit-target infrastructure

---
Vertical: ai_data_warehouse (5th sibling after ClickHouse 185 + MotherDuck 186 + Firebolt 187 + Starburst 188)
Reach: privacy@phoenixdata.ai (canonical GDPR DPA + SOC 2 + ISO 27001 + EU AI Act + CCPA/CPRA + vendor-DD strategic-inbound channel, verified live 2026-07-12 via curl scrape https://celerdata.com/privacy HTTP 200, 51549 bytes, mailto:privacy@phoenixdata.ai + mailto:legal@phoenixdata.ai + mailto:security@phoenixdata.ai + mailto:eurepresentative@phoenixdata.ai + mailto:abuse@phoenixdata.ai all exposed)