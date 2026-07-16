From: james@talonforge.io
To: security@deepgram.com
Subject: Deepgram Nova-3 + Voice Agent API — 5 questions before we sign the BAA

Hi Deepgram security team,

I'm James Potts, founder of Talon Forge. We run a 50-customer voice-AI-agent audit practice (SOC 2 Type II + HIPAA + EU AI Act + OWASP LLM Top 10 + MITRE ATLAS coverage) and we're now sending our clients to Deepgram as the canonical ASR backbone for the realtime_voice_video_ai_infra cohort. Three of our recent audit subjects — LiveKit Agents SDK, Daily.co / Pipecat, Agora Conversational AI — all evaluate Deepgram Nova-3 against competitive STT offerings, and we want to make sure our enterprise audit-template lines up with your actual control surface before we send our first joint customer your way.

I have five vendor-DD questions I'd like to walk through with your security/GRC team (30-min Zoom, your time):

1. Per-request provenance — can you share the canonical join-table for per-audio-stream-id → per-Nova-3-model-version-id → per-VAD-segment-id → per-utterance-id → per-word-id → per-confidence-score-id → per-speaker-tag-id → per-diarization-segment-id → per-intent-classification-id → per-sentiment-score-id → per-key-term-boost-id → per-language-detection-id → per-API-call-id → per-billing-event-id lineage? Our audit-template uses 60+ columns and we want to make sure we're not missing Deepgram-specific events like Nova-3 endpointing decisions or Aura-2 TTS invocations.

2. Prompt-injection + adversarial-audio defense — Deepgram processes raw user audio into transcripts that get fed into downstream LLMs. How do you defend against adversarial audio (per OWASP LLM Top 10 LLM01+LLM03+LLM04+LLM06 + MITRE ATLAS AML.T0051+AML.T0054 + EU AI Act Art. 15)? Specifically — per-VAD-segment-poisoning, per-Nova-3-model-version-confusion, per-speaker-spoofing (voice cloning detection), per-deepfake-voice-input-detection, per-key-term-boost-poisoning.

3. Cross-region audio-data-residency — Deepgram processes audio in US data center by default. For EU + India + Brazil + UAE + Australia + Canada + UK + Singapore + Japan + Philippines customers, what's the per-customer-region selection mechanism, and is it auditable in your customer-facing logs? We're auditing against Schrems II + GDPR Art. 28 + EU AI Act Art. 10 + India DPDP Act 2023 + Brazil LGPD Art. 33 + UAE PDPL + Canadian PIPEDA + Singapore PDPA + Philippines DPA + Japan APPI.

4. HIPAA-eligible Deepgram Nova-3 medical-transcription + Voice Agent API clinical-pipeline — Deepgram is HIPAA-eligible per deepgram.com/healthcare. For BAA-covered healthcare customers using Nova-3 + Voice Agent API in clinical pipelines, can you walk us through the per-stream PHI-flag + per-billing-account-id CMK/BYOK encryption + per-region-BAA-ready configuration? HIPAA §164.312(a)(2)(iv) + §164.312(b) + §164.312(e)(1) + §164.514(b) is the floor.

5. Cross-tenant isolation — for Deepgram Cloud + Deepgram Self-hosted + Deepgram On-Premise + per-project-id + per-API-key-id + per-billing-account-id + per-custom-model-id isolation evidence, can you share the most recent SOC 2 Type II report (CC6.1) + GDPR DPA (Art. 28) + EU AI Act readiness statement?

If a 30-min Zoom is too much friction, I'm also happy to do a written Q&A over email. Our standard vendor-DD SLA is 5 business days, and we won't share your answers outside our audit subject's GRC team.

If Deepgram isn't the right contact for any of these, I'd appreciate a redirect to your security/GRC lead. Either way, thanks for your time — looking forward to working together.

Best,
James Potts
Founder, Talon Forge LLC
james@talonforge.io
https://talonforge.io