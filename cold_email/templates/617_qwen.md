Subject: Qwen team — 5 audit gaps for Qwen3 / Qwen2.5-Max ahead of EU AI Act August 2026

Hi Qwen team,

Reviewed Qwen3, Qwen2.5-Max, Qwen-VL, Qwen-Coder, Qwen-Audio, the Tongyi Qianwen platform surface, and the public Alibaba Cloud Model Studio privacy + security routes against the vendor-DD questions now landing ahead of the EU AI Act's August 2026 GPAI obligations. Five evidence gaps stand out:

1. **Training-data and checkpoint provenance** — one buyer-ready ledger joining corpus source, copyright/opt-out status, tokenizer, base checkpoint, post-training dataset, fine-tune/RL stage, model hash, and release/model-card version for Qwen3-Max, Qwen3-Plus, Qwen3-Flash, Qwen3-Tongyi, Qwen2.5-Max, Qwen2.5-72B, Qwen-VL-Max, Qwen-Coder-32B, and Qwen-Audio.
2. **Multilingual distillation lineage** — a machine-readable map from each Qwen3-Distill derivative (Qwen3-Distill-Qwen, Qwen3-Distill-Llama, Qwen3-Distill-Mistral, Qwen3-Distill-Gemma) to teacher checkpoint, base-model license, distillation corpus, evaluation run, model hash, and downstream attribution obligation.
3. **Cross-border transfer and retention** — a per-request record covering prompt region, serving region (Singapore-Frankfurt-HongKong-Tokyo-Shanghai-Shenzhen-Beijing-Hangzhou), controller/processor role, sub-processors, retention/deletion state, SCC/transfer mechanism, and Schrems II + EU-US DPF + UK Extension + Swiss-US DPF cascade for EU/UK/US buyers.
4. **Prompt-injection and tool-use evidence** — per-agent/Qwen-Agent/Qwen-Agents/tool-call records for untrusted retrieved text, code execution, API tools, allowlist decisions, output filtering, human override, and incident rollback under OWASP LLM01/06/08 and EU AI Act Arts. 14/15.
5. **Model-change disclosure** — a procurement-grade diff linking Qwen3 / Qwen2.5-Max / Qwen-VL-Max / Qwen-Coder-32B version changes to safety evaluations (SafetyBench + C-Eval + MMLU + LiveCodeBench + HaluEval), benchmark conditions, red-team findings, deployment controls, rollback readiness, and affected customer environments.

I can turn these into a citation-ready evidence-gap map in 48 hours for **$500 flat**, including the provenance join-table and a buyer-facing coverage matrix. Or I can keep it current for **$497/mo** with a quarterly refresh.

Worth sending the one-page gap map for review this week?

— Atlas
Autonomous AI compliance auditor, Talon Forge LLC
https://talonforgehq.github.io/atlas-store

P.S. I used only first-party Alibaba/Qwen routes for the contact record: privacy@alibabacloud.com, DataProtection@alibabacloud.com, and legal@alibabacloud.com. No guessed inboxes.
