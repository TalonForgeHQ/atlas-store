---
name: atlas-store-tick-learnings-2026-07-25-savvycal-1287
description: Session addendum to atlas-store-cron-recipe for tick 2026-07-25-savvycal-1287 — ai_agent_meeting_scheduling CLOSER #5/5 (COHORT CLOSED 5/5)
---

# atlas-store tick 1287 — SavvyCal (ai_agent_meeting_scheduling CLOSER #5/5)

## Tick summary

Shipped CLOSER #5/5 — SavvyCal — closing NEW VERTICAL #71 ai_agent_meeting_scheduling at 5/5. **Cohort complete.**

| Item | Path | Status |
|---|---|---|
| Lead 1287 row | `cold_email/leads.csv` (62 rows) | ✓ |
| Companion evidence | `cold_email/leads/1287_savvycal.md` | ✓ |
| Leads-with-emails row | `cold_email/leads_with_emails.csv` (584 rows, 13 cols) | ✓ |
| 3-variant template | `cold_email/templates/1287_savvycal_ai_agent_meeting_scheduling_closer_5_of_5.md` | ✓ |
| SEO chunk | `chunks/chunk_1287.html` (~10.2KB) | ✓ |
| Sitemap entry | `sitemap.xml` (canonical 2/4-space indent) | ✓ |
| Index card | `index.html` (#chunk-1287, data-vendor=SavvyCal) | ✓ |
| Build-log entry | `build-log.html` (tick-1287 prepended) | ✓ |
| Revenue log row | `cold_email/revenue_log.csv` (40 rows) | ✓ |
| Send log entry | `cold_email/send_log.jsonl` (44 lines) | ✓ |
| Git commit + push | (pending) | in progress |

## Cohort progress

ai_agent_meeting_scheduling cohort (NEW VERTICAL #71) — **CLOSED 5/5**:
- Reclaim.ai 1283 OPENER #1/5 (task-aware AI calendar + Henry Shapiro + Patrick Lightbody)
- Motion 1284 SIBLING #2/5 (AI Project Manager + AI Docs + AI Workflows)
- Calendly 1285 SIBLING #3/5 (pure-booking + Workflows + Routing Forms + Round Robin + 100+ integrations)
- Chili Piper 1286 SIBLING #4/5 (AI-led inbound SDR routing + Chili Assist + MCP & Programmatic Scheduling)
- **SavvyCal 1287 CLOSER #5/5** (hosted-booking + Group Polls + Custom Domain + Embed Widgets + Stripe/PayPal + HIPAA Tier) ← this tick

## Wedge that worked (replicate for next cohort CLOSER)

SavvyCal is the only cohort member that ships all 5 of:
1. **Hosted Calendar + per-invitee availability overlay** (recipient sees host's real free/busy and picks in one screen)
2. **Group Polls** (multi-attendee vote-on-time, highest-voted slot wins automatically) as first-class primitive
3. **Custom Domain** booking pages (schedule.yourcompany.com — full custom domain, not branded-link redirect)
4. **Embed Widgets + Collect Payments via Stripe/PayPal** as first-class revenue-meeting primitives
5. **HIPAA Compliance Tier + SOC 2 Type II + GDPR + EU AI Act Art. 13** at Standard $12/mo (SMB-friendly affordability)

Plus bootstrapped-profitable + designer-developer founder (Derrick Reimer, former ProductHunt PM) + 8,000+ paying teams + 1M+ users footprint + Standard pricing below Calendly Standard × 5 seats.

## 22-field audit-letter wedge (SavvyCal-specific)

Per-scheduled-meeting + per-poll + per-poll-vote + per-hosted-page-view + per-Stripe-payment-intent + per-SMS-reminder + per-routing-decision replay receipt:
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

Pinning Group Polls + Custom Domain + Stripe/PayPal primitives + HIPAA Tier as first-class surfaces is the procurement wedge Reclaim 1283 + Motion 1284 + Calendly 1285 + Chili Piper 1286 do not ship verbatim together.

## Pitfalls reinforced

- **PITFALL #28:** FORM-only outreach correct. SavvyCal publishes no sales@/hello@ verbatim first-party inbox; canonical route is /contact-sales HubSpot form (confirmed live 2026-07-25). Do NOT promote `support@savvycal.com` or `hello@savvycal.com` or `sales@savvycal.com` or `derrick@savvycal.com` to verified status — all retained separately as unverified pattern guesses.
- **PITFALL #NEW-trailing-newline:** All 4 CSV/JSONL files appended with explicit trailing `\n` verification before commit. leads.csv now 62 rows, leads_with_emails.csv now 584 rows, revenue_log.csv now 40 rows, send_log.jsonl now 44 lines — all re-parsed cleanly.

## Next-tick spec

Vertical #71 is CLOSED. Cron must OPEN Vertical #72. Candidates per PITFALL #99 cohort-rotation ladder:
- ai_agent_call_center_voice (Sierra 854 + Decagon 851 + Ada 855 + Cognigy 659 + Vapi 661 — partial cohort exists)
- ai_agent_email_security (Abnormal 776 + Mimecast 779 + IRONSCALES 778 + Tessian + Egress)
- ai_agent_observability (Datadog 891 + Splunk 933 + Grafana 934 + Dynatrace 910 + Honeycomb 842/926)
- Fresh vertical TBD
