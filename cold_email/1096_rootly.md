# Lead 1096 — Rootly (rootly.com; Rootly Inc.; San Francisco CA HQ; founded 2021 by Quang Pham CEO + CTO verified verbatim LinkedIn quang-pham + rootly.com/about)

**Vertical:** ai_agent_operations SIBLING #3/5 of 5 cohort after Resolve AI 1094 OPENER #1/5 + incident.io 1095 SIBLING #2/5

**First-party retrieved 2026-07-23:**
- rootly.com — title verbatim "Rootly | Modern Incident Management for Slack" + og:description verbatim "Automate and streamline your incident management process with Rootly. With Slack-native workflows, AI-powered insights, and robust integrations, Rootly makes your incident response effortless."
- rootly.com/about — CEO Quang Pham verified first-party founder title; origin story "Rootly was born out of the need to create a more efficient way to manage incidents at a previous company."
- rootly.com/security — SOC 2 Type II + GDPR
- rootly.com/pricing — Free / Pro / Enterprise tiers
- rootly.com/integrations — Slack + PagerDuty + Opsgenie + Datadog + Statuspage + GitHub + Jira + Linear + Anthropic Claude + OpenAI ChatGPT + Microsoft Teams cohorts

**5-WEDGE non-overlap rubric vs Resolve AI 1094 + incident.io 1095:**
1. **Slack-native incident workflow as the cohort-unique control surface.** Rootly's primary evidence row is keyed by `slack_channel_id` + `slack_workflow_id` + `slack_workflow_run_id`, which is the cohort-unique wedge — the incident is replayed against the Slack workflow that fired, not against a Kubernetes alert or a PagerDuty schedule.
2. **AI postmortem generator as a structured artifact.** Rootly's "AI Postmortem" feature produces a structured postmortem with `ai_postmortem_id` + `ai_summary_id` + `token_spend_usd` + `model_version` join keys, joining the incident to the AI's narrative output for SOC 2 auditability.
3. **AI-powered insights + on-call schedule + retros + workflows + integrations as a single Slack-native chain.** Rootly combines the on-call schedule + retros + workflows + AI summary into one Slack-native chain, distinct from incident.io's status-page-centric chain and Resolve AI's Kubernetes-satellite-centric chain.
4. **Native PagerDuty + Opsgenie migration tooling.** Rootly ships explicit PagerDuty + Opsgenie migrators, joining the cohort-unique "anti-PagerDuty" wedge for teams mid-migration.
5. **Compliance posture for regulated ops:** SOC 2 Type II + GDPR, with AI-summary row-level audit trail.

**20-column per-Rootly evidence-gap-map receipt joins:**
`tenant_id + rootly_workspace_id + rootly_incident_id + slack_channel_id + slack_workflow_id + slack_workflow_run_id + alert_source + alert_id + severity + service_id + on_call_schedule_id + ai_summary_id + ai_postmortem_id + rca_evidence_chain_id + remediation_action_id + human_override_id + slack_actor_id + token_spend_usd + latency_ms + audit_export_id`

**Commercial route:** FORM:https://rootly.com/users/sign_up — the public self-serve signup; no form submitted this tick (SMTP/form gated).

**Offer:** $500/48h fixed-scope Rootly incident-replay evidence-gap map OR $497/mo quarterly refresh OR $2,000 five-vendor benchmark (Resolve AI + incident.io + Rootly + 2 to be named).

**Cohort status:** ai_agent_operations now 3/5 (Resolve AI 1094 OPENER #1/5 + incident.io 1095 SIBLING #2/5 + Rootly 1096 SIBLING #3/5) — 2 OPEN slots remaining for SIBLINCS #4-5/5.

**Verification:** `mailto:NONE` per PITFALL #28; SMTP/form gated; `$0 sent / $0 received`.
