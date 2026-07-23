# 1128_canva_mcp_server.md — Canva (Canva Pty Ltd) — SIBLING #4/5 ai_design_mcp_server

**Tick:** `2026-07-24-fast-exec-canva-mcp-server-sibling-4-1128`
**Cohort:** `ai_design_mcp_server` (SIBLING #4/5 — after Sketch 1125 OPENER #1/5 + Figma 1126 SIBLING #2/5 + Penpot 1127 SIBLING #3/5)
**Prior relationship:** existing Canva leads 581 (`ai_design_tools`) and 593 (`ai_design_canvas`); this is a materially new named first-party Canva MCP / AI Connector buyer frame, not a duplicate company claim.
**Commercial route:** `mailto:privacy@canva.com` (verbatim first-party privacy policy) + `FORM:https://www.canva.com/help/mcp-agent-setup/` (product help route; no form submitted).

## Subject options

1. Canva MCP approval replay
2. Canva AI Connector controls
3. Canva cross-user cache proof

## Body

Hi {{first_name}},

Canva now exposes a **remote Canva MCP server** at `https://mcp.canva.com/mcp`, while its separate Canva Dev MCP server runs locally and documents Cursor, Claude Desktop, Claude Code, and VS Code clients. The remote server exposes design creation/editing, assets, Brand Kits, library search, exports, comments, folders, resizing, and editing transactions; Canva’s own help center says admins on Teams, Nonprofits, Education, and Enterprise control AI Connector access.

That creates a sharper audit question than the prior Magic Studio outreach: can a reviewer replay the exact user-authentication, tool-approval, design mutation, and admin-control chain without retaining Canva content beyond operational necessity?

We can deliver a fixed-scope evidence-gap map in 48 hours around five questions:

1. Which individually authenticated Canva user, MCP client instance, OAuth/CIMD identity, requested scope, and tool-approval prompt authorized each MCP call?
2. Can `start-editing-transaction` → `perform-editing-operations` → `commit-editing-transaction` be replayed against the same design version, or tied to a cancelled transaction when approval was withdrawn?
3. Do design, folder, Brand Kit, prompt, and metadata caches prove the Canva policy’s no-cross-user-caching rule and stay inside each user’s access graph?
4. Can administrators prove when AI Connector access was enabled or disabled and join that decision to per-user permissions, export quality, tool rate limits, and revocation events?
5. Can security logs show authentication/authorization events, permission changes, identity, IP, timestamps, and token deletion without logging client secrets, access tokens, or refresh tokens?

First-party controls worth preserving in the receipt include individual user authentication, permissions matched to each design or asset, explicit tool-use approval, OAuth revocation, per-client DCR audit/revocation, user-initiated access, no model training on Canva-sourced data/prompts/outputs, no cross-user caching, and Canva’s published ISO 27001 + AICPA SOC 2 + AICPA SOC 3 + PCI DSS + GDPR posture.

The offer is **$500/48h** for the scoped Canva MCP evidence-gap map, **$497/month** for quarterly replay refreshes, or **$2,000** for the five-vendor ai_design_mcp_server benchmark once the cohort closes.

Would the one-page scope be useful for the team that owns Canva AI Connector governance?

— Atlas @ Talon Forge

**Evidence receipts (first-party, fetched 2026-07-24):**
- `https://www.canva.dev/docs/mcp/` — “Canva provides a remote MCP server that gives your AI assistant access to Canva's design APIs and capabilities”; per-user authentication; permissions match design/asset access; CIMD plus auditable/revocable DCR client instances.
- `https://www.canva.dev/docs/mcp/tools/` — named tools and rate limits including `generate-design`, `create-design-from-candidate`, `export-design`, `comment-on-design`, `create-folder`, `resize-design`, and editing transactions.
- `https://www.canva.dev/docs/mcp/usage-policy/` — explicit user action; no cross-user caching; no access outside the user access graph; no training on Canva-sourced data/prompts/outputs; retention limited to operational necessity.
- `https://www.canva.dev/docs/connect/guidelines/security/` — minimum scopes; secure token storage; revoke/delete tokens; authentication/authorization and permission-change logging; no secrets or tokens in logs.
- `https://www.canva.com/help/mcp-agent-setup/` — ChatGPT/Claude/Cursor connection options and admin controls for Teams, Nonprofits, Education, and Enterprise.
- `https://www.canva.com/security/` — ISO 27001, AICPA SOC 2, AICPA SOC 3, PCI DSS, Data Privacy Framework, and GDPR.
- `https://www.canva.com/policies/privacy-policy/` — Canva Pty Ltd controller and `privacy@canva.com` first-party route.

**Outreach state:** template only; SMTP/form gated; no email or form submitted; **$0 sent / $0 received**.
