Title: 7 things I check before shipping any LLM-powered product to real users

Built and shipped a few AI tools this week (none of which are the point of this post). After the third "works on my machine, breaks in prod" incident, I wrote down what I actually check now before flipping the switch. Sharing because I wish someone had given me this list 6 months ago.

1. **Failure mode parity across providers.** If your code does `provider_a → provider_b → provider_c` fallback, every provider must return the same error shape on the same failure modes. Empty content, rate limits, content-filter rejections, context-length overflow. If they don't, your "fallback" silently hides bugs.

2. **Cost ceiling per session.** Pick a number (mine is $0.50) and hard-abort if a single user session exceeds it. Without this, one user with a stuck retry loop will burn $40 in GPT-4 calls before you notice.

3. **Idempotency on every write path.** Webhooks fire twice. Users double-click. Your agent retries. If "create record" isn't idempotent, you double-charge customers. Use `Idempotency-Key` headers, hash the inputs, whatever.

4. **Manual handoff paths are features, not bugs.** Where humans still need to touch the system is where the highest-ROI automation lives. Don't hide it. Surface it. Make it easy. A "human review required" button that's 1 click away is better than an autonomous loop that silently makes bad decisions.

5. **Empty responses are errors.** Treat `""`, `null`, `"I'm sorry I can't help with that"` (the canned refusal), and `[]` all as failures. Retry, fallback, or escalate. Don't trust provider success codes alone.

6. **Log the prompt that caused the failure, not just the response.** When something breaks at 3am, the question isn't "what did the model say" — it's "what did I ask it." Log prompts with PII redaction.

7. **Ship with a kill switch.** A single env var that flips the whole system into read-only / static / "show the user an apology" mode. The day you need it, you need it in 30 seconds, not 30 minutes.

The hardest one for me was #4. I kept trying to automate the last 10% and shipping worse products. Now I just put a "human-in-the-loop" button on the edge cases and let the human hit it when needed.

What's on your pre-shipping checklist that I missed?