---
template_id: 310
target_company: Plaid
target_handle: "@plaid"
target_email: privacy@plaid.com
vertical: finance_ops
tier: 1
lead_index: 222
target_role: "CISO / Head of Data / VP Engineering / Head of AI / CTO"
subject: "Plaid bank-link + AI-fraud + Liabilities — audit-trail depth for the downstream finance_ops evidence-chain"
word_count: 248
---

**Subject:** Plaid bank-link + AI-fraud + Liabilities — audit-trail depth for the downstream finance_ops evidence-chain

Hi Zack,

Quick question on Plaid's bank-link + Balance + Transactions + Identity + Auth + Liabilities + Signal + Income + Transfer + Investments product surface: when a downstream finance_ops customer (Rillet, Numeric, Ramp, Brex, Mercury, BILL, Modern Treasury, Tipalti, etc.) walks an AI-decision BACK to the underlying bank-feed-row, what's the per-row provenance Plaid exposes that survives a SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 + GLBA + FCRA + ECOA audit window?

Most bank-aggregation vendors I've audited keep the bank-link-decision log at a single layer (e.g. only the Auth-credential-exchange, not the per-transaction-source-of-truth-id or the per-fraud-score-feature-store or the per-balance-snapshot-version or the per-Identity-verification-decision or the per-Liabilities-trade-line-pull or the per-Income-payroll-provider-pull or the per-Signal-risk-decision). For a Plaid customer running $50M+ ARR through downstream-AI-close with ASC 606 + multi-entity + GAAP-flux-analysis + audit-committee-board-pack, the auditors will want to walk from the auto-posted journal entry BACK to the source-of-truth Plaid bank-feed-row, the Plaid per-item-id, the Plaid per-account-id, the Plaid per-transaction-id, the Plaid per-balance-snapshot-version, the Plaid per-fraud-score-feature-store-row, the Plaid per-Identity-verification-decision-id, the Plaid per-Liabilities-trade-line-id, the Plaid per-Income-payroll-provider-pull-id, the Plaid per-Signal-risk-decision-id, the downstream-ERP-state-change, and the close-package-bind-event-id — in ONE query. That's the 22-column join-table.

I'd love to walk through how Plaid's existing audit-trail architecture handles the per-bank-feed-row + per-fraud-score-feature-store-row + per-Liabilities-trade-line-pull — and where you might have a gap before your first EU AI Act Annex III 4 high-risk-audit customer (any SaaS-mid-market customer with EU-revenue above €15M ARR + ASC 606 + IFRS reporting).

15 min next week? I built a short Plaid-specific audit-target-gap matrix that maps each Plaid product to the SOC 2 + EU AI Act + ISO 42001 + GLBA + FCRA + ECOA + ASC 606 evidence-column it should produce.

— Atlas
Talon Forge LLC
atlas@talonforge.ai | https://talonforge.io

P.S. Also curious whether Plaid's per-row-provenance is exposed via the same `/processor/` endpoint the rest of the Transactions + Auth + Identity + Liabilities API uses — or whether audit-target customers need a separate `/audit/` endpoint — most bank-aggregation vendors split the per-row-provenance into a separate product line which makes the regulator-trail much harder to defend.