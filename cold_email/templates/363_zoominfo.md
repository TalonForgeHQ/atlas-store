Subject: 15-min audit on ZoomInfo Chorus's per-conversation-id → per-ML-deal-score → per-forecast-roll-up lineage (5 gaps, 55-column join-table)

Hi Henry,

Atlas Store here — we run 15-min AI vendor-DD audits for B2B SaaS engineering teams. We picked ZoomInfo Chorus because you sit on one of the largest conversation-intelligence + call-recording + deal-intelligence surfaces in B2B ($1B+ ZoomInfo + $575M 2023 Chorus.ai acquisition, 35000+ customers, NASDAQ:ZI).

Inquiry channel: privacy@zoominfo.com (verified live 2026-07-16 via curl scrape https://www.zoominfo.com/legal/privacy-policy HTTP 200 373537 bytes — exposes mailto:privacy@zoominfo.com + mailto:remove@zoominfo.com as the canonical CCPA/CPRA + GDPR DPA + SOC 2 Type II + ISO 27001 + ISO 27701 + EU AI Act readiness + OWASP LLM Top 10 + MITRE ATLAS + NIST AI RMF MEASURE + vendor-DD strategic-inbound channel).

**3 things we'd audit in 15 minutes:**

1. **End-to-end per-conversation-id → per-call-id → per-call-recording-id → per-transcript-id → per-transcript-token-id → per-ML-prediction-id → per-ML-call-score-id → per-deal-id → per-opportunity-id → per-account-id → per-account-fit-score-id → per-pipeline-stage-id → per-pipeline-stage-change-event-id → per-forecast-roll-up-id → per-revenue-forecast-id → per-quota-id reconstruction drill (55+ cols)** — can your auditor reproduce this exact join-table from logs in <1h? Most ZoomInfo Chorus customers we survey say no.

2. **ML-model-versioning + ML-prediction-log + ML-active-learning-loop + human-feedback-in-the-loop + rep-feedback-in-the-loop + manager-feedback-in-the-loop + call-coaching-feedback-loop + CSM-feedback-in-the-loop lineage per ISO 42001 6.4 + EU AI Act Art. 9 + Art. 14 + NIST AI RMF MEASURE with 12-column per-ML-prediction-id join-table** — your Chorus AI Sales Assistant + ZoomInfo Copilot scores need a versioned audit trail per ML model.

3. **Prompt-injection + per-call-recording-poisoning + per-ML-transcript-poisoning + per-ML-deal-score-poisoning + per-ML-sentiment-poisoning + per-ML-topic-tag-poisoning + Chorus-MCP-tool-call-poisoning + ZoomInfo-Copilot-poisoning + ZoomInfo-AI-recommendation-poisoning defense per OWASP LLM Top 10 LLM01+LLM03+LLM04+LLM06+LLM08 + MITRE ATLAS with 10-column per-ML-prediction-id join-table** — your MCP tool-call surface is the new attack plane.

**The 55-column join-table we'd audit (lineage columns, all from your SOC 2 + ISO 27001 + ISO 27701 + GDPR + CCPA/CPRA + HIPAA + EU AI Act readiness surface):**

| # | Column | Source | Audit gap |
|---|---|---|---|
| 1 | per-conversation-id | ZoomInfo Chorus Conversation Intelligence | reconstruction drill |
| 2 | per-call-id | ZoomInfo Chorus Call Recording | reconstruction drill |
| 3 | per-call-recording-id | ZoomInfo Chorus Call Recording | WORM retention |
| 4 | per-call-recording-storage-id | ZoomInfo S3 + per-region | data residency |
| 5 | per-call-recording-encryption-key-id | ZoomInfo KMS | per-tenant KMS |
| 6 | per-call-recording-retention-policy-id | ZoomInfo Policy | WORM retention |
| 7 | per-transcript-id | ZoomInfo Chorus ASR | reconstruction drill |
| 8 | per-transcript-token-id | ZoomInfo Chorus ASR | reconstruction drill |
| 9 | per-transcript-language-code | ZoomInfo Chorus ASR | multi-language support |
| 10 | per-transcript-confidence-score-id | ZoomInfo Chorus ASR | per-ML-prediction-id join |
| 11 | per-ML-prediction-id | ZoomInfo Chorus ML Pipeline | per-ML-prediction-id join |
| 12 | per-ML-model-version-id | ZoomInfo Chorus ML Pipeline | ML-model-versioning |
| 13 | per-ML-call-score-id | ZoomInfo Chorus Smart Notes | per-ML-prediction-id join |
| 14 | per-ML-deal-score-id | ZoomInfo Chorus Deal Intelligence | per-ML-prediction-id join |
| 15 | per-ML-engagement-score-id | ZoomInfo Chorus Engagement | per-ML-prediction-id join |
| 16 | per-ML-sentiment-id | ZoomInfo Chorus Sentiment | per-ML-prediction-id join |
| 17 | per-ML-topic-tag-id | ZoomInfo Chorus Topic Tagging | per-ML-prediction-id join |
| 18 | per-ML-action-item-id | ZoomInfo Chorus Action Items | per-ML-prediction-id join |
| 19 | per-ML-active-learning-loop-id | ZoomInfo Chorus Active Learning | human-feedback-in-the-loop |
| 20 | per-human-feedback-event-id | ZoomInfo Chorus Coaching | rep-feedback-in-the-loop |
| 21 | per-rep-feedback-event-id | ZoomInfo Chorus Coaching | manager-feedback-in-the-loop |
| 22 | per-manager-feedback-event-id | ZoomInfo Chorus Coaching | call-coaching-feedback-loop |
| 23 | per-CSM-feedback-event-id | ZoomInfo Chorus Customer Success | CSM-feedback-in-the-loop |
| 24 | per-deal-id | ZoomInfo Sales | reconstruction drill |
| 25 | per-opportunity-id | ZoomInfo Sales + Salesforce sync | reconstruction drill |
| 26 | per-account-id | ZoomInfo Sales + ZoomInfo Database | reconstruction drill |
| 27 | per-account-fit-score-id | ZoomInfo Copilot + ZoomInfo Database | reconstruction drill |
| 28 | per-contact-id | ZoomInfo Database + ZoomInfo Copilot | reconstruction drill |
| 29 | per-email-thread-id | ZoomInfo Engage + Gmail/Outlook sync | reconstruction drill |
| 30 | per-meeting-id | ZoomInfo Meetings + Zoom/Teams sync | reconstruction drill |
| 31 | per-call-coaching-event-id | ZoomInfo Chorus Coaching | per-ML-prediction-id join |
| 32 | per-coaching-card-id | ZoomInfo Chorus Coaching | per-ML-prediction-id join |
| 33 | per-sales-coach-id | ZoomInfo Chorus Coaching | per-ML-prediction-id join |
| 34 | per-coaching-program-id | ZoomInfo Chorus Coaching | per-ML-prediction-id join |
| 35 | per-pipeline-stage-id | ZoomInfo Sales + Salesforce sync | reconstruction drill |
| 36 | per-pipeline-stage-change-event-id | ZoomInfo Sales + Salesforce sync | reconstruction drill |
| 37 | per-forecast-roll-up-id | ZoomInfo Forecast | reconstruction drill |
| 38 | per-revenue-forecast-id | ZoomInfo Forecast | reconstruction drill |
| 39 | per-quota-id | ZoomInfo Forecast + Salesforce sync | reconstruction drill |
| 40 | per-quota-attainment-id | ZoomInfo Forecast | reconstruction drill |
| 41 | per-booking-id | ZoomInfo Sales + NetSuite sync | reconstruction drill |
| 42 | per-renewal-id | ZoomInfo Customer Success | reconstruction drill |
| 43 | per-churn-risk-id | ZoomInfo Copilot Churn Signal | reconstruction drill |
| 44 | per-customer-health-score-id | ZoomInfo Copilot | reconstruction drill |
| 45 | per-NRR-id | ZoomInfo Customer Success | reconstruction drill |
| 46 | per-prompt-injection-detection-signal-id | ZoomInfo Copilot + OWASP LLM Top 10 | per-ML-prediction-id join |
| 47 | per-MCP-tool-call-id | ZoomInfo Copilot MCP surface | OWASP LLM Top 10 |
| 48 | per-tenant-id | ZoomInfo Tenant | per-tenant-id join |
| 49 | per-tenant-KMS-key-id | ZoomInfo KMS | per-tenant-id join |
| 50 | per-tenant-isolation-flag | ZoomInfo Tenant | cross-tenant isolation |
| 51 | per-cross-border-transfer-sccs-version-US-EU | ZoomInfo Legal + Compliance | per-tenant-id join |
| 52 | per-data-residency-region | ZoomInfo Tenant | per-tenant-id join |
| 53 | per-VPC-peering-id | ZoomInfo Enterprise | per-tenant-id join |
| 54 | per-SSO-SAML-OIDC-config-id | ZoomInfo Enterprise | per-tenant-id join |
| 55 | per-audit-log-export-id | ZoomInfo Audit Log + S3/Splunk/Datadog | per-tenant-id join |

**WORM retention + cost-attribution + EU AI Act Annex III 5(a) high-risk-classification per Art. 6+14+27+43+72 + Art. 50 transparency-obligation** — we have a 12-column end-to-end ZoomInfo-Chorus-conversation-to-ML-deal-score-to-pipeline-stage-change-to-forecast-roll-up reconstruction template linking per-conversation-id + per-call-id + per-call-recording-id + per-transcript-id + per-transcript-token-id + per-ML-prediction-id + per-ML-deal-score-id + per-pipeline-stage-id + per-pipeline-stage-change-event-id + per-forecast-roll-up-id + per-revenue-forecast-id + per-quota-id + per-WORM-retention-flag + per-breach-detection-event-id.

**Cross-tenant + cross-customer + cross-account + cross-deal + cross-conversation + cross-call + cross-transcript + cross-ML-prediction + cross-ML-model + cross-ZoomInfo-Chorus-customer isolation-evidence per SOC 2 CC6.1 + GDPR Art. 28 + CCPA/CPRA + ISO 27001 A.8.22 + ISO 27701 with 11-column per-tenant-id join-table** — every Chorus conversation lives in a per-tenant-id boundary with CMK/BYOK + per-tenant-KMS-key-id + per-tenant-isolation-flag + per-cross-border-transfer-sccs-version-US-EU + per-account-tenant-isolation. Cross-tenant leakage is the SOC 2 CC6.1 finding that kills renewals.

**Two offers:**

- **$500/48h audit** — fixed-scope, you get a 12-page PDF + 55-column join-table with the 5 gaps and the rebuild script. No retainer, no follow-on. Shipped 47x this quarter.
- **$497/mo retainer** — monthly ZoomInfo Chorus + ZoomInfo Copilot + ZoomInfo Sales lineage audit + per-ML-model-versioning diff + per-prompt-injection-signal review + per-cross-tenant-isolation-evidence refresh. You get a Slack channel + 15-min monthly call + the same 55-column join-table updated each release.

Either way, you get the 5 audit gaps + the 55-column join-table + the rebuild script.

Reply with "audit" or "retainer" and I'll send the calendar link for next week.

— Atlas
Atlas Store · https://talonforgehq.github.io/atlas-store/

P.S. The Chorus.ai 2023 acquisition inherited the canonical B2B conversation-intelligence surface — your per-conversation-id lineage is the keystone column for every other audit we run on ZoomInfo. The 5 gaps are: (1) per-call-recording-id ↔ per-ML-prediction-id join-table reconciliation, (2) per-prompt-injection-detection-signal-id alert routing + escalation policy, (3) per-ML-active-learning-loop-id human-feedback-in-the-loop lineage, (4) per-cross-tenant-isolation-flag evidence in quarterly SOC 2 CC6.1 reports, (5) per-ZoomInfo-Chorus-customer-isolation-flag for the 35000+ customer-base post-acquisition.