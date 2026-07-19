# Sunsama — Guided Daily Planner Cohort Sibling #3 (Lead 569)

**Subject:** Quick ask — Sunsama cross-app planning audit

Hi Ashutosh & Travis,

Sunsama is the guided-planning sibling in our `ai_work_management` cohort. Your task-manager + calendar layer pulls work from Asana, ClickUp, GitHub, Linear, Monday, Jira, Trello, Todoist, Notion, Gmail, Outlook, Slack, and Teams, then turns it into timeboxed daily plans. That cross-app write surface is exactly where a small evidence gap can become a wrong task, calendar block, or completion state in several systems.

We do fixed-fee evidence-gap maps: $500 / 48h for the first reconstruction, or $497/mo for quarterly refresh.

For Sunsama, I'd map:

- source-task-to-daily-plan-to-timebox-to-calendar-sync provenance
- deletion + completion propagation across task, email, messaging, and calendar connectors
- untrusted task-title/email/Slack-content injection before auto-scheduling
- workspace + OAuth token + per-connector permission isolation
- immutable evidence for human edits, deferrals, and shutdown decisions
- per-task + per-sync + per-calendar-block API cost attribution

Worth a 15-min call this week? Otherwise I'll assume the timing is bad and try again in Q4.

— Atlas
Talon Forge LLC · talonforge.dev

---

**Verified live 2026-07-19:**
- https://www.sunsama.com/ → HTTP 200; first-party schema lists timeboxing + auto-scheduling, Google/Outlook calendar sync, and Asana/ClickUp/GitHub/Linear/Monday/Jira/Trello/Todoist/Notion/Gmail/Outlook/Slack/Teams integrations
- https://www.sunsama.com/privacy → HTTP 200; privacy@sunsama.com + security@sunsama.com; SOC 2 Type 2 processes, AES-256 at rest, TLS 1.2+, GDPR/CCPA/CPRA
- https://www.sunsama.com/about → HTTP 200; names Ashutosh & Travis as Sunsama's cofounders
- https://www.ycombinator.com/companies/sunsama → HTTP 200; YC W19; Active Founders Travis Meyer + Ashutosh Priyadarshy
- Cohort siblings: Motion 567 + Akiflow 568
