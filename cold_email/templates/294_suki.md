# Lead 294 — Suki AI

**Vertical:** ai_healthcare_clinical_assistant
**Tier:** 1
**Website:** https://www.suki.ai/
**Founder / CEO:** Punit Soni
**Verified public inbox:** support@suki.ai

---

**Subject:** 5 audit questions on Suki’s ambient AI and EHR write path

Hi Punit,

Suki’s ambient assistant sits inside a high-consequence workflow: clinician speech becomes a draft note, coding guidance, inbox action, or EHR update. A hospital buyer therefore needs more than accuracy metrics. They need evidence tying each output to the exact encounter, source audio, model and prompt version, EHR integration, clinician review, and final state change—without exposing another patient or health-system tenant.

I run a focused **$500 / 48-hour audit** for production AI platforms. These are the five questions I would test against Suki:

1. **Encounter-to-EHR provenance:** Can one export join patient and encounter IDs, voice-session and transcript hashes, model and prompt versions, retrieved clinical context, generated note or code, clinician edits, approval timestamp, FHIR resource version, EHR write event, rollback, latency, and cost?
2. **Human review and clinical boundaries:** Is every generated note, coding suggestion, answer, or inbox action bound to the clinician who reviewed it? Can a buyer prove which functions only draft content and which can trigger downstream workflow or record changes?
3. **Hostile audio, text, and integration input:** What prevents spoken prompt injection, copied chart text, portal messages, attachments, FHIR payloads, or third-party EHR content from overriding instructions, leaking PHI, changing coding, or triggering unauthorized actions?
4. **PHI, tenant, and deletion isolation:** Can customers retrieve tests proving that audio, transcripts, notes, embeddings, caches, fine-tuning data, logs, and encryption keys remain isolated by health system, clinician, patient, and environment—and that deletion propagates through every derived artifact?
5. **Incident reconstruction:** After a hallucinated note, wrong-code suggestion, missed denial, cross-tenant exposure, or integration failure, can Suki produce WORM-capable evidence linking the source encounter through clinician approval and the final EHR state, including every retry and rollback?

The deliverable is a procurement-ready gap map and fix specification mapped to **HIPAA 45 CFR 164.312; HITECH; SOC 2 CC6.1 and CC7.2; EU AI Act Articles 9, 12, 14, and 15; GDPR Articles 28 and 32; ISO 42001; NIST AI RMF; OWASP LLM Top 10; MITRE ATLAS; HL7 FHIR R4; and ONC 45 CFR 170.315(d)(13)**. I test one live ambient-session-to-EHR path end to end rather than sending a generic checklist.

**Why Suki specifically:** ambient capture, clinical drafting, coding, Q&A, and inbox workflows compress multiple evidence boundaries into one clinician experience. That speed is the product advantage, but it also makes provenance, PHI isolation, and human-approval gaps compound quickly during hospital vendor review.

If this is on your radar for the next health-system procurement cycle, I can hold a slot this week and ship the gap map within 48 hours.

— Atlas (Talon Forge LLC)

$500 / 48 hours · procurement-ready gap map · one live clinical workflow tested end to end
