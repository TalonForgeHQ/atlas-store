# Lead 64 — Decagon

**Vertical:** ai_vertical
**Tier:** 1
**Website:** https://decagon.ai/
**Co-founders:** Jesse Zhang (CEO) and Ashwin Sreenivas (President)
**Verified public inboxes:** privacy@decagon.ai, sales@decagon.ai, and support@decagon.ai

---

**Subject:** 5 audit questions for Decagon's conversational AI agents

Hi Jesse + Ashwin,

Decagon's AI agents turn customer messages, voice calls, account context, and connected-system data into answers and operational actions. That makes the evidence chain commercially important: when an agent resolves a case or changes a customer record, can an enterprise reconstruct the source interaction, retrieved knowledge, prompt and model version, tool call, approval state, external mutation, and customer outcome?

I run a focused **$500 / 48-hour audit** for production AI platforms. These are the five questions I would test on one Decagon conversation-to-resolution route:

1. **End-to-end provenance:** Can one export join tenant, customer, channel, conversation, message or audio segment, consent state, retrieved source, prompt and model version, reasoning or policy decision, tool call, human reviewer, downstream mutation, final response, and token or compute cost?
2. **Hostile input and grounding:** What prevents prompt injection, poisoned knowledge articles, malicious attachments, manipulated customer records, or adversarial voice content from steering answers and actions—and can every customer-facing claim be traced to approved evidence?
3. **Tenant, identity, and secret isolation:** Can customers prove that transcripts, recordings, CRM credentials, API tokens, knowledge bases, exports, and regional data boundaries prevent cross-tenant, cross-brand, cross-workspace, or cross-customer leakage?
4. **Change control and approval:** Are prompt, model, retrieval, routing, redaction, and action-policy changes versioned and approval-bound, with a tested path to pause a bad rollout, identify affected interactions, and reverse an unsafe system-of-record side effect?
5. **Incident, retention, and deletion reconstruction:** After a false answer, unauthorized action, leaked transcript, compromised connector, or failed deletion request, can Decagon preserve WORM-capable evidence while proving retention and deletion across transcripts, recordings, embeddings, caches, analytics stores, exports, and backups?

The deliverable is a procurement-ready gap map and fix specification mapped to **SOC 2 CC6.1 and CC7.2; EU AI Act Articles 12, 14, and 15; GDPR Articles 5, 6, 22, 28, 30, and 32; ISO 42001; NIST AI RMF; OWASP LLM Top 10; and MITRE ATLAS**. I test one live conversation-to-agent-action route end to end rather than sending a generic checklist.

**Why Decagon specifically:** customer-experience teams increasingly let conversational agents resolve requests and mutate operational systems without a human touching every interaction. A defensible evidence spine turns that automation into a stronger enterprise procurement and incident-response story.

If this is on your radar for the next enterprise procurement cycle, I can hold a slot this week and ship the gap map within 48 hours.

— Atlas (Talon Forge LLC)

$500 / 48 hours · procurement-ready gap map · one live Decagon conversation-to-agent-action route tested end to end
