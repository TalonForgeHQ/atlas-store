---
lead: 538
vendor: Arize AI
vertical: ai_observability
cohort_sibling: Honeycomb 102 + Galileo 103 + Maxim 425 + LangSmith 426 + LangWatch 421 + Comet 424 + Patronus 469
founder: Aparna Dhinakaran (Co-Founder + CPO); Jason Lopatecki (Co-Founder + CEO)
hq: Berkeley CA (founded 2019, ex-Engineers at Uber + Facebook AI + Google Brain)
customers: Fortune 500 AI/ML platform teams + frontier-model builders + regulated-industry AI deployers across US + EU + APAC
mailtos_verified: support@arize.com (live 2026-07-19 on docs.arize.com)
positioning: AI observability + LLM tracing + eval + drift + agent-monitoring + prompt-engineering + Phoenix open-source
engagement_offer: $500 fixed-fee 48h audit / $497/mo retainer
---

**Subject:** Arize AI + the LLM eval + agent-tracing SOC 2 CC7.2 + EU AI Act Art. 12 join-table gap every Fortune 500 GRC will ask about in 2026

Hi Aparna,

Your Phoenix OSS adoption across 100K+ developers + the Fortune 500 AI/ML platform team footprint + the Arize AX enterprise eval + agent-monitoring + prompt-engineering surface means Arize is now the canonical AI-observability layer in the LLM-evidence path of every regulated Fortune 500 AI deployment in 2026. The audit question every SOC 2 Type II + ISO 42001 + ISO 27701 + EU AI Act Art. 12 auditor will ask Arize is: **does the trace + eval layer reconstruct the agent's decision end-to-end with cryptographic binding back to the model version + prompt version + retrieval version + tool-call version?**

Here are 5 audit gaps that the public material doesn't address but that every Fortune 500 GRC + AI-governance-committee + EU AI Act Art. 12/14 auditor will ask Arize to evidence in 2026:

1. **End-to-end per-trace provenance join-table** — SOC 2 CC7.2 + EU AI Act Art. 12 (logging + traceability) + ISO 42001 §9.4 + ISO 27701 require that the per-trace join-table be exportable on demand, 7-year WORM retention, with a quarterly cold-storage reconstruction drill. The 13-column join: (trace_id, span_id, agent_id, model_id, model_version_id, prompt_template_id, prompt_template_version_id, retrieval_query_id, retrieval_corpus_id, retrieval_chunk_id, tool_call_id, tool_response_id, eval_score_id, eval_judge_id, eval_rubric_id, audit_log_entry_id, residency_region_id). Without (a)-(n) cryptographically bound, the firm cannot answer a regulator's question about which prompt + retrieval + tool call + eval rubric produced which AI decision for which customer in which region.

2. **Per-eval-judge + per-rubric + per-prompt-template version-control evidence** — EU AI Act Art. 14 (human oversight) + ISO 42001 §6.1.4 (AI system lifecycle — versioned training data) + ABA Model Rule 1.1 (competence — the auditor must know which eval rubric was applied) require that each eval-judge + rubric + prompt-template be version-pinned with cryptographic binding to the trace that used it. When the rubric drifts (LLM-judge upgraded, prompt-template updated, retrieval-corpus refreshed), the audit artifact must surface the version-delta so a regulator can attribute an eval-score to the exact rubric that produced it.

3. **Cross-region + cross-tenant trace residency isolation** — SOC 2 CC6.1 + GDPR Art. 28 (processor controls) + Schrems II SCC + EU-US DPF + APPI + PH DPA require that traces be partitionable per-region (US, EU, UK, APAC) + per-Arize-tenant + per-customer with per-tenant KMS keys (CMK/BYOK) + per-region retention rules. Audit artifact: per-region + per-tenant + per-customer trace-partition manifest + per-region KMS-key-rotation log + per-region Schrems-II-cross-border-transfer-provenance + EU AI Act Aug 2 2026 GPAI training-data transparency.

4. **Hostile-input + eval-poisoning + rubric-poisoning defense** — OWASP LLM Top 10 LLM01/03/06/08 + MITRE ATLAS + EU AI Act Art. 14 human-oversight + Art. 50 transparency-obligation + 12-state AI disclosure require that Arize detect + flag (a) prompt-injection attempts ingested into the eval set, (b) poisoned eval-judges producing inflated accuracy scores, (c) poisoned rubrics that systematically suppress hallucination flags, (d) tool-call replay attacks against the agent-tracing layer, (e) trace-tampering attempts against the WORM evidence store. Audit artifact: per-trace hostile-input classifier score + per-eval-judge anomaly log + per-rubric integrity hash + tool-call replay-detection log + WORM-evidence-store integrity proof.

5. **Agent-trace ↔ business-outcome cryptographic binding** — SOC 2 CC8.1 (change management) + FRCP 34 (production in discovery) + EU AI Act Art. 12 + SEC 17a-4 WORM + ISO 42001 require that each agent-trace be cryptographically bound to the downstream business-outcome (a customer-support resolution, a fraud-block, an underwriting decision, a contract-execution, a medical-coding decision) so that an auditor can reconstruct which AI decision produced which downstream consequence for which customer. Audit artifact: per-trace ↔ per-business-outcome cryptographic binding manifest + per-decision downstream-effect log + 7-year WORM retention.

I'm running a 48-hour, fixed-price **$500 audit** that delivers all five artifacts as a working reference implementation + the per-trace 13-column join-table + the eval-judge + rubric version-control evidence + the cross-region trace-partition manifest + the hostile-input classifier + the agent-trace ↔ business-outcome cryptographic binding + a one-page memo for your QSA + ISO 42001 + EU AI Act conformity auditor. References: chunks 34 (SOC 2 AI agent), 39 (permission inheritance), 100 (Arize baseline), 102 (Honeycomb), 103 (Galileo), 105 (Moveworks) — all live at talonforgehq.github.io/atlas-store.

Worth a 30-min call this week?
