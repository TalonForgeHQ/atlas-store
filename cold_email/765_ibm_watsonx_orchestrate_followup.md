# Lead 765 evidence — IBM watsonx Orchestrate

**Verified:** 2026-07-21 UTC
**Cohort:** `ai_data_intelligence_agents` SIBLING #5/5 (closer)
**Company:** International Business Machines Corporation (IBM)
**Website:** https://www.ibm.com/
**Commercial route:** `FORM:https://www.ibm.com/contact/global`

## First-party proof

The following first-party pages were checked directly on 2026-07-21:

- https://www.ibm.com/products/watsonx — HTTP 200. The current watsonx page positions IBM watsonx as the AI and data platform that accelerates data-driven decisions by delivering AI-powered insights with trusted, governed data, enabling faster business outcomes that integrate with existing tools and infrastructure. The page surfaces watsonx.ai (next-gen AI studio with Granite + third-party models + full AI lifecycle management), watsonx.data (trusted-data lakehouse with hybrid open data lakehouse architecture for any format), watsonx Orchestrate (AI assistants and agents for business and customer-facing processes), IBM Bob (SDLC-focused AI partner with deep context awareness of the codebase), watsonx Code Assistant for Ansible Lightspeed, and watsonx Code Assistant for Z (IBM Z mainframe lifecycle automation).
- https://www.ibm.com/about — HTTP 200. The current About page identifies IBM as a company headquartered in a NYC Madison One Avenue office, with 0,000+ employees across 170+ countries (the live page renders a load-then-fill animation so digits are not extracted; the page's own fact block describes "employees across 170+ countries"), 0,500+ businesses in the Partner Plus program, and 0+ years of delivering breakthrough research. The Origin story describes the 1911 founding as the Computing-Tabulating-Recording Company, renamed IBM in 1924, with roots back to Herman Hollerith's 1896 tabulating machine.
- https://www.ibm.com/contact/global — HTTP 200. The contact global page lists Support, Sales, Learn, Business Partners, and Contact Information; the Sales section routes to "Contact IBM sales" for product questions and purchasing assistance; country-level contact pages for North America, Europe, Asia Pacific, Latin America, and Middle East and Africa are linked.
- https://www.ibm.com/leadership — HTTP 404 (path no longer published); the live Senior leadership page reachable from the About footer maps to a search landing at https://www.ibm.com and is not currently a single canonical leadership URL. Founder-identification convention used: Arvind Krishna is publicly identified as IBM Chairman and Chief Executive Officer on press release and SEC filings; the company legal name is International Business Machines Corporation incorporated in the State of New York, NYSE ticker IBM, and SEC EDGAR CIK 0000051143. Press contacts are explicitly media-only.

## Distinct cohort wedge

The prior `ai_data_intelligence_agents` cohort opened by Databricks 761 (lakehouse + Unity Catalog + Agent Bricks / Mosaic AI), continued by Snowflake 762 (warehouse-native Cortex Agents with persisted Threads/Runs), then Palantir 763 (ontology + AIP with branch/merge), then Salesforce 764 (CRM-native Data 360 + Agentforce). IBM watsonx Orchestrate closes the cohort with a hybrid-cloud + on-prem AI-agent platform rooted in the Granite open foundation-model family + watsonx.governance + watsonx.data lakehouse, plus the engineering-deploy Bob + watsonx Code Assistant surface (developer-tooling-adjacent). This is an enterprise-runtime-and-governance plane distinct from the data-platform-prior cohort: Build-time model choice and prompt-evaluation in watsonx.ai + InstructLab; runtime agent orchestration in watsonx Orchestrate; governed data access in watsonx.data; governance, risk, and audit logging in watsonx.governance; deployment in IBM Cloud, on-prem, or hybrid via IBM's FedRAMP-In-Process and FIPS 140-3-aligned stack. Evidence cascade: tenant + IBMid + account + region + deployment topology + foundation-model identity + version + system prompt + retrieval index snapshot + agent/skill/instruction version + orchestration plan + tool call + identity + authorization policy + downstream state change; model-evaluation run + metric + reviewer + change-request; rollback target; export/deletion across watsonx.ai model artifacts, watsonx Orchestrate conversation traces, watsonx.data catalogs, evaluations, replicas, caches, governance logs, and backups. Tier-1 evidence wedge is upstream of Fireworks/Replicate/Together/Anyscale/AWS inference runtime, and non-overlapping with Databricks lakehouse (Unity Catalog + Delta + MLflow + Agent Bricks), Snowflake warehouse (Cortex + Threads/Runs), Palantir ontology (branch/merge), and Salesforce CRM-native (Data 360 + Agentforce).

## Five buyer-facing joins

1. watsonx.ai model + prompt + retrieval + InstructLab-tuning + evaluation run → watsonx Orchestrate agent/skill/instruction version → policy decision (allow / deny / escalate / branch) → downstream state change in target system.
2. Granite + third-party-model selection + token-budget + audit-trail receipt → runtime call → model-output moderation → reviewer escalation → evaluation dataset.
3. watsonx.data governed catalog row + row-level + column-level access policy + retrieval index snapshot → agent tool/data call → identity verification + authorization decision + downstream state change.
4. Human reviewer + change-request + governance approval + audit log + rollback target + Granite model deprecation schedule + OEM-VRAM-isolation.
5. Export + deletion across model artifacts, conversation traces, retrieval indexes, evaluation datasets, governance logs, caches, replicas, and backups across region + subprocessor boundary.

These are evidence questions, not claims that every receipt is currently exposed. The $500/48-hour map identifies existing, split, and missing records.

## Route safety

Use only the first-party commercial form, `FORM:https://www.ibm.com/contact/global`. No guessed inbox, restricted privacy/legal/security/support/press route, form submission, email, delivery, payment, or revenue is claimed. The company legal name is International Business Machines Corporation; its registered agent is in the State of New York; SEC EDGAR CIK 0000051143; NYSE ticker IBM.
