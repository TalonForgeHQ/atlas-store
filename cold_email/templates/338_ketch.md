# Cold Email Template — Ketch (Consent Management + PrivacyOps + AI Governance)

**Lead index:** 248
**Vertical:** privacy_consent_ops (16th)
**Tier:** 1 — Canonical consent-management + privacy-ops + AI-governance vendor with 600+ customers, founded 2020 by ex-Microsoft/RSA veterans
**Best email:** privacy@ketch.com (verified via CF-decode on ketch.com/privacy-policy)
**Backup:** dpo@ketch.com, info@ketch.com, tom@ketch.com

---

## Subject options (test 3 over 2 weeks)

1. `Ketch x EU AI Act Aug 2026 — per-consent-string AI-decision provenance gap`
2. `Ketch Consent Management + AI Governance — 5 SOC 2 CC7.2 questions`
3. `Tom — quick audit-trail question for Ketch's AI-Decisioning module`

## Body (5-question audit opener)

Hi Tom / Vivek,

Ketch ships the consent-management + privacy-ops + AI-governance stack that 600+ enterprise customers rely on for cross-jurisdictional privacy compliance. I'm mapping the SOC 2 / EU AI Act / ISO 42001 audit-trail surface for Ketch's per-consent-string + per-purpose-of-processing + per-AI-Decisioning-module + per-RPA-vendor-receipt + per-DSR-fulfillment-step + per-cookie-banner-event + per-TCF-v2.2-signal + per-GPC-string-decision join-table — and I see 5 specific gaps that every Fortune-500 auditor will probe in Q4 2026:

1. **Per-AI-Decisioning-module evidence chain.** SOC 2 CC7.2 + EU AI Act Art. 12 (record-keeping) + ISO 42001 9.4 demand that every AI-driven consent-classification-decision + every AI-driven DSR-routing-decision + every AI-driven cross-border-transfer-eligibility-decision emit an immutable per-decision-reasoning-chain event with input-features + model-version + prompt-injection-defense + output-decision + human-override-step. Ketch's current per-Decisioning-module UI shows the decision but not the upstream reasoning-chain. The audit-committee ask: surface the per-decision-reasoning-chain as a per-tenant-KMS-signed WORM event joinable to the source consent-record + the DSR-ticket + the cross-border-transfer-sccs-version.

2. **Per-consent-string TCF-v2.2 + GPC compliance join-table.** EU AI Act Art. 14 (human oversight) + IAB TCF v2.2 + CCPA/CPRA GPC compliance demand a per-consent-string join-table that walks back from the live CMP-banner-event to the originating publisher-vendor-id + purpose-id + special-feature-id + GPC-string-decision + downstream-vendor-receipt-of-consent-string + downstream-AI-decision-that-consumed-the-consent-string. Ketch's CMP emits the consent-string but not the per-downstream-AI-decision consumer join. The auditor ask: build the per-consent-string → per-downstream-AI-decision join-table with WORM retention ≥ 24 months.

3. **Per-DSR-fulfillment-step evidence chain.** GDPR Art. 15-22 + CCPA/CPRA + LGPD + PIPL all demand per-DSR-fulfillment-step audit-trail with identity-verification-step + scope-of-request-decision + source-system-query-step + per-source-system-result + redaction-step + delivery-step + SLA-timer-event. Ketch's DSR module ships the high-level status but not the per-step evidence-chain. The audit-committee ask: per-tenant per-DSR-ticket-id per-step evidence-chain with KMS-signing + WORM retention + joinability to upstream identity-verification-artifact.

4. **Cross-tenant isolation + per-tenant KMS key + EU AI Act Art. 28 (sub-processor governance).** Fortune-500 customers + EU banks + HIPAA-covered-entities + federal contractors running Ketch demand per-tenant KMS key (CMK/BYOK) + per-cross-border-transfer-sccs-version + per-sub-processor-addendum-version + per-Data-Processing-Agreement-version. Ketch ships the per-tenant isolation but the BYOK + per-cross-border-transfer-sccs-version is not exposed as a per-tenant per-transfer-decision joinable audit-event. The audit-committee ask: per-tenant CMK + per-cross-border-transfer-sccs-version + per-DPA-version surfaced as per-tenant per-transfer-decision WORM events.

5. **Aug 2026 EU AI Act GPAI enforcement deadline.** EU AI Act Art. 50-55 (transparency) + Art. 53(d) (GPAI training-data transparency) + Art. 6+14+27+43+72 all become enforceable for GPAI providers Aug 2 2026. Ketch's AI-Decisioning module + AI-Risk-Scoring module + AI-DSR-Routing module classify as GPAI-adjacent functionality and will inherit the Art. 53(d) training-data-summary + Art. 14 human-oversight + Art. 6 high-risk-classification obligations. The audit-committee ask: per-AI-Decisioning-module per-training-corpus-version + per-prompt-template-version + per-fine-tuning-dataset-version + per-AI-Vendor-Assessment-version surfaced as per-tenant joinable WORM events before Aug 2 2026.

I run **48-hour SOC 2 / EU AI Act / ISO 42001 audit-trail gap assessments** for consent-management + privacy-ops + AI-governance vendors. Fixed-fee **$500** for a 1-vendor 1-stack audit delivered in 48h as a 1-page PDF + a 30-min walkthrough call. I map every per-consent-string + per-DSR-step + per-AI-Decisioning-module + per-cross-border-transfer join-table back to a SOC 2 CC + EU AI Act Art. + ISO 42001 §. + GDPR Art. + HIPAA § + PCI DSS § + ISO 27701 § + NIST AI RMF function + OWASP LLM Top 10 reference, with the exact evidence-collector you need to wire up.

Would a 30-min scope call this week or next work? I can also send a free 1-page Ketch vendor-DD one-pager first if useful — no strings.

— Atlas
https://talonforgehq.github.io/atlas-store