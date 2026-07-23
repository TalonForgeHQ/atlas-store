# 1126_figma_mcp_server.md — Figma (Figma, Inc.) — Sibling #2/5 ai_design_mcp_server

**Tick:** `2026-07-24-fast-exec-figma-mcp-server-sibling-2-1126`
**Cohort:** `ai_design_mcp_server` (SIBLING #2/5 — after Sketch 1125 OPENER #1/5)
**Substrate:** Figma, Inc. — figma.com — cloud-native collaborative design platform — first-party Dev Mode MCP Server + Figma AI features — 2026-07-24 first-party evidence.

## Subject options

1. Figma Dev Mode MCP Server + Figma AI audit-trail review for SOC 2 + ISO 27001 + GDPR + EU AI Act Art. 10 buyers
2. Per-Figma-MCP-tool-call + per-AI-client (Claude Code + Cursor + VS Code + Codex + Figma Make) replay for design+code audit
3. Figma (Figma, Inc.) SIBLING #2/5 ai_design_mcp_server — cloud-only MCP gateway, always-on, network egress to Figma cloud

## Body

Hi {{first_name}} —

Figma (Figma, Inc. — figma.com — HQ San Francisco CA — co-founder + CEO Dylan Field verified verbatim first-party /about 2026-07-24) ships a cloud-native design platform with a first-party Dev Mode MCP Server and an always-on Figma AI surface (Figma Make + visual search + auto-layout suggestions + generative-edit features) that runs over a network boundary to Figma's cloud. That is a deliberately different architecture from local-first design+AI vendors (Sketch MCP Server is local-on-Mac, off by default), and the audit-trail surface that comes with it is what your GRC and procurement teams will care about.

We built a compact procurement review that maps five evidence gaps teams commonly need before scaling a cloud-only MCP server that touches design files, always-on Figma AI features, and a long tail of MCP-compatible AI clients (Claude Code, Cursor, VS Code, Codex, plus Figma Make and any other MCP-compatible client):

1. **per-MCP-tool-call provenance** — which Figma Dev Mode MCP tool (get_file, get_node, create_frame, get_styles, get_variable_defs, etc.), which input args, which output response, which AI client produced each Figma edit, joined to the Figma file + library + team permission scope that authorized it;
2. **per-AI-client credential-scope** across Claude Code + Claude Desktop + Cursor + VS Code + Codex + Figma Make, with per-client-version + per-Figma-plugin-version pinning so a reviewer can replay a single MCP tool call end-to-end under ISO 27001 A.13.2 information-transfer + SOC 2 CC6.1 logical-access;
3. **per-Figma-AI-feature always-on decision audit-trail** — which Figma AI features (Figma Make, visual search, auto-layout, generative-edit) ran on which Figma file, with the per-tenant Figma team + seat + SSO/SAML identity that authorized the feature toggle, plus the Figma cloud egress destination (AWS region + GCP region) for the AI inference call;
4. **role-based access and tenant isolation** for cached Figma files, MCP tool-call transcripts, per-AI-client MCP session logs, and Figma AI inference traces — important for SOC 2 CC6.1 + ISO 27001 A.9 access-control buyers running multi-team Figma organizations; and
5. **reproducible review receipts** for MCP tool-call runs + Figma AI feature toggles + the per-tenant SSO/SAML identity that authorized each one, with the Figma cloud egress destination joinable to Figma's published sub-processor list + ISO 27001 + SOC 2 Type II control references.

Figma ships the controls worth checking: SOC 2 Type II (Figma enterprise trust page) + ISO 27001 (Figma enterprise trust page) + GDPR + CCPA/CPRA + HIPAA BAA (Figma enterprise plans) + EU AI Act readiness. The gap we usually surface is the *cloud-MCP tool-call replay + Figma AI inference-trace replay* lane — proving which AI client + which model + which Figma file produced a given Figma edit, and which SSO/SAML identity + seat authorization triggered it, across a full quarter of mixed design+code MCP activity, joined to the Figma cloud egress destination + sub-processor list.

Would a one-page version of that review be useful for the person who owns design-tooling governance or developer-platform procurement at Figma?

— Atlas @ Talon Forge
(tick-1126-figma-mcp-server-sibling-2)