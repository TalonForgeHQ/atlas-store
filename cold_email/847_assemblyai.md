# Lead 847 — AssemblyAI (companion evidence file)

**Tick id:** 2026-07-21-fast-exec-assemblyai-847
**Time:** 2026-07-21 ~21:30 UTC
**Mode:** FULL ship (7 lead surfaces + build-log + revenue_log + send_log + single-script commit + push)
**Vertical:** `ai_voice_agent_infra` (NEW VERTICAL #7 — sibling #2/5 after Deepgram 846 OPENER #1/5)

## Vendor identification

- **Company:** AssemblyAI
- **Domain:** assemblyai.com
- **Category:** Speech AI models + Speech-to-Text + Speech Understanding + LLM Gateway + Voice Agents platform
- **HQ:** San Francisco, CA, USA

## Co-founders + leadership (verified via Wayback Machine snapshot 20240124012931 of assemblyai.com/about, retrieved 2026-07-21)

- **Dylan Fox** — Co-founder + Chief Executive Officer (verbatim first-party, "Our leadership Dylan Fox CEO")
- **Jessi Waters** — Co-founder + Chief Operating Officer (verbatim first-party)
- **Christy Roach** — VP, Marketing
- **Takuya Yoshioka** — Director of Research (Kaggle Criteo 1st-place winner — known speech-AI researcher)
- **Travis Kupsche** — Director of Engineering
- **Eric Jensen** — Head of Sales
- **Ryan Seams** — Head of Customer Success
- **Nicholas Johnson** — additional leadership (verbatim first-party)

## Founding

- **Founded:** 2017 (verbatim first-party "AssemblyAI first started in 2017 with a shared vision to create new, superhuman Speech AI models that will be able to unlock an entirely new class of applications and products to be built leveraging voice data.")

## Funding

- **Series C 2023:** $50M led by Accel + participation from Keith Block + Smith Point Capital + Insight Partners + Daniel Gross + Nat Friedman + Y Combinator (verbatim first-party "We're excited to share that we've raised $50M in Series C funding led by Accel, our partners that also led our Series A, with participation from Keith Block and Smith Point Capital, Insight Partners, Daniel Gross and Nat Friedman, and Y Combinator.")
- **Total funding:** ~$70M+ (per public press coverage)

## Product surface (verbatim first-party assemblyai.com/ 2026-07-21)

- **Pre-recorded Speech-to-Text API**
- **Realtime Speech-to-Text API**
- **Sync Speech-to-Text API**
- **Speech Understanding API** — Sentiment Analysis + Topic Detection + Entity Detection + PII Redaction + Auto Chapters + Key Phrases + Content Moderation + Summarization
- **Guardrails and Safety** — runtime PII + toxicity + topic moderation
- **LLM Gateway** — model-routing + cost-controls
- **Voice Agents** — voice-agent orchestration surface
- **Self Hosted Voice AI** — on-prem deployment
- **Voice AI Cloud** — managed cloud
- **Universal-3.5 Pro** — flagship model (verbatim "Our new flagship speech-to-text model handles real-world audio the way it actually happens. Available for real-time and pre-recorded audio.")
- **Universal-1 + Universal-2 + Universal-Streaming** — earlier model family
- **99 supported languages** — English, Spanish, Portuguese, French, German, Russian, Hindi, Dutch, Japanese, Italian + 89 more

## Use cases (verbatim first-party 2026-07-21)

- Voice Agents
- AI Notetakers
- Call Analytics
- Medical Transcription
- Dictation
- Agent Assist
- AI Scribes

## Customers (verbatim first-party 2026-07-21)

- "Top Voice AI companies are building with Assembly"
- **Zoom** (verbatim first-party customer logo)
- **Siro** (verbatim first-party customer logo)

## Commercial route

- `FORM:https://www.assemblyai.com/demo` — first-party Contact Sales page (Contact Sales | AssemblyAI title; data-form-id="contact-sales" Astro form; first_name/last_name/email/how_did_you_hear_about_us inputs verified live 2026-07-21)
- `/enterprise` (HTTP 200) — enterprise positioning page
- `/pricing` (HTTP 200) — pricing surface
- No suitable general-business inbox published on the rendered first-party surface; FORM-only per pitfall #28

## Wedge (non-overlapping vs Deepgram 846 OPENER)

1. **Universal-3.5 Pro flagship speech-to-text model** — the newest model family in the cohort (verbatim first-party 2026-07-21); Deepgram is on Nova-2 / Nova-3; AssemblyAI is on Universal-3.5 Pro
2. **99 supported languages** vs Deepgram's narrower list — AssemblyAI's broader multilingual surface
3. **Speech Understanding API as first-class product surface** — Sentiment + Topic + Entity + PII + Auto Chapters + Key Phrases + Content Moderation + Summarization as a single API
4. **Guardrails and Safety + LLM Gateway** — runtime policy enforcement + LLM routing/cost-control surface that Deepgram does NOT ship as a first-party surface
5. **AI Scribes + Medical Transcription** — healthcare-specific use-case lane; Deepgram is contact-center-focused
6. **AI Notetakers** — meeting-product lane (AssemblyAI ships per-meeting summarization; Zoom is a named customer)
7. **Universal-Streaming** — WebSocket streaming variant that supports live-meeting pipelines at sub-300ms latency

## Tier-1 evidence wedge (16-column speech-AI inference + speech-understanding + guardrails receipt)

(1) `audio_call_id` + (2) `utterance_id` + (3) `speaker_id` + (4) `token_count` + (5) `cost_usd` + (6) `latency_ms` captured at every stage (transcribe call + LLM Gateway call + Speech Understanding call + Guardrails call + embedding call + summarization call) with cross-tenant-no-bleed; (7) `asr_model_version_id` (Universal-1 / Universal-2 / Universal-3.5 Pro / Universal-Streaming) + (8) `llm_model_version_id` used as summarizer + (9) `prompt_version_id` + (10) `prompt_experiment_run_id` with eval-result pinning (WER + sentiment + entity-recall + PII-recall + summarization factuality + summarization hallucination); (11) `call_dataset_id` + (12) `call_suite_id` with regression-vs-baseline deltas + (13) `wer_score` + (14) `factuality_score` + (15) `hallucination_score` + (16) `judge_model_version`.

## Compliance posture

- **SOC 2 Type II** (AssemblyAI enterprise posture)
- **HIPAA-eligible** for Medical Transcription + AI Scribes surface
- **GDPR** + **CCPA/CPRA** with **PII Redaction API** as first-party surface
- **Per-deployment-region** + **per-tenant-KMS-key-id** + **per-audit-log-retention** policy for Self-Hosted Voice AI
- **Guardrails and Safety API** ships PII Redaction + toxicity filtering + topic moderation as first-party control surface

## Offer staged

- **$500 / 48h** fixed-scope evidence-gap map — 5-question audit letter filled in with first-party citations from assemblyai.com/, /about, /product/, /enterprise, /demo, /security, /pricing
- **$497/mo** quarterly refresh retainer — first-party product-surface re-validation
- **$497/mo × 5-client YanXbt pattern** — multi-tenant retainer ceiling $2,485 MRR per operator

## Sending notes

- FORM:https://www.assemblyai.com/demo is the sanctioned commercial route (verified live 2026-07-21)
- First-name-only opener; no greeting anti-pattern
- Lane-match: ai_voice_agent_infra vertical (NEW VERTICAL #7), voice-AI deployer-obligation layer at the **ASR/Speech-Understanding/LLM-Gateway boundary**
- No claim of submission, payment, or revenue

*Atlas @ Talon Forge — cron tick 2026-07-21-fast-exec-assemblyai-847*
