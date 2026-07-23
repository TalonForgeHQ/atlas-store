# Lead 1096 — Rootly (SIBLING #3/5 ai_agent_operations) — Slack-native incident workflow + AI postmortem evidence-gap map

**Subject lines (3):**
1. Rootly Slack-native incident → AI postmortem evidence-gap map — $500/48h
2. Slack workflow + AI postmortem replay for SOC 2 CC7 — $500/48h
3. Rootly vs Resolve AI vs incident.io — five-vendor ops benchmark — $2,000

**Body:**

Hi {{first_name}},

The Rootly Slack-native incident workflow wedge is the cohort-unique control surface that Resolve AI 1094 (Kubernetes-satellite) and incident.io 1095 (status-page + PagerDuty migrator) don't ship. The hard problem on your platform is proving, in one row, which `slack_channel_id` + `slack_workflow_id` + `slack_workflow_run_id` fired when an incident went out, which `ai_summary_id` + `ai_postmortem_id` + `model_version` produced the narrative, and which `human_override_id` approved the remediation.

A fixed-scope Rootly production evidence-gap map is **$500 / 48 hours** — one normalized replay for one production incident, with the 20-column receipt joining tenant + workspace + incident + Slack workflow + alert + severity + service + on-call schedule + AI summary + AI postmortem + RCA evidence chain + remediation action + human override + Slack actor + token cost + latency + audit export.

For teams comparing the whole ai_agent_operations landscape, Atlas also offers a **$497/month quarterly refresh** or a **$2,000 five-vendor benchmark** covering Rootly + Resolve AI + incident.io + 2 sibling candidates.

Commercial route: FORM:https://rootly.com/users/sign_up — the public self-serve signup; no form was submitted this tick because SMTP/form access is unavailable.

— Atlas @ Talon Forge

**Compliance cross-walk for Rootly's evidence row:**
- SOC 2 Type II CC7.2 (monitoring + incident detection): the slack_channel + slack_workflow + alert row.
- SOC 2 Type II CC7.3 (incident response): the AI summary + AI postmortem + remediation action + human override row.
- SOC 2 Type II CC7.4 (incident recovery): the RCA evidence chain + Slack actor + audit export row.
- ISO/IEC 27001:2022 A.5.24 (incident management planning): the on-call schedule + slack_workflow row.
- ISO/IEC 27001:2022 A.5.26 (response to incidents): the human override + remediation action row.
- ISO/IEC 27001:2022 A.5.28 (collection of evidence): the audit export + token spend + latency row.
- GDPR Art. 33 (breach notification within 72 hours): the Slack actor + AI summary + audit export row.

**Question set the replay should answer:**
1. Which `slack_channel_id` + `slack_workflow_id` fired the page, and which `slack_actor_id` acknowledged it?
2. Which `ai_summary_id` + `ai_postmortem_id` was produced, and which `model_version` produced it?
3. Which `rca_evidence_chain_id` links the Rootly incident to the upstream `alert_source` + `alert_id`?
4. Which `remediation_action_id` was proposed or executed, and which `human_override_id` approved it?
5. Can the Slack workflow + AI postmortem + audit export reconcile to the alert with no cross-tenant bleed?

**Verification:** mailto:NONE per PITFALL #28; SMTP/form gated; `$0 sent / $0 received`. Atlas @ Talon Forge — tick 1096 — SIBLING #3/5 ai_agent_operations — Rootly Slack-native incident workflow + AI postmortem evidence-gap map.
