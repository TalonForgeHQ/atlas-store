# Temporal — durable-execution audit opener (SIBLING #2/5)

**Vertical:** ai_workflow_orchestration
**Cohort slot:** SIBLING #2/5 after Kestra 1161 (OPENER #1/5)
**First-party route:** https://temporal.io/get-cloud
**Offer:** $500 / 48h fixed-scope audit · $497/mo refresh · $2,000 five-vendor cohort benchmark

## Subject options

1. A 22-column receipt for Temporal workflow history
2. Map your Temporal Cloud audit trail in 48 hours
3. Durable execution needs a buyer-ready control matrix

## Email

Hi Samar —

Temporal persists workflow state and event history so a million-workflow fleet can recover mid-flight. Enterprise buyers still ask a narrower evidence question: can one exported record explain which workflow ran, which code and worker handled it, which activities retried, which signals and updates changed state, and which operator cancelled the run?

I can map that evidence gap in 48 hours for $500, or maintain it quarterly for $497/month. The output is a buyer-ready control matrix — not a Temporal replacement — and it will benchmark Temporal against the emerging five-vendor workflow-orchestration cohort.

Worth sending the five-question scope?

— Atlas

## Personalization evidence

- First-party `temporal.io/about` JSON-LD `@type:Organization` block lists Samar Abbas and Maxim Fateev as `@type:Person` founders and Temporal Technologies as the parent organization. Extracted 2026-07-24.
- The same first-party page lists Samar Abbas as **CEO & Co-Founder** and credits his work on Amazon Simple Workflow Service, Azure Durable Task Framework, and Cadence at Uber.
- The same first-party page lists Maxim Fateev as **CTO & Co-Founder** and credits his work on AWS Simple Workflow Service, Amazon SQS storage backend, Uber Cherami, and Cadence.
- First-party address from JSON-LD: `2337 148th Ave NE, #1335, Bellevue, WA 98007, US`.
- First-party `foundingDate` from JSON-LD: `2019-10-14`.
- First-party customer logos on `/about`: OpenAI (Venkat Venkataramani, ex-Rockset), HashiCorp (Mitchell Hashimoto), Netflix (Rob Zienert), Snap (Arash Fallah), Descript, Yum! Brands, Stripe, Datadog, Green Got.
- First-party investor list on `/about`: a16z, Tiger Global, Madrona, Stepstone, Amplify, Index Ventures, Sapphire Ventures, MongoDB, GIC, Sequoia, Conversion Capital, Hanwha, Lightspeed, 137 Ventures.
- First-party numbers on `/about`: **22,000+ Community Members · 2,900+ Customers · 1 Trillion Monthly Actions**.
- First-party commercial route from the homepage CTA: `https://temporal.io/get-cloud`.

## Evidence receipt proposed

`temporal_namespace_id` + `workflow_id` + `workflow_run_id` + `workflow_type` + `event_history_id` + `event_id` + `event_type` + `activity_id` + `activity_attempt` + `retry_policy_version` + `task_queue_id` + `worker_build_id` + `deployment_version` + `schedule_id` + `signal_id` + `update_id` + `search_attribute_set_id` + `cancellation_id` + `termination_id` + `operator_identity` + `audit_export_id` + `retention_policy_version`

## 5-WEDGE non-overlap vs Kestra 1161

1. Durable execution (workflow + activity + retry + replay) vs Kestra's declarative event-driven trigger bus.
2. First-party JSON-LD founder attribution (Samar + Maxim) on `/about` is unique to Temporal in the cohort.
3. First-party "1 Trillion Monthly Actions" production-scale card is unique to Temporal in the cohort.
4. Customer logos including OpenAI + HashiCorp + Netflix + Snap + Stripe + Datadog sit directly on the `/about` page, distinct from Kestra's Algolia/Datadog/dbt/Airbyte investor syndicate.
5. Customer-controlled worker + namespace + task-queue + worker-build-id substrate via `docs.temporal.io/cloud` and `cloud.temporal.io`, distinct from Kestra's 1,200+ plugin execution substrate.

## Guardrails

- Draft only; no form submitted and no email sent.
- Do not infer a public sales mailbox at `@temporalio.com` or `sales@temporal.io` — the homepage routes through the `get-cloud` form.
- Temporal is positioned as SIBLING #2/5 after Kestra 1161 OPENER #1/5; siblings #3-5/5 to follow.
- $0 sent / $0 received; SMTP remains gated.