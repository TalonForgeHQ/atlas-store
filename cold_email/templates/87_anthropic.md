# Cold Email — Anthropic (AI safety)

**Subject:** Anthropic's own AI agent + SOC 2 Type II scope question

Hi Dario,

Meta question for Anthropic's compliance team: when Anthropic's SOC 2 Type II covers Claude.ai (the chat product) and the Anthropic API, does it cover Claude Code's autonomous agent loop — the `npx @anthropic-ai/claude-code` flow that reads files, runs commands, edits code, opens PRs?

The agent loop has a fundamentally different threat model than the API: it's persistent across hours, makes dozens of tool calls per session, and writes to user filesystems. SOC 2 CC6.1 (logical access) and CC7.2 (monitoring) want different controls here than the chat product.

I run a 48-hour **AI Agent Compliance Audit** ($500, Stripe). Maps Claude Code's agent loop to SOC 2 + the new OWASP Top 10 for LLM Applications 2026. 12-page report with specific control evidence.

Worth a look before your next Type II audit?

— Atlas (Talon Forge)