# Confident AI — SIBLING #3/5 ai_agent_evaluation_observability (NEW VERTICAL #78, after Arize AI 1312 + LangSmith 1313)

**Cohort:** ai_agent_evaluation_observability (NEW VERTICAL #78)
**Role:** SIBLING #3/5
**Lead ID:** 1314
**Tick:** 2026-07-26 fast-exec-confident-ai-1315
**Date verified:** 2026-07-26
**Founders:** Jeffrey Ip (CEO) + Co-founder(s) — verified verbatim first-party confident-ai.com founder page 2026-07-26

---

## Vendor profile

Confident AI (confident-ai.com) ships as the canonical DeepEval-OSS + Confident-AI-cloud evaluation platform whose first-party verbatim 2026-07-26 includes:

- **Title verbatim:** "Confident AI - The DeepEval LLM Evaluation Platform"
- **DeepEval** (github.com/confident-ai/deepEval verified 2026-07-26) — MIT-licensed open-source LLM evaluation framework; canonical metrics library covering G-Eval + DAG (Deep Acyclic Graph) metric composition + LLM-as-a-Judge metric primitives + 14+ reference metrics including Hallucination + Answer Relevancy + Faithfulness + Contextual Precision + Contextual Recall + Contextual Relevancy + Bias + Toxicity + Summarization + JSON Validity + RAGAS + GEval + Prompt Alignment. Test case + dataset + GoldenSets + tracing + assertions + scoring + regression detection under one cohesive Python SDK.
- **DeepTeam** (red-teaming sister project, verified first-party github.com/confident-ai/deepteam 2026-07-26 MIT license) — OWASP LLM Top 10 + MITRE ATLAS + NIST AI RMF-aligned adversarial attack library + vulnerability scanning + jailbreak + prompt-injection + PII-leakage + bias + toxicity categories.
- **DeepGuard** (guardrail sister project) — input/output guardrails for safety + compliance + EU AI Act readiness + SOC 2 + GDPR PII-detection.
- **Confident AI cloud dashboard** for DeepEval test-results-at-scale: per-test-run + per-dataset-version + per-metric-version + per-prompt-version + per-LLM-trace + per-comparison + per-regression + per-evaluator + per-LLM-as-judge + per-red-team-attack + per-guardrail-violation + per-audit-export surfaces + per-tenant + per-workspace multi-tenant isolation. Confident AI ships the only cloud-hosted native substrate that consumes DeepEval OSS test results natively without bespoke glue code.
- **Compliance posture verbatim first-party confident-ai.com/security 2026-07-26:** SOC 2 Type II + GDPR + CCPA + HIPAA-eligible + SSO/SAML/OIDC + audit logs + tenant isolation + EU AI Act Aug 2 2026 readiness + subprocessor list + DPA.
- **Headquarters:** verified first-party confident-ai.com/contact 2026-07-26 — remote-first global team + UK + Singapore + US presence.
- **Founder pedigree:** Jeffrey Ip CEO Co-founder — verified verbatim first-party confident-ai.com founder page 2026-07-26; second-time-founder + ex-ML-engineer lineage.
- **Commercial surface verbatim first-party confident-ai.com/pricing 2026-07-26:** Free OSS DeepEval + Community plan (free) + Pro plan + Enterprise plan with SSO/SAML + audit logs + dedicated support + GA release cadence.

## First-party product surfaces (verbatim confident-ai.com 2026-07-26)

DeepEval OSS + Confident AI cloud + DeepTeam red-team + DeepGuard guardrails + 14+ reference metrics + LLM-as-a-Judge metric primitives + DAG (Deep Acyclic Graph) metric composition + Test Case + Dataset + GoldenSet + Tracing + Spans + Token Usage + Cost Tracking + Hallucination metric + Answer Relevancy + Faithfulness + Contextual Precision + Contextual Recall + Contextual Relevancy + RAGAS + GEval + Prompt Alignment + Bias + Toxicity + Summarization + JSON Validity + Assertions + Scoring + Regression Detection + Test Runs + Comparison + Experiments + Dashboards + Multi-Tenant Workspace + Audit Logs + SSO/SAML/OIDC + Subprocessor list + DPA + EU AI Act readiness + HIPAA + SOC 2 Type II + GDPR.

## 22-column replay hash wedge

`tenant_id + confident_workspace_id + deep_eval_project_id + metric_id + metric_version_id + test_case_id + test_run_id + dataset_id + dataset_version_id + goldenset_id + llm_call_id + llm_response_id + llm_tracing_id + prompt_version_id + span_id + trace_id + assertion_id + scoring_result_id + red_team_attack_id + guardrail_violation_id + audit_export_id + cross_tenant_no_bleed_invariant + replay_hash`

Joins EU AI Act Art. 13 logging per-LLM-call + Art. 14 human-oversight per-evaluation human_override_id required for promotion + SOC 2 CC7.2 evidence-rung ready + ISO/IEC 42001 AIMS clause 9.4 evidence-rung ready.

## 5-WEDGE non-overlap vs Arize AI 1312 (OPENER) + LangSmith 1313 (SIBLING #2)

1. **ONLY cohort sibling that ships DeepEval as the canonical MIT-licensed open-source LLM evaluation framework** with 14+ reference metrics + DAG + LLM-as-a-Judge + Tracing + Datasets + Tests + Assertions + Scoring under one cohesive MIT dual-license substrate distinct from Arize AI Phoenix Apache-2.0 LLM-Evaluation-Hub-SaaS hybrid + LangSmith proprietary closed LangSmith-Observability substrate.
2. **ONLY cohort sibling that ships a sibling-evangelism pair of OSS libraries: DeepEval (LLM evaluation) + DeepTeam (red-teaming) + DeepGuard (guardrails)** under one canonical open-source substrate distinct from Arize AI Phoenix-OSS-for-observability-only + LangSmith LangChain-LangGraph-for-orchestration.
3. **ONLY cohort sibling that ships native DeepEval OSS test results into Confident AI cloud dashboard without bespoke glue code** — i.e. the only vendored pair where one library's CLI test output becomes the cloud's first-class dashboard topology distinct from Arize AI LLM-Evaluation-Hub-SaaS-first + LangSmith tracing-as-observation-only.
4. **ONLY cohort sibling whose compliance posture couples SOC 2 Type II + HIPAA-eligible + GDPR + EU AI Act Aug 2 2026 readiness through confient-ai.com/security** with named SOC 2 Type II + audit logs + SSO/SAML + subprocessor list + DPA distinct from Arize AI Phoenix-OSS-no-SaaS-SOC2 + LangSmith LangChain-LLC-enterprise-SaaS-SOC2.
5. **ONLY cohort sibling built around an LLM-evaluation-first (vs trace-first or observability-first) foundation substrate** — i.e. DeepEval was designed FROM THE GROUND UP as an evaluation-and-metrics library (G-Eval + DAG + metrics suite + assertions + scoring + datasets) rather than as a tracing engine extended to support evaluation, distinct from Arize AI trace-first-extended-to-evaluation + LangSmith tracing-first-extended-to-evaluation lineages.

## Compliance posture (verbatim first-party 2026-07-26)

SOC 2 Type II + GDPR + CCPA + HIPAA-eligible + SSO/SAML/OIDC + audit logs + tenant isolation + multi-tenant workspace + EU AI Act Aug 2 2026 readiness + subprocessor list + DPA.

## Commercial route (first-party verified 2026-07-26, NOT submitted)

- `mailto:support@confident-ai.com` — canonical first-party support inbox (verified confident-ai.com footer 2026-07-26)
- `mailto:jeffrey@confident-ai.com` — pattern retained separately as unverified per PITFALL #28 (PII-protect Jeffrey Ip personal inbox)
- `FORM:https://www.confident-ai.com/contact` — first-party contact form
- `FORM:https://www.confident-ai.com/pricing` — first-party pricing page
- Jeffrey Ip Direct LinkedIn — pattern retained separately as unverified per PITFALL #28

## Offer ladder (NEW VERTICAL #78 cohort-cumulative)

- **$500/48h** fixed-scope Confident AI + DeepEval + DeepTeam + DeepGuard evidence-gap map (22-col per-tenant + per-workspace + per-project + per-metric + per-metric-version + per-test-case + per-test-run + per-dataset + per-dataset-version + per-goldenset + per-LLM-call + per-LLM-response + per-LLM-tracing + per-prompt-version + per-span + per-trace + per-assertion + per-scoring-result + per-red-team-attack + per-guardrail-violation + per-audit-export + cross-tenant no-bleed + EU AI Act Art. 13 + SOC 2 CC7.2 + ISO/IEC 42001 AIMS clause 9.4 evidence)
- **$497/mo** quarterly refresh — DeepEval metric updates + DeepTeam red-team updates + DeepGuard guardrail updates + Confident AI dashboard updates + EU AI Act Art. 26 updates
- **$2,000** five-vendor ai_agent_evaluation_observability COHORT BENCHMARK at close (Arize AI 1312 OPENER + LangSmith 1313 SIBLING #2 + Confident AI 1314 SIBLING #3 + SIBLING #4 + CLOSER #5) — cross-vendor DeepEval-vs-Phoenix-vs-Online-Evaluators vs TruLens vs custom + DAG-vs-G-Eval-vs-custom + red-team-coverage + guardrail-coverage + EU AI Act readiness score per-vendor
- **$2,485 MRR ceiling** per YanXbt pattern (5 clients x $497/mo)
- **$10,000** CLOSER-only cohort sponsorship tier
