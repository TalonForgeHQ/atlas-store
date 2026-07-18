# Lead 62 — PostHog

**Vertical:** dev_tools
**Tier:** 1
**Website:** https://posthog.com/
**Co-founders:** James Hawkins and Tim Glaser (Co-CEOs)
**Verified public inbox:** privacy@posthog.com
**Verified sales route:** sales@posthog.com

---

**Subject:** 5 audit questions for PostHog’s self-driving product stack

Hi James + Tim,

PostHog’s current first-party pages describe a product stack moving toward self-driving software, with AI agents and tools sitting beside product analytics, session replay, experiments, feature flags, data pipelines, error tracking, and customer data. That is a strong product story, but it also creates a procurement question: can one AI-generated product decision be reconstructed from source event through model context, approval, experiment, flag, and customer-facing action?

I run a focused **$500 / 48-hour audit** for production AI platforms. These are the five questions I would test against PostHog:

1. **Decision provenance:** Can one export join organization, project, user and session IDs, source events, replay and warehouse references, retrieved context, prompt and model version, agent or tool call, generated recommendation, human approval, feature flag, experiment exposure, downstream mutation, and token or compute cost?
2. **Hostile product data:** What prevents prompt injection or data poisoning in event properties, recordings, surveys, support text, warehouse rows, issue metadata, URLs, or uploaded context from changing an AI analysis or triggering an unsafe tool action?
3. **Tenant and environment isolation:** Can customers retrieve evidence that organization, project, development, staging, production, warehouse, replay, prompt, secret, and model-provider boundaries prevent cross-tenant or cross-environment leakage?
4. **Change control and rollback:** Are prompt, model, retrieval, agent, tool, feature-flag, and experiment changes versioned and approval-bound, with a deterministic path to identify affected users and roll back a bad recommendation or action?
5. **Incident and deletion reconstruction:** After a privacy incident, hallucinated insight, unsafe mutation, or compromised integration, can PostHog preserve WORM-capable evidence while proving deletion across recordings, derived features, embeddings, caches, exports, logs, and backups?

The deliverable is a procurement-ready gap map and fix specification mapped to **SOC 2 CC6.1 and CC7.2; EU AI Act Articles 12, 14, and 15; GDPR Articles 22, 28, 30, and 32; ISO 42001; NIST AI RMF; OWASP LLM Top 10; and MITRE ATLAS**. I test one live event-to-agent-to-product-action route end to end rather than sending a generic checklist.

**Why PostHog specifically:** combining analytics, recordings, experiments, flags, data movement, and AI agents can eliminate the fragmented handoffs that make product work slow. It also concentrates sensitive behavioral context and customer-facing decisions in one control plane, so evidence quality becomes part of the product promise.

If this is on your radar for the next enterprise procurement cycle, I can hold a slot this week and ship the gap map within 48 hours.

— Atlas (Talon Forge LLC)

$500 / 48 hours · procurement-ready gap map · one live AI product-decision route tested end to end
