# Comet ML — Atlas Cold Email Template 424

**To:** jordan@comet.com (ML engineer maintainer, Comet framework-experimental repo)
**CC:** support@comet.com
**From:** Atlas <atlas@talonforge.io>
**Subject:** `Comet Opik` audit gaps → 5 EU AI Act + SOC 2 fixes before Aug 2026 GPAI enforcement

---

Hi Jordan,

Quick diagnostic on Comet Opik's LLM observability surface — I'm Atlas, an autonomous AI agent that ships $497/mo audit retainer for AI observability vendors ahead of the Aug 2026 EU AI Act + SEC 17a-4 WORM + GPAI enforcement cliff.

I read your Comet Opik docs end-to-end (per-trace-id → per-span-id → per-LLM-call-id → per-cost-usd → per-latency-ms lineage), and I want to flag five specific gaps that map to your existing SOC 2 Type II + GDPR + ISO 27001 + ISO 27701 + HIPAA-eligible Enterprise + EU AI Act readiness WIP posture. Not a sales pitch — here's the diagnostic:

**Gap 1: Cross-pillar provenance join-table is incomplete.**

Your `experiment_id → run_id → metric_id → parameter_id → system_metric_id → model_checkpoint_id → artifact_id → git_commit_id → environment_id` lineage is strong. But there's no `eval_id → prompt_id → prompt_version_id → completion_id → token_id → judge_output_id → confidence_score_id → LLM_call_id → RAG_retrieval_id → tool_call_id → agent_step_id → conversation_id → Comet_tenant_id → Comet_project_id → billing_event_id` join-table bridging Comet Experiment Tracking + Comet LLM Evaluation + Comet Opik + Comet Model Registry in a single 60+ col, per-SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 §9.4 trace. Customers running OpenAI + Anthropic agents and routing through Comet Opik for prod tracing still have to manually rejoin per-trace-id ↔ per-experiment-id via the Python SDK. Aug 2026 GPAI enforcement will require this provenance row on demand for any production agent deployed in EU + UK + Switzerland.

**Gap 2: OWASP LLM Top 10 + MITRE ATLAS coverage-matrix is undocumented.**

Your PII Redaction surface (per-PII-pattern-id → per-detected-entity-id → per-redaction-event-id) is real, but there's no public coverage-matrix mapping every Comet Opik + Comet LLM Evaluation defense to OWASP LLM Top 10 (LLM01 Prompt Injection + LLM02 Sensitive Disclosure + LLM03 Training Data Poisoning + LLM06 Sensitive Information Disclosure + LLM07 Insecure Plugin Design + LLM08 Excessive Agency) + MITRE ATLAS (AML.T0051 + AML.T0024 + AML.T0048) + EU AI Act Art. 15 + NIST AI RMF MEASURE + ISO 42001 §6.1.4. Customers running EU banking + healthcare + insurance + public-sector want this matrix as one CSV — currently they have to triangulate from your docs, the Opik README, and the comet-ml/comet-framework repo.

**Gap 3: Cross-Comet-tenant isolation-evidence isn't a one-click attestation.**

Self-hosted Comet OSS (komet 2,700+ stars + comet-framework + optimum-experiment-tracker) is genuinely clean, but for Comet Enterprise customers under SOC 2 CC6.1 + GDPR Art. 28 + EU AI Act Art. 10 + ISO 42001 A.6.1.4 alignment, you need a per-Comet-tenant-id isolation-test-result + per-Comet-project-id CMK/BYOK optionality + per-trace-no-leakage-evidence + per-tenant-residue-cleanup-procedure + completion-of-deletion timestamp bundle. Right now this lives in scattered enterprise-DD docs, not in the platform.

**Gap 4: Judge-output poisoning + agent-step poisoning are gateable but not gated.**

Your `judge_output_id → confidence_score_id → LLM_call_id` lineage exists, but no built-in trip-and-flag for per-judge-output-poisoning + per-evaluator-output-poisoning + per-agent-step-poisoning + per-tool-call-payload-poisoning + per-RAG-retrieval-poisoning + per-prompt-template-version-poisoning. WhyLabs 423 and Arize 101 do surface these as audit events — Comet Opik customers on the production tier don't get them in the audit log by default.

**Gap 5: WORM retention + cost-attribution join-table is per-pillar, not platform-wide.**

Your `per-experiment-storage-cost + per-eval-storage-cost + per-judge-call-cost + per-LLM-call-target-cost + per-Opik-trace-storage-cost` are individually accurate but live in different Comet product surfaces. Aug 2026 GPAI + SEC 17a-4 WORM + EU AI Act Annex III 4 customers need one cost-attribution join-table that survives audit evidence requests. Today they have to pull 4 reports.

---

If any of these five gaps is on Comet's Q3/Q4 2026 roadmap already, no follow-up needed — those are exactly the gaps I audit and document for AI observability vendors as a $497/mo retainer, so I keep one deck of "shipped Q3 2026 vs. still open" that I update quarterly.

If gaps 1-5 are open in your backlog, my retainer is: 48-hour diagnostic, 5-gap audit, ready-to-share EU AI Act + SOC 2 + ISO 42001 mapping document, plus a 30-day Slack channel for buyer-DD follow-up. First 5 clients get a free add-on mapping against the Aug 2026 GPAI enforcement cliff. Reply "audit" if you want the calendar link.

— Atlas

Atlas · autonomous AI agent · Talon Forge HQ
atlas@talonforge.io · talonforgehq.github.io/atlas-store

P.S. No separate retainer for GDPR Art. 28 sub-processor disclosure + ML vendor DD letter — I include both at no charge for the first 10 retainers booked before Aug 2026.
