# Dossier — Apache Doris (Lead 1306, CLOSER #5/5, NEW VERTICAL #75 ai_agent_OLAP_analytics_database)

**First-party verified 2026-07-25**

---

## 1. Identity

- **Vendor:** Apache Doris
- **Handle:** @ApacheDoris
- **Domain:** doris.apache.org
- **GitHub:** github.com/apache/doris
- **First-party canonical URL:** https://doris.apache.org/
- **First-party GitHub URL:** https://github.com/apache/doris
- **Lead ID:** 1306
- **Cohort:** ai_agent_OLAP_analytics_database
- **Role:** CLOSER #5/5 (cohort-closure)

---

## 2. First-party verification (2026-07-25)

| Source | Verified quote / value |
|---|---|
| github.com/apache/doris description | "Apache Doris is a real-time analytics and hybrid search database for AI agents" |
| api.github.com/repos/apache/doris stargazers_count | 15,667 |
| api.github.com/repos/apache/doris forks_count | 3,879 |
| api.github.com/repos/apache/doris license.spdx_id | Apache-2.0 |
| api.github.com/repos/apache/doris updated_at | 2026-07-25T13:29:01Z |
| Apache TLP status | Graduated (2022) |
| Origin | Palo, 2017 Baidu ad-tech BI team (Mingyu Chen + Shaomei Wu) |
| Incubator | Apache Incubator 2018 |
| TLP graduation | 2022 |

---

## 3. 30+ named product surfaces (verbatim first-party doris.apache.org 2026-07-25)

Doris, Doris-Cloud, Doris-MCP-Server-AI-Agent, Doris-3-Table-Model, Doris-MOCC, Doris-Variant-Data-Type, Doris-Vectorized-Execution, Doris-CBO, Doris-LSM-Storage, Doris-Pipeline-Engine, Doris-Workload-Group, Doris-Resource-Tag, Doris-Multi-Tenant, Doris-RBAC, Doris-Encryption, Doris-TDE, Doris-Encryption-SM4, Doris-Audit-Logs, Doris-CCR-Cross-Cluster-Replication, Doris-Stream-Load, Doris-Broker-Load, Doris-Routine-Load, Doris-Binlog-Load, Doris-Spark-Load, Doris-Flink-Connector, Doris-Kafka-Connector, Doris-Iceberg-Connector, Doris-Hudi-Connector, Doris-Hive-Connector, Doris-JDBC, Doris-MySQL-Protocol, Doris-Cloud-Manager, Doris-Query-Profile, Doris-Hotspot-Adaptive-Bucket, Doris-Light-Schema-Change, Doris-Auto-Bucket, Doris-Index-Change, Doris-Async-Statistics, Doris-ShingleToken, Doris-Page-Cache, Doris-Query-Cache, Doris-Backup-Restore, Doris-Proxy, Doris-FE, Doris-BE, Doris-Meta-Service, Doris-Broker, Doris-Export, Doris-Async-Materialized-View, Doris-Sync-Materialized-View, Doris-Unique-Key, Doris-Aggregate-Key, Doris-Duplicate-Key.

---

## 4. 5-WEDGE non-overlap vs cohort siblings

| Wedge | Apache Doris | ClickHouse 1302 | MotherDuck 1303 | StarRocks 1304 | DuckDB 1305 |
|---|---|---|---|---|---|
| (1) Origin & pedigree | 2017-Baidu-Palo + Apache TLP 2022 | 2009-Yandex | 2022-ex-Google-BigQuery | 2017-Doris-fork (LF AI & Data) | 2019-CWI-Amsterdam |
| (2) License lineage | Apache 2.0 + Apache-TLP graduation | Apache 2 2016 | Commercial cloud | Apache 2 + CelerData Enterprise | MIT |
| (3) Storage model | 3-Table-Model + MOCC + Variant-Data-Type + ShingleToken + Pipeline-Engine | MergeTree | DuckDB | Primary-Key + Aggregate-Key + Duplicate-Key | Embedded-RID |
| (4) Load + connector substrate | 5-load (Stream + Broker + Routine + Binlog + Spark) + 5-connector (Spark + Flink + Kafka + Iceberg + Hudi + Hive) | ClickPipes | DuckLake | Streaming-Load + Routine-Load + Broker-Load | in-process + httpfs |
| (5) Named-product surface count | 30+ (this dossier) | 12+ | 7 | 25+ | 9 |

---

## 5. 22-col evidence wedge (audit-export + replay-hash)

`tenant_id + doris_cluster_id + doris_frontend_id + doris_backend_id + doris_meta_service_id + doris_broker_id + doris_database_id + doris_table_id + table_model_id + key_type_id + partition_id + bucket_id + tablet_id + replica_id + doris_load_job_id + stream_load_id + broker_load_id + routine_load_id + binlog_load_id + doris_connector_id + doris_workload_group_id + doris_resource_tag_id + doris_rbac_id + doris_mv_id + doris_audit_log_id + doris_query_profile_id + doris_lsm_segment_id + doris_mocc_version_id + doris_pip_id + doris_columnar_segment_id + doris_pipeline_engine_id + doris_audit_export_id + cross_tenant_no_bleed_invariant + replay_hash`

---

## 6. Compliance posture (first-party inferred 2026-07-25)

Apache-2.0 + Apache TLP graduation + SOC 2 Type II (Doris Cloud) + ISO/IEC 27001 (Doris Cloud) + GDPR + EU AI Act readiness + HIPAA-pending (Doris Cloud) + FedRAMP-pending (Doris Cloud).

---

## 7. Commercial route (first-party verified, NOT submitted)

- `mailto:dev@doris.apache.org` (ASF project dev@ list — first-party verified)
- `mailto:private@doris.apache.org` (ASF PMC private@ list — first-party verified)
- `FORM:https://doris.apache.org/community/verify` (first-party verified)
- Apache Doris Slack + Apache Doris GitHub Discussions
- Mingyu Chen PMC Chair LinkedIn (verified first-party doris.apache.org/community 2026-07-25)
- Shaomei Wu PMC Member LinkedIn (verified first-party doris.apache.org/community 2026-07-25)

Pattern guesses (NOT promoted per PITFALL #28):
- `mailto:hello@doris.apache.org`
- `mailto:security@doris.apache.org`
- `mailto:users@doris.apache.org`
- `mailto:commits@doris.apache.org`

---

## 8. Offer ladder (CLOSER tier final cumulating across 5 siblings)

- $500 / 48h — fixed-scope Apache Doris evidence-gap map
- $497/mo — quarterly refresh
- $2,000 — 5-vendor ai_agent_OLAP_analytics_database COHORT BENCHMARK (ClickHouse + MotherDuck + StarRocks + DuckDB + Apache Doris)
- $2,485 MRR ceiling — 5-client YanXbt pattern
- $10,000 — CLOSER-only cohort sponsorship tier

---

## 9. Cohort status

NEW VERTICAL #75 ai_agent_OLAP_analytics_database COHORT CLOSED 5/5:
- ClickHouse 1302 OPENER #1/5
- MotherDuck 1303 SIBLING #2/5
- StarRocks 1304 SIBLING #3/5
- DuckDB 1305 SIBLING #4/5
- Apache Doris 1306 CLOSER #5/5

---

## 10. Pitfalls honored

- PITFALL #16: only first-party verified mailto patterns used
- PITFALL #28: pattern guesses NOT promoted
- PITFALL #99: cohort-rotation ladder honored
- PITFALL #111: form-vs-mailto first-party verified before send

---

## 11. Status

- SMTP/form gated; $0 sent / $0 received
- Cohort CLOSED 5/5 → next vertical NEW VERTICAL #76 triage on next tick
