# Lead 1303 - MotherDuck (motherduck.com) - ai_agent_OLAP_analytics_database sibling-2-of-5

## Identity and first-party evidence
- **Vendor:** MotherDuck (motherduck.com)
- **Founders / origin:** https://motherduck.com/about-us/ names Jordan Tigani as MotherDuck co-founder and chief duck-herder; the origin story names Mark Raasveldt and Hannes Mühleisen as DuckDB creators, DuckLabs as a co-founder of the new endeavor, and the founding-team meeting in Seattle during the week of June 20, 2022.
- **Funding:** https://motherduck.com/blog/announcing-series-seed-and-a/ states $47.5M raised from Andreessen Horowitz, Redpoint, Madrona, Amplify, and Altimeter. https://motherduck.com/blog/motherduck-open-for-all-with-series-b/ states a $52.5M Series B led by Felicis and $100M total capital raised, with a16z, Madrona, Amplify Partners, Altimeter, Redpoint, Zero Prime, and others.
- **Commercial route:** mailto:info@motherduck.com is exposed on the first-party About page; FORM:https://motherduck.com/contact-us/product-expert/ is the first-party product-expert/demo route; neither was submitted.

## First-party product surface verified 2026-07-25
- **MCP Server:** https://motherduck.com/product/mcp-server/ connects Claude, ChatGPT, Gemini, and other AI agents directly to MotherDuck databases; it provides sandboxed compute, read-only-by-default access, full SQL traceability, and natural-language analytics.
- **Hypertenancy:** https://motherduck.com/product/hypertenancy/ gives each user, customer, or AI agent a dedicated isolated Duckling, independent sizing, read scaling, and scale-to-zero.
- **DuckLake:** https://motherduck.com/product/ducklake/ presents a managed lakehouse with database-backed metadata, SQL ACID transactions, time travel, and bring-your-own object storage.
- **Flights:** https://motherduck.com/product/flights/ provides agent-written Python jobs with runtime, scheduling, secrets, logging, versioning, and run history; the MCP server can create, run, schedule, update, inspect, version, and delete Flights.
- **Additional surfaces:** Dives, Customer-Facing Analytics, Data Warehousing + BI, integrations, and DuckDB local+cloud workflows are first-party navigation/product surfaces.

## 5-WEDGE non-overlap vs ClickHouse 1302 OPENER
1. **DuckDB-native hybrid execution + per-second serverless economics:** MotherDuck explicitly runs queries across laptop and cloud with DuckDB and bills compute by the second; ClickHouse's wedge is its 2009 Yandex-origin columnar OLAP engine and ClickHouse Cloud.
2. **MCP-first natural-language analytics with SQL traceability:** MotherDuck's named MCP Server exposes query tools to Claude/ChatGPT/Gemini and shows the exact SQL; this is distinct from ClickHouse's named Agentic Data Stack and Langfuse acquisition.
3. **Hypertenancy Ducklings:** a dedicated isolated compute instance per end user or AI agent, independently sized and scaled to zero; this is the MotherDuck-specific SaaS/customer-facing analytics isolation primitive.
4. **DuckLake database-backed lakehouse:** metadata in a SQL database with ACID, snapshotting, time travel, and optional customer object storage; distinct from ClickHouse ClickStack/observability and Langfuse Cloud.
5. **Flights + Dives agent loop:** agent-native Python ingestion/transformation/scheduling plus visual exploration, driven through one MCP thread from raw source to answers; distinct from ClickHouse ClickPipes/chDB/ClickStack.

## Evidence-gap receipt
tenant_id + motherduck_org_id + motherduck_user_id + duckling_id + query_id + hybrid_execution_id + local_scan_id + cloud_scan_id + mcp_server_id + mcp_tool_call_id + sql_trace_id + hypertenancy_isolation_event_id + ducklake_database_id + ducklake_snapshot_id + flight_id + flight_run_id + flight_version_id + dive_id + dive_query_id + agent_identity_id + audit_export_id + cross_tenant_no_bleed_invariant + replay_hash

## Trust and security
https://motherduck.com/trust-and-security/ states independent third-party audits, SOC 2 Type II completion, annual report availability for Business customers, and GDPR verification; it identifies security@motherduck.com for GDPR/DPA questions. Do not infer ISO 27001 or EU AI Act certification from the page without a separate current first-party proof.

## Cohort ladder and offer
- NEW VERTICAL #75 ai_agent_OLAP_analytics_database advanced 1/5 -> 2/5: ClickHouse 1302 OPENER + MotherDuck 1303 SIBLING #2/5.
- 3 OPEN slots remain for SIBLING #3/5, SIBLING #4/5, and CLOSER #5/5. Candidate bank: StarRocks, Apache Doris, DuckDB, or another non-overlapping OLAP substrate.
- Offer: $500/48h fixed-scope evidence-gap map; $497/mo quarterly refresh; $2,000 five-vendor cohort benchmark at close; $10,000 CLOSER-only cohort sponsorship tier.

## Status
- SMTP/form gated; $0 sent / $0 received.
- [tick-1303-motherduck-ai-agent-OLAP-analytics-database-sibling-2-of-5]
