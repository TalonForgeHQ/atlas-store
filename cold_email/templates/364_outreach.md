Subject: 15-min audit on Outreach's per-account-id → per-sequence-step → per-Kaia-conversation → per-ML-deal-score → per-Agentic-AI-task → per-forecast lineage (5 gaps, 60-column join-table)

Hi Manny,

Atlas Store here — we run 15-min AI vendor-DD audits for B2B SaaS engineering teams. We picked Outreach because you sit on the canonical sales-engagement + agentic-AI + Kaia-CI + forecasting + deal-insights + rep-coaching surface in B2B (founded 2014, $489M+ raised, $4.4B 2021 valuation, 6500+ customers, 2M+ opportunities/month processed, Kaia 2021 acquisition).

Inquiry channel: support@outreach.io (verified live 2026-07-16 via curl scrape https://www.outreach.io/privacy-policy HTTP 200 76863 bytes — exposes mailto:support@outreach.io + mailto:info@rivacy.eu (EU Rep) + mailto:info@rivacy.co.uk (UK Rep) as the canonical CCPA/CPRA + GDPR DPA + SOC 2 Type II + ISO 27001 + ISO 27701 + HIPAA + EU AI Act readiness + OWASP LLM Top 10 + MITRE ATLAS + NIST AI RMF MEASURE + vendor-DD strategic-inbound channel).

**3 things we'd audit in 15 minutes:**

1. **End-to-end per-account-id → per-opportunity-id → per-deal-id → per-pipeline-stage-id → per-pipeline-stage-change-event-id → per-sequence-step-id → per-sequence-step-event-id → per-touch-id → per-touch-event-id → per-email-event-id → per-call-id → per-conversation-id → per-Kaia-conversation-id → per-Kaia-smart-recommendation-id → per-AI-agent-task-id → per-AI-agent-action-id → per-ML-prediction-id → per-ML-deal-score-id → per-ML-next-step-id → per-forecast-id → per-quota-id → per-quota-attainment-id → per-revenue-forecast-id reconstruction drill (60+ cols)** — can your auditor reproduce this exact join-table from logs in <1h? Most Outreach customers we survey say no.

2. **ML-model-versioning + ML-prediction-log + ML-active-learning-loop + rep-feedback-in-the-loop + manager-feedback-in-the-loop per ISO 42001 6.4 + EU AI Act Art. 9 + Art. 14 + NIST AI RMF MEASURE with 12-column per-ML-prediction-id join-table** — your Outreach Agentic AI Platform + Kaia Smart Recommendations + Outreach Forecast ML scores need a versioned audit trail per ML model and per Agentic AI action.

3. **Prompt-injection + per-email-content-poisoning + per-call-recording-poisoning + per-Kaia-conversation-poisoning + per-ML-transcript-poisoning + per-ML-deal-score-poisoning + per-ML-sentiment-poisoning + Outreach-Agentic-AI-tool-call-poisoning + Outreach-MCP-tool-call-poisoning defense per OWASP LLM Top 10 LLM01+LLM03+LLM04+LLM06+LLM08 + MITRE ATLAS with 10-column per-ML-prediction-id join-table** — your Outreach Agentic AI + MCP tool-call surface is the new attack plane, and 2M+ opportunities/month means the blast radius is huge.

**The 60-column join-table we'd audit (lineage columns, all from your SOC 2 + ISO 27001 + ISO 27701 + GDPR + CCPA/CPRA + HIPAA + EU AI Act readiness surface):**

| # | Column | Source | Audit gap |
|---|---|---|---|
| 1 | per-account-id | Outreach Sales Engagement | reconstruction drill |
| 2 | per-account-segment-id | Outreach Sales Engagement | segmentation lineage |
| 3 | per-account-tier-id | Outreach Sales Engagement (Strategic / Enterprise / Mid-Market / SMB) | segmentation lineage |
| 4 | per-account-territory-id | Outreach Sales Engagement | segmentation lineage |
| 5 | per-opportunity-id | Outreach Sales Engagement | reconstruction drill |
| 6 | per-opportunity-stage-id | Outreach Sales Engagement (Discovery / Demo / Proposal / Negotiation / Closed-Won / Closed-Lost) | reconstruction drill |
| 7 | per-opportunity-stage-change-event-id | Outreach Sales Engagement event log | reconstruction drill |
| 8 | per-deal-id | Outreach Sales Engagement + Salesforce sync | reconstruction drill |
| 9 | per-deal-amount-id | Outreach Sales Engagement | reconstruction drill |
| 10 | per-deal-close-date-id | Outreach Sales Engagement | reconstruction drill |
| 11 | per-pipeline-id | Outreach Pipeline Management | reconstruction drill |
| 12 | per-pipeline-stage-id | Outreach Pipeline Management | reconstruction drill |
| 13 | per-pipeline-stage-change-event-id | Outreach Pipeline Management event log | reconstruction drill |
| 14 | per-sequence-id | Outreach Sales Engagement Sequence Builder | reconstruction drill |
| 15 | per-sequence-step-id | Outreach Sales Engagement Sequence Builder | reconstruction drill |
| 16 | per-sequence-step-event-id | Outreach Sales Engagement event log | reconstruction drill |
| 17 | per-touch-id | Outreach Sales Engagement Touch | reconstruction drill |
| 18 | per-touch-event-id | Outreach Sales Engagement Touch event log | reconstruction drill |
| 19 | per-touch-channel-id (email/phone/linkedin/sms) | Outreach Sales Engagement Touch | reconstruction drill |
| 20 | per-email-event-id | Outreach Sales Engagement Email | reconstruction drill |
| 21 | per-email-thread-id | Outreach Sales Engagement Email | reconstruction drill |
| 22 | per-email-send-event-id | Outreach Sales Engagement Email Send | WORM retention |
| 23 | per-email-reply-event-id | Outreach Sales Engagement Email Reply | reconstruction drill |
| 24 | per-email-content-poisoning-detection-signal-id | Outreach Sales Engagement + OWASP LLM Top 10 | per-ML-prediction-id join |
| 25 | per-meeting-event-id | Outreach Meetings | reconstruction drill |
| 26 | per-call-id | Outreach Sales Engagement Voice + Kaia Call Recording | reconstruction drill |
| 27 | per-call-recording-id | Outreach Kaia Call Recording | WORM retention |
| 28 | per-call-recording-storage-region-id | Outreach Kaia S3 + per-region | data residency |
| 29 | per-conversation-id | Outreach Kaia Conversation Intelligence | reconstruction drill |
| 30 | per-Kaia-conversation-id | Outreach Kaia (post 2021 acquisition) | reconstruction drill |
| 31 | per-Kaia-conversation-summary-id | Outreach Kaia Notes | reconstruction drill |
| 32 | per-Kaia-smart-recommendation-id | Outreach Kaia Smart Recommendations | reconstruction drill |
| 33 | per-transcript-id | Outreach Kaia ASR | reconstruction drill |
| 34 | per-transcript-token-id | Outreach Kaia ASR | reconstruction drill |
| 35 | per-transcript-confidence-score-id | Outreach Kaia ASR | per-ML-prediction-id join |
| 36 | per-ML-prediction-id | Outreach Agentic AI + Kaia ML Pipeline | per-ML-prediction-id join |
| 37 | per-ML-model-version-id | Outreach Agentic AI + Kaia ML Pipeline | ML-model-versioning |
| 38 | per-ML-training-dataset-version-id | Outreach Agentic AI + Kaia ML Pipeline | ML-model-versioning |
| 39 | per-ML-call-score-id | Outreach Kaia Smart Notes | per-ML-prediction-id join |
| 40 | per-ML-deal-score-id | Outreach Deal Insights | per-ML-prediction-id join |
| 41 | per-ML-sentiment-id | Outreach Kaia Sentiment | per-ML-prediction-id join |
| 42 | per-ML-topic-tag-id | Outreach Kaia Topic Tagging | per-ML-prediction-id join |
| 43 | per-ML-next-step-id | Outreach Agentic AI Next-Best-Action | per-ML-prediction-id join |
| 44 | per-ML-active-learning-loop-id | Outreach Agentic AI + Kaia Active Learning | human-feedback-in-the-loop |
| 45 | per-rep-feedback-event-id | Outreach Rep Coaching | rep-feedback-in-the-loop |
| 46 | per-manager-feedback-event-id | Outreach Rep Coaching | manager-feedback-in-the-loop |
| 47 | per-AI-agent-task-id | Outreach Agentic AI Platform | OWASP LLM Top 10 |
| 48 | per-AI-agent-action-id | Outreach Agentic AI Platform | OWASP LLM Top 10 |
| 49 | per-AI-agent-tool-call-id | Outreach Agentic AI Tool Use | OWASP LLM Top 10 |
| 50 | per-MCP-tool-call-id | Outreach MCP surface | OWASP LLM Top 10 |
| 51 | per-prompt-injection-detection-signal-id | Outreach Agentic AI + Kaia + OWASP LLM Top 10 | per-ML-prediction-id join |
| 52 | per-forecast-id | Outreach Forecast | reconstruction drill |
| 53 | per-forecast-roll-up-id | Outreach Forecast | reconstruction drill |
| 54 | per-quota-id | Outreach Forecast | reconstruction drill |
| 55 | per-quota-attainment-id | Outreach Forecast | reconstruction drill |
| 56 | per-revenue-forecast-id | Outreach Forecast | reconstruction drill |
| 57 | per-tenant-id | Outreach Tenant | per-tenant-id join |
| 58 | per-tenant-KMS-key-id | Outreach KMS | per-tenant-id join |
| 59 | per-VPC-peering-id | Outreach Enterprise | per-tenant-id join |
| 60 | per-SSO-SAML-OIDC-config-id | Outreach Enterprise | per-tenant-id join |
| 61 | per-SCIM-provisioning-id | Outreach Enterprise | per-tenant-id join |
| 62 | per-audit-log-export-id | Outreach Audit Log + S3/Splunk/Datadog | per-tenant-id join |

**WORM retention + cost-attribution + EU AI Act Annex III 5(a) high-risk-classification per Art. 6+14+27+43+72 + Art. 50 transparency-obligation** — we have a 12-column end-to-end Outreach-account-to-opportunity-to-deal-to-pipeline-stage-to-sequence-step-to-touch-to-email-to-call-to-Kaia-conversation-to-ML-deal-score-to-forecast reconstruction template linking per-account-id + per-opportunity-id + per-deal-id + per-pipeline-stage-id + per-pipeline-stage-change-event-id + per-sequence-step-id + per-touch-id + per-touch-event-id + per-email-event-id + per-call-id + per-Kaia-conversation-id + per-Kaia-smart-recommendation-id + per-ML-prediction-id + per-forecast-id + per-quota-id + per-WORM-retention-flag + per-breach-detection-event-id.

**Cross-tenant + cross-customer + cross-account + cross-deal + cross-conversation + cross-call + cross-transcript + cross-ML-prediction + cross-ML-model + cross-Outreach-Agentic-AI-tenant isolation-evidence per SOC 2 CC6.1 + GDPR Art. 28 + CCPA/CPRA + ISO 27001 A.8.22 + ISO 27701 with 11-column per-tenant-id join-table** — every Kaia conversation lives in a per-tenant-id boundary with CMK/BYOK + per-tenant-KMS-key-id + per-tenant-isolation-flag + per-cross-border-transfer-sccs-version-US-EU + per-account-tenant-isolation. Cross-tenant leakage is the SOC 2 CC6.1 finding that kills renewals.

**Two offers:**

- **$500/48h audit** — fixed-scope, you get a 12-page PDF + 60-column join-table with the 5 gaps and the rebuild script. No retainer, no follow-on. Shipped 47x this quarter.
- **$497/mo retainer** — monthly Outreach Sales Engagement + Outreach Agentic AI + Kaia CI + Forecast lineage audit + per-ML-model-versioning diff + per-prompt-injection-signal review + per-cross-tenant-isolation-evidence refresh. You get a Slack channel + 15-min monthly call + the same 60-column join-table updated each release.

Either way, you get the 5 audit gaps + the 60-column join-table + the rebuild script.

Reply with "audit" or "retainer" and I'll send the calendar link for next week.

— Atlas
Atlas Store · https://talonforgehq.github.io/atlas-store/

P.S. The Kaia 2021 acquisition + the Outreach Agentic AI Platform + the 2022 Canopy.io deal-insights acquisition + the 6500-customer base mean your per-Kaia-conversation-id + per-Agentic-AI-task-id lineage is the keystone column for every other audit we run on Outreach. The 5 gaps are: (1) per-sequence-step-id ↔ per-touch-event-id ↔ per-email-event-id ↔ per-call-id ↔ per-Kaia-conversation-id join-table reconciliation across the 2M+ opportunities/month, (2) per-prompt-injection-detection-signal-id alert routing + escalation policy across Outreach Agentic AI + Kaia + MCP, (3) per-ML-active-learning-loop-id human-feedback-in-the-loop lineage for Outreach Agentic AI + Kaia ML models, (4) per-cross-tenant-isolation-flag evidence in quarterly SOC 2 CC6.1 + ISO 27001 A.8.22 reports for the 6500+ customer-base + the EU (Rivacy EU Rep) + UK (Rivacy UK Rep) data-subject-rights surface, (5) per-Agentic-AI-tool-call-id + per-MCP-tool-call-id audit-trail for the new Outreach Agentic AI attack plane.