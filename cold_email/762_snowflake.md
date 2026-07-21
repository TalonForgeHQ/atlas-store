# Lead 762 evidence — Snowflake Cortex Agents

**Verified:** 2026-07-21 UTC
**Cohort:** `ai_data_intelligence_agents` sibling #2/5 after Databricks 761 OPENER
**Company:** Snowflake Inc.
**Website:** https://www.snowflake.com/
**Commercial route:** `FORM:https://www.snowflake.com/en/contact-sales/`

## First-party proof

The following first-party pages were checked directly on 2026-07-21:

- https://www.snowflake.com/en/company/overview/about-snowflake/ — rendered successfully. Snowflake describes its mission around enterprise data and AI, reports 12,062 global customers, and says its founders built the platform to harness cloud scale.
- https://www.snowflake.com/en/company/overview/leadership-and-board/ — rendered successfully. The page has a dedicated Co-Founders tab and names Benoit Dageville and Thierry Cruanes as co-founders.
- https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents — HTTP 200. Current documentation calls Cortex Agents a fully managed agentic platform inside Snowflake's governed environment. It documents the plan → use tools → reflect loop, schema-level Agent objects, persisted Threads, Run events, REST API access, monitoring, feedback, evaluations, and tools including Cortex Analyst, Cortex Search, isolated Python code execution, custom tools, agent skills, MCP connectors, and web search.
- https://www.snowflake.com/en/contact-sales/ — rendered successfully. The page asks visitors with questions about Snowflake offerings to complete the form and says response times are typically one business day.

## Distinct cohort wedge

Databricks 761 opens the governed lakehouse data plane. Snowflake 762 adds a distinct warehouse-native execution and observability chain: role and privilege → schema-level Agent object → model and instructions → Analyst/Search/code/custom/MCP tool choice → persisted Thread → Run and event stream → feedback/evaluation → downstream state → retention/deletion. This is not a generic inference-endpoint review.

## Five buyer-facing joins

1. User/session role and privileges → Agent object/version → governed data object or semantic view.
2. Thread → Run → plan/use-tools/reflect event → selected model and tool configuration.
3. Cortex Analyst/Search, code execution, custom tool, skill, MCP connector, or web-search call → authorization → input/output → downstream state.
4. End-user feedback or evaluation → metric → reviewer → agent/model/instruction change → promoted revision.
5. Export/deletion → threads, run events, prompts, tool outputs, traces, feedback, evaluation artifacts, caches, logs, replicas, and backups.

These are evidence questions, not claims that every receipt is currently exposed. The $500/48-hour map identifies existing, split, and missing records.

## Route safety

Use only the first-party Contact Sales form. The page's `press@snowflake.com` route is explicitly restricted to media inquiries and is excluded. No guessed inbox, form submission, email, delivery, payment, or revenue is claimed.
