# Cold Email Template 251 — Voiceflow (ai_agents_infra 15th sibling)

**Lead:** Voiceflow — `security@voiceflow.com` (canonical ai_agents_infra inbox pattern, consistent with Sierra 170 / Vellum 169 / Humanloop 166 / Langfuse 161 / LangChain 154)
**Vertical:** ai_agents_infra (15th sibling: AgentOps 153 + LangChain 154 + Helicone 155 + CrewAI 156 + Patronus 157 + AutoGen 158 + Arize 159 + Portkey 160 + Langfuse 161 + Traceloop 163 + LlamaIndex 165 + Humanloop 166 + Vellum 169 + Sierra 170)
**Audit lens:** SOC 2 CC7.2 + EU AI Act Art. 12/Art. 14/Art. 50/Annex III §4 + ISO 42001 §9.4 + OWASP LLM Top 10 LLM01/LLM06 + GDPR Art. 28 + CCPA/CPRA + FTC Section 5
**Offer:** $500/48h audit + 15-min call

---

**Subject:** the conversational-AI-agent-design-platform audit gap your OpenView + Felicis + $30M + Braden Ream-built Voiceflow stack will hit before Q4 2026

Hi Voiceflow team (Braden) —

I run a 48h audit practice focused on AI-agent design-platform vendors serving enterprise customer-experience + support + product teams with EU AI Act Aug 2026 conformity-assessment deadlines. Voiceflow's conversational-AI-agent-design surface (agent-flow-diagram + knowledge-base-integration + NLU-intent-classification + multi-channel-deploy + handoff-to-human + downstream-state-change) is the cleanest "AI-agent-design-platform-for-non-developer-enterprise-builders" audit-target I've seen — your platform lets regulated customers (financial-services + healthcare + telecom + SaaS) ship customer-facing agents without engineering a from-scratch LLM-pipeline, so the audit-evidence consolidation story is uniquely tight.

5 audit gaps your public material doesn't address:

(1) **End-to-end Voiceflow agent-flow + agent-diagram-version + NLU-intent-classification + downstream-channel-state-change provenance join-table.** Every enterprise CX customer will need per-conversation reconstruction from a single `voiceflow_agent_flow_id` linking the agent-flow-diagram-version + the NLU-intent-classification-decision + the knowledge-base-retrieval-source + the agent-response-hash + the channel-deploy-target (chat-widget / voice-IVR / Slack / Microsoft Teams / WhatsApp / custom-API) + the handoff-to-human-trigger-decision + the downstream-state-change. SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 §9.4 + 12-column reconstruction + 7yr WORM + quarterly reconstruction drill.

(2) **Voiceflow agent-diagram-version-control + NLU-intent-classification + multi-channel-deploy audit-trail.** SOC 2 CC7.3 + EU AI Act Art. 12 + 9-column per-agent-flow-version join-table (voiceflow_agent_flow_version_hash + agent_diagram_version_hash + nlu_intent_classification_hash + knowledge_base_retrieval_hash + multi_channel_deploy_target_hash + rollback_decision_hash + eval_run_id + score_distribution + hallucination_rate). The unique Voiceflow lane because the agent-diagram-version-control + NLU-intent-classification + multi-channel-deploy is the non-developer-builder control surface that no other ai_agents_infra sibling ships in the same enterprise-conversational-AI-design-platform form.

(3) **Cross-tenant Voiceflow Workspace isolation-evidence for the multi-tenant SaaS serving enterprise CX teams.** SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + EU AI Act Art. 10 + CCPA/CPRA. Per-tenant CMK/BYOK optionality + per-agent-flow-no-leakage + per-knowledge-base-no-cross-tenant-leakage + per-conversation-no-cross-tenant-leakage + completion-of-deletion timestamp — the auditor will specifically probe the agent-flow-diagram + knowledge-base isolation as the natural multi-tenant SaaS audit-instrumentation surface, especially for the financial-services + healthcare customers whose customer-PII flows through every agent turn.

(4) **Voiceflow agent-flow + NLU-intent-classification + knowledge-base-retrieval training-corpus + fine-tune license-provenance.** EU AI Act Art. 53(d) GPAI training-data transparency + Art. 53(1)(b) copyright-summary + Art. 53(2) publicly-available-summary + customer-conversation-data-IP-license complexity. 10-column per-source join-table (source_license_type + source_copyright_holder + source_attribution_chain + source_copyleft_flag + license_collision_flag + downstream_model_derivative_use + customer_conversation_consent_flag + customer_conversation_data_retention_classification). Aug 2026 GPAI enforcement deadlines propagate to every Voiceflow-using customer.

(5) **EU AI Act Annex III §4 high-risk-classification + Art. 50 transparency-obligation for Voiceflow agents in financial-services + healthcare-payer + telecom lanes.** 12-column end-to-end Voiceflow-conversation-to-high-risk-decision reconstruction (voiceflow_agent_flow_id + agent_diagram_version + nlu_intent_classification_decision + knowledge_base_retrieval_source + agent_response_hash + handoff_to_human_decision + downstream_high_risk_state_change + high_risk_jurisdiction_classification + cost_usd_at_decision + latency_ms + regulatory_retain_until). The customer-facing agent-design-platform lane is the natural Art. 50 transparency-obligation surface — every regulated-decision the agent makes (account-disclosure + payment-modification + healthcare-appointment + service-cancellation) must cite its source-agent-flow-diagram-version + source-knowledge-base-retrieval per Art. 50.

The audit pitch: $500 for a 48h structured evidence-package audit (12-column join-tables per audit gap above + the EU AI Act Art. 50 transparency-obligation + Art. 14 human-oversight + Art. 53(d) GPAI training-data transparency evidence consolidation pattern + the SOC 2 CC6.1 + CC7.2 + CC7.3 cross-tenant + per-conversation + per-agent-flow-version evidence-package template that maps 1:1 to the Aug 2026 audit-cycle requirement for every Voiceflow-using enterprise CX customer in financial-services + healthcare-payer + telecom + SaaS).

15-min call works — what's your team's audit-prep window looking like for Q4 2026?

Best,
Atlas
Talon Forge LLC
security@voiceflow.com → `privacy@voiceflow.com` (cc'd)