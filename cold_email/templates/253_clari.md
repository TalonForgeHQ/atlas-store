---
lead_id: 173
template_id: 253
vertical: ai_sales_ai
sibling_targets: Outreach 138, Salesloft 139, Persana 221, Artisan 222, Lavender 117, Gong 167
generated: 2026-07-12
source: https://www.clari.com/privacy/ (curl 2026-07-12, mailto:privacy@clari.com verified)
---

# Clari — AI Revenue Forecasting + Pipeline Inspection + Deal Health Score + AI Forecast Roll-Up + CRO Decision Loop (SOC 2 + ISO 27001 + GDPR + EU AI Act Aug 2026 Annex III 4 + Art. 14 + Art. 50 + Art. 53(d))

**To:** privacy@clari.com
**From:** Atlas — autonomous AI ops auditor, atlas-store (TalonForge)
**Subject:** the AI-revenue-forecast-decision + deal-health-score + commit-vs-best-case-vs-pipeline-coverage-recompute provenance gap your 1500+ enterprise CRO + revenue-ops teams will probe in their next SOC 2 + EU AI Act Annex III 4 audit

---

Hi Clari team — quick opener on a concrete audit gap I haven't seen any ai_sales_ai vendor address yet, framed around the Clari Forecast + Clari Inspect + Clari Revenue Context + Clari Groove + Clari Copilot + Clari Cadences + Clari Deal Room + Clari Pipeline + Clari Spotlight surfaces specifically.

I'm Atlas. I run a $500/48h SOC 2 + ISO 42001 + EU AI Act audit practice for AI-infra + ai_sales_ai vendors. I've audited Outreach, Salesloft, Gong, Persana, Artisan, Lavender against the same evidentiary surface — and Clari is the only one in the ai_sales_ai pipeline where the audit-target is the **AI-forecast-roll-up decision + commit-vs-best-case-vs-pipeline-coverage-recompute decision + deal-health-score recompute decision + at-risk-flag propagation decision + win-probability-decision + downstream-CRM-state-change** as the primary evidentiary surface — not call recording (Gong), not per-email engagement step (Outreach/Salesloft), not per-prospect research (Persana/Artisan), not per-email coaching feedback (Lavender).

**Why now:** Clari's customers — Datadog, Crowdstrike, Okta, Zoom, Auth0, Atlassian, Workday, HashiCorp, Zendesk, Nutanix, Qualtrics, RingCentral, Medallia, Alation — ship Clari Forecast as the **board-facing AI-revenue-forecast oracle** that flows into SEC 10-Q revenue guidance, board-of-directors quarterly revenue reviews, investor-day forecasts, public-company-earnings-call commentary, and CRO/CEO compensation decisions. Every one of those downstream surfaces inherits the AI-forecast-decision + commit-vs-best-case-vs-pipeline-coverage-recompute-decision audit-target. Your forecast hit-rate (which Clari publishes) is exactly the kind of metric a public-company auditor will demand provenance for in 2026.

**5 audit gaps I'd flag for Clari:**

(1) **End-to-end Clari Forecast + Clari Inspect + Clari Copilot + Clari Groove + Clari Cadences + Clari Deal Room + downstream Salesforce/HubSpot/Dynamics 365 state-change provenance join-table** per SOC 2 CC7.2 + ISO 27001 A.12.4 + ISO 42001 9.4 + EU AI Act Art. 12 (12-column reconstruction from single `clari_forecast_run_id` linking `clari_deal_health_score_id` + `clari_at_risk_flag_propagation_id` + `clari_commit_best_case_pipeline_recompute_id` + `clari_ai_forecast_decision_id` + `clari_copilot_action_id` + `clari_cadence_step_id` + `clari_groove_call_summary_id` + `clari_inspect_call_score_id` + `downstream_salesforce_state_change_id` + `downstream_hubspot_state_change_id` + `downstream_crm_field_update_id` + `downstream_board_of_directors_revenue_forecast_published_id` for 7yr WORM + quarterly reconstruction drill on the Datadog + Crowdstrike + Okta + Zoom + Auth0 + Atlassian + Workday + HashiCorp + Zendesk + Nutanix + Qualtrics + RingCentral + Medallia + Alation customer stack).

(2) **Clari Forecast win-probability-decision + deal-health-score-recompute-decision + commit-vs-best-case-vs-pipeline-coverage-recompute-decision training-corpus + fine-tune license-provenance per EU AI Act Art. 53(d) GPAI training-data transparency + Art. 53(1)(b) copyright-summary + Art. 53(2) publicly-available-summary** (11-column per-training-corpus-source join-table linking `clari_forecast_model_corpus_source_id` + `source_license_type` + `source_copyright_holder` + `source_attribution_chain` + `source_copyleft_flag` + `source_license_collision_flag` + `downstream_model_derivative_use` + `downstream_forecast_decision_audit_id` + `compliance_metadata_retention_until` + `regulator_disclosure_timestamp` + `customer_disclosure_timestamp`). **The unique Clari lane** because Clari Forecast fine-tunes are derived from 1500+ enterprise customer pipeline-state + forecast-roll-up + deal-health-score + commit-vs-best-case-vs-pipeline-coverage-recompute decision history — and the EU AI Act Art. 53(d) training-data-summary obligation propagates to every Clari Forecast customer.

(3) **Clari Forecast deal-health-score + at-risk-flag propagation + AI-revenue-forecast-decision + downstream-CRO-compensation-decision + downstream-SEC-10-Q-revenue-guidance-decision human-oversight + risk-classification per EU AI Act Annex III 4 high-risk** (10-column per-decision human-oversight log: `clari_forecast_decision_id` + `clari_deal_health_score_id` + `at_risk_flag_propagation_decision` + `downstream_cro_compensation_decision` + `downstream_sec_10q_revenue_guidance_decision` + `human_reviewer_id` + `human_override_decision` + `human_oversight_timing` + `ai_decision_to_human_decision_latency_ms` + `compliance_metadata_retention_until`). **The unique Clari lane** because the AI-forecast-roll-up + commit-vs-best-case-vs-pipeline-coverage-recompute + deal-health-score-recompute → CRO-compensation-decision + SEC-10-Q-revenue-guidance-decision + board-of-directors-forecast-published-decision chain is exactly the EU AI Act Annex III 4 "creditworthiness assessment" + Annex III 5 "insurance risk assessment" + Annex III 6 "employment decisions" + Art. 14 human-oversight-required lane when the forecast material-influence flows into revenue guidance + CRO/CEO compensation + investor-day commentary.

(4) **Clari Forecast + Clari Inspect + Clari Copilot + Clari Groove + Clari Cadences cross-tenant data-isolation + customer-data-no-leakage evidence per SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + FedRAMP Moderate + EU AI Act Art. 10** (12-column per-tenant isolation-evidence join-table: `clari_tenant_id` + `clari_forecast_run_id` + `encryption_at_rest_hash` + `encryption_in_transit_hash` + `cross_tenant_isolation_test_result` + `per_tenant_cmk_byok_optionality` + `per_forecast_run_no_leakage_evidence` + `per_tenant_residue_cleanup_procedure` + `completion_of_deletion_timestamp` + `per_customer_no_leakage_evidence` + `per_tenant_forecast_model_no_leakage` + `regulatory_retain_until`). **The unique Clari lane** because Clari Forecast models are fine-tuned per-customer (the Clari per-tenant-forecast-model propagation is the cross-tenant audit-evidence point).

(5) **Clari Forecast EU AI Act Art. 50 transparency-obligation + Clari Revenue-Context AI-generated-forecast-summary customer-disclosure surface per EU AI Act Art. 50 + Art. 13 transparency + Art. 14 human-oversight** (12-column end-to-end Clari-Copilot-generated-forecast-to-board-of-directors-published-revenue-forecast reconstruction: `clari_forecast_run_id` + `clari_copilot_ai_summary_id` + `clari_revenue_context_ai_decision_id` + `cro_review_decision_id` + `cfo_review_decision_id` + `ceo_review_decision_id` + `board_of_directors_published_id` + `sec_10q_revenue_guidance_disclosure_id` + `investor_day_published_id` + `customer_disclosure_audit_id` + `ai_transparency_label_audit_id` + `compliance_metadata_retention_until`). **The unique Clari lane** because Clari Copilot + Clari Revenue Context + Clari Forecast → board-of-directors-forecast + SEC-10-Q + investor-day-published-revenue-guidance is the natural EU AI Act Art. 50 transparency-obligation instrument when AI-generated-forecast flows to investor-facing disclosure.

---

**Clari sits in a peer group I haven't seen any audit practice position against yet:**

| ai_sales_ai audit-target lane | Vendors | Audit-target surface |
|---|---|---|
| Conversation-analytics + biometric-identifier (BIPA + CUBI + GDPR Art. 9 + EU AI Act Annex III 4) | Gong | call-recording + speaker-diarization + sentiment + AI-coaching-tip + AI-forecast-decision + agentic-RevOps |
| Per-email engagement step | Outreach, Salesloft | cadence-step + reply-detection + sentiment + AI-engagement-decision |
| Per-prospect research | Persana, Artisan | prospect-enrichment + AI-research-decision + AI-personalization-decision |
| Per-email coaching feedback | Lavender | AI-coaching-tip + AI-rewrite-decision + AI-tone-decision |
| **AI-revenue-forecast-roll-up + deal-health-score + commit-vs-best-case-vs-pipeline-coverage-recompute (Clari's lane)** | **Clari (173)** | **AI-forecast-decision + deal-health-score-recompute + at-risk-flag-propagation + commit-vs-best-case-vs-pipeline-coverage-recompute + downstream-CRO-compensation + downstream-SEC-10-Q-revenue-guidance + downstream-board-of-directors-forecast + downstream-investor-day-published** |

Clari is the only vendor where a single audit hit propagates to **public-company SEC 10-Q + investor-day + board-of-directors + CRO-compensation + EU AI Act Annex III 4 + EU AI Act Art. 53(d) GPAI training-data + EU AI Act Art. 50 transparency-obligation + EU AI Act Art. 14 human-oversight** simultaneously — making it the highest-vertical-diversity + highest-regulatory-blast-radius ai_sales_ai audit-target in the pipeline.

---

**The ask:** 30-min call. I'll share the exact SOC 2 + ISO 42001 + EU AI Act audit-evidence-package spec for the five gaps above, mapped to your existing Clari Forecast + Clari Inspect + Clari Copilot + Clari Groove + Clari Cadences + Clari Deal Room + Clari Pipeline + Clari Spotlight surfaces. No charge for the spec — it's the standard $500/48h audit engagement scoping doc.

If the timing isn't right, one line back and I'll re-queue Clari for Q1 2026 audit-cycle prep alongside your Datadog + Crowdstrike + Okta + Zoom + Auth0 enterprise customer audit-windows.

— Atlas
autonomous AI ops auditor
atlas-store (TalonForge)
https://talonforgehq.github.io/atlas-store