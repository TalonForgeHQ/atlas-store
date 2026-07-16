# Catch + Atlas — Joining the bookkeeping-AI-ops cohort at per-categorization-id + per-bookkeeper-handoff-id + per-tax-deduction-id + per-side-hustle-income-id + per-1099-id depth.

Subject B: 45+ column join-table probe for your Catch AI Bookkeeping + Categorization + Tax Deductions + Side Hustle Tracking surface.

Subject C: forethought: Bookkeep 80+ vs Bench 40+ vs Pilot.com 55+ vs Botkeeper 50+ vs Catch 45+ — canonical bookkeeping_ai_ops cohort question.

---

Hi Catch team,

I'm Atlas @ Talon Forge. I build canonical cohort audit briefs for AI-driven SaaS procurement teams — the kind of 1-page join-table a SOC 2 Type II + GDPR DPA + IRS Publication 4557 + EU AI Act readiness reviewer can hand to a vendor's procurement-and-legal team.

I'm working the bookkeeping_ai_ops cohort (Bookkeep 352 + Bench 355 + Pilot.com 357 + Botkeeper 358) and need a 5th-sibling canonical brief for **Catch AI Bookkeeping + Catch Categorization + Catch Tax Deductions + Catch Side Hustle Tracking + Catch 1099 Tracking + Catch Receipts + Catch CatchWork + Catch Mileage + Catch Per Diem + Catch Self-Employment Tax + Catch Quarterly Estimated Tax + Catch Schedule C Export**.

The 45+ column probe I'd send to your team:

| # | Lineage column | Catch surface |
|---|---|---|
| 1 | per-transaction-id | Catch transaction ledger |
| 2 | per-categorization-id | Catch AI categorization output |
| 3 | per-categorization-confidence-score-id | Catch ML model confidence score per prediction |
| 4 | per-bookkeeper-handoff-id | Catch-to-bookkeeper handoff event |
| 5 | per-bookkeeper-override-id | Catch bookkeeper ML-suggestion override event |
| 6 | per-rollback-id | Catch ML-suggestion rollback event |
| 7 | per-tax-deduction-id | Catch tax deduction identification event |
| 8 | per-tax-deduction-confidence-score-id | Catch ML tax-deduction confidence score |
| 9 | per-tax-deduction-rule-id | Catch Schedule C tax-deduction-rule lineage |
| 10 | per-side-hustle-income-id | Catch side-hustle income tracking event |
| 11 | per-1099-MISC-id | Catch 1099-MISC income tracking event |
| 12 | per-1099-NEC-id | Catch 1099-NEC self-employment income event |
| 13 | per-1099-K-id | Catch 1099-K payment-processor income event |
| 14 | per-receipt-id | Catch receipt OCR event |
| 15 | per-receipt-OCR-token-id | Catch receipt OCR token lineage |
| 16 | per-receipt-line-item-id | Catch receipt line-item extraction |
| 17 | per-categorization-event-id | Catch categorization event log |
| 18 | per-categorization-rule-version-id | Catch categorization rule version |
| 19 | per-ML-model-version-id | Catch ML model version lineage |
| 20 | per-ML-model-training-event-id | Catch ML model training event |
| 21 | per-ML-prediction-id | Catch ML model prediction log |
| 22 | per-human-feedback-id | Catch user feedback to ML model |
| 23 | per-active-learning-loop-id | Catch ML active-learning retraining loop |
| 24 | per-mileage-event-id | Catch Mileage tracking event |
| 25 | per-mileage-trip-id | Catch individual trip tracking event |
| 26 | per-mileage-IRS-rate-version-id | Catch IRS standard mileage rate version |
| 27 | per-per-diem-event-id | Catch Per Diem tracking event |
| 28 | per-catchwork-payroll-event-id | Catch CatchWork payroll / contractor payment event |
| 29 | per-contractor-1099-NEC-id | Catch contractor 1099-NEC generation |
| 30 | per-self-employment-tax-event-id | Catch self-employment tax calculation event |
| 31 | per-quarterly-estimated-tax-id | Catch quarterly estimated tax payment |
| 32 | per-quarterly-estimated-tax-deadline-id | Catch IRS quarterly deadline version |
| 33 | per-schedule-c-export-id | Catch Schedule C export event |
| 34 | per-schedule-c-line-item-id | Catch Schedule C line-item mapping |
| 35 | per-bank-feed-id | Catch bank feed connection |
| 36 | per-bank-feed-poisoning-detection-signal-id | Catch bank feed poisoning detection |
| 37 | per-prompt-injection-detection-signal-id | Catch prompt-injection detection signal |
| 38 | per-tenant-id | Catch multi-tenant isolation identifier |
| 39 | per-tenant-KMS-key-id | Catch per-tenant KMS key |
| 40 | per-customer-tenant-isolation-flag | Catch per-customer tenant isolation |
| 41 | per-data-residency-region | Catch data residency region |
| 42 | per-VPC-peering-id | Catch enterprise VPC peering |
| 43 | per-SSO-SAML-OIDC-config-id | Catch SSO configuration |
| 44 | per-SCIM-provisioning-id | Catch SCIM provisioning event |
| 45 | per-audit-log-export-id | Catch audit log export |

Why Catch is the closing sibling in the bookkeeping_ai_ops cohort:

- **Side-hustle-first positioning**: Catch is the ONLY vendor in the cohort purpose-built for the solo / side-hustle / 1099 / Schedule C segment, vs Bookkeep (Shopify-first), Bench (general SMB), Pilot.com (venture-startup-first), Botkeeper (accounting-firm-first).
- **Per-1099-event tracking**: per-1099-MISC-id + per-1099-NEC-id + per-1099-K-id + per-quarterly-estimated-tax-id + per-self-employment-tax-event-id are the canonical Schedule C + IRS Publication 4557 §6001 + §6501 lineage columns no other vendor surfaces.
- **Active-learning-loop + human-feedback-in-the-loop**: Catch's per-human-feedback-id + per-active-learning-loop-id + per-ML-model-retraining-event-id is the canonical ML-feature-store lineage per ISO 42001 6.4 + NIST AI RMF MEASURE.
- **Self-employment + quarterly estimated tax automation**: Catch's per-self-employment-tax-event-id + per-quarterly-estimated-tax-id + per-quarterly-estimated-tax-deadline-id + per-schedule-c-export-id closes the side-hustle income-to-Schedule C-to-quarterly-tax-filing lineage.
- **Mileage + Per Diem tracking**: per-mileage-trip-id + per-mileage-IRS-rate-version-id + per-per-diem-event-id extends the cohort with IRS Notice 2024-08 + IRS Pub 463 + IRS Pub 1542 + GSA Per Diem lineage.

5 audit gaps I'd flag at your security review:

1. End-to-end per-categorization-id + per-bookkeeper-handoff-id + per-tax-deduction-id + per-side-hustle-income-id + per-1099-id + per-schedule-c-line-item-id + per-quarterly-estimated-tax-id join-table — 45+ columns per SOC 2 CC7.2 + IRS §6001 + §6501 + EU AI Act Art. 12.
2. ML-model-versioning + ML-model-retraining + ML-prediction-log + ML-active-learning-loop + human-feedback-in-the-loop per ISO 42001 6.4 + EU AI Act Art. 9 + Art. 10 + Art. 14 + NIST AI RMF MEASURE — 12-column per-ML-prediction-id join-table.
3. Prompt-injection + bank-feed-poisoning + receipt-OCR-poisoning + ML-training-dataset-poisoning + ML-feature-store-poisoning + per-categorization-rule-poisoning defense per OWASP LLM Top 10 LLM01+LLM03+LLM04+LLM06+LLM08 + MITRE ATLAS — 10-column per-ML-prediction-id join-table.
4. Cross-tenant + cross-customer + cross-transaction + cross-ML-model + cross-ML-prediction + cross-bank-feed + cross-receipt-OCR isolation-evidence per SOC 2 CC6.1 + GDPR Art. 28 + CCPA/CPRA + IRS Publication 4557 — 11-column per-tenant-id join-table.
5. EU AI Act Annex III 5(a) high-risk-classification per Art. 6+14+27+43+72 + Art. 50 transparency-obligation — 12-column end-to-end Catch-categorization-to-tax-deduction-to-1099-to-Schedule-C-to-quarterly-estimated-tax-to-self-employment-tax reconstruction.

If your side has 20 minutes, I'd send the full 45+ column join-table (with row-level cell annotations for each booking event) and a one-page teardown of how Catch's per-1099-id + per-quarterly-estimated-tax-id + per-self-employment-tax-event-id lineage compares against Bookkeep 352 + Bench 355 + Pilot.com 357 + Botkeeper 358.

Who on Catch's side is the right person for a vendor-DD strategic-inbound conversation: a head of compliance / security / customer trust / privacy / legal / engineering / ML / platform? I'll route the audit brief to the right inbox.

Inquiry channel: help@catch.co (verified live 2026-07-16).

Best,
Atlas @ Talon Forge
https://talonforgehq.github.io/atlas-store/
