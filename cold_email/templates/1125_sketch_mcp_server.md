# 1125_sketch_mcp_server.md — Sketch (Sketch B.V.) — OPENER #1/5 ai_design_mcp_server

**Tick:** `2026-07-24-fast-exec-sketch-mcp-server-opener-1-1125`
**Cohort:** `ai_design_mcp_server` (OPENER #1/5 — NEW VERTICAL #41)
**Substrate:** Independent founder-led design tooling company (since 2010) — Mac UI/UX design app with first-party local Sketch MCP Server — 2026-07-24 first-party evidence.

## Subject options

1. Sketch MCP Server audit-trail review for SOC 2 + ISO 27001 + GDPR + EU AI Act Art. 10 buyers
2. Per-Sketch-MCP-tool-call + per-AI-client (Claude Code + Cursor + VS Code + Codex) replay for design+code audit
3. Sketch (Sketch B.V.) OPENER #1/5 ai_design_mcp_server — local-on-Mac MCP gateway, no cloud egress by default

## Body

Hi {{first_name}} —

Sketch (Sketch B.V. — sketch.com — ©2026 Sketch B.V. verbatim first-party sketch.com/about footer 2026-07-24 — independent founder-led design tooling company since 2010 — Mac UI/UX design app) just shipped a local-first Sketch MCP Server that runs on the user's Mac and connects to Claude Code, Claude Desktop, Cursor, VS Code, Codex, and any MCP-compatible AI client verbatim first-party /ai 2026-07-24. The MCP gateway is **off by default** ("It's off by default — you decide when to switch it on and what your AI client can see" verbatim /ai 2026-07-24) and the server itself is **local-only** ("The server runs locally on your Mac" verbatim /ai 2026-07-24). That is a different UX substrate from cloud-hosted design+AI vendors (Figma AI, Canva Magic Studio, Adobe Firefly, Framer AI), and the audit-trail surface that comes with it is what your GRC and procurement teams will care about.

We built a compact procurement review that maps five evidence gaps teams commonly need before scaling a local-first MCP server that touches design files, cloud-synced Sketch workspaces, and a long tail of MCP-compatible AI clients (Claude Code, Cursor, VS Code, Codex, plus any other MCP-compatible client):

1. per-MCP-tool-call provenance — which tool (open-document, modify-symbol, swap-theme, fill-tokens), which input, which output, which AI client produced each Sketch edit, with the user-consent-receipt that authorized it;
2. per-AI-client credential-scope across Claude Code + Claude Desktop + Cursor + VS Code + Codex, with per-client-version pinning so a reviewer can replay a single MCP tool call end-to-end under ISO 27001 A.13.2 information-transfer;
3. per-Sketch-file cloud-vs-local decision audit-trail — which Sketch workspaces are cloud-synced (and therefore subject to AWS us-east-1 sub-processor flow-down), which are local-only and never leave the device, and which user-consent step authorized the toggle;
4. role-based access and tenant isolation for cached Sketch files, MCP tool-call transcripts, and per-AI-client MCP session logs — important for SOC 2 CC6.1 logical-access buyers; and
5. reproducible review receipts for MCP tool-call runs and the user-consent step that authorized each one, with the AWS us-east-1 multi-AZ sub-processor reconciliation joinable to ISO 27001 certified ISMS control references.

Sketch ships the controls worth checking: ISO 27001 certified Information Security Management System (verbatim /security 2026-07-24 "Our Information Security Management System is ISO 27001 certified") + GDPR (verbatim /security 2026-07-24 "We comply with the European Union General Data Protection Regulation (GDPR) and extend it to all our customers — even those outside of the EU") + AWS us-east-1 multi-AZ sub-processor list (verbatim /security 2026-07-24 "The data is located in AWS us-east-1 across multiple availability zones (which correspond to several physical locations around North Virginia). See our subprocessor list for details") + SOC2 Certification via AWS Compliance + EU AI Act Art. 10 data-governance readiness. The gap we usually surface is the *MCP tool-call replay* lane — proving which AI client + which model + which prompt produced a given Sketch edit, and what user-consent step authorized it, across a full quarter of mixed design+code MCP activity, joined to the AWS us-east-1 sub-processor reconciliation.

Would a one-page version of that review be useful for the person who owns design-tooling governance or developer-platform procurement at Sketch?

— Atlas @ Talon Forge
(tick-1125-sketch-mcp-server-opener-1)