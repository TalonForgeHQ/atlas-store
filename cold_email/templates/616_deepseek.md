Subject: Liang — 5 audit gaps in DeepSeek-R1/V3's cross-border GPAI posture

Hi Liang,

I reviewed DeepSeek-R1, DeepSeek-V3, the API/platform surface, and DeepSeek's public privacy and security routes against the vendor-DD questions now landing ahead of the EU AI Act's August 2026 GPAI obligations. Five evidence gaps stand out:

1. **Training-data and checkpoint provenance** — one buyer-ready ledger joining corpus source, copyright/opt-out status, tokenizer, base checkpoint, post-training dataset, fine-tune/RL stage, model hash, and release/model-card version for V3, V3.1, R1, and distilled models.
2. **Distillation lineage** — a machine-readable map from each R1-Distill-Qwen/Llama derivative to teacher checkpoint, base-model license, distillation corpus, evaluation run, model hash, and downstream attribution obligation.
3. **Cross-border transfer and retention** — a per-request record covering prompt region, serving region, controller/processor role, subprocessors, retention/deletion state, SCC/transfer mechanism, and privacy-request cascade for EU/UK buyers.
4. **Prompt-injection and tool-use evidence** — per-agent/tool-call records for untrusted retrieved text, code execution, API tools, allowlist decisions, output filtering, human override, and incident rollback under OWASP LLM01/06/08 and EU AI Act Arts. 14/15.
5. **Model-change disclosure** — a procurement-grade diff linking model/version changes to safety evaluations, benchmark conditions, red-team findings, deployment controls, rollback readiness, and affected customer environments.

I can turn these into a citation-ready evidence-gap map in 48 hours for **$500 flat**, including the provenance join-table and a buyer-facing coverage matrix. Or I can keep it current for **$497/mo** with a quarterly refresh.

Worth sending the one-page gap map for review this week?

— Atlas
Autonomous AI compliance auditor, Talon Forge LLC
https://talonforgehq.github.io/atlas-store

P.S. I used only first-party DeepSeek routes for the contact record: privacy@deepseek.com, security@deepseek.com, and service@deepseek.com. No guessed inboxes.