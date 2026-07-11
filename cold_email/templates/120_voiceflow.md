# 120 — Voiceflow (Conversational AI Platform) — voice_ai vertical

**To:** braden@voiceflow.com (Braden Ream, CEO)
**From:** Atlas (Talon Forge)
**Subject:** When GM / JP Morgan / Amazon ask "where's the agent-decision trail?" — the Voiceflow-Designer audit gap

---

Hi Braden,

Congrats on Voiceflow being the canonical no-code agent-builder that GM + JP Morgan + Amazon + BMW + The Home Depot + Vodafone + Meta + ByteDance + Deloitte + Cisco all apparently picked for enterprise CX voice. The "designer-as-source-of-truth" architecture is elegant — but it surfaces a specific 2026 audit angle that no Voiceflow competitor (Cresta, Kore, Yellow.ai, Cognigy) is going to mention in their deck, because it cuts the same way across all of them.

The 5 questions that come up at Voiceflow customer enterprise-buyer audits (specifically because the customer stack is GM + JPM + Amazon, not SMB):

1. **Voiceflow-Designer prompt-flow version-pinning + lineage.** When a Voiceflow workspace exports a prompt-flow that gets embedded into GM's IVR or JPM's customer-onboarding voice agent, the auditor wants the SHA of the designer-version + the per-flow-node prompt-version + the model-version + which enterprise tenants were deployed against which combination — for **SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 §9.4**. Voiceflow's versioning UI is great for collaboration; what's the export shape for an auditor-grade WORM bucket?

2. **Voiceflow Phone voice-channel transcription + PII redaction provenance.** When Voiceflow Phone transcribes a call and redacts a credit-card number, the join-table between `caller_phone_hash` + `transcription_pii_redaction_event` + `downstream_crm_record_id` + `recording_retention_class` + `consent_capture_event` must be reconstructible for **HIPAA + GDPR + PCI-DSS + state wiretapping laws** (CA is two-party, FL is two-party, TX is one-party — the consent-capture flow varies per state and per Voiceflow Phone deployment). The GM OnStar + JPM Card Services + Amazon Alexa deployments all touch this.

3. **Voiceflow Knowledge Base RAG retrieval provenance + per-answer attribution.** When a Voiceflow Knowledge Base agent answers a customer's "what's my account balance" question, the join-table between `kb_doc_id` + `retrieval_score` + `answer_completion_hash` + `per-citation-groundedness-score` must be exportable for **SEC 17a-4 + FINRA 4511 + EU AI Act Art. 12**. The JPM Card Services customer is the canonical buyer of this; without it the agent's hallucinated-balance answer isn't defensible in a FINRA exam.

4. **Cross-tenant Voiceflow-workspace isolation evidence + customer-managed-keys.** Voiceflow's multi-tenancy is logical (row-level); the SOC 2 + EU AI Act + FedRAMP buyer needs the per-workspace isolation-evidence document + the admin-role audit-log + the option for customer-managed-keys (BYOK). What's the current Voiceflow posture, and is BYOK on the 2026 roadmap?

5. **EU AI Act Annex III §4 high-risk classification for Voiceflow Phone deployments** — financial-services IVR (JPM Card), healthcare-intake (provider network deployments), biometric-voice-recognition (caller-verification flows). Each is its own conformity-assessment lane under **EU AI Act Art. 6 + 14 + 43 + 27** (fundamental-rights impact assessment). For Voiceflow, this matters most because the enterprise customer stack is exactly the kind of customer that triggers the high-risk classification — Voiceflow's compliance posture becomes a procurement gate.

---

**What I do:** 48-hour AI-agent audit. $500 flat. You get a written gap-analysis against SOC 2 CC7.2 + EU AI Act Art. 12 + HIPAA + PCI-DSS + GDPR + ISO 42001, with the actual join-table schemas + an Annex III §4 conformity-assessment template your GM/JPM/Amazon customers can hand to their auditors.

**The ask:** 30-min call this week with you or your head of compliance to walk through which of these 5 gaps your enterprise customers are already asking about, and whether the audit deliverable is a buyable product (Path A — $497/mo retainer) or a one-shot ($500 — Path B).

— Atlas
Talon Forge | atlas@talonforge.io
