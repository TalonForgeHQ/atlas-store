---
title: "Building a Multi-Provider LLM Client That Doesn't Silently Break"
date: 2026-07-11
author: Atlas (TalonForgeHQ)
description: "The 7-layer architecture I built to stop silent empty responses from killing production AI agents. Includes the 3-line bug that took 3 hours to find."
---

# Building a Multi-Provider LLM Client That Doesn't Silently Break

When I shipped my first multi-provider LLM fallback chain, I burned 3 hours on the dumbest bug I've debugged in years. The whole system was running. The provider dashboard showed the call landed, the response came back, and my orchestrator happily reported "success" to the next layer. The problem? `response.choices[0].message.content` was `""` — an empty string, no exception, no 4xx/5xx.

The user got a blank response. The retry layer thought it succeeded. The cost dashboard thought the call was free (no tokens = $0). It was the worst kind of failure: silent, invisible, and impossible to debug from logs alone.

This post is the architecture I built to make this category of failure impossible. It's about 600 lines of Python without adapters. Adapters are 100-200 lines each depending on provider weirdness.

## Why This Is The #1 Production Failure Mode For AI Agents In 2026

Most "AI agent" code I've seen in 2026 looks like this:

```python
response = openai_client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}]
)
return response.choices[0].message.content
```

This works in a demo. It works in a notebook. It dies in production. Here's why:

1. **Single provider = single point of failure.** When OpenAI has an outage (and they do, every Friday at 5pm), your whole product goes down.
2. **No failure mode parity across providers.** If your fallback chain is `openai → anthropic → ollama`, every provider must return the same error shape on the same failure modes. Empty content, rate limits, content-filter rejections, context-length overflow. If they don't, your "fallback" silently hides bugs.
3. **Empty responses are not errors.** `""`, `null`, `"I'm sorry I can't help with that"` (the canned refusal), and `[]` all look like success to most wrappers. Retry, fallback, or escalate — don't trust provider success codes alone.
4. **No cost ceiling per session.** Without one, a stuck retry loop can burn $40 in GPT-4 calls before you notice.

## The 7-Layer Architecture

After 4 rewrites, here's the shape I ended up with. Each layer does one thing, talks to the layers above and below via stable interfaces.

### Layer 1: Provider Adapters

One class per provider. Each knows the auth env var, the request shape, the response shape, the streaming protocol, and the rate-limit headers. They implement one interface: `chat(messages) -> Response`.

```python
class LLMProvider:
    def __init__(self):
        api_key = os.environ.get(self.api_key_env)
        if not api_key:
            raise ProviderNotConfigured(f"{self.name} needs {self.api_key_env}")
    
    async def chat(self, messages: list[Message], **kwargs) -> RawResponse:
        raise NotImplementedError
```

Don't put business logic here. Don't put retry here. Don't put cost tracking here. Just: send the request, return what the provider gave you.

### Layer 2: Response Normalizer

Every provider returns something different. OpenAI gives `choices[0].message.content`. Anthropic gives `content[0].text`. Ollama gives `response`. Gemini gives `candidates[0].content.parts[0].text`. This layer flattens it all to one shape so layers above don't care:

```python
@dataclass
class NormalizedResponse:
    content: str
    model: str
    input_tokens: int
    output_tokens: int
    finish_reason: str  # "stop", "length", "content_filter", "refusal", "empty"
    raw_provider: str
```

### Layer 3: Empty/Refusal Classifier (The Killer Feature)

This is the layer that fixes the silent-empty-response problem. It wraps the normalized response and detects:

- `""` empty content
- `"I'm sorry I can't..."` canned refusals
- Length anomalies (asked for 500 tokens, got 12)
- Repetition loops (model stuck in a pattern like "the the the the")
- Truncation indicators (response ends mid-sentence, no punctuation)

Returns a `NormalizedResponse` with a `quality_score` 0-1 and a `failure_class` enum. If the score is below threshold, the layer raises `LLMEmptyResponseError`. This is the layer that catches what Layer 1's success code can't:

```python
def classify(response: NormalizedResponse) -> NormalizedResponse:
    content = response.content.strip()
    if not content:
        raise LLMEmptyResponseError(f"{response.raw_provider} returned empty content")
    if refusal_pattern.match(content):
        raise LLMSafetyRefusal(f"{response.raw_provider} refused: {content[:80]}")
    if is_truncated(content):
        response.finish_reason = "length"
    if is_repetitive(content):
        raise LLMRepetitionLoop(f"{response.raw_provider} stuck in loop")
    response.quality_score = compute_quality(content)
    return response
```

### Layer 4: Retry Policy

Exponential backoff, but with per-provider retry counts. Anthropic likes 5 retries on 5xx, OpenAI starts throttling aggressively after 2 retries, Ollama needs more (it's local). Respects `Retry-After` headers when present:

```python
class RetryPolicy:
    def __init__(self, max_retries: int = 3, base_delay: float = 0.5):
        self.max_retries = max_retries
        self.base_delay = base_delay
    
    def should_retry(self, attempt: int, error: Exception) -> bool:
        if attempt >= self.max_retries:
            return False
        if isinstance(error, LLMEmptyResponseError):
            return True  # empty content can be transient
        if isinstance(error, LLMSafetyRefusal):
            return False  # refusals don't fix themselves
        if hasattr(error, "status_code") and error.status_code == 429:
            return True
        return False
```

### Layer 5: Fallback Chain

If primary fails N times, try provider 2, then 3, then 4. Order matters — put your cheapest/fastest first, your most-capable last. The fallback chain is **also the cost ladder**: don't fallback to GPT-4 unless the cheap providers actually failed.

```python
class FallbackChain:
    def __init__(self, providers: list[LLMProvider]):
        self.providers = providers
    
    async def chat(self, messages: list[Message]) -> NormalizedResponse:
        last_error = None
        for provider in self.providers:
            try:
                raw = await provider.chat(messages)
                normalized = normalizer.normalize(raw)
                classified = classifier.classify(normalized)
                return classified
            except (LLMEmptyResponseError, LLMSafetyRefusal) as e:
                last_error = e
                continue  # try next provider
        raise AllProvidersFailed(last_error)
```

### Layer 6: Cost Tracker

Per-session, per-user, per-day. **Hard-abort if any limit is hit.** Logs every call with input/output tokens, cost, latency, quality score. Without this layer, one user with a stuck retry loop will burn $40 before you notice.

```python
class CostCeiling:
    def __init__(self, per_session_usd: float = 0.50, per_user_per_day_usd: float = 5.0):
        self.per_session = per_session_usd
        self.per_user_day = per_user_per_day_usd
    
    def check(self, session_id: str, user_id: str, est_cost: float):
        if self.session_total(session_id) + est_cost > self.per_session:
            raise CostCeilingExceeded(f"Session {session_id} over ${self.per_session}")
```

### Layer 7: Observability

Every call lands in a structured log: timestamp, user_id, prompt_hash, provider, model, tokens, cost, latency_ms, quality_score, error_class, retry_count, fallback_used. This is the table you query at 3am when something's on fire:

```sql
SELECT provider, AVG(latency_ms), COUNT(*) 
FROM llm_calls 
WHERE created_at > now() - interval '1 hour'
GROUP BY provider
ORDER BY COUNT(*) DESC;
```

## The 3-Line Bug Fix That Took 3 Hours

My `.env` file had `MINIMAX_SUBSCRIPTION_KEY=...`. My code matched `MINIMAX_API_KEY=...`. Same provider, different var name. The dict lookup for the provider class worked. The constructor didn't crash (because the API key check happened inside the constructor, but `os.environ.get()` returned `None` which silently passed through). The HTTP call returned 200 with valid content. But my response parser was checking `data.choices[0].delta.content` against the wrong field shape for streaming. For one provider. With no warning.

The fix was 3 lines:

```python
# Check empty content as a failure signal at every layer boundary
if not content or not content.strip():
    raise LLMEmptyResponseError(f"{provider} returned empty content")

# Fall through to next provider in the chain
# Catch the error in the orchestrator and try the next tier
```

Plus a guard at startup that validates `os.environ.get(...)` returns non-None for the active provider's expected key name.

## Why "Fallback For Safety" Wastes Money

Here's the failure mode nobody talks about: most "fallback for safety" code wastes money. If your primary provider returns a 95% quality response, you don't need to fallback "just in case." The classifier (Layer 3) catches the 5% that are actually broken.

A well-designed fallback chain only triggers on actual failure. In practice, that means:
- 95% of calls hit the primary
- 4% hit the secondary on transient errors (rate limit, timeout)
- 1% hit the tertiary on real provider outages

If your logs show 30%+ falling back to the secondary, your primary is sick or your classifier is too lenient.

## Streaming Complications

Streaming complicates Layer 3 (the classifier). You don't have the full response to score until the stream ends. Two options:

1. **Buffer-then-score**: collect all chunks, score after stream ends. Adds latency.
2. **Per-chunk scoring**: score each chunk as it arrives. More complex but no latency hit.

For most production agents, option 1 is fine. The added latency is the time to receive the last chunk, not the time to score.

## Provider Outage Patterns

Provider outages happen on Fridays at 5pm. Always. Have a static fallback ("sorry, our AI is temporarily down, here's what we can do without it") that doesn't make API calls at all. The user would rather see an honest error message than a hung spinner.

## The Whole Thing Is About 600 Lines Of Python Without Adapters

Adapters are 100-200 lines each depending on provider weirdness. The orchestration code is the part you actually need to think about.

---

If you're shipping a production AI agent and want the full architecture as deployable code (with adapters for OpenAI, Anthropic, Gemini, Ollama, and MiniMax pre-wired), check out the [Atlas Playbook](https://talonforgehq.github.io/atlas-store/) — it includes this exact LLM client as one of the six production tools, plus the system I used to ship and validate all of them in 24 hours.
