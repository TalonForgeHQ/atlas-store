# 287 - DataRobot (privacy@datarobot.com - GDPR/SOC 2/EU AI Act/ISO 42001/HIPAA/FedRAMP strategic-inbound channel) - ai_governance_ml_platform 1st sibling - DataRobot AI Platform + DataRobot Govern + DataRobot Agentic AI + DataRobot Apps + DataRobot AutoML + DataRobot MLOps + DataRobot Generative AI + DataRobot Vector Database + DataRobot Time Series + DataRobot Notebooks + DataRobot Enterprise + DataRobot Government + DataRobot for Healthcare + DataRobot for Financial Services

**To:** privacy@datarobot.com (verified live 2026-07-16 from https://www.datarobot.com/privacy/ HTTP 200 175KB+ exposing mailto:privacy@datarobot.com as the canonical GDPR Art. 28 DPA + SOC 2 Type II + EU AI Act Annex IV + ISO 42001 + ISO 27001 + HIPAA + FedRAMP Moderate strategic-inbound channel)

**Subject:** 4 questions for DataRobot before any EU bank signs DataRobot Govern for the Aug 2026 GPAI enforcement window

Hi DataRobot privacy team,

I run a 5-minute AI compliance audit for AI-governance + ML-platform + Agentic-AI vendors. I pulled your privacy policy at datarobot.com/privacy (verified live 2026-07-16) and want to flag four audit-trail gaps that come up on every US-top-10-bank + Fortune-500 + EU-public-sector RFP I see for DataRobot Govern + DataRobot Agentic AI + DataRobot AI Platform ahead of the Aug 2026 EU AI Act GPAI enforcement deadline:

1. **Per-AI-model-lineage + per-prompt-template-version join-table.** DataRobot Govern tracks model-cards + model-versions + model-stages + deployment-status. For the Aug 2026 GPAI technical-documentation requirement (Annex IV §1(c)) can you join per-model-id → per-prompt-template-version-id → per-Agentic-AI-tool-call-id → per-Agentic-AI-reasoning-chain-step → per-human-oversight-event-id → per-tenant-key → per-deployment-id for SOC 2 CC7.2 + EU AI Act Art. 12 record-keeping? Same question for the DataRobot Agentic AI surface — per-tool-call → per-tool-output → per-decision-step → per-next-action joinable to the model-lineage.

2. **NIST AI RMF MEASURE event + ISO 42001 §9.4 control-test reasoning-chain.** DataRobot Govern ships fairness + bias + explainability + model-monitoring. For each MEASURE event, do you persist per-model-id → per-evaluation-dataset-id → per-fairness-metric-id → per-bias-score → per-confidence-interval → per-mitigation-action-id under NIST AI RMF MEASURE + ISO 42001 §9.4? Same question for the AI-Bill-of-Rights evaluation surface and the per-tenant EU-AI-Act-Annex-IV-record joinable per-tenant-key.

3. **Per-tenant KMS-CMK-BYOK + cross-tenant Agentic-AI isolation.** US-top-10-banks + 100+ government-agencies + healthcare-systems running DataRobot AI Platform + DataRobot Govern + DataRobot Agentic AI on shared infrastructure need per-tenant-KMS-key-id + per-source-credential-hash + per-Agentic-AI-session-id + per-tool-execution-scope isolation evidence for HIPAA + FedRAMP Moderate + GDPR Art. 28 + Art. 32. Can DataRobot produce that on demand? Does customer-VPC deployment keep the Agentic-AI control surface intact, or does it degrade to a shared KMS in the DataRobot control plane?

4. **Cross-border transfer SCCs-version + data-residency pinning for EU customers.** Many DataRobot customers are EU-based (Deutsche Bank + European Commission + BNP Paribas + HSBC + EU-public-sector) and need SCCs version + UK Addendum + Swiss-US DPF + per-model-deployment-region pinning (US / EU / in-customer-VPC) for GDPR Art. 46 + Art. 49. Where is that surfaced in your standard DPA? Same question for the Agentic-AI + Generative-AI + Vector Database surface.

If any of these gaps is already covered by a control I'm not seeing on datarobot.com/privacy + datarobot.com/trust, point me at it — I want my map to be accurate before I send it to prospects.

**Closing offer:** $500 / 48h AI compliance audit (delivered as a 12-section PDF mapped to SOC 2 + ISO 27001 + ISO 42001 + GDPR + EU AI Act Annex IV + HIPAA + FedRAMP Moderate + OWASP LLM Top 10 + NIST AI RMF) plus a free 1-page DataRobot vs Domino vs Neptune.ai vs Weights & Biases vs Verta compliance-overlap map. **15-min scope call** if you'd like to compare notes before any paid audit.

— Atlas
atlas@talonforge.example
https://talonforgehq.github.io/atlas-store
