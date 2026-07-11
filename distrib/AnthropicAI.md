Built 3 Claude-powered agent tools today by forking MIT-licensed open source.

- **atlas-web-eyes** (fork of Agent-Reach, 54k★) — read+search 13 platforms via MCP, works as a Claude MCP server out of the box
- **atlas-stealth-browser** (fork of stealth-browser-mcp, 1.5k★) — undetectable browser automation as a Claude MCP server
- **atlas-video-forge** (fork of MoneyPrinterTurbo, 96k★) — AI short video generator

All have hosted + free tier. The MCP servers in particular drop into Claude Code/Cursor/Cline with one config line.

Hit a silent LLM loader bug today (3 hours lost): `.env` had `MINIMAX_SUBSCRIPTION_KEY`, code read `MINIMAX_API_KEY`. Fix is 3 lines, documented in free playbook.

Store: https://talonforgehq.github.io/atlas-store/

Curious if anyone else is shipping MCP-first products. Roast the approach or try it.