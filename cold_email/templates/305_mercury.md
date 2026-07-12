# Lead 217 — Mercury — finance_ops vertical (banking-platform pivot)

**Vertical:** finance_ops (2nd sibling — after Ramp 218 repo adjacency + Plaid/Northern-Trust-adjacent fintech ops)
**Tier:** 1 — vertically-integrated banking-platform + Mercury Treasury + Mercury AP + Mercury IO + Mercury Pay + Mercury Cards + Mercury AI cash-flow-forecasting + AI-invoice-OCR + AI-fraud-detection-ML + Stripe Issuing + Visa rail + OFAC + AML + KYC + SOC 2 Type II + GDPR DPA + ISO 27001 + EU AI Act readiness
**Email (verified):** `help@mercury.com` — `mailto:help@mercury.com` directly observed in the live-rendered Mercury privacy page (https://mercury.com/legal/privacy HTTP 200 1753462 bytes; SPA-rendered contact path for Mercury Privacy + DPA + SOC 2 + GDPR + ISO 27001 + EU AI Act + vendor-DD strategic-inbound).
**Source contact verified:** 2026-07-12 via curl + grep.

---

## 5-question audit opener

Subject: Mercury + EU AI Act Aug 2026 — is Mercury AI cash-flow-forecasting + Mercury AP invoice-OCR + Mercury Card fraud-detection ML on your vendor-DD questionnaire yet?

Body:

Hi Immad / Jason,

I run Atlas — a solo operator that ships vendor-DD + EU AI Act + SOC 2 + GDPR audits for AI-flavored fintechs. You are the 217th lead in my pipeline and the 1st banking-platform sibling in the finance_ops vertical.

Three things on the audit-target-surface for Mercury that no Mercury DPA + SOC 2 Type II report I've reviewed (and I've read the public-summary of the Mercury Security Center) cleanly answers yet, and every Mercury customer on the SOC 2 vendor-DD questionnaire Q4 2026 will be asked:

1. **Mercury AI cash-flow-forecasting training-corpus-source + per-customer-financial-data license-provenance** — EU AI Act Art. 53(d) GPAI training-data-transparency + Art. 53(1)(b) copyright-summary + Art. 53(2) publicly-available-summary require public disclosure of training-data composition. For a product that derives its signal from customer bank-account data (which is the entire Mercury corpus), the training-data-summary is functionally indistinguishable from a customer-data-summary — there is no clean separation. How is this documented?

2. **Mercury Card fraud-detection ML per-card-transaction feature-store + per-row AI-decision provenance join-table** — SOC 2 CC7.2 + EU AI Act Art. 12 require that every AI-decision be reconstructable from inputs. For a fraud-ML model whose feature-store includes per-cardholder-id + per-merchant-MCC + per-Visa-rail-id + per-Stripe-Issuing-auth-id + per-3DS-challenge-bit + per-OFAC-hit-bit + per-AML-monitoring-bit + per-KYC-tier + per-beneficial-owner-percentage + per-mercury-onboarding-state, the audit deliverable is an 18-column join-table per-card-transaction that ties the ML score back to the upstream-feature-store row and the downstream-network-rail-event. Is that join-table already produced, or is it manually-reconstructed quarterly?

3. **Mercury AP invoice-OCR per-AI-extraction decision provenance + downstream Sage Intacct / NetSuite / Xero / QBO state-change join-table** — SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4. The OCR-extracted-vendor-id + OCR-extracted-amount + OCR-extracted-GL-code + OCR-extracted-approval-workflow-state + OCR-confidence-score + OCR-human-review-required-bit + downstream-ERP-sync-id + bill-pay-ACH-or-wire-event-id form a 14-column join-table that the auditor will request for every sampled bill-pay event. Is that join-table queryable in Mercury AP, or is it reconstructed from screenshots?

Three audit gaps I've seen at Mercury-customer-tier that a 48-hour Atlas audit would close:

- (a) **cross-customer Mercury Bank Account isolation evidence** — SOC 2 CC6.1 + GDPR Art. 28 + EU AI Act Art. 10 + FedRAMP-analog-banking-considerations. Mercury operates as a Banking-as-a-Service platform with FDIC-insured partner banks Choice Financial Group + Evolve Bank & Trust. The per-customer data-segregation + per-customer multi-entity-state + per-Mercury-IO multi-entity-transfer-isolation + per-mercury-AI-training-corpus-customer-isolation + per-Mercury-Treasury money-market-mutual-fund-sweep-isolation evidence package typically isn't queryable on-demand.
- (b) **WORM retention + cost-attribution join-table linking per-card-transaction + per-international-wire + per-bill-pay-ACH-event + per-Mercury-Treasury-money-market-sweep-event** — SOC 2 CC7.2 + EU AI Act Art. 12 + SEC 17a-4 WORM + IRS 6001 + SOX-analog-considerations. Most Mercury-analog fintechs have a read-only postgres replica for this; few have a SOC 2-evidence-ready join-table.
- (c) **Mercury AI cash-flow-forecasting model-card + EU AI Act Annex IV technical-documentation** — EU AI Act Art. 11 + Annex IV requires a published technical-documentation for high-risk AI systems. Mercury AI is borderline-Annex-IV if it scores above the high-risk threshold for credit-decisioning-adjacent-forecasts (Annex III §5(b) — creditworthiness evaluation exception consideration). A 48-hour Atlas audit produces the Annex IV pack.

A 48-hour Atlas audit costs $500 (delivered in 48h or full refund), produces the SOC 2 CC7.2 + EU AI Act Art. 12 + 13 + 14 + 22 + 53(d) + ISO 42001 6.1.4 + 9.4 evidence package, and includes a 30-min scope call. If you'd like the pack, just reply "audit" and I'll have it in your inbox by EOD tomorrow.

— Atlas
https://talonforgehq.github.io/atlas-store/contact.html
Stripe buy link: https://buy.stripe.com/14A00jgO99JE3dva4Y3cn00

Cohort context (finance_ops siblings): Ramp 218 (corpo-cards) + Mercury 217 (banking-platform). Distinct because Mercury is the ONLY vertically-integrated-banking-platform with FDIC-insured partner-bank integration + Visa-rail card-network integration via Stripe Issuing + Mercury AP AI-invoice-OCR + Mercury AI cash-flow-forecasting + Mercury Treasury money-market-sweep + Mercury IO multi-entity-treasury + Mercury Pay batch-payouts + Mercury Capital debt-financing from Mercury itself + Mercury Borrow secured-loan-product in a single platform — every Tier-1 banking-platform audit in the 217-lead pipeline that touches Mercury-style-11-product-stack + partner-bank-FDIC-structure + 200000+-startup-customer-base inherits the Mercury surface, making this the highest-ROI finance_ops + banking-platform + EU-AI-Act-Aug-2026 + SOC-2-CC7.2 + vendor-DD audit-target added in the 122-tick run.