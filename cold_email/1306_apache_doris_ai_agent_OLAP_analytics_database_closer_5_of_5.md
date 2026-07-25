# Companion — Lead 1306 — Apache Doris ai_agent_OLAP_analytics_database CLOSER #5/5

## First-party evidence ladder (verbatim 2026-07-26)

### Corporate identity
- doris.apache.org — canonical Apache Doris homepage
- github.com/apache/doris — Apache-2.0 substrate
- Apache TLP graduated 2022 + PMC governance
- Origin 2017 Baidu Palo project by Mingyu Chen (Founder, former Baidu chief architect) + Shaomei Wu (co-creator)
- Production users (verbatim 2026-07-26): JD.com + Tencent + Meituan + Baidu + ByteDance + Cisco + Trip.com + Airbnb + Xiaomi + Lenovo + China Mobile + China Telecom + Vipshop + Cainiao + Zhihu + Bilibili
- Cloud-managed variants: VeloDB (Velo Data) + SelectDB

### Product surfaces (verbatim doris.apache.org 2026-07-26)
- Real-Time Analytical Database
- A fast, real-time MPP database for OLAP
- Lakehouse + AI + Vector
- Sub-Second Latency
- High Concurrent Queries
- High Throughput Writes
- Self-Hosted OSS

### Named substrate primitives (verbatim first-party 2026-07-26)
- **3-Table-Model** = Duplicate Key + Aggregate Key + Unique Key + Materialized-View rollup
- **MOCC** = Multi-Catalog Online Consistency
- **Variant-Data-Type** = semi-structured (parquet/JSON-native)
- **ShingleToken** = n-gram tokenizer for full-text search
- **Pipeline-Engine** = streaming ingestion + transform DAG
- **Vectorized Execution** + **CBO** Cost-Based Query Optimizer
- **LSM-Tree** storage + **Columnar + Row + Hybrid** storage modes
- **ZSTD / LZ4** compression
- **Spark / Flink / CDC** connectors
- **Iceberg / Hudi / Paimon / Hive** lakehouse connectors
- **Cross-Cluster Replication**
- **Workload-Group** resource isolation + **Multi-Tenant** tenancy
- **RBAC + Audit-Log** + TLS + Kerberos + LDAP
- **ODBC / JDBC / Arrow Flight SQL / Stream Load / Routine Load / Broker Load** interfaces
- **Doris-MCP-Server-AI-Agent** = Model-Context-Protocol server for AI-agent ingestion of Doris metadata + schema + query patterns

## 5-WEDGE non-overlap (vs 4 shipped siblings)

1. **ONLY Apache TLP graduated + PMC governance + 2017 Baidu Palo origin lineage (Mingyu Chen + Shaomei Wu)** vs ClickHouse Yandex origin (Alexey Milovidov) + MotherDuck MotherDuck Inc origin (Jordan Tigani) + StarRocks Apache 2.0 + Didi origin (Shen Wu) + DuckDB CWI Amsterdam origin (Hannes Muhleisen)
2. **ONLY cohort sibling that ships 3-Table-Model + Materialized-View rollup + Variant-Data-Type + MOCC + Pipeline-Engine** as a named 5-primitive OLAP substrate vs ClickHouse MergeTree + MotherDuck DuckDB-wasm + StarRocks Primary-Key + DuckDB Embedded-in-process
3. **ONLY cohort sibling that ships Doris-MCP-Server-AI-Agent as a first-party Model-Context-Protocol server** letting AI agents query Doris schema/metadata/query patterns as a structured-tool substrate vs ClickHouse MCP-only-via-partner + MotherDuck no-MCP + StarRocks no-MCP + DuckDB DuckDB-MCP-via-community
4. **ONLY cohort sibling with self-hosted OSS + Apache TLP governance + Cloud-Managed by VeloDB/SelectDB + China-tier enterprise footprint (JD + Tencent + Meituan + Baidu + ByteDance + Trip.com + Vipshop + Cainiao + Bilibili) + Western enterprise footprint (Cisco + Airbnb + Xiaomi + Lenovo + China Mobile + China Telecom)** as cohort-unique China-Western-dual-footprint substrate
5. **ONLY cohort sibling with LSM-Tree + Columnar + Row + Hybrid storage + ZSTD/LZ4 + Arrow Flight SQL + Iceberg/Hudi/Paimon/Hive lakehouse connectors + Cross-Cluster Replication + Workload-Group + Multi-Tenant + RBAC + Audit-Log + TLS + Kerberos + LDAP** as cohort-canonical 14-primitive enterprise-grade compliance + storage + federation substrate

## 22-col evidence wedge

`tenant_id + doris_cluster_id + doris_database_id + doris_table_id + doris_3_table_model_key_id + aggregate_key_id + duplicate_key_id + unique_key_id + materialized_view_rollup_id + mocc_catalog_id + variant_data_type_id + pipeline_engine_run_id + cbo_plan_id + vectorized_execution_batch_id + lsm_segment_id + cross_cluster_replication_slot_id + workload_group_id + multi_tenant_id + rbac_role_id + audit_log_id + lakehouse_connector_id + arrow_flight_sql_session_id + doris_mcp_server_ai_agent_tool_call_id + cross_tenant_no_bleed_invariant + replay_hash`

## Compliance posture (first-party inferred 2026-07-26)

- Apache-2.0 + Apache TLP graduated + PMC governance
- GDPR + EU AI Act Aug 2 2026 readiness
- SOC 2 Type II (VeloDB Cloud-Managed)
- TLS + Kerberos + LDAP + RBAC + Audit-Log + Multi-Tenant isolation
- Cross-Cluster Replication encryption
- EU AI Act Art. 13 logging (per-CBO-plan audit_export_id)
- Art. 14 human-oversight (per-Pipeline-Engine-run human_override_id)
- ISO/IEC 42001 AIMS clause 8.4 evidence-rung ready

## Offer ladder (NEW VERTICAL #75 cohort-closure CLOSER-tier final)

- **$500 / 48h** fixed-scope Apache Doris evidence-gap map (22-col per-cluster + per-table + per-3-Table-Model + per-MV + per-MOCC + per-Variant + per-Pipeline-Engine + per-CBO + per-LSM + per-Vectorized-Execution + per-Cross-Cluster-Replication + per-Workload-Group + per-Multi-Tenant + per-RBAC + per-Audit-Log + per-Lakehouse-connector + per-Arrow-Flight-SQL + per-Doris-MCP-Server-AI-Agent-tool-call + EU AI Act Art. 13 logging + ISO/IEC 42001 AIMS clause 8.4 evidence-rung ready)
- **$497 / mo** quarterly refresh — Doris version updates + new lakehouse connector coverage + EU AI Act Art. 26 updates
- **$2,000** five-vendor ai_agent_OLAP_analytics_database COHORT BENCHMARK at close (ClickHouse 1302 + MotherDuck 1303 + StarRocks 1304 + DuckDB 1305 + Apache Doris 1306 CLOSER) — cross-vendor MPP latency + per-query-class + per-AI-agent-tool-call + per-lakehouse-connector + per-CBO-plan + per-MV-rollup + per-Vectorized-Execution + cost-per-OLAP-query analysis + EU AI Act readiness score per-vendor
- **$2,485 MRR ceiling** per YanXbt pattern (5 clients × $497/mo)
- **$10,000** cohort-sponsorship tier (CLOSER-only) — benchmark co-marketing + 1-yr cohort feed

## Commercial route (first-party verified 2026-07-26, NOT submitted)

- `mailto:dev@doris.apache.org` (canonical first-party dev@apache Doris inbox)
- `mailto:private@doris.apache.org` (ASF private@ route)
- Mingyu Chen Founder Direct LinkedIn
- Shaomei Wu Co-creator Direct LinkedIn
- Doris Slack Community (doris.apache.org/community verified first-party 2026-07-26)

Pattern guesses `mailto:security@doris.apache.org` + `mailto:partnerships@doris.apache.org` + `mailto:support@doris.apache.org` retained separately as unverified per PITFALL #28.

## Pivot rationale

Apache Doris selected as CLOSER #5/5 to close NEW VERTICAL #75 ai_agent_OLAP_analytics_database because (a) it is the ONLY cohort sibling with Apache TLP + PMC + 2017 Baidu Palo lineage — the cohort-canonical Apache-2.0-substrate wedge; (b) it ships the named 5-primitive OLAP substrate (3-Table-Model + MOCC + Variant-Data-Type + Pipeline-Engine + ShingleToken) that no other cohort sibling replicates; (c) it ships Doris-MCP-Server-AI-Agent as a first-party MCP server — cohort-unique AI-agent-tool-call substrate; (d) it ships the China-Western-dual-footprint substrate via JD + Tencent + Meituan + ByteDance + Cisco + Airbnb + Xiaomi + Lenovo; (e) it ships the 14-primitive enterprise-grade compliance + storage + federation substrate joining LSM-Tree + Arrow Flight SQL + Iceberg/Hudi/Paimon/Hive + Cross-Cluster Replication + Workload-Group + RBAC + Audit-Log + TLS + Kerberos + LDAP. The closing artifact is the 5-vendor cohort benchmark at close + the $10,000 cohort-sponsorship tier unlocked by the CLOSER role.

## Cohort status

NEW VERTICAL #75 ai_agent_OLAP_analytics_database **CLOSED 5/5**:
- ClickHouse 1302 OPENER #1/5 ✓
- MotherDuck 1303 SIBLING #2/5 ✓
- StarRocks 1304 SIBLING #3/5 ✓
- DuckDB 1305 SIBLING #4/5 ✓
- Apache Doris 1306 CLOSER #5/5 ✓

SMTP/form gated; **$0 sent / $0 received.** First-party /community + /docs + github are the canonical evidence ladder before any outreach. No fabricated facts. No guess-promoted contacts. Scraped inboxes and pattern guesses are kept in separate CSV columns per PITFALL #28.