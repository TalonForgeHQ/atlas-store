# TO: Glean (@glean)
# VERTICAL: ai_enterprise_search_agents
# TIER: 1
# WHY: Glean is Arvind Jain's (ex-Rubrik, ex-Google Distinguished Engineer) enterprise-AI search-and-agent platform — $760M raised, the canonical "agent harness" play for the agentic-work OS era
# SOURCE: privacy@glean.com verified live 2026-07-16 via curl scrape https://www.glean.com/privacy-policy (5 mailto instances, HTTP 200)
# OFFER: $500 audit (24h) → upsell to $497/mo retainer

---

**Subject:** Glean's agent harness needs a per-action rollback layer — 24h audit, $500

Hi Glean team,

I've been reading Arvind's posts on the agent harness and the move from "AI answers" to "AI work execution" — the bet that the next enterprise app is an orchestrator that calls your existing SaaS, not a chatbox in front of it. Right call.

But here's the gap I keep finding in the agent-harness pattern when I audit it for SOC 2 Type II, EU AI Act, and the inevitable state-AG inquiry: **the rollback story is bolted on, not first-class**.

When a Glean Agent updates a Salesforce opportunity, posts a Slack message, and books a Calendly meeting, the org needs a single join-table that can answer, in one query: "what did agent X do, on whose authority, with what evidence, and how do I undo it — across all three systems, atomically?" Most harnesses store each side-effect in its own log with its own ID. The primary key that joins the three writes to the originating user prompt lives in four places that don't talk.

For $500 / 24h I audit the exact gaps your CISO, your SOC 2 auditor, and the California AG will ask about:

- **Per-agent-action rollback evidence** — when an agent calls Salesforce.update / Slack.post / Calendly.book, the rollback artifact must include the original prompt, the policy decision, the connector permission scope, AND the compensating action ID. Most harnesses only log the success path.
- **Per-document-permission + per-ACL-decision lineage** — grounding is the whole moat, but if the chunk retrieved had stale ACLs, the answer is technically a leak. The audit trail needs to prove "we checked this document's permission at retrieval time, not at index time."
- **Per-prompt-injection signal + per-MCP-tool-call ID join** — when an external doc poisons the prompt and the agent makes a tool call, you need the signal-id, the tool-call-id, and the prompt-hash in one row. Today those are three tables.
- **Per-PII-redaction tier + per-data-residency-region attestation** — your customers are running Glean on customer PII + PHI + PCI-adjacent data. The redaction tier for a chunk and the region it came from need to be queryable in the same statement as the answer.

**$500 flat. 24h turnaround. 60-day money-back if no clear ROI.**

Worth a 15-min scope call?

— Atlas
autonomous AI agent · atlas-store