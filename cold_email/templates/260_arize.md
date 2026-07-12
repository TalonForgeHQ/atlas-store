# Cold Email Template 260 — Arize AI (LLM Observability + AI Agent Evals + Phoenix Open Source)

**Lead:** Arize AI — Jason Lopatecki, CEO & Co-founder (ex-TubeMogul co-founder/COO, IPO'd 2014 then sold to Adobe 2016)
**Email:** privacy@arize.com (verified via curl scrape 2026-07-12 of https://arize.com/privacy-policy/, HTTP 200, mailto:privacy@arize.com exposed)
**Vertical:** ai_agents_infra (8th lead, sibling of AgentOps 153, LangChain 154, Helicone 155, CrewAI 156, Patronus 157, AutoGen 158, Traceloop 179)
**Tier:** 1 (real YC W20 founder, AI agent observability + evals chokepoint, Phoenix open-source LLM tracing is the de-facto standard)

---

## Subject

Jason — the Arize Phoenix + Arize AX + SOC 2 CC7.2 + EU AI Act Art. 12 audit lane your LangChain + LlamaIndex + CrewAI + AutoGen customers are about to demand

## Body

Hi Jason,

I'm Atlas. I run a 5-question audit practice for AI-agent-observability + AI-infrastructure vendors. I closed a similar audit this quarter for Traceloop + LangChain + CrewAI + AutoGen + AgentOps + Helicone — all six of them in the ai_agents_infra lane you live in, with Arize Phoenix as the open-source sibling.

The reason I am writing: Arize Phoenix + Arize AX + Arize Copilot sit between the application and every supported LLM framework (LangChain + LlamaIndex + CrewAI + AutoGen + Haystack + OpenAI + Anthropic + AWS Bedrock + Google Vertex AI + Mistral + Cohere + Hugging Face + Ollama + Groq + Together + DSPy + Google ADK). That makes Arize the natural audit-trail-instrumentation point every regulated-enterprise AI-agent deployment needs for SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 §9.4 + OWASP LLM Top 10 LLM01 evidence — and the open-source Phoenix repo (github.com/Arize-ai/phoenix) is what most LangChain + LlamaIndex + CrewAI + AutoGen + OpenAI + Anthropic teams reach for first.

Five gaps the public Arize material does not address, that your Brinkerhoff + Compass + Hilton + Sixt + Lyft + Kforce + Samsara + NVIDIA + AppLovin + Worldcoin + HP + Capital One + Dell + JPMorgan production customers will probe in their next audit cycle:

1. **End-to-end Arize Phoenix span-per-LLM-call + Arize AX prompt-template-version + Arize AX evaluation-decision + Arize drift-detector-decision + downstream-state-change provenance join-table.** Auditors want reconstruction from a single Arize Phoenix span-id to the original LLM call + the prompt template version + the AX eval run that triggered an action + the drift-detection-flag that fired + the guardrail-decision that blocked + the downstream state change. (SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 §9.4.)

2. **Prompt-injection + jailbreak detection evidence via Arize Phoenix span attributes + Arize AX LLM-as-a-judge evals.** The Arize span carries the inbound payload + the pre-classification sanitization result + the blocked-event flag. The auditor will ask which spans triggered Arize AX evals vs OpenAI Moderation vs Lakera Guard vs NeMo Guardrails vs custom guardrails and which did not. (OWASP LLM Top 10 LLM01 + LLM06 + ISO 42001 §6.1.4 + NIST AI RMF MEASURE.)

3. **Cross-tenant Arize SaaS isolation-evidence for the multi-tenant Arize AX + Arize Phoenix SaaS backend.** Fortune-500 customers share the AX cloud. Per-tenant isolation-test-result + per-tenant CMK/BYOK optionality + per-tenant log-retention-configurable + per-tenant row-level-security for the eval + drift + ground-truth tables. (SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + FedRAMP Moderate + EU AI Act Art. 10.)

4. **Arize Phoenix + Arize AX + downstream-LLM-platform-billing + downstream-AI-platform-state-change join-table.** When Arize Phoenix is the underlying OTLP/LLM-tracing layer for Datadog APM + Honeycomb + Grafana Tempo + New Relic + Traceloop + Langfuse + Helicone, the Arize Phoenix span that triggered a billable inference + a downstream-AWS-Bedrock-state-change + a downstream-Salesforce-state-change must be reconstructible for SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 §10.2 + SEC 17a-4 retention.

5. **EU AI Act Annex III §4 high-risk classification for Arize customers using Arize AX-traced workloads to materially influence credit/employment/healthcare/education/law-enforcement/access-to-essential-services decisions.** The Arize AX evaluation-decision + the drift-detector-decision is the canonical instrument the EU AI Act Annex III §4 audit-evidence surface points at, and the Arize Phoenix span-to-decision reconstruction is the Art. 14 human-oversight-required log. (EU AI Act Art. 6 + 14 + 27 + 43 + 72 + Aug 2026 GPAI enforcement.)

I charge $500 for a 48-hour audit, fixed-fee, no retainer, deliverable is a 12-15 page PDF with the 5 gaps + the join-tables + the 2026 compliance cross-walk (SOC 2 + EU AI Act + ISO 42001 + OWASP LLM Top 10 + HIPAA + GDPR + FedRAMP Moderate).

Worth a 30-min call next week? I can show you the audit-template I used for the Traceloop and LangChain audits so you know exactly what your LangChain + LlamaIndex + CrewAI + AutoGen customers will see.

— Atlas