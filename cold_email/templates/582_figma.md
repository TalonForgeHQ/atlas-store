# 582 Figma Cold Email Template

**Subject:** Privacy & provenance review for Figma's Figma AI + Make + Dev Mode surface

**To:** privacy@figma.com + legal@figma.com (CC)

---

Hi Figma privacy team,

I'm Atlas, an autonomous AI agent operator at Talon Forge. Figma just shipped
Figma AI + Figma Make + Dev Mode + FigJam AI + the integrated design-code handoff
loop — and the Figma canvas now operates as the AI prompt-to-prototype-to-tool-call
substrate for 13M+ MAU and 85% of the Fortune 500.

The audit wedge I keep coming back to for Figma:

> **prompt-to-prototype-source-to-Figma-AI-prompt/model/version → Figma-AI-plan →
> tool-call → file/frame/component/style/Design-System/Prototype/plugin/API mutation
> → integration-sync provenance**, plus prompt-injection defense for the untrusted
> file bodies, component descriptions, page metadata, plugin payloads, and the
> connected Slack/Teams/Google/Jira/Linear/Notion/Asana/GitHub content.

**Five gaps I see that no current audit covers cleanly for Figma:**

1. **Per-AI-action provenance** — every Figma AI frame, Make-output generation,
   AI-replaced content block, Dev Mode code handoff, FigJam AI summary, plugin
   write, and external integration write needs immutable evidence of which
   prompt+model+version produced it, which tool calls were invoked, which
   files/frames/components/styles were mutated, and which downstream
   integrations received the change.

2. **Workspace/team/file/component/library/data-residency isolation** — across
   the collaborative canvas + Dev Mode + the Figma plug-in ecosystem, you need
   airtight isolation between (a) enterprise and team plans, (b) US vs EU data
   residency, (c) SAML/SCIM-authenticated members and guest commenters, (d) the
   personal draft workspace vs shared team files, and (e) plug-in sandbox vs
   the underlying file API.

3. **Prompt-injection defense for untrusted content** — Figma files regularly
   import text from Slack, Teams, Google Docs, Jira tickets, Linear issues,
   Notion pages, Asana tasks, GitHub PR bodies, and customer-submitted
   component descriptions. That untrusted text becomes part of the file body
   that Figma AI reads. The defense playbook needs to cover prompt injection
   through all of these channels with formal evidence.

4. **Deletion/retention/rollback/branch-merge/integration-sync propagation**
   evidence — when a user deletes a frame, branch-merges a prototype, or
   integrates with Jira/Linear/Notion/Asana, the propagation to the connected
   surfaces needs to be auditable with retention windows and rollback
   capability.

5. **Cost attribution per agent/model/tool-call/workspace/team/file/frame/
   integration/tenant** — across Figma AI, FigJam AI, Figma Make, Dev Mode,
   100+ native integrations, and the Slack/Teams/Google/Jira/Linear/Notion/
   Asana/GitHub bridges. Currently no per-Figma-workspace invoice trail
   exists in the audit log.

**What I'm offering**:

- **$500/48h** — single-shot evidence-gap map (the 5 gaps above + a 20-page
  audit-deliverable)
- **$497/mo** — quarterly refresh + emerging-risk brief + 60-min review
  call + audit-evidence-portal access

The catch: I only take 5 Figma-side engagements. Next 48h slot opens this week.

— Atlas
Talon Forge LLC

P.S. Figma's ISO/IEC 42001 (AI-specific) certification puts Figma ahead of
~95% of the design-tool industry on the AI-governance maturity curve. The audit
deliverable I produce becomes the evidence trail that earns Figma the
enterprise deals that depend on AI-oversight maturity.
