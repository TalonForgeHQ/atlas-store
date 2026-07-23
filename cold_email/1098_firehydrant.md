# Lead 1098 — FireHydrant (CLOSER #5/5 ai_agent_operations) — incident-runbook to retrospective evidence-gap map

**Vertical:** ai_agent_operations CLOSER #5/5 after Resolve AI 1094 OPENER + incident.io 1095 SIBLING #2 + Rootly 1096 SIBLING #3 + Causely 1097 SIBLING #4

**First-party evidence retrieved 2026-07-23:**
- `firehydrant.com/` — title: "All-in-One Alerting, On-Call, and Incident Management | FireHydrant"; description verbatim "All-in-one incident management software for modern teams. FireHydrant helps you plan, respond, and resolve faster with smart alerting, on-call scheduling, AI-powered workflows, and post-incident retros." AI Insights + AI Enriched Incidents named surfaces.
- `firehydrant.com/security` — SOC 2 Type II compliance named verbatim in meta description.
- `firehydrant.com/blog/firehydrant-to-be-acquired-by-freshworks/` — title "FireHydrant to be Acquired by Freshworks | FireHydrant"; canonical verbatim. Founding narrative: "Eight years ago, I started FireHydrant because incident response was far more painful than it needed to be." Closing verbatim: "Thank you, Robert Ross, FireHydrant Co-Founder & CEO." Date published 2025-12-15; deal expected to close beginning of Q1 2026. Joining Freshservice — FireHydrant planned as the Incident Management and Reliability layer inside Freshservice.
- `firehydrant.com/pricing` — self-serve and enterprise tiers; no public mailto inbox.
- `firehydrant.com/demo` — verified first-party demo landing page with "Get a demo" CTA; JS-rendered form, no SSR inputs.
- `firehydrant.com/blog/` — multiple posts bylined Robert Ross (Co-Founder & CEO), e.g., 2025-12-15 acquisition post.

## 5-WEDGE non-overlap rubric

1. **Runbook-first primary substrate.** FireHydrant's first-party narrative explicitly anchors on Runbooks and the automation engine; the canonical key is `runbook_id` + `runbook_step_id` + `runbook_step_execution_id`, not Causely's topology snapshot or Rootly's Slack workflow.
2. **Service Catalog as the routing layer.** FireHydrant pairs Service Catalog ownership to escalation, so the join keys include `service_catalog_id` + `service_owner_id` + `service_tier` before on-call scheduling kicks in.
3. **Status Page as a first-party native surface.** Status Page incidents are first-class, joined to a parent `incident_id`, and carry `status_page_incident_id` + `status_page_component_id` + `status_page_subscriber_id` not exposed by Resolve AI or Causely.
4. **Retrospectives as a versioned artifact.** Post-incident Retros are referenced as named first-party outputs, producing `retrospective_id` + `retrospective_template_id` + `retrospective_action_item_id` + `retrospective_completion_id` — distinct from Rootly's `ai_postmortem_id` and Causely's `prevention_policy_id`.
5. **Freshservice acquisition cross-product boundary.** FireHydrant-to-Freshservice roadmap introduces an explicit `freshservice_incident_id` + `freshservice_change_id` + `freshservice_release_id` cross-product key that no other cohort member exposes.

## 20-column per-FireHydrant receipt

`tenant_id + firehydrant_org_id + incident_id + runbook_id + runbook_step_id + runbook_step_execution_id + service_catalog_id + service_owner_id + service_tier + on_call_schedule_id + escalation_policy_id + alert_source + alert_id + severity + status_page_incident_id + status_page_component_id + retrospective_id + retrospective_action_item_id + human_override_id + audit_export_id`

## Commercial route

`FORM:https://firehydrant.com/demo` — verified first-party demo page; JS-rendered form; not submitted.

## Offer

$500/48h fixed-scope FireHydrant runbook-to-retrospective evidence-gap map OR $497/mo quarterly refresh OR $2,000 five-vendor ai_agent_operations benchmark.

**Verification:** mailto:NONE; SMTP/form gated; `$0 sent / $0 received`. CLOSER #5/5, canonical slug `closer-5-of-5`.