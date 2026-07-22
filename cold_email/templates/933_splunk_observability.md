# Splunk Observability — Procurement-Review Cold Email (template 933)

**Vertical:** ai_observability_platform_broad
**Cohort position:** Sibling #4/5 (after Datadog 891 OPENER #1/5 + Dynatrace 910 SIBLING #2/5 + New Relic 911 SIBLING #3/5; one slot remains for CLOSER #5/5)
**First-party source:** https://www.splunk.com/en_us/observability.html (HTTP 200, 286KB verified 2026-07-22)
**Sanctioned contact route:** `https://www.splunk.com/en_us/talk-to-sales.html` (canonical "Contact Splunk sales" form, HTTP 200, Department dropdown includes "Start a trial / Pricing, demo, solutions, or product information / Talk to an expert about my use case", typical response 4-6 business hours)

## 3 Subject Options

1. `Splunk Observability + Cisco — procurement questions for Agent Observability / Splunk MCP Server`
2. `AI-trace + governance review — Splunk AppDynamics + Observability Cloud`
3. `Splunk Observability — Cisco-acquired AI-trace-stack diligence for 2026`

## Cold Email Body

Hi {{first_name}},

Saw that Splunk Observability now ships four NAMED first‑party AI surfaces — **Agent Observability** ("Monitor agents, models, and costs"), **AI SRE** ("Troubleshoot with agentic AI"), **Splunk MCP Server** ("Connect AI to Splunk data securely"), and **AI Toolkit** ("Build, test, and deploy custom AI") — on the same Observability Cloud substrate that already holds Splunk's "11‑time Leader in the Gartner® Magic Quadrant™ for SIEM" credential (verbatim first‑party /observability.html + /about-splunk.html 2026‑07‑22). With Cisco as the parent post‑$28B 2024 acquisition and AppDynamics + IT Service Intelligence + APM + Infrastructure Monitoring + Digital Experience Analytics all sharing that substrate, we have five questions before we standardize on Splunk for our LLM‑feature observability lane:

1. **Per‑agent‑trace provenance across MCP tool calls + agentic‑AI actions.** Splunk MCP Server ("Connect AI to Splunk data securely") and Agent Observability ("Monitor agents, models, and costs") need to produce a per‑trace evidence record that ties each MCP tool‑call id to the agent‑model name + version + prompt‑hash + response‑hash + per‑tenant credential scope — without leaking into a neighboring tenant's trace stream. What's the column‑level schema, and how is cross‑tenant no‑bleed enforced at the Splunk index layer?

2. **AI SRE "agentic AI" governance + per‑remediation‑action receipt.** AI SRE is described as "Troubleshoot with agentic AI" verbatim first‑party. For procurement we need a per‑incident per‑remediation‑action audit receipt (incident id → AI SRE diagnosis → proposed action → human approver → executed change) that holds up under SOC 2 CC7.2 + ISO 42001 A.6.2.7 + EU AI Act Art. 14 human‑oversight review. What's the immutable log path?

3. **AppDynamics + Cisco‑tenant data‑residency + cross‑product credential scoping.** AppDynamics ("Optimize apps with full‑stack insight") sits alongside Observability Cloud under Cisco. For a multi‑region customer (EU + US + APAC), how is per‑tenant data‑residency enforced across AppDynamics + Observability Cloud + IT Service Intelligence, and how is the credential scope kept from bleeding across product boundaries inside the Cisco tenant?

4. **AI Toolkit model‑registry + per‑model‑version lineage.** AI Toolkit ("Build, test, and deploy custom AI") is the per‑customer model‑build/deploy surface. Procurement needs a per‑model‑version lineage record (model name + version + training‑data‑source‑id + evaluation‑score + deploy‑tenant‑id + rollback‑event) that survives model retirement. What's the retention window and the chain‑of‑custody export format?

5. **"Supercharged by Cisco" + 11× Gartner SIEM Leader + per‑regional regulatory mapping.** With Cisco as the parent (verbatim "Supercharged by Cisco, Splunk extends resilience across the entire tech stack" /about-splunk.html 2026‑07‑22) + the 11× Gartner SIEM Leader pedigree, procurement needs a per‑regional regulatory‑mapping matrix (EU AI Act + GDPR + DORA + NIS2 + US SEC cyber‑disclosure 8‑K Reg‑FD + UK AI Bill + Swiss FADP + Singapore MAS TRM + Japan APPI + Australia SOCI + Canada PIPEDA + Brazil LGPD) that Splunk can produce on request. Do you have a current matrix we can review?

If useful, I can send a one‑page RFI that maps each of the five to the specific SOC 2 / ISO / EU AI Act / DORA / NIS2 / SEC Reg‑FD clauses above. Otherwise, can you confirm the canonical Talk‑to‑Sales route (Department = "Talk to an expert about my use case") is the right intake for a procurement‑review conversation at {{company}}?

Best,
{{sender_name}}
Atlas — Talon Forge LLC

---

**Pitfall reinforcement.** This template uses the FORM route `https://www.splunk.com/en_us/talk-to-sales.html` verbatim from the /observability.html nav (Department dropdown includes "Talk to an expert about my use case" + "Start a trial" + "Pricing, demo, solutions, or product information" + "General sales questions" + "None of the above apply to me"). No guessed inbox added per pitfall #28. Splunk is Cisco‑owned post‑March 2024 close (verbatim "Supercharged by Cisco" /about-splunk.html 2026‑07‑22) so any per‑agent‑trace / per‑MCP‑tool‑call diligence must reference both Splunk‑specific and Cisco‑parent compliance posture. AppDynamics is a NAMED first‑party product line ("AppDynamics — Optimize apps with full‑stack insight") under Splunk Observability, distinct from Cisco ThousandEyes or Cisco AppDynamics post‑acquisition lineage.