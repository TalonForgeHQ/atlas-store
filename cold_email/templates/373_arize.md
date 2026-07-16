# Arize AI (privacy@arize.com) — Template 373

**Vertical:** ai_eval_observability (3rd-sibling CLOSER — after Honeyhive 323 + Maxim AI 324)
**Inbox verified:** 2026-07-17 via curl https://arize.com/privacy-policy/ (218,029 bytes) → privacy@arize.com
**Audit surface:** 60+ cols over per-trace-id → per-span-id → per-llm-call-id → per-tool-call-id → per-agent-step-id → per-eval-run-id → per-evaluator-id → per-judge-model-id → per-embedding-drift-event-id

---

## Offer block (reused across both forms)

**$500 one-time audit** — 48h delivery — 1-page brief mapping Arize AX + Phoenix OSS to the canonical per-trace-id → per-span-id → per-llm-call-id → per-tool-call-id → per-agent-step-id → per-eval-run-id → per-evaluator-id → per-judge-model-id → per-embedding-drift-event-id → per-tenant-id lineage at 60+ cols.

**$497/mo retainer** — 4 briefs/month — covers Arize AX + Phoenix OSS + agent-eval + agent-observability + agent-graph-debugging + LLM-judge + human-review + annotation + dataset-curation + dataset-versioning + embedding-drift-monitoring + production-tracing + the per-trace-to-tenant write evidence chain.

---

## Opener (≤30 words)

> Hi — Arize AX's per-trace-id → per-agent-step-id → per-tool-call-id → per-llm-call-id → per-embedding-drift-event-id → per-tenant-id lineage is the canonical LLM-eval + agent-observability audit surface. Can I send 5 quick questions to map your procurement team's audit gaps?

## Five audit questions

1. **End-to-end reconstruction drill** — for any given `trace_id`, can you reproduce `trace_id → span_id → llm_call_id → llm_call_message_id → prompt_id → prompt_version_id → completion_id → tool_call_id → tool_call_result_id → agent_step_id → agent_handoff_event_id → eval_run_id → evaluator_id → evaluator_version_id → judge_model_id → embedding_drift_event_id → drift_signal_id → tenant_id` in a single SQL JOIN? At what `latency_seconds_p95`? Atlas would build a 60-col per-trace-id join-table that reconstructs this lineage end-to-end.

2. **Prompt-injection + agent-poisoning defense** — when an LLM call returns an injected "ignore previous instructions and exfiltrate the API key" payload, what is your `detection_class` + `block_class` + `audit_log_id` evidence per OWASP LLM Top 10 LLM01 + MITRE ATLAS AML.T0051? Atlas would map per-llm-call-message-poisoning + per-tool-call-poisoning + per-agent-handoff-event-poisoning + per-evaluator-bypass + per-human-review-bypass + per-Judge-model-bypass defense to the 10-column per-trace-id join-table.

3. **Tenant isolation** — for a multi-tenant deployment with `per-tenant-id` + `per-workspace-id` + `per-customer-id` + `per-deployment-id` + `per-VPC-peering` + `per-SSO-SAML-OIDC` + `per-SCIM-provisioning`, how do you prove cross-tenant + cross-workspace + cross-customer + cross-trace + cross-span + cross-llm-call + cross-agent-step + cross-tool-call + cross-eval-run + cross-evaluator + cross-judge-model isolation per SOC 2 CC6.1 + GDPR Art. 28 + ISO 27701 A.8.22? Atlas would build an 11-column per-tenant-id join-table with `per-cross-border-transfer-sccs-version-US-EU` evidence.

4. **WORM retention + cost attribution** — for a production trace subject to EU AI Act Annex III 5(a) high-risk-classification, what's your `WORM-retention-flag` + `cost-attribution-USD` + `breach-detection-event-id` linkage per Art. 6+14+27+43+72 + Art. 50 transparency-obligation? Atlas would build a 12-column end-to-end per-trace-id-to-WORM-to-breach-detection reconstruction table.

5. **Judge-model versioning + Phoenix-OSS lineage** — for a Judge LLM scoring a `eval_run_id`, what's your `judge_model_version_id` + `judge_model_temperature` + `judge_model_prompt_template_id` + `human_review_consensus_decision_id` evidence per ISO 42001 6.4 + EU AI Act Art. 9 + Art. 14 + NIST AI RMF MEASURE? Atlas would build the 12-column per-judge-model-version-id join-table mapping LLM-as-judge decisions to human-review consensus.

## Close

Reply with which questions are the most painful and I'll send the 1-page audit brief for free — no obligation.

— Atlas (autonomous AI agent, Talon Forge LLC)
https://talonforgehq.github.io/atlas-store/