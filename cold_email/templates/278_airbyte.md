# Cold Email — Airbyte (Lead 278) — data_ops_reverse_etl sibling

**Vertical:** data_ops_reverse_etl (sibling to Census 276, Hightouch 277)
**Tier:** 1
**Email:** privacy@airbyte.io (verified live 2026-07-16 via curl scrape of airbyte.com/privacy; security@airbyte.io also verified)
**Founders:** Michel Tricot (Co-Founder + CEO, ex-Rockset, ex-Iterable, ex-Stitch), John Lafleur (Co-Founder + Head of Engineering), Sasa Popovic (Co-Founder, ex-MuleSoft)
**Ask:** $500 / 48h audit (or trade for a $5K audit + 10 internal credits toward Connector Marketplace listing)

---

**Subject:** Airbyte — 4 questions on per-connector provenance + Connector Development Kit audit trail

Hi Michel —

Atlas here. We audit data-movement + reverse-ETL + CDP stacks for SOC 2 / ISO 42001 / EU AI Act evidence-chain readiness, and Airbyte is the next on our list given the Airbyte AI + Airbyte MCP server + Connector Development Kit + 300+ connectors footprint.

Four questions, all framable in one screen share:

1. **Per-connector sync-run provenance.** When a Sync Job runs from Postgres → Salesforce (or any of the 300+ connector pairs), do you surface a structured per-record provenance payload (source-system, source-LSN, source-tx-id, destination-API-call-id, retry-count, partial-failure-mode) that's joinable back to the warehouse raw event AND to the Salesforce audit log AND to the Sync Job `job_id`? Or is provenance currently scattered across Sync Logs + Connector Logs + the destination's own audit surface?

2. **Airbyte AI suggestion audit trail.** Airbyte AI now suggests schema mappings, anomaly-detection rules, and (per recent product pages) pipeline-natural-language edits. Do those suggestions carry a reasoning-chain payload (suggested-action, model-version, confidence, prompt-template-id, retrieval-context-snapshot-id, human-accept-event-id) so a SOC 2 CC7.2 / ISO 42001 9.4 auditor can reconstruct the suggestion 6 months later?

3. **Connector Development Kit (CDK) custom-connector isolation.** When a customer ships a CDK custom connector (Python-based, runs in the customer-isolated runtime), how is the connector's outbound-API-key material isolated from the rest of the connector pool, and what evidence record attaches to each outbound-API-call — especially for connectors touching destinations that themselves have audit-log retention floors (Salesforce Event Monitoring, Workday audit, NetSuite, etc.)?

4. **Airbyte MCP server tool-call attribution.** Airbyte just shipped an MCP server so agents can list / read / write / run sync jobs. Each MCP tool-call presumably fans out to multiple destination-API-calls + multiple connector-config-changes. Is there a per-MCP-session-id joinable across every destination-API-call + every config-change-event so the operator (or auditor) can replay one MCP session and get a complete causal chain?

If any of those surface a known gap, our 48h audit delivers:

- A SOC 2 CC7.2 + CC9.2 + ISO 42001 9.4 + EU AI Act Annex IV §1-3 evidence-chain map for Airbyte Cloud + Airbyte Open Source + Connector Development Kit + Airbyte AI + Airbyte MCP server, written against airbyte.com/security + airbyte.com/privacy + your public Trust Center.
- A 5-row gap-analysis table mapping your current evidence surface to the OWASP LLM Top 10 + NIST AI RMF MEASURE + ISO 42001 control families the EU AI Act Annex IV expects for high-risk AI-system vendors operating agentic surfaces.
- A 7-step vendor-DD playbook your enterprise customers can hand to their security review teams (cuts vendor-DD cycle from 6-8 weeks to 5-7 days in our prior rollouts).
- A 3-pager red-team plan covering prompt-injection through MCP tool inputs, cross-tenant connector-key leakage, and CDK custom-connector outbound-API-key exfiltration paths.

$500 flat. 48 hours from kickoff. You keep the SOC 2 evidence-map + the 5-row gap table whether or not you engage further.

If you want a free preview: I'll send you a one-page Airbyte vs Census (276) vs Hightouch (277) compliance-automation overlap map (the 3-vendor comparison we built when both competitors got the same audit offer). Reply "send the map" and I'll forward it.

15-min scope call this week?

— Atlas

P.S. — If the right address is security@airbyte.io or your CISO's inbox instead, happy to reroute. Same offer, same 48h.

P.P.S. — Reference: I sent a parallel audit offer to Hightouch (277) and Census (276) this week. Airbyte is the 3rd in the cohort because the connector-pool + open-source-deployment footprint adds a cross-tenant-isolation dimension neither Census nor Hightouch carries.
