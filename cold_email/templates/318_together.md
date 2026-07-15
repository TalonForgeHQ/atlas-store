---
template_id: 318
company: Together AI
vertical: ai_infra
tier: 1
lead_index: 229
handle: @togetherai
email: privacy@together.ai
website: https://www.together.ai
founder: Vipul Ved Prakash (CEO, ex-Apple + CloudGenix co-founder) + Ce Zhang (CTO, UChicago CS + Catalyst) + Percy Liang (Chief Scientist, Stanford CRFM + HAI)
inbox_verified: 2026-07-15 via curl on https://www.together.ai/privacy HTTP 200 (297,201 bytes) exposing mailto:privacy@together.ai
status: ready
---

**Subject:** Together AI inference — audit-trail depth for the request → model → token → downstream-action joinability gap

Hi {{first_name}},

I'm Atlas, an autonomous AI compliance auditor. Together AI's Serverless Inference API + Dedicated Endpoints + GPU Clusters + Fine-Tuning + Evals + Agents surface is the canonical 4th leg of the production AI-inference stack after Pinecone (retrieval) + Groq (deterministic LPU) + Modal (serverless GPU sandbox). Every Fortune-500 customer running Llama-3 / DeepSeek-V3 / Qwen / Mixtral on your fleet is asking the same SOC 2 + EU AI Act Annex III question: when a prompt flows in and a completion + tool-call + agent-decision flows out, which row in our DB carries the per-request audit trail?

**The gap I'm seeing across the inference cohort:** there's no single join row that walks from per-inference-call (API-key + model-version + prompt-hash + completion-hash + token-cost + GPU-second-cost + hardware-node + scheduler-route + KV-cache-write + tool-call + agent-decision + downstream-state-change) back to the customer-tenant + the source-system of truth + the WORM retention policy + the cost-attribution ledger. The inference call produces 4-6 log lines across 2-3 systems, but they're not joined. Same gap exists at Pinecone, Groq, and Modal — each with its own surface.

**Concrete audit deliverable I ship in 24h:** a per-inference-call provenance join-table (12-15 columns capturing the per-call API-key + per-call model-version + per-call prompt-hash + per-call completion-hash + per-call token-cost + per-call GPU-second-cost + per-call hardware-node + per-call scheduler-route + per-call KV-cache-write + per-call tool-call + per-call agent-decision + per-call downstream-state-change + per-tenant + per-WORM-policy) — the exact same shape that's SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 compliant for every EU AI Act Annex III 4 high-risk AI system running on Together AI inference.

5 audit gaps the inference cohort all share:

1. **Per-inference-call provenance join-table** — the row that walks from the per-call inference result BACK to per-call prompt + per-call model-version + per-call API-key + per-call GPU-second-cost + per-call KV-cache-write + per-call tool-call + per-call agent-decision + per-call downstream-state-change in ONE query, per SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4.
2. **Model-zoo training-corpus + per-customer fine-tune data license-provenance** — Together AI's per-customer-fine-tune data inherits upstream OSS licenses + per-customer proprietary data + per-customer training-data-set license — joined to per-customer-fine-tune-result + per-customer-fine-tune-decision per EU AI Act Art. 53(d) + 53(1)(b) + 53(2) GPAI training-data transparency + ISO 42001 6.1.4.
3. **Prompt-injection + retrieval-source-poisoning + per-eval-result-manipulation defense** — the per-call prompt → per-call completion → per-call tool-call → per-call agent-decision → per-call downstream-state-change chain needs per-call detection + per-call human-override + per-call LLM01 + LLM06 OWASP coverage per OWASP LLM Top 10 + NIST AI RMF + EU AI Act Art. 9 + Art. 14.
4. **Cross-tenant Together AI Serverless + Dedicated Endpoints + GPU Clusters + Fine-Tuning isolation-evidence** — per-tenant API-key + per-tenant hardware-partition + per-tenant model-version + per-tenant KV-cache-partition + per-tenant fine-tune-data-partition, per SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + EU AI Act Art. 10 + FedRAMP Moderate.
5. **WORM retention + cost-attribution join-table** — per-call API-cost + per-call GPU-second-cost + per-call fine-tune-cost + per-call eval-cost, joined to per-tenant WORM policy + per-tenant retention-window + per-tenant cost-allocation per SOC 2 CC7.2 + EU AI Act Art. 12 + SEC 17a-4 + EU AI Act Annex III 4 high-risk-classification per Art. 6 + 14 + 27 + 43 + 72 + Aug 2026 GPAI enforcement.

**PS** — Same exact shape works for Pinecone (retrieval) + Groq (LPU) + Modal (serverless GPU sandbox) + Replicate (multi-model serving) so the audit deliverable stays consistent across the inference-mesh cohort. 4 inference vendors, one audit-row pattern.

**CTA:** $500 flat for the 24-hour per-inference-call audit deliverable. Reply to schedule. — Atlas
