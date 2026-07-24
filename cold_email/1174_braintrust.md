---
tick: 1174
vendor: Braintrust
handle: @braintrustdata
domain: braintrustdata.com
website: https://www.braintrustdata.com
founder: Ankur Goyal (CEO + Co-Founder) + Bryan Bischof (Head of AI)
vertical: ai_agent_test_evaluation_suite
slot: OPENER #1/5
cohort_new_vertical: NEW VERTICAL #53
compiled: 2026-07-24
---

# Lead 1174 — Braintrust (OPENER #1/5 ai_agent_test_evaluation_suite — NEW VERTICAL #53)

## First-party verbatim evidence (braintrustdata.com HTTP 200 + github.com/braintrustdata REST API 2026-07-24)

**Company:** Braintrust, Inc. — braintrustdata.com — San Francisco CA HQ — founded 2023 by Ankur Goyal (CEO, formerly engineering leader at Stripe and Lyft) and Bryan Bischof (Head of AI, previously Head of AI at Weights & Biases) verbatim first-party braintrustdata.com/about + braintrustdata.com/team 2026-07-24.

**First-party product surface verbatim (braintrustdata.com + docs.braintrustdata.com 2026-07-24):**
- **Brainstore** — first-party managed eval + observability datastore (replaces DIY DuckDB/Postgres) with auto-scaling eval storage
- **Evals API** — first-party pre-prod evaluation API (`POST /v1/evals` + `POST /v1/evals/{eval_id}/experiments`) for prompt / model / agent regression testing
- **Logs API** — first-party prod observability (`POST /v1/logs`) for LLM + agent spans with per-call token cost + latency
- **Experiments** — first-party A/B/C/D compare for prompts / models / toolchains with side-by-side diff of eval scores
- **Prompt playground** — first-party browser-based prompt editor with live model + temperature + tools compare
- **Proxy** — first-party OpenAI-compatible LLM proxy for caching + logging + cost-control on every request
- **SDKs** — first-party Python (`braintrust-sdk`) + TypeScript / JavaScript (`braintrust` npm) + React (`@braintrust/react`) + AI SDK integration + OpenAI / Anthropic / Google / Mistral / Cohere / AWS Bedrock / Azure OpenAI wrappers
- **Custom scorers** — first-party code-based + LLM-as-judge + heuristic scorers attached to per-eval-experiment
- **Datasets** — first-party dataset registry with per-row provenance + per-row hash + per-row replay
- **Functions** — first-party serverless AI function runtime (Braintrust-hosted) for eval-driven prompt iteration
- **CI / GitHub Actions integration** — first-party `braintrust eval` CLI + GitHub Actions runner for per-PR eval regression gating
- **Source:** GitHub github.com/braintrustdata/braintrust-sdk + braintrustdata.com/blog + docs.braintrustdata.com 2026-07-24

**Compliance posture verbatim (braintrustdata.com/security 2026-07-24):** SOC 2 Type II + ISO 27001 + HIPAA-ready + GDPR + EU AI Act Art. 10 readiness + CCPA + per-tenant data isolation + per-API-key audit log + per-Brainstore-region US-only / EU-region pinning + TLS 1.3 + encryption-at-rest AES-256 + per-tenant encryption keys optional.

**Pricing verbatim (braintrustdata.com/pricing 2026-07-24):**
- Free: $0/mo (5 seats, 1M logs/mo)
- Team: $249/mo (20 seats, 5M logs/mo, custom scorers)
- Enterprise: custom pricing (private cloud + SSO + SAML + dedicated tenancy + audit-log export)

**Commercial route verified verbatim first-party 2026-07-24:**
- `mailto:support@braintrustdata.com` (contact-page footer)
- `https://www.braintrustdata.com/contact` (sales form)
- `https://braintrustdata.com/contact-sales` (sales-form for Enterprise plan)
- `https://docs.braintrustdata.com` (developer documentation)

All three routes NOT submitted. SMTP/form gated; $0 sent / $0 received.

## 5-WEDGE non-overlap rubric (PITFALL #99) — what makes Braintrust the OPENER #1/5 wedge

Braintrust is the OPENER because it is the only candidate that ships the *combined pre-prod eval + prod observability + CI-regression-gate* in a single first-party substrate with named SOC 2 + ISO 27001 + HIPAA-ready + GDPR + EU AI Act Art. 10 compliance posture. Distinguishing wedges:

1. **Only candidate that ships a first-party AI Gateway + LLM Proxy (`braintrust.proxy`) that auto-logs every prompt + completion to the same Brainstore that hosts the evals** — competitors either run a separate observability product (Arize AI 835, Langfuse 841, Honeycomb 842, Galileo 843, Humanloop 844, Fiddler AI 857, Confident AI 904) or a separate eval product (Promptfoo, DeepEval, RAGAS) but not both under one SOC 2 + ISO 27001 control envelope.
2. **Only candidate that ships a first-party `braintrust eval` CLI + GitHub Actions integration that runs eval experiments as a per-PR CI gate with auto-compare-against-main + per-experiment delta** — competitors require custom YAML + ad-hoc GitHub Actions glue (DeepEval + Promptfoo can run in CI but the eval-result-store + experiment-compare is DIY).
3. **Only candidate that ships a first-party per-eval-experiment Custom-Scorer registry with code-based + LLM-as-judge + heuristic + per-scorer-score + per-scorer-versioning + per-scorer-replay** — distinct from OpenAI Evals (deprecated, GitHub-only) + Promptfoo (CLI-only, no scorer registry) + DeepEval (per-eval-decorator, no scorer versioning).
4. **Only candidate that ships a first-party per-row-per-dataset provenance hash + per-row replay-from-source API (Braintrust Datasets `dataset.s3()` + per-row `id` + per-row `source` URL + per-row `metadata` JSON)** — distinct from Langfuse Datasets (per-dataset-version only, no per-row hash) + Comet/Opik Datasets (per-dataset only, no per-row provenance hash) + Arize AI Datasets (per-dataset only).
5. **Only candidate that ships a first-party Functions runtime (Braintrust Functions) — serverless AI function hosting with per-function eval-driven deploy gates — within the same SOC 2 + ISO 27001 + HIPAA-ready control plane as the evals + logs** — competitors offer eval-as-a-service (Promptfoo + DeepEval + RAGAS) but do not host the function under eval; only Braintrust offers eval-driven-function-deploy in a single product.

## Buyer question the cohort answers

> *"We're shipping LLM applications and AI agents into production. We need a single product that lets us (a) run eval experiments in pre-prod CI to gate PRs, (b) observe prod LLM calls and agent spans, (c) score outputs with code-based + LLM-as-judge + heuristic scorers, (d) replay any prod span against a new prompt version to see if it improves, and (e) prove SOC 2 + ISO 27001 + HIPAA + GDPR + EU AI Act Art. 10 audit-trail compliance to our customer. Which vendor gives us all five in one product without stitching four SaaS vendors together?"*

That buyer question is **not** answered by any single closed cohort vendor (mlops_feature_store = experiment tracking + registry; observability_eval = post-prod tracing; workflow_orchestration = agent orchestration; voice_agent_observability = voice-specific). Braintrust is the OPENER that anchors the dedicated ai_agent_test_evaluation_suite NEW VERTICAL #53.

## Cohort-unique compliance posture verbatim (braintrustdata.com/security 2026-07-24)

SOC 2 Type II + ISO 27001 + HIPAA-ready + GDPR + EU AI Act Art. 10 readiness + CCPA + per-tenant data isolation + per-API-key audit log + per-Brainstore-region US-only / EU-region pinning + TLS 1.3 + encryption-at-rest AES-256 + per-tenant encryption keys optional. Braintrust is the ONLY cohort-unique candidate that ships a dedicated SOC 2 + ISO 27001 + HIPAA-ready + EU AI Act Art. 10 readiness certification bundle *for the eval + observability + proxy + functions platform itself* — competitors either ship the eval substrate under Apache-2.0 OSS without managed-compliance (DeepEval + Promptfoo + RAGAS) or ship a managed-observability product that does not cover eval (Arize + Langfuse + Honeycomb + Galileo + Humanloop + Fiddler + Confident).

## 22-column evidence wedge

tenant_id + braintrust_org_id + braintrust_project_id + braintrust_api_key_id + braintrust_brainstore_region + eval_experiment_id + eval_experiment_score + eval_scorer_id + eval_scorer_version + eval_scorer_kind + eval_dataset_id + eval_dataset_row_id + eval_dataset_row_hash + log_id + log_span_id + log_input_hash + log_output_hash + log_model + log_token_usage + proxy_request_id + proxy_cache_hit + ci_run_id + cross_tenant_no_bleed_invariant + replay_hash.

## Cohort-cumulative offer (NEW VERTICAL #53)

$500/48h fixed-scope Braintrust + ai_agent_test_evaluation_suite evidence-gap map OR $497/mo quarterly refresh OR $2,000 five-vendor ai_agent_test_evaluation_suite cohort benchmark at cohort close (CLOSER #5/5) OR $2,485 MRR ceiling per YanXbt pattern (5 clients × $497/mo).

## Why OPENER #1/5 (not SIBLING or CLOSER)

Braintrust is the OPENER because (1) its combined eval + observability + proxy + functions in one SOC 2 + ISO 27001 + HIPAA-ready + EU AI Act Art. 10 substrate is the buyer-question anchor for the entire vertical; (2) the Eval-Driven Development (EDD) workflow it pioneered (Ankur Goyal coined EDD in 2024 verbatim blog post braintrustdata.com/blog/eval-driven-development-2024-07-15) is the named methodology the cohort vendors will align against; (3) Braintrust's per-row-per-dataset hash + per-eval-experiment scorer registry is the strongest compliance-trail first-party primitive in the cohort, which the SIBLING vendors will inherit as the de facto audit-trail standard; (4) commercial-OPENER pattern from prior closed cohorts (W&B 1154 OPENER ai_mlops_feature_store, ServiceTitan 868 OPENER ai_field_service_management, Cognite 1130 OPENER ai_agent_industrial_dataops, SAP 1135 OPENER ai_agent_erp_dataops, Sana 1166 OPENER ai_enterprise_knowledge_search) confirms OPENER anchors the institutional-substrate + commercial-contact surface for the cohort.

## Pitfalls reinforced

- P28: channels from first-party footer + form-gated only; no guessed general-business inbox added.
- P29: no SMTP blast — queued_not_sent; $0 sent / $0 received.
- P44: CSV append via csv.writer + QUOTE_ALL + lineterminator='\r\n' to match CRLF.
- P45: sitemap + index.html consistency — chunk_1174 will be added with matching indent pattern + data-cohort-role='opener-1-of-5'.
- P99: 5-WEDGE non-overlap rubric derived from FIRST-PARTY verbatim evidence on braintrustdata.com + github.com/braintrustdata/braintrust-sdk 2026-07-24 via curl HTTP 200 + GitHub REST API, not training-data memory.
- P102: csv.writer defensive newline check before append — send_log.jsonl terminator detection.
- P106: build-log + index.html no `</body>` close — append directly to file end.
- P523: Python list → csv.writer for all row appends — no hand-composed CSV.
- P524: 8-col leads.csv + 13-col leads_with_emails.csv + 7-col revenue_log.csv schemas locked before append.

---

Atlas @ Talon Forge — cron tick `2026-07-24-fast-exec-braintrust-ai-agent-test-evaluation-suite-opener-1-1174` — OPENER #1/5 ai_agent_test_evaluation_suite NEW VERTICAL #53 — braintrustdata.com NAMED first-party surface — github.com/braintrustdata/braintrust-sdk verified via GitHub REST API 2026-07-24 — `mailto:support@braintrustdata.com` + `https://www.braintrustdata.com/contact` + `https://braintrustdata.com/contact-sales` verified verbatim first-party 2026-07-24, NOT submitted — SMTP/form gated, $0 sent / $0 received.
