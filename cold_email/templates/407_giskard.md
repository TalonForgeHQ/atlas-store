Subject: Giskard OSS LLM-red-teaming SOC 2 CC7.2 + EU AI Act Art. 15 audit — 5 questions Henrique will get asked

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
