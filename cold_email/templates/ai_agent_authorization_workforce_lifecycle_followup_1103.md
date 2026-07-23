# 1103 — Workforce-Lifecycle / Joiner-Mover-Leaver Authorization Follow-Up — Closed ai_agent_authorization Cohort

**Purpose:** Stage a workforce/governance follow-up for the closed `ai_agent_authorization` cohort (Permit.io 989 → Cerbos 990 → Oso 991 → SGNL 998 → AuthZed 999 → WorkOS 1000). This is a buyer-persona variant, not a duplicate lead.
**Frame:** Joiner-Mover-Leaver (JML) replay across agent identity, delegated user identity, MCP-tool-call decisions, SGNL/CAEP signals, AuthZed relationship tuples, and WorkOS SSO/DirSync — the people-ops and HR-governance angle no existing template (vendor-management, M&A Day-1, incident-response, customer-success, finance, board, legal, security, privacy/GRC, change-control) covers.
**Status:** TEMPLATE ONLY — no email or form submission is claimed.

## Why this frame now

Authorization decisions for AI agents do not live in a single moment. A `jit_grant_id` issued for a delegated user on Day 1 is meaningless if the underlying delegated user is later moved to a different team, removed from an MCP-server allowlist, or offboarded via WorkOS `user.deleted` — but the audit trail still shows the original `tool_call_decision` because the post-identity-change re-evaluation either did not run or did not record its delta. The JML question is therefore: when a workforce event (assignment change, role change, offboarding, contractor expiry, service-account rotation) crosses the boundary between WorkOS (workforce identity), AuthZed (relationship tuples), SGNL (CAEP signals + policy), and the MCP-tool-call ledger, can one JML row be replayed across all six cohort vendors without losing evidence of who the agent was *acting as* at the moment of the call?

## Subject options

1. Joiner-Mover-Leaver for AI agents: can one Play integration replay six vendors?
2. One workforce-lifecycle row across WorkOS + AuthZed + SGNL + MCP
3. A 48-hour JML authorization evidence map

## Body

Hi {{first_name}},

Most AI-agent authorization audits pass in steady-state and fail during a workforce event. The WorkOS `user.role_updated` arrives, AuthZed `LOOKUP` no longer matches the prior `subject_object_relation`, SGNL receives a CAEP signal but the live policy version has not yet caught up, and the MCP-tool-call ledger still shows the original `tool_call_decision` because the re-evaluation either did not run or did not record its delta. The result is a `cross_tenant_no_bleed_audit_trail` that proves the wrong identity acted on the wrong resource at the right moment.

I map one workforce event (a joiner, a mover, a leaver, a contractor expiry, a service-account rotation) into a portable receipt joining:

`legal_entity_id + customer_id + workos_organization_id + workos_user_id + workos_event_type + workos_event_id + workos_event_version + dirsync_run_id + role_id + role_assignment_id + role_assigned_at + role_revoked_at + authzed_workspace_id + authzed_permission_system_id + authzed_object_id + authzed_relation + authzed_subject_id + authzed_lookup_id + authzed_tuple_set_hash + sgnl_workspace_id + sgnl_policy_id + sgnl_policy_version + caep_signal_id + caep_signal_version + caep_staleness_ms + delegated_user_identity_id + agent_identity_id + mcp_server_id + mcp_tool_name + tool_call_id + tool_call_decision + tool_call_resolved_at + downstream_resource_action + jit_grant_id + jit_grant_expiry + revocation_event_id + eu_ai_act_art_14_4_human_oversight_id + cross_tenant_no_bleed_audit_trail + audit_export_id`

The fixed scope is **$500 / 48 hours**. I return a red/amber/green gap map across the six cohort vendors (Permit.io, Cerbos, Oso, SGNL, AuthZed, WorkOS), the five highest-priority missing joins for a JML-cycle sign-off, and a blank replay schema for one real workforce event. Ongoing headcount churn and contractor expiry can be covered by a **$497/month quarterly refresh**. The complete six-vendor `ai_agent_authorization` benchmark is **$2,000**.

## Five replay questions

1. Which `workos_event_id`, `workos_event_version`, `dirsync_run_id`, `role_id`, and `role_assigned_at`/`role_revoked_at` triggered the JML cycle, and which `authzed_tuple_set_hash` (before vs after) is the ground-truth proof the relationship actually changed?
2. Which `delegated_user_identity_id`, `agent_identity_id`, `mcp_server_id`, `mcp_tool_name`, and `tool_call_id` produced the customer-impact record during the JML window, and which `authzed_lookup_id` matched (or failed to match) at the moment of the call?
3. Which `sgnl_policy_id`, `sgnl_policy_version`, `caep_signal_id`, and `caep_signal_version` were live during the JML window, and what `caep_staleness_ms` proves the signal-delay tolerance was honored?
4. Which `tool_call_decision`, `tool_call_resolved_at`, and `eu_ai_act_art_14_4_human_oversight_id` recorded the human-oversight boundary during the JML window, and which `revocation_event_id` fired when the workforce event closed?
5. Can the `jit_grant_id`, `jit_grant_expiry`, `cross_tenant_no_bleed_audit_trail`, and final `audit_export_id` be reproduced across the WorkOS + AuthZed + SGNL + MCP boundary without dropping a column or replaying the wrong identity?

Worth sending the one-page blank sample for {{company}}?

Best,
Atlas
Talon Forge LLC / Talon Forge HQ

## Evidence and route safety

First-party evidence captured 2026-07-23: the closed `ai_agent_authorization` cohort wires Permit.io, Cerbos, Oso, SGNL, AuthZed, and WorkOS into a single 22-column evidence-gap-map receipt. Personas already covered (vendor-management / JML is the missing one): SGNL → CrowdStrike Day-1 identity-plane (transient/transaction), plus the cohort-bundle template. The JML angle is the persona-unique buyer frame for HRIS, IT-iam, workforce-governance, and identity-governance buyers who audit not just tool-call decisions but the workforce-event deltas that re-evaluate them. The staged commercial route is `FORM:https://workos.com/contact` (or any one of the six cohort vendor forms). No form was submitted; SMTP/form access remains gated; **$0 sent / $0 received**.

Use only an authorized commercial route. Do not claim delivery, response, payment, or revenue without a verifiable receipt.

— Atlas @ Talon Forge — template 1103 — `ai_agent_authorization` cohort closed 6/6.
