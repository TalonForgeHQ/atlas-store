# Lead 56 — Linear

**Vertical:** b2b_saas
**Tier:** 1
**Website:** https://linear.app/
**Founder / CEO:** Tuomas Artman (CTO + co-founder), Karri Saarinen (co-founder, original design lead)
**Verified public inbox:** hello@linear.app

---

**Subject:** 5 audit questions on Linear AI triage, agent labels, and customer-data isolation

Hi Tuomas,

Linear is the issue-tracking backbone for product and engineering teams, and the AI triage and auto-label workflows now sit on top of customer roadmaps, customer issues, customer incident timelines, and customer internal comments. That makes the audit question bigger than what one label returned: a buyer needs to reconstruct which workspace, customer tenant, AI agent version, prompt, context window, ticket history, model call, integration, and downstream notification produced each classification.

I run a focused **$500 / 48-hour audit** for production AI platforms that touch customer data. These are the five questions I would test against Linear:

1. **Cross-workspace provenance:** Can one export join workspace and customer-tenant IDs, agent and version, ticket, parent and child issue, prompt, context-window payload, model call, label, confidence, latency, cost, and immutable audit event across AI triage, auto-label, duplicate detection, and customer-impact summary features?
2. **Prompt and classifier change control:** Does every AI label bind to the exact prompt, model, classifier, embedding version, and deployment approval that was active when the label was produced? Can a customer reproduce the answer from immutable evidence?
3. **Customer-data residency and prompt-injection defense:** When Linear AI ingests customer comments, customer internal notes, customer Jira/Linear/Slack mirrors, customer webhooks, and customer attachment text, what guards stop hostile prompt injection from customer-supplied issue text, customer attachments, customer GitHub/Slack mirror payloads, and customer webhook bodies from leaking across workspaces or tenants?
4. **Tenant isolation and PII handling:** Can enterprise customers retrieve workspace-scoped access logs, AI-label history, deletion completion, customer-PII redaction (especially email addresses, internal URLs, customer names appearing in issue text and comments), and isolation tests mapped to SOC 2 CC6.1?
5. **Incident evidence and rate-limit forensics:** When AI labels misfire, when customers dispute a label, when an integration floods Linear with hostile content, or when rate-limit telemetry looks off, can Linear reconstruct the lineage of every AI action in a workspace with WORM-capable evidence mapped to SOC 2 CC7.2?

The deliverable is a procurement-ready gap map and fix specification mapped to **SOC 2 CC6.1 and CC7.2; EU AI Act Articles 12, 14, and 15; GDPR Article 28; ISO 42001; NIST AI RMF; OWASP LLM Top 10; MITRE ATLAS; and ISO 27701**. I test one live Linear workspace end to end rather than sending a generic checklist.

**Why Linear specifically:** issue-tracking is now the canonical substrate where AI agents ingest customer intent, customer priority, and customer SLA context. A misfiring AI label propagates into customer-facing status pages, customer escalation queues, and customer reliability dashboards — the audit stakes are higher than a chat-only agent.

If this is on your radar for the next procurement cycle, I can hold a slot this week and ship the gap map within 48 hours. Otherwise I will close the loop in a follow-up after your Q3 SOC 2 refresh.

— Atlas (Talon Forge LLC)

$500 / 48 hours · procurement-ready gap map · one live environment tested end to end