# 329 — Vanta — Trust Management Platform + Compliance Automation (compliance_automation, 1st sibling)

**Lead index:** 239
**Company:** Vanta
**Handle:** @VantaCompliance
**Email (verified live 2026-07-15):** `privacy@vanta.com`
**Website:** https://vanta.com
**Vertical:** compliance_automation
**Tier:** 1
**Evidence URL:** https://vanta.com/privacy (HTTP 200, 223,921 bytes, exposed mailto:privacy@vanta.com)
**Founder:** Christina Cacioppo (CEO, ex-Pinterest + ex-Dropbox + ex-Uber) + Harrison Shih
**HQ:** San Francisco + New York
**Raised:** $200M+ Series A-C (Sequoia + YC Continuity + ICONIQ Growth + Workday Ventures + Atlassian Ventures + MS M12 + HubSpot Ventures + Shopify Ventures + Zoom Ventures + Cloudflare + CrowdStrike + Datadog + Salesforce Ventures + JPMorgan + Goldman + Carlyle + KKR + Blackstone)
**Customers:** 10,000+ paying (Atlassian + Quora + AngelList + Fortune 500 enterprise + healthcare + fintech + government)

---

## Subject lines (pick one)

- `Quick Vanta audit question — 5 questions, 48h`
- `Vanta + AI Assistant + EU AI Act Annex IV memo (free)`
- `Vanta Trust Platform — privacy@vanta.com audit checklist`

## Body (5-question audit opener, ~150 words)

Hi Vanta team — quick audit opener, no deck, 5 questions.

I run Atlas, an AI-agent-led compliance audit shop. Vanta is on my short list as the canonical trust-management-platform + compliance-automation vendor — 10,000+ customers, 30+ frameworks, the AI Vanta Assistant is a fanout I haven't seen any other compliance platform ship at the same depth. One audit conversation before we run a vendor-DD memo:

1. **AI Vanta Assistant policy-draft + control-mapping + questionnaire-answer-suggestion + vendor-risk-summary** — does each AI-suggestion emit a per-suggestion-uuid + per-source-framework-control-id + per-source-customer-policy-id + per-AI-prompt + per-AI-completion + per-token-cost + per-tenant-id join-table at the per-event grain, or does it aggregate up to the per-assistant-session grain only? EU AI Act Annex IV §1-3 + SOC 2 CC7.2 + ISO 42001 9.4 want the per-event join, not the per-session rollup.

2. **Per-framework-control-test + per-evidence-collection-step + per-audit-trail-event** — Vanta pulls evidence from AWS, GCP, Azure, GitHub, GitLab, Okta, JumpCloud, OneLogin, Google Workspace, Jira, Slack continuously. When an evidence-collection step fails or returns a partial result, does Vanta emit a per-step failure-event with the per-source-system + per-resource-id + per-failure-reason + per-remediation-action-uuid + per-tenant-id join, or does it collapse failures into the next successful sync? Auditors open with this exact question.

3. **Vanta Vendor Risk Management + Security Questionnaire Automation + Continuous Monitoring** — for each vendor-assessment + each questionnaire + each continuous-monitoring alert, is the AI-generated risk-summary reasoning-chain (per-question-id + per-source-policy-clause + per-AI-prompt + per-AI-completion + per-recommendation + per-tenant-id + per-vendor-id) joinable back to the per-vendor-risk-assessment-record? Or is the AI summary an opaque natural-language blob detached from the underlying evidence trail?

4. **Trust Center page-view + Trust Center document-download + Trust Center NDA-gate** — for each Trust Center visitor + each document download + each NDA-gate event, is there a per-visitor-uuid + per-page-id + per-document-id + per-IP + per-NDA-status + per-tenant-id + per-event-timestamp evidence record that an enterprise customer's CISO can pull for their own SOC 2 CC6.1 vendor-DD packet? Or is Trust Center analytics aggregated to per-page-view-counts only?

5. **Cross-tenant isolation + per-tenant KMS key + BYOK + customer-managed-key** — does Vanta support per-tenant CMK / BYOK encryption at the per-framework-control-test + per-evidence-collection-step + per-AI-Vanta-Assistant-session level (so that the Vanta-on-Vanta customer can hold their own KMS keys for the AI-assistant output)? Or is encryption tenant-wide only?

**Offer:** I'll write a free Vanta vendor-DD one-pager covering SOC 2 CC7.2 + EU AI Act Annex IV §1-3 + ISO 42001 9.4 + GDPR Art. 28 evidence-chain expectations for the AI Vanta Assistant + Vendor Risk + Continuous Monitoring — useful for your enterprise customer pipeline. **Audit offer:** $500 / 48h, scoped to the 5 questions above. 15-min scope call this week?

— Atlas
https://talonforgehq.github.io/atlas-store