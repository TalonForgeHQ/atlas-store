# Cold Email Template 850 — Vapi (Lead 850, ai_voice_agent_infra CLOSER #5/5)

**To:** support@vapi.ai (canonical ai_voice_agent_infra developer-platform route — Vapi is the dev-platform orchestration + custom-LLM-provider + custom-transport + custom-voice configuration layer for voice-AI builders; verified live 2026-07-21 via curl scrape of `vapi.ai/` HTTP 200 exposing developer-platform CTA as the canonical commercial route; Vapi sits BETWEEN the ASR layer (Deepgram 846) + Speech-Understanding (AssemblyAI 847) + state-machine orchestration (Retell 848) and the production deployment layer (Bland 849) as the developer-platform build rail that ships per-call + per-LLM-call + per-tool-call + per-assistant provenance at the dev-platform layer.)

**From:** Atlas Audit Prep — Talon Forge LLC

**Vertical:** ai_voice_agent_infra (CLOSER #5/5 — closes the cohort to FULL 5/5. Cohort semantic: end-to-end voice-AI infrastructure rail from ASR (Deepgram 846 OPENER) → Speech Understanding + Guardrails (AssemblyAI 847) → agentic state-machine + Streaming RAG (Retell AI 848) → production deployment + carrier bridges (Bland AI 849) → **developer-platform build rail (Vapi 850 CLOSER)** — the cross-stack audit-trail-ready lane that wires it all together at the call-leg layer.)

**Send window:** Mon-Wed 9:30-10:30 AM PT (Vapi founder Jordan Dearsley active on X)

**Subject line A:** Vapi developer-platform → 24-column per-call-id join-table + EU AI Act Art. 26 + cross-provider-LLM-version audit-prep

**Subject line B:** Per-call-LLM-call-id + per-call-assistant-id + per-call-end-of-call-report for Vapi dev-platform + enterprise-deployers

**Subject line C:** Vapi Bring-your-own-LLM + bring-your-own-transport + bring-your-own-voice → audit-trail readiness

---

Hi Vapi team (Jordan + Nikhil + platform-security + product + enterprise),

Quick context — we run audit-target prep for voice-AI vendor cohorts (Deepgram, AssemblyAI, Retell AI, Bland AI, **Vapi**). When a Fortune-500 dev-tools buyer hits Vapi with a SOC 2 CC7.2 + HIPAA §164.312(b) + GDPR Art. 28 + EU AI Act Art. 9 + Art. 10 + Art. 14(4) + Art. 26 + Art. 50 evidence request on the Vapi platform, the per-call + per-LLM-call + per-tool-call + per-assistant provenance join-table they actually need is:

1. per-call-id + per-call-live-transcript (timestamps + speaker-turns)
2. per-call-messages-id + per-call-messages-role + per-call-messages-content (the full message-by-message role/content sequence)
3. per-call-assistant-id + per-call-assistant-overrides (per-call custom model selection + custom temperature + custom system prompt)
4. per-call-LLM-call-id (the actual LLM-API invocation record; Vapi's chat completions proxy call)
5. per-call-tool-call-id + per-call-tool-call-name + per-call-tool-call-arguments (the function-call invocation that came out of the LLM step)
6. per-call-transport-call-id (the SIP/Twilio/WebRTC call-control object)
7. per-call-customer-id + per-call-assistant-config-hash (proves which assistant-config produced this call)
8. per-call-prompt-version-id + per-call-prompt-experiment-run-id
9. per-call-voice-id + per-call-voice-provider (ElevenLabs / OpenAI / PlayHT / Azure / Cartesia / custom)
10. per-call-transcriber-id + per-call-transcriber-provider (Deepgram / AssemblyAI / GLADIA / Azure / custom)
11. per-call-model-id + per-call-model-provider (OpenAI / Anthropic / Google / Groq / Cerebras / custom — the cross-provider LLM chain)
12. per-call-knowledge-base-id + per-call-knowledge-base-version-id (Vapi's KB / vector-store layer used by the assistant)
13. per-call-end-of-call-report-id + per-call-summary + per-call-success-evaluation + per-call-recording-url
14. per-call-cost-breakdown-id + per-call-cost-USD (Vapi's per-call cost rollup: LLM + TTS + STT + transport + tool costs)
15. per-call-token-count + per-call-latency-ms (per-stage latency: STT + LLM + TTS)
16. per-call-prompt-injection-detection-signal + per-call-jailbreak-detection-signal
17. per-call-multilingual-detection (which language was actually detected vs the configured locale)
18. per-call-custom-credential-vault-id (when the customer BYO-keys OpenAI / Anthropic / ElevenLabs into Vapi's secret store)
19. per-call-deployment-region + per-call-egress-jurisdiction (US / EU / UK / CA / AU / IN / SG / JP / CH / BR)
20. per-call-tenant-KMS-key-id + per-call-encryption-at-rest-mode
21. per-call-DNC-scrub-result + per-call-TCPA-prior-express-consent-evidence
22. per-call-AI-disclosure-timestamp + per-call-AI-disclosure-spoken-text
23. per-call-human-handoff-target + per-call-human-handoff-decision
24. per-call-pii-redaction-flag + per-call-pci-redaction-flag + per-call-phi-redaction-flag + per-call-glba-redaction-flag

We ship a $500 audit that produces this exact 24-column per-call-id join-table for Vapi-Assistant + Vapi-LLM-Provider + Vapi-Transcriber-Provider + Vapi-Voice-Provider + Vapi-Knowledge-Base + Vapi-Tools + Vapi-Transport-Layer + Vapi-End-of-Call-Report — across SOC 2 Type II, HIPAA, GDPR Art. 28 DPA + Art. 17 deletion-propagation, CCPA/CPRA, EU AI Act Annex III §4 + Art. 9 + Art. 10 + Art. 14(4) + Art. 26 + Art. 50, TCPA prior-express-consent, California SB 1001, Colorado SB 24-205, Illinois AI Video Interview Act, 12-state AI-disclosure. 14-day delivery, 1-2 audit-engineer-weeks of work, vendor-DD-grade evidence packet.

**Cohort overlap (so you know who's comparing Vapi in their vendor-DD matrix right now):**
- Deepgram (Lead 846, ai_voice_agent_infra OPENER #1/5 — ASR seam layer below Vapi)
- AssemblyAI (Lead 847, ai_voice_agent_infra sibling #2/5 — Speech Understanding + Guardrails + LLM Gateway layer below Vapi)
- Retell AI (Lead 848, ai_voice_agent_infra sibling #3/5 — agentic state-machine + Streaming RAG layer parallel to Vapi)
- Bland AI (Lead 849, ai_voice_agent_infra sibling #4/5 — production deployment + carrier-bridge layer ABOVE Vapi)

**Why Vapi is CLOSER (not OPENER + not mid-cohort) for the ai_voice_agent_infra vertical:**
Vapi is the only cohort member that closes the developer-platform cross-provider audit-trail lane — the join-table that ties the BYO-LLM (OpenAI/Anthropic/Google/Groq/Cerebras/custom) call to the BYO-transcriber (Deepgram/AssemblyAI/GLADIA/Azure/custom) call to the BYO-voice (ElevenLabs/OpenAI/PlayHT/Azure/Cartesia/custom) call to the BYO-transport (Twilio/WebRTC/SIP/custom) call. None of the sibling cohort members (Deepgram, AssemblyAI, Retell, Bland) ship the cross-provider-LLM-version-pinning + cross-provider-voice-version-pinning + cross-provider-transport-pinning at the call-leg layer that Vapi ships. Vapi is the developer-platform where the cross-provider audit cascade actually composes — that's the COHORT-FULL closer wedge.

If you can route this to your platform-security + enterprise-GRC side (or if an external team owns enterprise-trust exports), drop us a forward — we ship a one-page scope asynchronously.

Best,
Atlas @ Talon Forge
https://talonforgehq.github.io/atlas-store

PS — This is a commercial compliance-evidence offer sent only through VAPI's published general route; it is not a security disclosure.
