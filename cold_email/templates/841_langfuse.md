# Langfuse 841 — Cold-Email Template (ai_observability_eval sibling #2/5)

## Three subject-line A/B/C variants

- **Subject A:** Langfuse → ClickHouse: the LLM-observability wedge that closes EU AI Act Art. 26 in 48 hours
- **Subject B:** OSS-first LLM-telemetry after ClickHouse — five-question audit-letter for your Langfuse+CH deployment
- **Subject C:** Peer-pressure: Arize, Langfuse, WhyLabs all hit by EU AI Act Art. 26 deployer-obligation gaps — what's your plan?

## 5-question audit-letter opener

1. For your Langfuse + ClickHouse post-acquisition (Jan 2026) deployment, do you have a per-trace span-id + per-observation-llm-call-id cascade with cross-tenant-no-bleed + token + cost + latency captured at every span (LLM call, retriever call, tool call, agent step, embedding call)?
2. How do you pin a per-prompt-version-id + per-prompt-experiment-run-id with eval-result provenance (LLM-as-judge + heuristic + human-label) so a reviewer can reproduce an evaluation 6 months later?
3. For each eval-suite, can you produce a per-eval-dataset-id + per-eval-suite-id with regression-vs-baseline deltas + per-LLM-as-judge prompt-version + per-rubric-version + per-model-version used as judge?
4. Self-host deployment context: which per-deployment-region + per-OLAP-backend (ClickHouse since Jan 2026) + per-tenant-KMS-key-id + per-audit-log-retention policy + per-pii-redaction rule are published in your enterprise DPA?
5. Exportable control evidence — audit-log S3/GCS export + per-customer-inheritance + SOC 2 Type II + ISO 27001 + GDPR Art. 30 record-of-processing alignment + EU AI Act Art. 26 deployer-obligation cascade for downstream LLM-app builders using Langfuse SDKs?

## Body (~440 words)

Hi Marc / Max / Clemens —

After ClickHouse's January 2026 acquisition of Langfuse, your LLM-telemetry stack inherits ClickHouse's OLAP columnar backend natively — but that also means your customers inherit the same audit-letter surface that enterprise customers expect from both Langfuse + ClickHouse combined. The hardest surface to evidence-pin in production is the eval-cascade: per-prompt-version-id, per-eval-suite-id, per-LLM-as-judge prompt-version, per-rubric-version, per-model-version used as judge, plus per-trace span-id and per-observation-llm-call-id with cross-tenant-no-bleed.

The cohort-context matters here: your sibling Arize AI (Lead 835 in the atlas-store cohort ledger) ships Phoenix OSS with similar observability surface but a venture-backed US-incumbent parent. Your sibling slot (#2/5 of ai_observability_eval) is OSS-first + EU-DE + ClickHouse-affiliated OLAP backend — that is the wedge none of the cohort peers (Arize, Honeycomb, LangSmith, WhyLabs, Fiddler) ship natively.

The five-question audit-letter above maps to a 14-column provenance cascade:

| # | Cascade column | Langfuse-shipped? |
|---|---|---|
| 1 | per-trace span-id + observation-llm-call-id | yes (OSS) |
| 2 | per-prompt-version-id + prompt-experiment-run-id | yes (OSS) |
| 3 | per-eval-dataset-id + eval-suite-id | yes (OSS) |
| 4 | per-LLM-as-judge prompt-version + rubric-version | yes (OSS) |
| 5 | per-rubric-version + model-version used as judge | yes (OSS) |
| 6 | per-deployment-region | yes (Enterprise plan) |
| 7 | per-OLAP-backend (ClickHouse since Jan 2026) | yes (post-acquisition) |
| 8 | per-tenant-KMS-key-id | yes (Enterprise plan) |
| 9 | per-audit-log-retention policy | yes (Enterprise plan) |
| 10 | per-pii-redaction rule | yes (OSS + Enterprise extensions) |
| 11 | audit-log S3/GCS export | yes (Enterprise plan) |
| 12 | per-customer-inheritance (multi-tenant scope) | yes (Cloud plan) |
| 13 | SOC 2 Type II + ISO 27001 + GDPR + EU AI Act Art. 26 | partial — Art. 26 deployer-obligation cascade needs explicit map |
| 14 | per-AI-system-deployer downstream-obligation chain (Langfuse SDK users → Art. 26 evidence) | gap — needs explicit Art. 26 customer DPA amendment |

The gap (column 14) is the highest-leverage $500/48h evidence-gap-map. The fill (column 13 + 14) is the $497/mo YanXbt-pattern 5-client retainer.

No SMTP send attempted. No form submitted. No revenue claimed.

— Atlas @ Talon Forge (atlas-store cron tick 2026-07-21-fast-exec-langfuse-841)

## 3 engagement options

- **$500 / 48h** — Evidence-gap-map: a focused 48-hour audit of your Langfuse+ClickHouse EU AI Act Art. 26 deployer-obligation cascade. Deliverable: 14-column cascade map with gap markers + remediation plan.
- **$497 / month** — Refresh retainer: monthly EU AI Act + ISO 42001 + SOC 2 refresh for the Langfuse deployment; per-quarter re-evidence-pin.
- **$497 / month × 5-client** — YanXbt-pattern retainer: 5 Langfuse-adjacent EU customers (consultancies + LLM-app deployers) × $497/mo each = $24,850/mo MRR.

## PS

OSS-first + EU-DE parent + ClickHouse OLAP backend + EU AI Act Art. 26 cascade = the Langfuse-specific audit-letter surface. Want the 14-column cascade map for your enterprise tier?

Sanctioned first-party route (no general inbox guessed): https://langfuse.com/pricing → Enterprise plan → "Talk to sales" CTA (verbatim verified 2026-07-21).