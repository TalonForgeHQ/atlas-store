# Cold Email Template — Lead 423 WhyLabs (WhyLabs Inc.)

**Vertical:** ai_agents_infra (Tier-1, 23rd-sibling after Vellum 416 / Parea AI 417 / Confident AI 418 / Galileo AI 419 / Atla 420 / LangWatch 421 / Ragas 422)
**Best verified inbox:** founders@whylabs.ai (live 2026-07-17 from direct scrape of https://whylabs.ai/contact + footer rendering)
**Engineering inbox:** ahmad@whylabs.ai (Ahmad Alshareef, OSS maintainer of whylabs/llm-tools + whylogs OSS) — verified via github.com/whylabs commits API
**Generic front door:** hello@whylabs.ai + support@whylabs.ai

---

**Subject:** WhyLabs / whylogs OSS — 5 questions before we route our ai_agents_infra eval-cohort slot 23 to you.

Ahmad / Melissa — quick one. We're shipping a 60+ column join-table audit binder across the 23-vendor ai_agents_infra cohort (Vellum 416 + Parea 417 + Confident AI 418 + Galileo 419 + Atla 420 + LangWatch 421 + Ragas 422 + now WhyLabs 423). The whylogs OSS lane is the only one with a 8.5K+ star Apache-2.0 data-logging-first OSS vehicle behind it, and the LLM-evaluation extension (whylabs/llm-eval + whylabs/langkit) is the canonical reference for "data-quality-meets-LLM-Observability" teams in our diligence pipeline. Before we route the cohort slot and start drafting the WhyLabs-specific binder, five questions — answers go straight into the WhyLabs row of the public ai_agents_infra scorecard:

1. **per-eval-run-id → per-metric-id → per-llm-output-id → per-confusion-score-id → per-prompt-template-version-id → per-completion-id → per-token-id → per-data-profile-id → per-conversation-id lineage** at the WhyLabs Observe + LangKit + Guardrails row level: does whylabs/llm-eval ship a single join-table that maps every metric-run to the llm-output to the prompt-version to the completion to the token all the way to a per-WhyLabs-tenant-id + per-WhyLabs-project-id + per-billing-event-id? The auditors we work with want this in 60+ columns for SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4. Right now your index.html showcases Observe + Guardrails + LangKit — confirm the underlying lineage carries the 60-col shape so we can pull the audit row out clean.

2. **per-prompt-injection-id + per-data-drift-id + per-prompt-drift-id + per-response-quality-regression-id + per-guardrail-trip-id** surface in the WhyLabs Guardrails + Drift-detection trail: given that whylogs OSS is the canonical data-logging backbone for the major ML/LLM pipelines (LangChain + LlamaIndex + OpenAI + Anthropic + AWS SageMaker + Databricks + Snowflake), does your eval-pipeline detect OWASP LLM Top 10 LLM01 (prompt injection) + LLM02 (sensitive information disclosure) + LLM06 (excessive agency) + LLM09 (misinformation) coverage, with per-defense-row in 15+ columns tied to MITRE ATLAS AML.T0051 + EU AI Act Art. 15 + ISO 42001 6.1.4? LangKit text-quality + toxicity + privacy + relevance metrics + Guardrails real-time enforcement are the canonical hints — confirm the per-defense-row is exposed to customers.

3. **Cross-WhyLabs-tenant isolation-evidence** at the WhyLabs SaaS + self-hosted whylogs OSS row level: do you have SOC 2 CC6.1 + GDPR Art. 28 + EU AI Act Art. 10 + ISO 42001 A.6.1.4 attested per-WhyLabs-tenant-id + per-WhyLabs-project-id isolation-test-result, optional CMK/BYOK for self-hosted whylogs OSS deployments, and a per-tenant-residue-cleanup procedure with completion-of-deletion timestamp? We're seeing the EU-banking + insurance + healthcare side specifically ask for per-WhyLabs-tenant-id no-leakage-evidence baseline.

4. **Data-Drift + Model-Drift + Concept-Drift + LLM-Specific-Drift** lineage at the WhyLabs Observe + whylogs OSS row level: WhyLabs pioneered the canonical 8.5K+ star Apache-2.0 OSS data-logging-first vehicle, with the LLM-evaluation extension (LangKit) + Guardrails adding the eval + safety layer on top. Does the per-eval-id + per-metric-id + per-data-profile-id + per-drift-event-id lineage propagate through WhyLabs's drift-detection surface back to the per-eval-run-id + per-tenant-id + per-billing-event-id join-table, with per-metric-version change-log + per-data-profile-version-id? This is the audit row we're missing across all 22 siblings.

5. **WORM retention + per-eval-storage-cost-attribution** join-table: for SEC 17a-4 + EU AI Act Annex III 4 + Aug 2026 GPAI enforcement, does WhyLabs store every per-eval-run-id + per-metric-id + per-data-profile-id + per-drift-event-id in a WORM-tier storage class with a cost-attribution row breaking down per-eval-storage-cost + per-LLM-call-cost + per-guardrail-trip-cost? Auditor-friendly join in 12+ columns?

And one bonus question: **EU AI Act Art. 53(d) GPAI training-data transparency** for the whylogs OSS evaluation-corpus + LangKit fine-tune recipe — given that whylabs/whylogs is itself used as part of GPAI evaluation + data-quality pipelines, does WhyLabs publish a per-training-corpus-source + per-fine-tune-license-provenance row in 12+ columns tied to EU AI Act Art. 53(d) + Art. 53(1)(b) + Art. 53(2) + ISO 42001 6.1.4?

The deliverable is a **6-page audit binder** with the 5-evidence-table shape we ship for every ai_agents_infra vendor, plus a free **10-vendor ai_agents_infra cohort overlap map** (Vellum + Parea + Confident AI + Galileo + Atla + LangWatch + Ragas + WhyLabs + 2 more) as a no-strings deliverable. $500 fixed-fee in 48h, or $497/mo retainer with quarterly evidence refresh + audit-defender call participation — once we have your answers.

If 30 minutes in the next two weeks makes sense, send a Calendly link or just two windows that work for Ahmad + Melissa.

— Atlas / Talon Forge LLC
