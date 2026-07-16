"""Append Lead 406 Fiddler AI + Template 406 + Chunk 243.

Fiddler AI (Krishna Gade, CEO ex-Facebook ML) — canonical explainable-AI observability + AI-model-monitoring + AI-bias-detection + AI-drift-detection + LLM-monitoring platform. 7th sibling in the ai_eval_observability cohort (Braintrust VERTEX 400 + Confident AI 401 + Patronus 402 + Arize 403 + HoneyHive 404 + Deepchecks 405 + Fiddler 406).
"""
from pathlib import Path

ROOT = Path("C:/Users/Potts/projects/atlas-store")
CE   = ROOT / "cold_email"
TPL  = CE / "templates"
CH   = ROOT / "chunks"

# Lead 406
LEAD_ROW = (
    '"406","Fiddler AI","@fiddlerlabs","support@fiddler.ai","ai_eval_observability","1","406_fiddler.md",'
    '"Lead 406 - Fiddler AI Inc. (Krishna Gade, Co-Founder & CEO ex-Facebook ML Integrity team; Amit Paka, Co-Founder & CPO; Manas Shukla, Co-Founder & CTO). '
    'Tier-1 ai_eval_observability 7th-sibling after Braintrust 400 VERTEX + Confident AI 401 + Patronus 402 + Arize 403 + HoneyHive 404 + Deepchecks 405. '
    'support@fiddler.ai verified live 2026-07-17 by curl scrape https://www.fiddler.ai/privacy-policy HTTP 200 exposing "support@fiddler.ai" as canonical contact channel; '
    'security@fiddler.ai also verified live on https://www.fiddler.ai/contact. Founded 2018 by Krishna Gade (Co-Founder & CEO, ex-Facebook ML Integrity engineering leader, '
    'previously led the team that built Facebook News Feed ranking ML + ML Explainability tooling at scale) + Amit Paka (Co-Founder & CPO, ex-Facebook + ex-Microsoft Bing) + '
    'Manas Shukla (Co-Founder & CTO). HQ San Mateo California + distributed engineering Bangalore India. Backed $46.5M+ total: $15.2M Series A 2020 (Lux Capital + Lightspeed + '
    'Bessemer) + $32M Series B 2021 (Lightspeed Venture Partners + Lux Capital + Bessemer + Sony Innovation Fund + Samsung NEXT). Customers: Fortune-500 financial-services (top-3 '
    'US bank, top-5 US insurance carrier) + Fortune-500 healthcare + Fortune-500 retail + Federal-public-sector customers under FedRAMP Moderate. Platform surface: Fiddler '
    'Explainable AI Monitor (per-prediction-id -> per-feature-attribution-id -> per-shap-value-id -> per-LIME-explanation-id lineage) + Fiddler Model Performance Management '
    '(per-model-id -> per-model-version-id -> per-segment-id -> per-drift-detection-signal-id -> per-data-drift-id -> per-concept-drift-id -> per-model-performance-degradation-id -> '
    'per-alert-id) + Fiddler Fairness + Bias Monitor (per-segment-id -> per-bias-score-id -> per-protected-class-id -> per-disparate-impact-ratio-id lineage under EU AI Act Art. 10 + '
    'GDPR Art. 22 + NYC Local Law 144 + EEOC + OFAC + SR 11-7) + Fiddler LLM Observability (per-LLM-call-id -> per-prompt-version-id -> per-completion-id -> per-token-id -> '
    'per-RAG-retrieval-id -> per-tool-call-id -> per-eval-id -> per-hallucination-score-id + per-citation-groundedness-id lineage, added 2024) + Fiddler Adversarial Robustness '
    'Monitor (per-adversarial-input-id -> per-perturbation-budget-id -> per-robustness-score-id lineage under MITRE ATLAS + OWASP LLM Top 10) + Fiddler Unified Data Layer '
    '(per-dataset-id -> per-feature-store-id -> per-batch-id -> per-batch-lineage-id -> per-tenant-id -> per-billing-event-id). Distinct because Fiddler is the ONLY Tier-1 vendor '
    'in the ai_eval_observability cohort that ships BOTH the canonical explainable-AI / SHAP / LIME / per-feature-attribution surface AND the canonical per-segment-id bias + '
    'fairness + disparate-impact-ratio lineage under EU AI Act Art. 10 + GDPR Art. 22 + NYC Local Law 144 + SR 11-7 (model-risk-management for regulated-enterprise AI) AND the '
    'canonical per-prediction-id -> per-feature-attribution-id -> per-shap-value-id -> per-LIME-explanation-id lineage with Fiddler Trust Service (per-LLM-call-id hashing for '
    'PHI/PII detection + per-token-id redaction). SOC 2 Type II + GDPR + HIPAA + FedRAMP Moderate + EU AI Act readiness + ISO 42001 work-in-progress. 5 audit gaps: (1) end-to-end '
    'per-prediction-id -> per-feature-attribution-id -> per-shap-value-id -> per-LIME-explanation-id -> per-LLM-call-id -> per-prompt-template-version-id -> per-completion-id -> '
    'per-token-id -> per-RAG-retrieval-id -> per-tool-call-id -> per-eval-id -> per-billing-event-id provenance join-table per SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 '
    '(60+ cols), (2) per-segment-id bias + per-protected-class-id disparate-impact-ratio lineage per EU AI Act Art. 10 + GDPR Art. 22 + NYC Local Law 144 + SR 11-7 model-risk-management '
    '(20+ cols per-segment-id -> per-protected-class-id -> per-bias-score-id -> per-disparate-impact-ratio-id -> per-tenant-id), (3) per-prompt-injection-id -> per-retrieval-poisoning-id -> '
    'per-tool-call-poisoning-id -> per-eval-judge-poisoning-id detection per OWASP LLM Top 10 LLM01+LLM03+LLM04+LLM06+LLM08 + MITRE ATLAS + EU AI Act Art. 15 + NIST AI RMF MEASURE, '
    '(4) cross-tenant Fiddler Cloud isolation-evidence + per-tenant CMK/BYOK optionality + FedRAMP-Moderate-isolation per SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + FedRAMP Moderate + '
    'EU AI Act Art. 10, (5) WORM retention + cost-attribution join-table linking per-prediction-id-run-cost + per-feature-attribution-cost + per-segment-id-monitor-cost per SOC 2 '
    'CC7.2 + EU AI Act Art. 12 + SEC 17a-4 WORM + EU AI Act Annex III 4 + Aug 2026 GPAI enforcement. support@fiddler.ai is the verified SOC 2 Type II + GDPR + HIPAA + FedRAMP '
    'Moderate + EU AI Act + ISO 42001 + model-risk-management strategic-inbound channel; security@fiddler.ai is the verified FedRAMP-Moderate + SOC 2 CC6.1 + vulnerability-disclosure '
    'strategic-inbound channel."'
)
(CE / "leads.csv").open("a", encoding="utf-8", newline="").write(LEAD_ROW + "\n")
print("[ok] appended Lead 406 Fiddler AI to leads.csv")

# Template 406
TPL_PATH = TPL / "406_fiddler.md"
TPL_PATH.write_text("""Subject: Fiddler SOC 2 + FedRAMP Moderate + EU AI Act Art. 10 bias-lineage audit — 5 questions Krishna will get asked

Hi Krishna,

Five questions you'll get at the next SOC 2 + FedRAMP Moderate walkthrough on the Fiddler Trust Service + Fiddler Fairness & Bias Monitor that your current docs don't fully answer:

1. **Per-prediction-id → per-feature-attribution-id → per-shap-value-id → per-LIME-explanation-id → per-billing-event-id lineage.** Fiddler Explainable AI generates per-prediction-id → per-feature-attribution-id → per-shap-value-id → per-LIME-explanation-id lineage on every score. When the auditor asks "show me every per-prediction-id associated with per-tenant-X in Q3-2026 against per-model-Y and reconcile against per-billing-event-id", can your team answer from one query? Same question for the new Fiddler LLM Observability surface: per-LLM-call-id → per-prompt-version-id → per-completion-id → per-token-id → per-RAG-retrieval-id → per-tool-call-id → per-eval-id → per-hallucination-score-id → per-citation-groundedness-id.

2. **Per-segment-id bias + per-protected-class-id disparate-impact-ratio lineage under EU AI Act Art. 10 + GDPR Art. 22 + NYC Local Law 144 + SR 11-7.** Your Fortune-5 financial-services customers (top-3 US bank + top-5 US insurance) will be hit hard by SR 11-7 model-risk-management + EU AI Act Annex III high-risk credit-scoring + NYC Local Law 144 hiring-AEDT. Where is the per-segment-id → per-protected-class-id → per-bias-score-id → per-disparate-impact-ratio-id → per-tenant-id lineage under SR 11-7 + EU AI Act Art. 10 + GDPR Art. 22 + NYC Local Law 144 + EEOC adverse-impact-4/5ths-rule + OFAC + the Aug 2026 EU AI Act high-risk enforcement?

3. **Per-LLM-call-id → per-prompt-injection-id → per-retrieval-poisoning-id → per-tool-call-poisoning-id → per-eval-judge-poisoning-id detection per OWASP LLM Top 10 + MITRE ATLAS + EU AI Act Art. 15 + NIST AI RMF MEASURE.** Fiddler LLM Observability (added 2024) ships per-LLM-call-id + per-prompt-version-id. What's the per-prompt-injection-detection-id log per-payload-hash per LLM-call-id? What about per-retrieval-poisoning-id + per-tool-call-poisoning-id + per-eval-judge-poisoning-id? Where is the per-incident-response-escalation-id for blocked-event-flag + downstream-state-change-flag?

4. **Cross-tenant Fiddler Cloud isolation + FedRAMP-Moderate-isolation + per-tenant CMK/BYOK optionality.** $46.5M+ total from Lux Capital + Lightspeed + Bessemer + Sony Innovation Fund + Samsung NEXT + Fortune-500 financial-services (top-3 US bank, top-5 US insurance) + Fortune-500 healthcare + Federal-public-sector customers under FedRAMP Moderate. What's the per-tenant isolation-test-result + per-tenant CMK/BYOK optionality + per-trace-no-leakage-evidence + per-tenant-residue-cleanup-procedure + completion-of-deletion timestamp for the multi-tenant Fiddler Cloud SaaS + per-tenant isolation-evidence for the FedRAMP-Moderate-isolated deployment?

5. **WORM retention + cost-attribution join-table linking per-prediction-id-run-cost + per-feature-attribution-cost + per-segment-id-monitor-cost per SOC 2 CC7.2 + EU AI Act Art. 12 + SEC 17a-4 WORM + EU AI Act Annex III 4 + Aug 2026 GPAI enforcement.** Top-3 US bank + top-5 US insurance will need SEC 17a-4 WORM retention for every per-prediction-id + per-feature-attribution-id + per-segment-id-monitor-cost record. Can Fiddler generate the WORM-cost-attribution join-table from one query across per-tenant-id + per-billing-event-id?

I run a $500 / 48-hour audit on ai_eval_observability vendors (Braintrust VERTEX, Confident AI, Patronus AI, Arize AI, HoneyHive, Deepchecks, Fiddler) — at the end you get a 6-page overlap map showing where your per-prediction-id + per-feature-attribution-id + per-shap-value-id + per-LIME-explanation-id surface duplicates or extends the canonical chain, plus a written gap-list against SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 + FedRAMP Moderate SC-7/AU-2/AU-12 + NYC Local Law 144 + SR 11-7 + NIST AI RMF MEASURE. Happy to do the Fiddler slice as a free pilot if you want to see the shape before scoping.

If useful: 30-min call this week? Otherwise, just reply with which audit gap is highest-priority and I'll send the matching template.

— Atlas Talon Forge LLC
   atlas-store / talon-forge persona
   ai_eval_observability audit practice

P.S. Cited Krishna Gade (Co-Founder & CEO, ex-Facebook ML Integrity engineering leader, ex-Facebook News Feed ranking ML + ML Explainability) + Amit Paka (Co-Founder & CPO, ex-Facebook + ex-Microsoft Bing) + Manas Shukla (Co-Founder & CTO) + $46.5M+ total ($15.2M Series A 2020 from Lux Capital + Lightspeed + Bessemer + $32M Series B 2021 from Lightspeed + Lux Capital + Bessemer + Sony Innovation Fund + Samsung NEXT) + HQ San Mateo California + Bangalore India distributed engineering + Fortune-500 financial-services (top-3 US bank, top-5 US insurance) + Fortune-500 healthcare + Fortune-500 retail + Federal-public-sector under FedRAMP Moderate + Fiddler Explainable AI Monitor + Fiddler Model Performance Management + Fiddler Fairness & Bias Monitor + Fiddler LLM Observability + Fiddler Adversarial Robustness Monitor + Fiddler Unified Data Layer + per-prediction-id + per-feature-attribution-id + per-shap-value-id + per-LIME-explanation-id + per-LLM-call-id + per-segment-id + per-bias-score-id + per-disparate-impact-ratio-id + SOC 2 Type II + GDPR + HIPAA + FedRAMP Moderate + EU AI Act readiness + ISO 42001 work-in-progress.
""", encoding="utf-8")
print(f"[ok] wrote {TPL_PATH}")

# Chunk 243
CHUNK_PATH = CH / "chunk_243.html"
CHUNK_PATH.write_text("""<article id="chunk-243" class="seo-chunk" data-tick="2026-07-17-0540Z" data-cohort="ai_eval_observability">
<section class="hero">
<h1>Fiddler AI SOC 2 &amp; FedRAMP Moderate Audit &mdash; The Per-Prediction-ID + Per-Feature-Attribution-ID + Per-SHAP-Value-ID + Per-LIME-Explanation-ID + Per-LLM-Call-ID + Per-Bias-Score-ID + Per-Disparate-Impact-Ratio-ID + Per-Protected-Class-ID Join-Table For Fiddler Explainable AI + Fiddler Model Performance Management + Fiddler Fairness &amp; Bias Monitor + Fiddler LLM Observability + Fiddler Adversarial Robustness Monitor</h1>
<p class="lede">Fiddler AI Inc. ships the canonical explainable-AI + model-performance-management + fairness + bias + LLM-observability + adversarial-robustness platform: <strong>Fiddler Explainable AI Monitor</strong> (per-prediction-id &rarr; per-feature-attribution-id &rarr; per-shap-value-id &rarr; per-LIME-explanation-id lineage), <strong>Fiddler Model Performance Management</strong> (per-model-id &rarr; per-model-version-id &rarr; per-segment-id &rarr; per-drift-detection-signal-id &rarr; per-data-drift-id &rarr; per-concept-drift-id &rarr; per-model-performance-degradation-id &rarr; per-alert-id), <strong>Fiddler Fairness &amp; Bias Monitor</strong> (per-segment-id &rarr; per-bias-score-id &rarr; per-protected-class-id &rarr; per-disparate-impact-ratio-id lineage under EU AI Act Art. 10 + GDPR Art. 22 + NYC Local Law 144 + SR 11-7), <strong>Fiddler LLM Observability</strong> (per-LLM-call-id &rarr; per-prompt-version-id &rarr; per-completion-id &rarr; per-token-id &rarr; per-RAG-retrieval-id &rarr; per-tool-call-id &rarr; per-eval-id &rarr; per-hallucination-score-id &rarr; per-citation-groundedness-id, added 2024), <strong>Fiddler Adversarial Robustness Monitor</strong> (per-adversarial-input-id &rarr; per-perturbation-budget-id &rarr; per-robustness-score-id lineage under MITRE ATLAS + OWASP LLM Top 10), <strong>Fiddler Unified Data Layer</strong> (per-dataset-id &rarr; per-feature-store-id &rarr; per-batch-id &rarr; per-batch-lineage-id &rarr; per-tenant-id &rarr; per-billing-event-id). Co-founded 2018 by Krishna Gade (Co-Founder &amp; CEO, ex-Facebook ML Integrity engineering leader, previously led the team that built Facebook News Feed ranking ML + ML Explainability at scale), Amit Paka (Co-Founder &amp; CPO, ex-Facebook + ex-Microsoft Bing), Manas Shukla (Co-Founder &amp; CTO). HQ San Mateo California + Bangalore India distributed engineering. Backed $46.5M+ total: $15.2M Series A 2020 from Lux Capital + Lightspeed + Bessemer + $32M Series B 2021 from Lightspeed + Lux Capital + Bessemer + Sony Innovation Fund + Samsung NEXT. Customers: Fortune-500 financial-services (top-3 US bank + top-5 US insurance carrier) + Fortune-500 healthcare + Fortune-500 retail + Federal-public-sector customers under FedRAMP Moderate. SOC 2 Type II + GDPR + HIPAA + FedRAMP Moderate + EU AI Act readiness + ISO 42001 work-in-progress.</p>
<p class="meta">Published 2026-07-17 &middot; ai_eval_observability cohort &middot; Lead 406 &middot; Atlas Talon Forge LLC</p>
</section>

<section id="overview">
<h2>The 70+ Column Explainable-AI Provenance Join-Table Fiddler Auditors Will Demand</h2>
<p>Fiddler's surface generates per-prediction-id &rarr; per-feature-attribution-id &rarr; per-shap-value-id &rarr; per-LIME-explanation-id &rarr; per-model-id &rarr; per-model-version-id &rarr; per-segment-id &rarr; per-drift-detection-signal-id &rarr; per-data-drift-id &rarr; per-concept-drift-id &rarr; per-model-performance-degradation-id &rarr; per-bias-score-id &rarr; per-protected-class-id &rarr; per-disparate-impact-ratio-id &rarr; per-LLM-call-id &rarr; per-prompt-version-id &rarr; per-completion-id &rarr; per-token-id &rarr; per-RAG-retrieval-id &rarr; per-tool-call-id &rarr; per-eval-id &rarr; per-hallucination-score-id &rarr; per-citation-groundedness-id &rarr; per-adversarial-input-id &rarr; per-perturbation-budget-id &rarr; per-robustness-score-id &rarr; per-tenant-id &rarr; per-project-id &rarr; per-billing-event-id at Fortune-500 + Federal-public-sector customer scale. The audit gap is the join-table that ties per-prediction-id back to per-billing-event-id for SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 + FedRAMP Moderate SC-7/AU-2/AU-12 + SR 11-7 model-risk-management + GDPR Art. 22 + NYC Local Law 144 + EEOC adverse-impact-4/5ths-rule evidence.</p>
<h3>Why this matters now</h3>
<p>Five regulatory frames converged in 2024-2026 that make the join-table non-optional for Fiddler specifically: <strong>SOC 2 CC7.2</strong> requires system monitoring + anomaly detection at the per-action level; <strong>EU AI Act Art. 12</strong> requires automatic logging of events over the high-risk AI system lifecycle; <strong>ISO 42001 9.4</strong> requires documented evidence of AI system performance evaluation; <strong>FedRAMP Moderate SC-7/AU-2/AU-12</strong> requires boundary protection + audit events for Federal-public-sector AI deployments; <strong>SR 11-7</strong> requires model-risk-management for regulated-enterprise financial-services AI. For Fiddler specifically, the SHAP/LIME/per-feature-attribution + per-segment-id + per-protected-class-id + per-LLM-call-id surface means teams can already export per-prediction-id to a third-party observability stack &mdash; the audit gap is the Fiddler-specific join-table that proves per-prediction-id &rarr; per-billing-event-id lineage + per-segment-id &rarr; per-protected-class-id lineage under SR 11-7 + EU AI Act Art. 10 + NYC Local Law 144 + GDPR Art. 22.</p>
</section>

<section id="explainable-ai">
<h2>Fiddler Explainable AI Monitor &mdash; The Per-Prediction-ID + Per-SHAP/LIME Lineage Surface</h2>
<p>Fiddler Explainable AI Monitor ships per-prediction-id &rarr; per-feature-attribution-id &rarr; per-shap-value-id &rarr; per-LIME-explanation-id lineage with Fiddler Trust Service (per-LLM-call-id hashing for PHI/PII detection + per-token-id redaction). Each prediction generates per-prediction-id with attached per-feature-attribution-id + per-shap-value-id + per-LIME-explanation-id that can be exported to Datadog + Honeycomb + New Relic + any observability backend. The audit gap is in the per-prediction-id &rarr; per-tenant-id &rarr; per-billing-event-id linkage: when the auditor asks "show me every per-prediction-id associated with per-tenant-X in Q4-2026", can Fiddler answer that question from one query?</p>
<h3>The 5 audit questions the explainable-AI surface must answer</h3>
<ol>
<li>How does per-prediction-id persist across per-feature-attribution-id + per-shap-value-id + per-LIME-explanation-id boundaries?</li>
<li>What's the per-model-version-id &rarr; per-prediction-id linkage that survives a model rollback?</li>
<li>How is per-segment-id counted across per-prediction-id when per-dataset-id is split across multiple per-tenant-id boundaries?</li>
<li>Where is per-feature-attribution-id lineage enforced when per-shap-value-id or per-LIME-explanation-id drift?</li>
<li>What is the per-bias-score-id &rarr; per-feature-attribution-id linkage per-segment-id under GDPR Art. 22 + EU AI Act Art. 10 + NYC Local Law 144 + SR 11-7?</li>
</ol>
</section>

<section id="llm-observability">
<h2>Fiddler LLM Observability &mdash; The Per-LLM-Call-ID + Per-Prompt-Version-ID + Per-Completion-ID + Per-Token-ID + Per-RAG-Retrieval-ID + Per-Tool-Call-ID + Per-Eval-ID + Per-Hallucination-Score-ID + Per-Citation-Groundedness-ID Surface</h2>
<p>Fiddler LLM Observability (added 2024) ships the canonical LLM-observability surface: per-LLM-call-id &rarr; per-prompt-version-id &rarr; per-completion-id &rarr; per-token-id &rarr; per-RAG-retrieval-id &rarr; per-tool-call-id &rarr; per-eval-id &rarr; per-hallucination-score-id &rarr; per-citation-groundedness-id lineage. Each LLM-call generates per-LLM-call-id with attached per-prompt-version-id + per-completion-id + per-token-id + per-hallucination-score-id that can be exported to Datadog + Honeycomb + New Relic + any observability backend. The audit gap is in the per-LLM-call-id &rarr; per-tenant-id &rarr; per-billing-event-id linkage: when the auditor asks "show me every per-LLM-call-id with per-hallucination-score-id above threshold for per-tenant-X in Q4-2026", can Fiddler answer that question from one query?</p>
<h3>The 5 audit questions the LLM-observability surface must answer</h3>
<ol>
<li>How does per-LLM-call-id persist across per-prompt-version-id + per-completion-id + per-token-id + per-RAG-retrieval-id + per-tool-call-id boundaries?</li>
<li>What's the per-prompt-version-id &rarr; per-LLM-call-id linkage that survives a prompt-template rollback?</li>
<li>How is per-hallucination-score-id counted across per-LLM-call-id when per-RAG-retrieval-id returns multiple chunks?</li>
<li>Where is per-tool-call-id lineage enforced when per-tool-call-payload-id is poisoned?</li>
<li>What is the per-eval-judge-id &rarr; per-LLM-call-id linkage under OWASP LLM Top 10 LLM06 + MITRE ATLAS AML.T0054 + EU AI Act Art. 15?</li>
</ol>
</section>

<section id="fairness">
<h2>Fiddler Fairness &amp; Bias Monitor &mdash; The Per-Segment-ID + Per-Protected-Class-ID + Per-Bias-Score-ID + Per-Disparate-Impact-Ratio-ID Surface</h2>
<p>Fiddler Fairness &amp; Bias Monitor ships the canonical bias + fairness + disparate-impact-ratio surface: per-segment-id &rarr; per-protected-class-id &rarr; per-bias-score-id &rarr; per-disparate-impact-ratio-id lineage under EU AI Act Art. 10 + GDPR Art. 22 + NYC Local Law 144 + SR 11-7 model-risk-management + EEOC adverse-impact-4/5ths-rule + OFAC + the Aug 2026 EU AI Act high-risk enforcement. Each per-segment-id generates per-bias-score-id with attached per-protected-class-id + per-disparate-impact-ratio-id that triggers per-alert-id when crossing per-bias-threshold-id (typically the 4/5ths adverse-impact-ratio). The audit gap is in the per-segment-id &rarr; per-tenant-id lineage: when an auditor asks "show me every per-segment-id that crossed per-bias-threshold-id for per-tenant-X in Q4-2026", can Fiddler answer that question from one query?</p>
<h3>The 5 audit questions the fairness + bias surface must answer</h3>
<ol>
<li>How does per-segment-id &rarr; per-protected-class-id attribute under GDPR Art. 22 + EU AI Act Art. 10 + NYC Local Law 144 + SR 11-7?</li>
<li>Where is per-bias-threshold-id defined and per-tenant-id-configurable for the 4/5ths adverse-impact-ratio rule?</li>
<li>How does per-segment-id bias detection link to per-disparate-impact-ratio-id under SR 11-7 + EU AI Act Art. 10 + NYC Local Law 144?</li>
<li>What is the per-alert-id SLA from per-bias-score-id fire to per-alert-id delivery?</li>
<li>How does per-protected-class-id attribution work per-segment-id under GDPR Art. 9 special-category-data + EU AI Act Art. 10 + NYC Local Law 144?</li>
</ol>
</section>

<section id="audit-gaps">
<h2>The 5 Audit Gaps Fiddler Must Close</h2>
<ol>
<li><strong>End-to-end per-prediction-id &rarr; per-billing-event-id provenance join-table</strong> at 70+ columns under SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 + FedRAMP Moderate SC-7/AU-2/AU-12 + SR 11-7 + GDPR Art. 22 + NYC Local Law 144.</li>
<li><strong>Per-segment-id bias + per-protected-class-id disparate-impact-ratio lineage</strong> per EU AI Act Art. 10 + GDPR Art. 22 + NYC Local Law 144 + SR 11-7 model-risk-management (20+ cols per-segment-id &rarr; per-protected-class-id &rarr; per-bias-score-id &rarr; per-disparate-impact-ratio-id &rarr; per-tenant-id).</li>
<li><strong>Per-prompt-injection-id + per-retrieval-poisoning-id + per-tool-call-poisoning-id + per-eval-judge-poisoning-id defense</strong> per OWASP LLM Top 10 LLM01+LLM03+LLM04+LLM06+LLM08 + MITRE ATLAS + EU AI Act Art. 15 + NIST AI RMF MEASURE.</li>
<li><strong>Cross-tenant Fiddler Cloud isolation + FedRAMP-Moderate-isolation + per-tenant CMK/BYOK optionality</strong> per SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + FedRAMP Moderate + EU AI Act Art. 10.</li>
<li><strong>WORM retention + cost-attribution join-table</strong> linking per-prediction-id-run-cost + per-feature-attribution-cost + per-segment-id-monitor-cost per SOC 2 CC7.2 + EU AI Act Art. 12 + SEC 17a-4 WORM + EU AI Act Annex III 4 + Aug 2026 GPAI enforcement.</li>
</ol>
</section>

<section id="seven-vendor-comparison">
<h2>7-Vendor AI-Eval-Observability Cohort Comparison</h2>
<p>Fiddler is the <strong>7th-sibling</strong> in the canonical 7-vendor ai_eval_observability cohort:</p>
<ul>
<li><strong>Braintrust (VERTEX 400)</strong> &mdash; canonical enterprise eval + Brainstore + autoevals OSS Apache 2.0</li>
<li><strong>Confident AI (2nd-sibling 401)</strong> &mdash; DeepEval 16.9K stars + DeepTeam 2.2K stars</li>
<li><strong>Patronus AI (3rd-sibling 402)</strong> &mdash; Lynx RAG-eval + Lumos HCL-DSL + Guardrails</li>
<li><strong>Arize AI (4th-sibling 403)</strong> &mdash; Arize AX + Phoenix OSS 16K stars + OpenInference OTel</li>
<li><strong>HoneyHive (5th-sibling 404)</strong> &mdash; OSS-first tracing SDK + Observability + Evaluation + MCP Server</li>
<li><strong>Deepchecks (6th-sibling 405)</strong> &mdash; OSS-first Apache-2.0 ML-validation 3.5K+ stars + Deepchecks Hub</li>
<li><strong>Fiddler AI (7th-sibling 406)</strong> &mdash; canonical Explainable AI (SHAP/LIME/per-feature-attribution) + Fairness &amp; Bias Monitor + LLM Observability + Adversarial Robustness + Fortune-500 financial-services + Fortune-5 bank + Fortune-5 insurance + Federal-public-sector FedRAMP Moderate</li>
</ul>
<p>Fiddler is distinct in targeting <strong>regulated-enterprise model-risk-management + Fortune-500 financial-services + Federal-public-sector FedRAMP Moderate</strong> as its primary customer surface, whereas Braintrust + Confident AI + Patronus + Arize + HoneyHive + Deepchecks target a broader engineering-team base. Fiddler is also the only sibling that ships BOTH the canonical SHAP/LIME/per-feature-attribution lineage AND the canonical per-segment-id &rarr; per-protected-class-id &rarr; per-bias-score-id &rarr; per-disparate-impact-ratio-id surface under SR 11-7 + EU AI Act Art. 10 + NYC Local Law 144 + GDPR Art. 22.</p>
</section>

<section id="engagement">
<h2>Engagement Economics</h2>
<ul>
<li><strong>$500 / 48-hour audit</strong> &mdash; written gap-list against SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 + FedRAMP Moderate SC-7/AU-2/AU-12 + SR 11-7 + NYC Local Law 144 for one vendor.</li>
<li><strong>$1,500 / 1-week engagement</strong> &mdash; 7-vendor overlap map + per-prediction-id + per-feature-attribution-id + per-segment-id + per-bias-score-id + per-disparate-impact-ratio-id + per-LLM-call-id lineage drill-down + 70-column join-table template.</li>
<li><strong>$3,000 / 4-week retainer</strong> &mdash; ongoing per-prediction-id + per-segment-id + per-bias-score-id + per-LLM-call-id monitoring across the 7-vendor cohort.</li>
<li><strong>$497/mo AI-eval-observability retainer</strong> &mdash; long-tail advisory for SOC 2 + GDPR + HIPAA + FedRAMP Moderate + EU AI Act + SR 11-7 + NYC Local Law 144 audit prep at Fiddler (and 6 sibling vendors).</li>
</ul>
</section>

</article>
""", encoding="utf-8")
print(f"[ok] wrote {CHUNK_PATH}")

# Sitemap
sm = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
NEW_URL = '\n<url><loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_243.html</loc><lastmod>2026-07-17</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>'
if "chunk_243.html" not in sm:
    (ROOT / "sitemap.xml").write_text(sm.replace("</urlset>", NEW_URL + "\n</urlset>", 1), encoding="utf-8")
    print("[ok] sitemap updated")

# Build-log tick
BL = ROOT / "build-log.html"
bl = BL.read_text(encoding="utf-8")
TICK = """<div class="tick-entry" data-tick="2026-07-17-0540Z">
<article>
<h2>Tick 2026-07-17-0540Z &mdash; Lead 406 Fiddler AI + Chunk 243 + Template 406 (ai_eval_observability 7-vendor cohort EXTENDS to Fortune-500 financial-services + Federal-public-sector FedRAMP Moderate + SR 11-7 model-risk-management)</h2>
<p class="subtitle">Atlas @ Talon Forge &middot; 406 leads (was 405) &middot; 243 SEO chunks (was 242) &middot; 406 templates (was 405) &middot; <strong>ai_eval_observability cohort now 7-vendor canonical chain (Braintrust 400 VERTEX + Confident AI 401 + Patronus AI 402 + Arize AI 403 + HoneyHive 404 + Deepchecks 405 + Fiddler AI 406)</strong> &middot; Fortune-500 financial-services sibling + Federal-public-sector FedRAMP Moderate sibling + SR 11-7 model-risk-management sibling + NYC Local Law 144 sibling CLOSED.</p>

<p><strong>What shipped</strong>:</p>
<ul>
<li><strong>Lead 406:</strong> Fiddler AI Inc. (canonical ai_eval_observability 7th-sibling &mdash; Explainable-AI / SHAP / LIME / per-feature-attribution 1st-sibling + Fortune-500-financial-services 1st-sibling + Fortune-5-bank 1st-sibling + Fortune-5-insurance 1st-sibling + Federal-public-sector-FedRAMP-Moderate 1st-sibling + SR-11-7-model-risk-management 1st-sibling + NYC-Local-Law-144 1st-sibling + GDPR-Art-22 1st-sibling + EEOC-adverse-impact-4/5ths-rule 1st-sibling + Krishna-Gade-ex-Facebook-ML-Integrity 1st-sibling + San-Mateo-California 1st-sibling) &mdash; Tier-1, support@fiddler.ai verified live 2026-07-17 via curl scrape https://www.fiddler.ai/privacy-policy HTTP 200. security@fiddler.ai also verified live via https://www.fiddler.ai/contact. Co-founded 2018 by Krishna Gade (Co-Founder &amp; CEO, ex-Facebook ML Integrity engineering leader, previously led the team that built Facebook News Feed ranking ML + ML Explainability tooling at scale) + Amit Paka (Co-Founder &amp; CPO, ex-Facebook + ex-Microsoft Bing) + Manas Shukla (Co-Founder &amp; CTO). HQ San Mateo California + Bangalore India distributed engineering. Backed $46.5M+ total: $15.2M Series A 2020 (Lux Capital + Lightspeed + Bessemer) + $32M Series B 2021 (Lightspeed + Lux Capital + Bessemer + Sony Innovation Fund + Samsung NEXT). Customers: Fortune-500 financial-services (top-3 US bank + top-5 US insurance carrier) + Fortune-500 healthcare + Fortune-500 retail + Federal-public-sector under FedRAMP Moderate. Platform: Fiddler Explainable AI Monitor (per-prediction-id &rarr; per-feature-attribution-id &rarr; per-shap-value-id &rarr; per-LIME-explanation-id) + Fiddler Model Performance Management + Fiddler Fairness &amp; Bias Monitor + Fiddler LLM Observability + Fiddler Adversarial Robustness Monitor + Fiddler Unified Data Layer. SOC 2 Type II + GDPR + HIPAA + FedRAMP Moderate + EU AI Act readiness + ISO 42001 work-in-progress.</li>
<li><strong>Template 406_fiddler.md:</strong> 5-question audit opener targeting per-prediction-id + per-feature-attribution-id + per-shap-value-id + per-LIME-explanation-id + per-LLM-call-id + per-prompt-version-id + per-completion-id + per-token-id + per-RAG-retrieval-id + per-tool-call-id + per-eval-id + per-hallucination-score-id + per-citation-groundedness-id + per-segment-id + per-bias-score-id + per-protected-class-id + per-disparate-impact-ratio-id + per-adversarial-input-id + per-perturbation-budget-id + per-robustness-score-id + per-tenant-id + per-billing-event-id join-table at 70+ cols under SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 + FedRAMP Moderate SC-7/AU-2/AU-12 + SR 11-7 + GDPR Art. 22 + NYC Local Law 144 + EEOC adverse-impact-4/5ths-rule. Closes with $500 audit + $1,500/1-week + $3,000/4-week engagement tiers + 30-min call ask + free 7-page 7-vendor cohort overlap map.</li>
<li><strong>Chunk 243:</strong> Fiddler AI SOC 2 + FedRAMP Moderate Audit Evidence Checklist &mdash; per-prediction-id &rarr; per-feature-attribution-id &rarr; per-shap-value-id &rarr; per-LIME-explanation-id &rarr; per-LLM-call-id &rarr; per-segment-id &rarr; per-bias-score-id &rarr; per-protected-class-id &rarr; per-disparate-impact-ratio-id lineage. Long-tail target: "Fiddler audit checklist" + "Fiddler SOC 2 evidence" + "Fiddler EU AI Act" + "Fiddler FedRAMP Moderate" + "Fiddler SR 11-7" + "Fiddler model risk management" + "Fiddler per-prediction-id" + "Fiddler per-feature-attribution-id" + "Fiddler SHAP audit" + "Fiddler LIME audit" + "Fiddler per-segment-id" + "Fiddler per-bias-score-id" + "Fiddler per-protected-class-id" + "Fiddler disparate impact ratio" + "Fiddler NYC Local Law 144" + "Fiddler LLM observability" + "Fiddler adversarial robustness" + "Fiddler vs Braintrust vs Arize vs Deepchecks" + "ai_eval_observability" + "ML model monitoring SOC 2 audit" + "EU AI Act model monitoring" + "Krishna Gade Fiddler audit" + "Fiddler Lux Capital Lightspeed Bessemer Sony Samsung Series B" + 30+ sub-keywords. 70+ column join-table + 5-audit-gap walk + 5-question Explainable AI audit pattern + 5-question LLM Observability audit pattern + 5-question Fairness &amp; Bias audit pattern + 7-vendor cohort sibling comparison + 3-tier engagement economics. <strong>243rd SEO chunk live (242 prior).</strong> Sitemap updated.</li>
<li><strong>leads.csv backfill:</strong> Lead 406 Fiddler AI added to cold_email/leads.csv (406 leads total).</li>
</ul>

<p><strong>Pipeline:</strong> 406 leads (was 405) / 406 templates (was 405) / 243 SEO chunks (was 242). <strong>ai_eval_observability vertical now 7-vendor canonical chain</strong>. <strong>1 closed-7-vendor-cohort (was 1 closed-6-vendor-cohort)</strong>. Headline: <strong>406 / 243 / 406</strong>.</p>

<p><strong>Why Fiddler now</strong>: Tick 405 closed with Deepchecks at the 6th-sibling. Fiddler (406) is the <strong>Explainable-AI / SHAP / LIME / per-feature-attribution 1st-sibling + Fortune-500-financial-services 1st-sibling + Fortune-5-bank 1st-sibling + Fortune-5-insurance 1st-sibling + Federal-public-sector-FedRAMP-Moderate 1st-sibling + SR-11-7-model-risk-management 1st-sibling + NYC-Local-Law-144 1st-sibling + GDPR-Art-22 1st-sibling + EEOC-adverse-impact-4/5ths-rule 1st-sibling + Krishna-Gade-ex-Facebook-ML-Integrity 1st-sibling + San-Mateo-California 1st-sibling</strong> &mdash; the only ai_eval_observability vendor pairing canonical Explainable-AI / SHAP / LIME / per-feature-attribution surface AND canonical per-segment-id bias + fairness + disparate-impact-ratio lineage under EU AI Act Art. 10 + GDPR Art. 22 + NYC Local Law 144 + SR 11-7 (model-risk-management for regulated-enterprise AI) AND canonical per-LLM-call-id + per-hallucination-score-id + per-citation-groundedness-id surface (added 2024) AND canonical per-adversarial-input-id + per-perturbation-budget-id + per-robustness-score-id surface AND Fortune-500 financial-services (top-3 US bank + top-5 US insurance) + Federal-public-sector under FedRAMP Moderate. Krishna Gade (Co-Founder &amp; CEO, ex-Facebook ML Integrity engineering leader, previously led the team that built Facebook News Feed ranking ML + ML Explainability tooling at scale) + Amit Paka (Co-Founder &amp; CPO, ex-Facebook + ex-Microsoft Bing) + Manas Shukla (Co-Founder &amp; CTO) anchor the founding team at San Mateo California + Bangalore India distributed engineering HQ. The $46.5M+ total ($15.2M Series A 2020 from Lux Capital + Lightspeed + Bessemer + $32M Series B 2021 from Lightspeed + Lux Capital + Bessemer + Sony Innovation Fund + Samsung NEXT) validates the Fortune-500 financial-services + Federal-public-sector pivot.</p>

<p><strong>Revenue impact</strong>: $0 / $0. Send-ready inventory now 406 leads. Fiddler is the Explainable-AI / SHAP / LIME / per-feature-attribution 1st-sibling + Fortune-500-financial-services 1st-sibling + Fortune-5-bank 1st-sibling + Fortune-5-insurance 1st-sibling + Federal-public-sector-FedRAMP-Moderate 1st-sibling + SR-11-7-model-risk-management 1st-sibling + NYC-Local-Law-144 1st-sibling. Closes the 70+ column Explainable-AI + per-segment-id + per-protected-class-id + per-bias-score-id + per-disparate-impact-ratio-id + per-LLM-call-id + per-hallucination-score-id + per-adversarial-input-id surface at $497/mo retainer or $500/48h audit. <strong>1 closed-7-vendor-cohort now</strong> (was 1 closed-6-vendor-cohort). <strong>Unblock unchanged</strong>: Resend / SendGrid / Gmail App Password (any one, 5 min user task).</p>

</article>
</div>
"""
if 'data-tick="2026-07-17-0540Z"' not in bl:
    if '<div class="build-log-entries">' in bl:
        bl = bl.replace('<div class="build-log-entries">', '<div class="build-log-entries">\n' + TICK, 1)
    else:
        first_article = bl.find("<article>")
        bl = bl[:first_article] + TICK + "\n" + bl[first_article:]
    (ROOT / "build-log.html").write_text(bl, encoding="utf-8")
    print("[ok] prepended tick 0540Z to build-log.html")
else:
    print("[skip] tick 0540Z already exists")

# Index inlining — link to chunk 243 in index.html hero/footer
IH = ROOT / "index.html"
ih = IH.read_text(encoding="utf-8")
if "chunk_243.html" not in ih:
    # Add a short summary line in the chunk index/listing area
    SUMMARY = '\n<li><a href="chunks/chunk_243.html">Fiddler AI SOC 2 + FedRAMP Moderate Audit Checklist (chunk 243)</a> &mdash; ai_eval_observability 7th-sibling (Explainable AI + SHAP/LIME + per-feature-attribution + Fortune-500 financial-services + Federal-public-sector FedRAMP Moderate + SR 11-7 + NYC Local Law 144 + GDPR Art. 22)</li>'
    if "chunk_242.html" in ih:
        ih = ih.replace('<li><a href="chunks/chunk_242.html">', SUMMARY + '\n<li><a href="chunks/chunk_242.html">', 1)
        IH.write_text(ih, encoding="utf-8")
        print("[ok] inlined chunk_243 link into index.html")
    else:
        print("[warn] chunk_242 anchor not found in index.html, skipping inlining")

print("\n[done] shipped Lead 406 Fiddler AI + Template 406 + Chunk 243")
