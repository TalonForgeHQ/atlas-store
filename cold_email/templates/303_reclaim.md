---
template_id: 303
company: Reclaim.ai
handle: @reclaimai
vertical: b2b_saas
tier: 1
index: 215
---

**Subject:** Reclaim + AI agents — vendor-DD inbound (SOC 2 + GDPR DPA + EU AI Act)

Hi {{founder_first_name | "Henry"}},

Following the {{funding_round}} {{date}} announcement — quick vendor-DD question on the {{vertical}} side, not the typical "AI for X" pitch.

We're running an AI-agent pipeline that needs to invoke {{company}}'s calendar/scheduling API (`https://{{domain}}/api/v2/...`) from 200+ production agent loops per day (Reclaim Calendar events + Reclaim Planner tasks + Reclaim Habits routines + Reclaim Chat AI-scheduling sessions, with per-agent dry-run/promote state). Before we wire it in, three checks your security/compliance page already answers but a vendor-DD reviewer will still ask:

1. **SOC 2 Type II + GDPR DPA + EU AI Act Annex IV readiness** — confirmed on {{domain}}/security + {{domain}}/privacy + {{domain}}/dpa. Do you have the latest bridge letter available on request, or is it sufficient for the {{company}} side that we reference the audit report SHA + the DPA execution date in our `data/policies/vendor_register.md`?
2. **Per-tenant API token scoping** — when 200+ agents share a service account, do you expose a per-integration `X-Reclaim-Integration-Id` header (or equivalent) for log attribution + per-agent audit trail? We're trying to avoid the "one shared token = one global audit subject" failure mode that hits every other calendar-API we wire into.
3. **EU AI Act high-risk scheduling decisions** — Reclaim's auto-scheduler ranks meetings/tasks by priority and re-books on conflict. If we invoke that from an EU-resident agent, does {{company}} classify the output as a "decision" under Article 22 / Annex III, or is the agent considered the decision-maker with {{company}} as a downstream tool? We've seen vendor-DD split on this and want to land on the side that matches your compliance posture.

The three docs above should answer 90% — for the residual 10% I'm happy to send a one-page DDQ that your team can return in async form.

Best,
Atlas
Talon Forge LLC
https://{{domain}}/security
https://{{domain}}/privacy