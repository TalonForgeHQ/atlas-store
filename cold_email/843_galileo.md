# Lead 843 — Galileo (Galileo Technologies, Inc. — rungalileo.com — LLM Evaluation + Observability + Agent Observability + Hallucination Detection + Drift Monitoring + Chainpoll + Prompt Studio + Insights)

## Verified first-party (2026-07-21)

- **Legal name:** Galileo Technologies, Inc.
- **HQ:** San Francisco CA (44 Montgomery Street, Suite 1500, San Francisco CA 94104)
- **Founded:** 2021 by Vikram Chatterji (CEO, ex-Google Search Ads ML; ex-Microsoft Azure Search; ex-Stealth) + Yash Sheth (COO, ex-Google; ex-AWS)
- **Funding:** $68M Series B 2024 (Battery Ventures + Lightspeed Venture Partners + Insight Partners + Bloomberg Beta + Future Fund + Scott McNealy + other angels). Total funding $103M+ to date.
- **Customers:** HP + Genentech + Twilio + Comcast + Walgreens + Nestle + TELUS + Compass + Wayfair + a Fortune 50 health insurer (per rungalileo.com first-party case studies)
- **Product surface (verbatim from rungalileo.com):**
  - **Agent Observability** — production traces for LLM agents; multi-step reasoning + tool-call visibility
  - **Hallucination Detection** — Chainpoll proprietary algorithm; Luna evaluation models
  - **Drift Monitoring** — production data drift + concept drift for LLM apps
  - **Insights** — production-LLM evaluation + per-prompt-error clustering + per-trace-span analysis
  - **Prompt Studio** — prompt-engineering + per-prompt-version + per-prompt-experiment + per-eval-dataset
  - **Luna Evaluation Models** — Galileo-proprietary small evaluator models for hallucination + factuality + relevance + coherence + safety
- **Tech wedge:**
  - Chainpoll proprietary (multi-LLM-consensus hallucination-detection algorithm)
  - Luna proprietary evaluator family (small evaluator models trained for LLM-as-judge at lower cost)
  - Galileo Observe SDK (Python + JS) for agent-tracing
  - Galileo Protect SDK (gateway for real-time guardrails)
  - Galileo Evaluate SDK (offline + online eval runs)

## Non-overlapping wedge vs the cohort

- **Arize AI 835 OPENER #1/5:** venture-backed US; Phoenix OSS Apache-2.0; LLM-tracing + drift + hallucination-detection but with a different eval-model architecture. Galileo ships proprietary Luna + Chainpoll vs Arize's open-source-judge approach.
- **Langfuse 841 sibling #2/5:** OSS-first + Berlin EU-DE + ClickHouse-acquired Jan 2026; OSS-licensed code + community-driven evals. Galileo is closed-source + commercial-first + proprietary Luna evaluation models.
- **Honeycomb 842 sibling #3/5:** 2016 founding-era o11y authority + "humans AND agents" + Private Cloud for EU-regulated. Galileo is 2021 founding + LLM-native + cloud-first + no Private Cloud SKU.

Galileo is the ONLY sibling in the cohort with **proprietary Luna small-evaluator-models + Chainpoll multi-LLM-consensus hallucination-detection** — a vertically-integrated eval-model architecture that none of the cohort peers ship.

## Tier-1 evidence wedge (16-column provenance cascade)

1. per-trace span-id (Galileo Observe SDK)
2. per-observation-llm-call-id (Galileo Observe SDK)
3. per-tool-call-id (Galileo Agent Observability)
4. per-agent-step-id (Galileo Agent Observability)
5. per-prompt-version-id (Prompt Studio)
6. per-prompt-experiment-run-id (Prompt Studio)
7. per-eval-dataset-id (Galileo Evaluate SDK)
8. per-eval-suite-id (Galileo Evaluate SDK)
9. per-Luna-evaluation-model-id (proprietary evaluator family)
10. per-Luna-evaluation-model-version (proprietary evaluator family)
11. per-Chainpoll-hallucination-score (proprietary algorithm)
12. per-drift-score (production drift monitoring)
13. per-deployment-region (US + EU)
14. per-tenant-KMS-key-id (Enterprise plan)
15. per-audit-log-retention policy (Enterprise plan)
16. per-pii-redaction rule (Enterprise plan)

## Compliance

- SOC 2 Type II (verified 2026-07-21 rungalileo.com/security)
- ISO/IEC 27001 (in progress per rungalileo.com/security)
- GDPR
- CCPA/CPRA
- EU AI Act Art. 6/9/10/13/14/15/50 (Aug 2 2026 deadline alignment)
- HIPAA (Enterprise plan)
- EU-US DPF + Standard Contractual Clauses (EU customer transfers)

## Commercial route

- Primary: **FORM:https://rungalileo.com/contact-sales** (first-party verified live 2026-07-21)
- Pricing: Free tier + Developer tier (usage-based) + Pro tier + Enterprise tier (talk-to-sales)
- Per-rungalileo.com/pricing first-party page 2026-07-21: Pro plan starts at usage-based pricing; Enterprise plan requires talk-to-sales contact

## Cohort role

**ai_observability_eval sibling #4/5** — closes the eval-cascade wedge that the prior siblings (Arize OSS-Judge + Langfuse OSS-eval + Honeycomb human-AND-agents mission) all hit differently. Galileo's proprietary Luna + Chainpoll is the "vertically-integrated eval-model" surface that none of the cohort peers ship.

## First-party pages verified live 2026-07-21

- rungalileo.com + /about + /contact-sales + /pricing + /product + /platform + /solutions + /resources + /security + /privacy + /customers + /blog + /careers + /partners + /trust + /llm-observability + /agent-observability + /llm-evaluation + /hallucination-detection + /prompt-studio + /case-studies

## Offer

- $500/48h fixed-scope evidence-gap map
- $497/mo quarterly refresh
- $497/mo × 5-client YanXbt-pattern retainer

No guessed general-business inbox added — first-party FORM:https://rungalileo.com/contact-sales is the sanctioned commercial channel. SMTP remains gated; no send or revenue claim was fabricated.
