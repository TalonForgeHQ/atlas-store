# Continue — post-acquisition AI coding-agent evidence audit (Lead 343)

**To:** privacy@continue.dev (current public route; forward to the Continue/Cursor security or product owner)
**Subject:** Continue → Cursor: preserving agent evidence through the handoff
**Evidence re-checked:** 2026-07-18 — Continue's live homepage announces its acquisition by Cursor and says the open-source codebase remains available; the live Privacy Notice publishes the route above. Y Combinator's current Continue profile identifies former founders Ty Dunn and Nate Sesti.

---

Hi Ty + Nate,

Continue's move from an independent open-source coding agent into Cursor creates a narrow diligence question: can enterprise users still reconstruct what an agent read, decided, called, changed, and rolled back across the ownership handoff?

I'm Atlas at Talon Forge. I run fixed-scope evidence audits for AI-agent vendors. For Continue, I would trace one workflow from repository context and Hub configuration through model/prompt version, retrieved chunks, MCP or tool calls, proposed edits, approval, execution, and rollback—then map the evidence to SOC 2 CC7.2, ISO/IEC 42001, EU AI Act Articles 12 and 14, and the OWASP LLM Top 10.

**Five questions I would test:**

1. **Acquisition-boundary continuity:** Which Continue audit records, configuration histories, customer commitments, and incident runbooks transferred to Cursor, and which remain under the former Continue service or open-source project?

2. **Agent action provenance:** Can an enterprise export join repository/file and retrieved-chunk IDs to prompt/model/config versions, MCP or tool-call IDs, approval identity, resulting code diff, and rollback outcome without stitching multiple incomplete logs?

3. **Hostile-context controls:** When repository text, documentation, an MCP response, or tool output contains prompt injection, what policy blocks authority escalation, secret access, or unapproved side effects—and is that decision retained as evidence?

4. **Tenant and secret isolation:** Through the transition, how are customer code indexes, Hub configs, API keys, self-hosted deployments, residency choices, and deletion requests separated and reconciled between Continue and Cursor control planes?

5. **Open-source and support commitments:** Which components, security-fix channels, privacy requests, data-retention promises, and export paths remain supported now that the homepage describes Continue as acquired, and where is the authoritative owner recorded?

The deliverable is a one-page gap map plus an evidence matrix: control, current artifact, owner before/after acquisition, retention/export path, buyer-facing gap, and the smallest remediation. It is designed to answer an enterprise DDQ without pretending that pre-acquisition controls automatically survived the handoff.

**Price:** $500 fixed. **Delivery:** 48 hours. Optional monthly evidence refresh: $497/month.

Worth sending the sample matrix to the current Continue/Cursor security or product owner?

— Atlas
Talon Forge LLC
atlas@talonforge.com

P.S. If the former founder team no longer owns this surface, a forward to the transition owner is enough; I will keep the review scoped to the live Continue service, public codebase, and the commitments that actually remain.
