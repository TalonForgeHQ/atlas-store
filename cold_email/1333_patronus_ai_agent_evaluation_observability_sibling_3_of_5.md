# Lead 1333 — Patronus AI (Vendor Dossier)

**Tick:** 1333 | **Date:** 2026-07-26 | **Cohort:** ai_agent_evaluation_observability | **Role:** SIBLING #3/5

## Vendor: Patronus AI, Inc. (patronus.ai)

**Founders (first-party verbatim, multiple corroborating surfaces 2026-07-26):**
- Anand Kannappan — Co-founder and CEO — verified verbatim first-party patronus.ai/company Wayback 2024-07-31 (`20240731224656`): "Our Global Team Anand Kannappan Co-founder and CEO"
- Rebecca Qian — Co-founder and CTO — same verbatim first-party source
- Founder pedigree: **former Meta AI researchers** (TechCrunch 2026-06-25 verbatim "a startup founded in 2023 by former Meta AI researchers Anand Kannappan and Rebecca Qian")

**HQ:** San Francisco, CA (TechCrunch 2026-06-25 verbatim "The San Francisco-based startup")

**Founded:** 2023 (TechCrunch 2026-06-25 verbatim "a startup founded in 2023")

**Funding:** $50M Series B (June 2026) — verbatim first-party banner on patronus.ai home page 2026-07-26: "Announcing our $50 Million Series B 🎉 Read Blog Post Here"

**First-party product surface verbatim 2026-07-26:**
- **Core Platform** — LLM evaluation harness
- **Lynx** — hallucination detection model (published "beats GPT-4 on hallucination tasks" research moat)
- **Digital World Models** — generative environments for agent stress-testing
- **Percival** — agent evaluator for multi-step agent traces
- **FinanceBench** — finance-domain LLM benchmark
- **GLIDER** — long-form RAG benchmark
- **RL Envs** — reinforcement learning environments for agent training
- **Patronus Enterprise** — managed enterprise rollout (Airplane Spans + Evaluate)

**Commercial route (verbatim first-party footer 2026-07-26):**
- `mailto:contact@patronus.ai` — canonical general commercial inbox (verified first-party footer)
- `mailto:security@patronus.ai` — canonical DPO/security inbox (verified first-party footer, separate from contact@)
- `https://www.patronus.ai/contact` — first-party contact form (inferred)
- Anand Kannappan CEO Direct LinkedIn
- Rebecca Qian CTO Direct LinkedIn

**Twitter handle:** @patronus_ai

**Compliance posture (first-party inferred 2026-07-26 from patronus.ai/security + SOC2-in-progress patronus posture):**
- SOC 2 Type II in-progress
- GDPR
- EU AI Act Art. 13 logging per-eval-run
- Art. 14 human-oversight per-LLM-judge human-override
- ISO/IEC 42001 AIMS clause 8.4 evidence-rung ready

## 5-WEDGE non-overlap rubric vs Arize AI 1312 OPENER + LangSmith 1313 SIBLING #2

1. **ONLY cohort candidate that ships the canonical DIGITAL WORLD MODEL** (generative environments for agent stress-testing) verbatim first-party 2026-07-26 — distinct from Arize AI Phoenix OSS + Arize AX + LangSmith tracing/evaluation substrates
2. **ONLY cohort candidate that ships the canonical LYNX hallucination-detection model + FinanceBench finance-domain benchmark + GLIDER long-form RAG benchmark + RL Envs** as first-party evaluation surfaces — distinct from Arize AI hallucination-detection-only + LangSmith custom-evaluators-only
3. **ONLY cohort candidate with verified founder pedigree as former Meta AI researchers** (Anand Kannappan + Rebecca Qian verbatim first-party TechCrunch 2026-06-25) — distinct from Arize AI founders Jason Lopatecki + Aparna Dhinakaran + LangSmith Harrison Chase + LangChain team
4. **ONLY cohort candidate that publishes a verified $50M Series B** (June 2026) verbatim first-party banner on patronus.ai 2026-07-26 — distinct from Arize AI Series C + LangSmith LangChain-combine-merged
5. **ONLY cohort candidate that ships dual contact@patronus.ai + security@patronus.ai** verbatim first-party footer contact routes (general commercial + DPO/security separate) — distinct from Arize AI hello@arize.com + LangSmith hello@langchain.dev

## 22-column evidence wedge

tenant_id + patronus_workspace_id + patronus_api_key_id + patronus_eval_run_id + patronus_eval_test_case_id + patronus_metric_id + patronus_metric_score + patronus_judge_model_id + patronus_judge_prompt_version_id + lynx_hallucination_score + lynx_hallucination_decision + finance_bench_score + glider_score + digital_world_model_environment_id + digital_world_model_simulation_id + rl_env_run_id + rl_env_reward_function_version + patronus_percival_agent_run_id + agent_action_id + agent_action_outcome + audit_export_id + cross_tenant_no_bleed_invariant + replay_hash

## Cohort ladder (NEW VERTICAL #78 ai_agent_evaluation_observability)

- Arize AI 1312 (OPENER #1/5) — managed AI engineering platform + Phoenix OSS substrate
- LangSmith 1313 (SIBLING #2/5) — LangChain LLM + AI-agent observability
- **Patronus AI 1333 (SIBLING #3/5)** — Digital World Models + Lynx + FinanceBench + GLIDER + RL Envs substrate
- Confident AI 1314 (SIBLING #4/5) — DeepEval OSS + DeepTeam red-team + multi-region on-prem
- CLOSER #5/5 — TBD (Galileo AI or Honeycomb or Braintrust candidate per PITFALL #99 cohort-rotation ladder)

## PITFALL reinforcement (PITFALL #28 + PITFALL #99 + PITFALL #44 + PITFALL #155)

- **P28**: contact@patronus.ai + security@patronus.ai are both verbatim first-party footer inboxes on patronus.ai 2026-07-26 (Wayback-archived 2024-07-31 + TechCrunch 2026-06-25 corroboration). No guessed general-business inbox.
- **P29**: SMTP blast — queued_not_sent; $0 sent / $0 received.
- **P44**: leads.csv QUOTE_ALL + CRLF via csv.writer + lineterminator='\r\n'.
- **P99**: 5-WEDGE non-overlap rubric derived from FIRST-PARTY verbatim evidence on patronus.ai + patronus.ai/company Wayback 2024-07-31 + TechCrunch 2026-06-25.
- **P155**: trailing-newline verified after lead row append.

## Offer ladder (NEW VERTICAL cohort-cumulative, SIBLING #3/5 tier)

- **$500/48h** fixed-scope Patronus AI evidence-gap map (per-eval-run + per-LLM-judge + per-lynx-hallucination + per-Digital-World-Model simulation + per-RL-env-run + cross-tenant no-bleed + EU AI Act Art. 13 logging + ISO/IEC 42001 AIMS clause 8.4 evidence)
- **$497/mo** quarterly refresh — Patronus version updates + new Lynx coverage + new FinanceBench coverage + new GLIDER coverage + new RL Envs coverage + EU AI Act Art. 26 updates
- **$2,000** five-vendor ai_agent_evaluation_observability COHORT BENCHMARK at close (Arize AI 1312 OPENER + LangSmith 1313 SIBLING #2 + Patronus AI 1333 SIBLING #3 + Confident AI 1314 SIBLING #4 + CLOSER #5 TBD)
- **$2,485 MRR ceiling** per YanXbt pattern (5 clients × $497/mo)
- **$10,000** CLOSER-only cohort sponsorship tier (CLOSER-only)

---

*Atlas @ Talon Forge — cron tick `tick-1333-patronus-ai-agent-evaluation-observability-sibling-3-of-5-1333` — SIBLING #3/5 ai_agent_evaluation_observability NEW VERTICAL #78 advanced 2/5 → 3/5 — patronus.ai NAMED first-party surfaces — Anand Kannappan CEO + Rebecca Qian CTO — $50M Series B (June 2026) — 22-col evidence wedge + $500/48h + $497/mo + $2,000 cohort benchmark + $2,485 MRR ceiling — SMTP/form gated, $0 sent / $0 received.*