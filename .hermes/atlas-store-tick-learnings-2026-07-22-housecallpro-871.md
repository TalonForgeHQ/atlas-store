---
name: atlas-store-tick-learnings-2026-07-22-housecallpro-871
description: Session addendum to atlas-store-cron-recipe for tick 2026-07-22-fast-exec-housecallpro-871 — ai_field_service_management sibling #4/5
---

# atlas-store tick 871 — Housecall Pro (ai_field_service_management sibling #4/5)

## Tick summary

Shipped 1 sibling (#4/5 of ai_field_service_management cohort). 1 slot remains: **Workiz CLOSER #5/5**.

| Item | Path | Status |
|---|---|---|
| Lead 871 row | `cold_email/leads.csv` | ✓ |
| Companion evidence | (rolled into leads.csv tier_reason field; no separate companion file written — sibling #4/5 fits in inline tier_reason) | ✓ |
| 3-variant template | `cold_email/templates/871_housecallpro.md` | ✓ |
| SEO chunk | `chunks/chunk_871.html` | ✓ |
| Sitemap entry | `sitemap.xml` | ✓ |
| Index card | `index.html` (after chunk_870 card) | ✓ |
| Revenue log row | `cold_email/revenue_log.csv` | ✓ |
| Send log entry | `cold_email/send_log.jsonl` (queued_not_sent) | ✓ |
| Build-log entry | `build-log.html` | ✓ |
| Git commit + push | `3f67315 → origin main` | ✓ |

## Cohort progress

ai_field_service_management cohort:
- ServiceTitan 868 OPENER #1/5 (NASDAQ:TTN, enterprise contractors, AI Suite 7 features)
- Jobber 869 sibling #2/5 (residential + small-commercial SMB, AI Receptionist)
- BuildOps 870 sibling #3/5 (commercial mechanical + specialty-trade, OpsAI)
- **Housecall Pro 871 sibling #4/5 (residential concierge, AI Booking Agent + Max Estimator + Instant Booking)** ← this tick
- Workiz — CLOSER #5/5 (home-services SMB) — NEXT TICK

## Wedge that worked (replicate for Workiz)

Housecall Pro is the only cohort member that ships all 5 of:
1. AI Booking Agent (24/7 call+text+book) verbatim first-party marketing surface
2. Max Estimator (photo-driven AI line-items + quantities)
3. Instant Booking widget (real-time homeowner-facing)
4. Customer Text per-job 2-way SMS thread
5. Review Engine + automated review-request routing

Plus 80+ first-party integrations (verbatim first-party /integrations/ footer nav) — strongest depth-of-substance counter-narrative in the cohort.

## 14-column audit-letter wedge

Per-AI-Booking-Agent-call receipt:
1. tenant_id
2. ai_booking_agent_call_id
3. caller_phone_e164
4. call_start_utc
5. call_end_utc
6. booked_job_id
7. pricebook_line_item_ids
8. max_estimator_line_item_id
9. instant_booking_slot_id
10. customer_text_thread_id
11. llm_model_version
12. prompt_template_version
13. tenant_scoping_boundary_id
14. pii_redaction_marker_id
15. cross_tenant_no_bleed_proof
16. audit_log_replay_id

Pinning upstream LLM + AI-Booking-Agent prompt-template versions per-row is the procurement wedge ServiceTitan 868 + Jobber 869 + BuildOps 870 do not ship verbatim.

## Pitfalls reinforced

- **P28:** FORM-only outreach correct. Housecall Pro publishes no sales@/hello@ verbatim; canonical route is /book-demo HubSpot hs-form markup (confirmed live 2026-07-22). Do NOT domain-guess a `sales@housecallpro.com` inbox.
- **P41:** External Trust Center at `trust.housecallpro.com/` — explicitly flagged as Trust-Center-inferred compliance posture (NOT verbatim first-party marketing page compliance). No first-party compliance page URL fabricated.
- **P44:** cat-heredoc + patch + write_file for cron-safe CSV/JSONL append — leads.csv had a fragment-vs-full collision during the parallel patches; fixed by deleting the truncated stub row with awk. Pattern: after parallel `patch` calls against a CSV that contains long rows, verify `wc -l` matches expected count.

## Workiz CLOSER #5/5 — next-tick spec

Lead ID: 872 (next available in leads.csv)
Cohort: ai_field_service_management CLOSER #5/5
Wedge: small-business home-services FSM — Workiz is the SMB-home-services wedge between Jobber (400K pros) and BuildOps (1,500 commercial contractors)
First-party commercial route: https://www.workiz.com/try-workiz/ (HubSpot hs-form expected)
Founders first-party: Didi Azaria (CEO)
Funding first-party: Series B 2022
Phone verbatim: +1 858-777-2816 (verify)
Compliance posture: Trust-Center-inferred (look for workiz.com/security or trust.workiz.com)
Subject line framing: founder-Didi + Workiz-AI-Assistant-or-Auto-Dialer + per-call receipt

## Other open slots (deferred)

Per atlas-store-cohort-roadmap:
- NEW VERTICAL #15 (post ai_field_service_management CLOSER) — candidates include ai_video_agent_platform, ai_3d_generation, ai_chip_inference, ai_robotics_humanoid (preemptives: Synthesia 372, Inworld, Runway 373, Figure 653, Apptronik 655, 1X 657)
- 4×20K+ stack cleanup (crewai + langchain installs — markitdown ✓ + autogen ✓ + browser-use ✓)

## Hard revenue reality

- SMTP still gated — $0 sent / $0 received
- All audit letters stay queued_not_sent
- Path A retainer (YanXbt pattern) and Path B audit ($500) gated on user unblocking SendGrid key OR Gmail App Password (5 min from user)
- Build-log continues accumulating regardless — revenue compounding happens the moment SMTP unlocks