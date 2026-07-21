# Lead 771 — incident.io (OPENER #1/5 ai_incident_response_observability)

**Verified:** 2026-07-21 UTC
**Cohort:** `ai_incident_response_observability` OPENER #1/5 (NEW VERTICAL cohort)
**Company:** Incident.io Limited (incident.io)
**Headquarters:** London, UK (with offices in San Francisco + New York); team of 190 across UK + US
**Founders:** Chris Evans, Stephen Whitworth, Pete Hamilton — three Co-Founders; founded 2021 in a rented room in an old fire station
**Customer base:** 1,000+ companies including **Netflix, Airbnb, Block** (named on the first-party About page); Zendesk (1,200+ engineers), Intercom published as case studies
**Commercial route:** `FORM:https://incident.io/get-a-demo` + first-party `https://incident.io/` (Start a free trial CTA)
**Founding story:** "In 2021, we quit our jobs, rented a room in an old fire station and set out to build the platform we'd always wanted to use."

## First-party proof

The following first-party pages and structured-data fields were checked directly on 2026-07-21:

- https://incident.io/ — HTTP 200, title "All-in-one incident management platform | incident.io"; hero copy "Move fast when you break things" + sub-hero "The all-in-one AI platform for on-call, incident response, and status pages—built for fast-moving teams"; primary CTAs "Get a demo" + "Start a free trial"; product surface covers **On-call + Response + Investigations + Status Pages + AI + Catalog + Scribe + Workflows + Insights + Integrations**; positioning on **G2 reviews** (Leading Incident Management badge matrix), Zendesk case study ("ditched 15 years of patchwork tooling, in 10 weeks" + "If you took incident.io away tomorrow, we'd really struggle. It's foundational to our incident response" — Anna Roussanova, Engineering Manager), Intercom case study.
- https://incident.io/careers — HTTP 200, title "Careers | incident.io"; "A note from the founders" section explicitly names the three Co-Founders Chris Evans + Stephen Whitworth + Pete Hamilton, founding year 2021, "old fire station" origin story; names 1,000+ companies + Netflix + Airbnb + Block as customers; declares 190-person team across London + San Francisco + New York; lists "Product Development" / "Go To Market" / "Business Operations" departments in the team-by-area tab; "See open roles" CTA; canonical values: Make it magic / Find a way / Raise the pace / Trust by default / Win together.
- https://incident.io/contact — HTTP 200, "Get a demo" commercial form route.
- https://incident.io/security — HTTP 200, SOC 2 + GDPR + ISO 27001 trust badges on first-party security posture page.

## Distinct cohort wedge (opener)

This is the **OPENER** of the `ai_incident_response_observability` vertical — a non-overlapping AI-era procurement lane distinct from the previously-closed cohorts:

- `ai_third_party_risk` cycle-1 (Whistic 746 + SecurityScorecard 747 + UpGuard 748 + BitSight 749) covers vendor-risk-assessment workflows against third-party questionnaires + security ratings.
- `ai_observability` (Arize 632 + LangSmith 635 + Langfuse 636 + Honeycomb 637 + Sentry 638 + Datadog 639) covers LLM-trace + APM telemetry for engineering teams.
- `ai_incident_response_observability` (this new vertical) covers the **incident response + on-call + status pages + post-incident review + AI-assisted runbook + AI-suggested remediation** workflow that spans SRE + Engineering + Product + Support + Customer Success + Legal+Compliance — incident.io's wedge is the **unified platform for the whole incident lifecycle** (alert → on-call → response → investigation → status page → customer comms → post-incident review → Insights), not just the on-call schedule that PagerDuty pioneered nor the LLM-trace that Honeycomb/Sentry serve. The AI layer is incident.io Scribe (AI-assisted incident summarization) + Workflows (AI-suggested automation) + Insights (AI-derived incident-pattern analysis) + AI-assisted Status Page generation.

## Five-question audit scope

1. **Per-incident + per-AI-summary provenance.** Can one record join incident severity + on-call responder identity + response-channel participation (Slack/Teams) + AI Scribe summarization run + LLM sub-processor invoked + customer-facing status-page update + post-incident-review artifact + retention window + region routing + tenant for every incident event?
2. **Multi-tenant isolation across 1,000+ customer base.** When a Netflix-scale incident response is active, can a Block-scale customer incident-summary be summarized by the same LLM sub-processor without cross-tenant bleed in either the LLM context window, the embeddings cache, the vector retrieval, the post-incident insights aggregation, or the audit log?
3. **EU AI Act Art. 14(4) + Art. 50 evidence cascade for AI Scribe + AI Workflows.** Per EU AI Act Aug 2 2026 enforcement, incident.io's AI-assisted surface (Scribe + Workflows + Insights) is in scope as a GPAI-deployment. The audit must verify: per-incident human-oversight operational record (the on-call Incident Commander accepts/rejects/edits AI Scribe suggestions → provable human-in-the-loop log per incident), Art. 50 transparency-labeling on every AI-generated status page update ("AI-drafted, reviewed before publishing"), and Art. 53(1)(b) GPAI training-data transparency cascade across OpenAI / Anthropic / Google / self-hosted LLM sub-processors.
4. **NIS2 Art. 21(2)(e) + DORA + ISO 27001 + SOC 2 Type II per-incident security incident handling.** incident.io serves customers in BFSI + telco + energy + health + public sector — all in NIS2 + DORA + sectoral-regulation scope. The audit must verify: per-incident detection-to-notification SLA per Art. 21(2)(e), per-incident cross-border-incident-notification chain, per-incident forensic-chain-of-custody preservation, per-incident deletion-after-retention cascade, and per-tenant incident-data-residency pinning (US-only / EU-only / UK-only).
5. **Sub-processor cascade DPA + 14-day change-notification SLA across Slack + Microsoft Teams + Atlassian Jira + Linear + GitHub + Datadog + PagerDuty (legacy migrator) + AWS + GCP + OpenAI + Anthropic + LLM sub-processor.** incident.io's incident-response orchestration layer fires into Slack + Teams (per first-party home page), reads from Datadog + PagerDuty (legacy migrator), writes to Jira + Linear + GitHub (per integrations catalog), and runs AI Scribe + Workflows + Insights over OpenAI + Anthropic + Google + self-hosted LLM sub-processors — 12+ sub-processors in the per-incident cascade. The audit must verify: current sub-processor list with flow-down DPA per GDPR Art. 28(2), 14-day change-notification SLA, and per-tenant data-residency pinning capability (US-only / EU-only / UK-only / customer-pinned residency) that lets an EU BFSI customer pin their tenant to a specific sub-processor list + specific region routing.

## Compliance map

GDPR + UK GDPR + CCPA/CPRA + APPI + PIPEDA + Australia Privacy Act + Singapore PDPA + LGPD + EU AI Act Aug 2 2026 ready (AI Scribe + Workflows + Insights in GPAI-deployment scope); SOC 2 Type II + ISO 27001 verified on incident.io/security (live 2026-07-21); NIS2 Art. 21(2)(e) + DORA Art. 17-19 + PCI DSS scope-minimization for BFSI customers; HIPAA BAA availability for healthcare customers; sub-processor cascade DPA + 14-day change-notification SLA are the audit gaps to verify for the YanXbt 5-client $497/mo pattern target.

## Commercial posture

Canonical route: `FORM:https://incident.io/get-a-demo` + first-party `https://incident.io/` Start a free trial CTA. No general/business inbox is published; careers + support + security + legal routes are excluded from commercial outreach. No email, form submission, demo request, trial activation, or revenue is claimed in this cron tick.

Offer: $500 fixed-scope 48-hour evidence-gap map or $497/month quarterly refresh.
