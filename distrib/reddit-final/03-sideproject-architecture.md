Title: Architecture for a 7-layer LLM client (when OpenAI alone isn't enough)

If you're building anything beyond a demo, you'll eventually need this. Sharing the shape I ended up with after 4 rewrites.

**Layer 1: Provider adapters.** One class per provider. Each knows the auth env var, the request shape, the response shape, the streaming protocol, and the rate-limit headers. They implement one interface: `chat(messages) -> Response`.

**Layer 2: Response normalizer.** Every provider returns something different. OpenAI gives `choices[0].message.content`. Anthropic gives `content[0].text`. Ollama gives `response`. This layer flattens it to one shape so layers above don't care.

**Layer 3: Empty/refusal classifier.** Wraps the normalized response. Detects:
- `""` empty content
- `"I'm sorry I can't..."` canned refusals
- Length anomalies (asked for 500 tokens, got 12)
- Repetition loops (model stuck in a pattern)

Returns a `NormalizedResponse` with a `quality_score` 0-1.

**Layer 4: Retry policy.** Exponential backoff, but with per-provider retry counts (Anthropic likes 5 retries, OpenAI starts throttling at 2). Respects `Retry-After` headers when present.

**Layer 5: Fallback chain.** If primary fails N times, try provider 2, then 3. Order matters — put your cheapest/fastest first, your most-capable last.

**Layer 6: Cost tracker.** Per-session, per-user, per-day. Hard-abort if any limit is hit. Logs every call with input/output tokens, cost, latency, quality score.

**Layer 7: Observability.** Every call lands in a structured log: timestamp, user_id, prompt_hash, provider, model, tokens, cost, latency_ms, quality_score, error_class, retry_count, fallback_used. This is the table you query at 3am when something's on fire.

**Two things that saved me:**
- **Prompt caching is layer 2, not layer 7.** Cache the normalized response, not the raw provider response. Otherwise provider-specific quirks leak in.
- **The fallback chain is also the cost ladder.** Don't fallback to GPT-4 unless the cheap providers actually failed. Don't fallback at all if the quality_score from the primary is fine — most "fallback for safety" code wastes money.

**Two things that hurt me:**
- **Streaming complicates layer 3.** You don't have the full response to score until the stream ends. Either buffer + score (adds latency) or score per-chunk (more complex).
- **Provider outages happen on Fridays at 5pm.** Have a static fallback ("sorry, our AI is temporarily down, here's what we can do without it") that doesn't make API calls at all.

The whole thing is about 600 lines of Python without the adapters. Adapters are 100-200 each depending on provider weirdness.

What's your LLM client architecture? Especially curious if anyone has solved the streaming + quality-scoring problem better than buffer-then-score.