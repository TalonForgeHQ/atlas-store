# Lead 846 — Deepgram

## Vendor research packet

**Company:** Deepgram, Inc.
**Domain:** deepgram.com
**Vertical:** ai_voice_agent_infra (NEW VERTICAL #7, OPENER #1/5)
**Tier:** 1
**Commercial route:** FORM:https://deepgram.com/contact-us (verified live 2026-07-21, "Contact Us" CTA in global header; fallback enterprise CTA at https://deepgram.com/enterprise)

## Founder / leadership (first-party verified)

- **Scott Stephenson — CEO & Co-Founder** (verbatim deepgram.com/about "Founded in 2015 ... CEO and co-founder Scott Stephenson and his teammate later explored deep learning for audio analysis at the University of Michigan")
- Leadership page canonical: https://deepgram.com/company/leadership
- About page canonical: https://deepgram.com/about

## Company facts (first-party verified)

- Founded 2015 (verbatim "Founded in 2015")
- Originated in machine-learning research for waveform analysis in a dark-matter detector in China (verbatim about page)
- Vision verbatim: "Enabling human-machine interactions with Voice AI"
- Footer copyright: "Copyright © 2026 Deepgram"

## Product surface (first-party verified)

- **Speech-to-Text API** — https://deepgram.com/product/speech-to-text
- **Text-to-Speech API** — https://deepgram.com/product/text-to-speech
- **Voice Agent API** — https://deepgram.com/product/voice-agent-api (most relevant to EU AI Act Art. 26 voice-agent deployer-obligation cascade)
- **Audio Intelligence API** — https://deepgram.com/product/audio-intelligence (sentiment, intent, topic, summarization)

## Deployment surface (first-party verified)

- **Self-Hosted Deployment** — https://developers.deepgram.com/on-prem (verbatim "Self-Hosted Deployment" footer link; canonical https://developers.deepgram.com/docs/self-hosted-introduction)
- Cloud + on-prem + VPC deployment options

## Solutions surfaces (first-party verified)

- Contact Centers — https://deepgram.com/solutions/contact-centers
- Speech Analytics — https://deepgram.com/solutions/speech-analytics
- Conversational AI — https://deepgram.com/deepgram-for-voicebots-and-chatbots
- Media Transcription — https://deepgram.com/solutions/media-transcription
- Medical Transcription — https://deepgram.com/solutions/medical-transcription
- Podcast Transcription — https://deepgram.com/deepgram-for-podcast-transcription

## Non-overlapping wedge vs Observe.AI 845 (ai_voice_agent_observability OPENER)

Deepgram is the **infra layer** for voice agents (STT/TTS/Voice Agent API), not the **observability** layer. Distinct audit frame:

1. **Per-audio-call-id + per-utterance-id + per-speaker-id** at the **transcription layer** (before any LLM call ever happens) — Deepgram is the upstream source of truth for what was actually said. The audit cascade starts here, not in the LLM call.
2. **Per-model-version-id** for the ASR model (Nova-2 vs Nova-3 vs Whisper fallback) — required for EU AI Act Art. 26 deployer obligation to disclose the speech-recognition model identity to downstream deployers.
3. **Per-deployment-region + per-tenant-KMS-key-id + per-on-prem-vs-cloud** — the self-hosted deployment context is what Deepgram ships that no voice-agent observability vendor (Observe.AI, Cresta, etc.) can ship.
4. **Per-recording-retention-policy + per-pii-redaction-on-transcript (PCI/SSN/PHI for medical transcription)** — Deepgram sets this at the **ingestion boundary** so the downstream LLM never sees unredacted audio.
5. **Per-audio-intelligence-call (sentiment/intent/summarize)** — the Audio Intelligence API is itself an LLM-as-judge, and Deepgram must pin per-prompt-version-id + per-summary-prompt-version + per-LLM-model-version for Art. 26.

## 5-question audit-letter opener (NEW VERTICAL #7 — ai_voice_agent_infra)

1. For your Voice Agent API pipeline (audio in → transcribe → LLM call → TTS → audio out), do you have a per-audio-call-id + per-utterance-id + per-speaker-id + per-token + per-cost + per-latency cascade captured at every stage (transcribe call, LLM call, TTS call, embedding call) with cross-tenant-no-bleed?
2. How do you pin a per-ASR-model-version-id (Nova-2 / Nova-3 / Whisper fallback / custom) + per-TTS-model-version-id + per-LLM-model-version-id + per-prompt-version-id + per-prompt-experiment-run-id with eval-result provenance (WER, sentiment, intent, factuality, hallucination) so a reviewer can reproduce an evaluation 6 months later?
3. For each voice-agent cohort, can you produce a per-call-dataset-id + per-call-suite-id with regression-vs-baseline deltas + per-WER-score + per-factuality-score + per-hallucination-score + per-judge-model-version + per-rubric-version + per-LLM-model-version used as judge?
4. **Deepgram-specific:** per-recording-retention-policy + per-pii-redaction-on-audio-and-transcript (PCI / SSN / PHI / names / addresses) + per-call-recording-consent-bit + per-tenant-KMS-key-id + per-deployment-region (US / EU / APAC / on-prem / VPC) + per-audit-log-retention — what does Deepgram ship out-of-the-box vs what does the customer have to build?
5. Exportable control evidence — audit-log S3/GCS export + per-customer-inheritance + SOC 2 Type II + ISO 27001 + HIPAA + GDPR Art. 30 record-of-processing + EU AI Act Art. 26 deployer-obligation cascade for downstream voice-agent deployers using Deepgram Voice Agent API + per-call-recording-bit + per-call-pii-redaction-bit + per-recording-consent-bit?

## Compliance posture assumed (placeholder — verify before send)

- SOC 2 Type II (assumed for enterprise voice-AI infra)
- ISO 27001 (likely; verify on /security)
- HIPAA (likely for medical-transcription use case)
- GDPR + UK GDPR + CCPA/CPRA + EU AI Act
- PCI DSS (call-recording redaction for card data — verify on /security)

## Sending notes

- FORM:https://deepgram.com/contact-us is the sanctioned commercial route (verified 2026-07-21).
- First-name-only opener (Scott); no greeting anti-pattern (pitfall tick 664).
- Lane-match: ai_voice_agent_infra vertical (NEW), voice-AI deployer-obligation layer at the **infra boundary**.
- No claim of submission, payment, or revenue.
- Lead 846 is OPENER #1/5 of NEW VERTICAL #7 `ai_voice_agent_infra`. 4 OPEN slots remain for siblings #2/5 + #3/5 + #4/5 + CLOSER #5/5.