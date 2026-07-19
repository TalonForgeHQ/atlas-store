# monday.com — AI Work Management Cohort Sibling #7 (Lead 573)

**Subject:** Quick ask — monday AI agent evidence map

Hi Roy & Eran,

monday.com is the configurable-agent sibling in our `ai_work_management` cohort. Agent Factory, AI agents, Sidekick, Vibe, automations, workflows, integrations, and MCP can act across work management, CRM, software development, service, and campaigns. That breadth is the advantage—but it also raises a practical reconstruction question when context from one board or connector becomes a mutation somewhere else.

We build fixed-fee evidence-gap maps: $500 / 48h for the first reconstruction, or $497/mo for quarterly refresh.

For monday.com, I’d map:

- source board/item/column/update/CRM/dev/service/campaign record → retrieved context → prompt/model/version → agent plan → tool call → mutation
- prompt-injection defense for untrusted updates, docs, forms, email, tickets, repositories, and connected-app content
- account, workspace, board, guest, role, app, connector, and regional isolation across Agent Factory and MCP
- deletion, retention, rollback, notification, and downstream-sync propagation after an agent changes work
- immutable human-approval evidence for status changes, assignments, messages, code actions, campaign sends, and external writes
- per-agent, per-model, per-tool-call, per-board, per-product, and per-customer cost attribution

Your Trust Center already gives procurement teams strong anchors—SOC 1/2/3, ISO 27001/27017/27018/27701, GDPR, CCPA, HIPAA BAA, CSA STAR, and TX-RAMP resources. The missing layer I’d test is whether those controls can reconstruct one agent action end to end under EU AI Act Articles 12/14 and SOC 2 CC7.2.

Worth a 15-minute call this week? Otherwise I’ll assume the timing is bad and try again in Q4.

— Atlas
Talon Forge LLC · talonforge.dev

---

**Verified live 2026-07-19:**
- https://monday.com/about → HTTP 200, canonical redirect to `/p/about/`; first-party page names co-founders Roy Mann and Eran Zinman
- https://monday.com/trustcenter → HTTP 200; SOC 1 Type II, SOC 2 Type II, SOC 3, ISO 27001/27017/27018/27701, CSA STAR, TX-RAMP, GDPR/UK GDPR, CCPA, and HIPAA BAA resources
- https://monday.com/l/privacy/privacy-policy/ → HTTP 200; Cloudflare-decoded `privacy@monday.com`, `dpo@monday.com`, and `support@monday.com`
- monday.com MX → live Google Workspace mail exchangers
- Tier-1 `ai_work_management` cohort sibling #7 after Motion 567, Akiflow 568, Sunsama 569, Routine 570, Reclaim.ai 571, and ClickUp 572
