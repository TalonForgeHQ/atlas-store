# Weights & Biases (Lead 321) — Tier-1 ai_mlops_governance 5th-sibling

## Lead Facts (verified 2026-07-16)
- **Company:** Weights & Biases (W&B)
- **Domain:** wandb.ai (also wandb.com)
- **Verified contact:** privacy@wandb.com (canonical mailto exposed at /site/privacy HTTP 200)
- **Additional channels:** security@wandb.com; support@wandb.com; dpo@wandb.com
- **Vertical:** ai_mlops_governance
- **Tier:** 1
- **Handle:** @weights_biases
- **Cohort:** ai_mlops_governance 5th-sibling (after Domino 320 + Dataiku 318 + Neptune-pre + Domino-pre)

## Why W&B
W&B is the experiment-tracking and model-registry platform with the widest adoption in the cohort: 1M+ ML practitioners, used by OpenAI/Anthropic/Meta/DeepMind/Microsoft for production sweep + artifact lineage + W&B Prompts + W&B Traces + Weave traces. For an AI/ML governance audit, the surface creates concrete audit gaps no other vendor covers in one place — per-run-version-id immutable WORM, per-prompt-template-version-id (W&B Prompts), per-trace-id + per-span-id (W&B Traces + Weave), per-evaluation-id + per-ground-truth-id (W&B Tables + human-review-link), per-deployment-region artifacts.

## Pitch Angle (3 lines, strategic-inbound)
1. Lead with the audit gap they care about most: **end-to-end reasoning-chain provenance for every W&B Sweep + W&B Run + W&B Artifact + W&B Prompts version** — per-run-id → per-run-version-id → per-artifact-version-id → per-prompt-template-version-id → per-trace-id → per-evaluation-id in a single WORM-archived join-table.
2. Show you've read their privacy page: cite the canonical mailto and the explicit GDPR Art. 28 / CCPA / SOC 2 / HIPAA BAA / EU AI Act surface.
3. Offer a 20-min audit — point to the 5-gaps map (per-prompt-template-version-id / per-trace-id / per-evaluation-id / WORM retention on artifacts / cross-deployment-region isolation).

## Audit Gap Map (5 gaps, in Mermaid-style ASCII)
- **Gap 1 — Reasoning-chain provenance join-table:** per-run-id + per-run-version-id + per-artifact-version-id + per-prompt-template-version-id + per-trace-id + per-evaluation-id for HIPAA + SOC 2 CC7.2 + EU AI Act Art. 14 + NIST AI RMF MEASURE + OWASP ML Top 10.
- **Gap 2 — Per-evaluation-id + per-ground-truth-id + per-human-review-id layer.** W&B Tables + W&B Artifacts ground-truth-versioning creates the only canonical human-review-link in the experiment-tracking surface.
- **Gap 3 — Per-trace-id + per-span-id + per-prompt-template-version-id lineage edge-id (W&B Traces + Weave + W&B Prompts).** The only production LLM-trace surface in the experiment-tracking layer paired with prompt-template versioning.
- **Gap 4 — Cross-tenant isolation:** per-tenant-id + per-deployment-region + per-billing-account-id per SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + FedRAMP Moderate + W&B Dedicated (single-tenant).
- **Gap 5 — WORM retention:** 13-year archive per GDPR Art. 17 deletion-propagation + EU AI Act Annex III + Aug 2026 GPAI enforcement + W&B Artifacts content-addressed storage.

## Footer / P.S.
- P.S. 1 — If we miss, info@wandb.com routes to the partnerships team who tracks strategic-inbound audit-tier inquiries.
- P.S. 2 — I can include a free 5-vendor ai_mlops_governance compliance-overlap map (Domino 320 + Dataiku 318 + W&B 321 + Neptune-pre + Domino-pre) on the 20-min call.
- P.S. 3 — W&B's HIPAA BAA + ISO 27001 + SOC 2 Type II is a 14-day SOC 2 CC7.2 evidence-collection walk; we can run it asynchronously with your security team.
- P.S. 4 — Lukas Biewald + Chris Van Pelt + Shawn Lewis (all ex-CrowdFlower) and Coatue + Index + Insight + Salesforce Ventures + $250M Series E at $4B valuation — your board materials belong in the audit binder too.
