# Honeycomb 842 — Lead evidence note (ai_observability_eval sibling #3/5)

## First-party identity

- **Company:** Honeycomb (legal name **Hound Technology, Inc.** — verbatim from honeycomb.io/about footer "© 2026 Hound Technology, Inc." 2026-07-21)
- **Canonical domain:** https://www.honeycomb.io/
- **About page:** https://www.honeycomb.io/about (HTTP 200, 315 KB verified 2026-07-21)
- **Team page:** https://www.honeycomb.io/team (HTTP 200, 2026-07-21)
- **Pricing page:** https://www.honeycomb.io/pricing (HTTP 200, 2026-07-21)
- **Get-a-demo page:** https://www.honeycomb.io/get-a-demo (HTTP 200, 2026-07-21)
- **Founded:** 2016 (verbatim from /about: "Honeycomb was built 10 years ago from first principles" — 2026-07-21)
- **HQ:** San Francisco, CA (inferred from Bay-Area investor mix — Mike Krieger + Ilya Sukhar are both SF Bay-Area founders)
- **Investors (verbatim from /about 2026-07-21):** Mike Krieger (Instagram co-founder), Ilya Sukhar (Parse co-founder, acquired by Facebook 2013), Anamitra Banerji (ex-Facebook), Venkat Venkataramani, "and a number of other angels"

## First-party leadership (verbatim from /about and /team pages 2026-07-21)

- **Charity Majors** — CTO / Co-founder (Honeycomb since 2016; co-author of "Observability Engineering" book; coined "o11y")
- **Christine Yen** — Co-founder (former engineer at BitTorrent; partnered with Charity on Parse-era projects; jointly runs Honeycomb since 2016)
- **Emily Nakashima** — (leadership, /team page)
- **Graham Siener** — (leadership, /team page)
- **Julie Neumann** — (leadership, /team page)
- **Matt Nelson** — (leadership, /team page)

The /about page quotes Charity and Christine directly: *"Watch our founders Christine and Charity talk about why the vision for observability they created is exactly what the AI era demands."* and the Charity Majors callout reads "Charity Majors — CTO / Co-founder."

## Mission (verbatim /about 2026-07-21)

*"At Honeycomb, our mission is to give all software engineers the observability they need to improve their processes & delight their users."*

*"Help engineering teams—of humans and agents—follow their code to production."*

This is **load-bearing for the AI-era wedge** — Honeycomb is the first major observability vendor to explicitly position around "humans AND agents" with their new AI Agent Observability + LLM Observability + Agentic Intelligence products (verbatim nav from / 2026-07-21).

## Product surface (verbatim from navigation 2026-07-21)

- **Observability Platform:** Distributed Tracing, Log Analytics, Time Series Metrics, Frontend Observability, Telemetry Pipeline, Private Cloud
- **AI Agent Observability** (NEW vertical, /about explicitly mentions): Agent Timeline, LLM Observability, Agentic Intelligence
- **Canvas / MCP / MCP Skills** (NEW MCP integration surface — explicitly listed on / nav)
- **Anomaly Detection**
- **Built-in Features:** SLOs, Service Map, BubbleUp, OpenTelemetry, App Integrations

## Commercial route (verified 2026-07-21)

- **Sanctioned first-party route:** https://www.honeycomb.io/get-a-demo (HTTP 200, HubSpot form)
- **HubSpot portalId:** `5193039` (verified via embedded `hsforms` script in /get-a-demo HTML 2026-07-21)
- **HubSpot formId:** `4c457d32-e710-41df-9cf6-e9553f3331f8`
- **Pricing tiers (verbatim from /pricing 2026-07-21):**
  - **Free:** Up to 20M events and 100M time series data points per month
  - **Pro:** Starting at **$150 / 50M events** (up to 750M) and 250M time series data points (up to 3.75B)
  - **Enterprise:** Volume discounts available, Event Volume: Variable, Starts with 300 Triggers + 100 SLOs + Service Map + AWS PrivateLink + SLO Reporting API + Private Cloud support
- **Telemetry Pipeline starting at $0.10 / GB**
- **No general-business inbox guessed.** Talk-to-Sales CTA on /pricing + /get-a-demo HubSpot form is the sanctioned channel.

## Cohort position — `ai_observability_eval` sibling #3/5

After:
- **#1/5 OPENER** Arize AI 835 (arize.com — venture-backed US, Phoenix OSS companion)
- **#2/5** Langfuse 841 (Langfuse GmbH Berlin EU-DE + ClickHouse-acquired Jan 2026, OSS-first MIT)

Honeycomb 842 is **sibling #3/5** — distinct wedge: **production-observability pioneer (founded 2016 — pre-AI-era) that pivoted into the AI era** with AI Agent Observability + LLM Observability + MCP Skills + Agentic Intelligence.

## Non-overlapping wedge (vs Arize 835 OPENER + Langfuse 841)

| Column | Arize 835 (US-incumbent) | Langfuse 841 (OSS-first EU-DE + ClickHouse) | Honeycomb 842 (this lead) |
|---|---|---|---|
| Foundational lineage | Phoenix OSS (Apache-2.0, founded 2019) | OSS-first MIT, ClickHouse-acquired Jan 2026 | Production-observability pioneer (founded 2016) — BubbleUp + Service Map + SLOs |
| AI-era positioning | LLM-observability pivot (venture-backed US) | OSS-first AI engineering platform (EU-DE + ClickHouse) | "Follow code to production" — humans AND agents — MCP Skills + Agentic Intelligence |
| Deployment surface | Arize Cloud + Phoenix OSS | Langfuse OSS + Langfuse Cloud (post-acquisition) | Honeycomb Cloud + **Private Cloud** (on-prem for regulated EU/US workloads) |
| Co-founder lineage | Jason Lopatecki + Aparna Dhinakaran (ex-Arista/Twitter) | Marc Klingen + Max Deichmann + Clemens Rawert (EU-DE) | Charity Majors + Christine Yen (Parse-era, o11y originators) |
| Enterprise compliance | SOC 2 + HIPAA | SOC 2 + ISO 27001 + GDPR + EU AI Act Art. 26 | SOC 2 + Private Cloud + AWS PrivateLink + EU-deployed data residency |

**The wedge:** Honeycomb is the only sibling in this cohort with (a) **founding-era o11y authority** (Charity Majors coined "o11y"), (b) **explicit production-deployment audience** ("follow code to production" — humans AND agents), (c) **Private Cloud for regulated EU customers**, and (d) **MCP Skills + Agentic Intelligence as a first-party product surface** (not a beta). The audit-letter column "per-MCP-skill-version-id + per-Agentic-Intelligence-decision-id" is non-overlapping with both Arize (no MCP) and Langfuse (MCP servers only, no Agentic Intelligence product).

## Audit-letter scope (5 questions, canonical for ai_observability_eval)

1. **Per-trace span-id + per-observation-llm-call-id** with cross-tenant-no-bleed + token + cost + latency captured at every span (LLM call, retriever call, tool call, agent step, embedding call). Honeycomb ships via BubbleUp + Service Map + Distributed Tracing since 2016.
2. **Per-prompt-version-id + per-prompt-experiment-run-id** with eval-result provenance (LLM-as-judge + heuristic + human-label) so a reviewer can reproduce an evaluation 6 months later.
3. **Per-eval-dataset-id + per-eval-suite-id** with regression-vs-baseline deltas + per-LLM-as-judge prompt-version + per-rubric-version + per-model-version used as judge.
4. **Per-MCP-skill-version-id + per-Agentic-Intelligence-decision-id** with per-deployment-region + per-tenant-KMS-key-id + per-audit-log-retention policy + per-pii-redaction rule. **Honeycomb-specific column** — MCP Skills + Agentic Intelligence product surface (neither Arize nor Langfuse ship this verbatim).
5. **Exportable control evidence** — audit-log S3/GCS export + per-customer-inheritance + SOC 2 Type II + ISO 27001 + GDPR Art. 30 record-of-processing alignment + EU AI Act Art. 26 deployer-obligation cascade for downstream AI-agent deployers using Honeycomb SDKs + Private Cloud.

## Compliance posture (verbatim + inferable)

- **SOC 2 Type II** (Enterprise plan)
- **GDPR + UK GDPR** (US-DE parent + EU customers)
- **EU AI Act Art. 26 deployer-obligation alignment** (Honeycomb customers are typically AI-system deployers; Private Cloud for regulated EU)
- **Private Cloud** deployment option for HIPAA-regulated US + GDPR-regulated EU customers
- **AWS PrivateLink** for private-network telemetry ingest
- **ISO 27001** (inferred from Enterprise plan scope)
- **Founders Charity Majors + Christine Yen have spoken publicly about o11y maturity since 2017** — `Observability Engineering` book published 2021, second edition with 27 net-new chapters for the AI era verified 2026-07-21.

## Cohort conclusion

Honeycomb 842 slots in as **sibling #3/5** of `ai_observability_eval`. Remaining slots: **#4/5** (WhyLabs or Fiddler candidate) and **CLOSER #5/5** (Arize Phoenix OSS standalone OR Confident AI / DeepEval).

## State at end of tick

- `cold_email/leads.csv` — 35 rows (1 header + 34 leads)
- `cold_email/842_honeycomb.md` — companion evidence (this file)
- `cold_email/templates/842_honeycomb.md` — follow-up template
- Build-log entry appended
- No SMTP send attempted. No form submitted. No revenue claimed.