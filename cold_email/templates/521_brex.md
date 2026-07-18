# $500 / 48-Hour AI Audit — Brex (Lead 521)

**To:** privacy@brex.com (cc: dpo@brex.com — verified live 2026-07-18)
**From:** Atlas (Talon Forge)
**Subject:** Brex AI underwriting + AI expense-categorization — 5 audit gaps before Aug 2 2026

---

Hi Brex privacy team,

Henrique + Pedro's "AI-powered spend platform" now reaches tens of thousands of corporate-card
customers + their AP/AR teams + their controllers, and your AI underwriting decisions + AI GL
coding + AI expense categorization each touch $$B+ in annual throughput per customer. That's
why your customers' GRC teams + their EU regulators (EU AI Act Art. 6 + 14 + 50, Annex III 4) +
their CCPA/CPRA regulators + their SOC 2 CC7.2 + their PCI DSS 4.0 + their NACHA auditors will
all ask the same five provenance questions on the next 12-state AI-disclosure + the next
regulatory exam:

**Five gaps your team will be asked about on the next procurement-DD / SOC 2 Type II / ISO 42001
surveillance audit + the next EU AI Act Art. 14 human-oversight review:**

1. **End-to-end per-Brex-tenant-id -> per-cardholder -> per-AI-expense-categorization-id -> per-AI-receipt-extraction-id -> per-AI-GL-code-suggestion-id -> per-AI-bill-pay-approval-id -> per-AI-vendor-risk-score-id -> per-AI-underwriting-decision-id -> per-audit-log-entry-id provenance join-table** per SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 + ISO 27701 + GDPR Art. 22 + Schrems II + PCI DSS 4.0 + 12-state AI-disclosure. (Critical for a platform at your throughput.)
2. **AI underwriting + AI GL coding + AI expense categorization + AI receipt-extraction + AI vendor-risk-scoring training-corpus + fine-tune-license-provenance** per EU AI Act Art. 53(1)(b) GPAI training-data transparency + Art. 53(1)(d) copyright-summary + ISO 42001 6.1.4. (Brex corpus spans per-cardholder-transaction-history + per-vendor-history + per-cardholder-receipt-corpus + per-cardholder-LOB-history — canonical EU AI Act Aug 2 2026 GPAI documentation target.)
3. **Prompt-injection + AI receipt-extraction-poisoning + AI GL-coding-poisoning + AI vendor-risk-poisoning + AI underwriting-poisoning + per-tenant-prompt-injection + Brex-cardholder-self-promotion-bypass + Stripe-fraud-bypass + NACHA-bypass defense** per OWASP LLM Top 10 LLM01+LLM03+LLM06+LLM08 + MITRE ATLAS + EU AI Act Art. 14 human-oversight + Art. 50 transparency-obligation + 12-state AI-disclosure + Schrems II SCC. (Reaches every Brex cardholder + every Brex AP/AR team.)
4. **Cross-Brex-tenant + per-cardholder + per-cardholder-account + per-Brex-KMS-key-id + CMK/BYOK + per-Brex-AI-inference-endpoint + per-Brex-AI-training-pipeline + cross-border-data-residency-isolation** per SOC 2 CC6.1 + GDPR Art. 28 + Schrems II + FTC Safeguards Rule + ISO 27701. (Tens of thousands of tenants + their employees + their spend data, each in their own residency region.)
5. **WORM retention + cost-attribution join-table linking per-AI-underwriting-cost + per-AI-expense-categorization-cost + per-AI-GL-coding-cost + per-AI-receipt-extraction-cost + per-AI-bill-pay-approval-cost + per-AI-vendor-risk-cost + per-AI-forecasting-cost + per-Brex-tenant-cost + per-audit-log-entry-cost** per SOC 2 CC7.2 + EU AI Act Art. 12 + SEC 17a-4 WORM + PCI DSS 4.0 + NACHA retention + Schrems II + 12-state AI-disclosure + cross-border-data-residency-retention.

**The 48-hour audit deliverable: a fixed-scope artifact** ($500, 48-hour delivery) covering
training-to-inference provenance, model and corpus supply chain, hostile workload input, tenant/
secret/KMS/GPU isolation, rollback, deletion, WORM evidence, and per-run cost attribution —
mapped 1:1 to the EU AI Act Aug 2 2026 GPAI enforcement + the SOC 2 Type II evidence
requirements + the PCI DSS 4.0 audit-trail requirements + the 12-state AI-disclosure requirements.

Reply PRIVACY only — no shared air-gapped deliverable. No browser session, no third-party
processor on the audit lane. Single fixed-price $500. 48 hours from reply to document.

— Atlas
Talon Forge LLC (verified @TalonForgeHQ on X, 6 followers, real revenue)

---
