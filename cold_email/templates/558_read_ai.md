# Read AI — Focused Outreach Template (Lead 558, meeting_ai_ops cohort sibling #2)

**To:** privacy@read.ai (verified live 2026-07-19 via https://www.read.ai/privacy HTTP 200)
**Subject line:** Meeting-summary → coaching → CRM-sync — 5 evidence gaps your SOC 2 + EU AI Act auditor will ask about before Aug 2

---

Hi Read AI team,

Read AI's meeting-summary + speaker-talk-time + sentiment + coaching + cross-meeting-analytics triad is the canonical meeting_ai_ops wedge for Fortune 500 + growth-stage enterprise. With David Shim (ex-Foursquare CEO + Placed founder sold to Snapchat 2017) + Robert Williams + Elliott Waldron (all ex-Foursquare + Placed engineering/data-science) and the Madrona + Goodwater backing, the platform has the pedigree to win the enterprise meeting-intelligence lane.

Before your next SOC 2 Type II refresh and the EU AI Act Aug 2 2026 GPAI enforcement window, five evidence gaps are worth a 48-hour audit:

1. **End-to-end per-meeting-id → per-recording-id → per-transcript-id → per-speaker-attribution-id → per-engagement-score-id → per-coaching-recommendation-id → per-recap-delivery-id → per-crm-sync-event-id reconstruction drill (50+ cols).** Auditors will walk this end-to-end and ask: which prompt-template-version produced this coaching-recommendation? which LLM call? which knowledge-base-document? which action-item-id in the CRM sync?

2. **Prompt-injection + meeting-recording-poisoning + transcript-poisoning + AI-summary-poisoning + speaker-attribution-poisoning + engagement-score-poisoning + coaching-recommendation-poisoning + recap-delivery-poisoning + crm-sync-poisoning defense lineage (OWASP LLM Top 10 LLM01+LLM03+LLM06+LLM08 + MITRE ATLAS).** A poisoned coaching-recommendation could route an enterprise sales-rep to mis-prioritize a Fortune 500 deal; a poisoned recap-delivery could exfiltrate customer commitments to a malicious email-recipient.

3. **Cross-tenant + cross-customer + cross-account + cross-meeting + cross-recording + cross-transcript + cross-ai-summary + cross-ai-coaching + cross-engagement-score tenant isolation evidence (SOC 2 CC6.1 + GDPR Art. 28 + CCPA/CPRA + ISO 27001 A.8.22 + ISO 27701) with CMK/BYOK + per-tenant-KMS-key-id + per-cross-border-transfer-SCCs-version-US-EU + per-account-tenant-isolation.** Critical for the Fortune 500 enterprise customer-cohort where meeting-summary-leakage between tenants is a board-level risk.

4. **Per-prompt-injection-detection-signal-id + per-meeting-consent-event-id + per-recording-consent-event-id + per-speaker-consent-event-id + per-deletion-propagation-event-id coverage across meeting-recording + transcript + AI-summary + coaching + recap-delivery + CRM-sync.** The EU AI Act Art. 14 human-oversight + Art. 50 transparency-obligation + Schrems II SCC cross-border-transfer controls all hit the same deletion-propagation event log.

5. **WORM retention + cost-attribution join-table linking per-meeting-cost + per-recording-cost + per-transcript-cost + per-engagement-score-cost + per-coaching-recommendation-cost + per-recap-delivery-cost + per-crm-sync-cost + per-LLM-token-cost + per-multi-model-fallback-cost + per-tenant-cost + per-procurement-vendor-DD-event-cost (SOC 2 CC7.2 + EU AI Act Art. 12 + SEC 17a-4 WORM + Schrems-II-recordkeeping + HIPAA-6-year-recordkeeping + GDPR-Art-30-recordkeeping + SOX-404-recordkeeping + cross-border-data-residency-retention).** Fortune 500 customers will want the per-meeting-cost roll-up evidence for their own AI cost-allocation audit.

We offer a **$500 / 48-hour evidence-gap map** with a **$497/mo quarterly refresh** — both fixed-price and scoped to the meeting_ai_ops audit surface. The deliverable is a 5-section gap map keyed to the 5 audit gaps above, with the join-table templates, the OWASP/MITRE ATLAS defense lineage templates, the cross-tenant isolation test plan, the consent/deletion-propagation event-log schema, and the WORM/cost-attribution join-table SQL you can hand to your SOC 2 + EU AI Act auditor.

If useful, I can send the gap-map outline + the per-meeting-id join-table schema as a starter. Either way, the EU AI Act Aug 2 2026 GPAI enforcement window is the natural deadline to close these.

— Atlas
Talon Forge LLC
atlas@talonforge.io

---

**Why Read AI specifically:**
- meeting_ai_ops cohort sibling #2 (after Granola 557) — opens the meeting-summary + coaching lane
- David Shim CEO-pedigree (ex-Foursquare + Placed/Snapchat) signals enterprise-readiness
- Madrona + Goodwater backing signals enterprise go-to-market
- Fortune 500 customer-cohort = enterprise-procurement-vendor-DD strategic-inbound channel
- privacy@read.ai verified live (curl HTTP 200) 2026-07-19

**Audit-offer:**
- $500 / 48-hour evidence-gap map (fixed-price, scoped to meeting_ai_ops audit surface)
- $497/mo quarterly refresh (recurring revenue)
- 5 audit-gap sections keyed to SOC 2 + EU AI Act + OWASP LLM Top 10 + MITRE ATLAS
- WORM + cost-attribution join-table templates included in deliverable
