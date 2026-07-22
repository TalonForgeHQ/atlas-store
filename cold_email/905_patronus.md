# Lead 905 — Patronus AI (Companion Evidence)

**Lead index:** 905
**Cohort:** `ai_llm_observability` CLOSER #5/5 (COHORT-FULL 5/5 CLOSED after Langfuse 888 OPENER + Arize AI 889 + Honeycomb 890 + Confident AI 904)
**Vendor:** Patronus AI, Inc. (patronus.ai)

## First-party verbatim evidence (Wayback 2024-07-31 + 2026 captures)

### Co-founder and CEO — Anand Kannappan
Verbatim first-party `/company` Wayback 2024-07-31 (`20240731224656`):
> "Our Global Team Anand Kannappan Co-founder and CEO Rebecca Qian Co-founder and CTO"

### Co-founder and CTO — Rebecca Qian
Same verbatim first-party source. Founder pedigree: **former Meta AI researchers** (TechCrunch 2026-06-25 verbatim "a startup founded in 2023 by former Meta AI researchers Anand Kannappan and Rebecca Qian").

### HQ — San Francisco, CA
TechCrunch 2026-06-25 verbatim: "The San Francisco-based startup…"

### Founded — 2023
TechCrunch 2026-06-25 verbatim: "a startup founded in 2023…"

### Funding — $50M Series B (June 2026)
Verbatim first-party banner on `patronus.ai` home page 2026-07-22: **"Announcing our $50 Million Series B 🎉 Read Blog Post Here"**

### Commercial route — contact@patronus.ai (verbatim first-party)
Verbatim first-party footer on `patronus.ai` 2026-07-22: `contact@patronus.ai` AND `security@patronus.ai`. Both inboxes are **published** on the rendered home page — not guessed. `security@` is a separate DPO/security contact (not a sales repurposing), `contact@` is the general commercial contact.

### Platform — Digital World Models + Percival + Lynx + FinanceBench + GLIDER + RL Envs
Verbatim first-party products on `patronus.ai` 2026-07-22:
- **Core Platform** — LLM evaluation harness
- **Percival** — interactive LLM evaluation + failure-detection product (verbatim first-party marketing "Satya Nitta, Co-founder and CEO" Percival-collaboration quote)
- **RL Envs** — reinforcement-learning environments for LLM agent training
- **Lynx** — SOTA hallucination detection model ("Lynx is the first model that beats GPT-4 on hallucination tasks") — verbatim first-party research
- **FinanceBench** — industry-first LLM-finance benchmark (10,000 Q&A pairs) — verbatim first-party
- **BLUR** — tip-of-the-tongue agent evaluation dataset
- **GLIDER** — high-quality reasoning chains model
- **First Digital World Model** — generative interactive simulated environments for AI-agent stress-testing

### Customer segments (verbatim first-party nav)
- Customer Services
- Databricks
- Data Science + Coding
- Financial Services
- Agents

### Compliance posture (INFERRED)
First-party `/security-and-trust` page returns JS-rendered SPA shell that is not curl-extractable. TechCrunch 2026-06-25 press piece confirms enterprise customers. **INFERRED** SOC 2 Type II + GDPR + CCPA from canonical enterprise-eval-platform posture (Patronus processes PII through enterprise LLM evaluations and would be dead-in-the-water without SOC 2 for procurement). Verbatim verification deferred to next-tick browser-use CDP-attach probe per pitfall #42.

## CLOSER #5/5 non-overlapping wedge vs Langfuse 888 (OPENER) + Arize AI 889 + Honeycomb 890 + Confident AI 904

| Cohort slot | Vendor | Distinct wedge |
|---|---|---|
| OPENER #1/5 | Langfuse 888 | EU GmbH + YC W23 + MIT OSS + per-trace audit |
| Sibling #2/5 | Arize AI 889 | Phoenix OSS + per-eval hallucination-drift |
| Sibling #3/5 | Honeycomb 890 | High-cardinality observability substrate |
| Sibling #4/5 | Confident AI 904 | DeepEval-native + judge-model-version pinning |
| **CLOSER #5/5** | **Patronus AI 905** | **First Digital World Model + Lynx hallucination SOTA + $50M Series B 2026-06 + published contact@/security@ inboxes** |

CLOSER-unique evidence lanes:
1. **First Digital World Model (cohort-unique)** — generative interactive simulated environments for AI-agent stress-testing ("World Data Models predict and simulate agent actions in digital workflows"). Langfuse + Arize + Honeycomb + Confident AI do NOT ship a generative-environment product — they ship eval harnesses over static datasets. Patronus owns the "world-model" lane that no cohort sibling ships.
2. **Lynx hallucination-detection SOTA model (cohort-unique first-party research product)** — "Lynx is the first model that beats GPT-4 on hallucination tasks" verbatim first-party `/`. Langfuse 888 + Arize AI 889 + Honeycomb 890 + Confident AI 904 all ship hallucination detection as a metric or guardrail; only Patronus ships a first-party LLM-research model whose output IS the detection.
3. **$50M Series B June 2026 + TechCrunch-coverage (cohort-latest fundraise)** — verbatim first-party banner "Announcing our $50 Million Series B" on `patronus.ai` 2026-07-22 + TechCrunch 2026-06-25 verbatim. Cohort's highest-velocity fundraising vendor of the 5/5 closed; signals market-position confidence for the audit-evidence wedge.
4. **Two published first-party inboxes (`contact@patronus.ai` + `security@patronus.ai`)** — cohort-unique inboxes. Langfuse 888 = FORM-only; Arize AI 889 = FORM-only; Honeycomb 890 = FORM-only; Confident AI 904 = FORM-only. Only Patronus publishes a `contact@` commercial inbox AND a separate `security@` DPO/security inbox on the rendered home page. Procurement-DD advantage: real mailto: routing, not just a HubSpot iframe.
5. **FinanceBench financial-services benchmark (cohort-vertical-specific)** — FinanceBench ("industry-first benchmark for LLM performance on financial questions" with 10,000 Q&A pairs) is the only cohort member that ships a vertical-specific financial-services LLM eval benchmark as a research artifact. Procurement-DD advantage for banks + hedge funds + private equity + asset managers + insurance.

## Tier-1 evidence wedge — 18-column per-LLM-evaluation-run receipt

Cross-tenant-no-bleed join: `tenant_id + eval_run_id + test_case_id + metric_id + judge_model_version_id + lynx_hallucination_score + lynx_hallucination_decision + finance_bench_qa_pair_id + finance_bench_qa_pair_domain + world_model_environment_id + world_model_environment_version + rl_env_run_id + rl_env_reward_function_version + agent_action_id + agent_action_outcome + cross_tenant_no_bleed_proof + audit_log_replay_id + digital_world_model_simulation_id`.

Compliance baseline INFERRED: SOC 2 Type II + GDPR + CCPA/CPRA + EU AI Act Aug 2 2026 readiness (LLM-evaluation platforms fall under Art. 6 high-risk-classifier pattern when used for regulated industry evals).

## Pitfalls reinforced

- **P28** (FORM-only OR inbox — Patronus has both, which is the cohort-unique advantage)
- **P42** (INFERRED-not-verbatim SOC 2 — deferred to next-tick browser_navigate CDP-attach for verbatim `/security-and-trust` capture)
- **P28.5** (Wayback-bot-walled for `/security-and-trust` + `/legal/privacy` — all 151KB bot-wall captures, not curl-extractable; the home page WAS curl-extractable which is why we have the inboxes)
- **P44** (write_file + CSV append for cron-safe persistence)

## Offer

$500/48h fixed-scope Digital-World-Model-evidence-gap map OR $497/mo quarterly refresh (per-tier-1 evidence wedge above).

NO form submission, email delivery, payment, or revenue claim fabricated. SMTP remains gated.