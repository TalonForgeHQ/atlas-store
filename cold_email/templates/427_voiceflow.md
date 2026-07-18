# Lead 427 — Voiceflow

**Vertical:** voice_agents
**Tier:** 1
**Website:** https://www.voiceflow.com/
**Founder / CEO:** Braden Ream
**Verified public inbox:** support@voiceflow.com

---

**Subject:** 5 audit questions on Voiceflow agent traces, prompt versions, and live-call controls

Hi Braden,

Voiceflow is where enterprise teams design, deploy, and operate AI agents across chat and voice. That makes the audit question bigger than what one model returned: a buyer needs to reconstruct which tenant, agent version, prompt, knowledge source, integration, tool call, approval, channel event, and downstream action produced each outcome.

I run a focused **$500 / 48-hour audit** for production AI-agent platforms. These are the five questions I would test against Voiceflow:

1. **Cross-channel provenance:** Can one export join workspace and tenant IDs, agent and version, conversation, turn, prompt version, model call, knowledge-base chunk, integration or tool call, response, latency, cost, and immutable audit event across both chat and voice?
2. **Prompt and workflow change control:** Does every production transcript bind to the exact prompt, canvas or workflow version, model configuration, tool schema, and deployment approval that was active when the response executed?
3. **Live-call privacy and payment controls:** For voice workflows, can Voiceflow prove recording consent, transcript and audio redaction, retention, deletion, and PCI DSS Requirement 3 handling before sensitive data reaches a model, log, or third-party integration?
4. **Prompt-injection and tool-abuse testing:** What replayable tests cover hostile knowledge-base documents, user utterances, integration outputs, indirect prompt injection, secret exfiltration, and attempts to trigger unauthorized external actions?
5. **Tenant isolation and incident evidence:** Can enterprise customers retrieve workspace-scoped access logs, secret and OAuth-grant history, isolation tests, deletion completion, incident lineage, and WORM-capable evidence mapped to SOC 2 CC6.1 and CC7.2?

The deliverable is a procurement-ready gap map and fix specification mapped to **SOC 2 CC6.1 and CC7.2; EU AI Act Articles 12, 14, and 15; GDPR Article 28; ISO 42001; NIST AI RMF; OWASP LLM Top 10; MITRE ATLAS; and PCI DSS Requirement 3**. I test one live Voiceflow agent end to end rather than sending a generic checklist.

If useful, I can send a one-page scope for one chat-to-voice workflow. The audit is **$500 fixed**, delivered in **48 hours**, with an optional **$497/mo** evidence-maintenance follow-on.

Worth a 30-minute working session?

Best,
Atlas
Talon Forge LLC
https://talonforgehq.github.io/atlas-store/

**Public references verified 2026-07-18:**
- https://www.voiceflow.com/
- https://www.voiceflow.com/about
- https://www.voiceflow.com/privacy
