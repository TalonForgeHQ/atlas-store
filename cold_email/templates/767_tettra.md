# Lead 767 — Tettra (5-Question Audit Letter)

**Recipient:** Karthik Suresh (Co-Founder & CEO) + Jake Lumetta (Co-Founder & CTO) — Tettra / KinHR Inc.
**Route:** support@tettra.com (verified live 2026-07-21 on tettra.com/contact)
**Subject:** Tettra Knowledge Agents — EU AI Act Art. 14 human-oversight evidence gap (48h, $500 fixed)

---

Hi Karthik / Jake,

I built a 5-question evidence-gap audit for Tettra's Knowledge Agent stack as it sits on top of Slack + MS Teams + Google Drive + GitHub + Figma + Notion + Confluence. The EU AI Act Art. 14 enforcement window opens August 2 2026, and a Slack/Teams-resident Q&A bot has a specific human-oversight surface (expert-verification events, escalation logs, write-back provenance) that is non-overlapping with browser-resident copilots — so the audit template is different from a Guru or Notion AI audit.

**5 questions I would answer in your $500 fixed-scope 48-hour evidence-gap map:**

1. **Per-question provenance** — For each Tettra AI answer served inside Slack or MS Teams, do you capture and store (a) the user identity, (b) the question text, (c) the document/version that produced the answer, (d) the LLM sub-processor invoked (OpenAI vs. Anthropic vs. self-hosted), (e) the retention window, and (f) the region routing? If yes, where is the audit log persisted (your Postgres + your S3 + the LLM sub-processor's own log)? If no, what is the rebuild ETA?

2. **Expert-verification audit trail** — When a question escalates to a subject-matter expert and the answer is written back to a Tettra category, do you capture (a) the expert identity, (b) the verification timestamp, (c) the revision history, (d) the Strict-vs-Loose verification mode, and (e) the downstream re-retrieval flag that determines whether the same answer is served to the next asker? If yes, is this trail exportable in a single artifact for procurement review?

3. **Per-source ACL + integration-credential scope** — For each connected source (Google Drive folder + GitHub repo + Figma file + Notion page + Confluence space), do you maintain a mapping of which Tettra category + which role can retrieve from that source, and which OAuth credential / GitHub App installation backs that mapping? When a credential is rotated or revoked, do downstream ACL mappings cascade within 24h or is there a lag window where stale credentials still serve answers?

4. **Slack + MS Teams bot data-handling disclosure** — What scope of channel content + DM content + threaded conversation content + ephemeral message content can the Tettra bot read? Is there a per-workspace admin-set scope, or does the bot read everything the installing user can read (including private channels + DMs the user has joined)? How does this map to EU AI Act Art. 50 transparency-labeling (the bot's answers are watermarked as AI-generated, but the *prompt* the bot sees from a DM is not necessarily labeled)?

5. **Sub-processor cascade DPA + 14-day change-notification SLA** — Tettra's retrieval layer pulls from Google + GitHub + Figma + Notion + Confluence (5 first-party sub-processors), then forwards the assembled prompt to OpenAI or Anthropic (2 LLM sub-processors), then serves the answer back through Slack or MS Teams (2 delivery sub-processors) — totaling 9 sub-processors in the per-answer cascade. Do you maintain a current sub-processor list with flow-down DPA, and does your DPA with each include a 14-day change-notification SLA per GDPR Art. 28(2)?

**What you get for $500 / 48h:** a written 8-12 page evidence-gap map with each of the 5 questions answered (current state + gap + remediation ETA + dollar/effort estimate), plus a redlined Tettra sub-processor list + a Slack/Teams bot data-handling disclosure template you can hand to procurement.

**What you get for $497 / month:** quarterly refresh — every 90 days we re-run the 5-question audit, capture the delta (new sub-processor + new region + new integration + new LLM), and emit a refreshed evidence packet you can hand to the next EU enterprise buyer.

Reply with a yes/no on the 48h engagement and I'll send a Stripe payment link.

— Atlas / Talon Forge
atlas@talonforge.com

---

**Cohort marker:** ai_enterprise_knowledge_agents sibling #2/5 after Guru 766.
**Hard rules followed:** real company + real website + real founders + real verified inbox; no form submission; privacy/legal/security/press/careers/investor/founder routes excluded; offer $500/48h or $497/mo; no email sent, no delivery, no payment, no revenue claimed.
