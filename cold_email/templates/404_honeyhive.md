Subject: HoneyHive SOC 2 CC7.2 trace-provenance audit — 5 questions Dhruv will get asked

Hi Dhruv,

Five questions you'll get at the next SOC 2 Type II walkthrough on HoneyHive Observability that your current docs don't fully answer:

1. **Per-trace-id → per-billing-event-id lineage.** HoneyHive generates per-trace-id → per-span-id → per-LLM-call-id → per-tool-call-id → per-eval-id lineage. When the auditor asks "show me every per-span-id associated with tenant X in Q3-2026 and reconcile it against the per-billing-event-id record", can your team answer that from one query, or does it require joining HoneyHive Observability + HoneyHive Billing + HoneyHive Datasets exports?

2. **OpenAI Agents SDK + Claude Agent SDK + LangGraph auto-instrumentation across LiteLLM proxies.** HoneyHive's open-source SDK instruments 15+ frameworks. When an agent routes an LLM-call through a LiteLLM proxy, does the per-LLM-call-id → per-prompt-template-version-id → per-completion-id → per-token-id lineage survive the proxy hop, or does the proxy re-mint the per-LLM-call-id?

3. **Per-evaluator-output-poisoning + per-judge-output-poisoning defense.** HoneyHive Evaluation ships per-evaluator-id → per-evaluator-prompt-id → per-evaluator-model-id → per-evaluator-output-id → per-rubric-id lineage. How does the system detect when an attacker poisons per-evaluator-output-id between per-LLM-call-id and per-eval-id? What is the per-evaluator-output-confidence-score floor that triggers human review?

4. **Cross-tenant isolation evidence for HoneyHive Cloud Free + Pro + Enterprise + Dedicated + OSS-self-hosted.** Drata trust-center (app.drata.com/trust/9cc7ede3-...) shows SOC 2 Type II + GDPR + HIPAA. When the auditor requests cross-tenant isolation evidence per SOC 2 CC6.1 + GDPR Art. 28 + EU AI Act Art. 10, what is the audit-package you hand over?

5. **WORM retention + cost-attribution for HoneyHive Cloud Pro + Enterprise.** EU AI Act Annex III 4 high-risk classification per Art. 6+14+27+43+72 + Aug 2026 GPAI enforcement. Does HoneyHive Cloud retain per-LLM-call-token-cost + per-eval-cost + per-judge-call-cost with WORM retention, or does that data live in a separate cost-attribution pipeline?

I run a $500 / 48-hour audit on ai_eval_observability vendors (Braintrust, Confident AI, Patronus, Arize, HoneyHive, Maxim, Honeycomb) — at the end you get a 6-page overlap map showing where your per-trace-id surface duplicates or extends the canonical chain, plus a written gap-list against SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4. Happy to do the HoneyHive slice as a free pilot if you want to see the shape before scoping.

If useful: 30-min call this week? Otherwise, just reply with which audit gap is highest-priority and I'll send the matching template.

— Atlas Talon Forge LLC
   atlas-store / talon-forge persona
   ai_eval_observability audit practice

P.S. Cited Dhruv Patel (Co-Founder & CEO) + Ken Collins (Co-Founder & CTO) + $7.4M Seed 2024 from Hyperlink + Commas Capital + NYC HQ + 500+ engineering-team customer base + SOC 2 Type II + GDPR + HIPAA + Drata trust-center + OpenAI Agents SDK + Claude Agent SDK + LangGraph + Mastra + LlamaIndex + DSPy + AWS Bedrock + Vertex AI integrations + MCP server. The 5-vendor overlap map (Braintrust → Confident AI → Patronus → Arize → HoneyHive) is yours whether we work together or not.
