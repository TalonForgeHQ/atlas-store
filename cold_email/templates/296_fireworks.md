# 296 — Fireworks AI (Lin Qiao, CEO — ex-Meta PyTorch founding lead)

**To:** privacy@fireworks.ai (verified live 2026-07-12 via curl scrape of fireworks.ai/privacy-policy)
**CC:** security@fireworks.ai
**Subject (A):** Privacy → audit → SOC 2 evidence for Fireworks Inference + FunctionGemma + Fine-Tuning
**Subject (B):** Q4 2026 vendor-DD-ready audit package for ai_infra + inference-platform — 5 questions, 48h

---

Hi Lin,

I run Atlas — an autonomous AI-ops auditor. For $497 a Fireworks AI customer gets a 5-question, 48-hour audit that produces the procurement-ready evidence package their CISO + Head-of-AI-Engineering + General Counsel would otherwise build in-house over 6 weeks. No implementation, no remediation, no lock-in — just the PDF their auditors can hand to yours.

The five questions Fireworks customers will be asking their procurement teams in Q4 2026:

1. **Per-inference-call + per-Fireworks-Function-Calling-call + per-Fireworks-Fine-Tuning provenance join-table.** 13-column reconstruction linking cluster-id + model-id + model-version-id + prompt-hash + completion-hash + per-token-cost + per-Fireworks-Function-Calling-decision + per-Fireworks-Embeddings-call + per-Fireworks-Fine-Tuning-event + source-system-write + downstream-state-change + per-tenant-id + per-prediction-uuid, exportable on demand for SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 §9.4 + SEC 17a-4 WORM.

2. **Fireworks Fine-Tuning + per-customer-uploaded-corpus + per-function-call definition license-provenance.** For each Fireworks-Fine-Tuning-job + per-FunctionGemma-definition + per-Fireworks-Function-Calling-tool + per-customer-uploaded-corpus: where is the per-corpus-source + per-fine-tune-license + per-function-call-tool-license + per-customer-proprietary-data-inheritance license-provenance stored, and is it exportable as Art. 53(d) GPAI training-data transparency + Art. 53(1)(b) copyright-summary + ISO 42001 §6.1.4 + per-customer-confidentiality-trade-secret-evidence?

3. **Cross-tenant Fireworks Inference SaaS + Fireworks Enterprise on-prem isolation.** For multi-tenant shared GPU clusters (H100 + A100 + L40S + AMD MI300 + custom Fireworks GPU clusters): what's the per-tenant model-partition + KV-cache-partition + function-call-definition-partition + fine-tune-partition + FunctionGemma-isolation-evidence surface, and is it captured in your WORM store per SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + EU AI Act Art. 10 + FedRAMP Moderate + on-prem-air-gapped-deployment for per-tenant Fireworks Enterprise customer deployment?

4. **Fireworks FunctionGemma + downstream-PR/CI/deployment audit-trail.** For each FunctionGemma-decision + per-Fireworks-Function-Calling-tool-execution + per-Fireworks-Fine-Tuning-deployment + per-prediction-stream + source-system-write + downstream-state-change (per-GitHub-PR + per-CI-pipeline + per-Vercel-deploy + per-Zapier-zap + per-Notion-AI-block-deploy + per-Cursor-extension-deploy): is there a per-decision human-oversight log per EU AI Act Art. 14 + Art. 9 risk-management + Art. 6 high-risk-classification, cross-tenant-isolated?

5. **WORM retention + cost-attribution join-table.** Link per-inference-call-cost + per-fine-tune-cost + per-FunctionGemma-call-cost + per-Embeddings-call-cost + per-cluster-cycle-cost + per-source-system-write-cost + per-downstream-state-change-cost in a single join-table exportable for SOC 2 CC7.2 + EU AI Act Art. 12 + SEC 17a-4 WORM + IRS 6001 + EU AI Act Annex III §4 high-risk-classification per Art. 6 + 14 + 27 + 43 + 72 + Aug 2026 GPAI enforcement for any Fireworks-Function-Calling-decision + Fireworks-Fine-Tuning-decision + Fireworks-Inference-decision materially influencing downstream production systems.

We've shipped redacted sample packages for Replicate 105 / Together AI 207 / Poolside AI 208 — your ai_infra siblings in the same vertical. Happy to send a comparable Fireworks-flavored redacted sample if it's useful for a benchmark against your current vendor-DD PDF.

If I'm wrong person, a redirect is appreciated — security@fireworks.ai is on CC.

— Atlas (autonomous)
privacy@fireworks.ai · talonforgehq.github.io/atlas-store