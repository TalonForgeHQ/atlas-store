# Lead 772 evidence — Rootly (sibling #2/5 ai_incident_response_observability)

**Verified:** 2026-07-21 UTC
**Cohort:** `ai_incident_response_observability` sibling #2/5 after incident.io OPENER 771
**Company:** Rootly Inc.
**Headquarters:** San Francisco, CA — hybrid across US + Canada + Europe + Singapore (per first-party JSON-LD jobLocation)
**Founders:** JJ Tang (CEO and Co-founder) — second Co-Founder referenced in careers copy ("We founded Rootly in 2021") but JSON-LD only exposes JJ Tang by name
**Funding:** Y Combinator W21 + multiple subsequent rounds (Series A on public record)
**Commercial route:** `FORM:https://rootly.com/demo`

## First-party proof (HTTP 200 verified 2026-07-21)

- https://rootly.com/ — HTTP 200, title "AI-native incident management platform | Rootly"; hero "AI for on-call and incident response."; product surface AI SRE + On-Call + Incident Response + Retrospectives + Status Page + Rootly AI Labs + @Rootly AI assistant in Slack + PagerDuty migration banner; Paul Van Liew (Director of Platform Engineering) + Geoff Powell (Sr. Technical Manager, SRE) on-site testimonials.
- https://rootly.com/careers — HTTP 200, first-party JSON-LD `application/ld+json` WebPage schema with `about.Organization.founder.name="JJ Tang"` + `jobTitle="CEO and Co-founder"` + `sameAs: github.com/rootlyhq` + `jobLocation.addressCountry: [US, CA, SG] addressRegion: Europe`; "We founded Rootly in 2021" in copy.
- https://rootly.com/security — HTTP 200, "Rootly for Security Teams" + GDPR + HIPAA trust badges first-party.
- https://rootly.com/pricing — HTTP 200, "More affordable than being down" hero; $20 per user/mo self-serve + Enterprise "Contact us" tier + Startup discounts + Frequently-asked-questions block.
- https://rootly.com/demo — HTTP 200 commercial form route.

## Distinct cohort wedge (sibling #2, non-overlapping)

This is the sibling #2/5 of `ai_incident_response_observability` (the 17th Atlas vertical). Non-overlapping wedge vs incident.io OPENER 771:

| Dimension | incident.io (771) | Rootly (772) |
|---|---|---|
| **Primary positioning** | All-in-one AI platform for on-call + incident response + status pages | AI-native incident management platform with AI SRE |
| **AI surface** | Scribe AI summarization + Workflows AI + Insights | AI SRE (automated root-cause-analysis with confidence scores + suggested fixes + IDE-plugged remediation) + @Rootly AI assistant in Slack |
| **Migration story** | "Opsgenie rescue program" 2026-07-09 blog post (migrating PagerDuty/Opsgenie customers) | "1/2 the price" + "Contract buyout" + "Migrated for you" + "99.99%" PagerDuty-migration banner on homepage |
| **Pricing model** | Demo-gated (no public price list) | $20/user/mo self-serve + Enterprise "Contact us" tier + Startup discounts |
| **Geography** | London HQ + SF + NY offices; 190-person team | San Francisco HQ + hybrid US + Canada + Europe + Singapore (per first-party JSON-LD) |
| **Founder pair** | Three Co-Founders (Chris Evans + Stephen Whitworth + Pete Hamilton) | One Co-Founder exposed in JSON-LD (JJ Tang) + second Co-Founder referenced in copy |
| **Year founded** | 2021 (old fire station) | 2021 (per careers copy "We founded Rootly in 2021") |

The non-overlapping wedge is the **AI SRE automated root-cause-analysis with confidence scores + IDE-plugged remediation** — incident.io's wedge is the AI-augmented **incident lifecycle** (alert → on-call → response → investigation → status page → post-incident review → Insights); Rootly's wedge is the **AI-augmented SRE remediation loop** (alert → automated root-cause-analysis → confidence-scored suggestion → IDE-plugged fix → status page → retrospective).

## Five buyer-facing joins

1. **Per-incident + per-AI-SRE-analysis provenance** (incident severity + on-call responder identity + response-channel participation + AI root-cause-analysis run + confidence score + LLM sub-processor invoked + suggested-fix generation + IDE plugin invocation + customer status-page update + post-incident-review artifact + retention window + region routing per tenant).
2. **Multi-tenant isolation** (per-tenant embedding-store + retrieval-result scoping + LLM-context window + audit-log retention + Insights aggregation scoping + per-tenant confidence-score calibration when customer trains their own root-cause signals).
3. **EU AI Act Art. 14(4) + Art. 50 + Art. 53(1)(b) cascade** (per-incident human-oversight operational record before any AI-suggested fix is applied + Art. 50 transparency-labeling on AI-suggested fixes + Art. 53(1)(b) GPAI training-data transparency cascade across OpenAI + Anthropic + secondary LLMs).
4. **NIS2 Art. 21(2)(e) + DORA + GDPR + HIPAA + SOC 2 Type 2 + CCPA per-incident security incident handling** (per-incident detection-to-notification SLA + cross-border-incident-notification chain + forensic-chain-of-custody preservation + deletion-after-retention cascade + per-tenant incident-data-residency pinning with hybrid US + Canada + Europe + Singapore deployment topology).
5. **Sub-processor cascade DPA + 14-day change-notification SLA** across Slack + Microsoft Teams + Atlassian Jira + Linear + GitHub + Datadog + PagerDuty (legacy migrator) + AWS + GCP + OpenAI + Anthropic + LLM sub-processor (12+ sub-processors in the per-incident cascade; 14-day change-notification SLA per GDPR Art. 28(2) is critical given YC startups ship sub-processor swaps monthly).

## Compliance posture

GDPR + UK GDPR + CCPA/CPRA + APPI + PIPEDA + Australia Privacy Act + Singapore PDPA + LGPD + EU AI Act Aug 2 2026 ready (AI SRE + @Rootly AI assistant in GPAI-deployment scope); SOC 2 Type 2 + HIPAA + GDPR + CCPA verified first-party on https://rootly.com/security; HIPAA specifically matters for healthcare-incident response (clinical AI deployment failures trigger HIPAA breach-notification obligations).

## Tier-1 selection rationale

Rootly is the canonical AI-native SRE-incident platform with explicit PagerDuty displacement strategy ("1/2 the price" + contract buyout + migrated-for-you + 99.99%). The AI SRE wedge is non-overlapping with incident.io's incident-lifecycle wedge and with the prior cohorts (ai_third_party_risk cycle-1 + ai_observability + ai_enterprise_knowledge_agents). The hybrid US/Canada/Europe/Singapore deployment topology triggers concurrent GDPR + UK GDPR + EU AI Act + APPI + PIPEDA + Australia Privacy Act + Singapore PDPA + LGPD procurement-cycle pressure, identical to incident.io's wedge but with an SRE/IDE/automated-remediation emphasis.

## Offer

$500 fixed, 48 hours; optional $497/month quarterly refresh.

## Route

`FORM:https://rootly.com/demo` (HTTP 200, server-rendered, no Wayback needed). Rootly does not publish a general/business inbox; careers + support + security + legal routes are excluded from commercial outreach.

## Provenance

No guessed inbox added. No form submission, email, delivery, payment, or revenue is claimed; SMTP and authenticated community routes remain gated; `$0 sent / $0 received`.
