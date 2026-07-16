# Cold Email Template 402 — Patronus AI

**To:** contact@patronus.ai
**From:** atlas@talonforge.com
**Subject:** Patronus Lynx + Lumos + Guardrails audit — 60-col evaluator provenance join-table (SOC 2 CC7.2 + EU AI Act Art. 12)

---

Hi Apoorva,

Following up after seeing Patronus AI's YC W23 + $14M Series A from Lightspeed + Bain + the Evaluator fleet rollout (Lynx + Socrates + Haiku + RAG Hallucination + Conversational) + Lumos HCL-DSL + Guardrails real-time defense + the Compliance + Safety red-team surface.

I'm an AI-agent operator running an EU AI Act / SOC 2 Type II / HIPAA audit pipeline for LLM-eval-platform vendors. I noticed 5 audit-target gaps in the public Patronus AI surface that map cleanly to your roadmap:

1. **Per-evaluator provenance join-table** (per-evaluator-id → per-evaluator-prompt-id → per-evaluator-model-id → per-evaluator-output-id → per-evaluator-rubric-id → per-evaluator-confidence-score → per-LLM-call-id → per-prompt-template-version-id → per-completion-id → per-token-id → per-tool-call-id → per-RAG-retrieval-id → per-citation-id → per-groundedness-score-id → per-guardrail-id → per-prompt-injection-detection-id → per-annotation-id → per-annotator-id → per-tenant-id → per-billing-event-id) per SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 (60+ cols).
2. **Lumos HCL-DSL + Lynx RAG-eval + Guardrails + Safety + Compliance training-corpus-source + fine-tune-license-provenance** per EU AI Act Art. 53(d) GPAI training-data transparency + Art. 53(1)(b) copyright-summary + Art. 53(2) publicly-available-summary + ISO 42001 6.1.4 with 12-column join-table.
3. **Per-evaluator-output-poisoning + per-LLM-call-payload-poisoning + per-tool-call-poisoning + per-RAG-retrieval-poisoning + per-citation-poisoning + per-groundedness-score-poisoning + per-guardrail-bypass + per-red-team-bypass + per-annotation-poisoning** defense per OWASP LLM Top 10 LLM01+LLM03+LLM04+LLM06+LLM08 + MITRE ATLAS AML.T0051+AML.T0054 + EU AI Act Art. 15 + NIST AI RMF MEASURE with 10-column per-trace join-table.
4. **Cross-tenant Patronus Cloud Free + Pro + Enterprise + Dedicated + on-prem AWS/Azure/GCP + per-tenant-id + per-project-id + per-API-key-id isolation-evidence** per SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + EU AI Act Art. 10 + Schrems II + EU-US Data Privacy Framework (Patronus Cloud currently US-only at launch — per-execution region flag must be auditable for EU customer cohort).
5. **WORM-locked cost-attribution join-table** linking per-evaluator-call-cost + per-guardrail-call-cost + per-red-team-attack-cost + per-annotation-cost per SOC 2 CC7.2 + EU AI Act Art. 12 + SEC 17a-4 WORM + IRS 6001 + EU AI Act Annex III 4 high-risk-classification + Aug 2026 GPAI enforcement.

I built a one-page artifact that maps each gap to a specific Patronus AI control + the SOC 2 / EU AI Act clause it satisfies + the verifier command we'd run. Happy to share if useful — also open to a 30-min call to discuss whether this maps to your Q4 enterprise compliance roadmap.

Best,
Atlas
Talon Forge — autonomous AI-agent audit ops

P.S. If your team is exploring per-evaluator-output-traceability for Lynx's RAG-hallucination-detector + Lumos's HCL-based-eval-suite DSL, I have a worked example using Patronus's own public docs + the Lumos HCL spec as the source.
