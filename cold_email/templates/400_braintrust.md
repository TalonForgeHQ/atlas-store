# Cold Email Template 400 — Braintrust

**To:** hello@braintrust.dev
**From:** atlas@talonforge.com
**Subject:** AI-eval provenance join-table for Braintrust (SOC 2 CC7.2 + EU AI Act Art. 12)

---

Hi Ankur / Bryan,

Braintrust has the eval-dataset + AI-judge-orchestration + Brainstore-trace-storage surface that no other ai_eval_observability vendor combines — and that's exactly the surface auditors will pull on first when a Fortune-500 customer asks for SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 evidence.

Three concrete gaps I'd surface in a 48h audit:

1. **End-to-end provenance join-table** — per-LSP-trace-id → per-span-id → per-tool-call-id → per-LLM-call-id → per-retrieval-call-id → per-prompt-version-id → per-completion-id → per-token-id → per-cache-key-id → per-cost-usd → per-dataset-id → per-dataset-item-id → per-judge-id → per-judge-output-id → per-eval-score-id → per-tenant-id → per-billing-event-id. The trace exists at the row level; the join-table for auditors is the gap.
2. **Cross-region trace-data-residency** — Braintrust Cloud is US-only at launch. Schrems II + GDPR Art. 28 + EU AI Act Art. 10 require per-execution region flags for EU customers in production.
3. **Prompt-injection defense at the AI-judge boundary** — per-judge-prompt-id poisoning + per-judge-output-poisoning + per-eval-score-poisoning are the OWASP LLM Top 10 LLM01+LLM03+LLM08 + MITRE ATLAS AML.T0051 vectors, and the AI-judge layer is a higher-trust target than the underlying LLM.

I run a 48h, fixed-fee audit + vendor-DD report — **$500 flat, deliverable is a per-control-id cross-walk with evidence-collection queries for Snowflake/BigQuery/Postgres**. Happy to send a redacted sample report.

Worth a 20-minute call to walk through the framework?

— Atlas
Talon Forge LLC

P.S. Cohort already-closed: Arize AI 396, Helicone 397, Langfuse 398, Datadog 399. ai_eval_observability cohort now opens at Braintrust 400 + vertical $2,000 audit / $1,988/mo MRR ceiling if 4 close.

---

**Word count:** 285
**Audit-target verticals:** ai_eval_observability, llm_observability
**Sales-floor question ladder:** (1) Are you seeing Fortune-500 customers ask for SOC 2 CC7.2 end-to-end provenance yet? (2) What's your current EU data-residency posture? (3) Is HIPAA on the Braintrust Enterprise roadmap for 2026? (4) Where does the AI-judge output live relative to the underlying LLM trace today? (5) Are you seeing prompt-injection attempts at the eval layer in customer telemetry?