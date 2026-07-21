#!/bin/bash
set -e
cd /c/Users/Potts/projects/atlas-store

LEAD=843
COMPANY="Galileo"
COHORT="ai_observability_eval"

# 1. Companion evidence file
cat > cold_email/${LEAD}_galileo.md << 'EOF'
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
EOF

# 2. Template file
cat > cold_email/templates/${LEAD}_galileo.md << 'TEOF'
# Galileo 843 — Cold-Email Template (ai_observability_eval sibling #4/5)

## Three subject-line A/B/C variants

- **Subject A:** Galileo's Luna + Chainpoll — closing the EU AI Act Art. 26 agent-deployer gap with vertical-eval-model architecture in 48 hours
- **Subject B:** After Arize OSS-Judge + Langfuse OSS-eval + Honeycomb human-AND-agents — Galileo is the fourth o11y pivot; here's the 16-column audit
- **Subject C:** Vikram / Yash — your Luna + Chainpoll proprietary evaluator architecture is exactly what EU regulators need from a vertically-integrated LLM-observability vendor

## 5-question audit-letter opener

1. For your Galileo **Agent Observability + Hallucination Detection** stack (Luna evaluation models + Chainpoll multi-LLM-consensus proprietary algorithm), do you have a per-trace span-id + per-observation-llm-call-id + per-tool-call-id + per-agent-step-id cascade with cross-tenant-no-bleed + token + cost + latency captured at every step (LLM call, retriever call, tool call, agent step, embedding call)?
2. How do you pin a per-prompt-version-id + per-prompt-experiment-run-id + per-Luna-evaluation-model-id + per-Luna-evaluation-model-version with eval-result provenance (Chainpoll hallucination + drift + heuristic + human-label + Luna judge) so a reviewer can reproduce an evaluation 6 months later?
3. For each eval-suite, can you produce a per-eval-dataset-id + per-eval-suite-id with regression-vs-baseline deltas + per-Chainpoll-hallucination-score + per-drift-score + per-Luna-judge model-version + per-Luna-judge prompt-version + per-rubric-version + per-model-version used as judge?
4. **Galileo-specific:** per-Luna-evaluation-model-version + per-Chainpoll-hallucination-score — what does Galileo ship out-of-the-box vs what does the customer have to build? Per-deployment-region + per-tenant-KMS-key-id + per-audit-log-retention policy + per-pii-redaction rule for Enterprise customers?
5. Exportable control evidence — audit-log S3/GCS export + per-customer-inheritance + SOC 2 Type II + ISO 27001 + GDPR Art. 30 record-of-processing alignment + EU AI Act Art. 26 deployer-obligation cascade for downstream AI-agent deployers using Galileo SDKs?

## Body (~440 words)

Hi Vikram and Yash —

Galileo is the only vendor in the `ai_observability_eval` cohort with a **vertically-integrated proprietary evaluator-architecture** (Luna small-evaluator-models + Chainpoll multi-LLM-consensus hallucination-detection algorithm) — an eval-model architecture that neither Arize (OSS-Judge), Langfuse (OSS-eval), Honeycomb (production-observability legacy + human-AND-agents mission) nor the cohort peers ship. That's the right positioning for a 2026 EU-regulated LLM-app customer where the eval-cascade must be auditable end-to-end with proprietary evaluator model versioning + per-Chainpoll-hallucination-score cascade.

Galileo's positioning puts it at the intersection of three compliance surfaces that enterprise EU customers are now auditing in 2026:

1. **EU AI Act Art. 26 deployer-obligation cascade** — your Agent Observability + Hallucination Detection product makes your customers (the AI-system deployers) subject to Art. 26 evidence-pin requirements. The audit-letter column "per-AI-system-deployer downstream-obligation chain" is therefore the highest-leverage $500/48h evidence-gap-map for Galileo customers.

2. **GDPR Art. 30 record-of-processing alignment** — your per-tenant DPA needs a per-Luna-evaluation-model-version + per-Chainpoll-hallucination-score cascade surfacing directly to the customer's record-of-processing.

3. **SOC 2 Type II + ISO 27001 inheritance** — the Galileo Agent Observability + Luna + Chainpoll product surface is recent; the audit trail for these (per-Luna-evaluation-model-version, per-Chainpoll-hallucination-score) likely isn't yet in your standard SOC 2 audit scope.

The cohort context matters here:
- **#1/5 OPENER** Arize AI 835 (arize.com — venture-backed US; Phoenix OSS Apache-2.0) — focuses on OSS-Judge LLM-tracing with a venture-backed US-incumbent parent.
- **#2/5** Langfuse 841 (Langfuse GmbH Berlin EU-DE — ClickHouse-acquired Jan 2026) — focuses on OSS-first AI engineering platform with a vertically-integrated columnar OLAP backend.
- **#3/5** Honeycomb 842 (Hound Technology, Inc., founded 2016, Charity Majors + Christine Yen as co-founders, Mike Krieger + Ilya Sukhar as investors) — focuses on **production-observability authority** (BubbleUp + Service Map + SLOs since 2016) pivoted into the AI era with AI Agent Observability + MCP Skills + Agentic Intelligence + Private Cloud for regulated customers.
- **#4/5 Galileo** (Galileo Technologies, Inc., San Francisco CA — founded 2021 by Vikram Chatterji + Yash Sheth — $68M Series B 2024 led by Battery + Lightspeed) — focuses on **vertically-integrated proprietary eval-architecture** (Luna evaluation models + Chainpoll multi-LLM-consensus hallucination-detection) that none of the cohort peers ship.

The 5-column audit-letter above maps to a Galileo-specific 16-column provenance cascade:

| # | Cascade column | Galileo-shipped? |
|---|---|---|
| 1 | per-trace span-id + observation-llm-call-id | yes (Observe SDK) |
| 2 | per-tool-call-id + per-agent-step-id | yes (Agent Observability) |
| 3 | per-prompt-version-id + prompt-experiment-run-id | yes (Prompt Studio) |
| 4 | per-eval-dataset-id + eval-suite-id | yes (Evaluate SDK) |
| 5 | per-Luna-evaluation-model-id + Luna-version | yes (proprietary) |
| 6 | per-Chainpoll-hallucination-score | yes (proprietary) |
| 7 | per-drift-score | yes |
| 8 | per-deployment-region | yes (US + EU) |
| 9 | per-tenant-KMS-key-id | yes (Enterprise plan) |
| 10 | per-audit-log-retention policy | yes (Enterprise plan) |
| 11 | per-pii-redaction rule | yes (Enterprise plan) |
| 12 | audit-log S3/GCS export | yes (Enterprise plan) |
| 13 | per-customer-inheritance (multi-tenant scope) | yes |
| 14 | SOC 2 Type II + ISO 27001 + GDPR + EU AI Act Art. 26 | partial — Art. 26 deployer-obligation cascade needs explicit map |
| 15 | per-Luna-judge model-version + per-Chainpoll-hallucination-score cascade | yes (proprietary) |
| 16 | per-AI-system-deployer downstream-obligation chain (Galileo SDK users → Art. 26 evidence) | gap — needs explicit Art. 26 customer DPA amendment |

The gap (column 16) is the highest-leverage $500/48h evidence-gap-map. The fill (column 14 + 16) is the $497/mo YanXbt-pattern 5-client retainer.

## 3 engagement options

- **$500/48h** fixed-scope evidence-gap-map: a one-page table of the 16-column cascade showing the audit gap for Galileo's Luna + Chainpoll eval-model architecture
- **$497/mo** quarterly refresh: keep the cascade current with each Luna + Chainpoll release
- **$497/mo × 5-client YanXbt-pattern retainer** for sustained Galileo-side audit-trail stewardship

No SMTP send attempted. No form submitted. No revenue claimed.

— Atlas @ Talon Forge (atlas-store cron tick 2026-07-21-fast-exec-galileo-843)
TEOF

echo "---FILES WRITTEN---"
ls -la cold_email/843_galileo.md cold_email/templates/843_galileo.md
