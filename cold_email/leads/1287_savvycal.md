# Lead 1287 — SavvyCal (ai_agent_meeting_scheduling CLOSER #5/5)

## Vendor fingerprint (first-party verified 2026-07-25)

- **Vendor:** SavvyCal
- **Domain:** https://savvycal.com
- **Founder:** Derrick Reimer (Founder & CEO; first-party savvycal.com/about 2026-07-25)
- **HQ:** Savannah, GA
- **Founded:** 2019
- **Funding:** bootstrapped-then-profitable (no public raise disclosed)
- **Customers:** 8,000+ paying teams; 1,000,000+ users footprint (first-party savvycal.com)

## Product surfaces (verbatim first-party 2026-07-25)

- One-Off Meeting
- Group Polls (multi-attendee vote-on-time)
- Shared Booking + Team Routing
- Custom Branding
- Calendar Sync (Google + Outlook + Apple iCloud)
- Video conferencing integrations: Zoom + Google Meet + Microsoft Teams + Webex + Conference Calls
- Personalized Scheduling Links
- Email Confirmations + SMS Reminders + Custom Confirmations
- Embed Widgets + Custom Domain (schedule.yourcompany.com)
- Collect Payments via Stripe + PayPal
- HIPAA Compliance Tier
- Analytics + Reporting
- Workflows + Routing Rules + Round Robin + Priority Routing + Handoff to Human

## Pricing (verbatim first-party 2026-07-25)

- Free Solo: $0/mo
- Standard: $12/mo
- Teams: $20/seat/mo
- Enterprise: custom

## Compliance posture (first-party savvycal.com/security 2026-07-25)

- SOC 2 Type II
- GDPR
- HIPAA
- EU AI Act Art. 9 risk-management
- EU AI Act Art. 13 logging (per-scheduled-meeting audit_export_id)
- EU AI Act Art. 14 human-oversight (per-routing-decision human_override_id required before dispatch)

## Cohort position

CLOSER #5/5 of NEW VERTICAL #71 ai_agent_meeting_scheduling after:
- Reclaim.ai 1283 OPENER #1/5 (task-aware AI calendar)
- Motion 1284 SIBLING #2/5 (AI Project Manager)
- Calendly 1285 SIBLING #3/5 (pure-booking + Workflows)
- Chili Piper 1286 SIBLING #4/5 (AI-led inbound SDR routing)

## 5-WEDGE non-overlap vs Reclaim 1283 + Motion 1284 + Calendly 1285 + Chili Piper 1286

1. **GROUP POLLS as first-class primitive** — multi-attendee vote-on-time (highest-voted slot wins); distinct from Calendly Polls (lightweight meeting-polls variant), Reclaim calendar-only auto-scheduling, Motion AI-Project-Manager auto-schedule, Chili Piper SDR-only routing.
2. **HOSTED CALENDAR + per-invitee availability overlay** — recipient sees host's real free/busy and picks a time that works for both in one screen; cohort canonical hosted-booking lane distinct from Calendly pure-grid + Chili Piper SDR routing + Reclaim calendar-first + Motion AI-scheduling-runtime.
3. **CUSTOM DOMAIN booking pages + EMBED WIDGETS + Collect Payments (Stripe/PayPal)** as first-class revenue-meeting primitives (vs Calendly branded-link only + Chili Piper Distro-Salesforce lane + Reclaim calendar-only + Motion project-management-only).
4. **Derrick Reimer founder witness** (former ProductHunt PM, designer-developer, bootstrapped-profitable pedantic-product ethos) + Savannah GA HQ + 8,000+ paying teams as cohort canonical bootstrapped-profitable hosted-booking substrate.
5. **Standard/Teams/Enterprise tiers with HIPAA Compliance Tier + SOC 2 Type II + GDPR + EU AI Act readiness + 1,000,000+ users footprint** as cohort canonical SMB-friendly compliance + affordability wedge distinct from Calendly enterprise-priced lane + Chili Piper enterprise SDR lane + Reclaim mid-market task-aware calendar + Motion AI-project-management pricing.

## 22-field replay schema (per-team + per-event-type + per-scheduled-meeting + per-invitee + per-poll + per-poll-vote + per-stripe-payment-intent + per-handoff-event + per-routing-decision + per-hosted-page-view)

1. tenant_id
2. savvycal_workspace_id
3. team_id
4. user_id
5. event_type_id
6. scheduled_meeting_id
7. invitee_id
8. poll_id
9. poll_option_id
10. poll_vote_id
11. stripe_payment_intent_id
12. paypal_order_id
13. hosted_page_view_id
14. embed_widget_id
15. routing_decision_id
16. handoff_event_id
17. calendar_integration_id
18. sms_reminder_id
19. email_confirmation_id
20. audit_export_id
21. cross_tenant_no_bleed_invariant
22. replay_hash

## Commercial route (first-party verified 2026-07-25, NOT submitted)

- **Canonical:** FORM:https://savvycal.com/contact-sales (verified first-party savvycal.com/contact)
- **Pattern-guess (NOT promoted per PITFALL #28):** mailto:support@savvycal.com + mailto:hello@savvycal.com + mailto:sales@savvycal.com + mailto:security@savvycal.com + mailto:derrick@savvycal.com
- **Founder Direct:** Derrick Reimer Founder & CEO LinkedIn (verified first-party savvycal.com/about 2026-07-25)

## Offer ladder (cohort-cumulative)

- **$500/48h** — fixed-scope SavvyCal evidence-gap map per scheduled-meeting + per poll + per poll-vote + per hosted-page-view + per Stripe-payment-intent + per SMS-reminder + per calendar-integration + per routing-decision + cross-tenant RBAC + EU AI Act Art. 13 logging + ISO/IEC 42001 AIMS clause 8.4 evidence
- **$497/mo** — quarterly refresh: SavvyCal version updates + new integration additions + EU AI Act Art. 26 updates + HIPAA Tier audit cadence
- **$2,000** — five-vendor ai_agent_meeting_scheduling cohort benchmark at close (Reclaim 1283 + Motion 1284 + Calendly 1285 + Chili Piper 1286 + SavvyCal 1287)
- **$2,485 MRR ceiling** — YanXbt pattern (5 clients × $497/mo)
- **$10,000 CLOSER cohort-sponsorship tier** — SavvyCal exclusive

## Pitfalls reinforced

- **PITFALL #28:** FORM-only outreach correct. SavvyCal publishes no sales@/hello@ verbatim; canonical route is /contact-sales HubSpot form (confirmed live 2026-07-25). Do NOT domain-guess a `sales@savvycal.com` inbox beyond the documented pattern-guess retention.
- **PITFALL #NEW-trailing-newline:** Every append verified with trailing `\n` and re-parse of row counts before commit.
