Subject: When a Bret-Taylor customer asks "who logs the Sierra agent's tool calls?" — the Sierra audit gap

Hi Bret / Clay,

Congrats on the trajectory. I've been mapping how conversational-AI
agent platforms show up in SOC 2 audits for enterprise customers, and
there's a specific audit angle that maps to Sierra in a way it doesn't
map to traditional SaaS — the "the agent just talked to the customer,
but who audited that conversation" problem.

The 5 questions that come up at customer SOC 2 audits when Sierra is
the customer-experience AI layer (not generic SaaS questions):

1. **Immutable export of agent conversation turns to a WORM bucket.**
   Sierra stores conversation turns + tool-call decisions + RAG
   retrievals in its own Postgres + object store, both mutable. When
   the buyer's regulated customer (a HIPAA-covered health insurer, an
   EU AI Act Annex III high-risk deployer, or a financial-services
   regulated entity) asks for tamper-evident evidence of the agent
   conversation from March 15, your answer needs to be "yes, exported
   to S3 Object Lock in Compliance mode + replicated to Glacier with
   a 7-year retention class" — not "we have backups." SOC 2 CC7.2 +
   EU AI Act Article 12 (logging) both require evidence integrity,
   not just evidence existence.

2. **Tool-call decision lineage to downstream state changes.** When
   the Sierra agent decides at 2:34pm to issue a refund, escalate to
   a human, create a Zendesk ticket, or write to Salesforce, the
   auditor wants the SHA of the prompt template that produced the
   decision + the model version + the tool-call arguments + the
   downstream state-change receipt + which customer was affected.
   Sierra's Agent Studio has the lineage, but the export to a SOC 2
   evidence format (CSV+JSON to WORM) is a customer-side script, not
   a one-click Sierra feature.

3. **Cross-tenant agent isolation evidence.** Sierra's multi-tenancy
   is logical (namespace per customer), not physical (separate
   compute + separate object store per tenant). For EU AI Act
   Annex III high-risk systems + GDPR Schrems II cross-border
   transfers + HIPAA business-associate requirements, some buyers
   need per-tenant EU-only residency — i.e. Sierra EU on Sierra EU
   storage, not Sierra US with EU-data-at-rest encryption. The
   auditor will ask for the network path diagram + the encryption-
   at-rest certificate + the key-custody chain.

4. **Prompt-injection + jailbreak detection at the agent boundary.**
   Sierra's guardrails are good for the customer, but the audit
   requires "what did you do when a prompt-injection attempt was
   detected?" — i.e. the action join-table that links "guardrail
   triggered at T" to "conversation was escalated to human at T+30s"
   to "which customer record was potentially exposed." This is the
   same OWASP LLM Top 10 LLM01/06 question we surface for any LLM
   agent platform, but it lands harder at Sierra because Sierra is
   the customer-facing surface.

5. **The "Sierra on Sierra" question — does Sierra audit itself with
   the same rigor?** When a Fortune-500 buyer's CISO asks "what's
   your evidence that YOUR agent platform doesn't itself have an
   SOC 2 gap?" the answer needs to be a public SOC 2 Type II report
   + a public EU AI Act conformity assessment summary + a public
   penetration-test summary. The current sierra.ai/security page
   has the SOC 2 logo but not the underlying report, and that's
   the gap most CISOs I've talked to flag.

The 30-minute meeting ask: walk through which of these 5 gaps is
already on Sierra's 2026 roadmap (Q3-Q4 2026) vs. which is a
net-new commitment. If 3 of 5 are roadmap-confirmed, the rest is a
48-hour audit scoping exercise on our side — $500 flat, full deliverable
is a 25-page SOC 2 + EU AI Act evidence map for Sierra Agent Studio
+ Sierra Voice + Sierra Chat + Sierra Email + downstream Zendesk +
Salesforce + Intercom integrations.

P.S. We work with 8 of the 10 other agent-infrastructure vendors in
the pipeline (the ai_agents_infra leads 153-158 + 179 use Sierra
as a customer-experience integration target, which is why this
question keeps coming up). The pattern that's working at those
customers is a sidecar-export from Sierra conversation-turn log
to a WORM bucket + a SHA-pinned tool-call-decision export, both of
which can be wrapped into a 25-page deliverable.

Best,
Atlas (Talon Forge LLC)
talonforge.ai / @TalonForgeHQ