---
name: Confident AI
lead_id: 904
vertical: ai_llm_observability
position: sibling-4-of-5
commercial_route: FORM:https://www.confident-ai.com/book-a-demo
founders: Jeffrey Ip (Co-founder) + Kritin Vongthongsri (Co-founder) — first-party JSON-LD on /about
---

# Template 904 — Confident AI — ai_llm_observability sibling #4/5

## Subject variants

1. `Confident AI + DeepEval — buyer-ready eval evidence map?`
2. `Can a reviewer replay every DeepEval decision?`
3. `Five joins for Confident AI enterprise eval procurement`

## Email

Hi Jeffrey and Kritin —

I'm Atlas at Talon Forge. I mapped Langfuse, Arize AI, and Honeycomb as the first three members of an AI-LLM-observability cohort. Confident AI adds a distinct evaluation-native lane: the platform is built by the creators of DeepEval and positions itself around evaluating, observing, and improving LLM applications.

For an enterprise buyer reviewing a production evaluation program, I would test five joins:

1. `tenant_id → application_id → eval_run_id → dataset_id → test_case_id → metric_id → score_id → judge_model_version` so every score can be replayed without losing tenant or dataset scope.
2. `prompt_version → model_name → model_version → input_hash → output_hash → rubric_version → evaluator_version` so a release reviewer can distinguish a model regression from an evaluator or prompt change.
3. DeepEval test definitions, custom metrics, thresholds, retries, and pass/fail decisions joined to the exact CI or deployment event that promoted or blocked a release.
4. Online observation and feedback joined back to the offline evaluation case, including trace/span identity, user-feedback event, remediation decision, and the subsequent re-run result.
5. Retention, deletion, export, sub-processor, and cross-tenant authorization evidence for prompts, datasets, traces, evaluator outputs, and generated responses.

The fixed-scope offer is a $500 / 48h evidence-gap map, followed by an optional $497/month quarterly refresh. The deliverable is a buyer-ready join table plus the smallest set of missing evidence a security, legal, or procurement reviewer would ask for.

Would a one-page sample for one DeepEval release path be useful? The commercial route I verified is your first-party Book a Demo page: https://www.confident-ai.com/book-a-demo

Best,
Atlas
Talon Forge

## Why this is specific to Confident AI

- First-party `/about` JSON-LD identifies Confident AI as an evaluation platform built by the creators of DeepEval.
- The same first-party JSON-LD names Jeffrey Ip and Kritin Vongthongsri as co-founders and gives a founding date of 2023-11.
- The first-party `/book-a-demo` page is the sanctioned commercial route; no general-business inbox is guessed.
- The wedge is evaluation-native release evidence: DeepEval test definitions and evaluator decisions joined to prompt/model versions, traces, and deployment gates.

## Evidence questions for a discovery call

1. Which `eval_run_id` and dataset-version fields are exportable today?
2. Can custom metrics and judge-model versions be pinned at score level?
3. Are online traces and offline DeepEval cases joinable without a manual correlation step?
4. What deletion and retention receipts are available for evaluator inputs and outputs?
5. Which tenant and sub-processor boundaries are visible to an external reviewer?

## Cohort context

- Langfuse 888 — OPENER #1/5: EU GmbH, YC W23, MIT open source, LLM tracing and prompt management.
- Arize AI 889 — sibling #2/5: Arize AX + Phoenix OSS, multimodal evaluation and observability.
- Honeycomb 890 — sibling #3/5: OpenTelemetry-native production debugging, Agent Timeline, MCP, and Private Cloud.
- Confident AI 904 — sibling #4/5: DeepEval-native evaluation and release-quality evidence.
- One CLOSER slot remains; a fresh candidate must be independently verified before shipping.

## Commercial guardrails

- Route: `FORM:https://www.confident-ai.com/book-a-demo`
- No guessed sales, support, privacy, or security inbox.
- SMTP is gated. This template is queued-not-sent; no submission, delivery, payment, or revenue is claimed.
- Offer: `$500 / 48h` fixed-scope audit or `$497 / month` quarterly refresh.
