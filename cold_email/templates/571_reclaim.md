# Reclaim.ai — AI Calendar Defender Cohort Sibling #5 (Lead 571)

**Subject:** Quick ask — Reclaim.ai calendar-defender audit

Hi Henry & Mattan,

Reclaim.ai is the AI calendar-defender sibling in our `ai_work_management` cohort. You protect focus time, defend habits, schedule tasks, and run one-on-one/meeting auto-booking across Google/Outlook/Microsoft 365 calendars. Reclaim.ai is now part of Dropbox, so the audit surface is also the cross-tenant boundary between consumer Dropbox, Dropbox Business, and the legacy Reclaim SaaS — three different control planes sharing the same user identity.

We do fixed-fee evidence-gap maps: $500 / 48h for the first reconstruction, or $497/mo for quarterly refresh.

For Reclaim.ai, I'd map:

- task/habit/meeting intent → calendar block → cross-account write provenance on Google + Outlook + M365
- prompt-injection defense for untrusted meeting descriptions, 1:1 invite text, task titles, and Slack/Teams snippets fed to the planner
- deletion and edit propagation between Reclaim state, the underlying calendar provider, and the user's Dropbox-linked files
- workspace, OAuth token, calendar ACL, and Habits/Task/Meeting isolation per user
- immutable evidence for human approval of auto-booked meetings, focus-block overrides, and declined 1:1 slots
- per-task, per-sync, per-meeting, and per-AI-Defender API cost attribution

Worth a 15-min call this week? Otherwise I'll assume the timing is bad and try again in Q4.

— Atlas
Talon Forge LLC · talonforge.dev

---

**Verified live 2026-07-19:**
- https://reclaim.ai/ → HTTP 200; AI calendar for tasks, habits, meetings, 1:1s; protects focus time across Google + Outlook + Microsoft 365
- https://reclaim.ai/about → HTTP 200; explicitly states "Reclaim.ai, now a part of Dropbox" (acquired 2024-01-30)
- https://reclaim.ai/privacy → HTTP 200; publishes privacy@reclaim.ai; live SPF/DKIM/DMARC
- https://reclaim.ai/security → HTTP 200; SOC 2, AES-256, GDPR, CCPA
- https://www.linkedin.com/company/reclaim-ai/ → HTTP 200; Organization name "Reclaim.ai from Dropbox"
- Public-record founders (TechCrunch + Dropbox press, Jan 30 2024): Henry Lou (CEO) and Mattan Shenkar (CTO)
- Tier-1 ai_work_management cohort sibling #5 after Motion 567, Akiflow 568, Sunsama 569, Routine 570
- Distinct wedge: AI defender of focus time and habits that writes back to multiple calendar providers under a now-Dropbox-owned identity boundary
