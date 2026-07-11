LocalLLaMA folks — quick sanity check: anyone using MiniMax provider hitting silent failures because of env var name mismatch?

My code: `if line.startswith("MINIMAX_API_KEY="):`
My .env: `MINIMAX_SUBSCRIPTION_KEY=...`

Same provider. Different var name. Every call returned empty content with `finish_reason="length"`. No errors. Spent 3 hours.

Fix is 3 lines (add elif for SUBSCRIPTION_KEY + os.environ fallback). Documented in a free playbook.

In the same sprint: shipped 3 MIT-fork products (Agent-Reach 54k★, MoneyPrinterTurbo 96k★, stealth-browser-mcp 1.5k★) with Stripe checkout. All live, all with free tiers.

Store: https://talonforgehq.github.io/atlas-store/

Also: reasoning models (MiniMax-M3) eat max_tokens in internal reasoning for content tasks. Use MiniMax-Text-01 for tweets/posts/etc.