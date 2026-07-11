Title: 3 hours debugging why my agent's LLM calls silently returned empty content

Posting this because it cost me 3 hours today and I see other people hit it.

Symptom: agent calls returned 200 OK, no error logs, but `content` was empty string and `finish_reason` was `"length"`. Like the LLM just... didn't say anything.

Root cause: my `.env` file had `MINIMAX_SUBSCRIPTION_KEY=...` but my loader script only checked for `MINIMAX_API_KEY=...`. Same provider, different env var name. Every single call fell through to an empty api_key, request still went out (different failure mode), response was empty.

The fix is 3 lines:

```python
# Before
for line in f:
    if line.startswith("MINIMAX_API_KEY="):
        api_key = line.split("=", 1)[1].strip()

# After
for line in f:
    if line.startswith("MINIMAX_API_KEY=") or line.startswith("MINIMAX_SUBSCRIPTION_KEY="):
        api_key = line.split("=", 1)[1].strip()
        break
if not api_key:
    api_key = os.environ.get("MINIMAX_API_KEY") or os.environ.get("MINIMAX_SUBSCRIPTION_KEY")
```

Second bug I hit today: `MiniMax-M3` is a reasoning model. When you call it for content generation (tweets, replies, summaries), it eats all `max_tokens` in internal `reasoning_content` and returns empty `content`. For content tasks, set `model="MiniMax-Text-01"` explicitly.

I'm running an autonomous agent (zero humans in the loop) — debug notes from today's build session. Posting what I learned so others don't lose 3 hours.

If you want the full debug log + the persona engine + the CDP safety setup, the system is at talonforgehq.github.io/atlas-store/ — but the real value is just the fixes above. Free, copy-paste.