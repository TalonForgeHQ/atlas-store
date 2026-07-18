# Lead 353 — Helicone

**Vertical:** ai_observability
**Tier:** 1
**Website:** https://www.helicone.ai/
**Founder contact:** Cole Gottdank, co-founder
**Verified public inbox:** help@helicone.ai
**Current company state:** acquired by Mintlify; Helicone remains live in maintenance mode

---

**Subject:** 5 audit questions for Helicone's LLM observability evidence chain

Hi Cole,

Helicone says 16,000 organizations have routed more than 14.2 trillion tokens through the platform, and its March 2026 Mintlify announcement says the service will remain live in maintenance mode. That makes one diligence question especially concrete: can a customer still reconstruct every production LLM call from prompt and model version through provider route, tool or retrieval context, cache decision, evaluation, cost, and downstream action?

I run a focused **$500 / 48-hour audit** for production AI platforms. These are the five questions I would test on one Helicone-observed request path:

1. **End-to-end call provenance:** Can one export join organization, project, environment, user and session IDs to prompt-template version, model and provider route, request and response hashes, token usage, latency, error or fallback, cache event, evaluation result, tool call, downstream action, and cost?
2. **Prompt, model, and evaluation change control:** Are prompt commits, model/provider changes, routing rules, fallback policy, cache thresholds, evaluator versions, datasets, feature flags, and A/B tests tied to approvals, deployment windows, signed versions, and reproducible rollback points?
3. **Hostile input and telemetry integrity:** What prevents prompt injection, poisoned RAG context, malicious tool output, forged feedback, evaluation-dataset poisoning, or cache poisoning from corrupting the observability record or influencing another production decision?
4. **Tenant, secret, and residency isolation:** Can customers retrieve tests proving separation across organizations, projects, environments, API keys, provider credentials, prompts, responses, evaluations, caches, exports, regions, support access, and zero-retention paths?
5. **Maintenance-mode incident reconstruction:** After a provider outage, compromised prompt, incorrect score, cross-tenant exposure, acquisition handoff, or deletion request, can Helicone identify every affected call, preserve WORM-capable evidence, and prove rollback or deletion across logs, caches, datasets, exports, replicas, and backups?

The deliverable is a procurement-ready gap map and fix specification mapped to **SOC 2 CC6.1 and CC7.2; EU AI Act Articles 9, 12, 14, and 15; GDPR Articles 17, 28, 30, and 32; ISO 42001; NIST AI RMF; OWASP LLM Top 10; MITRE ATLAS; ISO 27701; and acquisition-transition controls**. I test one live request-to-observation-to-evaluation path end to end rather than sending a generic checklist.

**Why Helicone specifically:** observability systems hold the evidence buyers rely on when an AI incident happens. The Mintlify transition raises the value of proving that this evidence remains complete, isolated, exportable, retained, and deletion-aware while the product operates in maintenance mode.

If this is useful for the post-acquisition operating plan, I can hold a slot this week and ship the gap map within 48 hours.

— Atlas (Talon Forge LLC)

$500 / 48 hours · procurement-ready gap map · one live Helicone request-to-observation-to-evaluation path tested end to end
