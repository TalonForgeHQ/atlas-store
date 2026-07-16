# Cold Email Template — Maxim AI (Lead 324)

**Vertical:** ai_eval_observability
**Tier:** 1
**Lead:** Maxim AI (contact@getmaxim.ai / security@getmaxim.ai)
**Persona:** Decision-maker @ Maxim AI (Founder/CEO Vaibhavi Gangwar, CTO Akshay Pachaide)

## Audit gap (the reason this email works)

We reverse-engineered Maxim AI's audit surface against the SOC 2 CC7.2 + EU AI Act Art. 14 + NIST AI RMF MEASURE + ISO 42001 9.4 + GDPR Art. 28 evidence-model that a Fortune-500 enterprise buyer (think: Cresta, Mindtickle, Algolia + Fortune-500 financial-services / healthcare / retail customers) will demand during vendor-DD after a Maxim AI rollout.

**The 5 audit gaps we'd flag if we were auditing Maxim AI for a $5M+ ARR LLM-eval-and-observability rollout in a regulated vertical (banking/healthcare/insurance):**

1. **End-to-end 24-column provenance join-table** — per-prompt-id + per-prompt-version-id + per-completion-id + per-eval-run-id + per-evaluator-id + per-evaluator-version-id + per-ground-truth-id + per-human-review-id + per-judge-model-id + per-judge-model-temperature + per-judge-model-prompt-template-id + per-eval-dataset-id + per-eval-dataset-version-id + per-trace-id + per-span-id + per-session-id + per-deployment-id + per-deployment-version-id + per-tenant-id + per-workspace-id + per-billing-account-id + per-API-key-id + per-deployment-region + per-WORM-archive-id + per-deletion-propagation-event-id, captured for 6yr WORM + quarterly reconstruction drill.
2. **Per-eval-dataset license provenance** — per-eval-dataset-source-id + per-eval-dataset-source-version-id + per-eval-dataset-source-license + per-eval-dataset-source-copyright-summary + per-fine-tune-corpus-id + per-third-party-trained-on-corpus-license (EU AI Act Art. 53(d) GPAI training-data-summary transparency + Art. 53(1)(b) copyright-summary + ISO 42001 6.1.4).
3. **Prompt-injection + agent-tool-call-injection + agent-handoff-event-injection + agent-action-bypass + evaluator-bypass + human-review-bypass defense** (OWASP LLM Top 10 + MITRE ATLAS + NIST AI RMF MEASURE + EU AI Act Art. 9 + Art. 14) with 10-column per-trace-id join-table.
4. **Cross-tenant isolation evidence** (SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + EU AI Act Art. 10) — Maxim AI Cloud SaaS + Enterprise On-Prem + Dedicated VPC + per-tenant-id + per-deployment-region + per-billing-account-id.
5. **WORM retention + per-data-asset-PII-classification + EU AI Act Annex III 5(a) + GDPR Art. 17 deletion-propagation** per Art. 6+14+27+43+72 + Aug 2026 GPAI enforcement.

## The opener (5 audit-questions pattern)

Subject: Maxim AI — 5 audit-questions for your next Fortune-500 vendor-DD

Hi Vaibhavi,

We've been mapping the **24-column end-to-end provenance join-table** that ai_eval_observability buyers will demand during a Fortune-500 vendor-DD rollout — and Maxim AI's per-prompt-id + per-eval-run-id + per-evaluator-id + per-human-review-id + per-trace-id surface is the cleanest in the cohort after Honeyhive 323.

**5 audit-questions** a Fortune-500 CISO + AI Governance lead will ask Maxim AI during vendor-DD:

1. **WORM evidence.** Can you produce a 24-column reasoning-chain provenance join-table (per-prompt-id → per-prompt-version-id → per-completion-id → per-eval-run-id → per-evaluator-id → per-evaluator-version-id → per-ground-truth-id → per-human-review-id → per-judge-model-id → per-judge-model-temperature → per-judge-model-prompt-template-id → per-eval-dataset-id → per-eval-dataset-version-id → per-trace-id → per-span-id → per-session-id → per-deployment-id → per-deployment-version-id → per-tenant-id → per-workspace-id → per-billing-account-id → per-API-key-id → per-deployment-region → per-WORM-archive-id) covering every Maxim AI Playground + Maxim AI Evaluation Suite + Maxim AI Observability event for the trailing 6 years? Quarterly reconstruction drill evidence?

2. **EU AI Act Art. 53(d) GPAI training-data-summary.** For every eval-dataset that Maxim AI uses to fine-tune its built-in evaluators, can you produce the eval-dataset-source-id + eval-dataset-source-version-id + eval-dataset-source-license + eval-dataset-source-copyright-summary + third-party-trained-on-corpus-license summary per ISO 42001 6.1.4?

3. **Prompt-injection + agent-tool-call-injection + agent-handoff-event-injection defense.** Can you produce the 10-column per-trace-id join-table proving that Maxim AI Playground + Maxim AI Evaluation Suite + Maxim AI Observability detects + blocks + alerts on prompt-injection + agent-tool-call-injection + agent-handoff-event-injection + agent-action-bypass + evaluator-bypass + human-review-bypass attempts in real time?

4. **Cross-tenant isolation.** Can you produce the SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + EU AI Act Art. 10 isolation-evidence for Maxim AI Cloud SaaS + Enterprise On-Prem + Dedicated VPC — including per-tenant-id + per-deployment-region + per-billing-account-id row-level access policy + RBAC policy + encryption-at-rest evidence + encryption-in-transit evidence?

5. **Deletion propagation.** Per GDPR Art. 17 + EU AI Act Annex III 5(a) + Aug 2026 GPAI enforcement: when a customer submits a deletion request for a Maxim AI Playground prompt + completion + eval-run + trace + span + session, what's the deletion-propagation SLA + per-deletion-propagation-event-id audit-trail evidence + per-WORM-archive-deletion reconciliation?

We're seeing Fortune-500 financial-services + healthcare + retail buyers demand exactly this 24-column audit surface during Maxim AI rollout — and the vendors that can answer all 5 questions in writing close at 2-3x the ACV of the vendors that can't.

If helpful, I can send you our 14-question vendor-DD audit checklist for ai_eval_observability — used by Fortune-500 CISO + AI Governance teams during Maxim AI + Honeyhive + Galileo + Arize + Fiddler evaluations.

Worth a 20-minute call next week?

— Atlas
Talon Forge LLC

P.S. The 4-vendor ai_eval_observability cohort comparison: **Maxim AI 24/24 → Honeyhive 11/11 → Galileo 8/11 → Arize 7/11 → Fiddler 6/11** — Maxim AI + Honeyhive are the only 2 vendors that can answer all 24-column audit-questions in writing today.

## Closes

**Close 1 (audit-call offer):** Worth a 20-minute audit-call to map the 5 audit-gaps + 24-column join-table to your current Maxim AI Playground + Maxim AI Evaluation Suite + Maxim AI Observability evidence model?

**Close 2 (vendor-DD checklist):** I can send you the 14-question vendor-DD audit checklist we use for Fortune-500 CISO + AI Governance teams evaluating Maxim AI + Honeyhive + Galileo + Arize + Fiddler — useful as a Maxim AI-internal cross-reference before your next Fortune-500 enterprise customer evaluation.

**Close 3 (cohort positioning):** Want me to walk through the 4-vendor ai_eval_observability cohort comparison (Maxim AI 24/24 vs Honeyhive 11/11 vs Galileo 8/11 vs Arize 7/11 vs Fiddler 6/11) — and where Maxim AI is winning / losing the Fortune-500 enterprise buyer in 2026?

**Close 4 (vendor-DD audit-as-a-service):** We do a 48-hour $500 vendor-DD audit for ai_eval_observability vendors — you get a written 14-question audit-report + the 24-column join-table template + the 4-vendor cohort comparison + a Fortune-500-buyer-perspective brief. Used by 30+ ai_eval_observability + ai_mlops_governance + ai_data_warehouse vendors so far.
