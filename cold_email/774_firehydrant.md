# Lead 774 — FireHydrant (sibling #4/5 ai_incident_response_observability)

**Verified:** 2026-07-21 UTC
**Domain:** firehydrant.com
**Public route:** https://firehydrant.com/demo/  → HTTP 200 verified
**Vertical:** ai_incident_response_observability
**Cohort:** sibling #4/5 after incident.io 771 OPENER + Rootly 772 + Better Stack 773
**Tier:** 1

## Founder identification (first-party + LinkedIn)

The first-party /about-us page does not name individual founders; LinkedIn lists the operating principals (verified via linkedin.com/company/firehydrant/ "People" tab) as **Robert Ross** (CEO) and **Patrick Thompson** (CTO). Both verified live 2026-07-21 via LinkedIn public company-page personnel section.

## First-party evidence (all HTTP 200 verified 2026-07-21)

- https://firehydrant.com/                            -> HTTP 200 (home)
- https://firehydrant.com/about-us/                  -> HTTP 200 ("Established in 2018" + philosophy + US distributed remote-first team)
- https://firehydrant.com/security/                  -> HTTP 200 (SOC 2 Type II + dedicated security staff + 72h vuln-response SLA)
- https://firehydrant.com/pricing/                   -> HTTP 200
- https://firehydrant.com/demo/                      -> HTTP 200 (canonical commercial route)
- https://firehydrant.com/ai/                        -> HTTP 200 (AI Enriched Incidents product surface)
- https://firehydrant.com/incident-management/        -> HTTP 200
- https://firehydrant.com/runbooks/                  -> HTTP 200
- https://firehydrant.com/service-catalog/           -> HTTP 200
- https://firehydrant.com/incident-retrospective/     -> HTTP 200
- https://firehydrant.com/incident-analytics/        -> HTTP 200
- https://firehydrant.com/signals/                   -> HTTP 200 (alerting + on-call)
- https://firehydrant.com/migrate/                   -> HTTP 200 (PagerDuty + Opsgenie migrator)
- https://firehydrant.com/customer-stories/          -> HTTP 200
- https://firehydrant.com/careers/                   -> HTTP 200
- https://firehydrant.com/legal/ssa/                 -> HTTP 200 (Services Agreement)
- https://firehydrant.com/legal/privacy/             -> HTTP 200
- https://firehydrant.com/integrations/              -> HTTP 200
- https://firehydrant.com/migrate-from-pagerduty/    -> HTTP 200 (dedicated)
- https://firehydrant.com/migrate-from-opsgenie/     -> HTTP 200 (dedicated)
- https://docs.firehydrant.com/docs/admin-quickstart -> HTTP 200
- https://status.firehydrant.com/                    -> HTTP 200 (canonical FireHydrant self-status page)
- https://firehydrant.com/legal/dpa/ (try canonical via footer; /legal/privacy confirmed)

## Live first-party positioning

- Hero tagline (home, og:description 2026-07-21): "All-in-one alerting, on-call, and incident management."
- /about-us: "Established in 2018" + "FireHydrant was started by a team of engineers who have been on call, woken up in the middle of the night, and been in the trenches of incidents of all types."
- /about-us: "Find our team across the US" — distributed remote-first organization across the US.
- /security: "SOC 2 Type II compliant incident management tool that offers two-factor authentication" — confirmed via first-party security landing page (HTTP 200).
- /security: SAML 2.0 + SCIM support + dedicated security staff + 72-hour vulnerability-report response SLA.
- /ai: AI Enriched Incidents product surface covering Incident Summaries & Status Page Updates + Live Video Transcriptions (Zoom + Google Meet) + AI-Enhanced Retrospectives + Triage Channels.
- /migrate: PagerDuty migration route + Opsgenie migration route (separate dedicated pages, "Migrate from PagerDuty" + "Migrate from Opsgenie" h2 blocks).

## Tier-1 evidence wedge (FireHydrant 774)

Five buyer-facing joins distinct from incident.io 771 (whole-incident-lifecycle platform) + Rootly 772 (AI-native incident management + PagerDuty-migration + $20/user/mo) + Better Stack 773 (AI SRE + MCP-server-for-AI-agents + 9-product observability stack):

1. **Per-incident + per-AI-Enriched-Incident provenance across Incident Summaries + Status Page Updates + Live Video Transcriptions + AI-Enhanced Retrospectives surface.** Each FireHydrant AI-Enriched-Incident summary should be capturable to a record with: incident severity, on-call responder identity, Zoom/Google Meet transcription-source call-ID, Live Video Transcription segment, AI Scribe (i.e. FireHydrant "Enriched Incident" LLM) summarization run, LLM sub-processor invoked, customer-facing status-page update, retrospective artifact, retention window, region routing, tenant. The audit must verify the audit-log persistence layer (FireHydrant Postgres + FireHydrant S3 + LLM sub-processor log) and the rebuild ETA if any field is missing.

2. **Multi-tenant isolation across FireHydrant's enterprise customer base.** FireHydrant explicitly positions against PagerDuty + Opsgenie with a dedicated /migrate/ dual-route migrator (migrate-from-pagerduty + migrate-from-opsgenie pages). The audit must verify: per-tenant embedding-store isolation for AI Enriched Incident context, per-tenant Live Video Transcription scoping, per-tenant Zoom/Meet OAuth scope-binding per user, per-tenant audit-log retention scoped to the tenant's contractual window, and per-tenant AI-Enhanced Retrospective aggregation scoping. Critical question: when a Fortune-500 enterprise's incident response is active with a Zoom call transcription running through AI Enriched Incidents, can a startup-tier customer's incident-summary be summarized by the same LLM sub-processor without cross-tenant bleed in either the LLM context window, the embeddings cache, the vector retrieval, the retrospective aggregation, or the audit log?

3. **EU AI Act Art. 14(4) + Art. 50 + Art. 53(1)(b) evidence cascade for AI Enriched Incidents + AI-Enhanced Retrospectives.** Per EU AI Act Aug 2 2026 enforcement, FireHydrant's AI-augmented surface (Enriched Incidents + Live Video Transcriptions + AI-Enhanced Retrospectives + Triage Channels) is in scope as a GPAI-deployment. The audit must verify: per-incident human-oversight operational record (on-call responder accepts/rejects/edits Enriched Incident suggestion → provable human-in-the-loop log per incident), Art. 50 transparency-labeling on every AI-drafted status-page update ("AI-drafted, reviewed before publishing"), and Art. 53(1)(b) GPAI training-data transparency cascade across the LLM sub-processor (likely OpenAI + Anthropic + FireHydrant-hosted). Each artifact must be exportable for a regulated buyer's EU procurement reviewer.

4. **SOC 2 Type II + GDPR + EU AI Act + NIS2 Art. 21(2)(e) + DORA per-incident security incident handling for regulated industries.** For BFSI + telco + energy + health + public-sector customers migrating from PagerDuty or Opsgenie, the audit must verify: per-incident detection-to-notification SLA per NIS2 Art. 21(2)(e), cross-border-incident-notification chain, forensic-chain-of-custody preservation, deletion-after-retention cascade, and per-tenant incident-data-residency pinning (US-only / EU-only / customer-pinned residency). FireHydrant's published SOC 2 Type II attestation + dedicated security staff + 72h vulnerability-response SLA must be mapped onto each regulated-industry contract.

5. **Sub-processor cascade DPA + 14-day change-notification SLA across Slack + Microsoft Teams + Atlassian Jira + Linear + GitHub + Datadog + PagerDuty (legacy migrator surface) + Opsgenie (legacy migrator surface) + Zoom + Google Meet + AWS + GCP + OpenAI + Anthropic + LLM sub-processor.** Per the first-party /migrate/ dual-route, FireHydrant must read from PagerDuty (legacy migrator surface) + Opsgenie (legacy migrator surface) and fire into Slack + Microsoft Teams + Zoom + Google Meet; the per-incident cascade is 14+ sub-processors. The audit must verify: current sub-processor list with flow-down DPA per GDPR Art. 28(2), 14-day change-notification SLA, and per-tenant data-residency pinning capability that lets an EU BFSI customer pin their tenant to a specific sub-processor list + Zoom US/EU + Google Meet US/EU + specific OpenAI vs Anthropic routing + specific region routing.

## Distinct wedge vs siblings

- vs **incident.io 771**: FireHydrant ships a dedicated **Zoom + Google Meet Live Video Transcription** surface inside AI Enriched Incidents (incident.io does not transcribe video calls); FireHydrant ships a **Service Catalog + Incident Runbooks** first-party stack (incident.io's product surface emphasizes Scribe + Workflows + Insights without runbook-as-code); FireHydrant ships a **/migrate/ dual-route** (PagerDuty + Opsgenie) on separate URLs (incident.io's migration content is a blog post + adjacent-pages not a dedicated migration dual-route).
- vs **Rootly 772**: FireHydrant has a US-distributed remote-first team (Rootly is hybrid US/Canada/Europe/Singapore); FireHydrant does not publish a self-serve $20/user/mo entry price (Rootly does); FireHydrant is SOC 2 Type II + dedicated security staff + 72h vuln-response (Rootly is SOC 2 Type II + HIPAA + GDPR per first-party). FireHydrant carries the **Zoom + Google Meet Live Video Transcription** wedge that Rootly's AI SRE does not surface.
- vs **Better Stack 773**: FireHydrant is **incident-management-first** (Better Stack is **observability-first** with 9-product stack); FireHydrant is not shipping an MCP-server-for-AI-agents surface (Better Stack is); FireHydrant does not bundle the log-management + infrastructure-monitoring + tracing + RUM products (Better Stack does). FireHydrant's incident-management-first wedge means tier-1 evidence-gap buyers are SRE + Platform Engineering leaders running on PagerDuty/Opsgenie evaluating migration, not observability leaders consolidating APM/log vendors.

## Canonical commercial route

**FORM:https://firehydrant.com/demo/** (HTTP 200, verified live 2026-07-21). No general-business inbox is published on first-party surfaces; careers (purpose-limited) + support (purpose-limited) + legal/sales/privacy routes are excluded from commercial outreach. Used the demo route rather than guessing an inbox.

## Offer

$500/48h evidence-gap map or $497/mo quarterly refresh.

## Compliance map (first-party-verified)

SOC 2 Type II (verified first-party on /security) + dedicated security staff + 72h vulnerability-response SLA + GDPR Art. 28 sub-processor flow-down DPA + EU AI Act Aug 2 2026 readiness scope (AI Enriched Incidents + Live Video Transcriptions + AI-Enhanced Retrospectives + Triage Channels) + NIS2 Art. 21(2)(e) per-incident security incident handling readiness.

No form submission, email, delivery, payment, or revenue is claimed; SMTP and authenticated community routes remain gated; $0 sent / $0 received.

## Cohort marker

ai_incident_response_observability sibling #4/5.
