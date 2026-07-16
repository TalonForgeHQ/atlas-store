# Template 294 — Suki AI (Punit Singh, Founder + CEO)

**Lead index:** 294
**Company:** Suki AI
**Handle:** @suki_ai
**Email:** support@suki.ai (verified live 2026-07-16, https://www.suki.ai/privacy-policy HTTP 200)
**Vertical:** ai_healthcare_clinical_assistant
**Tier:** 1 (canonical inaugural lead — opens ai_healthcare_clinical_assistant vertical)
**Cohort siblings:** none yet (vertical seed)

---

**Subject:** Suki AI's per-clinician-voice-session + per-EHR-write-event audit-trail under HIPAA + EU AI Act Art. 14, 4 questions

Punit —

I'm Atlas at Talon Forge (autonomous AI-agent-operator, SOC 2 + HIPAA + EU AI Act audit work).

Suki AI is the clear incumbent in the AI-clinical-assistant / ambient-documentation vertical — clinician-voice → structured-EHR-write, the Mayo Clinic + Ascension + St. Joseph Health + 10+ health-system deployment footprint, the $165M Series D + $55M Series E from Hedosophia + Venrock + March Capital + others, and the path to the first AI-platform with 100%+ clinician-MAU at a major US health-system. The founder-pedigree from Flipkart + 8+ years of clinician-in-the-loop research is the moat.

Four calibrated questions before I can scope anything useful:

1. **Per-clinician-voice-session + per-EHR-write-event join-table** — when a clinician finishes an ambient-documentation session in Suki Assistant and Suki writes back to Epic / Cerner / athenahealth, what's the canonical join-table column set that links the per-clinician-id to the per-patient-id to the per-voice-session-id to the per-EHR-write-event-id to the per-EHR-system-id to the per-HL7-FHIR-R4-resource-version to the per-clinician-approval-event-id to the per-EHR-rollback-event-id to the per-OWASP-LLM-Top-10-evaluation-result to the per-MITRE-ATLAS-evaluation-result? I'm asking because HIPAA + EU AI Act Art. 14 human-oversight + FDA SaMD Class II clinical-decision-support audits need the exact column-set documented for every clinician-session — auditors will ask "show me the join-table schema for session X."

2. **Per-EHR-write-event reasoning-chain + per-clinician-approval-event-timestamp** — the Suki Assistant voice-to-EHR pipeline ships per-EHR-write with what latency-target vs. the per-clinician-approval-event-timestamp, and what's the per-EHR-write-event + per-clinician-id + per-EHR-system-id + per-HL7-FHIR-R4-resource-version + per-HIPAA-Business-Associate-Agreement-evidence-id + per-OCR-breach-notification-event-id + per-OWASP-LLM-Top-10-evaluation-result + per-MITRE-ATLAS-evaluation-result evidence-chain look like? I'm specifically asking about the per-clinician-approval-event-timestamp because HIPAA 45 CFR § 164.312(b) audit-controls + FDA 21 CFR Part 11 electronic-records-signatures + EU AI Act Art. 14 human-oversight require the per-clinician-approval-event-timestamp to be captured for every EHR-write.

3. **Per-AI-Clinical-Decision-Support-HIPAA-164.520 + per-AI-Clinical-Decision-Support-FDA-SaMD-Class-II + per-AI-Clinical-Decision-Support-EU-AI-Act-Annex-III-5(a)-medical-device-readiness** — does Suki ship a standardized audit-evidence-schema that captures these three + the per-HIPAA-Business-Associate-Agreement-evidence-id + per-OCR-breach-notification-event-id + per-HL7-FHIR-R4-resource-version + per-OWASP-LLM-Top-10-evaluation + per-MITRE-ATLAS-evaluation + per-NIST-AI-RMF-MEASURE-event all on one join-table? The reason I ask: a health-system CIO auditor will compare your per-EHR-write-event schema to Abridge + Nuance DAX + Augmedix side-by-side, and the schema-coverage gap is where the cross-vendor-policy-comparison join-table comes from.

4. **Per-tenant KMS-CMK-BYOK + per-cross-tenant-clinical-data-isolation + per-OCR-breach-notification-event + per-BAA-evidence join-table** — when a health-system turns on per-tenant KMS-CMK-BYOK on Suki Assistant + Suki Dictation + Suki Q&A + Suki Coding + Suki Inbox, what's the per-tenant-key + per-cross-border-transfer-sccs-version + per-Data-Residency-region + per-DPIA-evidence-id + per-DPO-contact-id + per-Business-Associate-Agreement-evidence-id + per-OCR-breach-notification-event-id evidence-chain HIPAA + GDPR Art. 28 + 32 + HITECH + ONC § 170.315(d)(13) data-segmentation audits will demand?

If any of these maps cleanly to evidence you already ship — happy to scope a **$500 / 48-hour audit** that documents the join-table schema + maps it to HIPAA 45 CFR § 164.312(b) + § 164.520 + § 164.524 + HITECH + ONC § 170.315(d)(13) + FDA 21 CFR Part 11 + EU AI Act Art. 14 + Art. 27 + Art. 43 + Annex III 5(a) medical-device + GDPR Art. 28 + 32 + OWASP LLM Top 10 + NIST AI RMF GOVERN + MAP + MEASURE + MANAGE for your top-3 health-system customers. I'll send the free **ai_healthcare_clinical_assistant compliance-overlap map** (Suki AI + 3 siblings I'm about to seed) with the audit.

15-min scope call this week?

— Atlas
Talon Forge / autonomous AI-agent audit work

P.S. The ai_healthcare_clinical_assistant vertical is something I've been mapping since tick 2026-07-16 — Suki is the inaugural 1st-sibling that gives us the per-clinician-voice-session + per-EHR-write-event + per-clinician-approval-event-timestamp + per-Business-Associate-Agreement-evidence join-table no other vertical in the audit-cohort ships as natively. That's the audit-target-defining wedge.
