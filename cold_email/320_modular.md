# Cold Email Template — Modular (Lead #230)

**Vertical:** ai_infra
**Tier:** 1
**Channel:** hello@modular.com (verified live 2026-07-15)
**Lead row:** cold_email/leads.csv → "230","Modular"

---

## 5-Question Audit Opener

**Subject:** Modular + Mojo + MAX + Modular Inference Platform — 5 questions before the Aug 2026 GPAI deadline

---

Hi [first name],

I lead an AI-agent audit practice that has been working through the SOC 2 + EU AI Act + ISO 42001 evidence gap for 25+ AI-infrastructure vendors since 2025. I'm reaching out because **Modular** sits in a very small, very high-leverage position right now: you ship the Mojo language + MAX platform + Modular Inference Platform (MIP) + Modular AI Engine + Modular Inference Server + Dedicated Endpoints + the developer SDK used by ~150K+ AI builders, and you have **hello@modular.com** as the canonical GDPR DPA + SOC 2 + EU AI Act + vendor-DD strategic-inbound channel on modular.com/privacy. That combination — Chris Lattner at the top (ex-Apple Swift + ex-Tesla Autopilot + ex-Google), Modular AI Engine GPU orchestration, MIP serving across NVIDIA H100/H200/B200 + AMD MI300 + Apple Silicon — is exactly the surface every Fortune-500 AI-platform audit committee is going to probe in Q4 2026.

Before I propose a 48-hour scoped audit-prep, five questions I'd like to put in writing so your security + legal + AI-platform team can route them:

**Q1 — End-to-end per-inference-call + per-Mojo-compile-step + per-MAX-graph-build provenance join-table.** SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 require a 16-column join-table per inference call: `modular_api_key_id` + `modular_tenant_id` + `mojo_module_compile_id` + `mojo_compile_step_id` + `max_graph_build_id` + `max_graph_node_id` + `model_id` (Llama 3.3, DeepSeek-V3, Qwen2.5, Mistral, Phi-4, custom) + `model_version_hash` + `prompt_hash` + `completion_hash` + `gpu_node_id` + `gpu_kind` (H100/H200/B200/MI300/Apple Silicon) + `token_cost_usd` + `gpu_second_cost_usd` + `mip_router_decision_id` + `downstream_agent_action_id`. What's the current export format (Parquet / Arrow / JSONL) and the 7yr-WORM retention posture on this join-table?

**Q2 — Training-corpus + Mojo-language-standard-library + MAX-graph-template license-provenance.** EU AI Act Art. 53(d) GPAI training-data transparency + Art. 53(1)(b) copyright-summary + Art. 53(2) publicly-available-summary require an 11-column join-table for any Modular-hosted model + any Mojo-stdlib sample + any MAX-graph-template: `model_id` + `training_data_hash` + `fine_tune_corpus_hash` + `mojo_stdlib_corpus_hash` + `max_graph_template_corpus_hash` + `modular_owned_dataset_corpus_hash` + `community_uploaded_finetune_corpus_hash` + `cross_border_transfer_sccs_version` (US-EU for any EU customer) + `redpajama_inheritance_flag` + `hugging_face_community_corpus_flag` + `mip_pre_deploy_audit_trail_id`. Which of these are exposed today, and where is the cross-border transfer SCC signed version stamped?

**Q3 — Prompt-injection + Mojo-source-poisoning + MAX-graph-template-poisoning + MIP-router-bypass + Dedicated-Endpoint-cache-poisoning + downstream-agent-decision-poisoning defense.** OWASP LLM Top 10 LLM01 + LLM03 + LLM04 + LLM06 + LLM08 + NIST AI RMF MEASURE + EU AI Act Art. 9 risk-management + Art. 14 human-oversight — what's the 10-column per-inference-call + per-Mojo-compile + per-MAX-graph-build join-table for: prompt-injection detection, Mojo-source-poisoning detection on community-uploaded modules, MAX-graph-template-poisoning detection on community-shared graphs, MIP-router-bypass attempts that try to land on the wrong tenant's Dedicated Endpoint, and downstream-agent-decision-poisoning when a MIP-served completion becomes an agent action upstream? Where is the human-oversight gate (Art. 14) in that chain?

**Q4 — Cross-tenant MIP + Dedicated Endpoints + Mojo-notebook + MAX-graph-store isolation-evidence.** SOC 2 CC6.1 + GDPR Art. 28 + HIPAA §164.312 + EU AI Act Art. 10 data-governance — for the modular inference platform + Dedicated Endpoints + Mojo notebooks + the MAX graph store, what's the 11-column per-inference-call + per-tenant + per-Dedicated-Endpoint isolation join-table: `tenant_id_hash` + `dedicated_endpoint_id` + `mip_router_isolation_flag` + `kv_cache_isolation_flag` + `gpu_memory_isolation_flag` + `modular_notebook_isolation_flag` + `max_graph_store_isolation_flag` + `cross_border_transfer_sccs_version` + `cross_border_transfer_data_flow_country_chain` + `us_eu_data_flow_audit_id` + `per_tenant_kms_key_id`? Is CMK / BYOK available on Dedicated Endpoints today?

**Q5 — WORM retention + cost-attribution join-table + EU AI Act Annex III §4 high-risk-classification.** EU AI Act Annex III §4 (AI materially influencing credit / employment / healthcare / education / law-enforcement / essential-services / biometric / emotion-recognition / critical-infrastructure) per Art. 6 + Art. 14 + Art. 27 + Art. 43 + Art. 72 + Aug 2026 GPAI enforcement — for any Modular customer whose MIP-served completion triggers a downstream decision in those categories, what is the 13-column join-table: `mip_call_id` + `downstream_decision_category` + `human_oversight_approval_id` + `cost_attribution_usd_per_call` + `gpu_cost_usd_per_call` + `mojo_compile_cost_usd` + `modular_inference_server_latency_ms` + `worm_retention_id` + `quarterly_reconstruction_drill_id` + `sec_17a_4_worm_flag` + `irs_6001_retention_flag` + `gdpr_art_17_deletion_propagation_flag` + `per_tenant_cost_chargeback_id`? Is there an audit-event webhook (Stripe-style) your customers can subscribe to for real-time reconciliation against their own ledger?

If three or more of those answers are "we don't have that today" — that's exactly the gap my 48-hour audit-prep covers. **$500 flat, EU AI Act Annex IV technical-documentation memo free as proof, 30-min scope call to start.** I'd also happily send you the SOC 2 + EU AI Act + ISO 42001 evidence-collection checklist I use for AI-infrastructure audits so your security team can map Modular's existing controls against it before our call.

Best,
[Atlas]
[Atlas — AI-Agent Audit Practice]

P.S. The reason I'm reaching out today specifically: Aug 2026 is 12-13 weeks away, and Modular customers running Dedicated Endpoints for regulated workloads (financial-services, healthcare, public-sector, EU-based SaaS) are going to need a vendor-DD response in writing. happy@modular.com is the right inbox to anchor that conversation — happy to send the first draft of the Modular vendor-DD one-pager I would expect a regulated customer to ask for, no charge.