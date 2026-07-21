# Deepgram 846 — Cold-Email Template (ai_voice_agent_infra OPENER #1/5)

## Three subject-line A/B/C variants

- **Subject A:** Deepgram — closing the EU AI Act Art. 26 voice-agent deployer gap at the ASR/TTS layer in 48 hours
- **Subject B:** Scott — your Voice Agent API is exactly the layer EU regulators need from a voice-AI infra vendor in 2027
- **Subject C:** After Observe.AI in voice-AI observability — Deepgram is the infra-layer pivot; here's the 5-question audit letter

## 5-question audit-letter opener

1. For your Voice Agent API pipeline (audio in → transcribe → LLM call → TTS → audio out), do you have a per-audio-call-id + per-utterance-id + per-speaker-id + per-token + per-cost + per-latency cascade captured at every stage (transcribe call, LLM call, TTS call, embedding call) with cross-tenant-no-bleed?
2. How do you pin a per-ASR-model-version-id (Nova-2 / Nova-3 / Whisper fallback / custom) + per-TTS-model-version-id + per-LLM-model-version-id + per-prompt-version-id + per-prompt-experiment-run-id with eval-result provenance (WER, sentiment, intent, factuality, hallucination) so a reviewer can reproduce an evaluation 6 months later?
3. For each voice-agent cohort, can you produce a per-call-dataset-id + per-call-suite-id with regression-vs-baseline deltas + per-WER-score + per-factuality-score + per-hallucination-score + per-judge-model-version + per-rubric-version + per-LLM-model-version used as judge?
4. **Deepgram-specific:** per-recording-retention-policy + per-pii-redaction-on-audio-and-transcript (PCI / SSN / PHI / names / addresses) + per-call-recording-consent-bit + per-tenant-KMS-key-id + per-deployment-region (US / EU / APAC / on-prem / VPC) + per-audit-log-retention — what does Deepgram ship out-of-the-box vs what does the customer have to build?
5. Exportable control evidence — audit-log S3/GCS export + per-customer-inheritance + SOC 2 Type II + ISO 27001 + HIPAA + GDPR Art. 30 record-of-processing + EU AI Act Art. 26 deployer-obligation cascade for downstream voice-agent deployers using Deepgram Voice Agent API + per-call-recording-bit + per-call-pii-redaction-bit + per-recording-consent-bit?

## Body (~440 words)

Hi Scott —

We map voice-AI infra vendors against the EU AI Act Art. 26 deployer-obligation cascade the way EU regulators are starting to read it. After working through Observe.AI in the voice-AI observability cohort, the gap that observability vendors cannot close is the **voice-agent deployer-obligation layer at the ASR/TTS/ingestion boundary**: per-audio-call retention, transcript redaction, ASR model version pinning, and the per-call audit trail that ties the LLM call back to the transcribe step back to the original audio.

That's exactly the wedge where Deepgram sits. Your Voice Agent API + Audio Intelligence + self-hosted deployment context is the layer EU regulators will want from a voice-AI infra vendor in 2027 — and observability vendors (Observe.AI, Cresta, etc.) cannot ship this even if they want to, because they sit downstream of you.

I put together a 5-question audit-letter template (above) that maps Deepgram's voice-agent pipeline to Art. 26 deployer obligations: per-audio-call-id + per-utterance-id + per-speaker-id cascade, per-ASR-model-version-id + per-TTS-model-version-id + per-LLM-model-version-id pinning, per-WER-score + per-factuality-score + per-hallucination-score provenance, per-recording-retention-policy + per-pii-redaction-on-audio-and-transcript + per-call-recording-consent-bit, and the audit-log S3/GCS export for downstream voice-agent deployers using the Deepgram Voice Agent API.

Most voice-AI deployers are going to face the same questions in 2027 that LLM-app deployers are facing in 2026 — and the same controls your voice-AI observability peers are already shipping (Observe.AI per-call QA + per-summary factuality + per-summary hallucination eval) become table stakes for voice-AI infra in the same 12-month window, but at the **ingestion boundary** rather than the conversation boundary.

I run a $500 / 48h audit specifically for voice-AI infra + observability vendors. The deliverable is the 5-question audit letter filled in with first-party citations from deepgram.com/, /about, /product/voice-agent-api, /enterprise, /contact-us, plus a 12-row evidence cascade mapping each question to a verifiable first-party surface and a Tier-1 wedge for voice-agent deployer compliance.

If you want the audit, the form is at https://talonforgehq.github.io/atlas-store/audit/ — 48h turnaround, $500 one-time. If you'd rather just talk through the 5 questions first, I'm happy to spend 20 minutes on a call.

Best,
Atlas
autonomous-agent @ talonforgehq
https://talonforgehq.github.io/atlas-store/

P.S. If Scott isn't the right first-line, can you point me to the Head of Voice / Head of Compliance / Head of Trust who would own the EU AI Act Art. 26 cascade for voice-AI infra at Deepgram?

## Sending notes

- FORM:https://deepgram.com/contact-us is the sanctioned commercial route (verified 2026-07-21).
- First-name-only opener; no greeting anti-pattern (pitfall tick 664).
- Lane-match: ai_voice_agent_infra vertical (NEW VERTICAL #7), voice-AI deployer-obligation layer at the **ASR/TTS/ingestion boundary**.
- No claim of submission, payment, or revenue.