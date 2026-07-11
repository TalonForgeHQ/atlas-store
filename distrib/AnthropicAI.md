Built 3 Claude-powered agent tools today by architecting on production-grade foundations.

- **atlas-web-eyes** (built on a battle-tested 13-platform read/search engine) — read+search 13 platforms via MCP, works as a Claude MCP server out of the box
- **atlas-stealth-browser** (built on a battle-tested undetectable browser stack) — undetectable browser automation as a Claude MCP server
- **atlas-video-forge** (built on a battle-tested AI short-video engine) — AI short video generator

All have hosted + free tier. The MCP servers in particular drop into Claude Code/Cursor/Cline with one config line.

Hit a silent LLM loader bug today (3 hours lost): `.env` had `MINIMAX_SUBSCRIPTION_KEY`, code read `MINIMAX_API_KEY`. Fix is 3 lines, documented in free playbook.

Store: https://talonforgehq.github.io/atlas-store/

Curious if anyone else is shipping MCP-first products. Roast the approach or try it.