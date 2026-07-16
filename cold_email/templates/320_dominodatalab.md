# Domino Data Lab (Lead 320) — Tier-1 ai_mlops_governance 4th-sibling

## Lead Facts (verified 2026-07-16)
- **Company:** Domino Data Lab
- **Domain:** dominodatalab.com
- **Verified contact:** privacy@dominodatalab.com (canonical mailto exposed at /privacy-policy HTTP 200)
- **Vertical:** ai_mlops_governance
- **Tier:** 1
- **Handle:** @dominodatalab
- **Cohort:** ai_mlops_governance 4th-sibling (after Dataiku 318 + Domino 318-pre + Neptune 318-pre)

## Why Domino
Domino is the enterprise MLOps platform with the deepest single-tenant isolation story in the cohort: a dedicated compute grid per workspace, per-project reproducible environments, and per-model-version + per-run-id lineage all rolled up to a single per-tenant-id. For an AI/ML governance audit, that stack creates concrete audit gaps that almost no other vendor covers in one place — model-bias-audit-id, feature-store-lineage-id, WORM retention on artifacts, and cross-region deployment-region isolation.

## Pitch Angle (3 lines, strategic-inbound)
1. Lead with the audit gap they care about most: **end-to-end reasoning-chain provenance for every Domino deployment** — per-model-id → per-model-version-id → per-run-id → per-prompt-template-version-id → per-prediction-id in a single WORM-archived join-table.
2. Show you've read their privacy page: cite the canonical mailto and the explicit GDPR Art. 28 / CCPA / SOC 2 surface.
3. Offer a 20-min audit — point to the 5-gaps map (per-model-bias-audit / per-feature-store-lineage / per-deployment-region isolation / WORM retention / per-artifact-version license-provenance).

## Audit Gap Map (5 gaps, in Mermaid-style ASCII)
- **Gap 1 — Reasoning-chain provenance join-table:** per-model-id + per-model-version-id + per-run-id + per-prompt-template-version-id + per-prediction-id for HIPAA + SOC 2 CC7.2 + EU AI Act Art. 14 + NIST AI RMF MEASURE.
- **Gap 2 — Per-model-bias-audit-id + per-explainability-record-id layer.** No other ai_mlops_governance sibling exposes this as a first-class join key.
- **Gap 3 — Feature Store lineage edge-id (Domino Feature Store).** Per-feature-id + per-feature-version-id + per-feature-store-version-id layered on top of the model registry.
- **Gap 4 — Cross-tenant isolation:** per-tenant-id + per-deployment-region + per-billing-account-id per SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + FedRAMP Moderate.
- **Gap 5 — WORM retention:** 13-year archive per GDPR Art. 17 deletion-propagation + EU AI Act Annex III + Aug 2026 GPAI enforcement.

## Compliance Cross-Walk (highlighted rows)
| Framework | Article / Control | Domino-specific surface |
|---|---|---|
| SOC 2 Type II | CC6.1 / CC7.2 / CC7.3 | per-tenant-id + per-deployment-region + per-run-id |
| GDPR Art. 28 | processor obligations | privacy@dominodatalab.com (canonical DPA channel) |
| EU AI Act | Art. 9 / 10 / 12 / 14 / 50 | per-model-version-id + per-prediction-id |
| ISO 27001 / 27701 | A.8 / A.18 / PIMS | per-deployment-region |
| HIPAA | §164.312(b) | per-run-id + per-artifact-id |
| FedRAMP Moderate | SC-7 / AU-2 / AU-12 | per-tenant-id isolation |
| NIST AI RMF | MEASURE / MANAGE | per-model-bias-audit-id |
| OWASP ML Top 10 | all 10 | per-feature-id + per-feature-store-version-id |
| MITRE ATLAS | model supply chain | per-artifact-id + per-prompt-template-version-id |

## Subject Line Options (A/B/C)
- A) "Domino deployment-region audit — 5 gaps to close before Aug 2026 GPAI enforcement"
- B) "privacy@… — quick 20-min check on Domino Art. 28 reasoning-chain provenance"
- C) "5 audit gaps in your ai_mlops_governance stack (per-model-bias-audit + feature-store lineage)"

## CTA
20-min audit. No deck. Three concrete reasoning-chain evidence artifacts pulled live from your stack, so you can take them straight into your next quarterly audit review.
