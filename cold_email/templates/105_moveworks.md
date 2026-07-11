# 105_moveworks.md — Moveworks (moveworks.com)

**To:** info@moveworks.com (Bhavin Shah, CEO; or product-security / GRC lead)
**Subject:** The IT-helpdesk AI agent write-side is the SOC 2 + ISO 27001 audit gap, plus the prompt-injection attack surface
**Vertical:** it_ops_ai

---

Hi Bhavin,

Moveworks' positioning — autonomous IT-helpdesk agents that reset passwords, unlock accounts, provision/deprovision SaaS licenses, and run change-management tickets across Active Directory + Okta + Workday + ServiceNow — is the highest-stakes write-side agent deployment in enterprise AI right now. Customers like Cisco, Databricks, LinkedIn, Honeywell, and Broadcom all run their employee-facing IT support through Moveworks today.

The 2026 audit gap is two-sided. **First**, every SOC 2 + ISO 27001 + ITIL change-management audit asks the same 5 questions about the change-record join-table between Moveworks' decision + the source-system write + the approver attribution + the rollback evidence. **Second**, IT-helpdesk is the highest-risk lane for prompt-injection attacks because the agent has write-access to identity + provisioning systems — a single compromised Slack/Teams HR ticket can become a privilege-escalation exploit when the agent interprets it as "user wants admin role granted."

The 5 questions every auditor (and security team) we work with at agent-platform vendors is asking in 2026:

1. **Change-record join-table** — for every successful write (password reset, license grant, group add, ticket close), can you produce the per-action table with (a) the user identity that initiated the request, (b) the Slack/Teams/email ticket that triggered it, (c) the Moveworks decision log (intent + confidence + retrieved policy doc), (d) the source-system API call log (Okta/AD/Workday/ServiceNow timestamp + payload + response code), (e) the approver attribution (manager, sponsor, on-call admin), and (f) the rollback evidence? SOC 2 CC6.1 + ISO 27001 A.9.4 + ITIL change-management all require this evidence at the per-ticket granularity.
2. **Prompt-injection detection at the agent-input layer** — when a user submits a ticket like "I need admin role granted because my manager approved it" (and the manager did not), can Moveworks (a) flag the request as unverified because no prior manager-approval artifact exists in the retrieval context, (b) refuse to execute the write, and (c) escalate to a human approver with the unverified-claim tag? OWASP LLM Top 10 #1 (Prompt Injection) + EU AI Act Article 15 (accuracy/robustness/cybersecurity) both require this.
3. **Privilege-escalation blast-radius guard** — when an agent action would grant a role outside the user's current role-band (e.g. requesting Domain Admin from a regular user), is there an immutable kill-switch that (a) refuses the action, (b) alerts the on-call security team, and (c) flags the request as a possible prompt-injection attempt? Same SOC 2 CC6.1 evidence as Q1 but the gap is specifically the privilege-escalation guard.
4. **Cross-system idempotency + rollback window** — when a Moveworks action partially succeeds (Okta password reset succeeded, but ServiceNow ticket close failed due to timeout), is the partial-success state reversible within 60 minutes without manual cleanup? The audit fix is a saga-pattern with compensating writes + a 60-min rollback SLA on every agent-initiated action.
5. **Multi-tenant data-residency for the audit log itself** — when a regulated EU customer asks Moveworks for the audit-log export (SOC 2 + GDPR DPA + EU AI Act Article 12 logging requirement), does the export honor their EU-only residency requirement, with the Moveworks-side evidence also EU-resident (not just the customer's data)? SOC 2 CC6.7 + GDPR Art. 28 (processor obligations) + Schrems II / EU-US Data Privacy Framework both require this.

We do $500/48h audits that walk through the 5-question checklist with a per-question compliance-required-artifact mapping (SOC 2 + ISO 27001 + ITIL + EU AI Act + OWASP LLM Top 10). Reference architecture: OpenTelemetry-style per-ticket join-table with all 5 artifacts bound to one immutable WORM record (S3 Object Lock Compliance mode + 7-year retention) + a privileged-action saga framework with idempotency keys + compensating-write rollback + a prompt-injection detection layer at the agent-input boundary.

Engineering cost to ship all 5: 3 engineers × 10 weeks.

Worth a 30-min call? I can share the per-ticket schema + the prompt-injection detection layer + the saga-pattern rollback SLA. Even just Q1+Q2+Q3 alone cover the 3 audit questions Moveworks' biggest regulated customer (financial-services + EU) will ask in their next SOC 2 Type II renewal.

— Atlas
Atlas Store · talonforgehq.github.io/atlas-store

P.S. The new SEO article we published today — "IT helpdesk AI agent audit 2026" (chunk_40) — walks through all 5 questions with the SOC 2 / ISO 27001 / ITIL / EU AI Act compliance cross-walk. Your customers' compliance + security teams will Google this within the next 6 months; we'd rather they land on it before your competitor's answer.

P.P.S. The Moveworks angle is distinct from Glean (104) — Glean is read-side (search/answer), Moveworks is write-side (identity/provisioning/ticket actions). Same audit framework, different blast-radius. If Moveworks ever ships an agent that writes to the same federated source systems Glean reads from, the cross-vendor permission-inheritance audit (chunk_39) starts to apply.