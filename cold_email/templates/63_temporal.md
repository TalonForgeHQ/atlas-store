# Lead 63 — Temporal

**Vertical:** dev_infra
**Tier:** 1
**Website:** https://temporal.io/
**Co-founders:** Samar Abbas (CEO) and Maxim Fateev (CTO)
**Verified public inbox:** legal@temporal.io

---

**Subject:** 5 audit questions for Temporal-powered AI agents

Hi Samar + Maxim,

Temporal’s durable execution model is a natural foundation for production AI agents: workflows can survive retries, outages, long-running approvals, and external tool failures without losing state. That reliability promise also raises a procurement question for customers building agents on Temporal: can one consequential agent action be reconstructed from the original request through workflow history, model context, human approval, activity retries, and the final external side effect?

I run a focused **$500 / 48-hour audit** for production AI platforms. These are the five questions I would test against a Temporal-backed agent route:

1. **End-to-end provenance:** Can one export join namespace, workflow and run IDs, task queue, workflow code version, source request, retrieved context, prompt and model version, tool or activity call, retry history, human approval, external mutation, and token or compute cost?
2. **Hostile inputs and replay safety:** What prevents prompt injection or poisoned payloads in signals, updates, activity results, search attributes, documents, webhooks, or tool output from steering an agent into an unsafe action—and are nondeterministic model calls kept outside replay-sensitive workflow code?
3. **Tenant and secret isolation:** Can customers retrieve evidence that namespaces, task queues, workers, mTLS identities, API keys, payload encryption, model credentials, and data residency boundaries prevent cross-tenant or cross-environment leakage?
4. **Change control and rollback:** Are workflow, worker, prompt, model, retrieval, activity, and policy changes versioned and approval-bound, with a deterministic path to identify affected runs, pause or terminate unsafe executions, and compensate an external side effect?
5. **Incident and deletion reconstruction:** After a hallucinated action, compromised worker, leaked payload, or failed compensation, can Temporal preserve WORM-capable evidence while proving deletion across histories, visibility stores, payload codecs, archives, logs, caches, and backups?

The deliverable is a procurement-ready gap map and fix specification mapped to **SOC 2 CC6.1 and CC7.2; EU AI Act Articles 12, 14, and 15; GDPR Articles 22, 28, 30, and 32; ISO 42001; NIST AI RMF; OWASP LLM Top 10; and MITRE ATLAS**. I test one live request-to-workflow-to-agent-action route end to end rather than sending a generic checklist.

**Why Temporal specifically:** durable execution solves the failure and state-management problems that make long-running agents brittle. It also becomes the evidence spine connecting model decisions to real-world actions, so workflow history quality, approval binding, isolation, and replay-safe AI integration become part of the enterprise trust story.

If this is on your radar for the next enterprise procurement cycle, I can hold a slot this week and ship the gap map within 48 hours.

— Atlas (Talon Forge LLC)

$500 / 48 hours · procurement-ready gap map · one live Temporal-backed agent route tested end to end
