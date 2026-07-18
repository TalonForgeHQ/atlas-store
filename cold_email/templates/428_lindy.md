# Lead 428 — Lindy AI

**Vertical:** ai_agents_smb
**Tier:** 1
**Website:** https://www.lindy.ai/
**Founder:** Flo Crivello
**Verified public inbox:** founders@lindy.ai

---

**Subject:** 5 audit questions on Lindy agent actions, credentials, and email prompt injection

Hi Flo,

Lindy sits where AI intent becomes real work across inboxes, calendars, CRMs, support systems, and other connected apps. When an agent sends the wrong message, exposes a credential, or follows hostile instructions hidden in an attachment, the audit question is not only what the model generated; it is which tenant, agent, trigger, input, tool call, authorization, approval, and downstream action produced the result.

I run a focused **$500 / 48-hour audit** for production AI-agent platforms. These are the five questions I would test against Lindy:

1. **End-to-end action provenance:** Can one evidence row join workspace and tenant IDs, agent and version, trigger, conversation or job, prompt and model versions, tool schema, tool call, connected-account grant, policy decision, human approval, downstream response, cost, and immutable audit event?
2. **Credential and tenant isolation:** Can Lindy prove that OAuth grants, API keys, inbox content, memory, files, and tool results stay isolated by workspace and agent, including revocation and deletion evidence under SOC 2 CC6.1 and GDPR Article 28?
3. **Prompt-injection resistance:** What replayable tests cover hostile instructions in emails, attachments, webpages, calendar invites, CRM notes, and tool outputs, including attempts to exfiltrate secrets or bypass an approval gate?
4. **High-impact action controls:** Which sends, deletes, purchases, record changes, and external mutations require policy checks or human approval, and is the exact approved payload cryptographically bound to the action that executes?
5. **Retention and cost attribution:** Are model calls, retries, tool executions, approvals, failures, storage, and vendor charges joined to WORM-capable evidence with named owners and regression tests?

The deliverable is a procurement-ready gap map and fix specification mapped to **SOC 2 CC6.1 and CC7.2; EU AI Act Articles 12, 14, and 15; GDPR Article 28; ISO 42001; NIST AI RMF; OWASP LLM Top 10; MITRE ATLAS; and CAN-SPAM controls**. I test one live Lindy workflow end to end rather than sending a generic AI checklist.

If useful, I can send a one-page scope for one email, calendar, or CRM agent workflow. The audit is **$500 fixed**, delivered in **48 hours**, with an optional **$497/mo** evidence-maintenance follow-on.

Worth a 30-minute working session?

Best,
Atlas
Talon Forge LLC
https://talonforgehq.github.io/atlas-store/

**Public references:**
- https://www.lindy.ai/
- https://docs.lindy.ai/
