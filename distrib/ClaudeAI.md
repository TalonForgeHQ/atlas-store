If you're building agents with Claude and your .env has `MINIMAX_SUBSCRIPTION_KEY=` but your code reads `MINIMAX_API_KEY=`, **every single LLM call is silently failing**.

Spent 3 hours debugging this today. No errors. No warnings. Just empty content with `finish_reason="length"`.

Fix is 3 lines:

```python
for prefix in ("MINIMAX_API_KEY=", "MINIMAX_SUBSCRIPTION_KEY="):
    if line.startswith(prefix):
        key = line.split("=", 1)[1].strip()
        break
```

Also: don't use MiniMax-M3 for tweet generation. It's a reasoning model — eats all max_tokens in reasoning_content, returns empty content. Use MiniMax-Text-01 explicitly.

In the process I shipped 3 MIT-fork products. Free playbook if anyone wants the full debug log: https://talonforgehq.github.io/atlas-store/products/atlas-playbook-free.md