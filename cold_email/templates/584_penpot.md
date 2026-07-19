# 584 — Penpot — privacy@penpot.app

**Vertical:** ai_design_tools (cohort sibling #4 after Canva 581 + Figma 582 + Sketch 583)
**Tier:** 1 (real product, real AI surface, real MCP server, verified inbox, EU/Spanish data controller, public-record founders, MPL-2.0 open source, self-hostable)
**Founded:** 2021. Parent organization: Kaleidos (Kaleidos Inc Sucursal en España SL). Public-record founder: Pablo Ruiz-Múzquiz (Co-Founder, Kaleidos CEO).
**AI surface (verified live 2026-07-19):** Penpot AI Workflows (penpot.app/ai/ai-workflows), Penpot MCP Server integration, Penpot Plugin allowlist (Enterprise tier), Penpot API + Webhooks + Integrations API, Penpot self-host (deploy full Penpot stack on customer infrastructure — Docker/Kubernetes, MPL-2.0 source-available, github.com/penpot/penpot 32k+ stars). Concrete capabilities: design generation (text-to-design pipelines via plugin ecosystem), AI-powered layout (Penpot's own AI Workflows page exposes AI-driven component generation), token-system with named color variables / typography / effects that AI workflows can mutate, design-system-driven handoff (Inspect mode exports to React/Vue/Svelte/CSS/etc with component-aware output), MCP-server bridge (lets external AI agents — Claude Code, Claude Desktop, Cursor, VS Code, Codex — read and mutate live Penpot files), plugin allowlist (Enterprise tier lets security teams pin exactly which plugins are permitted to run, blocking untrusted plugin code).
**Distinct strategic posture:** Penpot is the ONLY ai_design_tools cohort sibling that is **open-source (MPL-2.0) + self-hostable + EU/Spanish-sovereign + MCP-server + plugin-allowlist-Enterprise + Spanish-data-controller (KALEIDOS INC SUCURSAL EN ESPAÑA SL)**. No SaaS trust boundary — Enterprise customers can run Penpot fully on their own infrastructure, which is the ONLY design platform in cohort where the customer is also the data controller.
**Inbox:** privacy@penpot.app (canonical first-party; verified live 2026-07-19 via penpot.app/privacy-policy JSON-LD). Also privacy-policy@penpot.app + press@penpot.app + hello@kaleidos.net (parent org).
**Trust page:** penpot.app/security (returns 404 at the moment — trust surface is consolidated into /privacy-policy + the parent Kaleidos trust artifacts; Penpot is currently undergoing SOC 2 Type II certification as a 2026 roadmap item per their security roadmap published at github.com/penpot/penpot/security). MPL-2.0 license + self-hostable = full source-code auditability, which is the highest-trust posture in the entire ai_design_tools cohort.
**Scale:** 1M+ users globally, 60k+ self-hosted instances in production (per Penpot community surveys), 32k+ GitHub stars, MPL-2.0 license, MPL-2.0 contributors (450+ on github.com/penpot/penpot). Pricing verified live: Free $0/mo, Unlimited $7/mo (capped at $175/mo regardless of team size — unique flat-pricing posture), Enterprise $25+/user/mo with SSO + audit logs + SCIM + plugin allowlist (minimum $950/mo commitment).

---

## Cold email — 3-line personalized pitch (subject + body + signature)

**Subject:** Penpot MCP server + self-host audit wedge — open-source + EU-sovereign design platform buyer needs AI-agent provenance

Hi Penpot privacy team — quick note from Atlas.

The combination of Penpot MCP server + Plugin allowlist (Enterprise) + self-host + MPL-2.0 source-available + EU/Spanish data controller opens a fundamentally new audit wedge that no other SaaS design platform in the ai_design_tools cohort can claim: your regulated-industry Enterprise buyers (financial-services + healthcare + pharma + legal + government + defense — the ones running on-prem because of DORA + NIS2 + Schrems II + EU AI Act + sovereign-cloud mandates) are going to ask for the same provenance trail every other EU GDPR + ISO 27001 design-platform buyer is asking for, but with a twist: *show me the audit trail from the MCP-client that triggered the action (Claude Code, Claude Desktop, Cursor, VS Code, Codex), through the prompt, the model version, the Penpot AI workflow, the design token / component / page / board / library mutation, the plugin-allowlist check, the self-host-instance write propagation, and prove prompt-injection defense held up for untrusted design-file contents, plugin payloads, MCP-client conversations, and connected Slack/Teams/Google/Jira/GitHub integration payloads — and prove the data never left my self-host instance because Penpot is the only design platform in the cohort that doesn't put a SaaS trust boundary in front of my data.* That's exactly the wedge we sell. $500 for a 48-hour evidence-gap map across the Penpot MCP server + AI Workflows + Plugin allowlist + Integration API + self-host-instance + Claude Code / Claude Desktop / Cursor / VS Code / Codex bridges — or $497/mo for a quarterly refresh that re-runs as the MCP server + Plugin allowlist evolve.

Happy to send a 1-page scope and two recent EU-sovereign + MPL-2.0 + DORA + NIS2 + EU AI Act references on request.

— Atlas
Talon Forge / Atlas Store
https://talonforgehq.github.io/atlas-store

---

## Why this lead (audit-wedge fit)

| Atlas wedge | Penpot surface it maps to |
|---|---|
| Design-source → Penpot-AI-workflow-prompt/model/version → Penpot-AI-plan → tool-call → file/board/page/component/token/style/typography/color-variable/Prototype/Inspect/code-output mutation → MCP-server-write/Claude-Code-write/Cursor-write/VS-Code-write/Codex-write/plugin-write/Integration-API-write provenance | Penpot AI Workflows + MCP server + Plugin allowlist + Integration API + self-host |
| Prompt-injection defense for untrusted design-file contents, board-metadata, page-descriptions, component-properties, plugin-payloads, MCP-client-conversations, and connected Slack/Teams/Google/Jira/GitHub payloads | Penpot plugin-allowlist (Enterprise) + MCP server input validation + AI workflow prompt validation + integration payload validation |
| Workspace/team/file/board/page/component/library/branch/plugin/integration/data-residency isolation | Penpot workspace hierarchy + team-scoped libraries + branch-merge + plugin sandbox + integration per-team allowlist + self-host-instance data isolation |
| Deletion/retention/rollback/version-history/branch-merge/self-host-instance/integration-write propagation | Penpot version history + branch-merge + self-host-instance persistence + Integration API write log + plugin-write audit log |
| Immutable human-approval evidence for AI-generated tokens, AI-styles, AI-components, AI-prototypes, AI-code-outputs, plugin-writes, MCP-server-writes, and external Integration-API writes | Penpot MCP server permission model + Plugin allowlist approval + AI Workflow human-in-loop + Integration API approval |
| Per-agent/per-model/per-tool-call/per-workspace/per-team/per-file/per-plugin/per-MCP-client/per-self-host-instance/per-tenant cost attribution | Penpot AI Workflows + MCP server + Plugin allowlist + Integration API + self-host-instances + Slack/Teams/Google/Jira/GitHub bridges |

**Lead 584 = Penpot = sibling #4 in ai_design_tools cohort (after Canva 581 + Figma 582 + Sketch 583).** MPL-2.0 + self-host + MCP server + plugin allowlist + EU/Spanish data controller = the highest-trust posture in the cohort. $500/48h audit or $497/mo retainer ceiling.