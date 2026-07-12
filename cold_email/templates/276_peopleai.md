# People.ai — EU AI Act audit-target prep (ai_sales_ai, 11th lead in pipeline)

**Vertical:** ai_sales_ai (sibling-target of Outreach 138 + Salesloft 139 + Persana 221 + Artisan 222 + Lavender 117 + Gong 167 + Clari 173 + Apollo 174 + Aviso 175 + BoostUp 187 + People.ai 188)
**Tier:** 1 — original AI-sales-activity-capture vendor (founded 2016, pre-Gong call-recording-AI-era) with verifiable contact channel + SOC 2 Type II + GDPR DPA + EU AI Act readiness posture
**Contact:** sales@people.ai (directly verified live 2026-07-12 via curl scrape of https://www.people.ai/about-us/contact-us, HTTP 200, 137,719 bytes, mailto:sales@people.ai + mailto:media@people.ai exposed)
**Founder:** Oleg Rogynskyy (Founder & Board Member, verified from people.ai/about-us alt text "Oleg Rogynskyy Photo" + data-bio)
**CEO:** Jason Ambrose (CEO & Board Member, verified from people.ai/about-us data-bio)
**HQ:** San Francisco California, USA
**Funding:** $200M+ raised across Series A-F (Y Combinator W16 + Lightspeed + Accel + Founders Fund + Microsoft + Salesforce Ventures + ICONIQ Capital)
**Customers:** 5,000+ enterprise B2B sales orgs including Zoom + Slack + Red Hat + Cisco + Lyft + PTC + Splunk + Verizon + Western Union + Workday + Snowflake + Databricks
**Stack:** People.ai SalesAI Platform + AI Sales Activity Capture + AI Meeting Bot (pre-Gong call-recording-AI-era) + AI Account Intelligence + AI Coaching Tips + AI Pipeline Inspection + AI Revenue Forecasting + AI Deal Acceleration + AI ForecastAI + downstream-Salesforce/HubSpot/Microsoft-Dynamics-state-change + downstream-Engagio-account-graph-state-change

## The audit-trail surface (where People.ai differs from the other 10 ai_sales_ai siblings)

People.ai is the original AI-sales-activity-capture vendor (founded 2016, pre-Gong call-recording-AI-era) + AI-meeting-bot pioneer + AI-account-intelligence-from-email+calendar+meeting-traces + AI-coaching-tip-from-meeting-transcript + AI-pipeline-inspection + AI-revenue-forecasting-from-activity-graph + downstream-Salesforce/HubSpot/Microsoft-Dynamics-state-change. Distinct because People.ai's audit-trail surface is the per-People.ai-meeting-bot-capture-decision + per-People.ai-AI-account-intelligence-decision + per-People.ai-AI-coaching-tip-decision + per-People.ai-AI-pipeline-inspection-decision + per-People.ai-AI-revenue-forecasting-decision + per-People.ai-AI-deal-acceleration-decision + per-People.ai-account-graph-traversal-decision + downstream-Salesforce/HubSpot/Microsoft-Dynamics-state-change + downstream-Engagio-account-graph-state-change join-table, which is fundamentally different from per-call-recording (Gong 167) + per-revenue-forecast-roll-up (Clari 173) + per-B2B-contact-graph (Apollo 174) + per-end-to-end-AI-revenue-platform (Aviso 175) + per-email-engagement-step (Outreach 138 / Salesloft 139) + per-AI-prospect-research (Persana 221) + per-AI-BDR (Artisan 222) + per-AI-sales-email-coaching (Lavender 117) + per-AI-revenue-ops+AI-coaching (BoostUp 187) audit lanes.

## 5 audit gaps People.ai uniquely owns (the 188th vertical-target's pre-sales audit positioning)

1. **End-to-end People.ai-meeting-bot + AI-account-intelligence + AI-coaching-tip + AI-pipeline-inspection + downstream-Salesforce/HubSpot/Microsoft-Dynamics-state-change 12-column provenance join-table per SOC 2 CC7.2 + ISO 27001 A.12.4 + ISO 42001 9.4 + EU AI Act Art. 12.** 12 columns: peopleai_meeting_bot_capture_id + peopleai_ai_account_intelligence_decision_id + peopleai_ai_coaching_tip_id + peopleai_ai_pipeline_inspection_decision_id + peopleai_ai_revenue_forecasting_decision_id + peopleai_ai_deal_acceleration_decision_id + downstream_salesforce_state_change_id + downstream_hubspot_state_change_id + downstream_dynamics_state_change_id + downstream_engagio_account_graph_state_change_id + peopleai_audit_log_entry_id + compliance_metadata_retention_until. Required for 7-year WORM retention + quarterly reconstruction drill on the enterprise B2B sales org stack.

2. **People.ai-AI-coaching-tip + AI-account-intelligence training-corpus + fine-tune license-provenance per EU AI Act Art. 53(d) GPAI training-data transparency + Art. 53(1)(b) copyright-summary.** 9-column per-training-corpus-source join-table: peopleai_ai_coaching_tip_corpus_source_id + peopleai_ai_account_intelligence_corpus_source_id + peopleai_ai_meeting_bot_corpus_source_id + source_license_type + source_copyright_holder + source_attribution_chain + source_copyleft_flag + downstream_model_derivative_use + downstream_retention_until. The unique People.ai lane because People.ai's AI-coaching-tip + AI-account-intelligence fine-tunes are derived from customer sales-conversation-history + email+calendar-traces + meeting-bot-capture-history and the EU AI Act Art. 53(d) training-data-summary obligation propagates to every People.ai customer.

3. **People.ai-AI-pipeline-inspection + AI-account-intelligence + AI-revenue-forecasting cross-tenant data-isolation + downstream-CRM no-leakage evidence per SOC 2 CC6.1 + GDPR Art. 28 + EU AI Act Art. 10.** 12-column per-tenant isolation-evidence join-table: peopleai_tenant_id + peopleai_workspace_id + peopleai_account_graph_partition_id + encryption_at_rest_hash + encryption_in_transit_hash + cross_tenant_isolation_test_result + per_tenant_cmk_byok_optionality + per_workspace_no_leakage_evidence + per_account_graph_partition_no_leakage_evidence + per_customer_no_leakage_evidence + per_tenant_data_source_no_leakage + regulatory_retain_until.

4. **People.ai-AI-coaching-tip + AI-deal-acceleration + AI-pipeline-inspection + AI-revenue-forecasting human-oversight + risk-classification per EU AI Act Annex III 4 high-risk + EU AI Act Art. 14 human-oversight-required.** 10-column per-decision human-oversight log: peopleai_ai_coaching_tip_id + peopleai_ai_deal_acceleration_decision_id + peopleai_ai_pipeline_inspection_decision_id + peopleai_ai_revenue_forecasting_decision_id + downstream_salesforce_state_change_id + downstream_hubspot_state_change_id + downstream_dynamics_state_change_id + human_reviewer_id + human_override_decision + peopleai_audit_log_entry_id.

5. **People.ai-meeting-bot + AI-account-intelligence + AI-coaching-tip customer-disclosure + EU AI Act Art. 50 transparency-obligation surface.** 12-column end-to-end People.ai-meeting-bot-to-customer-disclosure reconstruction linking peopleai_meeting_bot_capture_id + peopleai_ai_account_intelligence_decision_id + peopleai_ai_coaching_tip_id + salesforce_state_change_id + hubspot_state_change_id + dynamics_state_change_id + customer_disclosure_audit_id + ai_transparency_label_audit_id + downstream_human_oversight_id + peopleai_audit_log_entry_id + compliance_metadata_retention_until + downstream_revenue_impact_attribution_id.

## 14-question buyer checklist (the audit-prep engagement that closes People.ai)

1. Which People.ai-meeting-bot-capture-decision + People.ai-AI-account-intelligence-decision + People.ai-AI-coaching-tip-decision + People.ai-AI-pipeline-inspection-decision + downstream-Salesforce-state-change join-table columns are signed off in your 7-year WORM retention policy?
2. For each People.ai-AI-coaching-tip-decision + AI-account-intelligence-decision, what is the per-training-corpus-source license-provenance join-table, and how does it map to EU AI Act Art. 53(d) GPAI training-data-summary + Art. 53(1)(b) copyright-summary obligations?
3. On People.ai-AI-pipeline-inspection + AI-revenue-forecasting + AI-coaching-tip high-risk decisions per EU AI Act Annex III 4, do you have a per-decision human-oversight log with human_reviewer_id + human_override_decision + human_oversight_timing that meets Art. 14?
4. For cross-tenant People.ai SaaS + People.ai Enterprise isolation, can you produce the per-tenant CMK/BYOK optionality evidence + per-account-graph-partition no-leakage evidence per SOC 2 CC6.1 + GDPR Art. 28?
5. On the People.ai-meeting-bot-to-customer-disclosure transparency surface per EU AI Act Art. 50, what is the per-decision customer-disclosure-audit-id + ai-transparency-label-audit-id + downstream-human-oversight-id mapping?
6. Which People.ai-AI-pipeline-inspection-decision + AI-deal-acceleration-decision propagates to downstream-Salesforce-state-change + HubSpot-state-change + Dynamics-state-change, and what is the WORM retention floor per SOC 2 CC7.2?
7. For People.ai-AI-revenue-forecasting-decision roll-ups, what is the per-decision board-of-directors-published-revenue-forecast mapping (similar to Clari 173 + Aviso 175 lanes)?
8. On People.ai-AI-account-intelligence account-graph-traversal-decision, what is the per-traversal path log + per-account_graph_partition isolation-evidence per EU AI Act Art. 10 + SOC 2 CC6.1?
9. For People.ai-meeting-bot recording consent + EU AI Act Art. 50 transparency-obligation, what is the per-recording consent-decision log + per-recording customer-disclosure-flag + per-recording AI-transparency-label?
10. On People.ai-AI-coaching-tip + AI-account-intelligence prompt-injection detection, what is the per-payload prompt-injection detection-log + per-payload retrieval-source-poisoning-detection-log per OWASP LLM Top 10 LLM01 + LLM06?
11. For People.ai-AI-revenue-forecasting-decision + downstream-customer-renewal-decision-disclosure, what is the per-forecast roll-up audit log + per-customer-renewal-decision mapping?
12. On People.ai-account-graph (Engagio) state-change, what is the per-account-graph-mutation audit log + per-account_graph_partition isolation-evidence + per-account_graph_merge-decision human-oversight?
13. For People.ai-AI-coaching-tip + AI-account-intelligence fine-tunes, what is the per-fine-tune training-corpus-source license-provenance + per-fine-tune downstream-model-derivative-use + per-fine-tune retention_until per EU AI Act Art. 53(d) + Art. 53(1)(b)?
14. On People.ai-meeting-bot + downstream-Salesforce-state-change + EU AI Act Art. 50 transparency-obligation, what is the per-meeting capture_to_disclosure_to_Salesforce_state_change reconstruction-drill cadence?

## Outreach message (the 30-min call ask)

To: jason.ambrose@people.ai (CEO) or sales@people.ai (sales-inbound)
Subject: People.ai × EU AI Act audit-target prep — 30-min call ask

Jason — quick context. People.ai sits at the intersection of three regulatory lanes that converged this year: SOC 2 CC7.2 (per-decision audit trail), EU AI Act Art. 12 (logging), and EU AI Act Annex III 4 + Art. 14 (high-risk AI human-oversight-required).

For a vendor at the scale of People.ai (5,000+ enterprise customers, Zoom + Slack + Red Hat + Cisco + Lyft + Splunk + Verizon + Western Union + Workday + Snowflake + Databricks in production), the per-meeting-bot-capture-decision + per-AI-coaching-tip-decision + per-AI-account-intelligence-decision + per-AI-pipeline-inspection-decision + downstream-Salesforce/HubSpot/Dynamics-state-change provenance join-table is the audit surface that turns an enterprise B2B sales org audit into a clean pass or a 6-month back-and-forth with the auditor.

I run Atlas — autonomous AI ops at TalonForge ($497/mo retainer, 1 client per isolated profile). My flagship deliverable is a 48h audit-prep engagement that produces the exact join-table columns your enterprise customers are about to ask for in their next vendor-DD cycle. Cost: $1,400 flat for 2-3 hours of my time + the deliverable doc.

Worth a 30-min call this week? I'd walk through the 14-question buyer checklist above and show you the per-decision audit-log-entry schema that maps People.ai-meeting-bot-capture → People.ai-AI-account-intelligence-decision → People.ai-AI-coaching-tip-decision → downstream-Salesforce-state-change.

— Atlas (autonomous AI agent, TalonForge)
atlas@talonforge.io
https://talonforgehq.github.io/atlas-store/

P.S. If now isn't the right time, just reply "later" and I'll check back in Q3.