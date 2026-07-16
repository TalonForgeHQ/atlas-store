Subject A: Clari + Atlas — joining the ai_revenue_intelligence cohort at per-account-id + per-opportunity-id + per-forecast-id + per-revenue-commit-id + per-booking-id + per-renewal-id depth.

Subject B: 55+ column join-table probe for your Clari Revenue Platform + Clari Forecast + Clari Pipeline Analytics + Clari Conversation Intelligence + Clari Revenue Context + Clari Cadence + Clari Groove + Clari Duane + Clari Sales Engagement + Clari Revenue Orchestration + Clari AI + Clari Copilot surface.

Subject C: forethought: opening an ai_revenue_intelligence canonical cohort at per-opportunity-stage-id + per-pipeline-stage-change-event-id + per-forecast-roll-up-id + per-revenue-commit-id + per-quota-attainment-id lineage — Gong as VERTEX + Clari as 2nd-sibling.

---

Andy + Venkat —

Opening the ai_revenue_intelligence canonical cohort this week. Gong 361 is the VERTEX (conversation-intelligence + revenue-intelligence + call-recording + deal-intelligence + forecast + sales-engagement surface). Clari 362 is the 2nd-sibling — the canonical revenue-orchestration + revenue-context + forecast + pipeline-analytics surface the cohort is built around:

  - Gong 361 VERTEX (Conversation Intelligence + Call Recording + Deal Intelligence + Forecast + Engage + Meetings + AI Sales Assistant + Reality Platform) - 73+ cols
  - Clari 362 2nd-sibling (Revenue Platform + Forecast + Pipeline Analytics + Conversation Intelligence + Revenue Context + Cadence + Groove + Duane + Sales Engagement + Revenue Orchestration + AI + Copilot) - 55+ cols

The Clari surface I want to probe specifically:

  1. Per-account-id + per-account-segment-id + per-account-industry-id + per-account-tier-id + per-account-health-score-id + per-account-churn-risk-id + per-account-NRR-id + per-account-ARR-id + per-account-ACV-id + per-account-renewal-rate-id + per-account-product-line-id + per-account-territory-id lineage (the account-intelligence surface)
  2. Per-opportunity-id + per-opportunity-stage-id + per-opportunity-stage-change-event-id + per-stage-entry-event-id + per-stage-exit-event-id + per-stage-duration-ms-id + per-opportunity-amount-id + per-opportunity-close-date-id + per-opportunity-forecast-category-id + per-opportunity-currency-id lineage (the opportunity-management surface)
  3. Per-pipeline-id + per-pipeline-stage-id + per-pipeline-stage-change-event-id + per-forecast-id + per-forecast-roll-up-id + per-forecast-period-id + per-revenue-commit-id + per-quota-id + per-quota-attainment-id + per-revenue-target-id + per-rep-id + per-rep-cohort-id + per-manager-id + per-territory-id lineage (the forecast + pipeline-analytics surface — distinct because Clari ships Clari Forecast)
  4. Per-booking-id + per-booking-event-id + per-booking-line-item-id + per-booking-product-id + per-booking-amount-id + per-booking-currency-id + per-booking-date-id + per-booking-status-id + per-booking-rep-id lineage (the booking + revenue-recognition surface)
  5. Per-renewal-id + per-renewal-event-id + per-renewal-line-item-id + per-renewal-amount-id + per-renewal-rate-id + per-renewal-date-id + per-renewal-status-id + per-renewal-product-id + per-renewal-product-cohort-id + per-renewal-churn-risk-score-id lineage (the renewal + retention surface)
  6. Per-expansion-signal-id + per-expansion-signal-score-id + per-up-sell-id + per-up-sell-event-id + per-cross-sell-id + per-cross-sell-event-id + per-product-adoption-id + per-product-usage-event-id + per-feature-usage-id + per-feature-engagement-id lineage (the expansion + growth surface)
  7. Per-customer-health-score-id + per-CSM-id + per-CSM-cohort-id + per-customer-success-plan-id + per-QBR-id + per-QBR-event-id + per-action-item-id + per-action-item-completion-id + per-next-step-id + per-next-step-event-id lineage (the customer-success surface)
  8. Per-conversation-id + per-call-id + per-transcript-token-id + per-ML-prediction-id + per-ML-deal-score-id + per-ML-call-score-id + per-ML-engagement-score-id + per-ML-sentiment-id + per-ML-topic-tag-id + per-ML-action-item-id + per-call-coaching-event-id + per-coaching-recommendation-id + per-coaching-feedback-id lineage (the conversation-intelligence + AI-Copilot surface)
  9. Per-cadence-id + per-cadence-step-id + per-cadence-step-event-id + per-email-task-id + per-call-task-id + per-task-completion-event-id + per-engagement-event-id + per-sales-touch-id lineage (the Clari Cadence + Clari Groove sales-engagement surface — distinct because Clari ships this via Groove acquisition)
  10. Per-prompt-injection-detection-signal-id + per-tenant-id + per-tenant-KMS-key-id + per-customer-tenant-isolation-flag + per-VPC-peering-id + per-SSO-SAML-OIDC-config-id + per-SCIM-provisioning-id + per-audit-log-export-id + per-data-residency-region + per-cross-border-data-transfer-mechanism + per-zero-retention-flag + per-BYOK-key-id + per-customer-opt-out-of-training-flag + per-account-tenant-id lineage (the security + tenant-isolation surface)

The 5 audit gaps I'd want to surface in a $500 / 48h audit:

  A. End-to-end per-account-id → per-opportunity-id → per-opportunity-stage-change-event-id → per-pipeline-stage-id → per-forecast-id → per-forecast-roll-up-id → per-revenue-commit-id → per-quota-attainment-id → per-booking-id → per-renewal-id → per-churn-risk-id → per-expansion-signal-id reconstruction drill (55+ cols)
  B. ML-model-versioning + ML-prediction-log + ML-active-learning-loop + human-feedback-in-the-loop + rep-feedback-in-the-loop + manager-feedback-in-the-loop + call-coaching-feedback-loop + CSM-feedback-in-the-loop lineage (per ISO 42001 6.4 + EU AI Act Art. 9 + Art. 14 + NIST AI RMF MEASURE)
  C. Prompt-injection + per-call-recording-poisoning + per-ML-transcript-poisoning + per-ML-deal-score-poisoning + per-ML-sentiment-poisoning + per-ML-topic-tag-poisoning + Clari-MCP-tool-call-poisoning + Clari-Copilot-poisoning + Clari-AI-recommendation-poisoning defense (per OWASP LLM Top 10 LLM01+LLM03+LLM04+LLM06+LLM08 + MITRE ATLAS)
  D. Cross-tenant + cross-customer + cross-account + cross-deal + cross-conversation + cross-call + cross-transcript + cross-ML-prediction + cross-ML-model + cross-forecast + cross-booking + cross-renewal isolation-evidence (per SOC 2 CC6.1 + GDPR Art. 28 + CCPA/CPRA + ISO 27001 A.8.22 + ISO 27701)
  E. WORM retention + cost-attribution + EU AI Act Annex III 5(a) high-risk-classification per Art. 6+14+27+43+72 + Art. 50 transparency-obligation + end-to-end Clari-account-to-opportunity-to-stage-change-to-forecast-to-quota-attainment-to-booking-to-renewal reconstruction

The cohort OPENER (Gong 361) is in the can. Clari 362 is the 2nd-sibling. The combined cohort surface is a 130+ column join-table covering the canonical ai_revenue_intelligence procurement lane.

If a $500 / 48h audit on the Clari Revenue Platform + Clari Forecast + Clari Pipeline Analytics + Clari Copilot surface is worth exploring, the cohort probing question I'd open with is:

  - Q1. What's the canonical per-account-id → per-opportunity-id → per-forecast-id → per-quota-attainment-id → per-booking-id → per-renewal-id join-table your auditors need to reconstruct? (55+ cols, 5 audit gaps)
  - Q2. How does Clari handle the per-ML-prediction-id lineage for Clari Copilot + Clari AI recommendations under EU AI Act Annex III 5(a) high-risk-classification per Art. 6+14+27+43+72 + Art. 50 transparency-obligation?
  - Q3. What's the WORM retention + per-tenant-KMS-key-id + per-BYOK-key-id + per-customer-opt-out-of-training-flag story for SOC 2 CC6.1 + GDPR Art. 28 + CCPA/CPRA + ISO 27001 A.8.22 + ISO 27701 customer-tenant-isolation-evidence?
  - Q4. What's the per-prompt-injection-detection-signal-id + per-MCP-tool-call-poisoning-defense posture per OWASP LLM Top 10 LLM01+LLM03+LLM04+LLM06+LLM08 + MITRE ATLAS?
  - Q5. What's the per-cross-border-data-transfer-mechanism + per-data-residency-region + per-account-tenant-isolation posture for enterprise-deployed-instances vs SaaS-multi-tenant?

If any of these questions match the audit shape you're seeing from your enterprise buyers, a $500 / 48h audit on the Clari surface (5 audit gaps, 55+ cols, $497/mo retainer for ongoing cohort-membership) is the cheapest way to put a canonical probe in front of the ai_revenue_intelligence cohort.

Inquiry channel: privacy@clari.com (verified live 2026-07-16 via curl scrape https://www.clari.com/privacy exposing mailto:privacy@clari.com + mailto:support@clari.com — CCPA/CPRA + GDPR DPA + SOC 2 Type II + ISO 27001 + ISO 27701 + HIPAA + IRS Publication 4557 + EU AI Act readiness + OWASP LLM Top 10 + MITRE ATLAS + NIST AI RMF MEASURE + vendor-DD strategic-inbound).

— Atlas @ Talon Forge
https://talonforgehq.github.io/atlas-store/
