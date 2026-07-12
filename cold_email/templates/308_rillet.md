---
template_id: 308
target_company: Rillet
target_handle: "@rilletapp"
target_email: privacy@rillet.com
vertical: finance_ops
tier: 1
lead_index: 220
target_role: "VP Engineering / CTO / Head of AI / CISO / Head of Data"
subject: "Rillet AI-native ERP — audit-trail depth for ASC 606 + IFRS 15 + multi-entity + EU AI Act"
word_count: 247
---

**Subject:** Rillet AI-native ERP — audit-trail depth for ASC 606 + IFRS 15 + multi-entity + EU AI Act

Hi {{first_name}},

Quick question on Rillet's AI-native ledger + close + revenue-recognition stack: when your AI classifies a Stripe-Plaid-Ramp-Brex-Mercury bank-feed transaction into a GL account + reconciles it + posts the journal entry + ties out the month-end close + runs the ASC 606 SSP calculation + the 50-state Wayfair-economic-nexus sales-tax decision — what's the end-to-end reasoning-chain provenance that survives a SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 audit window?

Most AI-ledger vendors I've worked with keep AI-decision logs at a single layer (e.g. only the GL-classification decision, not the reconciliation-tie-out decision or the SSP-decision or the nexus-decision). For a Rillet customer running $50M+ ARR through the AI-ledger + multi-entity close, the auditors will want to walk from the auto-posted journal entry BACK to the source-of-truth bank-feed row, the LLM prompt + completion text, the token cost, the AI-confidence-score, the human-review-required-bit, the downstream-ERP-state-change, the Stripe-Plaid-Ramp-Brex-Mercury feed-source-of-truth-id, the ASC 606 performance-obligation-id, the IFRS 15 currency-translation-rate-id, and the multi-entity-elimination-id — in ONE query. That's the 20-column join-table.

I'd love to walk through how Rillet's existing audit-trail architecture handles the AI-Revenue-Recognition-SSP-decision + the AI-Sales-Tax-nexus-decision + the AI-close-tie-out-decision — and where you might have a gap before your first EU AI Act Annex III 4 high-risk-audit customer (any SaaS customer with EU-revenue above €15M ARR + IFRS reporting).

15 min next week? I built a short Rillet-specific audit-target-gap matrix that maps each Rillet AI-feature to the SOC 2 + EU AI Act + ISO 42001 + ASC 606 + IFRS 15 evidence-column it should produce.

— Atlas
Talon Forge LLC
atlas@talonforge.ai | https://talonforge.io

P.S. Also curious whether your AI-close engine's human-review-required-bit is per-decision (single GL-posting) or per-batch (the whole close package) — most ERPs default to per-batch which makes the regulator-trail much harder to defend.