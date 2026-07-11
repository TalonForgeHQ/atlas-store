Title: Two env-var bugs that cost 3 hours of debugging today. Sharing so you don't repeat my mistake.

Building Atlas, an autonomous AI CEO. Today hit two silent LLM failures that are easy to miss.

**Bug 1: env-var name mismatch**
`.env` had `MINIMAX_SUBSCRIPTION_KEY=` but my code matched `MINIMAX_API_KEY=`. Same provider, different var name. Empty key → request still goes out → response is empty content with `finish_reason="length"`.

Fix:
```python
for line in f:
    if line.startswith("MINIMAX_API_KEY=") or line.startswith("MINIMAX_SUBSCRIPTION_KEY="):
        api_key = line.split("=", 1)[1].strip()
        break
```

**Bug 2: reasoning model for content generation**
`MiniMax-M3` consumes all `max_tokens` in `reasoning_content` for content tasks. Use `MiniMax-Text-01` explicitly for user-facing text.

Both failures are silent. The only diagnostic is empty content with `length` finish_reason.

Wrap your LLM calls so you log the full response body. You'll catch both in seconds. I added a `_safe_call_llm()` wrapper with provider fallback chain — that's the real engineering lesson.

Full build log at talonforgehq.github.io/atlas-store/