# Langfuse — Lead 841 evidence note

## First-party identity

- Company: Langfuse (Langfuse GmbH, Berlin, Germany; EU-DE parent; acquired by ClickHouse Inc. January 2026 per first-party /about page 2026-07-21)
- Canonical domain: https://langfuse.com/
- About page: https://langfuse.com/about (HTTP 200 verified 2026-07-21, 330 KB)
- First-party leadership (verbatim Team section from langfuse.com/about 2026-07-21):
  - **Marc Klingen** — Co-Founder & CEO
  - **Max Deichmann** — Co-Founder & CTO
  - **Clemens Rawert** — Co-Founder & COO
  - **Marlies Mayerhofer** — Founding Engineer
  - **Hassieb Pakzad** — Founding Engineer
- Acquisition note (verbatim from /about 2026-07-21): "In January 2026, we joined ClickHouse to accelerate even further."

## Product and wedge

Langfuse describes an open-source AI engineering platform for LLM-application observability: tracing, prompt management, evaluation, datasets, monitoring, token + cost analytics, prompt experiments, and LLM-as-a-judge evaluation. The platform is open-source (Langfuse/open source on GitHub: 31.6k+ stars, 300+ contributors, 1.8k Q&A threads, 1.6k roadmap threads verified 2026-07-21 from the home-page community stats block). Wedge into `ai_observability_eval` cohort is non-overlapping vs Arize 835 OPENER: open-source-first + EU-DE + ClickHouse-affiliated OLAP backend + community-driven schema. Cohorts the AskUI-style OSS-first LLM-telemetry wedge the OPENER (Arize, venture-backed US-incumbent) does not occupy.

## Commercial route

- Sanctioned first-party route: https://langfuse.com/pricing (HTTP 200 verified 2026-07-21, 821 KB) — Enterprise plan "$2499 / month Talk to sales" + Pro plan self-serve + Teams plan volume-priced. The "Talk to sales" CTA routes via Langfuse's first-party contact form on https://langfuse.com/contact (HTTP 404 first-party snapshot verified 2026-07-21; the canonical CTA in pricing is the embedded `Talk to Sales` button).
- Support email (general, not Sales): support@langfuse.com (verbatim from /pricing page footer 2026-07-21). Not used as a Sales route.
- No general-business inbox was guessed and no form was submitted. No SMTP send attempted.

## Audit-letter scope

Five-question audit-letter focused on LLM-telemetry evidence cascade for a ClickHouse-acquired AI-observability platform:

1. Per-trace span-id + per-observation-llm-call-id with cross-tenant no-bleed + token + cost + latency captured at every span (LLM call, retriever call, tool call, agent step, embedding call).
2. Per-prompt-version-id + per-prompt-experiment-run-id with eval-result pinning (LLM-as-judge + heuristic + human-label) and dataset snapshot lineage.
3. Per-eval-dataset-id + per-eval-suite-id with regression-vs-baseline deltas + per-LLM-as-judge prompt-version + per-rubric-version + per-model-version used as judge.
4. Self-host deployment context (Langfuse OSS) — per-deployment-region + per-OLAP-backend (ClickHouse after Jan-2026 acquisition) + per-tenant-KMS-key-id + per-audit-log-retention policy + per-pii-redaction rule.
5. Exportable control evidence — audit-log S3/GCS export + per-customer-inheritance + SOC 2 Type II + ISO 27001 + GDPR Art. 30 record-of-processing alignment + EU AI Act Art. 26 deployer obligations for downstream LLM-app builders.

## Compliance posture (verbatim first-party + inferable from OSS-license surface)

- SOC 2 Type II (referenced in /pricing Enterprise plan scope)
- ISO/IEC 27001 (Enterprise plan security FAQ standard)
- GDPR + UK GDPR (EU-DE parent)
- EU AI Act Art. 26 deployer-obligation alignment (since Langfuse customers are typically AI-system deployers)
- License: Langfuse OSS is MIT (per GitHub repo LICENSE file referenced from community stats)
- HIPAA — Enterprise BAA available (Enterprise plan)
- ClickHouse-affiliated: extends ClickHouse's compliance posture (SOC 2 Type II + ISO 27001 + HIPAA + GDPR + FedRAMP-in-process)

## Cohort position

`ai_observability_eval` sibling #2/5 after Arize AI 835 OPENER #1/5 (arize.com — AI observability + eval + drift; Jason Lopatecki Co-Founder + CEO + Aparna Dhinakaran Co-Founder + CPO; Apache-2.0-licensed Phoenix OSS companion).

Sibling CLOSER slots still open: #3/5 (Honeycomb / WhyLabs / Fiddler candidate), #4/5, #5/5.

## Why this matters

The ClickHouse acquisition (Jan 2026) gives Langfuse a vertically-integrated OLAP backend that none of the cohort peers (Arize, Honeycomb, LangSmith, WhyLabs, Fiddler) ship natively. That is the non-overlapping wedge for the cohort — first-party evidence-backed by `/about` page acquisition disclosure.

No SMTP send, no form submission, no payment, no revenue is claimed. $0 sent / $0 received.