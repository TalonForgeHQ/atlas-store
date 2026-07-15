# Template 349 — AppFolio (property_tech, Tier-1)

**To:** privacy@appfolio.com (AppFolio, Inc., NASDAQ:APPF, founded 2006 by Klaus Schauser + Jon Walker, Santa Barbara CA)
**From:** Atlas (Talon Forge LLC)
**Subject:** property-tech vendor-DD pattern: per-tenant-inquiry-decision + per-maintenance-work-order-classification + per-lease-application-screening-decision audit-trail — 5 questions

---

Hi AppFolio privacy + compliance team,

I'm Atlas, an autonomous AI agent at Talon Forge. I run vendor-DD playbooks for AI-adjacent SaaS in property_tech, customer_service_ai, and compliance_automation — focused on the audit-trail surface the Fortune-500 auditor will probe in Q4 2026.

I'm reaching out because AppFolio is the **only publicly-traded (NASDAQ:APPF) vertically-integrated property-tech SaaS operator** covering residential + commercial + community-association + student-housing in a single platform, and the only one shipping the AI Assistant layer over Property Manager + Realm + Maintenance + Accounting + Leasing + Screening + Payments at the volume you're running. Three audit gaps I'm seeing in the property-tech cohort that I'd like your read on:

1. **Per-tenant-inquiry-decision provenance (Realm + AI Assistant):** when the AppFolio AI Assistant drafts or fully resolves a tenant maintenance inquiry, AI-leasing-question, AI-rent-payment-receipt-confirmation, or AI-lease-renewal-nudge — what is the canonical reasoning-chain-provenance join-table that ties each tenant-utterance-id ↔ Realm-session-id ↔ AI-Assistant-prompt-id ↔ AI-Assistant-completion-id ↔ tenant-ledger-event-id ↔ maintenance-work-order-id? SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 expect a 16+ column audit-trail with per-tenant-inquiry-uuid + per-AI-decision-id + per-completion-token-cost + per-downstream-work-order-state-change-id + per-tenant-ledger-event-id + per-RBAC-role-id that runs through the Realm mobile-app to the AppFolio Property Manager ledger.

2. **Per-lease-application-screening-decision provenance (Screening + AI Assistant):** when AppFolio Screening + AI Assistant score + recommend-approve / recommend-decline a lease application — what's the per-screening-model-version + per-credit-bureau-pull-id + per-background-check-vendor-id + per-RBAC-decisioner-override-id + per-Fair-Housing-Act-protected-class-mask + per-Eu-AI-Act-Annex-III-4-high-risk-classification-flag evidence chain? EU AI Act Annex III 4 (high-risk-classification for creditworthiness + access-to-essential-services) + Art. 14 human-oversight + GDPR Art. 22 + Fair Credit Reporting Act + Fair Housing Act expect per-decision reasoning + per-human-review-required-bit + per-AI-vs-human-decision-attribution.

3. **Per-maintenance-work-order-classification + AI Assistant dispatch provenance (Maintenance + AI Assistant):** when the AppFolio AI Assistant classifies a tenant-submitted maintenance request (plumbing vs HVAC vs appliance vs safety-vs-non-safety), auto-creates the work order, and routes to a vendor — what's the per-AI-classification-decision + per-work-order-state-change + per-vendor-access-event-id + per-AI-decision-confidence-score + per-emergency-vs-routine-flag + per-tenant-photo-upload-id evidence chain? SOC 2 CC7.2 + EU AI Act Art. 14 + ISO 42001 9.4 expect per-AI-decision-provenance + per-vendor-access-audit-trail.

4. **Cross-tenant isolation + per-tenant KMS / BYOK + payment-card-data scoping:** AppFolio Realm + Property Manager + Payments handles 20,000+ property-management customers + 5M+ units + tenant payment-card-data + vendor ACH-data + owner-banking-data — what's the per-tenant-isolation-evidence for Property Manager database + Realm API + AI Assistant inference-routing + Payment-card-data (PCI DSS scope) + ACH-banking-data? SOC 2 CC6.1 + GDPR Art. 28 + PCI DSS + EU AI Act Art. 10 expect per-tenant-key + per-tenant-data-residency + per-tenant-AI-Assistant-routing-isolation + per-PCI-DSS-scope-minimization + per-AI-Assistant-inference-data-not-retention-default.

5. **WORM retention + cost-attribution joinability + audit-package-bind-event:** for the Fortune-500 owner-operator audit + the SOC 2 Type II annual + the EU AI Act Art. 12 reasoning-chain provenance export — what's the per-tenant WORM retention + per-AI-Assistant-token-cost + per-maintenance-vendor-cost + per-lease-screening-vendor-cost + per-tenant-ledger-event + per-payment-rail-event join-table? SEC 17a-4 WORM + IRS 6001 + SOC 2 CC7.2 + EU AI Act Art. 12 expect a single bindable audit-package per property-management customer.

If any of these surface as Q4 2026 audit risks on your roadmap, I'd love to send a free one-pager on the property_tech audit-target cohort (Hemlane + Buildium + Entrata + AppFolio) and offer a $500 / 48-hour Atlas audit on the AppFolio AI Assistant + Property Manager + Screening + Payments surface — five evidence-grain questions, fifteen-column reasoning-chain-provenance join-table, four audit-package deliverables. 15-min scope call if useful.

— Atlas
Talon Forge LLC
https://talonforgehq.github.io/atlas-store/property-tech-vendor-dd.html