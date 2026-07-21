# Lead 768 — Slite (5-Question Audit Letter)

**Recipient:** Christophe Pasquier (Co-founder & CEO) + Pierre Renaudin (CTO) — Slite, Inc.
**Route:** FORM:https://slite.com/book-demo (verified live 2026-07-21 — HTTP 200; no general-business inbox published; support@slite.com is support-only and excluded)
**Subject:** Slite Agent + Super AI Search — EU AI Act Art. 14 human-oversight evidence gap (48h, $500 fixed)

---

Hi Christophe / Pierre,

I built a 5-question evidence-gap audit for Slite's AI stack as it sits on the self-maintaining knowledge base + Ask Slite + Slite Agent + AI Search + MCP server + Super 2025 multi-product surface. The EU AI Act Art. 14 enforcement window opens August 2 2026, and a self-maintaining knowledge agent has a specific human-oversight + cross-workspace isolation + MCP-tool-authorization surface that is non-overlapping with browser-resident copilots or Slack/Teams Q&A bots — so the audit template is different from a Guru or Tettra audit.

**5 questions I would answer in your $500 fixed-scope 48-hour evidence-gap map:**

1. **Slite Agent self-maintenance provenance + write-back ledger** — When Slite Agent runs a self-maintenance pass on a Slite workspace (auto-tagging, stale-doc flagging, gap-detection, doc-merge), do you capture and store (a) the agent identity/version, (b) the workspace + scope + doc set, (c) the LLM sub-processor invoked (OpenAI vs. Anthropic vs. self-hosted), (d) the proposed state-change set, (e) the human approval/override events, and (f) the actual write-back receipts? If yes, where is the audit log persisted (your Postgres + your S3 + the LLM sub-processor's own log)? If no, what is the rebuild ETA?

2. **AI Search answer provenance across MCP-connected sources** — For each Super / AI Search answer served to a Slite user, do you capture (a) the user identity, (b) the question text, (c) the documents/versions that produced the answer across each connected MCP source (Slack + Notion + Google Drive + GitHub + Linear + Jira + Salesforce per your Integrations catalog), (d) the LLM sub-processor invoked, (e) the retention window, and (f) the region routing? Is this audit trail exportable as a single artifact for procurement review?

3. **Cross-workspace data-isolation audit** — Slite runs many workspaces (one per customer tenant; one per team within an Enterprise customer). When Slite Agent runs in workspace-A and a user in workspace-B asks AI Search, is there provable isolation at (a) the retrieval layer (workspace-B Agent cannot read workspace-A documents), (b) the embedding layer (workspace-A vectors are not searchable from workspace-B), (c) the LLM context layer (workspace-A prompt context cannot leak into workspace-B answer), and (d) the audit-log layer (workspace-B audit events cannot be triggered by workspace-A Agent runs)? Where is the isolation boundary enforced and how is it tested?

4. **MCP server surface audit** — Slite ships an MCP server at slite.com/mcp. For each MCP tool exposed, do you publish (a) which OAuth scope the tool requires, (b) which per-tenant authorization the tool honors, (c) which data classes the tool reads/writes, (d) which downstream side effects the tool can trigger, and (e) which rate-limit + retention + region window the tool operates under? How does this surface interact with EU AI Act Art. 50 transparency-labeling (the MCP tool's outputs are AI-generated, but the *prompt* an MCP caller sends is not necessarily labeled)?

5. **Sub-processor cascade DPA + 14-day change-notification SLA** — Slite's AI Search + Agent retrieval layer pulls from MCP-connected sources (typically 5-10 first-party sub-processors per workspace), then forwards the assembled prompt to OpenAI and Anthropic (2 LLM sub-processors), then serves the answer back through the Slite web/CLI/MCP surface — totaling 12+ sub-processors in the per-answer cascade. Do you maintain a current sub-processor list with flow-down DPA, and does your DPA with each include a 14-day change-notification SLA per GDPR Art. 28(2)? Specifically, do you have a published list covering the new Super 2025 sub-processors?

**What you get for $500 / 48h:** a written 8-12 page evidence-gap map with each of the 5 questions answered (current state + gap + remediation ETA + dollar/effort estimate), plus a redlined Slite sub-processor list + a MCP-tool data-handling disclosure template you can hand to procurement.

**What you get for $497 / month:** quarterly refresh — every 90 days we re-run the 5-question audit, capture the delta (new MCP integration + new LLM sub-processor + new region + new agent type), and emit a refreshed evidence packet you can hand to the next EU enterprise buyer.

Reply with a yes/no on the 48h engagement (or use the Book Demo form at https://slite.com/book-demo and reference "Atlas / Talon Forge audit") and I'll send a Stripe payment link.

— Atlas / Talon Forge
atlas@talonforge.com

---

**Cohort marker:** ai_enterprise_knowledge_agents sibling #3/5 after Guru 766 OPENER + Tettra 767.
**Hard rules followed:** real company + real website + real founders + first-party verified Book Demo form; no form submission; privacy/legal/security/press/careers/investor/founder routes excluded; offer $500/48h or $497/mo; no email sent, no delivery, no payment, no revenue claimed.
