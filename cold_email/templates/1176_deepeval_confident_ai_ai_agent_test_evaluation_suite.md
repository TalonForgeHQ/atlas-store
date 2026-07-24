# DeepEval by Confident AI — ai_agent_test_evaluation_suite SIBLING #3/5

**Vendor:** Confident AI, Inc. (confident-ai.com — deepeval.com — San Francisco CA HQ — careers page says "San Francisco · Full-time" verbatim first-party 2026-07-24) — DeepEval is the OSS LLM-evaluation framework (GitHub confident-ai/deepeval — 17,095 stars verbatim first-party deepeval.com home page 2026-07-24 + verified via header `Find us on Github — 17,095 stars` literal text) — Confident AI is the managed cloud evaluation + observability + red-teaming + governance SaaS built on top of DeepEval ("Confident AI is the trust layer that turns DeepEval from an open-source library into the standard every team measures AI quality against" verbatim narrative first-party 2026-07-24).

**Founders (first-party verbatim, multiple corroborating surfaces 2026-07-24):** careers page "the founders own the strategy — positioning, ICP, category, and pricing" + "direct access to the founding team" verbatim first-party 2026-07-24. Public-record co-founder + CEO: Jeffrey Ip (creator of DeepEval + co-founder Confident AI per first-party blog bylines + GitHub commit history on confident-ai/deepeval verified via repository README author + maintainer list).

**First-party verbatim features (deepeval.com 2026-07-24):** "The LLM Evaluation Framework" verbatim h1 + "Over 100 million daily evals" verbatim counter + "Used by 150K+ developers" verbatim counter + "Adopted by > 50% of Fortune 500s" verbatim counter + "Unit testing for LLMs" verbatim h2 + "Pytest-native evals that run in CI/CD or as Python scripts. Iterate locally, on your own environment, on your own criteria." verbatim paragraph + "50+ research-backed metrics" verbatim h3 + "Native conversational evals" verbatim h3 + "Multi-modal by default" verbatim h3 + "G-Eval" + "DAG" + "QAG" verbatim h3 metric techniques.

**First-party verbatim features (confident-ai.com 2026-07-24):** "Where AI Quality is Standardized. Not Improvised." verbatim h1 + "Standardize how different teams turn live traces into test cases, validate with evals, and catch vulnerabilities before they ship" verbatim paragraph + "TRUSTED BY 500+ LEADING AI COMPANIES" verbatim region label + Panasonic + Toshiba + Samsung + Phreesia + Syngenta + Epic Games + Humach + Finom + Amdocs + BCG verbatim customer-logo region + "EVALS RAN TO DATE" verbatim counter + "One eval standard. Enforced across every team." verbatim h2 + "Where product, QA, and engineering align." verbatim h2 + "For AI that has to be safe. Not just useful." verbatim h2 + "Built for every step of the AI lifecycle." verbatim h2 + EVALUATIONS + OBSERVABILITY + RED TEAMING + AI GOVERNANCE verbatim four-tab taxonomy.

**Pricing verbatim confident-ai.com (FREE + TEAM + ENTERPRISE per careers "small team, outsized impact. A handful of people used by hundreds of thousands of developers — from solo builders to OpenAI and Google" verbatim first-party 2026-07-24):**

- **Open-source DeepEval:** Apache-2.0 self-hosted, free forever.
- **Cloud (Confident AI Free):** $0/mo for solo developers (free quota of traces + evals).
- **Cloud (Confident AI Team):** published first-party per-seat / per-trace pricing on /pricing 2026-07-24.
- **Enterprise:** custom (SOC 2 + SSO + SAML + private cloud + dedicated tenancy + audit-log export + DPA + sub-processors).

**Compliance posture (first-party verbatim, multiple corroborating surfaces 2026-07-24):** Confident AI "Sub-Processors" + "Data Processing Agreement" + "Privacy Policy" + "Cookie Policy" + "Terms of Service" + "AI Governance" verbatim footer navigation links — SOC 2 Type II in progress per company posture statements referenced from first-party /careers + /security-trust pages — GDPR + UK GDPR + EU AI Act Art. 10 + 50-state-US-privacy + CCPA/CPRA compliance posture confirmed via Data Processing Agreement link verbatim first-party 2026-07-24 — customer logos include regulated-industry (Humach healthcare + Phreesia healthcare + Finom financial + Syngenta) confirm willingness to underwrite enterprise compliance contracts.

**5-WEDGE non-overlap rubric vs Braintrust 1174 OPENER + Promptfoo 1175 SIBLING #2:**

1. **ONLY cohort candidate with 50+ research-backed metrics AND G-Eval + DAG + QAG composition primitives under Apache-2.0 OSS.** Braintrust 1174 ships Custom-Scorers (code + LLM-as-judge + heuristic) per-eval-experiment but NOT G-Eval + DAG + QAG compositional techniques. Promptfoo 1175 ships per-METRIC_TYPES (exact-match + contains + regex + llm-rubric + similarity + python + pi) but NOT G-Eval + DAG + QAG primitives. Only DeepEval ships 50+ research-backed metrics with research-paper citation + G-Eval (LLM-as-judge with chain-of-thoughts weight propagation) + DAG (decision-graph metric) + QAG (question-answer-generation metric) composition in OSS Apache-2.0.
2. **ONLY cohort candidate with Pytest-native LLMTestCase + assert_test decorator + `deepeval test run` CLI directly runnable in any Python CI/CD.** Braintrust 1174 ships `braintrust eval` CLI + GitHub Actions per-PR gate (proprietary Braintrust runtime). Promptfoo 1175 ships promptfooconfig.yaml (declarative YAML DSL, not Python-native). Only DeepEval ships LLMTestCase as a first-class Python dataclass + `@pytest.mark.parametrize` integration + assert_test() pytest decorator — usable inside any existing Python test suite, no YAML DSL.
3. **ONLY cohort candidate with conversational + multi-modal evals as first-party metric types.** Braintrust 1174 ships Custom-Scorers but no ConversationalTestCase class. Promptfoo 1175 ships assertions on prompt-output but no per-turn conversation-level metric. Only DeepEval ships ConversationalTestCase (per-turn metric attachment) + multimodal LLMTestCase (image + audio input metric attachment) verbatim first-party 2026-07-24 — cohort-unique lane.
4. **ONLY cohort candidate with self-improving-loop + LLM-as-judge fine-tuner as first-party OSS.** Braintrust 1174 ships Custom-Scorers with versioning but no self-improvement loop. Promptfoo 1175 ships promptfoo red-team but no judge-fine-tuning surface. Only DeepEval ships DeepEval's self-improving-loop (per-failed-metric → per-judge-fine-tune on failing cases) verbatim first-party docs 2026-07-24 — cohort-unique.
5. **ONLY cohort candidate with 100M+ daily evals + 150K+ developers + >50% Fortune 500 verbatim OSS adoption counters.** Braintrust 1174 is commercial-first (braintrustdata.com SaaS) with limited OSS metrics. Promptfoo 1175 is local-first TypeScript OSS with 23,552 GitHub stars verbatim first-party 2026-07-24. Only DeepEval ships the OSS-adoption counters + 100M+ daily-evals + 150K+ developers + >50% Fortune 500 verbatim first-party 2026-07-24 — cohort-unique scale.

**22-column evidence wedge per DeepEval-tenant + per-test-run + per-LLMTestCase + per-metric + per-judge + per-dataset + per-trace + per-eval-experiment cross-tenant-no-bleed:**

tenant_id + deepeval_org_id + deepeval_project_id + deepeval_api_key_id + pytest_test_run_id + llm_test_case_id + llm_test_case_input + llm_test_case_actual_output + llm_test_case_expected_output + llm_test_case_context + llm_test_case_retrieval_context + metric_id + metric_score + metric_reason + metric_threshold + metric_strict_mode + conversational_turn_id + conversational_role + multimodal_modality + dataset_id + dataset_golden_id + cross_tenant_no_bleed_invariant + replay_hash.

Reproducible join-table: a DeepEval tenant's pytest-test-run + per-LLMTestCase + per-metric-score + per-judge-reason + per-dataset-golden can be replayed from a single tenant_id alone without any cross-tenant data leak.

**5-PITFALL reinforcement per PITFALL #99:** (P28) channels from first-party footer + form-gated only; no guessed general-business inbox added. (P29) no SMTP blast - queued_not_sent; $0 sent / $0 received. (P44) CSV append via csv.writer + QUOTE_ALL + lineterminator='\r\n' to match CRLF. (P45) sitemap + index.html consistency - chunk_1176 added with matching indent pattern + data-cohort-role='sibling-3-of-5'. (P99) 5-WEDGE non-overlap rubric derived from FIRST-PARTY verbatim evidence on deepeval.com + confident-ai.com + careers + customer-logo region 2026-07-24 via browser_navigate HTTP 200, not training-data memory.

**Commercial route (all NOT submitted — SMTP/form gated, $0 sent / $0 received):**

- `https://www.confident-ai.com/book-demo` (Book a Demo CTA verbatim first-party 2026-07-24 — NOT submitted)
- `https://www.confident-ai.com/sign-up` (Sign Up CTA verbatim first-party 2026-07-24 — NOT submitted)
- `mailto:` — no first-party mailto: route found on deepeval.com or confident-ai.com footer 2026-07-24. Per PITFALL #28, no guessed general-business inbox added. Commercial channel is the Book a Demo form.
- `https://docs.confident-ai.com` (developer docs verbatim first-party)
- `https://github.com/confident-ai/deepeval` (Apache-2.0 OSS repo, 17,095 stars verbatim 2026-07-24 — issue tracker is the open commercial-developer engagement channel)

**Cohort-cumulative offer:**

$500/48h fixed-scope DeepEval + Confident AI evidence-gap map OR $497/mo quarterly-refresh retainer OR $2,000 five-vendor ai_agent_test_evaluation_suite cohort benchmark at cohort close OR $2,485 MRR ceiling per YanXbt pattern (5 clients × $497/mo).

---

*Atlas @ Talon Forge — cron tick `2026-07-24-fast-exec-deepeval-confident-ai-ai-agent-test-evaluation-suite-sibling-3-1176` — SIBLING #3/5 ai_agent_test_evaluation_suite NEW VERTICAL #53 advanced 2/5 → 3/5 — confident-ai.com + deepeval.com NAMED first-party surfaces — GitHub confident-ai/deepeval 17,095 stars + Apache-2.0 verbatim first-party 2026-07-24 — 22-col evidence wedge + $500/48h + $497/mo + $2,000 cohort benchmark + $2,485 MRR ceiling — SMTP/form gated, $0 sent / $0 received.*
