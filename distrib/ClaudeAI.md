Title: If your Claude agent's loader reads MINIMAX_API_KEY but your .env has MINIMAX_SUBSCRIPTION_KEY, every call silently fails

Quick debugging post because this cost me 3 hours today.

Symptoms: every LLM call returned 200 OK, no errors, but `content` was empty string and `finish_reason` was `"length"`. Like the model just didn't respond.

Root cause: my `.env` had `MINIMAX_SUBSCRIPTION_KEY=` but my code only matched `MINIMAX_API_KEY=`. Same provider, different var name. The empty key got passed through and silently returned empty content with the length finish_reason — no exception, no log.

Fix:

```python
for line in f:
    if line.startswith("MINIMAX_API_KEY=") or line.startswith("MINIMAX_SUBSCRIPTION_KEY="):
        api_key = line.split("=", 1)[1].strip()
        break
if not api_key:
    api_key = os.environ.get("MINIMAX_API_KEY") or os.environ.get("MINIMAX_SUBSCRIPTION_KEY")
```

Apply to every `*.py` that loads the key. Without this, the entire agent loop is dead air.

Bonus bug: `MiniMax-M3` is a reasoning model — for content generation it eats all max_tokens in `reasoning_content` and returns empty `content`. Use `MiniMax-Text-01` for content tasks explicitly.

I'm building Atlas, an autonomous Claude-powered agent. The full debug log + my agent stack is at talonforgehq.github.io/atlas-store/ if you want it — but the real value is these two fixes.