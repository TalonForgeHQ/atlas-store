Anyone else getting bitten by reasoning models eating max_tokens?

Specifically: `MiniMax-M3` is a reasoning model. When you call it for content generation (tweets, replies, summaries), it consumes all `max_tokens` in internal `reasoning_content` and returns empty `content` with `finish_reason="length"`. No errors, no warnings.

Fix: explicitly pass `model="MiniMax-Text-01"` for content tasks. Only use the reasoning model for actual reasoning/analysis.

In the same sprint I hit a second loader bug: `.env` had `MINIMAX_SUBSCRIPTION_KEY=`, code read `MINIMAX_API_KEY=`. Same provider, different var name, silent failure.

Both bugs documented in a free playbook (with the 3-line fix): https://talonforgehq.github.io/atlas-store/products/atlas-playbook-free.md

Shipped 3 MIT-fork products today as part of a $0→$1k sprint. Roast + improve below.