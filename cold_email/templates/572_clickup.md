# ClickUp — Converged AI Workspace Cohort Sibling #6 (Lead 572)

**Subject:** Quick ask — ClickUp Super Agents evidence map

Hi Zeb & Alex,

ClickUp is the converged-workspace sibling in our `ai_work_management` cohort. Tasks, Docs, Chat, Calendar, Automations, Brain, Super Agents, Ambient Agents, Notetaker, and Enterprise Search all share one work context. That convergence is the product advantage—but it also makes an agent action harder to reconstruct when retrieved content becomes a task, comment, assignment, automation, or cross-app write.

We build fixed-fee evidence-gap maps: $500 / 48h for the first reconstruction, or $497/mo for quarterly refresh.

For ClickUp, I’d map:

- source task/doc/chat/calendar event → retrieved context → prompt/model/version → agent plan → tool call → workspace mutation
- prompt-injection defense for untrusted Docs, comments, attachments, meeting notes, and connected search results
- tenant, Space, Folder, List, task, guest, connector, and data-residency isolation for Super and Ambient Agents
- deletion, retention, rollback, and notification propagation after an agent changes work
- immutable human-approval evidence for assignments, due dates, messages, automations, exports, and external writes
- per-agent, per-model, per-tool-call, per-workspace, and per-customer cost attribution

ClickUp’s security page already gives procurement teams strong anchors: SOC 1/2/3, ISO 27001/27017/27018/27701, ISO 42001, AES-256 at rest, TLS 1.2, and regional data residency. The missing layer I’d test is whether those controls can reconstruct one autonomous action end to end under EU AI Act Articles 12/14 and SOC 2 CC7.2.

Worth a 15-minute call this week? Otherwise I’ll assume the timing is bad and try again in Q4.

— Atlas
Talon Forge LLC · talonforge.dev

---

**Verified live 2026-07-19:**
- https://clickup.com/about → HTTP 200; converged software + AI + human workspace used by millions of teams
- https://clickup.com/press → HTTP 200; first-party press page describes the Converged AI Workspace and $300M+ ARR
- https://clickup.com/security → HTTP 200; SOC 1/2/3, ISO 27001/27017/27018/27701/42001, AES-256, TLS 1.2, regional residency; sales@clickup.com published
- https://clickup.com/terms/privacy → HTTP 200; support@clickup.com published for privacy-rights requests
- Public-record founders: Zeb Evans (co-founder/CEO) and Alex Yurkowski (co-founder/CTO), founded 2017
- Tier-1 `ai_work_management` cohort sibling #6 after Motion 567, Akiflow 568, Sunsama 569, Routine 570, and Reclaim.ai 571
