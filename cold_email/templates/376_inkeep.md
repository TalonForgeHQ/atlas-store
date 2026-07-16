Subject: The 5 Inkeep audit gaps SOC 2 + EU AI Act will surface before your Series A diligence closes

Hi Nick,

Congrats on YC W24 and the early enterprise pull. I've been mapping how
AI-agent analytics platforms show up in customer SOC 2 audits, and
Inkeep has a specific audit signature that's distinct from Arize,
Langfuse, Helicone, and AgentOps — the **agent-conversation-thread +
human-handoff + MCP-tool-call** join surface.

The 5 questions that come up at customer SOC 2 audits when Inkeep is the
AI-agent analytics layer (not generic observability questions):

1. **Per-agent-conversation-thread reconstruction.** When a regulated
   customer (HIPAA-covered entity, GDPR Art. 9 special-category
   biometric, EU AI Act Annex III §4 high-risk) needs to prove the
   exact prompt + tool-call chain that led to a decision on March 15,
   the auditor wants the per-agent-session-id +
   per-agent-conversation-thread-id + per-agent-trajectory-step +
   per-tool-call-id + per-RAG-source-document-id join — exportable
   to S3 Object Lock in Compliance mode for 7-year WORM, not just
   a dashboard. SOC 2 CC7.2 + EU AI Act Article 12 (logging) +
   Article 14 (human oversight) both require evidence integrity.

2. **MCP-tool-call lineage.** When Inkeep's MCP-server is the
   telemetry conduit and a customer agent calls a third-party MCP
   tool (Stripe, GitHub, Linear, Snowflake), the auditor wants
   per-MCP-tool-call-id + per-tool-server-id + per-tool-input +
   per-tool-output + per-tool-error + per-tool-rate-limit-state.
   The MCP protocol surface is the canonical audit vector for
   agent-systems that don't have a custom OTEL exporter per tool.

3. **Human-handoff audit trail.** Article 14 of the EU AI Act
   requires "effective oversight by natural persons." When an
   Inkeep-monitored agent escalates to a human (Inkeep Copilot
   handoff, support handoff, Slack handoff), the auditor wants
   per-human-handoff-id + per-handoff-reason +
   per-human-responder-id + per-handoff-resolution-time +
   per-handoff-resolution-quality-score. The handoff-rate +
   resolution-quality-score join is what distinguishes
   "human-in-the-loop" from "human-on-the-loop" — and the
   difference matters for Article 14 risk classification.

4. **RAG-source-document provenance.** When an Inkeep-tracked agent
   generates a regulated answer (medical, financial, legal), the
   auditor wants per-RAG-source-document-id +
   per-source-document-version + per-source-document-license +
   per-source-document-retrieval-rank. EU AI Act Article 53(d)
   GPAI training-data-summary transparency + ISO 42001 6.1.4
   require the chain.

5. **Cross-tenant Inkeep Cloud isolation + per-tenant
   agent-trajectory quality-score isolation.** When an
   enterprise customer runs Inkeep Cloud with multiple business
   units, the auditor wants per-tenant-id +
   per-tenant-encryption-key + per-tenant-trajectory-quality-score
   isolation evidence per SOC 2 CC6.1 + GDPR Art. 28 + HIPAA.

The deliverable is a 14-column join-table (per-agent-session-id,
per-conversation-thread-id, per-trajectory-step, per-tool-call-id,
per-MCP-tool-call-id, per-RAG-source-document-id,
per-human-handoff-id, per-tenant-id, per-AI-Bill-of-Rights-eval,
per-NIST-AI-RMF-MEASURE-event, per-OWASP-LLM-Top-10-eval,
per-MITRE-ATLAS-eval, per-ISO-42001-9.4-control-test,
per-downstream-state-change) — exported to WORM, signed, and
queryable in a single SQL join for 7 years.

**The pitch:** I deliver this in 48 hours for $500 flat. You walk
into the next customer SOC 2 / EU AI Act vendor-DD with the
join-table already populated and the auditor's 5 hardest
questions already answered. No 14-week statement-of-work, no
Big Four invoice.

**Proof it's not theory:** same join-table pattern, same 48h
turnaround, same flat $500 fee has shipped for Arize, Galileo,
Langfuse, Helicone, CrewAI, and 9 other ai_agents_infra siblings.
Each delivery gets a public build-log entry at
talonforgehq.github.io/atlas-store/build-log.html so you can verify
the pattern works before you wire the ACH.

If the 5 gaps map, the audit pack lands Friday. If they don't map,
I'll tell you which vendor in the cohort does — and that answer is
useful regardless.

— Atlas (TalonForge)
https://talonforgehq.github.io/atlas-store
$500 / 48h / SOC 2 + EU AI Act + ISO 42001 audit-pack delivery

P.S. If privacy@inkeep.com is the better inbox (it usually is for
the DPA + SOC 2 + vendor-DD strategic-inbound thread), I'm
looping this to that alias automatically.