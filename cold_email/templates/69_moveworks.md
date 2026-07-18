# Lead 69 — Moveworks

**Vertical:** enterprise_ai
**Tier:** 1
**Website:** https://www.moveworks.com/
**Co-founders:** Bhavin Shah (CEO), Varun Singh (President), Jiang Chen (CTO of AI), and Vaibhav Nivargi (CTO)
**Verified public inbox:** support@moveworks.com

---

**Subject:** 5 audit questions for Moveworks' enterprise agentic AI

Hi Bhavin + Varun + Jiang + Vaibhav,

Moveworks' agentic AI sits where employee intent becomes action across IT, HR, finance, and enterprise systems. For a buyer, the diligence question is concrete: can they reconstruct what the agent understood, which enterprise context and policy it used, which tool it called, who approved the action, and what changed downstream?

I run a focused **$500 / 48-hour audit** for production AI-agent platforms. These are the five questions I would test on one Moveworks employee-request-to-enterprise-action route:

1. **End-to-end provenance:** Can one export join employee and tenant, request and attachments, retrieved knowledge and records, prompt and model version, policy decision, tool call, approval, downstream mutation, response, timestamp, and attributed cost?
2. **Authority and human approval:** Which password resets, access grants, HR changes, finance requests, ticket closures, messages, and other high-impact actions require explicit approval—and can Moveworks prove the approver held the right authority at that moment?
3. **Tenant, identity, and secret isolation:** Can customers retrieve evidence that employee data, conversations, search context, connector credentials, OAuth scopes, tool results, and model caches remain isolated across tenants, business units, roles, and regions?
4. **Hostile input and change control:** What prevents prompt injection or poisoned tickets, documents, messages, knowledge articles, and connector results from steering an agent—and are prompts, models, retrieval rules, policies, and tool scopes versioned with tested rollback?
5. **Incident, retention, and deletion reconstruction:** After a wrong entitlement, leaked record, unauthorized system change, discriminatory outcome, or deletion request, can Moveworks identify every affected action, preserve WORM-capable evidence, and prove correction or deletion across stores, caches, analytics, exports, and backups?

The deliverable is a procurement-ready gap map and fix specification mapped to **SOC 2 CC6.1 and CC7.2; EU AI Act Articles 9, 12, 14, and 15; GDPR Articles 5, 17, 22, 28, 30, and 32; ISO 42001; NIST AI RMF; OWASP LLM Top 10; and MITRE ATLAS**. I test one live employee-request-to-enterprise-action route end to end rather than sending a generic checklist.

**Why Moveworks specifically:** an enterprise agent that resolves requests across multiple systems removes handoffs, but it also concentrates identity, policy, retrieval, and mutation authority. A defensible evidence spine turns that concentration into a stronger procurement, compliance, and incident-response story.

If this is on your radar for the next enterprise procurement cycle, I can hold a slot this week and ship the gap map within 48 hours.

— Atlas (Talon Forge LLC)

$500 / 48 hours · procurement-ready gap map · one live Moveworks employee-request-to-enterprise-action route tested end to end
