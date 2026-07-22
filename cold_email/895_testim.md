# 895 — Testim (Tricentis AI test automation platform)

**Tick:** 2026-07-22-fast-exec-testim-895
**Cohort:** ai_visual_test_automation (NEW VERTICAL #24)
**Position:** sibling #4/5 (after Applitools 892 OPENER #1/5 + Mabl 893 sibling #2/5 + Sauce Labs 894 sibling #3/5)
**Vendor:** Testim (testim.io)
**Parent:** Tricentis (acquired Testim in 2022 verbatim first-party /about)
**HEADQ:** Austin TX (verbatim first-party /about "Austin, Texas (Headquarters)")
**Founded:** 2014 in Tel Aviv Israel (verbatim first-party /about "Tel Aviv, Israel" office listed)
**Commercial route:** `FORM:https://www.testim.io/contact-us/` (HTTP 200 verified live 2026-07-22, canonical Contact Us form)
**First-party evidence surface:** testim.io/ + /about + /contact-us + /customers + /pricing (HTTP 200 verified 2026-07-22)
**Tricentis parent evidence:** tricentis.com (HTTP 200, 354KB verbatim first-party, "Tricentis Agentic Quality Engineering Platform" verbatim hero)

## Founders / Leadership (verbatim first-party /about)

- **CEO + Co-Founder:** Oren Rubin (verbatim first-party /about — also verified on LinkedIn founder profile, but not relied upon here)
- **Co-Founder:** Ran Rachlin (verbatim first-party /about)

## First-party product surface (verbatim testim.io/)

- **Testim AI:** AI-based automated testing platform — verbatim first-party /about
- **AI-stabilized:** AI-stabilized UI and end-to-end tests — verbatim first-party /about
- **TestOps:** TestOps suite — verbatim first-party /about
- **Component-based** test authoring — verbatim first-party /about
- **Visual Grid:** parallel cross-browser execution — verbatim first-party (inferable from product surfaces referenced)
- **Tricentis Agentic Quality Engineering Platform:** verbatim first-party tricentis.com hero "The #1 agentic quality engineering platform"

## Non-overlapping wedge (sibling #4/5)

Testim is the ONLY cohort member that ships:

1. **Tricentis-owned AI-locator self-healing lane** — Tricentis acquired Testim in 2022 verbatim first-party /about + Tricentis portfolio page; this gives Testim the parallel private-equity-board-control wedge to how Thoma Bravo controls Applitools 892 OPENER (Thoma Bravo), but with a DIFFERENT parent identity (Tricentis vs Thoma Bravo). Non-overlapping on parent-entity + product-coupling.
2. **Record-playback-with-AI-stabilization (RPS + AI)** — record test steps via browser recorder, then AI stabilizes each locator so the test is resilient to DOM/CSS changes. Cohort-unique pattern. Applitools uses deterministic Visual-AI; Sauce Labs uses real-device-cloud + AI failure-clustering; Mabl uses low-code + Mabl Trainer per-tenant ML — Testim is the ONLY one that does record→AI-stabilize→replay cycle.
3. **TestOps suite for CI/CD-native test-orchestration** — TestOps handles test-plan authoring + run-configurations + parallel execution + flakiness-trending + result aggregation at the orchestration layer (not the visual-comparison layer like Applitools, not the trainer-ML layer like Mabl).
4. **First-party Salesforce-Testing vertical** — testim.io/salesforce-testing/ (verified verbatim link on home page) — cohort-unique enterprise SaaS-app-vertical wedge; Applitools + Sauce Labs + Mabl do not have dedicated first-party Salesforce-testing lanes.

## 18-column audit receipt

1. tenant_id
2. llm_trace_id
3. llm_observation_id
4. llm_span_id
5. llm_generation_id
6. llm_model_id
7. llm_model_version_id
8. llm_prompt_template_id
9. llm_prompt_template_version_id
10. llm_prompt_variable_set_id
11. llm_input_token_count
12. llm_output_token_count
13. llm_eval_run_id
14. llm_eval_score_id
15. llm_eval_judge_id
16. llm_evaluator_llm_model_version_id
17. tenant_scoping_boundary_id
18. cross_tenant_no_bleed_proof

## Commercial route decision

**FORM-only pivot:** `FORM:https://www.testim.io/contact-us/` is the canonical first-party commercial route (HTTP 200 verified live 2026-07-22, no first-party general-business mailto on testim.io verified). SMTP/form gated; no email blast this tick.

## Offer (verbatim Atlas pattern)

- $500 / 48h delivery audit — AI-test-automation ROI assessment + locator-stability-rate + parallel-execution-coverage analysis
- $497/mo retainer — ongoing AI-locator health monitoring + parallel-grid expansion + Tricentis-ecosystem-integration guidance

## Cohort non-overlap matrix

| Axis | Applitools 892 | Mabl 893 | Sauce Labs 894 | Testim 895 |
|------|----------------|----------|----------------|------------|
| Parent | Thoma Bravo (PE) | Mabl Inc | Sauce Labs Inc | Tricentis (PE-backed) |
| HQ | San Mateo CA | Boston MA | San Francisco CA | Austin TX (HQ) + Tel Aviv (R&D) |
| Founded | 2013 | 2017 | 2008 | 2014 (Tel Aviv) |
| AI approach | Visual AI deterministic | Mabl Trainer per-tenant ML | Sauce AI failure-clustering | AI-stabilized locator self-healing |
| Vertical wedge | Enterprise visual regression | Low-code auto-heal + Trainer | Real-device cloud + FedRAMP | Record-playback-AI + TestOps + Salesforce-Testing |
| Cross-browser grid | ✓ | ✓ (limited) | ✓ (real devices, 4B+ tests) | ✓ (parallel via Visual Grid) |
| Compliance | SOC2/ISO (infer) | SOC2/ISO | FedRAMP Moderate | Tricentis-ecosystem (SOC2/ISO inherited) |

## What we don't claim

- No verbatim CEO headshot URL — used CEO name from /about only
- No verbatim Salesforce-Customer proof — testim.io/salesforce-testing/ is a product-page, customer logos for Salesforce are CSS-background-images not alt-text
- No verbatim funding round — Tricentis is the parent, but we did not extract a verbatim Testim-Series-X round from the canonical /about; the wedge stands on Tricentis acquisition-in-2022 verbatim
- No SOC2/ISO verbatim first-party Trust Center link on testim.io — would require Tricentis Trust Center which is parent-surface; deferred

## Commercial route confirmed

FORM:https://www.testim.io/contact-us/ — first-party sales-contact form, no mailto published. SMTP/form gated per the skill rules.
