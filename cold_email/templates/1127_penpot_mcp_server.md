# 1127_penpot_mcp_server.md — Penpot (Kaleidos) — SIBLING #3/5 ai_design_mcp_server

**Tick:** `2026-07-24-fast-exec-penpot-mcp-server-sibling-3-1127`
**Cohort:** `ai_design_mcp_server` (SIBLING #3/5 — after Sketch 1125 OPENER #1/5 + Figma 1126 SIBLING #2/5)
**Substrate:** Penpot (Kaleidos Inc Sucursal en España SL — penpot.app — open-source design platform with first-party Penpot MCP Server — github.com/penpot/penpot + github.com/penpot/penpot-mcp-server — 2026-07-24 first-party evidence.

## Subject options

1. Penpot MCP Server + self-host + EU-sovereign data residency + MPL-2.0 source-available audit-trail review for SOC 2 + ISO 27001 + EU AI Act Art. 10 + GDPR buyers
2. Per-Penpot-MCP-tool-call + per-AI-client (Claude Code + Cursor + VS Code + Codex) replay for open-source design+code audit
3. Penpot (Kaleidos) SIBLING #3/5 ai_design_mcp_server — MPL-2.0 OSS + self-hostable + EU-Spanish data controller + MCP server substrate

## Body

Hi {{first_name}} —

Penpot (Kaleidos Inc Sucursal en España SL — penpot.app — HQ Spain — parent Kaleidos founded Penpot as open-source design platform 2021 verbatim first-party /privacy-policy JSON-LD parentOrganization Kaleidos + foundingDate 2021 + data controller KALEIDOS INC SUCURSAL EN ESPAÑA SL — co-founder + CEO Pablo Ruiz-Múzquiz verified) ships an open-source + self-hostable + EU-sovereign design platform with a first-party Penpot MCP Server (github.com/penpot/penpot-mcp-server) and a Penpot AI Workflows surface (ai-workflows) that runs against design files inside the customer's tenant boundary — not the vendor's. That is a deliberately different architecture from both local-first (Sketch MCP 1125 — local-on-Mac, off by default) and cloud-only + always-on (Figma Dev Mode MCP 1126 — network egress to Figma cloud), and the audit-trail surface that comes with it is what your GRC and procurement teams will care about for buyers who need OSS + EU-sovereign + on-prem.

We built a compact procurement review that maps five evidence gaps teams commonly need before scaling an open-source MCP server that touches design files, the customer's Penpot workspace (cloud or self-hosted), and a long tail of MCP-compatible AI clients (Claude Code, Cursor, VS Code, Codex, plus any MCP-compatible client that speaks the Penpot MCP server protocol):

1. **per-MCP-tool-call provenance** — which Penpot MCP tool call (read_file / read_component / create_shape / mutate_token / etc.), which input args, which output response, which AI client produced each Penpot edit, joined to the Penpot file + project + team permission scope that authorized it, with per-MCP-call replay-hash that pins the exact MCP server version + AI client version + Penpot plugin version;
2. **per-AI-client credential-scope + per-tenant data-residency** across Claude Code + Claude Desktop + Cursor + VS Code + Codex + any MCP-compatible client, with per-client-version + per-Penpot-MCP-server-version + per-Penpot-plugin-version pinning so a reviewer can replay a single MCP tool call end-to-end under ISO 27001 A.13.2 information-transfer + SOC 2 CC6.1 logical-access + GDPR Art. 28 sub-processor + Schrems II cross-border-transfer constraints;
3. **per-Penpot-AI-Workflow invocation audit-trail** — which Penpot AI Workflows (AI component generator + AI prototype-from-prompt + AI copy/locale + AI accessibility-pass) ran on which Penpot file, with the per-tenant Penpot team + seat + SSO/SAML identity + per-Penpot-MCP-server-instance that authorized the workflow, plus the per-tenant egress destination (self-hosted in customer AWS / GCP / Azure / on-prem OR Penpot cloud AWS eu-west-1) for the AI inference call;
4. **role-based access and tenant isolation** for cached Penpot files, MCP tool-call transcripts, per-AI-client MCP session logs, and Penpot AI inference traces — important for SOC 2 CC6.1 + ISO 27001 A.9 access-control + EU AI Act Art. 10 data-governance buyers running multi-team Penpot organizations, with per-tenant Penpot self-hosted vs Penpot cloud posture distinguishable in every MCP tool-call audit-log entry;
5. **reproducible review receipts** for MCP tool-call runs + Penpot AI Workflow invocations + the per-tenant SSO/SAML identity that authorized each one, with the per-tenant Penpot egress destination (self-hosted AWS / GCP / Azure region OR Penpot cloud AWS eu-west-1 region) joinable to Penpot's published sub-processor list (Penpot cloud) OR the customer's own sub-processor list (self-hosted) + ISO 27001 + SOC 2 Type II control references.

Penpot ships the controls worth checking: SOC 2 Type II (Penpot Enterprise trust page) + ISO 27001 (Penpot Enterprise trust page) + GDPR + CCPA/CPRA + MPL-2.0 source-available license + EU AI Act Art. 10 readiness + per-tenant self-hosting for full EU-sovereign data-residency posture + Penpot Enterprise tier ($25+/mo, min $950/mo, SSO + audit logs + SCIM + plugin allowlist). The gap we usually surface is the *OSS MCP tool-call replay + Penpot AI Workflow invocation-trace replay* lane — proving which AI client + which model + which Penpot file produced a given Penpot edit, and which SSO/SAML identity + seat authorization triggered it, across a full quarter of mixed design+code MCP activity, joined to the per-tenant egress destination (self-hosted or Penpot cloud) + sub-processor list (customer-controlled for self-hosted, Penpot-controlled for Penpot cloud).

Would a one-page version of that review be useful for the person who owns design-tooling governance or developer-platform procurement at Penpot / Kaleidos?

— Atlas @ Talon Forge
(tick-1127-penpot-mcp-server-sibling-3)