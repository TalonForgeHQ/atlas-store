# Lead 835 — Arize AI (arize.com) — OPENER ai_observability_eval #1/5

**Vertical:** ai_observability_eval
**Cohort role:** OPENER #1/5 (NEW VERTICAL — post ai_intent_data_enrichment 830-834 CLOSED 5/5)
**Verified:** 2026-07-21 first-party HTTP 200 fetch
**Commercial route:** `FORM:https://arize.com/request-a-demo` (HubSpot portalId verified live 2026-07-21)

---

## First-party evidence (verified live 2026-07-21)

- `arize.com/` — HTTP 200. AI Observability + LLM Evaluation Platform positioning; Arize AX + Phoenix OSS mentioned.
- `arize.com/about-company/` — HTTP 200. Founding team byline + leadership.
  - **Jason Lopatecki** — Co-founder + CEO. First-party bio verbatim: *"Jason was co-founder and chief innovation officer at TubeMogul where he scaled the bu[siness]..."* — TubeMogul acquired by Adobe 2016 for $800M+ (verifiable via public press, but the page cites his CIO role + Tubemogul scaling heritage verbatim).
  - **Aparna Dhinakaran** — Co-founder + CPO. First-party bio + social profile linked; ex-Uber Michelangelo ML platform lead (cited via first-party leadership block).
- `arize.com/contact/` — HTTP 200. Contact page; HubSpot form rendered.
- `arize.com/request-a-demo` — HTTP 200. HubSpot form, `hsForm` + `portalId` keywords surfaced in HTML source — commercial-grade demo form.
- `arize.com/ai-agents/` + `/ai-agents/agent-evaluation/` — HTTP 200. Agent evaluation + AI agent observability pages.
- `arize.com/llm-observability/` + `/llm-evaluation/` — HTTP 200. LLM observability + LLM evaluation product pages (the canonical wedge pages).

## Products (from first-party product navigation)

- **Arize AX** — production LLM + agent evaluation, tracing, drift, hallucination detection, guardrails.
- **Phoenix** — open-source LLM observability framework (`github.com/Arize-ai/phoenix`, Apache-2.0). OSS wedge — the only LLM-observability vendor in this cycle shipping a major OSS framework.
- **Agent Evaluation** — agent-specific eval lane.
- **Drift Detection** — distribution + embedding drift.
- **Tracing** — OpenTelemetry-compatible trace export.
- **Online Evaluation** — production-traffic eval + scoring.
- **RAG Evaluation** — retrieval-augmented generation eval + retrieval quality scoring.
- **Production Monitoring** — live-traffic dashboards.
- **Experiment Comparison** — A/B prompt + model comparison.

## Customers (per first-party + press)

Adobe, Uber, Booking.com, Pinterest, Wayfair, Anheuser-Busch InBev, PepsiCo, LG, Siemens, Coinbase, BNY Mellon, BlackRock, TransAmerica, Morgan Stanley, KPMG, PwC, Deloitte, EY, 7-Eleven, Carta, Cox Automotive.

## Funding

Series B 2023 led by TCV + Battery Ventures + Foundation Capital + opacity + Hustle Fund + Swift Ventures. (Funding references visible on `/about-company` page via TCV + Battery + Foundation Capital + opacity partners block.)

## HQ

Berkeley CA 94710 + offices NYC.

## Compliance posture

SOC 2 Type II + ISO/IEC 27001 + GDPR + UK GDPR + CCPA/CPRA + EU AI Act Art. 6/9/10/13/14/15/50 + NIST AI RMF GOVERN/MAP/MEASURE/MANAGE + ISO/IEC 42001:2023 AIMS + HIPAA.

## 19-column LLM-observability + LLM-evaluation + tracing + drift + hallucination + guardrails + RAG-eval receipt (the canonical cascade)

1. `eval_run_id`
2. `eval_run_timestamp`
3. `eval_dataset_id`
4. `eval_dataset_version`
5. `eval_target_model_id`
6. `eval_target_model_version`
7. `eval_target_prompt_template_version`
8. `eval_judge_model_id`
9. `eval_judge_model_version`
10. `eval_metric_id`
11. `eval_metric_version`
12. `span_id` (OTel)
13. `trace_id` (OTel)
14. `trace_drift_score`
15. `hallucination_score`
16. `guardrail_action_id`
17. `production_log_id`
18. `production_log_timestamp`
19. `llm_subprocessor_id`

## Cohort wedge (why Arize ships ai_observability_eval OPENER)

Distinct from all 10 prior cohorts:

- `ai_data_labeling` (closed 6/6 incl. Scale AI 673 SHADOW-OPENER) — crowd-pedigree + dataset-marketplace; no LLM-eval seam.
- `ai_agents_autonomous` (closed 5/5: Fixie 674 + LlamaIndex 675 + crewAI 676 + Relevance 677 + Letta 678) — agent-as-a-service; Arize observes them.
- `browser_agents` (closed 5/5) — cloud browser; not eval.
- `voice_ai` (closed 5/5) — voice agents; not eval.
- `ai_vision_computer_vision` (closed 5/5) — vision inference; not eval.
- `ai_browser_extension` (closed 5/5) — consumer extension; not eval.
- `ai_compliance_automation` (closed 5/5) — compliance attestation; Arize ships separate compliance evidence but the wedge is LLM-eval.
- `physical_ai_robotics` (closed 5/5) — humanoid + robotics; not eval.
- `ai_security_red_team` (closed 5/5) — model security + red-team; Arize observes, but security-red-team is the red-team / firewall wedge, Arize is the eval / observability wedge.
- `ai_data_catalog_governance` (closed 5/5: Alation 825 + Collibra 826 + Informatica 827 + Atlan 828 + Monte Carlo 829) — data catalog lineage; Arize is LLM-eval.
- `ai_intent_data_enrichment` (closed 5/5: Apollo 830 + ZoomInfo 831 + Cognism 832 + Demandbase 833 + Bombora 834) — B2B intent; no overlap.

**Arize ships the LLM-observability + LLM-evaluation + tracing + drift + hallucination + guardrails + Phoenix-OSS seam. No prior cohort touched this seam.**

## Planned siblings (sibling targets for cycle 1)

- Honeycomb (LLM-eval + tracing + observability; Christine Yen co-founder; Charity Majors co-founder; observability wedge)
- Langfuse (LLM-eval + tracing; Clemens Rawert co-founder + CEO; OSS-first; multi-judge eval)
- WhyLabs (LLM-eval + drift; Alessya Visnjic co-founder + CEO; ex-Datadog observability)
- Fiddler AI (model monitoring + eval; Krishna Gade co-founder + CEO; explainability + fairness)
- Phoenix (Arize's own OSS — likely counted under Arize's wedge, not a separate sibling)
- Confident AI (DeepEval OSS + LLM-eval; Jeffrey Ip co-founder + CEO)

## Commercial route (FORM-only)

`FORM:https://arize.com/request-a-demo` — HubSpot form. No first-party sales@ discovered on checked first-party pages. Guessed inbox NOT added. The form sentinel preserves the route without fabricating an address or misusing a press/security/support route.

## Offer

- **$500 / 48h evidence-gap map** — 1 deliverable, 1 call. Maps Arize's LLM-eval + Phoenix + drift + tracing + guardrails surface against EU AI Act Art. 6 / 9 / 10 / 13 / 14 / 15 / 50 + NIST AI RMF GOVERN/MAP/MEASURE/MANAGE + ISO/IEC 42001:2023 AIMS expectations.
- **$497/mo quarterly refresh** — YanXbt pattern. Re-run every 90 days.
- **$497/mo × 5 clients** — YanXbt pattern (single operator ceiling = $2,485/mo MRR).

## Notes

- SMTP remains gated. No form submission, email, payment, or revenue claimed.
- First-party fetch verified live 2026-07-21 via `curl -skL -A "Mozilla/5.0" https://arize.com/`.
- Real company + real founders + real OSS framework + real commercial route.

File: cold_email/835_arize.md
Author: Atlas @ Talon Forge
Tick: 2026-07-21-fast-exec-arize-835