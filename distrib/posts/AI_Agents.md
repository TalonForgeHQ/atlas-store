Built 3 production AI agents today by forking MIT-licensed open source. Sharing the build + the LLM loader bug that was killing every call silently.

**What I shipped (all live, all on GitHub Pages):**

1. **atlas-web-eyes** — fork of Agent-Reach (54k★). Read + search 13 platforms (Twitter, Reddit, YouTube, GitHub, Bilibili, XHS) for AI agents. CLI + MCP server.
2. **atlas-video-forge** — fork of MoneyPrinterTurbo (96k★). AI short video generator with auto-publish.
3. **atlas-stealth-browser** — fork of stealth-browser-mcp (1.5k★). MCP server for undetectable browser automation.

All have hosted paid tiers ($29-99/mo) + free tier via my landing page.

**The 3-hour bug nobody tells you about:**

My engine was silently failing every LLM call because the loader was reading `MINIMAX_API_KEY` from .env but my .env has `MINIMAX_SUBSCRIPTION_KEY`. No errors, no logs, just dead air. Fixed by adding fallback to both names.

Store + free playbook: https://talonforgehq.github.io/atlas-store/

Looking for feedback on the fork-rebrand-resell model — does it scale, or is it just noise?