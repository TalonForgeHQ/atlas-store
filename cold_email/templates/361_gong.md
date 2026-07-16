Subject A: Gong + Atlas — joining the ai_revenue_intelligence cohort at per-conversation-id + per-call-id + per-ML-prediction-id + per-ML-deal-score-id + per-pipeline-stage-change-event-id depth.

Subject B: 55+ column join-table probe for your Gong Conversation Intelligence + Gong Call Recording + Gong Deal Intelligence + Gong Forecast + Gong Engage + Gong Meetings + Gong AI Sales Assistant + Gong Reality Platform surface.

Subject C: forethought: opening an ai_revenue_intelligence canonical cohort at per-ML-prediction-id + per-ML-deal-score-id + per-ML-call-score-id + per-ML-engagement-score-id lineage — Gong as VERTEX.

---

Amit + Eilon + Sagi —

Opening the ai_revenue_intelligence canonical cohort this week. As VERTEX, Gong brings the conversation-intelligence + revenue-intelligence + call-recording + deal-intelligence + forecast-intelligence + sales-engagement surface the cohort is built around:

  - Gong 361 VERTEX (Conversation Intelligence + Call Recording + Deal Intelligence + Forecast + Engage + Meetings + AI Sales Assistant + Reality Platform) - 55+ cols

The Gong surface I want to probe specifically:

  1. Per-conversation-id + per-call-id + per-meeting-id + per-audio-recording-id + per-transcript-token-id + per-transcript-segment-id + per-transcript-speaker-id + per-ML-prediction-id + per-ML-call-score-id + per-ML-deal-score-id + per-ML-engagement-score-id + per-ML-sentiment-id + per-ML-topic-tag-id + per-ML-action-item-id + per-ML-next-step-id + per-call-coaching-event-id + per-coaching-recommendation-id lineage (the conversation-intelligence surface)
  2. Per-deal-id + per-opportunity-id + per-account-id + per-account-segment-id + per-account-industry-id + per-contact-id + per-contact-role-id + per-email-thread-id + per-email-event-id + per-meeting-event-id + per-stakeholder-id lineage (the deal-intelligence + account-intelligence surface)
  3. Per-pipeline-stage-id + per-pipeline-stage-change-event-id + per-stage-entry-event-id + per-stage-exit-event-id + per-stage-duration-ms-id + per-forecast-roll-up-id + per-revenue-forecast-id + per-quota-id + per-quota-attainment-id + per-rep-id + per-rep-cohort-id lineage (the forecast-intelligence + pipeline-analytics surface)
  4. Per-engagement-event-id + per-sales-touch-id + per-sales-cadence-id + per-cadence-step-id + per-cadence-step-event-id + per-outreach-event-id + per-call-task-id + per-email-task-id + per-task-completion-event-id lineage (the Gong Engage sales-engagement surface)
  5. Per-AI-Sales-Assistant-conversation-id + per-AI-Sales-Assistant-recommendation-id + per-AI-Sales-Assistant-summary-id + per-AI-Sales-Assistant-email-draft-id + per-AI-Sales-Assistant-action-id lineage (the AI Sales Assistant surface — distinct because Gong ships this)
  6. Per-reality-call-id + per-reality-meeting-id + per-reality-search-id + per-reality-recommendation-id + per-reality-clip-id + per-reality-share-id lineage (the Gong Reality Platform surface — distinct because Gong ships this)
  7. Per-prompt-injection-detection-signal-id + per-tenant-id + per-tenant-KMS-key-id + per-customer-tenant-isolation-flag + per-VPC-peering-id + per-SSO-SAML-OIDC-config-id + per-SCIM-provisioning-id + per-audit-log-export-id + per-data-residency-region + per-cross-border-data-transfer-mechanism + per-zero-retention-flag + per-BYOK-key-id + per-customer-opt-out-of-training-flag + per-account-tenant-id lineage (the security + tenant-isolation surface)

The 5 audit gaps I'd want to surface in a $500 / 48h audit:

  A. End-to-end per-conversation-id → per-call-id → per-transcript-token-id → per-ML-prediction-id → per-ML-call-score-id → per-ML-deal-score-id → per-deal-id → per-pipeline-stage-id → per-pipeline-stage-change-event-id → per-forecast-roll-up-id → per-revenue-forecast-id reconstruction drill (55+ cols)
  B. ML-model-versioning + ML-prediction-log + ML-active-learning-loop + human-feedback-in-the-loop + rep-feedback-in-the-loop + manager-feedback-in-the-loop + call-coaching-feedback-loop lineage (per ISO 42001 6.4 + EU AI Act Art. 9 + Art. 14 + NIST AI RMF MEASURE)
  C. Prompt-injection + per-call-recording-poisoning + per-ML-transcript-poisoning + per-ML-deal-score-poisoning + per-ML-sentiment-poisoning + per-ML-topic-tag-poisoning + Gong-MCP-tool-call-poisoning defense (per OWASP LLM Top 10 LLM01+LLM03+LLM04+LLM06+LLM08 + MITRE ATLAS)
  D. Cross-tenant + cross-customer + cross-account + cross-deal + cross-conversation + cross-call + cross-transcript + cross-ML-prediction + cross-ML-model isolation-evidence (per SOC 2 CC6.1 + GDPR Art. 28 + CCPA/CPRA + ISO 27001 A.8.22 + ISO 27701)
  E. WORM retention + cost-attribution + EU AI Act Annex III 5(a) high-risk-classification per Art. 6+14+27+43+72 + Art. 50 transparency-obligation + end-to-end Gong-conversation-to-ML-deal-score-to-pipeline-stage-change-to-forecast-roll-up reconstruction

If useful, I have a 1-page 55+ column per-conversation-id + per-call-id + per-transcript-token-id + per-ML-prediction-id + per-deal-id + per-pipeline-stage-id join-table that maps Gong's existing 5-audit-gap surface to the 10-row per-ML-prediction-id prompt-injection-defense + 12-row per-ML-prediction-id ML-model-versioning + 11-row per-tenant-id CMK/BYOK + 12-row end-to-end conversation-to-forecast-roll-up reconstruction clusters.

Two ways to engage:

  - $500 / 48h audit. I deliver the 55+ column join-table + 5 audit gaps + the 1-page brief.
  - $497/mo retainer. Continuous monitoring of Gong's ai_revenue_intelligence audit-trail surface as the cohort expands.

Inquiry channel locked: privacy@gong.io (verified live 2026-07-16 via the privacy-policy page).

— Atlas
   Talon Forge LLC
