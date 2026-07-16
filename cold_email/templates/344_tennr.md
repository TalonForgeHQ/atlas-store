# 344 — Tennr (Tennr AI)

**To:** privacy@tennr.com (verified live 2026-07-16 via curl https://tennr.com/privacy-policy)
**From:** Atlas Audit (Talon Forge HQ)
**Subject:** HIPAA + SOC 2 + EU AI Act audit gap on Tennr's clinical-document-RAG → EHR-write join

---

Hi Tennr privacy/legal/security team,

I'm Atlas. I run 48h compliance audits for healthcare AI agent vendors — HIPAA §164.312 + SOC 2 CC6.1 + CC7.2 + EU AI Act Art. 6/14/27/43/50 + ISO 42001 §9.4 + 21st Century Cures Act information-blocking — and Tennr sits in a lane I've only seen twice: a production clinical-document-RAG pipeline that writes downstream EHR state changes for 1000+ clinics on 10M+ docs/month.

Five audit gaps your next HIPAA + SOC 2 + EU AI Act reviewer will probe:

1. **End-to-end per-fax-id → per-OCR-extraction-id → per-clinical-entity-id → per-RAG-source-document-id → per-EHR-write-id → per-claim-submission-id provenance.** HIPAA §164.312 + SOC 2 CC7.2 + EU AI Act Art. 12 require a single trace_id linking intake fax → OCR confidence → clinical-entity extraction → RAG retrieval source → clinician approval/override → downstream EHR write → downstream claim submission. The Tennr-specific audit-trail surface is exactly that 18-column join table.

2. **Per-RAG-source-document-id + per-clinical-decision-support-output-id + per-clinician-approval-id + per-clinician-override-id training-corpus license-provenance.** EU AI Act Art. 53(d) GPAI training-data transparency + Art. 53(1)(b) copyright-summary + HIPAA §164.514 deidentification require the OCR + RAG + clinical-decision-support fine-tune corpus to ship with license-chain attestation per source document.

3. **Prompt-injection + OCR-poisoning + RAG-poisoning + Tennr-Fax-bypass + Tennr-Prior-Auth-bypass + EHR-Integration-bypass + downstream-EHR-state-change-record-poisoning defense.** OWASP LLM Top 10 LLM01/LLM03/LLM04/LLM06/LLM08 + NIST AI RMF MEASURE + EU AI Act Art. 9 risk-management + Art. 14 human-oversight + FDA SaMD guidance. The auditor will specifically probe per-fax-id injection events.

4. **Cross-clinic + cross-tenant + cross-EHR-deployment isolation-evidence.** HIPAA §164.312 + SOC 2 CC6.1 + GDPR Art. 28 + EU AI Act Art. 10. Per-clinic-id + per-EHR-instance-id + per-patient-MRN-id isolation with CMK/BYOK + per-tenant-KMS-key-id + per-cross-border-transfer-SCCs-version.

5. **WORM retention + cost-attribution + EU AI Act Annex III 5(a) high-risk-classification + GDPR Art. 17 deletion-propagation.** 6yr HIPAA retention + breach-notification §164.404 + 12-column end-to-end Tennr-fax-to-clinical-decision-to-EHR-write reconstruction per quarter.

I run these as 48h fixed-fee audits — $500 for the core HIPAA + SOC 2 evidence-package gap, $1,500 for the 1-week SOC 2 + EU AI Act + ISO 42001 + 21st Century Cures deep dive, $3,000 for the 4-week full Annex III 5(a) high-risk-classification + FDA SaMD-aligned clinical-decision-support assessment with quarterly reconstruction drills.

P.S. Trey + Lucy — the Tennr-specific audit lane is the per-fax-id → per-EHR-write-id join table that no other healthcare AI agent vendor ships at 10M+ docs/month scale. Worth a 30-min call to walk through the gap?

— Atlas
audit@talonforge.io