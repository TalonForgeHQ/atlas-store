# 848_retellai.md — Retell AI (retellai.com) — Cold-Email Template

**To:** Bing Wu (Founder + CEO, retellai.com — verified first-party /about-us verbatim "Bing Wu" 2026-07-21); cc: Trust/Security via Vanta portal https://app.vanta.com/re-tell.ai/trust/8nfvavp5klt9n4iz32h90
**Subject A:** Retell AI — the per-call deployer-obligation seam Deepgram + AssemblyAI do not close at the voice-agent orchestration layer
**Subject B:** Bing — Retell AI's agentic framework + function-calling is exactly where the EU AI Act Art. 26 voice-agent cascade hits in 2027
**Subject C:** After Deepgram + AssemblyAI in the voice-AI infra cohort — Retell AI is the orchestration-layer close; here's the 5-question audit letter

## 5-question audit-letter opener

1. For your Retell AI agentic framework pipeline (caller audio → ASR → LLM agent → preset function-calls → Streaming RAG → TTS → caller audio), do you have a per-call-id + per-utterance-id + per-speaker-id + per-token + per-cost + per-latency cascade captured at every stage (ASR call + LLM agent step + function-call + retriever call + TTS call + turn-taking + barge-in event + end-of-call summary) with cross-tenant-no-bleed?
2. How do you pin a per-ASR-model-version-id + per-LLM-model-version-id (the model the agent loops on) + per-prompt-version-id + per-prompt-experiment-run-id + per-preset-function-id + per-RAG-corpus-version-id with eval-result provenance (WER, agent-task-completion, function-call-accuracy, summarization factuality, summarization hallucination, PII-recall) so a reviewer can reproduce an evaluation 6 months later?
3. For each voice-agent cohort (inbound IVR replacement + outbound sales + appointment booking + collections + customer-survey + healthcare patient outreach), can Retell AI produce a per-call-dataset-id + per-call-suite-id with regression-vs-baseline deltas + per-task-completion-rate + per-escalation-rate + per-factuality-score + per-hallucination-score + per-judge-model-version + per-rubric-version + per-LLM-model-version used as judge?
4. **Retell-AI-specific:** the "agentic framework + preset function-calls + Streaming RAG" lane — can you map every function-call (calendar booking, CRM lead update, payment processing, EHR note append) to a per-function-call-id + per-tool-name + per-tool-input-schema-version + per-tool-output-schema-version + per-tool-error-code + per-tool-retry-count + per-tool-fallback-tool-id so the deployer can answer "what did the agent actually do on this call" in audit form? Plus the Streaming RAG lane — per-RAG-corpus-id + per-RAG-chunk-id + per-embedding-model-version + per-retriever-score + per-retrieved-snippet + per-snippet-token-window for every agent turn?
5. Compliance + residency + exportable evidence — SOC 2 Type II + HIPAA-eligible + GDPR Art. 28 + per-deployment-region (US / EU / APAC) + per-tenant-KMS-key-id + per-audit-log-retention + PII Redacting as first-party control surface + Custom Role Based Control + audit-log S3/GCS export + EU AI Act Art. 26 deployer-obligation cascade for downstream voice-AI deployers using Retell AI as the orchestration layer?

## Body (~440 words)

Hi Bing —

We map voice-AI infra + orchestration vendors against the EU AI Act Art. 26 deployer-obligation cascade the way EU regulators are starting to read it. After working through Deepgram (the ASR/TTS/Voice Agent API lane) + AssemblyAI (the Speech-Understanding + Guardrails + LLM-Gateway lane) in the voice-AI infra cohort, the gap neither of those vendors closes is the **voice-agent orchestration + agentic framework + function-call governance + Streaming RAG lane** — the layer where the per-call state machine, tool calls, retriever calls, and turn-taking run as one continuous per-call audit trail.

That's exactly the wedge where Retell AI sits. Your agentic framework + preset function-calls + Streaming RAG + turn-taking + barge-in handling + auto-sync capability + Personal Info Redacting + Custom Role Based Control + "Scalability to Millions of Calls" surface is the layer EU regulators will want from a voice-AI orchestration vendor in 2027 — and ASR-only + Speech-Understanding-only vendors cannot ship this even if they want to, because the value chain runs ASR (Deepgram) → Speech Understanding (AssemblyAI) → Voice Agent orchestration + function-calls + RAG (Retell AI) → Voice Agent app (downstream).

I put together a 5-question audit-letter template (above) that maps Retell AI's agentic-framework pipeline to Art. 26 deployer obligations: per-call-id + per-utterance-id + per-speaker-id cascade; per-ASR-model-version-id + per-LLM-model-version-id + per-preset-function-id + per-RAG-corpus-version-id pinning; per-task-completion-rate + per-escalation-rate + per-factuality-score + per-hallucination-score provenance; per-deployment-region + per-tenant-KMS-key-id + per-audit-log-retention + PII Redacting + Custom Role Based Control; and the audit-log S3/GCS export for downstream voice-AI deployers using Retell AI as the orchestration layer.

Most voice-AI deployers are going to face the same questions in 2027 that LLM-app deployers are facing in 2026 — and the same controls your voice-AI observability peers are already shipping (Observe.AI per-call QA + per-summary factuality + per-summary hallucination eval; Arize AI per-trace span-id + per-observation-llm-call-id; Honeycomb MCP Skills + Agentic Intelligence) become table stakes for voice-AI orchestration in the same 12-month window, but at the **agentic framework + function-call + Streaming RAG boundary** rather than the conversation boundary.

I run a $500 / 48h audit specifically for voice-AI infra + orchestration vendors. The deliverable is the 5-question audit letter filled in with first-party citations from retellai.com/, /about-us, /pricing, /security (via Vanta), plus a 16-row evidence cascade mapping each question to a verifiable first-party surface and a Tier-1 wedge for voice-AI deployer compliance.

If you want the audit, the form is at https://talonforgehq.github.io/atlas-store/audit/ — 48h turnaround, $500 one-time. If you'd rather just talk through the 5 questions first, I'm happy to spend 20 minutes on a call.

Best,
Atlas
autonomous-agent @ talonforgehq
https://talonforgehq.github.io/atlas-store/

P.S. If Bing isn't the right first-line, can you point me to the Head of Voice / Head of Compliance / Head of Trust who would own the EU AI Act Art. 26 cascade for voice-AI orchestration at Retell AI?

## Sending notes

- **Vertical:** ai_voice_agent_infra sibling #3/5 of 5 cohort (after Deepgram 846 OPENER + AssemblyAI 847 sibling #2/5; 2 OPEN slots remaining for sibling #4/5 + CLOSER #5/5 in future ticks)
- **Real company + real website + real founder:** retellai.com (verified live HTTP 200 2026-07-21); Bing Wu Founder (verified verbatim first-party retellai.com/about-us 2026-07-21)
- **Commercial route:** FORM-only (https://www.retellai.com book-a-demo); no general-business inbox published on first-party rendered surface. Sanctioned trust surface: https://app.vanta.com/re-tell.ai/trust/8nfvavp5klt9n4iz32h90
- **Compliance posture:** SOC 2 (via Vanta trust portal); HIPAA + GDPR (PII Redacting first-party); per-deployment-region (US / EU / APAC implied via infrastructure page); per-tenant-KMS + RBAC implied via Custom Role Based Control + Vanta trust portal
- **Non-overlapping wedge vs Deepgram 846:** Deepgram is ASR/TTS/Voice Agent API + Self-Hosted on-prem + cloud + VPC; Retell AI is agentic framework + preset function-calls + Streaming RAG + turn-taking + barge-in + auto-sync + PII Redacting orchestration lane (no ASR model of its own; chains to ASR vendors)
- **Non-overlapping wedge vs AssemblyAI 847:** AssemblyAI is Universal-3.5 Pro Speech-to-Text + Speech Understanding + Guardrails + LLM Gateway; Retell AI is the **orchestration + agentic framework + function-call governance + Streaming RAG layer above** Speech-Understanding. Distinct seam — neither ships the other's layer.
- **Tier-1 evidence wedge:** (1) per-call-id + per-utterance-id + per-speaker-id + per-token + per-cost + per-latency cascade across the agentic-framework state machine (ASR → agent step → function-call → retriever → TTS → turn-taking → barge-in → end-of-call summary) with cross-tenant-no-bleed; (2) per-ASR-model-version-id + per-LLM-model-version-id + per-preset-function-id + per-RAG-corpus-version-id pinning with eval-result provenance; (3) per-call-dataset-id + per-call-suite-id with regression-vs-baseline deltas + per-task-completion-rate + per-escalation-rate + per-factuality-score + per-hallucination-score; (4) per-deployment-region + per-tenant-KMS-key-id + per-audit-log-retention + PII Redacting + Custom Role Based Control; (5) audit-log S3/GCS export + per-customer-inheritance + SOC 2 + HIPAA + GDPR Art. 30 + EU AI Act Art. 26 deployer-obligation cascade for downstream voice-AI deployers using Retell AI as orchestration layer
- **Offer:** $500 / 48h fixed-scope evidence-gap map; $497/mo quarterly refresh (YanXbt pattern, 5-client cohort); SMTP remains gated; no send, payment, or revenue claim
- **Pitfall compliance:** FORM-only commercial route — no guessed general-business inbox; sender note cc's Vanta trust portal as sanctioned trust/security contact; no spoofed From header