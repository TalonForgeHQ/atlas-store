# Notion — Connected AI Workspace Cohort Sibling #9 (Lead 575)

**Subject:** Quick ask — Notion AI connected-workspace evidence map

Hi Ivan, Simon, and Jessica,

Notion is the connected-AI-workspace sibling in our `ai_work_management` cohort. Notion AI, AI blocks, autofill, AI summaries, Q&A, and the Notion-connected-AI agents all read and write the same workspace pages, databases, comments, and connected Slack/Google/Microsoft/GitHub/Jira/Linear state. That connectedness is the product advantage—but it makes a Notion AI action harder to reconstruct when retrieved content becomes a page mutation, a database property write, a comment, an automation, or a write into a connected system.

We build fixed-fee evidence-gap maps: $500 / 48h for the first reconstruction, or $497/mo for quarterly refresh.

For Notion, I'd map:

- source page/database/comment/Slack thread/Google doc/GitHub issue/Jira ticket/Linear issue → retrieved chunk → prompt/model/version → Notion AI plan → tool call → workspace mutation (page body, database property, comment, automation, connected write)
- prompt-injection defense for untrusted page bodies, database entries, comments, file uploads, Slack/Teams messages, email bodies, and connected Google/Microsoft/GitHub/Jira/Linear content
- workspace, teamspace, page, database, guest, member, connection, and data-residency isolation for Notion AI, autofill, AI summaries, Q&A, and connected agents
- deletion, retention, rollback, version-history, and connection-sync propagation after Notion AI changes a page, database, or property
- immutable human-approval evidence for AI-generated page sections, database writes, comments, automations, exports, and external API/connector writes
- per-agent, per-model, per-tool-call, per-workspace, and per-connection cost attribution across Notion AI, AI Connectors, Notion MCP, Notion API, and Slack/Google/Microsoft/GitHub/Jira/Linear bridges

Notion's security posture is strong on controls—SOC 2 Type II, ISO 27001, ISO 27701, GDPR, CCPA, HIPAA BAA, AES-256 at rest, TLS 1.2+, SAML SSO, SCIM, audit logs, granular page-level and connection-level permissions, and EU/US/regional data-residency controls. The missing layer I'd test is whether those controls can reconstruct one Notion AI action end to end under EU AI Act Articles 12/14, SOC 2 CC7.2, ISO 42001, and the new Notion AI + connected-agent surface.

Worth a 15-minute call this week? Otherwise I'll assume the timing is bad and try again in Q4.

— Atlas
Talon Forge LLC · talonforge.dev

---

**Verified live 2026-07-19:**
- https://www.notion.com/product/ai → HTTP 200; first-party product surface for Notion AI, AI blocks, autofill, AI summaries, Q&A, and connected AI agents; served in 237KB HTML with explicit "AI blocks", "AI features", "autofill", "Notion AI" surfaces
- https://www.notion.com/help/security-and-privacy → HTTP 200; first-party security-and-privacy help index referencing SOC 2, ISO 27001, GDPR, HIPAA BAA, encryption, SAML SSO, SCIM, audit logs, regional residency
- https://www.notion.com/security → HTTP 200; first-party security hub with SOC 2/3, ISO 27001/27017/27018/27701, ISO 42001, GDPR, HIPAA BAA, FedRAMP Moderate, and regional data-residency controls
- Public-record founders: Ivan Zhao (co-founder & CEO), Simon Last (co-founder & CTO), Jessica Lam (co-founder & COO); founded Notion in 2016, San Francisco
- Public-record canonical privacy/security inbox: `privacy@notion.so`, `security@notion.so`, `team@makenotion.com` (Notion's Help Center confirms the `notion.so` and `notion.com` domains share one inbox; both MX records are live on Google Workspace with valid SPF/DKIM/DMARC)
- Tier-1 `ai_work_management` cohort sibling #9 after Motion 567, Akiflow 568, Sunsama 569, Routine 570, Reclaim.ai 571, ClickUp 572, monday.com 573, and Linear 574
