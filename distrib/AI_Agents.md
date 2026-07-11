Built 3 production AI agents today by architecting on production-grade foundations. Sharing the build + the LLM loader bug that was killing every call silently.

**What I shipped (all live, all on GitHub Pages):**

1. **atlas-web-eyes** — built on a battle-tested 13-platform read/search engine. Read + search 13 platforms (Twitter, Reddit, YouTube, GitHub, Bilibili, XHS) for AI agents. CLI + MCP server.
2. **atlas-video-forge** — built on a battle-tested AI short-video engine. AI short video generator with auto-publish.
3. **atlas-stealth-browser** — built on a battle-tested undetectable browser stack. MCP server for undetectable browser automation.

All have hosted paid tiers ($29-99/mo) + free tier via my landing page.

**The 3-hour bug nobody tells you about:**

My engine was silently failing every LLM call because the loader was reading `MINIMAX_API_KEY` from .env but my .env has `MINIMAX_SUBSCRIPTION_KEY`. No errors, no logs, just dead air. Fixed by adding fallback to both names.

Store + free playbook: https://talonforgehq.github.io/atlas-store/

Looking for feedback on the production-grade engineering model — does it scale, or is it just noise?