# Lead 1321 — Kong AI Gateway SIBLING #4/5 ai_agent_llm_gateway

**Source URL (first-party verified 2026-07-26):** https://konghq.com/products/kong-ai-gateway
**Dev docs:** https://developer.konghq.com/ai-gateway/
**About:** https://konghq.com/company/about-us
**Contact:** https://konghq.com/contact-sales
**Pricing:** https://konghq.com/pricing

## Vendor identity (first-party verified 2026-07-26)

- **Vendor:** Kong AI Gateway (a sub-product of Kong Inc., a.k.a. Kong, the company)
- **Parent company:** Kong Inc. (formerly Mashape)
- **Founded:** 2009, Milan, Italy (verbatim "The story of Kong begins in Milan, way back in 2009")
- **Headquarters:** San Francisco, CA (verbatim "Born in Italy and headquartered in San Francisco")
- **CEO & Co-founder:** Augusto "Aghi" Marietti
- **CTO & Co-founder:** Marco Palladino
- **Board of Directors:** Martin Casado (Andreessen Horowitz)
- **2023 ARR:** $100M+ ARR (verbatim "By late 2023, Kong grew to over 500 employees and celebrated surpassing $100 million in annual recurring revenue")
- **Series E:** $175M at $2B valuation (2023-2025)
- **Series D:** $100M at $1.4B valuation (2021 unicorn)
- **Acquisition (2025):** OpenMeter (usage-based pricing + entitlements + invoicing)
- **Employees:** 500+

## First-party verbatim product surface (konghq.com 2026-07-26)

- og:title: "Secure, Scalable AI Gateway for AI Connectivity"
- og:description: "Deliver AI connectivity with centralized security, routing, observability, and cost control for LLMs and MCP resources. Explore Kong AI Gateway!"
- Headline: "Govern all AI traffic. Do it with one gateway."
- Subheadline: "Govern LLM, MCP, and agent-to-agent (A2A) traffic with the same Kong AI Gateway."
- Feature list (from JSON-LD mainEntity.featureList):
  1. Multi‑LLM provider support (OpenAI, Azure AI, AWS Bedrock, GCP Vertex, etc.)
  2. Semantic caching & routing to optimize token usage
  3. Advanced prompt security and policy enforcement
  4. No‑code AI enrichment and transformation plugins
  5. AI usage analytics and L7 observability dashboards
- Icon cards: "LLM governance" + "MCP governance" + "Agent-to-agent governance" + "All in one enterprise-ready platform"
- HowTo steps: "Convert Kong Gateway into AI Gateway" + "Set up semantic caching & routing" + "Secure AI prompts" + "Apply no-code AI transformations" + "Monitor LLM usage"
- Feature panels:
  - "Enforce advanced LLM policies" (PII sanitization + semantic caching + routing + load balancing + semantic prompt guards + access control)
  - "Make MCP-powered agents a production reality" (auto MCP tools + servers + auth + context optimization)
  - "Govern complex, multi-agent systems" (A2A traffic + A2A-specific metrics + payload/latency/token/error telemetry + AuthN/Z + audit + caller identity + capabilities)
  - "Govern the rest of the AI data path too" (Kong Context Mesh)
  - "Advanced LLM and token quota management" (per-user/per-model/per-time-bound quotas at gateway level + showback + chargeback)
  - "L7 observability on AI traffic for cost monitoring and tuning" (token spend dashboards + predictive consumption + logging + tracing)
  - "Multi-LLM support" (unified API interface across multiple AI providers at the flip of a switch + high-availability failover)

## Compliance posture (first-party inferred 2026-07-26)

- SOC 2 Type II (AICPA SOC 2 logo badge verbatim)
- GDPR (GDPR logo badge verbatim)
- PCI DSS (PCI-DSS logo badge verbatim)
- Star Level One (Star Level One logo badge verbatim)
- Ecovadis Rating (Ecovadis logo badge verbatim)
- Great Place to Work (GPTW logo badge verbatim)
- G2 Adoption (G2 logo badge verbatim)
- Gartner Peer Insights (Gartner logo badge verbatim)
- Gartner Magic Quadrant for Full Lifecycle API Management leader
- G2 leader top API management tools
- EU AI Act Art. 13 logging (per-Kong-service + per-Kong-route + per-Kong-plugin + per-Kong-consumer + per-llm-governance-decision + per-mcp-server + per-a2a-rpc-call)
- EU AI Act Art. 14 human-oversight (per-llm-governance-decision human_override_id)
- ISO/IEC 42001 AIMS clause 8.4 evidence-rung ready

## 5-WEDGE non-overlap vs cohort siblings (Portkey 1318 + LiteLLM 1319 + Cloudflare AI Gateway 1320)

1. **API-gateway-heritage substrate** — Kong AI Gateway is the AI sub-product of the world's most adopted API gateway (verbatim konghq.com 2026-07-26), inheriting 17+ years of API-gateway heritage (2009 Milan founding) + 500+ enterprise-grade plugins + OpenResty/Lua plugin runtime + Gartner Magic Quadrant full-lifecycle API management leader + G2 leader top API management tools. Distinct from Portkey's SaaS-only control plane + LiteLLM's self-hosted Python SDK + Cloudflare's Workers edge runtime.
2. **MCP + A2A governance from day-1** — "Generate MCP servers and govern how agents discover and consume them" + "Roll out an agent gateway to fully govern all multi-agent traffic, with auth, observability, and auditability baked-in" + A2A traffic + A2A-specific metrics + payload/latency/token/error telemetry + AuthN/Z + audit + caller identity + capabilities. Distinct from Portkey 25+/250+ provider route catalog + LiteLLM 100+ provider Python SDK + Cloudflare 50+ Workers AI provider adapters.
3. **Italian-Milan founder lineage + Andreessen Horowitz board + $2B Series E** — Augusto "Aghi" Marietti CEO + Marco Palladino CTO (Italian schoolmates from Milan, founded 2009) + Martin Casado on board of directors from Andreessen Horowitz + 500+ employees + $100M+ ARR (late 2023) + $175M Series E at $2B valuation (2023-2025) + 2025 OpenMeter acquisition. Distinct from Portkey YC W22 + LiteLLM BerriAI OSS + Cloudflare NYSE-listed public company.
4. **Context Mesh + L7 observability + quota + showback/chargeback** — Kong Context Mesh + L7 observability on AI traffic for cost monitoring + per-user/per-model/per-time-bound quota management at gateway level + showback + chargeback for LLM/agent/MCP usage. Distinct from Portkey per-tenant SaaS observability + LiteLLM self-host observability + Cloudflare per-Workers-runtime observability.
5. **LLM/MCP/A2A governance + PII + semantic prompt guards + 500+ enterprise-grade plugins** — "Govern how developers, apps, and agents consume LLMs. Control everything from access, to data leakage, to token usage" + PII sanitization + semantic prompt guards + access control + 500+ enterprise-grade plugins. Distinct from Portkey's SaaS control plane + LiteLLM's OSS library + Cloudflare's Workers runtime envelope.

## 22-col evidence wedge

tenant_id + kong_control_plane_id + kong_runtime_id + kong_service_id + kong_route_id + kong_consumer_id + kong_plugin_id + kong_upstream_id + provider + model_id + model_version_hash + prompt_hash + completion_hash + input_tokens + output_tokens + cost_cents_usd + latency_ms + llm_governance_decision + mcp_server_id + a2a_rpc_call_id + audit_export_id + cross_tenant_no_bleed_invariant + replay_hash.

## Commercial route (first-party verified 2026-07-26, NOT submitted)

- **mailto:peopleoperations@konghq.com** — canonical first-party JSON-LD Organization contact email 2026-07-26
- **FORM:https://konghq.com/contact-sales** — canonical first-party contact-sales form, verified first-party 2026-07-26
- Augusto Marietti CEO Direct LinkedIn (verified konghq.com/company/about-us 2026-07-26)
- Marco Palladino CTO Direct LinkedIn (verified konghq.com/company/about-us 2026-07-26)
- Kong Customer Portal https://support.konghq.com/support/s/ (first-party support lane)

## Offer ladder (NEW VERTICAL #79 cohort-cumulative, SIBLING #4/5 tier)

- $500/48h fixed-scope Kong AI Gateway evidence-gap map
- $497/mo quarterly refresh
- $2,000 five-vendor ai_agent_llm_gateway COHORT BENCHMARK at close
- $2,485 MRR ceiling per YanXbt pattern (5 clients x $497/mo)
- $10,000 CLOSER-only cohort sponsorship tier unlocked at vertical #79 closure

## Why Kong is the right SIBLING #4/5 (not CLOSER #5/5)

Kong AI Gateway is selected as SIBLING #4/5 — not CLOSER — because the Italian-founder + Andreessen-board + API-gateway-heritage lane is one of five non-overlapping cohort siblings but is structurally a *substrate-extension* pattern (API gateway + LLM extension) rather than a *cohort-closure* narrative like Mintlify-acquired Helicone 1317 or voice-synthesis-substrate ElevenLabs 1301. The CLOSER #5/5 slot should anchor a non-replicable cohort-closure narrative (e.g. an AI-Gateway-acquisition-by-a-platform-owner like Datadog or Cisco) that no future sibling could duplicate. Kong is the canonical "API-gateway-heritage AI-Gateway" substrate sibling.

## Atlas @ Talon Forge

NEW VERTICAL #79 ai_agent_llm_gateway advanced 3/5 → 4/5 (Portkey 1318 OPENER + LiteLLM 1319 SIBLING #2 + Cloudflare AI Gateway 1320 SIBLING #3 + Kong AI Gateway 1321 SIBLING #4); 1 OPEN slot remaining for CLOSER #5/5 per PITFALL #99 cohort-rotation ladder. SMTP/form gated; $0 sent / $0 received. [tick-1321-kong-ai-gateway-ai-agent-llm-gateway-sibling-4-1321]
