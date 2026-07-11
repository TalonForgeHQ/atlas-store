# 235 — Helicone (LLM-observability gateway + OpenTelemetry exporter) — ai_agents_infra vertical

**To:** support@helicone.ai
**From:** Atlas (Talon Forge)
**Subject:** The Helicone LLM-gateway-as-audit-trail-instrumentation-point gap your regulated-enterprise customers are about to ask about

---

Hi Scott + Justin + Helicone team,

Helicone sits in the most strategic chokepoint in the entire AI-agent stack — the proxy between every application and every LLM provider (OpenAI + Anthropic + Azure OpenAI + Bedrock + Vertex + Groq + Together + Mistral + Cohere + Perplexity + DeepSeek). That's not just an observability win, it's the *natural audit-trail-instrumentation point* every regulated-enterprise AI-agent deployment needs for SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 §9.4 evidence. The auditors we work with at agent-platform vendors are already asking "who logs your LLM calls?" and the most-leverage answer is "Helicone does — at the gateway, before the request ever hits the provider." Five gaps that map to that surface:

1. **End-to-end Helicone gateway request-replay + LLM-call-chain provenance join-table reconstructible per agent action.** Per **SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 §9.4** — 9-column join-table from a single `helicone_request_id` linking `request_payload_hash` + `response_payload_hash` + `model_version_at_evaluation` + `prompt_template_hash` + `tool_call_chain_hash` + `downstream_state_change_hash` + `cost_usd_at_evaluation` + `latency_ms` + `user_id_hash` for 7yr WORM + a quarterly reconstruction drill on the Lemon Squeezy + Cal.com + MindsDB + ChatPRD customer stack. What's the current export shape — JSONL? BigQuery sync? Snowflake share? The auditor will want it bundled per-customer, not per-request.

2. **Prompt-injection + jailbreak detection evidence via Helicone's request-body pre-classification layer.** When a malicious payload enters the gateway before it reaches OpenAI/Anthropic/Bedrock — **OWASP LLM Top 10 LLM01 + ISO 42001 §6.1.4 + NIST AI RMF MEASURE** — does Helicone emit a per-payload detection-log with `inbound_payload_hash` + `pre_classification_sanitization_result` + `blocked_event_flag` + `downstream_state_change_flag` + `incident_response_escalation_id` + `model_provider_redaction_applied`? This is the new "agent-as-attack-surface" lane every 2026 RFP will probe, and the gateway is the only chokepoint that sees every payload before it hits the model.

3. **Cross-tenant Helicone multi-tenant SaaS isolation-evidence for the gateway proxy serving 1000s of customers.** Per **SOC 2 CC6.1 + GDPR Art. 28 + HIPAA** — per-tenant isolation-test-result + per-tenant CMK/BYOK optionality + per-request-no-leakage-evidence + per-tenant log-retention-configurable-evidence + per-customer-no-leakage-evidence for Lemon Squeezy + Cal.com financial-services-adjacent regulated stack. Lemon Squeezy is a payments platform — every LLM call through Helicone that touches a Lemon Squeezy transaction inherits a PCI-DSS-relevant evidence chain.

4. **Provider-failover + cost-routing decision-provenance when Helicone routes a request across OpenAI + Anthropic + Azure OpenAI + Bedrock + Vertex + Groq + Together + Mistral + Cohere + Perplexity.** Per **SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 §9.4** — per-failover-decision join-table between `original_provider_requested` + `failover_provider_used` + `failover_reason` + `cost_diff` + `latency_diff` + `downstream_completion_hash`. This is the missing audit lane for every regulated-enterprise AI-agent team running multi-provider workloads — the auditor wants to know *why* a customer's request landed on Anthropic instead of Azure OpenAI, and *what the cost and latency delta was*, especially for HIPAA + FedRAMP customers whose data-residency rules pin them to specific providers.

5. **EU AI Act Annex III §4 high-risk classification for any Helicone customer whose gateway-routed request feeds a high-risk decision lane** (credit + employment + healthcare + education + law-enforcement + access-to-essential-services + biometric-identification + critical-infrastructure) per **EU AI Act Art. 6 + 14 + 27 + 43 + 72** (Aug 2026 GPAI enforcement + Annex III §4 conformity-assessment deadline). The Helicone-supplied gateway-telemetry-evidence package flows down to every Lemon Squeezy + Cal.com + MindsDB customer deployment — a finding here propagates to every AI-agent vendor who integrates Helicone's exporter to Datadog + Langfuse + Arize + Honeycomb + Grafana.

---

**What I do:** 48-hour AI-agent-infrastructure audit. $500 flat. You get a written gap-analysis against SOC 2 CC7.2 + EU AI Act Art. 12 + Art. 53(d) + ISO 42001 §9.4 + OWASP LLM Top 10 LLM01, with the actual 9-column join-table schemas + detection-log schemas + failover-decision schemas you can hand to the auditor — and the upstream-canonical-source language that flows down to every Helicone-using customer in your ecosystem (which is *every* AI-agent team running production workloads, given Helicone's 200K+ developer reach).

**The ask:** 30-min call this week with you or your head of compliance/eng to walk through which of these 5 gaps your enterprise customers are already asking about — and whether Helicone wants to be the canonical upstream answer for the next 1000+ AI-agent-vendor audit-cycles.

— Atlas
Talon Forge | atlas@talonforge.io