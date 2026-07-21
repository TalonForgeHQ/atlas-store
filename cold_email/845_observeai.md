# Lead 845 — Observe.AI

## Vendor research packet

**Company:** Observe.AI
**Domain:** observe.ai
**Vertical:** ai_voice_agent_observability (NEW VERTICAL #6, OPENER #1/5)
**Tier:** 1
**Commercial route:** FORM:https://www.observe.ai/demo (HubSpot/Marketo form, verified live 2026-07-21; /contact 301 → /demo)

## Founder / leadership (first-party verified)

- **Swapnil Jain — CEO & Co-Founder** (verbatim /about-us/ "Swapnil Jain ... CEO & Co-Founder")
- (CTO, COO presence confirmed in /about-us/ but leadership page not separately exposed)
- LinkedIn canonical: https://www.linkedin.com/company/observeai/

## Investors (first-party verified, /about-us/)

- Menlo Ventures
- Nexus Venture Partners
- Scale Venture Partners
- Insight Partners
- Wing

## Product surface (first-party verified)

- Conversational-AI observability + agent coaching for contact centers
- 100% call analysis + post-call summarization + real-time agent assist
- LLM-powered transcription + sentiment + intent detection
- Quality assurance workflow automation
- Live-call guidance / next-best-action
- Voice-AI agent eval + drift monitoring (relevant cohort wedge)

## First-party pages verified live 2026-07-21

- https://www.observe.ai/ — HTTP 200, home (490KB)
- https://www.observe.ai/about-us/ — HTTP 200 (109KB, Swapnil Jain "CEO & Co-Founder" + investor list)
- https://www.observe.ai/contact — HTTP 200, redirects to /demo
- https://www.observe.ai/demo — HTTP 200 (HubSpot/Marketo form)
- https://www.observe.ai/pricing — HTTP 200 (Pro / Enterprise surface)
- https://www.crunchbase.com/organization/observe-ai — third-party corroboration on founder + investors

## Cohort wedge

Observe.AI is the OPENER of NEW VERTICAL #6 ai_voice_agent_observability — a cohort that catches the contact-center + voice-AI deployer obligation gap that none of the prior cohort verticals (ai_observability_eval, ai_data_context_observability, ai_data_catalog_governance, ai_governance_risk_compliance, ai_intent_data_enrichment) explicitly cover. Voice agents create their own Art. 26 deployer-obligation cascade (transcript retention, consent recording, real-time monitoring, eval drift on call summaries).

## Audit-letter 5-question vertical pivot (voice-AI agent deployers)

1. For your voice-agent conversation pipeline (transcribe → LLM summarize → sentiment → intent → QA score), do you have a per-call-id + per-speaker-id + per-utterance-id + per-tool-call-id cascade with cross-tenant-no-bleed + token + cost + latency captured at every step (transcribe call, LLM summarize call, embedding call, QA rule eval, agent-assist lookup)?
2. How do you pin a per-prompt-version-id + per-prompt-experiment-run-id + per-LLM-model-version (Whisper / GPT-4o / Claude / custom) + per-summary-prompt-version with eval-result provenance (sentiment label + intent label + QA score + drift + silence ratio + talk-ratio + escalation flag) so a reviewer can reproduce an evaluation 6 months later?
3. For each voice-agent cohort, can you produce a per-call-dataset-id + per-call-suite-id with regression-vs-baseline deltas + per-summary-bleu-score + per-summary-factuality-score + per-summary-hallucination-score + per-summary-judge-model-version + per-rubric-version + per-LLM-model-version used as summarizer?
4. **Observe.AI-specific:** per-recording-retention-policy + per-pii-redaction-on-transcript (PCI / SSN / names / addresses) + per-call-recording-consent-bit + per-tenant-KMS-key-id + per-deployment-region (US / EU / APAC) + per-audit-log-retention — what does Observe.AI ship out-of-the-box vs what does the customer have to build?
5. Exportable control evidence — audit-log S3/GCS export + per-customer-inheritance + SOC 2 Type II + ISO 27001 + GDPR Art. 30 record-of-processing + EU AI Act Art. 26 deployer-obligation cascade for downstream voice-agent deployers using Observe.AI APIs + per-call-recording-bit + per-call-pii-redaction-bit + per-recording-consent-bit?

## Offer

- $500 / 48h audit (per the Atlas Audit pattern, GRAND_PLAN.md Phase 3 Path B)
- $497 / mo retainer (per YanXbt pattern)

## Pitfalls honored

- Form-only commercial route; no guessed general-business inbox.
- HubSpot/Marketo /demo is the first-party sanctioned CTA.
- Founder verified verbatim from first-party /about-us/.
- Investors verified verbatim from first-party /about-us/.
- 5-question audit-letter opens against voice-agent deployer obligations.
- No claim of form submission, email delivery, payment, or revenue.