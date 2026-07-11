# 103_galileo.md — Galileo AI (rungalileo.com)

**To:** founders@rungalileo.com (Vikram Chatterji, CEO)
**Subject:** Your eval-rubric versioning is the SOC 2 + EU AI Act Art. 15 gap auditors are asking about
**Vertical:** ai_eval

---

Hi Vikram,

Quick read on Galileo's public material — Luna-2 (the hallucination-evaluation model), Pulse (RAG quality monitoring), and the ChainPoll multi-judge consensus layer are excellent on the eval-metric side. The Galileo Hallucination Index (RAGTruth + HaluEval + HaluEval-WT) is the canonical reference dataset for the field.

The 2026 audit gap that none of the public material addresses: **when Galileo IS the eval layer the buyer's SOC 2 + EU AI Act Article 15 (accuracy, robustness, cybersecurity) auditor inspects, the eval-rubric versioning, golden-set line of provenance, hallucination-judge LLM model-card + temperature-pin at audit time, and the ChainPoll multi-judge consensus trail all need WORM evidence.**

The 5 questions an SOC 2 CC7.2 + EU AI Act Article 15 + GDPR Art. 22 auditor is asking Galileo this quarter:

1. **Eval-rubric versioning** — when the judge prompt template changes from v3.2 to v3.3, can you replay every past eval call against the rubric version that was live at eval time? (most eval platforms lose the rubric-at-eval-time binding)
2. **Golden-set line of provenance** — the 200-question golden set you ship with Galileo — does it carry the source-document IDs + the source-system ACL snapshot at the time the golden set was authored? (because the auditor will ask: "when this golden-set answer was judged correct, was the source document the user was supposed to be able to see?")
3. **Hallucination-judge model-card + temperature-pin** — if Luna-2 is itself an LLM, the auditor needs (a) the exact model version + checkpoint SHA at audit time, (b) the temperature pin (= 0 by convention), (c) the system prompt SHA. Galileo Pulse shipping today logs the judge model but not the checkpoint SHA.
4. **ChainPoll consensus-trail evidence** — the 3-judge or 5-judge ChainPoll pattern is great for accuracy, but the WORM evidence row needs (judge_id, model_version, prompt_template_SHA, raw_vote, weight, consensus_decision, latency_ms, cost_usd) per query, not just the consensus decision.
5. **Eval-on-eval audit trail** — when the buyer's customer asks "why did Galileo flag this answer as a hallucination in production on 2026-04-12?" the auditor needs the full re-runnable pipeline: judge prompt + model version + golden-set reference + ChainPoll trace + token-level attribution back to the source chunk.

We do $500/48h audits that walk through exactly these 5 questions for AI-eval platforms. Reference architecture for fixing Q1-Q5 in production: S3 Object Lock + per-eval-call join-table with the model-card + temperature-pin + rubric-version all bound to a single immutable record. Engineering cost: 1 platform engineer + 2 weeks to ship.

Worth a 30-min call? I can show you the 5-question worksheet we use and the WORM-evidence schema we recommend for ChainPoll.

— Atlas
Atlas Store · talonforgehq.github.io/atlas-store

P.S. If your customers are asking about SOC 2 Type II + EU AI Act Article 15 conformity assessment in 2026, the gap Q3 (model-card + temperature-pin at audit time) is the one most agent-platform vendors we audit have not closed. Galileo's Pulse logging already has most of the data — it's a pipeline-shape fix, not a model retrain.