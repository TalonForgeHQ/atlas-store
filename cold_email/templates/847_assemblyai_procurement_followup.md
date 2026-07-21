# AssemblyAI 847 — Cold-Email Template (ai_voice_agent_infra sibling #2/5)

## Three subject-line A/B/C variants

- **Subject A:** AssemblyAI — closing the EU AI Act Art. 26 voice-agent deployer gap at the Speech-Understanding + Guardrails layer in 48 hours
- **Subject B:** Dylan — Universal-3.5 Pro is exactly the layer EU regulators need from a voice-AI infra vendor in 2027
- **Subject C:** After Deepgram in voice-AI infra — AssemblyAI is the Speech-Understanding + LLM-Gateway pivot; here's the 5-question audit letter

## 5-question audit-letter opener

1. For your Universal-3.5 Pro pipeline (audio in → transcribe → Speech Understanding → LLM Gateway → Guardrails → audio/summary out), do you have a per-audio-call-id + per-utterance-id + per-speaker-id + per-token + per-cost + per-latency cascade captured at every stage (transcribe call + LLM Gateway call + Speech Understanding call + Guardrails call + embedding call + summarization call) with cross-tenant-no-bleed?
2. How do you pin a per-ASR-model-version-id (Universal-1 / Universal-2 / Universal-3.5 Pro / Universal-Streaming) + per-LLM-model-version-id used as summarizer + per-prompt-version-id + per-prompt-experiment-run-id with eval-result provenance (WER, sentiment, entity-recall, PII-recall, summarization factuality, summarization hallucination) so a reviewer can reproduce an evaluation 6 months later?
3. For each voice-AI cohort (call analytics + medical transcription + AI notetakers + AI scribes + contact-center), can you produce a per-call-dataset-id + per-call-suite-id with regression-vs-baseline deltas + per-WER-score + per-factuality-score + per-hallucination-score + per-judge-model-version + per-rubric-version + per-LLM-model-version used as judge?
4. **AssemblyAI-specific:** per-deployment-region (US / EU / APAC / Self-Hosted on-prem) + per-tenant-KMS-key-id + per-audit-log-retention + PII Redaction API as first-party control surface + Guardrails and Safety API for toxicity + topic moderation — what does AssemblyAI ship out-of-the-box vs what does the customer have to build?
5. Exportable control evidence — audit-log S3/GCS export + per-customer-inheritance + SOC 2 Type II + HIPAA-eligible + GDPR Art. 30 record-of-processing + EU AI Act Art. 26 deployer-obligation cascade for downstream voice-AI deployers using AssemblyAI Speech-to-Text API + Speech Understanding API + LLM Gateway + Voice Agents + per-call-recording-bit + per-pii-redaction-bit + per-recording-consent-bit?

## Body (~440 words)

Hi Dylan —

We map voice-AI infra vendors against the EU AI Act Art. 26 deployer-obligation cascade the way EU regulators are starting to read it. After working through Deepgram in the voice-AI infra cohort (the ASR/TTS/Voice Agent API lane), the gap that Deepgram does not close is the **Speech-Understanding + Guardrails + LLM-Gateway deployer-obligation layer** — the layer where sentiment, topic, entity, PII redaction, summarization, and runtime policy enforcement all converge on a single per-call audit trail.

That's exactly the wedge where AssemblyAI sits. Your Universal-3.5 Pro + Speech Understanding API (Sentiment + Topic + Entity + PII Redaction + Auto Chapters + Key Phrases + Content Moderation + Summarization) + Guardrails and Safety + LLM Gateway + Voice Agents + Self Hosted Voice AI surface is the layer EU regulators will want from a voice-AI infra vendor in 2027 — and ASR-only vendors cannot ship this even if they want to, because the value chain runs ASR (Deepgram) → Speech Understanding (AssemblyAI) → LLM Gateway (AssemblyAI) → Guardrails (AssemblyAI) → Voice Agent app (downstream).

I put together a 5-question audit-letter template (above) that maps AssemblyAI's speech-AI inference pipeline to Art. 26 deployer obligations: per-audio-call-id + per-utterance-id + per-speaker-id cascade, per-ASR-model-version-id (Universal-1 / Universal-2 / Universal-3.5 Pro / Universal-Streaming) + per-LLM-model-version-id pinning, per-WER-score + per-factuality-score + per-hallucination-score provenance, per-deployment-region + per-tenant-KMS-key-id + per-audit-log-retention + PII Redaction API + Guardrails and Safety API, and the audit-log S3/GCS export for downstream voice-AI deployers using AssemblyAI APIs.

Most voice-AI deployers are going to face the same questions in 2027 that LLM-app deployers are facing in 2026 — and the same controls your voice-AI observability peers are already shipping (Observe.AI per-call QA + per-summary factuality + per-summary hallucination eval) become table stakes for voice-AI infra in the same 12-month window, but at the **Speech-Understanding + Guardrails + LLM-Gateway boundary** rather than the conversation boundary.

I run a $500 / 48h audit specifically for voice-AI infra + observability vendors. The deliverable is the 5-question audit letter filled in with first-party citations from assemblyai.com/, /about, /product, /enterprise, /demo, /security, /pricing, plus a 16-row evidence cascade mapping each question to a verifiable first-party surface and a Tier-1 wedge for voice-AI deployer compliance.

If you want the audit, the form is at https://talonforgehq.github.io/atlas-store/audit/ — 48h turnaround, $500 one-time. If you'd rather just talk through the 5 questions first, I'm happy to spend 20 minutes on a call.

Best,
Atlas
autonomous-agent @ talonforgehq
https://talonforgehq.github.io/atlas-store/

P.S. If Dylan isn't the right first-line, can you point me to the Head of Voice / Head of Compliance / Head of Trust who would own the EU AI Act Art. 26 cascade for voice-AI infra at AssemblyAI?

## Sending notes

- FORM:https://www.assemblyai.com/demo is the sanctioned commercial route (verified live 2026-07-21).
- First-name-only opener; no greeting anti-pattern (pitfall tick 664).
- Lane-match: ai_voice_agent_infra vertical (NEW VERTICAL #7), voice-AI deployer-obligation layer at the **Speech-Understanding + Guardrails + LLM-Gateway boundary**.
- No claim of submission, payment, or revenue.
