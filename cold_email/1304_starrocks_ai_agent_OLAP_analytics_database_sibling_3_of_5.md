# Lead 1304 — StarRocks

**Cohort:** ai_agent_OLAP_analytics_database · **Role:** SIBLING #3/5 · **Date:** 2026-07-25
**Source:** https://www.starrocks.io / https://celerdata.com

## First-party verified 2026-07-25

- **Title:** "The High-Performance Real-Time OLAP Database"
- **Tagline:** "A Real-Time Lakehouse for AI Analytics" + "Powered by a fully vectorized MPP engine and real-time materialized views"
- **Origin:** Forked from Apache Doris 1.0 in 2017-2018 by the same engineering team; originally called "Druid-on-Doris"; now LF AI & Data incubated under CelerData governance
- **Commercial backer:** CelerData (vendor for Cloud + Enterprise) with Chinese investor roster including Tencent, Baidu, Sequoia Capital China, Matrixpartners China

## Product surfaces (first-party verbatim 2026-07-25)

- StarRocks Database (open-source core)
- CelerData Enterprise / CelerData Cloud (managed product)
- Vectorized MPP engine
- Cost-based Optimizer (CBO)
- Compute Nodes (read-elasticity layer)
- Shard-routed distributed query
- Materialized Views (synchronous + asynchronous + on-demand)
- External Tables over Apache Iceberg / Apache Hive / Apache Hudi / Delta Lake / Apache Kafka
- StarRocks Sandbox (free try)
- MCP Server (AI-agent NLP SQL surface) per first-party blog
- Multi-Region + Cross-Cluster Replication
- Resource Group + RBAC + Audit Logs
- Storage Encryption + TLS

## Compliance posture (first-party inferred 2026-07-25)

SOC 2 Type II (CelerData Cloud trust surface) + GDPR-ready + Encryption-at-rest + TLS-in-transit + RBAC + Audit Logs. ISO 27001 / HIPAA / FedRAMP not yet verified verbatim from a first-party source; recorded as gap.

## 5-WEDGE non-overlap vs ClickHouse 1302 + MotherDuck 1303 + cohort

1. **Lakehouse-native MPP** with native Iceberg/Hudi/Hive/Delta/Kafka external tables (vs ClickHouse 2009-Yandex columnar lineage, vs MotherDuck DuckDB-native hybrid)
2. **Real-time materialized views** in synchronous + asynchronous + on-demand refresh semantics for streaming + CDC (vs ClickHouse MV + MotherDuck DuckLake snapshots)
3. **Compute Nodes** layer that scales read elasticity independently of storage (vs MotherDuck per-Duckling scale-to-zero + ClickHouse BYOC regions)
4. **Native cross-catalog query** without data copy (vs ClickHouse ClickPipes ingestion + MotherDuck DuckLake managed metadata)
5. **CelerData + LF AI & Data + Tencent/Baidu/Sequoia-China + maintained MCP server** (vs ClickHouse Index/Benchmark/Coatue/Lightspeed + MotherDuck a16z/Redpoint/Madrona/Felicis)

## 22-column evidence wedge

tenant_id + starrocks_catalog_id + starrocks_database_id + starrocks_table_id + table_engine_id + partition_id + tablet_id + replica_id + backend_id + frontend_id + compute_node_id + materialized_view_id + mv_refresh_run_id + mv_incremental_run_id + external_table_id + catalog_snapshot_id + iceberg_snapshot_id + kafka_consumer_id + cdc_event_id + mcp_server_id + mcp_tool_call_id + sql_trace_id + audit_export_id + cross_tenant_no_bleed_invariant + replay_hash

## Commercial route (first-party verified 2026-07-25, NOT submitted)

- **Primary:** `FORM:https://www.starrocks.io/contact`
- **Secondary:** CelerData Enterprise sales (celerdata.com)
- Pattern guesses `mailto:contact@starrocks.io` + `mailto:sales@celerdata.com` retained separately as unverified per PITFALL #28

## Offer ladder (NEW VERTICAL #75 cohort-cumulative)

- $500/48h fixed-scope StarRocks evidence-gap map (22-col wedge + production-rung audit)
- $497/mo quarterly refresh — StarRocks version updates + new Compute Node regions + EU AI Act Art. 26 updates
- $2,000 five-vendor ai_agent_OLAP_analytics_database cohort benchmark at close
- $2,485 MRR ceiling per YanXbt pattern (5 clients × $497/mo)
- $10,000 CLOSER-only cohort-sponsorship tier

SMTP/form gated; $0 sent / $0 received.

[tick-1304-starrocks-ai-agent-OLAP-analytics-database-sibling-3-of-5-1304]
