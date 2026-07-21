# Template 816 — Chargebee (ai_billing_usage sibling #2/5)

**Commercial route:** `FORM:https://www.chargebee.com/schedule-a-demo/` (first-party Schedule a Demo page verified HTTP 200 with verbatim title "Get a demo of Chargebee's Recurring Billing Platform Today" + Marketo form `mktoForm_9` on 2026-07-21; not submitted).
**Founders:** Krish Subramanian, CEO & Co-founder; Rajaraman Santhanam, CPO & Co-founder; Saravanan KP, CTO & Co-founder (verified verbatim first-party `chargebee.com/company` 2026-07-21).
**Current exec roster:** Jeff Sant COO + Mike Beach CFO + Lydia Stone CAO + Guy Marion CMO + Denis Curran CLO + Denise Haselhorst CHRO.
**Restricted route excluded:** no security@, privacy@, or support@ inbox was used as the commercial route.

## Three subject-line A/B/C variants

**Subject A — audit-letter opener:** Krish / Rajaraman / Saravanan — 5 evidence gaps between Chargebee quotes, pricebook versions, and ASC 606 revenue-recognition periods

**Subject B — regulation-anchored:** Chargebee's 19-column quote-to-cash receipt for SOC 2 + ISO 27001 + ASC 606/IFRS 15 + EU AI Act Art. 50 evidence support

**Subject C — peer-pressure:** Chargebee + Lago + Maxio + Recurly: which subscription-billing platform can replay one quote version into the exact invoice line and ASC 606 performance-obligation allocation?

## 5-question audit-letter opener

Krish / Rajaraman / Saravanan — Talon Forge is extending its `ai_billing_usage` audit cohort past the Lago 815 OPENER and needs the enterprise quote-to-cash half of the audit surface from Chargebee. The buyer-side procurement question: can a buyer replay any sold subscription from raw quote through product-catalog version, plan version, pricebook version, currency conversion, tax engine, usage event, invoice, credit note, dunning, and ASC 606 revenue-recognition allocation without a spreadsheet?

1. **What is the quote-to-cash event chain?** For every quote, contract, subscription, plan change, and renewal, what is the immutable receipt joining `quote_id`, `quote_version`, customer, product-catalog version, plan id, plan version, pricebook version, currency-conversion timestamp, fx-rate source, tax-engine version, and tax jurisdiction?
2. **What is the usage-event-to-invoice evidence chain?** When a customer switches from flat subscription to usage-based or hybrid (usage + flat + committed + overage), what is the per-event lineage joining metered event id, plan id, plan version, aggregation window, unit price, currency, tax jurisdiction, and the final invoice line that absorbed the event?
3. **What is the pricebook and plan-version evidence chain?** When a SaaS buyer changes a tier, ramp, percentage, volume, tiered, stairstep, or commitment-discount rule, what is the effective-dated plan version and the approval trail that proves which rule rated each invoice line and credit note?
4. **What is the ASC 606 / IFRS 15 revenue-recognition evidence chain?** What joins each invoice line to its revenue-recognition contract id, performance obligation id, allocation percentage, recognized period, deferred period, and refund-credit-note reclassification when the contract is amended mid-period?
5. **What is the multi-entity, multi-currency, multi-tax-jurisdiction evidence chain?** Across Chargebee's US + EU + UK + CA + AU + IN + SG + ZA + JP subsidiaries and tax engines (Avalara / Vertex / Stripe Tax / TaxJar), what is the per-customer per-period reconciliation report that links one invoice line to its booking-entity, settlement-entity, tax-jurisdiction, fx-rate source, and remittance-trail?

## Body (~480 words)

Chargebee's public product surface is the enterprise-anchor end of the subscription-and-usage-billing market: Recurring Billing, Subscription, Usage Billing, Billing for SaaS, Retain, Recover, Billing Workflow Studio, CPQ, Revenue Recognition, and the Chargebee 2.0 platform. The buyer-side risk is not feature coverage. It is proving that every invoice line, credit note, and revenue-recognition allocation is reproducible after a plan, pricebook, currency, tax-jurisdiction, or contract-amendment change — across multiple entities and ASC 606 performance obligations.

We package that proof as a fixed-scope **19-column quote-to-cash receipt**: quote id, quote version, customer id, product-catalog version, plan id, plan version, pricebook version, currency-conversion timestamp, fx-rate source, tax-engine version, tax jurisdiction, usage event id, metered quantity, invoice id, invoice line id, credit note id, dunning state, revenue-recognition contract id, and revenue-recognition period, with a per-period ASC 606 performance-obligation allocation pin.

**Prior sibling in this cohort:** Lago 815 (getlago.com) owns the open-source, AI-native usage-metering + billing wallet + credit-liability lane. **Chargebee 816 fills the gap that Lago does not ship:** enterprise quote-to-cash, multi-entity / multi-currency / multi-tax-jurisdiction, ASC 606 / IFRS 15 revenue recognition, CPQ, contract amendments mid-period, and the SaaS-buyer enterprise-anchor commercial surface. **Planned next siblings:** Maxio 817 (SaaSOptics + Maxio revenue-recognition specialization), Recurly 818 (subscriber-lifecycle + churn-management lane), Stripe Billing 819 (platform-anchor + parent-Stripe control-plane inheritance). Together the five siblings cover open-source metering, enterprise quote-to-cash, dedicated revenue-recognition, subscriber-lifecycle, and platform-anchor.

We are not asking for a free trial. We are asking for one 48-hour scoping call where Chargebee's enterprise solutions-engineering team hands Talon Forge (a) one anonymized multi-entity quote, (b) one amended contract with mid-period pricebook change, (c) one credit-note-with-reclassification event, and (d) one ASC 606 performance-obligation allocation report. We then return a 14-page evidence-gap map that an enterprise SaaS buyer's CISO, CFO, and RevOps can use to shortlist Chargebee against Maxio + Recurly + Stripe Billing in a single procurement cycle.

## Three engagement options

1. **$500 / 48h fixed-scope** — one chargebee.com evidence-gap map, one Maxio + Recurly + Stripe Billing peer comparison, one prioritized remediation queue.
2. **$497 / mo quarterly refresh** — per-quarter evidence-map refresh + per-chargebee.com release-note audit + per-incident post-mortem.
3. **$497 / mo × 5-client YanXbt pattern** — five Chargebee enterprise buyers × $497/mo recurring evidence-map retainer (verifiable: chargebee.com/customers page + chargebee.com/case-studies).

## PS

If you would like the audit gap-map shape pre-populated for your next SOC 2 Type II surveillance window or ASC 606 year-end close, reply to this email and I will share a redacted sample.
