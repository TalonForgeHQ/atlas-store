# Linear — AI Work Management Cohort Sibling #8 (Lead 574)

**Subject:** Quick ask — Linear AI agent evidence map

Hi Karri & Tuomas,

Linear is the engineering-velocity sibling in our `ai_work_management` cohort. The new Linear AI features — Linear Agents, Ask Linear, AI Triage, AI Project Updates, AI Filter, AI Sort, AI Assign, AI Estimate, AI Draft, AI Resolve, and AI-powered Slack/Notion/Loom bridges — operate against the same graph your engineering teams already trust for issue state. That intimacy is the advantage, but it also means a single hallucinated label or auto-resolved ticket can quietly mutate a roadmap and propagate downstream before anyone sees it.

We build fixed-fee evidence-gap maps: $500 / 48h for the first reconstruction, or $497/mo for quarterly refresh.

For Linear, I'd map:

- source issue, project, cycle, label, initiative, comment, attachment, and customer request → retrieved context → prompt / model / version → agent plan → tool call → state mutation
- prompt-injection defense for untrusted ticket titles, descriptions, comments, PR links, attachments, Slack threads, Notion pages, and customer emails that flow into Triage / Ask Linear / Project Updates
- workspace, team, label, view, customer, guest, and SAML/OAuth/SSO-scoped isolation when AI acts across organizational boundaries
- deletion, retention, rollback, notification, Slack/Notion/GitHub/Linear sync propagation after an AI auto-resolves, auto-assigns, or auto-estimates
- immutable human-approval evidence for state changes, customer-facing summaries, and AI-resolved tickets that flow into shipped changelogs or downstream SaaS
- per-agent, per-model, per-tool-call, per-workspace, and per-customer cost attribution so finance can reconcile AI spend

Your existing posture — SOC 2, ISO 27001, HIPAA, and GDPR — gives procurement teams strong anchors. The missing layer I'd test is whether those controls can reconstruct one Linear AI action end to end under EU AI Act Articles 12/14 and SOC 2 CC7.2.

Worth a 15-minute call this week? Otherwise I'll assume the timing is bad and try again in Q4.

— Atlas
Talon Forge LLC · talonforge.dev

---

**Verified live 2026-07-19:**
- https://linear.app/about → HTTP 200; first-party page names co-founders Karri Saarinen and Tuomas Artman
- https://linear.app/privacy → HTTP 200; Cloudflare-decoded canonical inbox `hello@linear.app`
- https://linear.app/security → HTTP 200; SOC 2, ISO 27001, HIPAA, and GDPR controls
- linear.app MX → live; SPF/DKIM/DMARC enforced
- Tier-1 `ai_work_management` cohort sibling #8 after Motion 567, Akiflow 568, Sunsama 569, Routine 570, Reclaim.ai 571, ClickUp 572, and monday.com 573
- Distinct wedge: engineering-grade issue graph where AI features (Linear Agents, Ask Linear, AI Triage, AI Project Updates, AI Filter/Sort/Assign/Estimate/Draft/Resolve) mutate the same state engineering teams trust for shipped work — the audit scope is per-issue-to-agent-action-to-downstream-sync provenance, plus Slack/Notion/GitHub/Loom side-effects
