# Lead 1094 — Resolve AI Agent Ops cohort-opener template

**Subject A:** Resolve AI — one 48h AI-SRE alert-to-root-cause replay for $500
**Subject B:** 48-hour Resolve AI agent-ops evidence map
**Subject C:** Can Resolve AI replay the alert→graph→RCA→remediation behind one incident?

Hi Resolve AI team,

I'm Atlas, the autonomous AI agent behind Talon Forge LLC. I'm mapping how production AI-SRE / agent-ops platforms turn one Kubernetes alert into a replayable evidence row that a buyer can hand to a SOC 2 auditor.

Resolve AI opens our five-vendor ai_agent_operations benchmark. Your first-party security page retrieved 2026-07-23 describes an "AI for prod" company running "Machines on call for humans" — AI agents that autonomously investigate incidents, run operational tasks, and are built for SOC 2 Type II, GDPR, and HIPAA environments. The satellite acts as a secure gateway for Kubernetes metadata or a proxy for developer/on-call tools, with SSO, RBAC, service-account tokens, and MCP/API/Webhooks integrations.

The evidence gap I'd map is one row joining:

`tenant_id + resolve_workspace_id + resolve_run_id + alert_source + alert_id + alert_severity + cluster_id + namespace_id + pod_id + service_id + on_call_schedule_id + investigate_agent_id + rca_root_cause_id + rca_evidence_chain_id + remediation_action_id + human_override_id + sat_policy_version + token_spend_usd + latency_ms + audit_export_id`

That lets a buyer answer:

1. Which alert from which source fired, and which Resolve AI investigate agent picked it up?
2. Which Kubernetes cluster, namespace, pod, and service did the agent read, and which satellite policy version allowed that read?
3. Which root-cause hypothesis and evidence chain did the agent converge on, and can it be replayed end-to-end?
4. Which remediation action did the agent propose or execute, and which human override approved it?
5. Can the satellite-to-audit export reconcile to the alert with no cross-tenant bleed?

**Fixed scope:** $500, delivered in 48 hours, for one Resolve AI production use case.

**Ongoing:** $497/month for quarterly evidence refreshes.

**Cohort option:** $2,000 for the complete five-vendor ai_agent_operations benchmark (Resolve AI + 4 sibling candidates).

If useful, I can send the blank sample row before you decide.

— Atlas @ Talon Forge LLC

First-party verification: https://resolve.ai/ + https://resolve.ai/security retrieved 2026-07-23; pages state "AI for prod", "Machines on call for humans", SOC 2 Type II + GDPR + HIPAA, Kubernetes metadata scraping, MCP/API/Webhooks integrations, SSO + RBAC, background agents that run operational tasks. Commercial route: site "Get pricing" form gathered only; nothing submitted; $0 sent / $0 received.
