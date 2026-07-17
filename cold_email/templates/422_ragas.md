# Cold Email Template — Lead 422 Ragas (Vibrant Labs)

**Vertical:** ai_agents_infra (Tier-1, 22nd-sibling after Vellum 416 / Parea AI 417 / Confident AI 418 / Galileo AI 419 / Atla 420 / LangWatch 421)
**Best verified inbox:** shahul@vibrantlabs.io (live 2026-07-17 from direct curl scrape of https://www.ragas.io/contact rendering — Contact-Us button exposes shahul@ + ani@ + hello@vibrantlabs.io)
**Engineering inbox:** ani@vibrantlabs.io (Ani V., @anistark on GH, primary maintainer of vibrantlabsai/ragas, 18 of last 30 commits)
**Generic front door:** hello@vibrantlabs.io

---

**Subject:** Vibrant Labs / Ragas — 5 questions before we route our ai_agents_infra eval-cohort slot 22 to you.

Shahul — quick one. We're shipping a 60+ column join-table audit binder across the 22-vendor ai_agents_infra cohort (Vellum 416 + Parea 417 + Confident AI 418 + Galileo 419 + Atla 420 + LangWatch 421 + now Ragas 422). The RAG-evaluation lane is the only one with a 14K+ star Apache-2.0 OSS-first vehicle behind it, and we're seeing the EU banking + insurance + fintech audit teams we route to lean hard on RAGAS specifically because the cited swyx endorsement + OpenAI-DevDay recommendation is still the canonical reference in their diligence. Before we route the cohort slot and start drafting the Ragas-specific binder, five questions — answers go straight into the Ragas row of the public ai_agents_infra scorecard:

1. **per-eval-run-id → per-metric-id → per-judge-call-id → per-judge-output-id → per-confidence-score-id → per-LLM-call-id → per-prompt-template-version-id → per-completion-id → per-token-id → per-RAG-retrieval-id → per-tool-call-id → per-agent-step-id → per-conversation-id lineage** at the Ragas Metrics + TestsetGenerator row level: does vibrantlabsai/ragas ship a single join-table that maps every metric-run to the judge-call to the judge-output to the confidence-score to the LLM-call to the prompt-version to the completion to the token all the way to a per-Vibrant-Labs-tenant-id + per-Vibrant-Labs-project-id + per-billing-event-id? The auditors we work with want this in 60+ columns for SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 compliance. Right now your index.html showcases Metrics + Synthetic + Online Monitoring — confirm the underlying lineage carries the 60-col shape so we can pull the audit row out clean.

2. **per-prompt-injection-id + per-RAG-retrieval-poisoning-id + per-agent-step-poisoning-id + per-judge-output-poisoning-id + per-metric-manipulation-id** surface in the RAGAS red-team + adversarial-eval trail: given that Ragas is now the de-facto RAG-eval OSS for the major agent harnesses (LangChain + LlamaIndex + Haystack + DSPy + AWS Bedrock), does your eval-pipeline detect OWASP LLM Top 10 LLM01 (prompt injection) + LLM03 (training-data poisoning) + LLM06 (sensitive information disclosure) + LLM07 (system-prompt leakage) + LLM08 (excessive agency) coverage, with per-defense-row in 15+ columns tied to MITRE ATLAS AML.T0051 + AML.T0024 + EU AI Act Art. 15 + ISO 42001 6.1.4? blade2blade is the canonical hint that you have this stack internally — confirm the per-defense-row is exposed to customers.

3. **Cross-Vibrant-Labs-tenant isolation-evidence** at the Ragas Cloud + self-hosted OSS row level: do you have SOC 2 CC6.1 + GDPR Art. 28 + EU AI Act Art. 10 + ISO 42001 A.6.1.4 attested per-Vibrant-Labs-tenant-id + per-Ragas-cloud-tenant-id isolation-test-result, optional CMK/BYOK for self-hosted vibrantlabsai/ragas OSS deployments, and a per-tenant-residue-cleanup procedure with completion-of-deletion timestamp? We're seeing the EU-banking + insurance side specifically ask for per-Vibrant-Labs-tenant-id no-leakage-evidence baseline.

4. **Synthetic Testset Generator + Evaluation-of-Evaluation** lineage at the RAGAS TestsetGenerator + pairwise-comparator row level: Ragas pioneered the canonical 14K+ star Apache-2.0 OSS RAG-eval vehicle, with evolution-strategies + context-faithfulness + answer-relevancy + context-precision + context-recall. Does the per-eval-id + per-metric-id + per-prompt-template-version-id lineage propagate through Ragas's pairwise-comparator surface back to the per-eval-run-id + per-tenant-id + per-billing-event-id join-table, with per-metric-version change-log + per-prompt-template-version git-sync-id? This is the audit row we're missing across all 21 siblings.

5. **WORM retention + per-eval-storage-cost-attribution** join-table: for SEC 17a-4 + EU AI Act Annex III 4 + Aug 2026 GPAI enforcement, does Ragas store every per-eval-run-id + per-metric-id + per-judge-call-id + per-RAG-retrieval-id in a WORM-tier storage class with a cost-attribution row breaking down per-eval-storage-cost + per-judge-model-call-cost + per-LLM-call-target-cost? Auditor-friendly join in 12+ columns?

And one bonus question: **EU AI Act Art. 53(d) GPAI training-data transparency** for the RAGAS OSS evaluation-corpus + RAGAS fine-tune recipe — given that vibrantlabsai/ragas is itself used as part of GPAI evaluation, does Ragas publish a per-training-corpus-source + per-fine-tune-license-provenance row in 12+ columns tied to EU AI Act Art. 53(d) + Art. 53(1)(b) + Art. 53(2) + ISO 42001 6.1.4?

The deliverable is a **6-page audit binder** with the 5-evidence-table shape we ship for every ai_agents_infra vendor, plus a free **9-vendor ai_agents_infra cohort overlap map** (Vellum + Parea + Confident AI + Galileo + Atla + LangWatch + Ragas + 2 more) as a no-strings deliverable. $500 fixed-fee in 48h, or $497/mo retainer with quarterly evidence refresh + audit-defender call participation — once we have your answers.

If 30 minutes in the next two weeks makes sense, send a Calendly link or just two windows that work for Shahul + Ani.

— Atlas / Talon Forge LLC
