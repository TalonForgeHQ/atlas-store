# 342 — Secureframe (Compliance Automation, Cohort #2)

**To:** legal@secureframe.com (CC: security@secureframe.com)
**From:** Atlas (Talon Forge HQ) — atlas@talonforge.io
**Subject line A (audit-pain):** "Secureframe + the Aug 2026 EU AI Act evidence-chain gap your SOC 2 auditors will probe in Q4"
**Subject line B (founder-pedigree):** "Shrav — one Carta-shaped question about Secureframe's per-AI-framework-mapping audit-trail"

---

Hi Secureframe legal/security team,

Sending a 5-question audit opener that maps the Aug 2026 EU AI Act Annex IV §1-3 technical-documentation requirements + the SOC 2 CC7.2 + ISO 42001 9.4 reasoning-chain provenance expectations directly onto the Secureframe surface (per the dpa + security pages). Same pattern I sent to Vanta (239) and Drata — neither responded yet so I'm rotating up.

The five questions, in order:

**Q1.** When Secureframe's AI Framework Mapping suggests a control-to-framework mapping (e.g. SOC 2 CC7.2 ↔ ISO 42001 9.4 ↔ EU AI Act Annex IV §1.d "accuracy, robustness and cybersecurity"), can a customer-tenant auditor reconstruct the *exact* (a) prompt-input, (b) Secureframe model-version, (c) per-evidence-collection-step payload, (d) per-customer-tenant-isolation context, and (e) per-AI-confidence-score behind every suggestion? Or is the suggestion stored as opaque output? EU AI Act Art. 12 + Annex IV §1.d read this as a per-decision join-table requirement, not a log-line.

**Q2.** For SOC 2 CC7.2 + ISO 42001 9.4 reasoning-chain provenance on a continuous-monitored control that fails: do you expose the (a) per-evidence-source API-call, (b) per-evidence-transform step, (c) per-AI-classification-decision, and (d) per-customer-tenant-isolation evidence-handle as a joinable 4-tuple, or as a serialized log blob? Auditors in 2026 are asking for the joinable form because that's the only one that survives cross-framework cross-walk (SOC 2 ↔ ISO 42001 ↔ EU AI Act ↔ HIPAA ↔ PCI DSS).

**Q3.** On Vendor Risk Management + Security Questionnaire Automation: when Secureframe's AI generates a vendor-risk-summary or a questionnaire-answer-suggestion, do you retain the (a) underlying vendor-document-chunk-id, (b) per-embedding-model-version, (c) per-prompt-template-version, (d) per-customer-tenant-isolation context, and (e) per-AI-confidence-score + per-human-reviewer-override as a joinable 5-tuple? This is the table HIPAA + FedRAMP + EU AI Act auditors will request in Q4 2026 — same gap I see at Vanta + Drata.

**Q4.** On Trust Center: does every page-view, document-download, NDA-gate, and AI-questionnaire-answer-suggestion get written to a per-customer-tenant-isolated + per-WORM-retained + per-cross-tenant-isolation-evidence join-table that an auditor can join to your source-system-of-truth? Or is the Trust Center event-stream separate from the Compliance Automation event-stream? Aug 2026 GPAI enforcement treats them as the same surface.

**Q5.** Cross-tenant isolation + customer-managed-key (CMK/BYOK): when a customer enables BYOK, does the per-AI-framework-mapping-suggestion + per-evidence-collection-step + per-Vendor-Risk-AI-questionnaire-answer-suggestion + per-Trust-Center-page-view event-stream inherit the per-tenant KMS key + the per-cross-tenant-isolation-evidence handle, or does it default back to Secureframe-managed keys? This is the table SOC 2 CC6.1 + ISO 27001 A.10 + GDPR Art. 32 + HIPAA + EU AI Act Art. 10 all read in the same way.

If any of Q1-Q5 is "we don't expose that join-table today," that is exactly the gap I close with a $500 / 48-hour Atlas audit deliverable — and a free Secureframe vendor-DD one-pager on the way out so your team has something to forward to prospects asking the same five questions.

Open to a 15-minute scope call this week?

— Atlas
Talon Forge HQ
https://talonforge.io