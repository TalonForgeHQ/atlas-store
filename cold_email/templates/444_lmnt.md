# Lead 444 — LMNT

**Vertical:** voice_agents
**Tier:** 1
**Website:** https://www.lmnt.com/
**Founders:** Zachary DeWitt, Albert Xu, and Phil Chau
**Verified public inbox:** team@lmnt.com

---

**Subject:** 5 audit questions on LMNT voice-clone consent, provenance, and deepfake controls

Hi Zachary,

LMNT sits on a particularly sensitive boundary: low-latency synthetic speech becomes a real person or brand voice inside customer-support, healthcare, insurance, financial-services, and telephony workflows. When a cloned voice is disputed, the audit question is not only which model generated it, but which tenant, source recording, consent record, voice version, streaming request, watermark, approval, and downstream call produced it.

I run a focused **$500 / 48-hour audit** for AI voice platforms. These are the five questions I would test against LMNT:

1. **Synthesis provenance:** Can one evidence row join tenant/workspace, synthesis request, voice and clone versions, source-audio and consent records, model version, streaming chunks, output format, latency, destination, cost, watermark, and final result?
2. **Voice-clone consent:** Is every Instant or Professional clone bound to a verifiable speaker authorization, permitted-use scope, revocation path, and retained training-audio license rather than a checkbox detached from the model artifact?
3. **Abuse resistance:** What replayable tests cover unauthorized cloning, audio deepfakes, voice-biometric spoofing, prompt or input poisoning, cross-tenant clone access, and attempts to strip or bypass provenance signals?
4. **Tenant and biometric isolation:** Can LMNT prove that voice templates, recordings, custom pronunciations, generated audio, and deletion events remain isolated by organization and region, including cross-border transfer evidence?
5. **Retention and cost evidence:** Are clone-training, synthesis, detection, watermarking, storage, deletion, and telephony-attestation costs joined to immutable audit records with named owners and acceptance tests?

The deliverable is a procurement-ready gap map and fix specification mapped to **EU AI Act Articles 12, 14, 15, and 50; GDPR Articles 9 and 28; SOC 2 CC6.1 and CC7.2; ISO 42001; NIST AI RMF; OWASP LLM Top 10; MITRE ATLAS; and applicable FCC/TCPA telephony controls**. I test one real workflow end to end rather than sending a generic security checklist.

If this is relevant, I can send a one-page scope for one LMNT cloning or production TTS workflow. The audit is **$500 fixed**, delivered in **48 hours**, with an optional **$497/mo** evidence-maintenance follow-on.

Worth a 30-minute working session?

Best,
Atlas
Talon Forge LLC
https://talonforgehq.github.io/atlas-store/

**Public references:**
- https://www.lmnt.com/
- https://docs.lmnt.com/
