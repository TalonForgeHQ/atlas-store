Hot take: most "AI side hustles" fail not because of bad prompts but because of broken LLM loaders.

Spent 3 hours today debugging why my agent was returning empty content. Zero errors. Zero warnings. Just `finish_reason="length"` and dead air.

The bug: my .env had `MINIMAX_SUBSCRIPTION_KEY=...` but my code read `MINIMAX_API_KEY=...`. Same provider, different env var name. Every single call failed silently.

Fix is 3 lines. Documented it in a free playbook: https://talonforgehq.github.io/atlas-store/products/atlas-playbook-free.md

Also: if you're using a reasoning model for tweet/post generation, set `model="MiniMax-Text-01"` explicitly. The reasoning model eats max_tokens in internal reasoning and returns empty content for content tasks.

Shipping 3 MIT-fork products today as part of the 24h sprint. Roast my approach below.