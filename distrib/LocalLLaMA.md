Title: MiniMax provider env-var mismatch silently breaks every call. Reasoning model eats max_tokens for content. Two bugs, 3 hours lost.

Posting both because I hit them back-to-back today and want to save others the time.

**Bug 1 — loader mismatch**

`.env` had `MINIMAX_SUBSCRIPTION_KEY=...`, code matched `MINIMAX_API_KEY=...`. Same provider, different env var name. Empty key passed through, request still went out (different failure mode), response was empty content with `finish_reason="length"`.

Fix:
```python
for line in f:
    if line.startswith("MINIMAX_API_KEY=") or line.startswith("MINIMAX_SUBSCRIPTION_KEY="):
        api_key = line.split("=", 1)[1].strip()
        break
if not api_key:
    api_key = os.environ.get("MINIMAX_API_KEY") or os.environ.get("MINIMAX_SUBSCRIPTION_KEY")
```

**Bug 2 — reasoning model for content**

`MiniMax-M3` is a reasoning model. For content generation (summarize, tweet, classify, anything user-facing) it consumes all `max_tokens` in `reasoning_content` and returns empty `content`. Fix: explicit `model="MiniMax-Text-01"` for content chains.

Both failures are silent. Wrap your LLM calls so you log the response body to stderr — you'll catch both in seconds.

I'm running an autonomous local-stack agent. Build log + the wrapper: talonforgehq.github.io/atlas-store/