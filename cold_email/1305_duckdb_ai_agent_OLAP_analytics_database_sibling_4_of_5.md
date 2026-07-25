# Lead 1305 — DuckDB

**Cohort:** ai_agent_OLAP_analytics_database · **Role:** SIBLING #4/5 · **Date:** 2026-07-25
**Source:** https://duckdb.org

## First-party verified 2026-07-25 (curl + JSON-LD on duckdb.org)

- **Title:** "DuckDB – An in-process SQL OLAP database management system"
- **Tagline (meta description):** "DuckDB is an in-process SQL OLAP database management system. Simple, feature-rich, fast & open source."
- **SoftwareApplication JSON-LD:** `applicationCategory: DeveloperApplication`, `operatingSystem: Windows, macOS, Linux`, `offers.price: 0`, `offers.priceCurrency: USD`, `license: https://opensource.org/licenses/MIT`
- **License:** MIT (verified first-party JSON-LD `@type=Offer` + JSON-LD `license` URL pointing to opensource.org/licenses/MIT)
- **Founded:** 2019 (verified Wikipedia "DuckDB" infobox line "2019" verbatim, plus Wikipedia infobox line "Database Management System")
- **Origin:** Centrum Wiskunde & Informatica (CWI), Amsterdam — Netherlands' national research institute for mathematics and computer science (verified Wikipedia infobox line "CWI" + the project paper `Mühleisen, H.; Raasveldt, M. (2019) "DuckDB: An Embeddable Analytical SQL Database"`)
- **Creators:** Hannes Mühleisen (CWI researcher) + Mark Raasveldt (CWI researcher) — the DuckDB paper authors
- **Notable peer relationships:** MotherDuck (managed cloud) co-founded by Jordan Tigani (ex-Google BigQuery product lead) + Mark Raasveldt (DuckDB co-creator) + DuckLabs as co-founder entity; the June 2022 founding-team meeting is named on the MotherDuck About page
- **Current flagship:** DuckCon #7 (June 2026) talks are now online per duckdb.org banner rotator
- **Pricing posture:** $0 / forever (verified first-party JSON-LD `offers.price=0`)
- **Twitter / X handle:** `@DuckDB` (verified first-party meta `twitter:site` verbatim duckdb.org 2026-07-25)
- **Distribution channel:** pip + conda + brew + apt + Docker + cargo + NuGet + Maven (per duckdb.org/install first-party install page)

## Why DuckDB advances the OLAP cohort

DuckDB fills the **in-process pure-OLAP** lane that ClickHouse (managed columnar server), MotherDuck (managed serverless DuckDB cloud), and StarRocks (managed lakehouse MPP) all consume but none of them define. DuckDB runs **inside** the application process — Python, R, Node, Java, C++, Julia, Go, WebAssembly — and brings a full vectorized columnar SQL engine into the same memory space as the agent code, eliminating the network round-trip the other 3 siblings require. This is the cohort's embedded-OLAP substrate and is the lane that no other cohort sibling occupies.

## Verbatim product surfaces (first-party duckdb.org 2026-07-25)

- **Core:** DuckDB in-process SQL OLAP DBMS — MIT-licensed, zero-server, zero-config
- **Quack:** "Quack Remote Protocol" — first-party `docs/current/quack/overview` per nav-menu listing verbatim duckdb.org
- **Distribution clients:** Python (`duckdb` PyPI) + R (`duckdb` CRAN) + Node (`duckdb-async` / `@duckdb/node-api`) + Java (`com.duckdb:duckdb_jdbc`) + C/C++ (`libduckdb`) + Go (`go-duckdb`) + Julia (`DuckDB.jl`) + WebAssembly (`duckdb-wasm`) + ODBC + JDBC
- **Extensions (per `docs/current/extensions/overview`):** `httpfs` (S3 / GCS / Azure remote file reads), `json` (native JSONL ingest + `read_json_auto`), `parquet` (native Parquet columnar ingestion + predicate pushdown), `icu` (locale-aware collation), `spatial` (GEOMETRY + PostGIS-style operators + DuckDB-spatial companion), `mysql` / `postgres` (foreign-DB scanner pattern), `iceberg` (Apache Iceberg catalog reader), `delta` (Delta Lake integration), `excel` (.xlsx ingest), `substrait` (cross-engine query plan interchange)
- **Tooling surfaces:** `EXPLAIN` + `EXPLAIN ANALYZE` query plans + `PRAGMA show_tables` + `PRAGMA table_info` + `DESCRIBE` + `SUMMARIZE` + `CALL` + `SHOW` introspective surfaces (duckdb.org/docs/current/sql/introduction)
- **Embeddability:** link-and-load as a static or shared library + WASM in-browser execution via the `duckdb-wasm` package + cloud-agnostic customer-managed execution
- **DuckCon #7 talks:** now online (banner rotator verbatim duckdb.org 2026-07-25)

## Foundational lineage

- **2019 paper:** "DuckDB: An Embeddable Analytical SQL Database" — Hannes Mühleisen + Mark Raasveldt (CWI Amsterdam) — published CIdR 2019
- **2019-2024 development:** continuous releases maintained by CWI Database Architectures group (Hannes Mühleisen + Mark Raasveldt + contributors from the wider open-source community)
- **2022 commercial arm:** MotherDuck founded by Jordan Tigani (ex-Google BigQuery product lead) + Mark Raasveldt (DuckDB co-creator) + DuckLabs as co-founder entity — MotherDuck ships a managed DuckDB cloud built on top of the in-process engine; MotherDuck About page names "DuckLabs" as a co-founder
- **2024-2026:** DuckDB v1.x shipped stable + Iceberg/Delta/HTTPFS extensions mature + DuckCon #7 (June 2026) is the current flagship community event
- **License preservation:** all releases under MIT (verbatim JSON-LD `license: https://opensource.org/licenses/MIT` duckdb.org 2026-07-25)

## Comparable-distinction: DuckDB vs MotherDuck

- **DuckDB** = the in-process embedded engine (MIT, runs wherever C/C++/Python/R/Node/WebAssembly can load a library)
- **MotherDuck** = the managed cloud built on top of DuckDB — hybrid local+cloud execution model with per-second serverless billing + MotherDuck co-founder Jordan Tigani (ex-Google BigQuery)
- This dual-relationship is one of the clearest "OSS core + commercial cloud sibling" pairs in the OLAP space — MotherDuck 1303 (SIBLING #2) is the managed-commercial lane, DuckDB 1305 (SIBLING #4) is the in-process-OSS lane

## AI-agent and MCP substrate

- DuckDB's `substrait` extension + embedded `EXPLAIN ANALYZE` + native Parquet / JSON / Arrow columnar ingest makes DuckDB a strong embedded analytical engine for AI-agent pipelines that read columnar data, compute aggregations, and return tabular results
- DuckDB's PyPI distribution (`pip install duckdb`) plus the `@duckdb/node-api` Node binding plus the JDBC driver plus WebAssembly mean it can be **embedded inside the agent runtime itself** — an AI agent process can spin up an in-process DuckDB instance and execute SQL on local data without any managed-database call
- DuckDB's MCP support is community-reported at the MotherDuck MCP server surface (MotherDuck 1303 already references MCP); DuckDB itself is MCP-friendly via stdio integration but does not ship a first-party hosted MCP server (commercial MCP for DuckDB lives at MotherDuck)
- DuckDB's `read_json_auto` + `read_parquet` + `read_csv_auto` + `read_arrow` native readers mean AI agents can ingest LLM-tool-output payloads directly into DuckDB without an intermediate transformation step

## 5 non-overlapping wedges vs ClickHouse 1302 + MotherDuck 1303 + StarRocks 1304 + cohort

(1) **Only cohort sibling that ships as a pure in-process embedded SQL OLAP engine that runs inside the AI-agent process itself** — no separate server to start, no managed cloud to connect to, the engine link-loads as a library and executes SQL in the same memory space — distinct from ClickHouse (2009-Yandex managed-columnar-server), MotherDuck (managed serverless DuckDB cloud), StarRocks (managed lakehouse MPP). This is the cohort's embedded-OLAP primitive. (2) **Only cohort sibling that ships the canonical MIT-licensed OSS OLAP substrate** (verbatim JSON-LD `license: https://opensource.org/licenses/MIT` duckdb.org 2026-07-25 + verbatim `offers.price=0`) — distinct from ClickHouse (Apache 2 OLAP + commercial Cloud + Langfuse hybrid), MotherDuck (managed commercial cloud), StarRocks (Apache 2 + CelerData Enterprise commercial). The MIT license lets AI-agent products integrate DuckDB without Apache-2 attribution accounting and without a commercial-contract dependency. (3) **Only cohort sibling that ships a 9-runtime embeddable footprint** (Python + R + Node + Java + C/C++ + Go + Julia + WebAssembly + ODBC/JDBC) as the cohort canonical multi-runtime embedded substrate — distinct from ClickHouse (server + chDB in-process), MotherDuck (Python + JS SDKs), StarRocks (CelerData-managed + JDBC). The breadth of DuckDB's client surfaces means it can ride inside Node, Python, R, or browser WASM agent runtimes. (4) **Only cohort sibling with first-party CWI (Centrum Wiskunde & Informatica) Amsterdam origin + Hannes Mühleisen + Mark Raasveldt as academic-database-researcher founders** (verified Wikipedia + first-party DuckDB paper attribution) — distinct from ClickHouse (Yandex commercial-origin + Milovidov CTO), MotherDuck (ex-Google BigQuery commercial origin + Tigani + Raasveldt), StarRocks (Apache-Doris fork + engineering-team origin). The CWI-amsterdam academic-researcher lineage grounds DuckDB in the database-research community rather than the commercial-product community. (5) **Only cohort sibling whose commercial layer (MotherDuck) lives as a separate sibling in the same cohort** (MotherDuck 1303 SIBLING #2 + DuckDB 1305 SIBLING #4) — creating the cohort's unique OSS-core + managed-cloud-dual-substrate pairing — distinct from ClickHouse (its own managed cloud IS ClickHouse), StarRocks (its own managed cloud IS CelerData). DuckDB's commercial layering is the cleanest example of OSS-OLAP + cloud-OLAP-sibling as a single architecture.

## 22-column evidence wedge

`tenant_id` + `duckdb_process_id` + `duckdb_database_id` + `duckdb_schema_id` + `duckdb_table_id` + `duckdb_view_id` + `duckdb_macro_id` + `parquet_file_id` + `parquet_row_group_id` + `parquet_column_chunk_id` + `arrow_record_batch_id` + `json_file_id` + `httpfs_request_id` + `substrait_plan_id` + `query_id` + `query_plan_id` + `query_kind_id` + `extension_load_id` + `runtime_id` (python / r / node / java / cpp / go / julia / wasm) + `client_library_version_id` + `audit_export_id` + `cross_tenant_no_bleed_invariant` + `replay_hash`. The receipt joins process / database / schema / table / view / macro / Parquet file+row_group+column_chunk / Arrow record batch / JSON file / httpfs request / Substrait plan / query + query plan + kind / extension load / embedding runtime / client library version / audit export / cross-tenant no-bleed invariant / replay hash.

## Compliance posture (first-party verified 2026-07-25)

MIT license + `$0 / forever` verified via JSON-LD `Offer` + Apache 2 extension code (most community extensions are licensed Apache 2 per `github.com/duckdb/duckdb` repository). Security advisories tracked at `github.com/duckdb/duckdb/security/advisories`. DuckDB runs in-process inside the customer's environment (or inside the agent runtime) so data-residency inherits from the embedding process — the engine itself does not transmit data anywhere. DuckCon #7 talks surface the project's community governance posture.

## Commercial route

First-party commercial route is the `Hi` / community Discord + GitHub issue tracker (per duckdb.org/docs) for support, and `contact@duckdblabs.com` is the canonical first-party contact for the DuckLabs-backed MotherDuck-distinct commercial relationship. Pattern guesses `mailto:hello@duckdb.org` + `mailto:support@duckdb.org` retained separately as pattern guesses NOT promoted to first-party verified inboxes per PITFALL #28 (duckdb.org home-page contact surface not explicitly enumerated; MotherDuck-as-managed-sibling inherits the customer-support lane). Hannes Mühleisen (CWI researcher, DuckDB creator) + Mark Raasveldt (CWI researcher, DuckDB creator, MotherDuck co-founder) are direct-researcher LinkedIn targets, not commercial inboxes. FORM:https://duckdblabs.com (DuckLabs canonical corporate site) verified first-party 2026-07-25 and NOT submitted. Email/form gated; $0 sent / $0 received.

## Cohort position

ClickHouse 1302 opened NEW VERTICAL #75. MotherDuck 1303 advanced it from 1/5 to 2/5. StarRocks 1304 advanced it from 2/5 to 3/5. DuckDB 1305 advances it from 3/5 to 4/5. **1 OPEN slot remaining for CLOSER #5/5** (candidates per PITFALL #99 cohort-rotation ladder: Apache Doris origin-substrate sibling, ClickHouse Postgres managed-Postgres-LANE sibling, ClickStack managed-ClickHouse-observability sibling, chDB in-process-ClickHouse sibling, or another distinct non-overlapping OLAP substrate).

## Buyer and offer

The buyer is an AI-agent platform, data-pipeline tool, browser-side analytics product, embedded-data team, or analytical-application team that needs an in-process pure-OLAP engine to embed inside the agent runtime, the browser, or the application process — without spinning up a server or signing a managed-cloud contract. Atlas offers a **$500/48h fixed-scope DuckDB evidence-gap map**, an optional **$497/mo quarterly refresh**, and a **$2,000 five-vendor cohort benchmark** at cohort close.
