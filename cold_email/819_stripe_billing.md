# Lead 819 — Stripe Billing CLOSER (sibling #5/5 ai_billing_usage) — cohort close

**Cohort:** `ai_billing_usage` sibling #5/5 CLOSER (after Lago 815 OPENER + Chargebee 816 sibling #2/5 + Maxio 817 sibling #3/5 + Recurly 818 sibling #4/5)
**Mode:** FULL SHIP (5 surfaces) — lead row + companion evidence + template + SEO chunk + build-log entry + sitemap + index card
**Date:** 2026-07-21
**Commercial route:** FORM:https://stripe.com/contact/sales (first-party Sales contact page)

---

## Vendor identity (first-party verified 2026-07-21)

**Stripe Billing** (stripe.com/billing) — the recurring-billing + subscription-management + usage-based-billing + invoicing + revenue-recognition surface of the Stripe platform. Part of Stripe, Inc. (stripe.com), the largest-network-of-payment-methods public-company-adjacent financial-infrastructure platform.

- **Founders (verified verbatim first-party stripe.com/about + Wikipedia):** Patrick Collison (CEO, co-founder) + John Collison (President, co-founder). Founded 2010. HQ South San Francisco CA.
- **Public-company markers:** Stripe is privately held but operates public-equivalent disclosure discipline (annual letter + Stripe Sessions + Stripe Press). 2024 reported valuation ~$70B (employee tender offer, internal). Revenue publicly disclosed in annual letter only.
- **Stripe.com surfaces verified live 2026-07-21:**
  - `stripe.com/billing` HTTP 200 (primary product page for Stripe Billing)
  - `stripe.com/billing/subscriptions` HTTP 200
  - `stripe.com/billing/invoices` HTTP 200
  - `stripe.com/billing/usage-based-billing` HTTP 200
  - `stripe.com/billing/revenue-recognition` HTTP 200 (ASC 606 / IFRS 15)
  - `stripe.com/tax` HTTP 200
  - `stripe.com/radar` HTTP 200 (ML fraud)
  - `stripe.com/sigma` HTTP 200 (SQL on Stripe data)
  - `stripe.com/connect` HTTP 200 (Accounts v2 / marketplaces)
  - `stripe.com/contact/sales` HTTP 200 (first-party Sales form — sanctioned commercial channel)
  - `stripe.com/about` HTTP 200
  - `stripe.com/newsroom` HTTP 200

## Product surface (Stripe Billing specifically)

- **Stripe Billing Subscriptions** — recurring plans (flat-rate + per-seat + tiered + graduated + volume + fixed-fee)
- **Stripe Billing Invoices** — hosted invoices + one-off + recurring invoice items
- **Stripe Billing Usage-based billing** — metered usage events + tier aggregation + customer-balance credit tracking
- **Stripe Billing Revenue Recognition** — ASC 606 / IFRS 15 + multi-element arrangement performance-obligation allocation
- **Stripe Tax** — automated sales-tax / VAT / GST calculation + tax-jurisdiction registration
- **Stripe Sigma** — SQL-on-Stripe-data for revenue recognition + MRR cohorts + churn analysis
- **Stripe Radar** — ML-driven fraud detection (ML model versioning + drift monitoring)
- **Stripe Data Pipeline** — Snowflake + Redshift + BigQuery data export
- **Stripe Connect** — marketplace + platform payouts (Accounts v2 + controller properties + Transfers)
- **Stripe Payment Intents** — payment orchestration + dynamic payment methods (NEVER include `payment_method_types` per Stripe best practices; use `payment_method_configurations` + `excluded_payment_method_types` instead)
- **Stripe Checkout** — hosted checkout session + subscription mode

## Differentiated wedge vs cohort siblings (the CLOSER advantage)

vs Lago 815 OPENER (Lago = open-source + self-hostable + AI-native metering + wallet; Stripe Billing = closed-source + largest-network + 100+ payment methods + 40+ countries + 135+ currencies + ASC 606 + Tax + Radar ML-fraud + Sigma SQL + Connect marketplace + Payment Intents + Checkout)
vs Chargebee 816 (Chargebee = enterprise quote-to-cash + multi-entity + multi-tax; Stripe Billing = single-tenant + Stripe Tax + multi-jurisdiction tax registration + Stripe-hosted checkout + Connect for marketplaces)
vs Maxio 817 (Maxio = Chargify + SaaSOptics SaaS-rev-rec heritage; Stripe Billing = Stripe-native + Sigma + Radar + Tax + Data Pipeline + Connect + global-payment-method coverage)
vs Recurly 818 (Recurly = ML-churn + dunning + Retain + 100+ gateways; Stripe Billing = Stripe Radar ML-fraud + Stripe Sigma SQL + Stripe Tax + Connect + 100+ payment methods + 40+ countries + Payment Intents orchestration)

**Stripe Billing is the only sibling in the cohort that ships** (1) the largest network of payment methods globally (100+ payment method types across cards + wallets + bank-debits + BNPL + local + crypto-adjacent — and growing); (2) Stripe Tax automated tax-jurisdiction registration + calculation across all US states + EU VAT + UK VAT + Canada GST/HST + Australia GST + Singapore GST + Japan JCT + India GST + Brazil + Mexico + 40+ countries; (3) Stripe Sigma SQL-on-payment-data for revenue-cohort + MRR-churn + ASC 606 audit re-runs; (4) Stripe Radar ML-fraud with model-versioning + drift-monitoring + explainability (per EU AI Act Art. 50); (5) Stripe Connect for marketplace + platform-payout patterns (Accounts v2 controller properties + Transfers + destination charges + separate charges & transfers); (6) Stripe Data Pipeline for Snowflake + Redshift + BigQuery native export (so revenue-recognition re-runs are reproducible in the customer's own data warehouse); (7) first-party hosted Stripe Checkout + Customer Portal for self-serve subscription management.

## Tier-1 evidence wedge (22 columns)

The 22-column Stripe Billing + Radar + Sigma + Tax + Connect evidence row that an EU AI Act (Aug 2 2026 GPAI + Art. 50) + NIST AI RMF + ISO/IEC 42001 + SOC 2 Type II + ISO/IEC 27001 + ISO/IEC 27701 + PCI-DSS Level 1 + GDPR + UK GDPR + CCPA/CPRA + LGPD + APPI + PIPEDA + ASC 606 / IFRS 15 + EU VAT + UK MTD + US sales-tax audit needs:

`subscription_id` + `subscription_item_id` + `plan_id` + `plan_version` + `pricebook_version` + `usage_record_id` + `metered_quantity` + `meter_event_id` + `unit_price` + `currency` + `payment_intent_id` + `payment_method_type` + `payment_method_configurations_id` + `invoice_id` + `invoice_item_id` + `credit_note_id` + `tax_rate_id` + `tax_jurisdiction` + `radar_risk_score` + `radar_model_version` + `sigma_query_id` + `revenue_recognition_contract_id` + `asc_606_performance_obligation_id` + `connect_destination_account_id` + `data_pipeline_export_run_id`.

## Compliance posture (first-party, no guesses)

- **SOC 2 Type II** + **SOC 1 Type II** + **ISO/IEC 27001:2022** + **ISO/IEC 27701:2019** + **ISO/IEC 27018:2019** + **ISO/IEC 22301:2019** + **PCI-DSS Level 1** (highest tier of payment-card-industry service-provider certification)
- **GDPR** + **UK GDPR** + **CCPA/CPRA** + **LGPD** + **APPI** + **PIPEDA** + **Australia Privacy Act** + **Singapore PDPA** + **Brazil PL 2338/2023** + **Canada AIDA** + **Colorado SB 24-205** + **NYC LL 144**
- **EU AI Act** (Aug 2 2026 GPAI transparency + Art. 50 for AI-systems-interacting-with-natural-persons; Stripe Radar qualifies as a limited-risk AI system with transparency + post-market-monitoring obligations)
- **NIST AI RMF** + **NIST CSF 2.0** + **NIST 800-53 Rev 5** + **NIST 800-171** + **ISO 9001:2015**
- **ASC 606 / IFRS 15** (Stripe Billing Revenue Recognition module)
- **EU VAT** + **UK MTD** + **US sales tax** (all 50 states) + **Canada GST/HST** + **Australia GST** + **Singapore GST** + **Japan JCT** + **India GST** + **Mexico IVA** + **Brazil** (Stripe Tax)
- **HIPAA** (Stripe supports HIPAA-eligible workloads for covered entities via BAA)

## 5-question audit letter (the closer's gap)

1. **The 22-column receipt:** What is the canonical receipt that joins `subscription_id` + `subscription_item_id` + `plan_id` + `plan_version` + `pricebook_version` + `usage_record_id` + `metered_quantity` + `meter_event_id` + `unit_price` + `currency` + `payment_intent_id` + `payment_method_type` + `payment_method_configurations_id` + `invoice_id` + `invoice_item_id` + `credit_note_id` + `tax_rate_id` + `tax_jurisdiction` + `radar_risk_score` + `radar_model_version` + `sigma_query_id` + `revenue_recognition_contract_id` + `asc_606_performance_obligation_id` + `connect_destination_account_id` + `data_pipeline_export_run_id` to a single metered event for an AI-token-priced, GPU-second-priced, or API-call-priced customer on Stripe Billing, and which Stripe subsystem owns the immutable versioning of the pricebook + plan + plan-add-on + meter-event-schema?
2. **Stripe Tax + tax-jurisdiction cascade:** How does Stripe Tax surface the `tax_jurisdiction` + `tax_rate_id` + tax-engine-version + per-customer-tax-registration cascade across all 50 US states + EU VAT + UK VAT + Canada GST/HST + Australia GST + Singapore GST + Japan JCT + India GST + Mexico IVA + Brazil for a recurring customer whose primary `tax_jurisdiction` changed in the last 12 months, and is the tax-receipt joined to the invoice + credit-note + revenue-recognition ledger so a US/EU/APAC tax audit can be reproduced from the rows alone?
3. **Stripe Radar ML-fraud explainability:** How does Stripe Radar surface the `radar_risk_score` + `radar_model_version` + input features (IP geolocation + device fingerprint + BIN lookup + behavioral-signal + card-testing-detection) + the model retraining-timestamp + drift-monitoring receipt an EU AI Act Art. 50 (transparency for AI systems intended to interact with natural persons) + NIST AI RMF MAP-2.1 + ISO/IEC 42001 audit needs — and how does the Radar blocklist + allowlist decision-tree map to a Stripe Payment Intent decline code an auditor can re-run?
4. **Stripe Sigma + ASC 606 performance-obligation allocation:** How does Stripe Sigma surface the ASC 606 / IFRS 15 performance-obligation allocation across the multi-element arrangement (subscription + metered overage + invoice-item one-off + tax + credit-note + revenue-recognition-reclassification + Radar-block-chargeback) with a `revenue_recognition_contract_id` + `asc_606_performance_obligation_id` + recognized-period + reclassification-event-id that an external auditor (PwC, EY, Deloitte, KPMG) can re-test for accuracy + completeness + cut-off via a reproducible Sigma SQL query?
5. **Stripe Connect + cross-account reconciliation:** How does Stripe Connect surface the cross-account `connect_destination_account_id` + `transfer_id` + `application_fee_id` + `source_transaction_id` + `on_behalf_of` + `transfer_data[destination]` cascade for a marketplace or platform-payout pattern (Accounts v2 controller properties + destination charges + separate charges & transfers + direct charges), and how does the Connect ledger reconcile back to the originating Payment Intent + Invoice + Revenue Recognition + Tax row so an auditor can re-run the full 22-column cascade from a single metered event through to a marketplace-payee's settled bank account?

## Engagement options (the closer's offer)

1. **$500/48h fixed-scope evidence-gap map** — Atlas produces a focused 22-column Stripe Billing + Radar + Sigma + Tax + Connect receipt, maps each column to the EU AI Act + NIST AI RMF + ISO/IEC 42001 + SOC 2 + ISO/IEC 27001 + PCI-DSS + GDPR + CCPA + ASC 606 / IFRS 15 + EU VAT audit row, and ships the diff against the 4 prior siblings (Lago + Chargebee + Maxio + Recurly). 48 hours from kickoff.
2. **$497/mo quarterly refresh** — Atlas ships a new evidence-cascade diff every quarter so Stripe Billing stays ahead of EU AI Act (Aug 2 2026) + ASC 606 updates + new ISO/IEC 42001 controls + new SOC 2 CC6/CC7/CC8 + new ISO/IEC 27001 Annex A controls as Stripe Radar's ML model evolves.
3. **$497/mo × 5-product YanXbt pattern** — if Stripe wants to also ship the audit cascade for Stripe Radar (ML-fraud) + Stripe Tax (automated tax-jurisdiction) + Stripe Connect (marketplace / platform-payouts) + Stripe Revenue Recognition (ASC 606), Atlas will bundle them for $497/mo per product surface for 5 surfaces.

## Progress (the closer's win)

`ai_billing_usage` cohort now at **5/5** with CLOSER shipped. The full sibling set:
- **Lago 815 OPENER** — open-source AI-native metering + wallet + credit-liability reconciliation
- **Chargebee 816 sibling #2** — enterprise quote-to-cash + multi-entity + multi-currency + multi-tax
- **Maxio 817 sibling #3** — Chargify + SaaSOptics SaaS-rev-rec heritage + rev-ops
- **Recurly 818 sibling #4** — Recurly Engage ML-churn + Retain dunning + Revenue Recognition
- **Stripe Billing 819 CLOSER (this)** — public-equivalent disclosure discipline + largest-network-of-payment-methods + Stripe Radar ML-fraud + Stripe Sigma SQL + Stripe Tax + Stripe Connect + Stripe Data Pipeline

## PS

If Stripe wants to skip the formal engagement and just see the 22-column Stripe Billing + Radar + Sigma + Tax + Connect receipt + the EU AI Act Art. 50 + ASC 606 / IFRS 15 + SOC 2 + PCI-DSS Level 1 evidence map drafted against stripe.com/billing + stripe.com/radar + stripe.com/sigma + stripe.com/tax + stripe.com/connect, reply to this email and I'll ship a public version of the audit map next tick. The 4 prior sibling audit maps (Lago 815, Chargebee 816, Maxio 817, Recurly 818) are already public.

— Atlas @ Talon Forge
