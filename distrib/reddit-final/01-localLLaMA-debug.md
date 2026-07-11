Title: Spent 3 hours today on a silent LLM loader bug. Posting the autopsy so you don't.

I shipped a multi-provider LLM client today (Ollama → OpenAI → Anthropic → fallback chain) and burned 3 hours on the dumbest bug.

**Symptom:** Every LLM call returned empty content string. No exception. No 4xx/5xx. The provider dashboard showed the request landed, the response came back, but `response.choices[0].message.content` was `""`.

With the recent HN threads about AI agents bankrupting operators + deleting databases, I figured this autopsy might help.

**What I had:**
```python
class LLMClient:
    def __init__(self):
        provider = os.environ.get("LLM_PROVIDER", "openai")
        self.impl = {
            "openai": OpenAIClient,
            "anthropic": AnthropicClient,
            "ollama": OllamaClient,
            "minimax": MiniMaxClient,
        }[provider]()
```

**What was wrong:** My MiniMax provider was reading `os.environ["MINIMAX_API_KEY"]`. My `.env` file had `MINIMAX_SUBSCRIPTION_KEY=...` (different name). The dict lookup worked, the constructor didn't crash, the HTTP call returned 200 with valid content, but my response parser was checking `data.choices[0].delta.content` against the wrong field shape for streaming. For one provider. With no warning.

**Why this is nasty:**
1. Provider-level fallbacks meant the failure only surfaced on the LAST tier of the chain
2. Empty content passed my "did this fail?" check because I was only checking for `None` and exceptions, not empty string
3. Tests passed because they mocked the response, not the env var

**The 3-line fix:**
```python
# Check empty content as a failure signal
if not content or not content.strip():
    raise LLMEmptyResponseError(f"{provider} returned empty content")

# Fall through to next provider in the chain
# Catch the error in the orchestrator and try the next tier
```

Plus a guard at startup that validates `os.environ.get(...)` returns non-None for the active provider's expected key name.

**The deeper lesson:** When you have N providers behind one interface, a silent empty-content return is worse than a 500. Your retry logic treats it as success, your idempotency layer thinks it's a duplicate, and your cost dashboard thinks the call was free (no tokens = $0).

For everyone shipping multi-provider agents in 2026 — the silent failure is the #1 way you go broke or corrupt data without knowing.

Anyone else hit this with multi-provider fallback chains? Curious how others handle the "provider succeeded but returned garbage" case — that's the case my old single-provider code never had to think about.