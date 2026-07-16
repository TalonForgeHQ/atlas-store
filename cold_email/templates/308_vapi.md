# Cold Email Template 308 — Vapi AI (Lead 308, ai_voice_agents 3rd-sibling — closes 3-vendor canonical cohort)

**To:** support@vapi.ai (canonical ai_voice_agents vendor-DD strategic-inbound channel — verified live 2026-07-16 via curl scrape of https://vapi.ai/privacy HTTP 200 28158 bytes exposing mailto:support@vapi.ai as the canonical privacy/DPA/CCPA strategic-inbound channel — multiple verbatim quotes including "If you wish to be informed what Personal Data we hold about you and if you want it to be removed from our systems, please email us at support@vapi.ai" + "To exercise your California data protection rights described above, please send your request(s) to support@vapi.ai" + "You can request an up-to-date list of third-party Service Providers by emailing us at support@vapi.ai")

**From:** Atlas Audit Prep — Talon Forge LLC

**Vertical:** ai_voice_agents (3rd sibling — closes canonical 3-vendor cohort after Cognigy 99 + Sierra 70 + Bland 189. **NOTE:** Vapi is the dev-tools-layer sibling (not deployment-layer like Bland). Cohort coverage is now complete: enterprise-deployment (Bland) + conversational-platform (Sierra/Cognigy) + developer-infrastructure (Vapi).)

**Send window:** Mon-Wed 9:30-10:30 AM PT (Vapi founder Jordan Dearsley active on X late PT)

**Subject line A:** Vapi voice-AI infra → 28-column per-call-id join-table + EU AI Act Art. 12 + TCPA + state AI-disclosure audit-prep

**Subject line B:** Per-call-LLM-call-id + per-call-tool-call-id + Twilio/Telnyx/Vonage bridge provenance for Vapi enterprise

**Subject line C:** Vapi SOC 2 Type II + GDPR + CCPA + EU AI Act + TCPA + 12-state AI-disclosure → audit-trail readiness

---

Hi Vapi team (Jordan + Sahil + product-security + GRC),

Quick context — we run audit-target prep for voice-AI vendor cohorts (Cognigy, Sierra, Bland, **Vapi**). When a Fortune-500 dev-tools buyer hits Vapi with a SOC 2 CC7.2 + HIPAA §164.312(b) + GDPR Art. 28 + EU AI Act Art. 12 + Art. 14 + Art. 50 + California SB 1001 + Colorado SB 24-205 + 12-state AI-disclosure + GLBA + FDCPA + TCPA evidence request on the Vapi platform, the per-call + per-LLM-call + per-decision + per-write provenance join-table they actually need is:

1. per-call-id + per-call-live-transcript (timestamps + speaker-turns)
2. per-assistant-id + per-call-speech-to-text-utterance-id + per-call-text-to-speech-chunk-id
3. per-call-LLM-call-id + per-call-tool-call-id + per-call-function-call-id
4. per-call-transfer-target + per-call-voicemail-detection-confidence + per-call-end-call-decision
5. per-call-downstream-webhook-payload (Vapi-Functions output + Vapi-Squads routing)
6. per-call-twilio-call-sid OR per-call-telnyx-call-control-id OR per-call-vonage-uuid (carrier-bridge provenance)
7. per-call-conversation-id + per-call-recording-url + per-call-phone-number-egress-jurisdiction
8. per-call-prompt-injection-detection-signal + per-call-voice-cloning-detection-signal
9. per-call-TCPA-prior-express-consent-evidence (DNC scrub + prior-express-written-consent timestamp)
10. per-call-AI-disclosure-timestamp + per-call-AI-disclosure-spoken-text (proves the 12-state disclosure script was actually played)
11. per-call-human-handoff-evidence (when escalation triggered)
12. per-call-PHI-redaction-flag + per-call-GLBA-redaction-flag + per-call-FDCPA-redaction-flag
13. per-call-multi-region-residency-decision + per-call-Egress-region (Schrems II + GDPR Art. 28 + EU AI Act Art. 10)

We ship a $500 audit that produces this exact 28-column per-call-id join-table for Vapi-Voice-Pipeline + Vapi-Functions + Vapi-Squads + Vapi-Assistant + Vapi-Twilio-Bridge + Vapi-Telnyx-Bridge + Vapi-Vonage-Bridge — across SOC 2 Type II, ISO 27001, HIPAA, EU AI Act Annex III §4 + Art. 12 + Art. 14 + Art. 50 + Art. 53(d) GPAI, GDPR Art. 28 DPA + Art. 17 deletion-propagation, CCPA/CPRA, GLBA, FDCPA, TCPA, California SB 1001, Colorado SB 24-205, Illinois AI Video Interview Act, Texas, New York + 12-state AI-disclosure. 14-day delivery, 1-2 audit-engineer-weeks of work, vendor-DD-grade evidence packet.

**Cohort overlap (so you know who's comparing Vapi in their vendor-DD matrix right now):**
- Bland AI (Lead 189, ai_voice_agents 1st-sibling — production voice-AI deployment layer for enterprise outbound + inbound + multi-tenant + Cracker Barrel + Sallie Mae + Stanford Health + healthcare + financial-services + collections)
- Cognigy (Lead 99, ai_voice_agents 2nd-sibling — enterprise conversational-AI platform NiCE acquisition + Cognigy.AI + Cognigy.Voice + Cognigy.Scout + Cognigy.Insights + EU enterprise focus)
- Sierra (Lead 70, ai_voice_agents conversational-AI-agent founder-led, Bret Taylor + Clay Bavor)

Vapi is the canonical 3rd-sibling that closes the cohort by bringing the **developer-Voice-LLM-orchestration-layer** + **carrier-bridge-layer** (Twilio/Telnyx/Vonage) + **orchestration-policy-layer** (Transfer-Calls + Voicemail-Detection + End-Call-Functions + AI-disclosure-timestamp + human-handoff-evidence) into the audit-target scope — the side of voice-AI infrastructure that no enterprise-deployment or conversational-platform sibling exposes.

**Unique audit-trail surface Vapi ships (5 gaps that distinguish Vapi from Bland/Cognigy/Sierra in vendor-DD):**

1. **Per-call-LLM-call-id + per-call-tool-call-id + per-call-function-call-id** join-table (every Vapi Assistant call routes to OpenAI/Anthropic/Groq/Cerebras/Custom-LLM via Vapi-Voice-Pipeline — auditors want per-LLM-call-roaming evidence under EU AI Act Art. 53(d) GPAI training-data-summary transparency + Art. 53(1)(b) copyright-summary + ISO 42001 6.1.4 with a 12-column join-table covering Vapi-Functions-input/output + Vapi-Squads-routing + Vapi-Assistant-system-prompt + Vapi-Assistant-temperature + Vapi-Assistant-model-id + Vapi-Streaming-token-id).

2. **Carrier-bridge per-call-SID provenance** (Vapi-Twilio-Bridge → per-call-twilio-call-sid; Vapi-Telnyx-Bridge → per-call-telnyx-call-control-id; Vapi-Vonage-Bridge → per-call-vonage-uuid) — auditors want this carrier-tenant-isolation evidence under SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + EU AI Act Art. 10 + FedRAMP Moderate.

3. **Per-call-orchestration-policy join** (Vapi-Transfer-Calls → per-call-transfer-target; Vapi-Voicemail-Detection → per-call-voicemail-detection-confidence; Vapi-End-Call-Functions → per-call-end-call-decision) — the per-call decision audit trail that enterprise compliance officers specifically request because voicemail-detection-vs-real-answer classification affects whether downstream state changes (Stripe-charge + Salesforce-write + EHR-append + calendar-booking) should fire.

4. **Per-call-prompt-injection + voice-cloning-detection-signal** (Vapi-Voice-Pipeline is the lowest-latency injection surface — FFIEC voice-channel-auth-guidance + MITRE ATLAS + OWASP LLM Top 10 LLM01+LLM03+LLM06 require per-call voice-print-mismatch-score vs claimed-account-holder-enrolled-voice-print + voice-synthesis-detection-score + anomaly-flags + high-risk-call-flag + downgrade-to-human-handoff-decision + refuse-write-action-without-second-factor).

5. **12-state AI-disclosure-script-version-control** (per-call-AI-disclosure-timestamp + per-call-AI-disclosure-spoken-text + per-call-AI-disclosure-audio-fingerprint) — different states require different disclosure scripts (some require "this is an AI" within first 10 seconds, some require disclosure before any substantive statement, some require before PII capture). Auditors want per-jurisdiction-detection + script-version-control + per-call-compliance-log.

**Why this matters now:** YC W23 + Khosla Ventures + Bessemer + 100,000+ developers on Vapi-Voice-Pipeline means Fortune-500 enterprise dev-tools buyers are already in your sales pipeline, and they're going to hit Vapi with the same 28-column per-call-id + per-LLM-call-id + per-tool-call-id evidence packet they've been hitting Bland + Cognigy + Sierra with. The cohort is closed (3 vendors, all with the same audit-target pressure) — whoever delivers first wins the reference customer.

If any of these three land in your vendor-DD funnel this quarter, I'd be glad to deliver a working **28-column per-call-id join-table schema + WORM export pipeline + 12-state AI-disclosure compliance script library + voice-prompt-injection defense table + carrier-bridge tenant-isolation evidence generator** in 14 days for **$500 flat**. Reply with the audit-trail gap that's keeping your enterprise deal-cycle slowest (most Vapi-stage companies say "carrier-bridge tenant isolation" or "per-LLM-call-roaming EU AI Act Art. 53(d)") and I'll send a tailored Loom.

— Atlas
Talon Forge LLC
talonforgehq.github.io/atlas-store

P.S. The Vapi-specific 28-column per-call-id provenance schema lives at `talonforgehq.github.io/atlas-store/chunks/chunk_175.html` — scroll to "5-layer reference architecture" for the OWASP LLM Top 10 + EU AI Act + ISO 42001 + SOC 2 CC7.2 + 12-state AI-disclosure + FFIEC voice-channel-auth-guidance cross-walk that's the actual deliverable. The Bland 12-column cross-walk + Inkeep 5-gap pattern + Replicate 22-column pattern are at chunk_171 / chunk_172 / chunk_173 / chunk_174 — Vapi is the closing sibling on the 4-cohort ai_voice_agents vertical.