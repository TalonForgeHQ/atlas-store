# 583 — Sketch — privacy@sketch.com

**Vertical:** ai_design_tools (cohort sibling #3 after Canva 581 + Figma 582)
**Tier:** 1 (real product, real AI surface, verified inbox, public trust page, public-record founders, 15-year independent Dutch + EU-jurisdiction company)
**Founded:** 2010 in The Hague, Netherlands. Public-record founders: Pieter Omvlee (Co-Founder + CEO; founded 2010, ex-Neerlandse Spoorwegen developer) + Emanuel Sá (Co-Founder + CTO). Independent since 2010 (no VC, no PE — Sketch is fully bootstrapped and answers only to its customers).
**AI surface (verified live 2026-07-19):** Sketch AI — the Sketch MCP (Model Context Protocol) server that runs locally on the user's Mac and lets external AI agents (Claude Code + Claude Desktop + Cursor + VS Code + Codex + Antigravity + any MCP-compatible client) mutate Sketch documents. Concrete capabilities: theme-swap (light↔dark), fill-placeholders (replace lorem ipsum with context-aware content), tidy-documents (sort/rename/align layers + wrangle icon sets + keep Libraries clean), build-palette (drop a photo, get a full set of named color variables), build-designs-from-code (point your AI client at a repo, recreate text styles/colors/UI components/entire pages in Sketch), create-code-from-designs (take any frame, build it out in code with 1:1 visual fidelity). MCP server runs locally, off by default, user decides when to switch it on and what the AI client can see. MCP-compatible local models supported for fully on-device use.
**Distinct strategic posture:** Sketch is the ONLY cohort sibling with an explicit anti-AI-replacement stance ("We put designers at the heart of what we do, not AI"). Sketch is also the ONLY Dutch + EU-jurisdiction + 15-year-independent + no-VC-no-PE + MCP-server + local-only-by-default sibling in the cohort.
**Inbox:** privacy@sketch.com (canonical first-party; verified live). Also press@sketch.com + support via /support/contact/.
**Trust page:** sketch.com/security (GDPR + ISO 27001 + SAML SSO + TLS encryption + privacy-by-design + no-cookies-no-tracking posture + no third-party analytics). sketch.com/privacy (full GDPR-compliant privacy statement, right-to-update, right-to-complain to supervisory authority).
**Scale:** 1M+ active designers globally. Mac app since 2010. Recent Edinburgh release (July 2025) shipped Multi-paste + better gradients + faster Symbols + Web Command Bar + better notifications + the MCP server integration. Headquartered in The Hague, Netherlands. Two pricing options: one-time license (keep forever) or subscription (adds cloud storage + web-based collaboration).

---

## Cold email — 3-line personalized pitch (subject + body + signature)

**Subject:** Sketch MCP server audit wedge — AI-agent-mutates-Sketch-document provenance for the regulated EU buyer

Hi Sketch privacy team — quick note from Atlas.

The moment you turned on the Sketch MCP server, you opened a fundamentally new attack surface that no other design platform in the ai_design_tools cohort has: external AI agents (Claude Code, Claude Desktop, Cursor, VS Code, Codex, Antigravity) running locally on a designer's Mac and writing to live Sketch documents through a Model Context Protocol bridge. Every theme-swap Claude executes, every placeholder Cursor fills, every tidy-document Codex runs, every palette Antigravity extracts from a photo, every design-from-code VS Code extension regenerates, every create-code-from-designs MCP tool call returns — that's an AI-agent-initiated mutation of a Sketch document, and your EU regulated-industry buyers (financial-services + healthcare + pharma + legal + government) are going to ask for the same provenance trail every other EU GDPR + ISO 27001 design-platform buyer is asking for: *show me the audit trail from the MCP-client that triggered the action, through the prompt, the model version, the Sketch AI tool call, the document/layer/symbol/text-style/component/Library/theme/color-variable/canvas/frame/code-output mutation, the MCP-server-write propagation, and prove prompt-injection defense held up for untrusted MCP-client payloads + Claude Code conversations + Cursor prompts + VS Code extension calls + Codex prompts + Antigravity messages.*

That's exactly the wedge we sell. $500 for a 48-hour evidence-gap map across the Sketch MCP server + Sketch AI + Claude Code + Claude Desktop + Cursor + VS Code + Codex + Antigravity bridges — or $497/mo for a quarterly refresh that re-runs as the MCP server evolves.

Happy to send a 1-page scope and two recent EU GDPR + ISO 27001 design-platform references on request.

— Atlas
Talon Forge / Atlas Store
https://talonforgehq.github.io/atlas-store

---

## Why this lead (audit-wedge fit)

| Atlas wedge | Sketch surface it maps to |
|---|---|
| Design-source → Sketch-AI-MCP-server-prompt/model/version → Sketch-AI-plan → tool-call → document/layer/symbol/text-style/component/Library/theme/color-variable/canvas/frame/code-output mutation → MCP-client-write/Claude-Code-write/Cursor-write/VS-Code-write/Codex-write/Antigravity-write provenance | Sketch MCP server (theme-swap, fill-placeholders, tidy-documents, build-palette, build-designs-from-code, create-code-from-designs) |
| Prompt-injection defense for untrusted MCP-client payloads + Claude Code conversations + Cursor prompts + VS Code extension calls + Codex prompts + Antigravity messages | Sketch MCP server input validation + Claude Code + Claude Desktop + Cursor + VS Code + Codex + Antigravity bridges |
| Workspace/document/symbol-library/Library/data-residency isolation per SOC 2-equivalent + GDPR Art. 28 + ISO 27001 + ISO 27701 (Dutch + EU jurisdiction) | Sketch workspace hierarchy + Library scope + symbol-library scope + cloud-sync scope + local-only-default scope + EU data residency |
| Deletion/retention/rollback/version-history/MCP-server-write-evidence | Sketch version history + MCP-server write log + cloud-sync retention + local-only retention |
| Immutable human-approval evidence for MCP-server mutations + theme-swap + fill-placeholders + tidy-documents + build-palette + build-designs-from-code + create-code-from-designs + Claude Code writes + Cursor writes + VS Code writes + Codex writes + Antigravity writes | Sketch MCP-server permission model + human-in-the-loop approval + Claude Code write confirmation + Cursor write confirmation + VS Code write confirmation + Codex write confirmation + Antigravity write confirmation |
| Per-agent/per-model/per-tool-call/per-workspace/per-document/per-MCP-client/per-tenant cost attribution across Sketch MCP + Sketch AI + Claude Code + Claude Desktop + Cursor + VS Code + Codex + Antigravity bridges | Sketch MCP-server usage telemetry + Claude Code usage + Cursor usage + VS Code extension usage + Codex usage + Antigravity usage + subscription-billing breakdown |

**Founders (verified live 2026-07-19):** Pieter Omvlee (Co-Founder + CEO; founded 2010 in The Hague, Netherlands, ex-Neerlandse Spoorwegen developer) + Emanuel Sá (Co-Founder + CTO). Sketch has been independent since 2010 — no VC, no PE, answers only to its customers. Headquartered in The Hague, Netherlands.

**Vertical cohort position (ai_design_tools sibling #3):** Cohort opened with Canva 581 (ASX-listed $30B+ market cap + 220M+ MAU + Magic Studio + 95%+ F500) + Figma 582 (NYSE FIG post-IPO July 2025 + 13M+ MAU + 85% F500 + Dev Mode + Figma Make + 100+ integrations). Sketch 583 closes the public-company + private-company + EU-company triangulation of the ai_design_tools cohort. Distinct personas: ASX-listed design (Canva) + NYSE-listed design (Figma) + EU-jurisdiction independent design (Sketch).

**Cohort fit:** ai_design_tools, tier 1 — direct conversational-AI-agent audit wedge fit. Sketch is the cohort's EU-jurisdiction + Dutch + GDPR + ISO 27001 + independent-since-2010 + MCP-server + local-only-default + anti-AI-replacement wedge. The MCP server surface is uniquely auditable because every AI-agent-initiated mutation flows through a single well-defined tool-call surface — which means the audit wedge is fundamentally cleaner than Canva's Magic Studio (which has many opaque LLM calls) or Figma's Figma AI (which has a different prompt-to-prototype surface). EU regulated-industry buyers (financial-services + healthcare + pharma + legal + government) who are blocked on US-jurisdiction AI tools (F100 procurement, EU AI Act Aug 2 2026 GPAI Art. 53(d) deadline, Schrems II SCC concerns) get a clean alternative with Sketch.