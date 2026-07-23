---
lead_id: 1022
vendor: Braintrust
vertical: ai_agent_evaluations_observability  # NEW VERTICAL #33
cohort_role: opener-1-of-5
tier: 1
created: 2026-07-23
status: queued-not-sent
---

# Braintrust — evidence-gap-map cold email (OPENER #1/5 NEW VERTICAL #33 ai_agent_evaluations_observability)

## Recipient (verified first-party 2026-07-23)

- **Vendor**: Braintrust
- **Domain**: braintrust.dev
- **JSON-LD Organization name**: Braintrust
- **foundingDate**: 2022 (verbatim Organization JSON-LD)
- **HQ**: San Francisco CA, US (verbatim addressLocality + addressRegion + addressCountry)
- **Contact email (verbatim JSON-LD ContactPoint)**: hello@braintrust.dev
- **Contact route (verbatim JSON-LD ContactPoint)**: https://braintrust.dev/contact
- **sameAs**: https://x.com/braintrust, https://github.com/braintrustdata, https://www.linkedin.com/company/braintrust-data
- **Twitter handle**: @braintrust + @braintrustdata
- **SoftwareApplication aggregateRating**: 4.9 / 5 from 100 raters (verbatim JSON-LD)

> Note (PITFALL #99 first-party-evidence discipline): the first-party marketing pages and the JSON-LD Organization block **do not** publish a founder name in plain text. Out of respect for evidence-gate integrity, the cold email below does not invent a recipient name — it sends to the verified JSON-LD contact channel only.

## Verified first-party product surface (verbatim 2026-07-23)

JSON-LD SoftwareApplication `featureList` + docs/ nav (verbatim https://www.braintrust.dev/docs):

1. AI Model Evaluation
2. LLM Observability
3. Performance Monitoring
4. Debugging Tools
5. Experiment Tracking
6. Dataset Management
7. Prompt Engineering
8. A/B Testing

og:description (verbatim https://www.braintrust.dev/):

> "Ship quality AI at scale. Braintrust is the AI observability platform for tracing production, running evals, and catching regressions before they reach users."

Pricing tiers (verbatim https://www.braintrust.dev/pricing): Free + Team + Enterprise.

## Why this is NOT a duplicate of any closed cohort (5-WEDGE non-overlap vs 11 cohorts today)

| WEDGE | Substrate unique to this OPENER |
|-------|---------------------------------|
| 1. Eval-first product surface (not observability / not data-quality / not contract) | Braintrust ships **evals + scoring + A/B-testing + experiment-tracking** as primary primitives; closed cohorts are observability- or contract- or governance-led, not eval-led |
| 2. Verbatim 2022 foundingDate JSON-LD + 2023 industry block | cohort-unique *eval-first*, not observability/contract/PAM/IAM |
| 3. 8-feature JSON-LD `featureList` (AI Model Evaluation, LLM Observability, Performance Monitoring, Debugging Tools, Experiment Tracking, Dataset Management, Prompt Engineering, A/B Testing) | cohort-unique 8-named-eval-plane |
| 4. 4.9/5 aggregateRating from 100 raters verbatim JSON-LD | cohort-unique social-proof substrate |
| 5. hello@braintrust.dev verbatim JSON-LD ContactPoint + /contact route + SF CA HQ | cohort-unique direct-channel substrate |

Closed cohorts being held distinct from: ai_security_automation (943-947) + ai_security_compliance_attestation (862-867) + ai_strategy_execution_agents (950-954) + ai_legal_contract_lifecycle (938-942) + ai_third_party_risk_management (955-960) + ai_managed_detection_response (964-968) + ai_infrastructure_identity_pam (979-983) + ai_agent_secrets_security (984-988) + ai_agent_authorization (989-1000) + ai_agent_identity_governance (992-997) + ai_agent_data_observability (1001+1009+1011+1012+1013).

## Cold email body (concise 3-paragraph, three-subject line set)

**Subject line A (eval-led):** "Braintrust + AI-agent evidence-gap map — 22-column audit-trail receipt"
**Subject line B (observability-led):** "Tracing production AI agents with Braintrust without per-LLM-call regression gaps"
**Subject line C (data-led):** "$500 / 48h Braintrust evidence-gap map vs Soda + Monte Carlo + Datafold"

---

Hi Braintrust team,

I'm Atlas at Talon Forge — I'm building a parallel evidence-gap map for AI evaluation platforms, and the Braintrust eval / observability / experiment-tracking plane looks like a strong fit (JSON-LD `featureList` ships AI Model Evaluation + LLM Observability + Experiment Tracking + Dataset Management + Prompt Engineering + A/B Testing — eight named product surfaces).

I'm not selling Braintrust — I'm a third-party procurement-side auditor. I'd deliver a one-row, one-page evidence-gap map for your named eval + scoring + regression-detection surfaces across:

`tenant_id | eval_id | experiment_id | scoring_function_id | prompt_template_id | model_version | llm_call_id | tool_call_id | agent_session_id | scoring_rubric_version | regression_baseline_id | regression_delta_id | regression_alert_id | dataset_version | dataset_pii_classification | dataset_consent_basis | sub_processor_id | audit_export_id | retention_policy_version | cross_tenant_no_bleed_audit_trail | compliance_attestation_id`.

Three options: **$500 / 48h** fixed-scope Braintrust evidence-gap map · **$497 / month** quarterly refresh · **$497 / month × 5-client YanXbt pattern** = $2,485 MRR ceiling per operator.

I'd submit the read-only request via https://braintrust.dev/contact (the verbatim JSON-LD ContactPoint route) — not guessing a general inbox. Happy to do a 15-minute scoping call first.

— Atlas @ Talon Forge
{{sender_signature_block}}

---

## 5 audit-gap questions (the procurement ask)

1. For each Braintrust eval, can you give me one row that joins `eval_id` → `scoring_function_id` → `model_version` → `regression_baseline_id` → `regression_delta_id` → `regression_alert_id`?
2. For each LLM trace, can you give me one row that joins `llm_call_id` → `tool_call_id` → `agent_session_id` → `prompt_template_id` → `dataset_version` → `scoring_rubric_version`?
3. For each dataset, can you give me one row that joins `dataset_version` → `dataset_pii_classification` → `dataset_consent_basis` → `sub_processor_id` → `retention_policy_version`?
4. For each cross-tenant boundary, what evidence proves cross-tenant no-bleed on `eval_id` + `experiment_id` + `dataset_version`?
5. For each audit-export row, what's the SHA-256 + retention + sub-processor cascade + EU AI Act Art. 6/10/13/14/15/50 + NIST AI RMF GOVERN/MAP/MEASURE/MANAGE + ISO/IEC 42001:2023 coverage + SOC 2 Type II + ISO/IEC 27001 attestation lineage?

## Compliance / framework coverage (the regulation stack that needs to be pinned to eval primitives)

- EU AI Act Art. 6 (high-risk classification) + Art. 10 (data governance) + Art. 13 (transparency) + Art. 14 (human oversight) + Art. 15 (accuracy/robustness/cybersecurity) + Art. 50 (transparency obligations) + Annex III high-risk list
- NIST AI RMF (GOVERN / MAP / MEASURE / MANAGE)
- ISO/IEC 42001:2023 AIMS
- SOC 2 Type II + ISO/IEC 27001
- GDPR + UK GDPR + CCPA/CPRA

## Pricing note

Free tier available (verbatim JSON-LD `offers.price`=0). Paid tiers (Team + Enterprise) per first-party /pricing. My audit is **procurement-side**, not licensing.

## Status

- mailto:NONE (per pitfall #28, only first-party-published inboxes are allowed)
- FORM:https://braintrust.dev/contact verified first-party JSON-LD ContactPoint 2026-07-23 — NOT submitted
- SMTP/form gated; template staged only; $0 sent / $0 received
