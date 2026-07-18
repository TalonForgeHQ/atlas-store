# Lead 57 — Vercel

**Vertical:** b2b_saas
**Tier:** 1
**Website:** https://vercel.com/
**Founder / CEO:** Guillermo Rauch
**Verified public inbox:** privacy@vercel.com

---

**Subject:** 5 audit questions on Vercel AI SDK, v0, and agentic deploys

Hi Guillermo,

Vercel now sits on both sides of the production-AI boundary: teams build agentic interfaces with the AI SDK and v0, then ship them through Vercel's deployment, preview, observability, and integration surfaces. That means a buyer needs more than a successful deployment badge. They need to reconstruct which tenant, user prompt, model, provider route, tool call, generated code change, environment variable, preview deployment, approval, and production promotion produced each customer-facing result.

I run a focused **$500 / 48-hour audit** for production AI platforms. These are the five questions I would test against Vercel:

1. **Prompt-to-deploy provenance:** Can one export join project and team IDs, user/session, AI SDK or v0 prompt, model and provider route, prompt/template version, retrieved context, tool calls, generated files, Git commit, preview deployment, approver, production deployment, latency, token usage, and cost?
2. **Model and provider change control:** Does every completion bind to the exact AI SDK version, provider adapter, model identifier, routing/fallback policy, system prompt, safety policy, and deployment approval active at execution time? Can an enterprise buyer reproduce the path after a provider outage or fallback?
3. **Hostile-input and supply-chain defense:** When an agent consumes repository text, issue content, documentation, generated UI instructions, third-party MCP output, package metadata, or integration webhooks, what stops prompt injection and dependency poisoning from reaching tool calls, secrets, build steps, or production state?
4. **Tenant, secret, and preview isolation:** Can customers retrieve project-scoped access logs, secret-read events, AI Gateway/model-routing events, preview-to-production promotion history, deletion evidence, regional residency, and tests proving one team's prompt, cache, logs, embeddings, or environment variables cannot cross into another team?
5. **Incident evidence and rollback:** When generated code deploys successfully but behaves incorrectly, a model fallback changes output, or an agent mutates production state, can Vercel reconstruct the full chain and bind a rollback to the exact prompt, tool call, build artifact, deployment, and human approval with WORM-capable evidence?

The deliverable is a procurement-ready gap map and fix specification mapped to **SOC 2 CC6.1 and CC7.2; EU AI Act Articles 12, 14, and 15; GDPR Article 28; ISO 42001; NIST AI RMF; OWASP LLM Top 10; MITRE ATLAS; SLSA; and ISO 27001**. I test one live prompt-to-preview-to-production path end to end rather than sending a generic checklist.

**Why Vercel specifically:** AI SDK provider abstraction and v0-generated applications compress model selection, code generation, tool execution, and deployment into one workflow. That speed is the product advantage, but it also makes evidence gaps compound across model, code, infrastructure, and customer-facing state.

If this is on your radar for the next enterprise procurement cycle, I can hold a slot this week and ship the gap map within 48 hours.

— Atlas (Talon Forge LLC)

$500 / 48 hours · procurement-ready gap map · one live environment tested end to end
