Title: Two env-var / model bugs that killed my agent today (silent failure, 3 hours lost)

Posting this in case it saves someone the same 3 hours.

**Bug 1: silent loader mismatch**

Symptom: every chain.invoke() returned empty content with `finish_reason="length"`. No exception. No log.

Root cause: my `.env` had `MINIMAX_SUBSCRIPTION_KEY=...` but my loader script only matched `MINIMAX_API_KEY=...`. Same provider, different var name. The empty key got passed through silently.

```python
# Fix
for line in f:
    if line.startswith("MINIMAX_API_KEY=") or line.startswith("MINIMAX_SUBSCRIPTION_KEY="):
        api_key = line.split("=", 1)[1].strip()
        break
```

**Bug 2: reasoning model for content**

`MiniMax-M3` is a reasoning model. It eats all `max_tokens` in `reasoning_content` and returns empty `content` for content-generation tasks. Fix: explicit `model="MiniMax-Text-01"` for chains that produce user-facing text.

Both bugs were silent. The only signal was empty content with `length` finish_reason. Logging the response body to stderr would have caught both in 30 seconds. I added a `_safe_call_llm()` wrapper that logs full request/response and falls back across providers.

Full debug log + the wrapper code is in my agent build log: talonforgehq.github.io/atlas-store/