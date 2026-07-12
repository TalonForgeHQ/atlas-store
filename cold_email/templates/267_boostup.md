# BoostUp.ai — EU AI Act audit-target prep (ai_sales_ai, 10th lead in pipeline)

**Vertical:** ai_sales_ai (sibling-target of Outreach + Salesloft + Persana + Artisan + Lavender + Gong + Clari + Apollo + Aviso + BoostUp + People.ai)
**Tier:** 1 — public SaaS AI-revenue-ops + AI-sales-coaching vendor with verifiable contact channel + SOC 2 + EU AI Act readiness posture
**Contact:** info@boostup.ai (verified live 2026-07-12 via curl scrape of https://boostup.ai/, HTTP 200, mailto:info@boostup.ai exposed in footer)
**Founder:** David Dussau (CEO, ex-Marketo + ex-Tibco + ex-Adobe)
**HQ:** San Jose California, USA + remote
**Funding:** Bootstrapped + private investors
**Customers:** Mid-market + enterprise B2B sales orgs
**Stack:** BoostUp.ai Sales Execution Platform + AI Revenue Forecasting + AI Pipeline Inspection + AI Coaching + AI Deal Acceleration + AI Conversation Intelligence + AI Account Intelligence + downstream-Salesforce/HubSpot/Dynamics-state-change

## The audit-trail surface (where BoostUp differs from the other 9 ai_sales_ai siblings)

BoostUp is the only AI-revenue-ops-platform-with-native-AI-pipeline-inspection + AI-deal-acceleration + AI-coaching + AI-conversation-intelligence + AI-account-intelligence in the pipeline. Distinct because BoostUp's audit-trail surface is the per-BoostUp-AI-pipeline-inspection-decision + per-BoostUp-AI-coaching-tip-decision + per-BoostUp-AI-conversation-intelligence-decision + per-BoostUp-AI-account-intelligence-decision + per-BoostUp-AI-deal-acceleration-decision + per-BoostUp-AI-revenue-forecast-step-decision + per-BoostUp-AI-quote-decision + per-BoostUp-AI-account-graph-traversal-decision + downstream-Salesforce/HubSpot/Dynamics-state-change + downstream-CRM-state-change join-table, which is fundamentally different from per-call-recording (Gong 167) + per-revenue-forecast-roll-up (Clari 173) + per-B2B-contact-graph (Apollo 174) + per-end-to-end-AI-revenue-platform (Aviso 175) + per-email-engagement-step (Outreach 138 / Salesloft 139) + per-AI-prospect-research (Persana 221) + per-AI-BDR (Artisan 222) + per-AI-sales-email-coaching (Lavender 117) + per-AI-sales-activity-capture-meeting-bot (People.ai 182) audit lanes.

## 5 audit gaps BoostUp uniquely owns (the 267th vertical-target's pre-sales audit positioning)

1. **End-to-end BoostUp-AI-pipeline-inspection + AI-coaching + AI-conversation-intelligence + AI-account-intelligence + AI-deal-acceleration + downstream-Salesforce/HubSpot/Dynamics-state-change 12-column provenance join-table per SOC 2 CC7.2 + ISO 27001 A.12.4 + ISO 42001 9.4 + EU AI Act Art. 12.** 12 columns: boostup_ai_pipeline_inspection_id + boostup_ai_coaching_tip_id + boostup_ai_conversation_intelligence_decision_id + boostup_ai_account_intelligence_decision_id + boostup_ai_deal_acceleration_decision_id + boostup_ai_revenue_forecast_step_id + boostup_ai_quote_id + downstream_salesforce_state_change_id + downstream_hubspot_state_change_id + downstream_dynamics_state_change_id + boostup_audit_log_entry_id + compliance_metadata_retention_until. Required for 7-year WORM retention + quarterly reconstruction drill on the mid-market + enterprise B2B sales org stack.

2. **BoostUp-AI-coaching + AI-conversation-intelligence + AI-pipeline-inspection training-corpus + fine-tune license-provenance per EU AI Act Art. 53(d) GPAI training-data transparency + Art. 53(1)(b) copyright-summary.** 9-column per-training-corpus-source join-table: boostup_ai_coaching_corpus_source_id + boostup_ai_conversation_intelligence_corpus_source_id + boostup_ai_pipeline_inspection_corpus_source_id + source_license_type + source_copyright_holder + source_attribution_chain + source_copyleft_flag + downstream_model_derivative_use + downstream_retention_until. The unique BoostUp lane because BoostUp's AI-coaching + AI-conversation-intelligence fine-tunes are derived from customer sales-conversation-history + coaching-tip-history + pipeline-inspection-history and the EU AI Act Art. 53(d) training-data-summary obligation propagates to every BoostUp customer.

3. **BoostUp-AI-pipeline-inspection + AI-account-intelligence cross-tenant data-isolation + downstream-CRM no-leakage evidence per SOC 2 CC6.1 + GDPR Art. 28 + EU AI Act Art. 10.** 12-column per-tenant isolation-evidence join-table: boostup_tenant_id + boostup_workspace_id + encryption_at_rest_hash + encryption_in_transit_hash + cross_tenant_isolation_test_result + per_tenant_cmk_byok_optionality + per_workspace_no_leakage_evidence + per_tenant_residue_cleanup_procedure + completion_of_deletion_timestamp + per_customer_no_leakage_evidence + per_tenant_data_source_no_leakage + regulatory_retain_until.

4. **BoostUp-AI-coaching + AI-deal-acceleration + AI-pipeline-inspection human-oversight + risk-classification per EU AI Act Annex III 4 high-risk + EU AI Act Art. 14 human-oversight-required.** 10-column per-decision human-oversight log: boostup_ai_coaching_tip_id + boostup_ai_deal_acceleration_decision_id + boostup_ai_pipeline_inspection_decision_id + downstream_salesforce_state_change_id + downstream_hubspot_state_change_id + downstream_dynamics_state_change_id + human_reviewer_id + human_override_decision + human_oversight_timing + boostup_audit_log_entry_id.

5. **BoostUp-AI-pipeline-inspection + AI-conversation-intelligence + AI-deal-acceleration customer-disclosure + EU AI Act Art. 50 transparency-obligation surface.** 12-column end-to-end BoostUp-AI-pipeline-inspection-to-downstream-Salesforce-state-change reconstruction linking boostup_ai_pipeline_inspection_id + boostup_ai_conversation_intelligence_decision_id + boostup_ai_deal_acceleration_decision_id + salesforce_state_change_id + hubspot_state_change_id + dynamics_state_change_id + customer_disclosure_audit_id + ai_transparency_label_audit_id + downstream_human_oversight_id + boostup_audit_log_entry_id + compliance_metadata_retention_until + downstream_revenue_impact_attribution_id.

## 14-question buyer checklist (the audit-prep engagement that closes BoostUp)

1. Which BoostUp-AI-pipeline-inspection-decision + BoostUp-AI-coaching-decision + BoostUp-AI-conversation-intelligence-decision + BoostUp-AI-account-intelligence-decision + downstream-Salesforce-state-change join-table columns are signed off in your 7-year WORM retention policy?
2. Which EU AI Act Art. 53(d) training-corpus-summary columns are exposed via BoostUp's customer-disclosure API?
3. Which BoostUp-AI-coaching + AI-conversation-intelligence + AI-pipeline-inspection fine-tune license-provenance rows are bit-for-bit reconstructable for the 5-year audit window?
4. Which BoostUp-AI-pipeline-inspection-decision + AI-deal-acceleration-decision events are gated by per-decision human-oversight per EU AI Act Art. 14?
5. Which cross-tenant BoostUp-AI-pipeline-inspection + AI-conversation-intelligence isolation-evidence rows pass per-tenant no-leakage testing per SOC 2 CC6.1?
6. Which BoostUp-AI-pipeline-inspection + AI-account-intelligence downstream-Salesforce-state-change events trigger AI-transparency-label-insertion per EU AI Act Art. 50?
7. Which BoostUp-AI-coaching + AI-conversation-intelligence prompt-injection-detection + jailbreak-detection events fire per OWASP LLM Top 10 LLM01 + LLM06?
8. Which BoostUp-AI-pipeline-inspection + AI-deal-acceleration decisions are subject to AI-fairness-bias-monitoring per EU AI Act Art. 10 + NIST AI RMF MEASURE?
9. Which BoostUp-AI-conversation-intelligence + AI-account-intelligence + downstream-Salesforce-state-change + downstream-HubSpot-state-change + downstream-Dynamics-state-change chain-of-custody hashes are reconcilable against your CRM's audit log?
10. Which BoostUp-AI-pipeline-inspection-decision revenue-impact-attribution rows reconcile against your Board-of-Directors published revenue forecast per SEC 17a-4 WORM?
11. Which BoostUp-AI-coaching + AI-conversation-intelligence downstream-CRM-state-change chain-of-custody-evidence rows pass the audit reconstruction drill cadence (quarterly for high-risk-classification workloads, annually otherwise)?
12. Which BoostUp-AI-pipeline-inspection + AI-deal-acceleration + AI-conversation-intelligence downstream-revenue-impact-attribution + downstream-CRM-billing join-table rows match your Finance team's GL extract per SOC 2 CC7.2 + IRS 6001 + 7-year retention?
13. Which BoostUp-AI-coaching + AI-conversation-intelligence customer-disclosure + AI-transparency-label audit rows are reconcilable against your customer-facing-DPA disclosures?
14. Which BoostUp-AI-pipeline-inspection + AI-account-intelligence per-payload prompt-injection detection-log + per-decision jailbreak-detection-log rows are bit-for-bit reconstructable for the EU AI Act Aug 2026 GPAI enforcement window?

## Cold-email 3-line opening (the audit-prep that ships)

David — your BoostUp AI pipeline-inspection + AI-coaching + AI-conversation-intelligence surface is exactly where the EU AI Act Annex III 4 high-risk classification lands hardest because every AI-coaching-tip + AI-pipeline-inspection-decision + AI-deal-acceleration-decision → downstream-Salesforce-state-change chain becomes an AI-act-disclosure-event the moment your customer's customer is a regulated entity. We're pre-selling a $1,400 / 2-3 hour audit-prep engagement that lands a signed-off 12-column BoostUp-AI-pipeline-inspection + downstream-Salesforce-state-change provenance join-table per SOC 2 CC7.2 + EU AI Act Art. 12 — so your customer's CISO signs off in a single review meeting instead of 6-8 weeks of back-and-forth. Worth a 15-min call this week to walk through the 14-question buyer checklist?

Best,
Atlas (Talon Forge)
ai-act-audit-prep · atlas-talonforge.example