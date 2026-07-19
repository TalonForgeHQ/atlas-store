# Wrike — $500/48h Evidence-Gap Audit

**To:** privacy@wrike.com (privacy@team.wrike.com cc)
**From:** Talon Forge LLC — Atlas
**Subject:** Wrike AI + 400+ integrations: prompt-injection + provenance audit, $500

---

Hi Wrike team,

You ship Wrike AI, AI Studio, AI workflows, AI summaries, AI project briefs, AI subtasks, AI risk prediction, and AI request forms into the same task-project-folder-dashboard-workflow surface that 50%+ of the Fortune 500 uses, with 400+ native integrations reading and writing connected Slack, Microsoft Teams, Google Workspace, Salesforce, Jira, ServiceNow, GitHub, Adobe, DocuSign, Box, Dropbox, and OneDrive state.

I'm offering a 48-hour evidence-gap audit against OWASP LLM Top 10 + MITRE ATLAS + NIST AI RMF + EU AI Act for the Wrike AI surface. The deliverable is a 25-40 page map of which audit signals you can already produce, which ones you can't, and the cheapest path to the missing ones.

**What's in the audit (5 sections):**

1. **Provenance coverage for Wrike AI.** Source-task-to-retrieved-context-to-prompt/model/version-to-Wrike-AI-plan-to-tool-call-to-task/project/folder/dashboard/workflow-mutation-to-integration-sync reconstruction, with per-task-id + per-prompt-id + per-summary-id + per-integration-write-id traceability.

2. **Prompt-injection defense for untrusted inputs.** Task bodies, project descriptions, request forms, dashboard inputs, workflow payloads, file attachments, AI Studio prompt templates, and connected Slack/Teams/Google/Salesforce/Jira/ServiceNow/GitHub/Adobe content. Current sanitization, current allow/deny lists, and the gap between them.

3. **Tenant + workspace + integration isolation.** Workspace/space/folder/project/task/guest/integration/data-residency boundary enforcement per SOC 2 Type II CC6.1 + GDPR Art. 28 + ISO 27701. Citrix acquisition raised the bar here — your enterprise customers will ask.

4. **Deletion + retention + rollback + version-history propagation across 400+ integrations.** When a customer deletes a record under CCPA / GDPR Art. 17, what happens in connected Slack channels, Salesforce opportunities, Jira tickets, ServiceNow incidents, GitHub issues, Adobe assets, DocuSign envelopes, Box folders, Dropbox files, OneDrive documents?

5. **Immutable human-approval evidence + per-agent/per-model/per-tool-call/per-workspace/per-integration/per-tenant cost attribution.** Critical for your AI Studio + AI workflows + AI risk prediction surface, especially for SOX + HIPAA BAA customers.

**Why now:** EU AI Act general-purpose model obligations land August 2026. Your enterprise customers in financial services, healthcare, and government will demand evidence-gap maps from you in the next 90 days.

**Pricing:** $500 for the 48-hour audit, $497/mo for a quarterly refresh against the same scope as your Wrike AI surface evolves.

If useful, reply with a 30-minute slot this week and I'll send the audit brief.

— Atlas, Talon Forge LLC
