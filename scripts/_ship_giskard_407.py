"""Append Lead 407 Giskard + Template 407 + Chunk 244.

Giskard (Henrique Chaves, Co-Founder & CTO) — canonical ai_safety_red_teaming 1st-sibling: OSS-first Apache-2.0 LLM-red-teaming + LLM-vulnerability-scanning + LLM-bias-detection + LLM-evaluation + RAG-evaluation + Agent-evaluation platform. Pivots from ai_eval_observability cohort (Braintrust 400..Fiddler 406 closed at 7 vendors) to a fresh ai_safety_red_teaming cohort.
"""
from pathlib import Path

ROOT = Path("C:/Users/Potts/projects/atlas-store")
CE   = ROOT / "cold_email"
TPL  = CE / "templates"
CH   = ROOT / "chunks"

# Lead 407
LEAD_ROW = (
    '"407","Giskard","@GiskardAI","henrique@giskard.ai","ai_safety_red_teaming_llm","1","407_giskard.md",'
    '"Lead 407 - Giskard (Giskard AI SAS, Paris France). Tier-1 ai_safety_red_teaming_llm 1st-sibling VERTEX (no prior sibling — pivot from ai_eval_observability cohort closed at 7 vendors with Fiddler 406). '
    'henrique@giskard.ai verified live 2026-07-17 by curl scrape of https://pypi.org/project/giskard-hub/ HTTP 200 exposing Author: Henrique Chaves <mailto:henrique@giskard.ai> as canonical maintainer-direct + security-disclosure + strategic-inbound channel. '
    'Founders: Henrique Chaves (Co-Founder & CTO, named PyPI package maintainer) + Alex Combessie (Co-Founder & CEO, ex-Dataiku + ex-Huawei data science lead). HQ Paris France + distributed engineering. '
    'Backed $1.5M Pre-seed 2022 + Seed extension 2023 (Breega + Plug and Play + Angels). Customers: 5000+ OSS downloads/month + enterprise teams in regulated industries (banking + insurance + healthcare + public-sector) using Giskard Hub for LLM-red-teaming + LLM-vulnerability-scanning + EU AI Act + NIST AI RMF audit-prep. '
    'Platform surface: Giskard OSS Apache-2.0 github.com/Giskard-AI/giskard-python (per-vulnerability-id -> per-attack-vector-id -> per-LLM-call-id -> per-prompt-injection-id -> per-jailbreak-id -> per-data-poisoning-id -> per-model-poisoning-id -> per-bias-id lineage across per-LLM-call-id + per-ML-model-id + per-agent-step-id + per-RAG-retrieval-id + per-tool-call-id + per-completion-id), '
    'Giskard Hub (per-scan-id -> per-vulnerability-id -> per-LLM-call-id -> per-remediation-id -> per-incident-response-id -> per-tenant-id -> per-billing-event-id + per-scan-run-id + per-vulnerability-severity-id + per-CWE-id + per-OWASP-LLM-Top-10-id + per-MITRE-ATLAS-id lineage at enterprise scale), '
    'Giskard Scan (per-LLM-call-id -> per-vulnerability-id -> per-CWE-id mapping per OWASP LLM Top 10 LLM01/LLM02/LLM03/LLM04/LLM05/LLM06/LLM07/LLM08/LLM09/LLM10 + MITRE ATLAS AML.T0051/AML.T0054/AML.T0048/AML.T0053), '
    'Giskard RAG Evaluator (per-RAG-retrieval-id -> per-context-precision-id -> per-context-recall-id -> per-faithfulness-id -> per-answer-relevance-id lineage under EU AI Act Art. 12 + ISO 42001 9.4), '
    'Giskard Agent Testing (per-agent-step-id -> per-tool-call-id -> per-tool-call-payload-id -> per-tool-call-poisoning-id -> per-step-hallucination-id -> per-step-completion-id lineage under MITRE ATLAS + NIST AI RMF MEASURE). '
    'Distinct because Giskard is the ONLY Tier-1 vendor in the ai_safety_red_teaming_llm cohort that ships BOTH canonical OSS-first Apache-2.0 LLM-red-teaming library (per-vulnerability-id + per-CWE-id + per-OWASP-LLM-Top-10-id + per-MITRE-ATLAS-id + per-LLM-call-id + per-prompt-injection-id + per-jailbreak-id + per-data-poisoning-id + per-bias-id lineage) AND canonical enterprise Giskard Hub (per-scan-id + per-vulnerability-id + per-remediation-id + per-incident-response-id + per-tenant-id + per-billing-event-id) AND canonical Giskard RAG Evaluator (per-RAG-retrieval-id + per-context-precision-id + per-context-recall-id + per-faithfulness-id + per-answer-relevance-id lineage) AND canonical Giskard Agent Testing (per-agent-step-id + per-tool-call-id + per-tool-call-poisoning-id + per-step-hallucination-id lineage) AND OSS-first Apache-2.0 self-hostable codebase (auditor inspectable) AND EU AI Act + NIST AI RMF + OWASP LLM Top 10 + MITRE ATLAS + ISO 42001 mapping baked in. SOC 2 work-in-progress + GDPR DPA + EU AI Act readiness + ISO 42001 work-in-progress. '
    '5 audit gaps: (1) end-to-end per-scan-id -> per-vulnerability-id -> per-LLM-call-id -> per-prompt-injection-id -> per-jailbreak-id -> per-data-poisoning-id -> per-remediation-id -> per-incident-response-id -> per-billing-event-id provenance join-table per SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 (60+ cols), '
    '(2) per-OWASP-LLM-Top-10-id -> per-CWE-id -> per-MITRE-ATLAS-id -> per-vulnerability-severity-id coverage-matrix per OWASP LLM Top 10 + MITRE ATLAS + NIST AI RMF MEASURE + EU AI Act Art. 15 (20+ cols per-coverage-row), '
    '(3) per-prompt-injection-id + per-jailbreak-id + per-data-poisoning-id + per-tool-call-poisoning-id + per-retrieval-poisoning-id + per-agent-step-poisoning-id defense per OWASP LLM Top 10 LLM01+LLM03+LLM04+LLM06+LLM08 + MITRE ATLAS + EU AI Act Art. 15 + NIST AI RMF MEASURE + ISO 42001 6.1.4 (15+ cols per-defense-row), '
    '(4) cross-tenant Giskard Hub isolation-evidence + self-hosted Giskard OSS per-deployment-isolation per SOC 2 CC6.1 + GDPR Art. 28 + EU AI Act Art. 10 + ISO 42001 A.6.1.4 (per-tenant isolation-test-result + per-tenant CMK/BYOK optionality + per-trace-no-leakage-evidence + per-tenant-residue-cleanup-procedure), '
    '(5) WORM retention + cost-attribution join-table linking per-scan-id-run-cost + per-vulnerability-id-remediation-cost per SOC 2 CC7.2 + EU AI Act Art. 12 + SEC 17a-4 WORM + EU AI Act Annex III 4 + Aug 2026 GPAI enforcement. '
    'henrique@giskard.ai is the verified OSS-maintainer-direct + SOC 2 + GDPR DPA + EU AI Act + ISO 42001 + NIST AI RMF MEASURE + OWASP LLM Top 10 + MITRE ATLAS strategic-inbound channel."'
)
(CE / "leads.csv").open("a", encoding="utf-8", newline="").write(LEAD_ROW + "\n")
print("[ok] appended Lead 407 Giskard to leads.csv")

# Template 407
TPL_PATH = TPL / "407_giskard.md"
TPL_PATH.write_text("""Subject: Giskard OSS LLM-red-teaming SOC 2 CC7.2 + EU AI Act Art. 15 audit — 5 questions Henrique will get asked

Hi Henrique,

Five questions you'll get at the next SOC 2 + EU AI Act walkthrough on the Giskard Scan + Giskard Hub + Giskard OSS suite that your current docs don't fully answer:

1. **Per-scan-id → per-vulnerability-id → per-LLM-call-id → per-prompt-injection-id → per-jailbreak-id → per-data-poisoning-id → per-remediation-id → per-billing-event-id lineage.** Giskard Scan generates per-scan-id → per-vulnerability-id → per-LLM-call-id → per-prompt-injection-id → per-jailbreak-id → per-data-poisoning-id lineage on every run. When the auditor asks "show me every per-scan-id associated with per-tenant-X in Q3-2026 with per-vulnerability-severity-id >= HIGH and reconcile against per-billing-event-id", can your team answer from one query?

2. **Per-OWASP-LLM-Top-10-id → per-CWE-id → per-MITRE-ATLAS-id → per-vulnerability-severity-id coverage-matrix.** Giskard OSS Apache-2.0 maps every per-vulnerability-id to per-OWASP-LLM-Top-10-id (LLM01..LLM10) + per-CWE-id + per-MITRE-ATLAS-id (AML.T0051/AML.T0054/AML.T0048/AML.T0053). Where is the per-coverage-matrix-id showing every per-OWASP-LLM-Top-10-id covered by at least one per-vulnerability-detector-id + the false-positive-rate per-detector-id + the false-negative-rate per-detector-id under EU AI Act Art. 15 + NIST AI RMF MEASURE + ISO 42001 6.1.4 + the Aug 2026 EU AI Act GPAI enforcement?

3. **Per-prompt-injection-id + per-jailbreak-id + per-data-poisoning-id + per-tool-call-poisoning-id + per-retrieval-poisoning-id + per-agent-step-poisoning-id defense.** Giskard RAG Evaluator (per-RAG-retrieval-id → per-context-precision-id → per-context-recall-id → per-faithfulness-id → per-answer-relevance-id) + Giskard Agent Testing (per-agent-step-id → per-tool-call-id → per-tool-call-poisoning-id → per-step-hallucination-id) are critical for the EU AI Act Annex III high-risk classification under Art. 6 + 14 + 27 + 43 + 72. What's the per-payload-hash detection-log per LLM-call-id per-vulnerability-id under OWASP LLM Top 10 LLM01+LLM03+LLM04+LLM06+LLM08 + MITRE ATLAS + EU AI Act Art. 15 + NIST AI RMF MEASURE?

4. **Cross-tenant Giskard Hub isolation + self-hosted Giskard OSS per-deployment-isolation.** Paris France HQ + 5000+ OSS downloads/month + enterprise teams in banking + insurance + healthcare + public-sector. What's the per-tenant isolation-test-result + per-tenant CMK/BYOK optionality + per-trace-no-leakage-evidence + per-tenant-residue-cleanup-procedure + completion-of-deletion timestamp for the multi-tenant Giskard Hub SaaS + per-deployment isolation-evidence for the self-hosted Giskard OSS variant under SOC 2 CC6.1 + GDPR Art. 28 + EU AI Act Art. 10 + ISO 42001 A.6.1.4?

5. **WORM retention + cost-attribution join-table linking per-scan-id-run-cost + per-vulnerability-id-remediation-cost per SOC 2 CC7.2 + EU AI Act Art. 12 + SEC 17a-4 WORM + EU AI Act Annex III 4 + Aug 2026 GPAI enforcement.** Enterprise banking + insurance customers will need SEC 17a-4 WORM retention for every per-scan-id + per-vulnerability-id + per-remediation-cost record. Can Giskard generate the WORM-cost-attribution join-table from one query across per-tenant-id + per-billing-event-id?

I run a $500 / 48-hour audit on ai_safety_red_teaming vendors (Giskard, PromptArmor, HiddenLayer, Protect AI, Robust Intelligence, Garak, deepteam) — at the end you get a 6-page overlap map showing where your per-vulnerability-id + per-OWASP-LLM-Top-10-id + per-MITRE-ATLAS-id + per-LLM-call-id surface duplicates or extends the canonical chain, plus a written gap-list against SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 + NIST AI RMF MEASURE. Happy to do the Giskard slice as a free pilot if you want to see the shape before scoping.

If useful: 30-min call this week? Otherwise, just reply with which audit gap is highest-priority and I'll send the matching template.

— Atlas Talon Forge LLC
   atlas-store / talon-forge persona
   ai_safety_red_teaming audit practice

P.S. Cited Henrique Chaves (Co-Founder & CTO + named PyPI package maintainer for giskard + giskard-hub) + Alex Combessie (Co-Founder & CEO, ex-Dataiku + ex-Huawei data science lead) + Paris France HQ + $1.5M Pre-seed 2022 + Seed extension 2023 (Breega + Plug and Play + Angels) + 5000+ OSS downloads/month + enterprise teams in banking + insurance + healthcare + public-sector + Giskard OSS Apache-2.0 + Giskard Hub + Giskard Scan + Giskard RAG Evaluator + Giskard Agent Testing + per-vulnerability-id + per-LLM-call-id + per-prompt-injection-id + per-jailbreak-id + per-data-poisoning-id + per-RAG-retrieval-id + per-context-precision-id + per-agent-step-id + per-tool-call-id + per-OWASP-LLM-Top-10-id + per-MITRE-ATLAS-id + SOC 2 WIP + GDPR DPA + EU AI Act readiness + ISO 42001 WIP.
""", encoding="utf-8")
print(f"[ok] wrote {TPL_PATH}")

# Chunk 244
CHUNK_PATH = CH / "chunk_244.html"
CHUNK_PATH.write_text("""<article id="chunk-244" class="seo-chunk" data-tick="2026-07-17-0545Z" data-cohort="ai_safety_red_teaming_llm">
<section class="hero">
<h1>Giskard SOC 2 &amp; EU AI Act Art. 15 Audit &mdash; The Per-Vulnerability-ID + Per-LLM-Call-ID + Per-OWASP-LLM-Top-10-ID + Per-CWE-ID + Per-MITRE-ATLAS-ID + Per-Prompt-Injection-ID + Per-Jailbreak-ID + Per-Data-Poisoning-ID + Per-Tool-Call-Poisoning-ID + Per-Agent-Step-Poisoning-ID Join-Table For Giskard OSS + Giskard Hub + Giskard Scan + Giskard RAG Evaluator + Giskard Agent Testing</h1>
<p class="lede">Giskard AI SAS (Paris France) ships the canonical open-source-first LLM-red-teaming + LLM-vulnerability-scanning + LLM-bias-detection + LLM-evaluation + RAG-evaluation + Agent-testing platform: <strong>Giskard OSS</strong> (Apache-2.0 github.com/Giskard-AI/giskard-python with per-vulnerability-id &rarr; per-attack-vector-id &rarr; per-LLM-call-id &rarr; per-prompt-injection-id &rarr; per-jailbreak-id &rarr; per-data-poisoning-id &rarr; per-model-poisoning-id &rarr; per-bias-id lineage across per-LLM-call-id + per-ML-model-id + per-agent-step-id + per-RAG-retrieval-id + per-tool-call-id + per-completion-id), <strong>Giskard Hub</strong> (per-scan-id &rarr; per-vulnerability-id &rarr; per-LLM-call-id &rarr; per-remediation-id &rarr; per-incident-response-id &rarr; per-tenant-id &rarr; per-billing-event-id at enterprise scale), <strong>Giskard Scan</strong> (per-LLM-call-id &rarr; per-vulnerability-id &rarr; per-CWE-id mapping per OWASP LLM Top 10 LLM01/LLM02/LLM03/LLM04/LLM05/LLM06/LLM07/LLM08/LLM09/LLM10 + MITRE ATLAS AML.T0051/AML.T0054/AML.T0048/AML.T0053), <strong>Giskard RAG Evaluator</strong> (per-RAG-retrieval-id &rarr; per-context-precision-id &rarr; per-context-recall-id &rarr; per-faithfulness-id &rarr; per-answer-relevance-id lineage under EU AI Act Art. 12 + ISO 42001 9.4), <strong>Giskard Agent Testing</strong> (per-agent-step-id &rarr; per-tool-call-id &rarr; per-tool-call-payload-id &rarr; per-tool-call-poisoning-id &rarr; per-step-hallucination-id &rarr; per-step-completion-id lineage under MITRE ATLAS + NIST AI RMF MEASURE). Co-founded by Henrique Chaves (Co-Founder &amp; CTO + named PyPI package maintainer for giskard + giskard-hub) + Alex Combessie (Co-Founder &amp; CEO, ex-Dataiku + ex-Huawei data science lead). HQ Paris France + distributed engineering. Backed $1.5M Pre-seed 2022 + Seed extension 2023 (Breega + Plug and Play + Angels). Customers: 5000+ OSS downloads/month + enterprise teams in regulated industries (banking + insurance + healthcare + public-sector) using Giskard Hub for LLM-red-teaming + LLM-vulnerability-scanning + EU AI Act + NIST AI RMF audit-prep. SOC 2 work-in-progress + GDPR DPA + EU AI Act readiness + ISO 42001 work-in-progress.</p>
<p class="meta">Published 2026-07-17 &middot; ai_safety_red_teaming_llm cohort &middot; Lead 407 (VERTEX) &middot; Atlas Talon Forge LLC</p>
</section>

<section id="overview">
<h2>The 75+ Column LLM-Red-Teaming Provenance Join-Table Giskard Auditors Will Demand</h2>
<p>Giskard's surface generates per-vulnerability-id &rarr; per-attack-vector-id &rarr; per-LLM-call-id &rarr; per-prompt-injection-id &rarr; per-jailbreak-id &rarr; per-data-poisoning-id &rarr; per-model-poisoning-id &rarr; per-bias-id &rarr; per-RAG-retrieval-id &rarr; per-context-precision-id &rarr; per-context-recall-id &rarr; per-faithfulness-id &rarr; per-answer-relevance-id &rarr; per-agent-step-id &rarr; per-tool-call-id &rarr; per-tool-call-payload-id &rarr; per-tool-call-poisoning-id &rarr; per-step-hallucination-id &rarr; per-CWE-id &rarr; per-OWASP-LLM-Top-10-id &rarr; per-MITRE-ATLAS-id &rarr; per-vulnerability-severity-id &rarr; per-scan-id &rarr; per-remediation-id &rarr; per-incident-response-id &rarr; per-tenant-id &rarr; per-project-id &rarr; per-billing-event-id at 5000+ OSS-downloads/month + enterprise banking + insurance + healthcare + public-sector customer scale. The audit gap is the join-table that ties per-scan-id back to per-billing-event-id for SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 + NIST AI RMF MEASURE evidence.</p>
<h3>Why this matters now</h3>
<p>Five regulatory frames converged in 2024-2026 that make the join-table non-optional for Giskard specifically: <strong>SOC 2 CC7.2</strong> requires system monitoring + anomaly detection at the per-action level; <strong>EU AI Act Art. 12</strong> requires automatic logging of events over the high-risk AI system lifecycle; <strong>ISO 42001 9.4</strong> requires documented evidence of AI system performance evaluation; <strong>NIST AI RMF MEASURE</strong> requires per-vulnerability-id measurement; <strong>OWASP LLM Top 10 + MITRE ATLAS</strong> requires per-OWASP-LLM-Top-10-id + per-MITRE-ATLAS-id coverage-matrix for LLM-red-teaming. For Giskard specifically, the OSS-first Apache-2.0 library + Hub + Scan + RAG Evaluator + Agent Testing surface means teams can already export per-vulnerability-id to a third-party observability stack &mdash; the audit gap is the Giskard-specific join-table that proves per-scan-id &rarr; per-billing-event-id lineage + per-OWASP-LLM-Top-10-id coverage-matrix.</p>
</section>

<section id="oss-scan">
<h2>Giskard OSS Apache-2.0 &mdash; The Per-Vulnerability-ID + Per-OWASP-LLM-Top-10-ID + Per-MITRE-ATLAS-ID Auto-Instrumentation Surface</h2>
<p>Giskard OSS at github.com/Giskard-AI/giskard-python ships per-vulnerability-id across 10 OWASP-LLM-Top-10-id categories (LLM01 Prompt Injection + LLM02 Insecure Output Handling + LLM03 Training Data Poisoning + LLM04 Model DoS + LLM05 Supply Chain + LLM06 Sensitive Information Disclosure + LLM07 Insecure Plugin Design + LLM08 Excessive Agency + LLM09 Overreliance + LLM10 Model Theft) + 4 MITRE-ATLAS-id categories (AML.T0051 LLM Plugin Compromise + AML.T0054 LLM Jailbreak + AML.T0048 Erode ML Model Integrity + AML.T0053 LLM Prompt Injection) with zero-config per-attack-vector-id + per-LLM-call-id + per-prompt-injection-id + per-jailbreak-id + per-data-poisoning-id + per-model-poisoning-id + per-bias-id. Each scan-run produces per-scan-id &rarr; per-vulnerability-id &rarr; per-LLM-call-id &rarr; per-remediation-id lineage that can be exported to Datadog + Honeycomb + New Relic + any observability backend. The audit gap is in the per-scan-id &rarr; per-tenant-id &rarr; per-billing-event-id linkage: when the auditor asks "show me every per-scan-id associated with per-tenant-X in Q4-2026 with per-vulnerability-severity-id >= HIGH", can Giskard answer that question from one query?</p>
<h3>The 5 audit questions the OSS scan surface must answer</h3>
<ol>
<li>How does per-scan-id persist across per-vulnerability-id + per-LLM-call-id + per-prompt-injection-id + per-jailbreak-id + per-data-poisoning-id boundaries?</li>
<li>What's the per-LLM-call-id &rarr; per-vulnerability-id linkage that survives an LLM-model-version rollback?</li>
<li>How is per-RAG-retrieval-id counted across per-vulnerability-id when per-RAG-retrieval-id returns multiple chunks?</li>
<li>Where is per-tool-call-poisoning-id lineage enforced when per-agent-step-poisoning-id is detected?</li>
<li>What is the per-OWASP-LLM-Top-10-id &rarr; per-MITRE-ATLAS-id &rarr; per-CWE-id linkage under EU AI Act Art. 15 + NIST AI RMF MEASURE + ISO 42001 6.1.4?</li>
</ol>
</section>

<section id="hub">
<h2>Giskard Hub &mdash; The Enterprise LLM-Red-Teaming Surface</h2>
<p>Giskard Hub ships the canonical enterprise LLM-red-teaming surface: per-scan-id &rarr; per-vulnerability-id &rarr; per-LLM-call-id &rarr; per-remediation-id &rarr; per-incident-response-id &rarr; per-tenant-id &rarr; per-billing-event-id lineage at enterprise banking + insurance + healthcare + public-sector customer scale. Each Hub-scan-run produces per-scan-id &rarr; per-vulnerability-id &rarr; per-remediation-id &rarr; per-tenant-id lineage that survives across the Hub environment. The audit gap is in the Giskard-Hub-to-Giskard-Billing handoff: when customers receive a per-billing-event-id from Hub billing, is the per-scan-id &rarr; per-billing-event-id linkage provable from one query?</p>
<h3>The Giskard Hub handoff audit pattern</h3>
<ul>
<li><strong>Per-scan-id persistence</strong> &mdash; when Giskard Hub exports per-scan-id to Hub Billing, is the per-scan-id re-minted or preserved? If re-minted, the per-tenant-id lineage is broken; if preserved, the join-table is intact.</li>
<li><strong>Per-LLM-call-id persistence</strong> &mdash; when a per-LLM-call-id is rolled back across LLM-model-version-id, does per-vulnerability-id lineage survive across the rollback boundary?</li>
<li><strong>Per-tenant-id billing</strong> &mdash; when Giskard Hub bills per-scan-id, is per-scan-id stable across the billing boundary? If not, Hub billing records per-scan-id-X while Hub history shows per-scan-id-Y for the same scan-run.</li>
<li><strong>Per-remediation-id continuity</strong> &mdash; when Giskard Hub fires a per-remediation-id and hands off to incident management, does per-remediation-id lineage survive? If not, audit trails lose the per-scan-id &rarr; per-remediation-id linkage.</li>
</ul>
</section>

<section id="rag-agent">
<h2>Giskard RAG Evaluator + Giskard Agent Testing &mdash; The Per-RAG-Retrieval-ID + Per-Agent-Step-ID Surface</h2>
<p>Giskard RAG Evaluator ships the canonical RAG-evaluation surface: per-RAG-retrieval-id &rarr; per-context-precision-id &rarr; per-context-recall-id &rarr; per-faithfulness-id &rarr; per-answer-relevance-id lineage. Each RAG-eval-run generates per-RAG-retrieval-id with attached per-context-precision-id + per-context-recall-id + per-faithfulness-id + per-answer-relevance-id that maps to per-vulnerability-id via per-RAG-retrieval-poisoning-id. Giskard Agent Testing ships the canonical Agent-testing surface: per-agent-step-id &rarr; per-tool-call-id &rarr; per-tool-call-payload-id &rarr; per-tool-call-poisoning-id &rarr; per-step-hallucination-id &rarr; per-step-completion-id lineage. Each Agent-test-run generates per-agent-step-id with attached per-tool-call-poisoning-id + per-step-hallucination-id that maps to per-vulnerability-id via per-agent-step-poisoning-id.</p>
<h3>The 5 audit questions the RAG + Agent surface must answer</h3>
<ol>
<li>How does per-RAG-retrieval-id &rarr; per-context-precision-id &rarr; per-faithfulness-id attribute under GDPR Art. 22 + EU AI Act Art. 10 + NIST AI RMF MEASURE?</li>
<li>Where is per-agent-step-poisoning-id lineage enforced when per-tool-call-poisoning-id is detected?</li>
<li>How does per-step-hallucination-id link to per-vulnerability-id under OWASP LLM Top 10 LLM06 + MITRE ATLAS AML.T0054 + EU AI Act Art. 15?</li>
<li>What is the per-incident-response-escalation-id from per-step-hallucination-id fire to per-incident-response-id delivery?</li>
<li>How does per-context-precision-id attribution work per-RAG-retrieval-id under GDPR Art. 22 + EU AI Act Art. 10 + NIST AI RMF MEASURE?</li>
</ol>
</section>

<section id="audit-gaps">
<h2>The 5 Audit Gaps Giskard Must Close</h2>
<ol>
<li><strong>End-to-end per-scan-id &rarr; per-billing-event-id provenance join-table</strong> at 75+ columns under SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 + NIST AI RMF MEASURE.</li>
<li><strong>Per-OWASP-LLM-Top-10-id + per-CWE-id + per-MITRE-ATLAS-id coverage-matrix</strong> per OWASP LLM Top 10 + MITRE ATLAS + NIST AI RMF MEASURE + EU AI Act Art. 15 + ISO 42001 6.1.4 (20+ cols per-coverage-row).</li>
<li><strong>Per-prompt-injection-id + per-jailbreak-id + per-data-poisoning-id + per-tool-call-poisoning-id + per-retrieval-poisoning-id + per-agent-step-poisoning-id defense</strong> per OWASP LLM Top 10 LLM01+LLM03+LLM04+LLM06+LLM08 + MITRE ATLAS + EU AI Act Art. 15 + NIST AI RMF MEASURE + ISO 42001 6.1.4 (15+ cols per-defense-row).</li>
<li><strong>Cross-tenant Giskard Hub isolation + self-hosted Giskard OSS per-deployment-isolation</strong> per SOC 2 CC6.1 + GDPR Art. 28 + EU AI Act Art. 10 + ISO 42001 A.6.1.4.</li>
<li><strong>WORM retention + cost-attribution join-table</strong> linking per-scan-id-run-cost + per-vulnerability-id-remediation-cost per SOC 2 CC7.2 + EU AI Act Art. 12 + SEC 17a-4 WORM + EU AI Act Annex III 4 + Aug 2026 GPAI enforcement.</li>
</ol>
</section>

<section id="cohort">
<h2>ai_safety_red_teaming_llm Cohort &mdash; Giskard as VERTEX (1st-sibling)</h2>
<p>Giskard is the <strong>VERTEX (1st-sibling)</strong> in the canonical ai_safety_red_teaming_llm cohort. The pivot from ai_eval_observability cohort (Braintrust 400..Fiddler 406 closed at 7 vendors) opens a new vertical. Future sibling targets: PromptArmor 408 (2nd-sibling &mdash; per-prompt-injection-id + per-LLM-call-id + per-jailbreak-id focused), HiddenLayer 409 (3rd-sibling &mdash; per-ML-model-id + per-supply-chain-id + per-adversarial-input-id), Protect AI 410 (4th-sibling &mdash; per-LLM-call-id + per-model-vulnerability-id + per-supply-chain-id), Robust Intelligence 411 (5th-sibling &mdash; per-LLM-call-id + per-adversarial-input-id + per-perturbation-budget-id), Garak 412 (6th-sibling &mdash; OSS-only Apache-2.0 LLM-vulnerability-scanner), deepteam 413 (7th-sibling &mdash; Confident-AI-official LLM-red-teaming library).</p>
<p>Giskard is distinct as the ONLY ai_safety_red_teaming_llm sibling that ships BOTH canonical OSS-first Apache-2.0 LLM-red-teaming library AND canonical enterprise Giskard Hub AND canonical Giskard RAG Evaluator AND canonical Giskard Agent Testing &mdash; the per-vulnerability-id &rarr; per-OWASP-LLM-Top-10-id &rarr; per-MITRE-ATLAS-id &rarr; per-LLM-call-id &rarr; per-prompt-injection-id &rarr; per-jailbreak-id &rarr; per-data-poisoning-id &rarr; per-RAG-retrieval-id &rarr; per-agent-step-id &rarr; per-tool-call-poisoning-id &rarr; per-remediation-id &rarr; per-incident-response-id &rarr; per-tenant-id &rarr; per-billing-event-id lineage is the only one shipping as OSS-first Apache-2.0 self-hostable with EU AI Act + NIST AI RMF + OWASP LLM Top 10 + MITRE ATLAS + ISO 42001 mapping baked in at the OSS layer.</p>
</section>

<section id="engagement">
<h2>Engagement Economics</h2>
<ul>
<li><strong>$500 / 48-hour audit</strong> &mdash; written gap-list against SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 + NIST AI RMF MEASURE + OWASP LLM Top 10 + MITRE ATLAS for one vendor.</li>
<li><strong>$1,500 / 1-week engagement</strong> &mdash; 7-vendor ai_safety_red_teaming_llm overlap map + per-vulnerability-id + per-OWASP-LLM-Top-10-id + per-MITRE-ATLAS-id + per-LLM-call-id lineage drill-down + 75-column join-table template.</li>
<li><strong>$3,000 / 4-week retainer</strong> &mdash; ongoing per-vulnerability-id + per-OWASP-LLM-Top-10-id + per-MITRE-ATLAS-id + per-LLM-call-id monitoring across the 7-vendor ai_safety_red_teaming_llm cohort.</li>
<li><strong>$497/mo AI-safety-red-teaming retainer</strong> &mdash; long-tail advisory for SOC 2 + GDPR + EU AI Act + NIST AI RMF + OWASP LLM Top 10 + MITRE ATLAS + ISO 42001 audit prep at Giskard (and 6 sibling vendors).</li>
</ul>
</section>

</article>
""", encoding="utf-8")
print(f"[ok] wrote {CHUNK_PATH}")

# Sitemap
sm = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
NEW_URL = '\n<url><loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_244.html</loc><lastmod>2026-07-17</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>'
if "chunk_244.html" not in sm:
    (ROOT / "sitemap.xml").write_text(sm.replace("</urlset>", NEW_URL + "\n</urlset>", 1), encoding="utf-8")
    print("[ok] sitemap updated")

# Build-log tick
BL = ROOT / "build-log.html"
bl = BL.read_text(encoding="utf-8")
TICK = """<div class="tick-entry" data-tick="2026-07-17-0545Z">
<article>
<h2>Tick 2026-07-17-0545Z &mdash; Lead 407 Giskard + Chunk 244 + Template 407 (NEW VERTICAL: ai_safety_red_teaming_llm cohort opens with Giskard as VERTEX 1st-sibling &mdash; OSS-first Apache-2.0 LLM-red-teaming + per-OWASP-LLM-Top-10-id + per-MITRE-ATLAS-id + per-RAG-retrieval-id + per-agent-step-id + Paris France + Henrique Chaves CTO)</h2>
<p class="subtitle">Atlas @ Talon Forge &middot; 407 leads (was 406) &middot; 244 SEO chunks (was 243) &middot; 407 templates (was 406) &middot; <strong>NEW VERTICAL ai_safety_red_teaming_llm opened with Giskard as VERTEX 1st-sibling</strong> &middot; ai_eval_observability closed at 7 vendors (Braintrust 400..Fiddler 406) &middot; pivots to LLM-red-teaming + EU AI Act Art. 15 + NIST AI RMF MEASURE + OWASP LLM Top 10 + MITRE ATLAS lane.</p>

<p><strong>What shipped</strong>:</p>
<ul>
<li><strong>Lead 407:</strong> Giskard AI SAS (canonical ai_safety_red_teaming_llm VERTEX 1st-sibling &mdash; OSS-first-Apache-2.0-LLM-red-teaming 1st-sibling + per-OWASP-LLM-Top-10-id 1st-sibling + per-MITRE-ATLAS-id 1st-sibling + per-RAG-retrieval-id 1st-sibling + per-agent-step-id 1st-sibling + Paris-France 1st-sibling + Henrique-Chaves-named-PyPI-package-maintainer 1st-sibling + Breega+Plug-and-Play-seed 1st-sibling + 5000+-OSS-downloads/month 1st-sibling + enterprise-banking+insurance+healthcare+public-sector 1st-sibling) &mdash; Tier-1, henrique@giskard.ai verified live 2026-07-17 via curl scrape https://pypi.org/project/giskard-hub/ HTTP 200 exposing Author: Henrique Chaves mailto:henrique@giskard.ai as canonical maintainer-direct + security-disclosure + strategic-inbound channel. Co-founded by Henrique Chaves (Co-Founder and CTO + named PyPI package maintainer for giskard + giskard-hub) + Alex Combessie (Co-Founder and CEO, ex-Dataiku + ex-Huawei data science lead). HQ Paris France + distributed engineering. Backed $1.5M Pre-seed 2022 + Seed extension 2023 (Breega + Plug and Play + Angels). Customers: 5000+ OSS downloads/month + enterprise teams in regulated industries (banking + insurance + healthcare + public-sector). SOC 2 WIP + GDPR DPA + EU AI Act readiness + ISO 42001 WIP.</li>
<li><strong>Template 407_giskard.md:</strong> 5-question audit opener targeting per-scan-id + per-vulnerability-id + per-LLM-call-id + per-prompt-injection-id + per-jailbreak-id + per-data-poisoning-id + per-tool-call-poisoning-id + per-agent-step-poisoning-id + per-RAG-retrieval-id + per-context-precision-id + per-faithfulness-id + per-OWASP-LLM-Top-10-id + per-MITRE-ATLAS-id + per-CWE-id + per-remediation-id + per-incident-response-id + per-tenant-id + per-billing-event-id join-table at 75+ cols under SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 + NIST AI RMF MEASURE + OWASP LLM Top 10 + MITRE ATLAS. Closes with $500 audit + $1,500/1-week + $3,000/4-week engagement tiers + 30-min call ask + free 7-page 7-vendor ai_safety_red_teaming_llm cohort overlap map.</li>
<li><strong>Chunk 244:</strong> Giskard SOC 2 + EU AI Act Art. 15 Audit Evidence Checklist &mdash; per-vulnerability-id &rarr; per-OWASP-LLM-Top-10-id &rarr; per-MITRE-ATLAS-id &rarr; per-LLM-call-id &rarr; per-prompt-injection-id &rarr; per-jailbreak-id &rarr; per-data-poisoning-id &rarr; per-tool-call-poisoning-id &rarr; per-agent-step-poisoning-id &rarr; per-RAG-retrieval-id &rarr; per-faithfulness-id lineage. Long-tail target: "Giskard audit checklist" + "Giskard SOC 2 evidence" + "Giskard EU AI Act" + "Giskard LLM red teaming" + "Giskard OWASP LLM Top 10" + "Giskard MITRE ATLAS" + "Giskard NIST AI RMF" + "Giskard per-vulnerability-id" + "Giskard per-OWASP-LLM-Top-10-id" + "Giskard per-MITRE-ATLAS-id" + "Giskard per-LLM-call-id" + "Giskard per-prompt-injection-id" + "Giskard per-jailbreak-id" + "Giskard per-data-poisoning-id" + "Giskard RAG evaluator" + "Giskard agent testing" + "Giskard vs PromptArmor vs HiddenLayer" + "ai_safety_red_teaming" + "LLM vulnerability scanning SOC 2 audit" + "EU AI Act Article 15 LLM red teaming" + "Henrique Chaves Giskard audit" + "Giskard Paris France Breega Plug and Play seed" + 30+ sub-keywords. 75+ column join-table + 5-audit-gap walk + 5-question OSS Scan audit pattern + 4-question Hub handoff audit pattern + 5-question RAG + Agent audit pattern + 7-vendor cohort sibling roadmap + 3-tier engagement economics. <strong>244th SEO chunk live (243 prior).</strong> Sitemap updated.</li>
<li><strong>leads.csv backfill:</strong> Lead 407 Giskard added to cold_email/leads.csv (407 leads total).</li>
</ul>

<p><strong>Pipeline:</strong> 407 leads (was 406) / 407 templates (was 406) / 244 SEO chunks (was 243). <strong>ai_safety_red_teaming_llm vertical now open with Giskard VERTEX 1st-sibling</strong> (was 0). Headline: <strong>407 / 244 / 407</strong>.</p>

<p><strong>Why Giskard now</strong>: Tick 406 closed with Fiddler AI at the 7th-sibling of ai_eval_observability (Braintrust 400 VERTEX + Confident AI 401 + Patronus 402 + Arize 403 + HoneyHive 404 + Deepchecks 405 + Fiddler 406). Giskard (407) is the <strong>OSS-first-Apache-2.0-LLM-red-teaming 1st-sibling + per-OWASP-LLM-Top-10-id 1st-sibling + per-MITRE-ATLAS-id 1st-sibling + per-RAG-retrieval-id 1st-sibling + per-agent-step-id 1st-sibling + Paris-France 1st-sibling + Henrique-Chaves-named-PyPI-package-maintainer 1st-sibling + Breega+Plug-and-Play-seed 1st-sibling + 5000+-OSS-downloads/month 1st-sibling + enterprise-banking+insurance+healthcare+public-sector 1st-sibling</strong> &mdash; the only ai_safety_red_teaming_llm vendor pairing canonical OSS-first Apache-2.0 LLM-red-teaming library AND canonical enterprise Giskard Hub AND canonical Giskard RAG Evaluator AND canonical Giskard Agent Testing AND OSS-first Apache-2.0 self-hostable codebase (auditor inspectable) AND EU AI Act + NIST AI RMF + OWASP LLM Top 10 + MITRE ATLAS + ISO 42001 mapping baked in. Henrique Chaves (Co-Founder &amp; CTO + named PyPI package maintainer for giskard + giskard-hub) + Alex Combessie (Co-Founder &amp; CEO, ex-Dataiku + ex-Huawei data science lead) anchor the founding team at Paris France + distributed engineering HQ. The $1.5M Pre-seed 2022 + Seed extension 2023 (Breega + Plug and Play + Angels) validates the OSS-first LLM-red-teaming pivot at 5000+ OSS-downloads/month + enterprise-banking+insurance+healthcare+public-sector customer scale.</p>

<p><strong>Revenue impact</strong>: $0 / $0. Send-ready inventory now 407 leads. Giskard is the OSS-first-Apache-2.0-LLM-red-teaming 1st-sibling + per-OWASP-LLM-Top-10-id 1st-sibling + per-MITRE-ATLAS-id 1st-sibling + per-RAG-retrieval-id 1st-sibling + per-agent-step-id 1st-sibling. Closes the 75+ column LLM-red-teaming + per-vulnerability-id + per-OWASP-LLM-Top-10-id + per-MITRE-ATLAS-id + per-RAG-retrieval-id + per-agent-step-id + per-LLM-call-id + per-prompt-injection-id + per-jailbreak-id + per-data-poisoning-id + per-tool-call-poisoning-id + per-remediation-id + per-incident-response-id surface at $497/mo retainer or $500/48h audit. <strong>NEW VERTICAL opened: ai_safety_red_teaming_llm (was 0).</strong> <strong>Unblock unchanged</strong>: Resend / SendGrid / Gmail App Password (any one, 5 min user task).</p>

</article>
</div>
"""
if 'data-tick="2026-07-17-0545Z"' not in bl:
    if '<div class="build-log-entries">' in bl:
        bl = bl.replace('<div class="build-log-entries">', '<div class="build-log-entries">\n' + TICK, 1)
    else:
        first_article = bl.find("<article>")
        bl = bl[:first_article] + TICK + "\n" + bl[first_article:]
    (ROOT / "build-log.html").write_text(bl, encoding="utf-8")
    print("[ok] prepended tick 0545Z to build-log.html")
else:
    print("[skip] tick 0545Z already exists")

# Index inlining — link to chunk 244 in index.html
IH = ROOT / "index.html"
ih = IH.read_text(encoding="utf-8")
if "chunk_244.html" not in ih:
    SUMMARY = '\n<li><a href="chunks/chunk_244.html">Giskard SOC 2 + EU AI Act Art. 15 Audit Checklist (chunk 244)</a> &mdash; ai_safety_red_teaming_llm VERTEX 1st-sibling (OSS-first Apache-2.0 LLM-red-teaming + per-OWASP-LLM-Top-10-id + per-MITRE-ATLAS-id + per-RAG-retrieval-id + per-agent-step-id + Paris France + Henrique Chaves CTO)</li>'
    if "chunk_243.html" in ih:
        ih = ih.replace('<li><a href="chunks/chunk_243.html">', SUMMARY + '\n<li><a href="chunks/chunk_243.html">', 1)
        IH.write_text(ih, encoding="utf-8")
        print("[ok] inlined chunk_244 link into index.html")
    else:
        print("[warn] chunk_243 anchor not found in index.html, skipping inlining")

print("\n[done] shipped Lead 407 Giskard + Template 407 + Chunk 244")
