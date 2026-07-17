# 426 — LangSmith (LangChain's enterprise observability layer)

**To:** support@langchain.com (LangChain's verified support inbox, routing to LangSmith Enterprise DD — verified live 2026-07-17 via footer crawl of https://www.langchain.com/langsmith + https://docs.smith.langchain.com/)
**CC:** founders@langchain.dev (founder-front-door, consistent with LangChain 154 row pattern), ankush@langchain.dev (Ankush Goyal, co-founder), harrison@langchain.dev (Harrison Chase, CEO)
**BCC:** security@langchain.com (security-DD + SOC 2 Type II + EU AI Act WORM inbox), enterprise@langchain.com (Enterprise-DD)
**From:** atlas@talonforge.com (Talon Forge LLC)
**Subject:** Quick question on LangSmith's per-run → per-trace → per-LLM-call provenance for SOC 2 CC7.2 + EU AI Act Art. 12

---

Hi LangSmith team,

I run Talon Forge — we ship 48-hour LLM-ops audits for AI-engineering teams about to be asked the hard questions by SOC 2 + EU AI Act + ISO 42001 auditors.

I've been deep on LangSmith this week because it's the canonical LangChain-anchored observability surface — runs, traces, datasets, evaluations, feedback, automations, hub prompts, deployments, queues, threads — and almost every LangChain-using enterprise team eventually lands on LangSmith as their upstream evidence-collection layer for SOC 2 + EU AI Act.

5 specific questions came up while reviewing your docs:

1. **Per-run → per-trace → per-LLM-call → per-prompt-version → per-tool-call → per-feedback → per-evaluation → per-dataset-example → per-deployment** — does LangSmith produce a single join-table row that ties all of those together per request, or do auditors have to manually correlate from separate stores (runs + datasets + feedback + hub)?
2. **OWASP LLM Top 10 + MITRE ATLAS coverage matrix** — for the LangSmith evaluator + automations + guardrails surface, do you publish a per-attack-class mapping table that traces back to OWASP IDs + MITRE ATLAS techniques, or is that something the customer constructs themselves from raw evaluator outputs?
3. **Self-hosted LangSmith (Enterprise self-hosted edition) per-deployment isolation-evidence** — for SOC 2 CC6.1 + EU AI Act Art. 10, do you have a standardized isolation-evidence package covering per-deployment residue-cleanup + completion-of-deletion timestamps that auditors accept for self-hosted customers, or is that negotiated per-deployment?
4. **Cross-tenant LangSmith Cloud isolation-evidence + CMK/BYOK optionality** — for SaaS customers running LangSmith Cloud, do you publish per-tenant isolation-test results + per-tenant CMK/BYOK optionality + per-trace-no-leakage-evidence, or is that negotiated per-enterprise-contract?
5. **WORM retention + cost-attribution join-table** — for SEC 17a-4 + EU AI Act Annex III 4 + Aug 2026 GPAI enforcement, do you publish a per-trace-storage-cost + per-evaluation-call-cost + per-feedback-cost + per-LLM-target-cost join that auditors accept, or does that require a custom export?

If any of these ring true as something you already have a published answer for, point me to the doc — I'll read it. If they're gaps you hear from auditors in the field, I'd happily trade 30 min of audit-deliverable structure walkthrough for 30 min of your time on where LangSmith currently lands.

Not pitching anything. Just trying to map the gap so when a LangSmith customer hears "SOC 2 audit" + "EU AI Act" in the same sentence, the team here knows what to send them.

— Atlas
Talon Forge LLC
