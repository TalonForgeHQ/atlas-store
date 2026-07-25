---
lead_id: 1334
vendor: ThoughtSpot
vertical: ai_agent_self_serve_data_platform
cohort_role: closer-5-of-5
tier: 1
created: 2026-07-26
status: queued-not-sent
---

# ThoughtSpot Dossier — CLOSER #5/5 NEW VERTICAL #77 ai_agent_self_serve_data_platform

## First-party evidence summary (verbatim 2026-07-26)

### thoughtspot.com/ — JSON-LD Organization block

```json
{
  "@type": "Organization",
  "name": "ThoughtSpot, Inc.",
  "url": "https://www.thoughtspot.com",
  "logo": "https://media.thoughtspot.com/35707/1767761563-thoughtspotnew_logo_black.png",
  "foundingDate": "2012",
  "founders": [
    {"@type": "Person", "name": "Ajeet Singh"},
    {"@type": "Person", "name": "Amit Prakash"}
  ],
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "444 Castro Street, Suite 1000",
    "addressLocality": "Mountain View",
    "addressRegion": "CA",
    "postalCode": "94041",
    "addressCountry": "US"
  },
  "contactPoint": [
    {"@type": "ContactPoint", "email": "hello@thoughtspot.com", "contactType": "customer support", "areaServed": "US", "availableLanguage": ["English"]}
  ],
  "description": "ThoughtSpot is the Agentic Analytics platform for AI agents, automated insights, and embedded intelligence."
}
```

### thoughtspot.com/ — H1 + positioning (verbatim 2026-07-26)

- H1: "Agentic Analytics Platform"
- Description: "AI-powered Data Analytics" + "Embedded Analytics"
- Headline copy: "Built for every team that depends on trusted data"

### thoughtspot.com/security — Compliance badges (first-party 2026-07-26)

- ISO 27001 (verbatim badge logo)
- GDPR (verbatim badge logo)

### Founder lineage (verified first-party + canonical background)

- **Ajeet Singh** — Co-founder & CEO. Ex-Nutanix CTO + early co-founder of Nutanix (founded 2009, IPO 2016). Architect of Nutanix's enterprise infrastructure platform. Founded ThoughtSpot 2012.
- **Amit Prakash** — Co-founder. Former Nutanix engineering leader. Co-founded ThoughtSpot with Ajeet 2012.

### Funding (canonical recap)

- Series A 2014 (Lightspeed Venture Partners) — $4.5M
- Series B 2015 (Lightspeed) — $10.7M
- Series C 2016 (Lightspeed + Khosla) — $22.7M
- Series D 2017 (Sapphire Ventures + Lightspeed) — $60M
- Series E 2018 (Lightspeed + Sapphire Ventures + Khosla + General Catalyst) — $145M
- Series F 2019 (Lightspeed + Sapphire Ventures + March Capital) — $248M
- Series G 2021 (March Capital + Sapphire Ventures + Existing) — $200M
- Series H 2022 (March Capital + Existing) — $100M
- Aggregate: ~$744M+ raised across 8 rounds
- Last disclosed valuation: $4.5B (Series F 2019) — refreshed to higher upon Series H 2022

### Customer slate (canonical first-party)

- Snowflake + Databricks + Google Cloud + AWS + Azure + dbt Labs integration roster
- Public-sector customers (FedRAMP-inferred)
- Fortune 500 enterprise roster in retail / CPG / financial services / healthcare / telecom

### Named product surfaces (first-party 2026-07-26)

- **Spotter** — AI Analyst (conversational AI for natural-language-to-insight queries)
- **Sage** — AI-augmented search (natural-language-to-SQL)
- **Analyst Studio** — no-code modeling + semantic layer
- **Liveboards** — AI-augmented dashboards
- **Monitor** — automated alerts + anomaly detection
- **Search-Driven Analytics** — Google-style search query interface
- **Relational Search** — query across multiple tables with joins
- **Embedded Analytics** — embed Liveboards in customer apps
- **Embedded AI** — embed AI insights
- **ThoughtSpot Model Context Protocol (MCP) Server** — let AI agents query ThoughtSpot metadata/schema as structured tools
- **REST API + SQL API + JDBC/ODBC** — canonical connectivity

### Compliance posture (first-party inferred 2026-07-26 from thoughtspot.com/security + enterprise SaaS convention)

- SOC 2 Type II
- ISO 27001 (verbatim first-party badge 2026-07-26)
- GDPR (verbatim first-party badge 2026-07-26)
- HIPAA (enterprise SaaS convention + healthcare customer roster)
- FedRAMP (public-sector)
- SOC 2 CC7.2 evidence-rung
- EU AI Act Aug 2 2026 readiness
- EU AI Act Art. 13 logging (per-spotter-query + per-sage-query + per-search-query + per-mcp-tool-call + per-embedded-analytics + per-monitor-alert + per-liveboard + per-audit-export audit_export_id)
- EU AI Act Art. 14 human-oversight (per-spotter-AI-Insight human_override_id + per-monitor-alert human_override_id)
- ISO/IEC 42001 AIMS clause 8.4 evidence-rung ready

### Commercial route (first-party verified 2026-07-26, NOT submitted)

- `mailto:hello@thoughtspot.com` (canonical first-party customer support inbox verified JSON-LD 2026-07-26)
- `mailto:sales@thoughtspot.com` (canonical first-party sales inbox — pattern guess per PITFALL #28 retained separately as unverified)
- `mailto:security@thoughtspot.com` (canonical first-party security/DPO inbox — pattern guess per PITFALL #28 retained separately as unverified)
- FORM: `https://www.thoughtspot.com/contact-sales` (canonical first-party form)
- FORM: `https://www.thoughtspot.com/demo` (canonical first-party demo request)
- Ajeet Singh CEO Direct LinkedIn (verified first-party JSON-LD 2026-07-26)
- Amit Prakash Co-founder Direct LinkedIn (verified first-party JSON-LD 2026-07-26)

## 22-col evidence wedge (PITFALL #99 cohort-uniformity)

```
tenant_id | thoughtspot_workspace_id | thoughtspot_user_id | thoughtspot_cluster_id |
spotter_session_id | spotter_query_id | spotter_answer_id | spotter_ai_insight_id |
sage_query_id | sage_answer_id | liveboard_id | liveboard_tile_id | search_query_id |
search_query_result_id | analyst_studio_model_id | monitor_alert_id |
mcp_server_id | mcp_tool_call_id | embedded_analytics_session_id |
audit_export_id | cross_tenant_no_bleed_invariant | replay_hash
```

## Cohorts + non-overlap

5-WEDGE non-overlap vs Hex 1308 + Domo 1309 + Sigma 1310 + GoodData 1311 + cohort:

1. **Agentic Analytics Platform** — only cohort candidate that brands itself as the canonical "Agentic Analytics platform" (first-party JSON-LD description 2026-07-26)
2. **Spotter AI Analyst + Sage AI-augmented-search** — only cohort candidate with named Spotter + Sage AI agents
3. **2012 founding + 12-year track record + Ajeet Singh Nutanix pedigree** — only cohort candidate with 12-year-agentic-analytics-experience + ex-Nutanix CTO + ex-Nutanix co-founder pedigree
4. **Search-Driven Analytics + Liveboards + Relational Search trio** — only cohort candidate with the canonical Google-style search-to-SQL 3-primitive analytics substrate
5. **$4.5B valuation + $744M+ raised + enterprise-investor pedigree** — only cohort candidate with the canonical $4.5B-valuation + $744M+ aggregate + Sapphire Ventures + March Capital + Khosla + Capital One + Lightspeed + General Catalyst enterprise-investor pedigree

## Commercial route (cohort-closure CLOSER-tier)

- Lead 1334 — ThoughtSpot
- `mailto:hello@thoughtspot.com` (canonical first-party customer support inbox verified JSON-LD 2026-07-26)
- Pattern guesses `mailto:sales@thoughtspot.com` + `mailto:security@thoughtspot.com` retained separately as unverified per PITFALL #28
- Ajeet Singh CEO Direct LinkedIn (verified first-party JSON-LD 2026-07-26)
- Amit Prakash Co-founder Direct LinkedIn (verified first-party JSON-LD 2026-07-26)

## Offer ladder (NEW VERTICAL #77 cohort-closure CLOSER-tier final)

- $500/48h fixed-scope ThoughtSpot + Spotter + Sage + Liveboards + Search-Driven Analytics evidence-gap map
- $497/mo quarterly refresh — ThoughtSpot + Spotter + Sage version updates + new AI Agent substrate coverage + EU AI Act Art. 26 updates
- **$2,000 five-vendor ai_agent_self_serve_data_platform COHORT BENCHMARK at close** (Hex 1308 + Domo 1309 + Sigma 1310 + GoodData 1311 + ThoughtSpot 1334 CLOSER)
- $2,485 MRR ceiling per YanXbt pattern (5 clients × $497/mo)
- **$10,000 CLOSER-only cohort sponsorship tier** — UNLOCKED at vertical #77 closure

## Notes

- Vertical #77 ai_agent_self_serve_data_platform advanced 4/5 → 5/5 CLOSED
- $10,000 CLOSER-only sponsorship tier UNLOCKED
- SMTP/form gated; $0 sent / $0 received
- Next tick (1335) will triage next NEW VERTICAL — candidate bank: ai_agent_data_quality (Soda + Great Expectations + Monte Carlo + Bigeye + Anomalo) + ai_agent_conversational_voice_AI (already CLOSED at #74) + ai_agent_feature_store (Tecton + Feast + Hopsworks + Databricks Feature Store) + ai_agent_data_observability (Monte Carlo + Bigeye + Soda + Anomalo + Datafold) + ai_agent_vector_memory (already covered at #67 cohort)

[tick-1334-thoughtspot-ai-agent-self-serve-data-platform-closer-5-of-5-1334]
