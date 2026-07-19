# Asana — Work-Graph AI Cohort Sibling #10 (Lead 576)

**Subject:** Quick ask — Asana AI work-graph evidence map

Hi Dustin and Justin,

Asana is the work-graph sibling in our `ai_work_management` cohort. Asana AI Studio, Smart Goals, Workflow Studio, AI chat, AI fields, AI summaries, AI stand-ups, AI project health, and connected agents all read and write the same task-project-goal-portfolio-rule-form surface, plus connected Slack, Google Workspace, Microsoft 365, Jira, GitHub, and Salesforce state. That graph-connectedness is the product advantage — but it makes one Asana AI action harder to reconstruct when a retrieved chunk becomes a task mutation, a project property write, a goal update, a rule firing, a form response, or a write into a connected system.

We build fixed-fee evidence-gap maps: $500 / 48h for the first reconstruction, or $497/mo for quarterly refresh.

For Asana, I'd map:

- source task / project / goal / portfolio / rule / form / Slack thread / Google doc / Jira ticket / GitHub issue → retrieved chunk → prompt / model / version → Asana AI plan → tool call → task / project / goal / portfolio / rule / form mutation → connected write
- prompt-injection defense for untrusted task bodies, project descriptions, goal names, form responses, file attachments, Slack/Teams messages, email bodies, and connected Google/Microsoft/Jira/GitHub/Salesforce content
- workspace, team, project, portfolio, goal, rule, form, guest, connector, and data-residency isolation for AI Studio, Smart Goals, Workflow Studio, AI chat, AI fields, AI summaries, and connected agents
- deletion, retention, rollback, version-history, and connection-sync propagation after an Asana AI action mutates a task, project, goal, or rule
- immutable human-approval evidence for AI-resolved tasks, AI-generated comments, AI stand-up summaries, AI project-health scores, automated rules, exports, and external API/connector writes
- per-agent, per-model, per-tool-call, per-workspace, and per-connection cost attribution across Asana AI Studio, Smart Goals, Workflow Studio, AI chat, AI fields, AI summaries, Asana API, and Slack/Google/Microsoft/Jira/GitHub/Salesforce bridges

Asana's security posture is strong on controls — SOC 2 Type II, SOC 3, ISO/IEC 27001:2022, ISO/IEC 27017, ISO/IEC 27018, ISO/IEC 27701, GDPR, CCPA, HIPAA BAA, AES-256 at rest, TLS 1.2+, SAML SSO, SCIM, audit logs, and EU/US/APAC regional data residency. The missing layer I'd test is whether those controls can reconstruct one Asana AI action end to end under EU AI Act Articles 12/14, SOC 2 CC7.2, ISO 42001, and the new Asana AI Studio + connected-agent surface.

Worth a 15-minute call this week? Otherwise I'll assume the timing is bad and try again in Q4.

— Atlas
Talon Forge LLC · talonforge.dev

---

**Verified live 2026-07-19:**
- https://asana.com/product/ai → HTTP 200; first-party product surface for Asana AI Studio, Smart Goals, Workflow Studio, AI chat, AI fields, AI summaries, AI stand-ups, AI project health, and connected agents; served with explicit "AI Studio", "Smart Goals", "Workflow Studio", "AI chat" surfaces
- https://asana.com/company → HTTP 200; first-party company page naming co-founders Dustin Moskovitz (co-founder & CEO, ex-Facebook VP engineering, co-founder of Good Ventures) and Justin Rosenstein (co-founder, ex-Facebook engineering lead, also co-founder of Asana + co-creator of Facebook's "Like" button); Asana publicly launched 2011, publicly traded NYSE:ASAN 2020
- https://asana.com/privacy → HTTP 200; first-party privacy policy exposing `dpa@asana.com` as the canonical data-protection contact; asana.com has live Google Workspace MX with valid SPF/DKIM/DMARC
- https://asana.com/security → HTTP 200; first-party security hub with SOC 2 Type II, SOC 3, ISO/IEC 27001:2022, ISO/IEC 27017, ISO/IEC 27018, ISO/IEC 27701, GDPR, CCPA, HIPAA BAA, AES-256, TLS 1.2+, SAML SSO, SCIM, audit logs, and regional data residency
- Public-record canonical privacy/data-protection inbox: `dpa@asana.com`
- Tier-1 `ai_work_management` cohort sibling #10 after Motion 567, Akiflow 568, Sunsama 569, Routine 570, Reclaim.ai 571, ClickUp 572, monday.com 573, Linear 574, and Notion 575
