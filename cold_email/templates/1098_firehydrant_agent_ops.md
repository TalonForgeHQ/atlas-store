# Lead 1098 — FireHydrant (CLOSER #5/5 ai_agent_operations)

**Subject lines:**
1. FireHydrant runbook → retrospective evidence map — $500/48h
2. Runbook steps + status page + retros replay for FireHydrant
3. FireHydrant vs Resolve AI vs incident.io vs Rootly vs Causely — $2,000 benchmark

Hi {{first_name}},

FireHydrant's cohort-unique wedge is the runbook-as-primary-key: the replay can show which `runbook_id` + `runbook_step_id` + `runbook_step_execution_id` translated a `service_catalog_id` ownership change into a `status_page_incident_id` update and which `retrospective_id` + `retrospective_action_item_id` closed the loop after the incident.

A fixed-scope FireHydrant evidence-gap map is **$500 / 48 hours** — one normalized production replay with the 20-column receipt joining tenant, organization, incident, runbook, runbook step, runbook execution, service catalog, service owner, on-call schedule, escalation policy, alert source, status page incident, status page component, retrospective, retrospective action items, human override, and audit export.

For teams comparing the whole ai_agent_operations landscape, Atlas also offers a **$497/month quarterly refresh** or a **$2,000 five-vendor benchmark** covering Resolve AI, incident.io, Rootly, Causely, and FireHydrant.

Commercial route: `FORM:https://firehydrant.com/demo` — verified first-party demo page; JS-rendered form not submitted. The normalized replay ends at `audit_export_id` for a portable evidence handoff.

— Atlas @ Talon Forge

## Five replay questions

1. Which `runbook_id` and `runbook_step_id` triggered when the alert fired, and which `runbook_step_execution_id` recorded the actual sequence?
2. Which `service_catalog_id` + `service_owner_id` + `service_tier` owned the affected service, and which `escalation_policy_id` fired first?
3. Which `status_page_incident_id` + `status_page_component_id` was published, and which subscribers were notified?
4. Which `retrospective_id` + `retrospective_template_id` was opened, and which `retrospective_action_item_id` was assigned?
5. Which `human_override_id` approved or stopped the runbook step, and can the audit export reproduce the chain with no cross-tenant bleed?

## Evidence and compliance posture

- First-party title/description: "All-in-One Alerting, On-Call, and Incident Management | FireHydrant"; smart alerting, on-call scheduling, AI-powered workflows, post-incident retros; AI Insights + AI Enriched Incidents named surfaces.
- First-party security: SOC 2 Type II named verbatim in the security page meta description.
- First-party leadership: Robert Ross, FireHydrant Co-Founder & CEO, bylined author at firehydrant.com/blog/firehydrant-to-be-acquired-by-freshworks/.
- First-party M&A: FireHydrant announced its planned acquisition by Freshworks on 2025-12-15, with FireHydrant planned to become the Incident Management and Reliability layer inside Freshservice; deal expected to close at the beginning of Q1 2026.

**Verification:** mailto:NONE; SMTP/form gated; `$0 sent / $0 received`. CLOSER #5/5, canonical slug `closer-5-of-5`.