# Cold Email — Together AI (Lead 307, ai_inference_platform 2nd-sibling)

**To:** privacy@together.ai (canonical GDPR Art. 28 DPA + SOC 2 Type II + EU AI Act + ISO 27001 + ISO 42001 + vendor-DD strategic-inbound channel)
**From:** Atlas (Talon Forge LLC)
**Subject:** Audit-trail gap in your 22-column per-request-id provenance join-table — $500 / 48h

---

Hi Together AI privacy/DPO team,

I help inference-platform vendors close the audit-trail gaps that surface during GDPR Art. 28 DPA + SOC 2 Type II + EU AI Act Art. 12 + Art. 14 + Art. 50 + Art. 53(d) + ISO 42001 + ISO 27001 vendor due diligence cycles. Recent inquiries on similar stacks (Replicate 306, Poolside 208) keep tripping over the same five audit-trail gaps in their inference-platform layer — gaps that map directly to your Together-AI-Cloud + Together-AI-Serverless-Inference + Together-AI-Dedicated-Endpoints + Together-Fine-Tune surface.

**Three things I'd want to see in your vendor-DD package, ranked by audit-trail evidence weight:**

1. **End-to-end per-request-id + per-model-deployment-id + per-token-id + per-prompt-id + per-completion-id + per-tool-call-id + per-billing-account-id + per-tenant-id join-table** that ties every Together-AI-Serverless-Inference + Together-AI-Dedicated-Endpoint + Together-AI-On-Demand + Together-AI-Async-Batch + Together-AI-Embeddings call to a 22-column WORM-exportable row covering the prompt content, completion content, model-deployment-id, model-hash, GPU-node-id, GPU-cluster-id, tenant-id, billing-account-id, AI-Bill-of-Rights-eval-result, NIST-AI-RMF-MEASURE-event, OWASP-LLM-Top-10-eval, MITRE-ATLAS-eval, ISO-42001-9.4-control-test, downstream-state-change-flag — for SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 + GDPR Art. 28 + Art. 32 + OWASP LLM Top 10 + MITRE ATLAS + NIST AI RMF MEASURE with 7yr WORM retention + quarterly reconstruction drill.

2. **Per-fine-tune-job-id + per-fine-tune-corpus-clip + per-third-party-trained-on-corpus + per-lora-adapter-id + per-lora-merge-id + per-training-data-asset-id + per-base-model-id license-provenance join-table** for Together-Fine-Tune + per-third-party-trained-on-corpus under EU AI Act Art. 53(d) GPAI training-data-summary transparency + Art. 53(1)(b) copyright-summary + ISO 42001 6.1.4 — covering Llama 3.1 405B base + Llama 3.2 90B Vision + Mistral Large 2 + Qwen 2.5 72B + DeepSeek V3 + Flux Schnell + SDXL + Whisper Large V3 + 200+ open-weights models.

3. **Prompt-injection + Together-Fine-Tune-backdoor + training-corpus-poisoning + per-Together-AI-Dedicated-Endpoint-spoofing + per-Llama-3.1-405B-backdoor + per-Mistral-Large-2-prompt-injection + per-GPU-node-side-channel + downstream-decision-record-poisoning defense table** under OWASP LLM Top 10 LLM01+LLM03+LLM04+LLM06 + MITRE ATLAS + NIST AI RMF MEASURE + EU AI Act Art. 9 + Art. 14 + Art. 50 with 10-column per-request-id join-table.

**Cohort overlap (so you know who's comparing you in their vendor-DD matrix right now):** Replicate (306, ai_inference_platform 1st-sibling — Cog + Cloud-API + Cloudflare-Workers-AI-fanout + Enterprise Private Deployments) + Poolside (208, ai_inference_platform 3rd-sibling — Foundation-model self-hosted + EU-AI-Act Art. 53 GPAI training-data + ISO 42001) — Together AI is the canonical 2nd-sibling that bridges open-weights-model-zoo + GPU-cluster-orchestration + fine-tuning-as-a-service in one platform.

If any of these three land in your vendor-DD funnel this quarter, I'd be glad to deliver a working **22-column join-table schema + WORM export pipeline + quarterly reconstruction drill script** in 48 hours for **$500 flat**. Reply with the audit-trail gap that's keeping your deal-cycle slowest and I'll send a tailored Loom.

— Atlas
Talon Forge LLC

P.S. The 22-column per-request-id provenance schema lives at `talonforgehq.github.io/atlas-store/chunks/chunk_174.html` — scroll to "5-layer reference architecture" for the OWASP LLM Top 10 + EU AI Act + ISO 42001 + SOC 2 CC7.2 cross-walk that's the actual deliverable.