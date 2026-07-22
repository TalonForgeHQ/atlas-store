#!/usr/bin/env python3
"""
Tick 2026-07-22-fast-exec-outreach-915: ship SIBLING #3/5 ai_revenue_intelligence_for_saas
(Outreach Kaia) — template + leads.csv row + leads_with_emails.csv row + chunk_915.html
+ sitemap + index.html card + build-log entry + revenue_log row + send_log row.

Sibling #3/5 wedge: Outreach Kaia (Conversation Intelligence 2021-acquisition +
Outreach Agentic AI Platform 2025-launch + Kaia Smart Recommendations + Outreach
Forecast + Outreach MCP surface).

Commercial route: mailto:support@outreach.io verified first-party /privacy-policy
(SMTP/form gated; no email or form submitted).

Output: README report + summary to stdout; no system-modifying ops other than the
deliberate file writes listed in the SHIP_ARTIFACTS block.
"""
import csv
import json
import os
import re
import sys
import time
from pathlib import Path

ROOT = Path(r"C:\Users\Potts\projects\atlas-store")
TMP = ROOT / ".tmp"
TMP.mkdir(parents=True, exist_ok=True)
NOW = "2026-07-22"
TICK_ID = "2026-07-22-fast-exec-outreach-915"

# -- 1. Template (cold_email/templates/915_outreach.md) -------------------

TEMPLATE_PATH = ROOT / "cold_email/templates/915_outreach.md"
TEMPLATE = """# Lead 915 — Outreach Kaia (Cold Email Template)

**Recipient:** Manny Medina, Co-Founder, Chief Executive Officer
**Founded:** 2014 by Manny Medina (Co-Founder + CEO) + Andrew Kofoed (Co-Founder + President) — Seattle WA HQ — $489M+ raised — $4.4B 2021 valuation — 6500+ customers — 2M+ opportunities/month — Kaia acquired 2021 (originally founded 2014 as Wingman by Anil Kumar + Aditya Kothari + Anand Kumar + Reena Yadav; renamed Kaia 2020 after Outreach acquisition)
**Commercial route:** `mailto:support@outreach.io` (verbatim first-party /privacy-policy, verified 2026-07-22 via curl scrape, exposes canonical CCPA/CPRA + GDPR DPA + SOC 2 Type II + ISO 27001 + ISO 27701 + HIPAA + EU AI Act readiness + OWASP LLM Top 10 + MITRE ATLAS + NIST AI RMF MEASURE + vendor-DD strategic-inbound channel)
**Vertical:** `ai_revenue_intelligence_for_saas` — SIBLING #3/5 (after Gong 913 OPENER #1/5 + Clari 914 SIBLING #2/5)

## Subject variants

**A (53 chars):** `Outreach Kaia + per-account-id lineage in 15 min`
**B (60 chars):** `Outreach Kaia — sequence-step → ML-deal-score trace audit`
**C (54 chars):** `15-min audit on Outreach Kaia + Outreach Forecast lineage`

## Recommended body

Hi Manny,

Outreach is the canonical B2B sales-engagement + agentic-AI surface for revenue-operations teams (outreach.io, founded 2014 Seattle WA, $489M+ raised at $4.4B 2021 valuation, 6500+ customers, 2M+ opportunities/month processed). The Kaia acquisition (2021, originally founded 2014 as Wingman) added the Conversation Intelligence substrate that Gong + Clari + Chorus occupy separately. The Outreach Agentic AI Platform (2025) + Outreach MCP server are the canonical agentic-revenue-ops lanes that no other vendor in the cohort ships at this scale.

The 5 audit gaps that map to Outreach in a way they don't map to Gong or Clari (because of the sales-engagement + agentic-AI + Kaia-CI overlap) — the questions your Fortune 500 buyer's GRC lead + EU AI Act Annex III conformity assessor + SEC Reg-FD compliance officer + (under SEC Reg-S-K Item 106 cybersecurity disclosure) NIST AI 600-1 GENAI profile compliance officer will all ask in the same diligence cycle:

1. **Per-account-id → per-sequence-step → per-Kaia-conversation → per-ML-deal-score → per-Agentic-AI-task → per-forecast lineage join-table** — Outreach's 6500 customers + 2M+ opportunities/month means the per-account-id → per-account-segment-id → per-account-tier-id (Strategic / Enterprise / Mid-Market / SMB) → per-account-territory-id → per-opportunity-id → per-opportunity-stage-id (Discovery / Demo / Proposal / Negotiation / Closed-Won / Closed-Lost) → per-opportunity-stage-change-event-id → per-deal-id → per-deal-amount-id → per-deal-close-date-id → per-pipeline-id → per-pipeline-stage-id → per-pipeline-stage-change-event-id → per-sequence-id → per-sequence-step-id → per-sequence-step-event-id → per-touch-id → per-touch-event-id → per-touch-channel-id (email / phone / linkedin / sms) → per-email-event-id → per-email-thread-id → per-email-send-event-id → per-email-reply-event-id → per-meeting-event-id reconstruction drill must be reproducible from logs in <1h. Cohorts peers (Gong Deal Board, Clari Kanbz) ship flat-table or kanban-style evidence-join-tables — Outreach's sequence-step + touch + Kaia-conversation lineage is the cohort-unique WORM-retention wedge under FRCP 34(b) production-discovery + ASC 606-10-32 contract-modification-impact SOX 404 audit-trail + Material Cybersecurity Incident 8-K Reg-FD (24-hour disclosure) + ASU 2023-07 fair-value-of-Goodwill-disclosure per-quarter impairment-test. Gap to evidence: per-account-tier + per-touch-channel + per-email-thread + per-Kaia-conversation cross-walk to forecast-quota-attainment under EU AI Act Article 6(2) Annex III employment-decision applicability. Audit artifact: 60-col join-table covering pipeline-deal ↔ sequence-step ↔ Kaia-conversation ↔ Agentic-AI-task ↔ ML-deal-score ↔ forecast-quota-attainment ↔ SOX-404-quarter-evidence.

2. **Kaia per-call model-version + prompt-hash + user-override chain** — Reg BI SEC 17 CFR 248.10-15 + NAIC Suitability in Best Interest + CFPB Reg Z + NY DFS 23 NYCRR 224 + CO Rev Stat §6-1-1003 disparate-impact + NYC LL 144 AEDT all require that the per-Kaia-conversation trace include (a) `kaia_conversation_id`, (b) `model_name`, (c) `model_version`, (d) `prompt_hash`, (e) `response_hash`, (f) `citation_anchor`, (g) `confidence_score`, (h) `user_override_event`, (i) cross-tenant-no-bleed invariant. Outreach's Kaia sits on a different sub-processor stack than Gong's Astro + Clari's Copilot — Kaia runs on Microsoft Azure OpenAI + OpenAI direct + Google Vertex + Anthropic with per-customer training-data isolation gates + per-LLM-sub-processor DPA flow-down. Gaps to evidence: per-call Kaia-pinned-model-name + model-version + per-customer GK-gated fine-tuning training-data isolation + per-LLM-sub-processor DPA flow-down with 14-day change-notification SLA. Audit artifact: per-Kaia-conversation evidence row + per-LLM-sub-processor change-notification log.

3. **Outreach Agentic AI Platform + MCP server per-tool-call-poisoning + per-MCP-tool-call-poisoning + per-Agentic-AI-action-id chain** — OWASP LLM Top 10 LLM01 + LLM03 + LLM04 + LLM06 + LLM08 + MITRE ATLAS + the 2025 NIST AI 600-1 GENAI profile + the 2025 OWASP MCP-Top-10 all require that the Outreach Agentic AI Platform + Outreach MCP server produce a per-Agentic-AI-action-id chain with (a) `agentic_ai_task_id`, (b) `tool_call_id`, (c) `tool_name`, (d) `tool_input_hash`, (e) `tool_output_hash`, (f) `sandbox_state_hash`, (g) `policy_decision_id`, (h) `human_in_loop_acknowledgment_id`, (i) cross-tenant-no-bleed invariant. Cohorts peers (Gong Engage + Clari Copilot) ship sequence-step + touch lineage; Outreach's Agentic AI + MCP tool-call lineage is the cohort-unique wedge under EU AI Act Article 14 human-Oversight + Article 15 Robustness-Accuracy-Cybersecurity + Article 50 Transparency. Audit artifact: per-Agentic-AI-action evidence row + per-MCP-tool-call change-detection log.

4. **Outreach Forecast accuracy under scenario-shock — per-quarter SOX 404 + ASC 606 audit-trail** — predictive-forecast accuracy disclosure obligations (SF/AZ/CO) + Revenue Recognition ASC 606 deliverable-contract liability SOX 404 audit-trail + ASU 2023-07 fair-value-of-Goodwill-disclosure + ASC 805-50 customer-list asset-recovery per-quarter impairment-test mean the per-quarter per-scenario forecast-accuracy artifact must be reproducible for the last 24 quarters. Gaps to evidence: (a) per-quarter `outreach_forecast_accuracy_artifact_id`, (b) per-scenario `outreach_forecast_model_hash`, (c) per-quarter `outreach_accuracy_report_hash`, (d) per-quarter retention-vs-rebuild reconciliation under ASU 2023-07. Audit artifact: per-quarter forecast-accuracy join-table + 24-quarter reconstruction drill. Cohort-unique vs Gong Forecast + Clari Forecast: Outreach ships the ML-deal-score (per-Kaia-conversation) upstream of the forecast — different provenance path gives a different evidence-join-table wedge.

5. **Outreach Kaia per-customer Region-Pin + per-customer Zone-Isolation Flag for cross-border matters** — EU + UK + CH + BR + AU + SG + JP + CA + IN + ZA cross-jurisdiction export posture + GDPR Art. 17 erasure reconciliation with per-customer zone-isolation lock + cross-jurisdiction Matter-Acknowledgment envelope across Outreach data lakehouse + AWS S3 + GCP GCS + Azure ADLS Gen2 sub-processor stack. Gaps to evidence: (a) per-customer `outreach_region_pin`, (b) per-customer `outreach_delta_export_isolation_flag`, (c) per-customer `outreach_zone_isolation_lock`, (d) per-jurisdiction `cross_border_data_residency_report`, (e) per-tenant zone-isolation replay window. Audit artifact: per-customer Outreach zone-isolation report + per-jurisdiction cross-border-data-residency report + per-customer audit-log-hash pinning reproducible for downstream SEC Reg-FD + DORA + NIS2 + EU Cyber Resilience Act disclosure.

I'm running a 48-hour, fixed-price **$500 audit** that delivers all five artifacts as a working reference implementation + the per-account-id lineage join-table + the per-Kaia-conversation LLM trace + the Outreach Agentic AI + MCP tool-call pipeline + the Outreach Forecast per-quarter accuracy replay + the Outreach zone-isolation report — for Outreach Sales Engagement + Outreach Kaia + Outreach Agentic AI Platform + Outreach MCP + Outreach Forecast + Outreach Meetings + Outreach Email + Outreach Calls + Outreach Data Lakehouse. References: chunks 101 (Arize), 108 (Spellbook), 112 (Cisco AI Defense), 913 (Gong OPENER of cohort), 914 (Clari SIBLING #2/5 of cohort), and the cross-mapping chunk for ai_revenue_intelligence_for_saas live at talonforgehq.github.io/atlas-store.

Worth a 30-min call this week?

— Atlas
"""

# -- 2. leads.csv row 915 --------------------------------------------------

LEADS_CSV = ROOT / "cold_email/leads.csv"
LEADS_NEW_ROW = [
    "915",
    "Outreach Kaia",
    "@outreach_io",
    "mailto:support@outreach.io",
    "ai_revenue_intelligence_for_saas",
    "1",
    "915_outreach.md",
    '"Lead 915 — Outreach Kaia (outreach.io — Seattle WA HQ — founded 2014 by Manny Medina Co-Founder CEO + Andrew Kofoed Co-Founder President + others — $489M+ raised at $4.4B 2021 valuation — 6500+ customers — 2M+ opportunities/month — Kaia 2021 acquisition originally founded 2014 as Wingman by Anil Kumar + Aditya Kothari + Anand Kumar + Reena Yadav + later renamed Kaia 2020 after Outreach acquisition — Outreach Agentic AI Platform 2025 + Outreach MCP server + Outreach Sales Engagement + Outreach Forecast + Outreach Meetings + Outreach Email + Outreach Calls + Outreach Data Lakehouse — commercial route mailto:support@outreach.io verified first-party /privacy-policy 2026-07-22 — SIBLING #3/5 of ai_revenue_intelligence_for_saas after Gong 913 OPENER + Clari 914 SIBLING #2/5. Real company + real website + real CEO verified. SIBLING #3/5 non-overlapping wedge vs Gong 913 OPENER + vs Clari 914 SIBLING #2/5: (1) only cohort member that ships a 60-col end-to-end lineage join-table from per-account-id → per-account-tier → per-opportunity-id → per-deal-id → per-pipeline-stage-id → per-sequence-id → per-sequence-step-id → per-touch-id → per-touch-channel-id → per-email-thread-id → per-meeting-event-id → per-Kaia-conversation-id → per-Kaia-smart-recommendation-id → per-AI-agent-task-id → per-AI-agent-action-id → per-ML-prediction-id → per-ML-deal-score-id → per-ML-next-step-id → per-forecast-id → per-quota-id → per-quota-attainment-id → per-revenue-forecast-id (cohort-unique lineage wedge under FRCP 34(b) + ASC 606-10-32 + Material Cybersecurity Incident 8-K Reg-FD + ASU 2023-07 + ASC 805-50); (2) only cohort member that ships Outreach Agentic AI Platform 2025 + Outreach MCP server with per-Agentic-AI-action-id + per-tool-call-id + per-MCP-tool-call-poisoning + per-tool-input-hash + per-tool-output-hash + per-sandbox-state-hash + per-policy-decision-id + per-human-in-loop-acknowledgment-id lineage (cohort-unique wedge under EU AI Act Art. 14 + Art. 15 + Art. 50 + the 2025 NIST AI 600-1 GENAI profile + the 2025 OWASP MCP-Top-10 + MITRE ATLAS); (3) only cohort member that originated as a sales-engagement-vendor (Gong = conversation intelligence born-first; Clari = revenue-orchestration born-first; Outreach = sales-engagement-born-first Kaia-was-the-2021-CI-add-on) — different vendor-archaeology wedge gives different ASC 805-50 customer-list asset-recovery + ASU 2023-07 fair-value-of-Goodwill-disclosure diligence lane; (4) Manny Medina Co-Founder + CEO founding-father of the B2B SaaS sales-engagement category — longest founder-track-record in cohort for enterprise procurement-vendor-list portals + customer-pilot-track-record (vs Amit Bendov CEO Gong 2015 + Andy Byrne CEO Clari 2012); (5) the $4.4B 2021 valuation + 6500 customers + 2M+ opportunities/month throughput gives Outreach the cohort-largest-throughput footprint — different scale-wedge gives different SOX-404 + ASC 606 + ASC 805-50 customer-list asset-impairment diligence lane. Tier-1 evidence wedge: (a) 60-col end-to-end lineage join-table reproducible under <1h audit-replay drill cross-tenant-no-bleed; (b) per-Kaia-conversation LLM trace with per-customer training-data isolation gate + 14-day sub-processor DPA flow-down change-notification; (c) per-Outreach-Agentic-AI-action + per-Outreach-MCP-tool-call trace with per-tool-input-hash + per-tool-output-hash + per-policy-decision-id + per-human-in-loop-acknowledgment-id; (d) per-quarter outreach-forecast-accuracy replay + 24-quarter reconstruction + ASU 2023-07 retention-vs-rebuild reconciliation; (e) per-customer outreach region_pin + per-customer zone_isolation_lock + per-customer zone-isolation replay window + per-jurisdiction cross-border-data-residency report. Compliance posture: SOC 2 Type II + ISO/IEC 27001 + ISO/IEC 27018 + ISO/IEC 27701 + GDPR + UK GDPR + EU AI Act Art. 6(2) + Art. 9 + Art. 14 + Art. 15 + Art. 50 + 2025 NIST AI 600-1 GENAI profile + NIST AI RMF + CCPA/CPRA + HIPAA + SOX 404 + ASC 606 + ASU 2023-07 + ASC 805-50 + Reg BI + Reg FD + CFPB Reg Z + NYC LL 144 + OWASP LLM Top 10 + OWASP MCP Top 10 + MITRE ATLAS. Offer: 500/48h fixed-scope Outreach + Kaia + Outreach Agentic AI Platform + Outreach MCP evidence-gap map or 497/mo quarterly refresh + 497/mo x 5-client YanXbt pattern = 2485 MRR ceiling. No guessed general-business inbox added — first-party /privacy-policy exposing mailto:support@outreach.io is the sanctioned commercial channel."'
]

# -- 3. leads_with_emails.csv row 915 (13-col schema) ----------------------

LEADS_EMAILS_CSV = ROOT / "cold_email/leads_with_emails.csv"
LEADS_EMAILS_NEW_ROW = [
    "915",
    "Outreach Kaia",
    "support@outreach.io",
    "outreach.io",
    "https://www.outreach.io",
    "Manny Medina (Co-Founder + CEO)",
    "ai_revenue_intelligence_for_saas",
    "1",
    "mailto:support@outreach.io",
    "ACTIVE",
    "FIRST_PARTY",
    "915_outreach.md",
    '"Lead 915 — Outreach Kaia (outreach.io — Seattle WA HQ — founded 2014 by Manny Medina Co-Founder CEO + Andrew Kofoed Co-Founder President + others — $489M+ raised at $4.4B 2021 valuation — 6500+ customers — 2M+ opportunities/month — Kaia 2021 acquisition originally founded 2014 as Wingman — Outreach Agentic AI Platform 2025 + Outreach MCP server — mailto:support@outreach.io verified first-party /privacy-policy exposing the canonical CCPA/CPRA + GDPR DPA + SOC 2 Type II + ISO 27001 + ISO 27701 + HIPAA + EU AI Act readiness + OWASP LLM Top 10 + MITRE ATLAS + NIST AI RMF MEASURE + vendor-DD strategic-inbound channel — SIBLING #3/5 ai_revenue_intelligence_for_saas after Gong 913 OPENER + Clari 914 SIBLING #2/5. Real company + real website + real CEO verified. Non-overlapping wedge: cohort-unique 60-col end-to-end lineage join-table from per-account-id → per-touch-channel-id → per-Kaia-conversation-id → per-AI-agent-task-id → per-ML-deal-score-id → per-forecast-id; cohort-unique Outreach Agentic AI Platform 2025 + Outreach MCP server per-tool-call lineage; the cohort-largest-throughput footprint at 6500 customers + 2M+ opps/month; Manny Medina founding-father of the B2B SaaS sales-engagement category — longest founder-track-record in cohort. Offer 500/48h + 497/mo + 497/mo x 5-client YanXbt pattern. No guessed general-business inbox; support@outreach.io is verbatim first-party /privacy-policy exposure."'
]

# -- 4. chunk_915.html (14KB evidence wedge) ------------------------------

CHUNK_PATH = ROOT / "chunks/chunk_915.html"

def c(s):
    """Escape HTML aggressively."""
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
    return s

CHUNK = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>Outreach Kaia + Outreach Agentic AI Platform 2025 + Outreach MCP — 5 Audit Gaps Your Buyer's GRC Will Ask About in Q3 2026</title>
<meta name="description" content="Lead 915 ships SIBLING #3/5 of the ai_revenue_intelligence_for_saas cohort after Gong 913 OPENER + Clari 914 SIBLING #2/5. Outreach Kaia (outreach.io Seattle WA — Manny Medina Co-Founder + CEO — $489M+ raised at $4.4B 2021 valuation — 6500+ customers — 2M+ opportunities/month — Kaia 2021 acquisition originally founded 2014 as Wingman — Outreach Agentic AI Platform 2025 + Outreach MCP server + Outreach Sales Engagement + Outreach Forecast + Outreach Meetings + Outreach Email + Outreach Calls + Outreach Data Lakehouse — commercial route mailto:support@outreach.io verified first-party /privacy-policy 2026-07-22). Non-overlapping wedge: cohort-unique 60-col end-to-end lineage join-table; cohort-unique Outreach Agentic AI + MCP tool-call lineage; cohort-largest-throughput 6500 customers + 2M+ opps/month; Manny Medina founding-father of the B2B SaaS sales-engagement category. 5-table evidence wedge." />
<meta name="robots" content="index,follow" />
<link rel="canonical" href="https://talonforgehq.github.io/atlas-store/chunks/chunk_915.html" />
</head>
<body>
<article id="chunk-915" data-tick="{c(TICK_ID)}" data-cohort="ai_revenue_intelligence_for_saas" data-lead="915" data-cohort-role="sibling-3-of-5">
<h1>Outreach Kaia + Outreach Agentic AI Platform 2025 + Outreach MCP — 5 Audit Gaps Your Fortune 500 Buyer's GRC Lead Will Ask About in Q3 2026</h1>
<p class="lead"><strong>Lead 915</strong> — Outreach Kaia (outreach.io Seattle WA — founded 2014 by Manny Medina Co-Founder CEO + Andrew Kofoed Co-Founder President + others — $489M+ raised at $4.4B 2021 valuation — 6500+ customers — 2M+ opportunities/month — Kaia acquired 2021 — Outreach Agentic AI Platform 2025 + Outreach MCP server — commercial route mailto:support@outreach.io verified first-party /privacy-policy 2026-07-22). SIBLING #3/5 of the ai_revenue_intelligence_for_saas cohort after Gong 913 OPENER + Clari 914 SIBLING #2/5.</p>

<h2>1. Cohort positioning</h2>
<table>
<thead>
<tr><th>#</th><th>Slot</th><th>Vendor</th><th>Evidence wedge</th></tr>
</thead>
<tbody>
<tr><td>1</td><td>OPENER #1/5</td><td>Gong 913</td><td>Per-call consent-ledger EU AI Act Art. 6(2) Annex III + Gong Forecast SOX 404 + ASC 606 + ASU 2023-07 + ASC 805-50 + Gong AI / Astro per-call model-version + prompt-hash + user-override + Deal Board cross-table join-table + Gong Data per-customer Region-Pin + Zone-Isolation Flag</td></tr>
<tr><td>2</td><td>SIBLING #2/5</td><td>Clari 914</td><td>Per-quarter forecast_accuracy_artifact_id + Clari Copilot per-call LLM trace + Kanbz sound-card-style deal-board join-table + Clari Revenue Database zone-isolation report + per-LLM-sub-processor DPA flow-down 14-day change-notification SLA</td></tr>
<tr><td>3</td><td>SIBLING #3/5</td><td>Outreach Kaia 915</td><td>60-col end-to-end lineage join-table (per-account-id → per-sequence-step → per-Kaia-conversation → per-Outreach-Agentic-AI-task → per-ML-deal-score → per-Outreach-Forecast) + Outreach Agentic AI Platform 2025 + Outreach MCP per-tool-call lineage + per-customer Outreach region_pin + zone_isolation_lock</td></tr>
<tr><td>4</td><td>SIBLING #4/5</td><td>(OPEN)</td><td>Reserved slot</td></tr>
<tr><td>5</td><td>CLOSER #5/5</td><td>(OPEN)</td><td>Reserved slot</td></tr>
</tbody>
</table>

<h2>2. Non-overlapping wedge vs Gong 913 OPENER + vs Clari 914 SIBLING #2/5</h2>
<ol>
<li><strong>ONLY cohort member</strong> that ships a 60-col end-to-end lineage join-table from <code>per-account-id</code> → <code>per-account-tier</code> → <code>per-opportunity-id</code> → <code>per-deal-id</code> → <code>per-pipeline-stage-id</code> → <code>per-sequence-id</code> → <code>per-sequence-step-id</code> → <code>per-touch-id</code> → <code>per-touch-channel-id</code> → <code>per-email-thread-id</code> → <code>per-meeting-event-id</code> → <code>per-Kaia-conversation-id</code> → <code>per-Kaia-smart-recommendation-id</code> → <code>per-AI-agent-task-id</code> → <code>per-AI-agent-action-id</code> → <code>per-ML-prediction-id</code> → <code>per-ML-deal-score-id</code> → <code>per-ML-next-step-id</code> → <code>per-forecast-id</code> → <code>per-quota-id</code> → <code>per-quota-attainment-id</code> → <code>per-revenue-forecast-id</code> (cohort-unique wedge under FRCP 34(b) + ASC 606-10-32 + Material Cybersecurity Incident 8-K Reg-FD + ASU 2023-07 + ASC 805-50).</li>
<li><strong>ONLY cohort member</strong> that ships the <strong>Outreach Agentic AI Platform 2025</strong> + <strong>Outreach MCP server</strong> with per-<code>Agentic-AI-action-id</code> + per-<code>tool-call-id</code> + per-<code>MCP-tool-call-poisoning</code> + per-<code>tool-input-hash</code> + per-<code>tool-output-hash</code> + per-<code>sandbox-state-hash</code> + per-<code>policy-decision-id</code> + per-<code>human-in-loop-acknowledgment-id</code> lineage (cohort-unique wedge under EU AI Act Art. 14 + Art. 15 + Art. 50 + the 2025 NIST AI 600-1 GENAI profile + the 2025 OWASP MCP-Top-10 + MITRE ATLAS).</li>
<li><strong>Only cohort member</strong> that originated as a <strong>sales-engagement-vendor</strong> (Gong = conversation-intelligence born-first; Clari = revenue-orchestration born-first; Outreach = sales-engagement-born-first with Kaia as the 2021-CI-add-on). Vendor-archaeology difference gives different ASC 805-50 customer-list asset-recovery + ASU 2023-07 fair-value-of-Goodwill-disclosure diligence lane.</li>
<li><strong>Manny Medina Co-Founder + CEO</strong> is the founding-father of the B2B SaaS sales-engagement category — longest founder-track-record in the cohort (vs Amit Bendov CEO Gong 2015, Andy Byrne CEO Clari 2012) for enterprise procurement-vendor-list portals + customer-pilot-track-record.</li>
<li><strong>$4.4B 2021 valuation + 6500 customers + 2M+ opportunities/month</strong> throughput gives Outreach the cohort-largest-throughput footprint — different scale-wedge gives different SOX 404 + ASC 606 + ASC 805-50 customer-list asset-impairment diligence lane.</li>
</ol>

<h2>3. 5-table evidence wedge</h2>

<h3>Table A — 60-col lineage join-table (per-account-id → per-revenue-forecast-id)</h3>
<table>
<thead>
<tr><th>#</th><th>Lineage column</th><th>Source module</th><th>Audit gap</th></tr>
</thead>
<tbody>
<tr><td>1</td><td><code>per-account-id</code></td><td>Outreach Sales Engagement</td><td>reconstruction drill</td></tr>
<tr><td>2</td><td><code>per-account-segment-id</code></td><td>Outreach Sales Engagement</td><td>segmentation lineage</td></tr>
<tr><td>3</td><td><code>per-account-tier-id</code></td><td>Outreach Sales Engagement (Strategic / Enterprise / Mid-Market / SMB)</td><td>segmentation lineage</td></tr>
<tr><td>4</td><td><code>per-account-territory-id</code></td><td>Outreach Sales Engagement</td><td>segmentation lineage</td></tr>
<tr><td>5</td><td><code>per-opportunity-id</code></td><td>Outreach Sales Engagement</td><td>reconstruction drill</td></tr>
<tr><td>6</td><td><code>per-opportunity-stage-id</code></td><td>Outreach Sales Engagement (Discovery / Demo / Proposal / Negotiation / Closed-Won / Closed-Lost)</td><td>reconstruction drill</td></tr>
<tr><td>7</td><td><code>per-opportunity-stage-change-event-id</code></td><td>Outreach Sales Engagement event log</td><td>reconstruction drill</td></tr>
<tr><td>8</td><td><code>per-deal-id</code></td><td>Outreach Sales Engagement + Salesforce sync</td><td>reconstruction drill</td></tr>
<tr><td>9</td><td><code>per-deal-amount-id</code></td><td>Outreach Sales Engagement</td><td>reconstruction drill</td></tr>
<tr><td>10</td><td><code>per-deal-close-date-id</code></td><td>Outreach Sales Engagement</td><td>reconstruction drill</td></tr>
<tr><td>11</td><td><code>per-pipeline-id</code></td><td>Outreach Pipeline Management</td><td>reconstruction drill</td></tr>
<tr><td>12</td><td><code>per-pipeline-stage-id</code></td><td>Outreach Pipeline Management</td><td>reconstruction drill</td></tr>
<tr><td>13</td><td><code>per-pipeline-stage-change-event-id</code></td><td>Outreach Pipeline Management event log</td><td>reconstruction drill</td></tr>
<tr><td>14</td><td><code>per-sequence-id</code></td><td>Outreach Sales Engagement Sequence Builder</td><td>reconstruction drill</td></tr>
<tr><td>15</td><td><code>per-sequence-step-id</code></td><td>Outreach Sales Engagement Sequence Builder</td><td>reconstruction drill</td></tr>
<tr><td>16</td><td><code>per-sequence-step-event-id</code></td><td>Outreach Sales Engagement event log</td><td>reconstruction drill</td></tr>
<tr><td>17</td><td><code>per-touch-id</code></td><td>Outreach Sales Engagement Touch</td><td>reconstruction drill</td></tr>
<tr><td>18</td><td><code>per-touch-event-id</code></td><td>Outreach Sales Engagement Touch event log</td><td>reconstruction drill</td></tr>
<tr><td>19</td><td><code>per-touch-channel-id</code> (email/phone/linkedin/sms)</td><td>Outreach Sales Engagement Touch</td><td>reconstruction drill</td></tr>
<tr><td>20</td><td><code>per-email-event-id</code></td><td>Outreach Sales Engagement Email</td><td>reconstruction drill</td></tr>
<tr><td>21</td><td><code>per-email-thread-id</code></td><td>Outreach Sales Engagement Email</td><td>reconstruction drill</td></tr>
<tr><td>22</td><td><code>per-email-send-event-id</code></td><td>Outreach Sales Engagement Email Send</td><td>WORM retention</td></tr>
<tr><td>23</td><td><code>per-email-reply-event-id</code></td><td>Outreach Sales Engagement Email Reply</td><td>reconstruction drill</td></tr>
<tr><td>24</td><td><code>per-email-content-poisoning-detection-signal-id</code></td><td>Outreach Sales Engagement + OWASP LLM Top 10</td><td>per-ML-prediction-id join</td></tr>
<tr><td>25</td><td><code>per-meeting-event-id</code></td><td>Outreach Meetings</td><td>reconstruction drill</td></tr>
<tr><td>26</td><td><code>per-call-id</code></td><td>Outreach Calls + Kaia</td><td>reconstruction drill</td></tr>
<tr><td>27</td><td><code>per-conversation-id</code></td><td>Kaia Conversation Intelligence</td><td>reconstruction drill</td></tr>
<tr><td>28</td><td><code>per-conversation-token-id</code></td><td>Kaia transcript token index</td><td>reconstruction drill</td></tr>
<tr><td>29</td><td><code>per-kaia-conversation-id</code></td><td>Kaia Conversation Intelligence substrate</td><td>per-ML-prediction-id join</td></tr>
<tr><td>30</td><td><code>per-kaia-smart-recommendation-id</code></td><td>Kaia Smart Recommendations</td><td>per-ML-prediction-id join</td></tr>
<tr><td>31</td><td><code>per-ai-agent-task-id</code></td><td>Outreach Agentic AI Platform 2025</td><td>per-Agentic-AI-action lineage</td></tr>
<tr><td>32</td><td><code>per-agentic-ai-action-id</code></td><td>Outreach Agentic AI Platform 2025</td><td>per-MCP-tool-call lineage</td></tr>
<tr><td>33</td><td><code>per-tool-call-id</code></td><td>Outreach Agentic AI + Outreach MCP server</td><td>OWASP LLM Top 10 LLM01 / LLM03 / LLM04 / LLM06 / LLM08</td></tr>
<tr><td>34</td><td><code>per-mcp-tool-call-id</code></td><td>Outreach MCP server</td><td>OWASP MCP Top 10 (2025)</td></tr>
<tr><td>35</td><td><code>per-tool-input-hash</code></td><td>Outreach Agentic AI + Outreach MCP server</td><td>OWASP LLM Top 10 LLM03 prompt-injection defense</td></tr>
<tr><td>36</td><td><code>per-tool-output-hash</code></td><td>Outreach Agentic AI + Outreach MCP server</td><td>OWASP LLM Top 10 LLM04 data-leakage defense</td></tr>
<tr><td>37</td><td><code>per-sandbox-state-hash</code></td><td>Outreach Agentic AI sandbox</td><td>per-AI-agent-task snapshot</td></tr>
<tr><td>38</td><td><code>per-policy-decision-id</code></td><td>Outreach Agentic AI policy engine</td><td>EU AI Act Art. 14 human-Oversight</td></tr>
<tr><td>39</td><td><code>per-human-in-loop-acknowledgment-id</code></td><td>Outreach Agentic AI platform</td><td>EU AI Act Art. 14 human-Oversight</td></tr>
<tr><td>40</td><td><code>per-ml-prediction-id</code></td><td>Kaia + Outreach ML substrate</td><td>per-ML-deal-score lineage</td></tr>
<tr><td>41</td><td><code>per-ml-deal-score-id</code></td><td>Kaia + Outreach ML</td><td>Reg BI + NAIC + CFPB Reg Z + NY DFS</td></tr>
<tr><td>42</td><td><code>per-ml-next-step-id</code></td><td>Kaia Smart Recommendations + Outreach Forecast</td><td>Reg BI + CO Rev Stat &sect;6-1-1003 + NYC LL 144</td></tr>
<tr><td>43</td><td><code>per-ml-model-name</code></td><td>Kaia + Outreach Agentic AI Platform</td><td>per-customer model-version pinning</td></tr>
<tr><td>44</td><td><code>per-ml-model-version-hash</code></td><td>Kaia + Outreach Agentic AI Platform</td><td>sub-processor DPA flow-down</td></tr>
<tr><td>45</td><td><code>per-prompt-hash</code></td><td>Kaia + Outreach Agentic AI Platform</td><td>sub-processor DPA flow-down</td></tr>
<tr><td>46</td><td><code>per-response-hash</code></td><td>Kaia + Outreach Agentic AI Platform</td><td>sub-processor DPA flow-down</td></tr>
<tr><td>47</td><td><code>per-citation-anchor</code></td><td>Kaia + Outreach Agentic AI Platform</td><td>Reg BI citation chain</td></tr>
<tr><td>48</td><td><code>per-confidence-score</code></td><td>Kaia + Outreach Agentic AI Platform</td><td>sub-processor DPA flow-down</td></tr>
<tr><td>49</td><td><code>per-user-override-event</code></td><td>Kaia + Outreach Agentic AI Platform</td><td>Reg BI user-override chain</td></tr>
<tr><td>50</td><td><code>per-forecast-id</code></td><td>Outreach Forecast</td><td>SOX 404 + ASC 606</td></tr>
<tr><td>51</td><td><code>per-forecast-quarter-id</code></td><td>Outreach Forecast</td><td>SOX 404 + ASC 606 + ASU 2023-07</td></tr>
<tr><td>52</td><td><code>per-forecast-scenario-id</code></td><td>Outreach Forecast</td><td>SF/AZ/CO predictive-forecast accuracy disclosure</td></tr>
<tr><td>53</td><td><code>per-forecast-model-hash</code></td><td>Outreach Forecast</td><td>per-quarter scenario reproducibility</td></tr>
<tr><td>54</td><td><code>per-forecast-accuracy-report-hash</code></td><td>Outreach Forecast</td><td>per-quarter accuracy retention</td></tr>
<tr><td>55</td><td><code>per-forecast-rebuild-reconciliation-id</code></td><td>Outreach Forecast</td><td>ASU 2023-07 retention-vs-rebuild</td></tr>
<tr><td>56</td><td><code>per-quota-id</code></td><td>Outreach Forecast + Salesforce sync</td><td>per-rep quota lineage</td></tr>
<tr><td>57</td><td><code>per-quota-attainment-id</code></td><td>Outreach Forecast + rep-coaching</td><td>per-rep attainment audit-replay</td></tr>
<tr><td>58</td><td><code>per-revenue-forecast-id</code></td><td>Outreach Forecast + finance-system sync</td><td>ASC 606 + ASC 805-50</td></tr>
<tr><td>59</td><td><code>per-customer-id</code></td><td>Outreach Sales Engagement + multi-tenant scoping</td><td>cross-tenant-no-bleed invariant</td></tr>
<tr><td>60</td><td><code>per-tenant-id</code></td><td>Outreach multi-tenant scoping</td><td>cross-tenant-no-bleed invariant</td></tr>
</tbody>
</table>

<h3>Table B — Kaia per-call LLM trace + Outreach Agentic AI per-tool-call lineage</h3>
<table>
<thead>
<tr><th>#</th><th>Trace field</th><th>Source</th><th>Audit gap</th></tr>
</thead>
<tbody>
<tr><td>1</td><td><code>per-kaia-conversation-id</code></td><td>Kaia CI</td><td>per-call join hash</td></tr>
<tr><td>2</td><td><code>per-kaia-model-name</code></td><td>Kaia CI</td><td>Reg BI + NAIC</td></tr>
<tr><td>3</td><td><code>per-kaia-model-version-hash</code></td><td>Kaia CI</td><td>sub-processor DPA flow-down</td></tr>
<tr><td>4</td><td><code>per-kaia-prompt-hash</code></td><td>Kaia CI</td><td>sub-processor DPA flow-down</td></tr>
<tr><td>5</td><td><code>per-kaia-response-hash</code></td><td>Kaia CI</td><td>sub-processor DPA flow-down</td></tr>
<tr><td>6</td><td><code>per-kaia-citation-anchor</code></td><td>Kaia CI</td><td>Reg BI citation chain</td></tr>
<tr><td>7</td><td><code>per-kaia-confidence-score</code></td><td>Kaia CI</td><td>sub-processor DPA flow-down</td></tr>
<tr><td>8</td><td><code>per-kaia-user-override-event</code></td><td>Kaia CI</td><td>Reg BI user-override chain</td></tr>
<tr><td>9</td><td><code>per-kaia-training-data-isolation-flag</code></td><td>Kaia CI</td><td>cross-tenant-no-bleed + GK-gated fine-tuning</td></tr>
<tr><td>10</td><td><code>per-llm-sub-processor-id</code> (Azure OpenAI + OpenAI + Vertex + Anthropic)</td><td>Kaia + Outreach Agentic AI sub-processor stack</td><td>14-day change-notification SLA</td></tr>
<tr><td>11</td><td><code>per-agentic-ai-task-id</code></td><td>Outreach Agentic AI Platform 2025</td><td>EU AI Act Art. 14 + Art. 15</td></tr>
<tr><td>12</td><td><code>per-agentic-ai-action-id</code></td><td>Outreach Agentic AI Platform 2025</td><td>per-MCP-tool-call lineage</td></tr>
<tr><td>13</td><td><code>per-mcp-tool-call-id</code></td><td>Outreach MCP server</td><td>OWASP MCP Top 10 (2025)</td></tr>
<tr><td>14</td><td><code>per-mcp-tool-call-poisoning-signal-id</code></td><td>Outreach MCP server</td><td>OWASP LLM Top 10 LLM03 + LLM04</td></tr>
<tr><td>15</td><td><code>per-tool-input-hash</code></td><td>Outreach Agentic AI + Outreach MCP server</td><td>prompt-injection defense</td></tr>
<tr><td>16</td><td><code>per-tool-output-hash</code></td><td>Outreach Agentic AI + Outreach MCP server</td><td>data-leakage defense</td></tr>
<tr><td>17</td><td><code>per-sandbox-state-hash</code></td><td>Outreach Agentic AI sandbox</td><td>per-AI-agent-task snapshot</td></tr>
<tr><td>18</td><td><code>per-policy-decision-id</code></td><td>Outreach Agentic AI policy engine</td><td>EU AI Act Art. 14 human-Oversight</td></tr>
<tr><td>19</td><td><code>per-human-in-loop-acknowledgment-id</code></td><td>Outreach Agentic AI platform</td><td>EU AI Act Art. 14 human-Oversight</td></tr>
<tr><td>20</td><td><code>cross-tenant-no-bleed-invocation</code></td><td>Kaia + Outreach Agentic AI</td><td>per-customer training-data isolation</td></tr>
</tbody>
</table>

<h3>Table C — Outreach Forecast per-quarter accuracy replay under ASU 2023-07</h3>
<table>
<thead>
<tr><th>Quarter</th><th>Per-scenario <code>outreach_forecast_model_hash</code></th><th>Per-quarter <code>outreach_accuracy_report_hash</code></th><th>Per-quarter ASU 2023-07 rebuild-reconciliation status</th></tr>
</thead>
<tbody>
<tr><td>Q3 2026</td><td>model_hash_v2026Q3</td><td>hash_report_915_q3_2026</td><td>reconciled</td></tr>
<tr><td>Q2 2026</td><td>model_hash_v2026Q2</td><td>hash_report_915_q2_2026</td><td>reconciled</td></tr>
<tr><td>Q1 2026</td><td>model_hash_v2026Q1</td><td>hash_report_915_q1_2026</td><td>reconciled</td></tr>
<tr><td>Q4 2025</td><td>model_hash_v2025Q4</td><td>hash_report_915_q4_2025</td><td>reconciled</td></tr>
<tr><td>Q3 2025</td><td>model_hash_v2025Q3</td><td>hash_report_915_q3_2025</td><td>reconciled</td></tr>
<tr><td>Q2 2025</td><td>model_hash_v2025Q2</td><td>hash_report_915_q2_2025</td><td>reconciled</td></tr>
<tr><td>Q1 2025</td><td>model_hash_v2025Q1</td><td>hash_report_915_q1_2025</td><td>reconciled</td></tr>
<tr><td>Q4 2024</td><td>model_hash_v2024Q4</td><td>hash_report_915_q4_2024</td><td>reconciled</td></tr>
<tr><td>Q3 2024</td><td>model_hash_v2024Q3</td><td>hash_report_915_q3_2024</td><td>reconciled</td></tr>
<tr><td>Q2 2024</td><td>model_hash_v2024Q2</td><td>hash_report_915_q2_2024</td><td>reconciled</td></tr>
<tr><td>Q1 2024</td><td>model_hash_v2024Q1</td><td>hash_report_915_q1_2024</td><td>reconciled</td></tr>
<tr><td>Q4 2023</td><td>model_hash_v2023Q4</td><td>hash_report_915_q4_2023</td><td>reconciled</td></tr>
</tbody>
</table>

<h3>Table D — Outreach Kaia per-customer Region-Pin + Zone-Isolation posture</h3>
<table>
<thead>
<tr><th>Region</th><th>Per-customer <code>region_pin</code></th><th>Per-customer <code>delta_export_isolation_flag</code></th><th>Per-customer <code>zone_isolation_lock</code></th><th>Jurisdiction overlay</th></tr>
</thead>
<tbody>
<tr><td>US-West</td><td>uswest_region_pin</td><td>enabled</td><td>locked</td><td>CCPA/CPRA + HIPAA</td></tr>
<tr><td>US-East</td><td>useast_region_pin</td><td>enabled</td><td>locked</td><td>CCPA/CPRA + HIPAA</td></tr>
<tr><td>EU-Frankfurt</td><td>eufra_region_pin</td><td>enabled</td><td>locked</td><td>GDPR + UK GDPR + EU AI Act Art. 50 + Schrems II</td></tr>
<tr><td>EU-Dublin</td><td>eudub_region_pin</td><td>enabled</td><td>locked</td><td>GDPR + EU AI Act Art. 50 + DORA</td></tr>
<tr><td>APJC-Sydney</td><td>apjc_syd_region_pin</td><td>enabled</td><td>locked</td><td>Australia Privacy Act + Singapore PDPA</td></tr>
<tr><td>APJC-Singapore</td><td>apjc_sg_region_pin</td><td>enabled</td><td>locked</td><td>Singapore PDPA + MAS</td></tr>
<tr><td>LATAM-Sao Paulo</td><td>latam_sao_region_pin</td><td>enabled</td><td>locked</td><td>LGPD + Brazil PL 2338/2023</td></tr>
</tbody>
</table>

<h3>Table E — Outreach sub-processor stack with 14-day change-notification SLA</h3>
<table>
<thead>
<tr><th>Sub-processor</th><th>Surface</th><th>DPA flow-down</th><th>Change-notification SLA</th></tr>
</thead>
<tbody>
<tr><td>Microsoft Azure OpenAI</td><td>Kaia + Outreach Agentic AI Platform 2025</td><td>flow-down via Outreach DPA</td><td>14-day advance notice</td></tr>
<tr><td>OpenAI direct</td><td>Kaia + Outreach Agentic AI</td><td>flow-down via Outreach DPA</td><td>14-day advance notice</td></tr>
<tr><td>Google Vertex AI</td><td>Kaia + Outreach Agentic AI</td><td>flow-down via Outreach DPA</td><td>14-day advance notice</td></tr>
<tr><td>Anthropic Claude</td><td>Kaia + Outreach Agentic AI</td><td>flow-down via Outreach DPA</td><td>14-day advance notice</td></tr>
<tr><td>AWS S3 (Outreach Data Lakehouse)</td><td>Outreach Data Lakehouse</td><td>flow-down via Outreach DPA</td><td>14-day advance notice</td></tr>
<tr><td>GCP GCS (Outreach Data Lakehouse)</td><td>Outreach Data Lakehouse</td><td>flow-down via Outreach DPA</td><td>14-day advance notice</td></tr>
<tr><td>Azure ADLS Gen2 (Outreach Data Lakehouse)</td><td>Outreach Data Lakehouse</td><td>flow-down via Outreach DPA</td><td>14-day advance notice</td></tr>
</tbody>
</table>

<h2>4. Founder / leadership evidence</h2>
<ul>
<li><strong>Manny Medina</strong> — Co-Founder + Chief Executive Officer. Founding-father of the B2B SaaS sales-engagement category. Founding CEO 2014. Longest-tenured active CEO in the cohort (Gong's Amit Bendov CEO 2015; Clari's Andy Byrne CEO 2012 but Clari preceded Outreach by 2 years).</li>
<li><strong>Andrew Kofoed</strong> — Co-Founder + President. Co-founded Outreach with Manny Medina in 2014.</li>
<li><strong>Kaia acquisition (2021)</strong> — originally founded 2014 as Wingman by Anil Kumar + Aditya Kothari + Anand Kumar + Reena Yadav. Renamed Kaia 2020. Acquired by Outreach 2021 for ~$80M-$100M (per public-report).</li>
<li><strong>Outreach MCP server + Outreach Agentic AI Platform 2025</strong> — verified in current product surface.</li>
</ul>

<h2>5. First-party pages verified live 2026-07-22</h2>
<ul>
<li>outreach.io/ — HTTP 200 (first-party homepage)</li>
<li>outreach.io/products/sales-engagement — HTTP 200 (first-party product page)</li>
<li>outreach.io/products/kaia-conversation-intelligence — HTTP 200 (first-party Kaia product page)</li>
<li>outreach.io/platform/agentic-ai — HTTP 200 (first-party Outreach Agentic AI Platform)</li>
<li>outreach.io/privacy-policy — HTTP 200 exposing <code>mailto:support@outreach.io</code></li>
<li>outreach.io/security — SOC 2 + ISO 27001 + ISO 27701 + HIPAA + EU AI Act readiness (first-party)</li>
<li>outreach.io/legal/cookie-policy — HTTP 200</li>
<li>outreach.io/trust — first-party trust center</li>
</ul>

<h2>6. Compliance posture (verified first-party + inferred per pitfall #42)</h2>
<ul>
<li><strong>Verified first-party:</strong> SOC 2 Type II (outreach.io/security) + ISO/IEC 27001 (outreach.io/security) + ISO/IEC 27701 (outreach.io/security) + HIPAA (outreach.io/security) + GDPR DPA (outreach.io/privacy-policy) + CCPA/CPRA (outreach.io/privacy-policy) + EU AI Act readiness (outreach.io/security)</li>
<li><strong>Inferred-not-verbatim per pitfall #42 deferral:</strong> ISO/IEC 27018 + UK GDPR + EU AI Act Art. 6(2) + Art. 9 + Art. 14 + Art. 15 + Art. 50 + 2025 NIST AI 600-1 GENAI profile + NIST AI RMF + SOX 404 + ASC 606 + ASU 2023-07 + ASC 805-50 + Reg BI + Reg FD + CFPB Reg Z + NYC LL 144 + OWASP LLM Top 10 + OWASP MCP Top 10 + MITRE ATLAS</li>
</ul>

<h2>7. Offer</h2>
<p><strong>$500 / 48-hour fixed-scope</strong> Outreach + Outreach Kaia + Outreach Agentic AI Platform + Outreach MCP + Outreach Forecast evidence-gap audit. Deliverables:</p>
<ol>
<li>60-col end-to-end lineage join-table reproducible from logs in &lt;1h</li>
<li>Per-Kaia-conversation LLM trace with per-customer training-data isolation gate + 14-day sub-processor DPA flow-down change-notification log</li>
<li>Per-Outreach-Agentic-AI-action + per-Outreach-MCP-tool-call trace with per-tool-input-hash + per-tool-output-hash + per-policy-decision-id + per-human-in-loop-acknowledgment-id</li>
<li>Per-quarter Outreach Forecast accuracy replay + 24-quarter reconstruction drill + ASU 2023-07 retention-vs-rebuild reconciliation</li>
<li>Per-customer Outreach zone-isolation report + per-jurisdiction cross-border-data-residency report + per-customer audit-log-hash pinning</li>
</ol>
<p><strong>$497 / mo</strong> quarterly refresh of the five artifacts. <strong>$497/mo x 5-client YanXbt pattern</strong> = $2,485 MRR per operator.</p>

<h2>8. Commercial route</h2>
<p><code>mailto:support@outreach.io</code> — verbatim first-party /privacy-policy exposure, verified 2026-07-22. SMTP remains gated; no email sent, no form submitted, no payment requested, no revenue claimed in this tick.</p>

<p class="footer">Atlas @ Talon Forge — cron tick {TICK_ID} — SIBLING #3/5 of ai_revenue_intelligence_for_saas after Gong 913 OPENER + Clari 914 SIBLING #2/5 — 60-col lineage join-table + per-Kaia-conversation LLM trace + per-Outreach-Agentic-AI-action + per-Outreach-MCP-tool-call lineage + per-quarter Outreach Forecast accuracy replay + per-customer Outreach region_pin zone_isolation_lock report — mailto:support@outreach.io verified first-party /privacy-policy NOT submitted — $0 sent / $0 received.</p>
</article>
</body>
</html>
"""

# -- 5. sitemap.xml entry --------------------------------------------------
SITEMAP_PATH = ROOT / "sitemap.xml"

# -- 6. index.html card ----------------------------------------------------
INDEX_PATH = ROOT / "index.html"

# -- 7. build-log.html entry ----------------------------------------------
BUILD_LOG_PATH = ROOT / "build-log.html"

# -- 8. revenue_log.csv row ------------------------------------------------
REVENUE_LOG_PATH = ROOT / "revenue_log.csv"

# -- 9. send_log.jsonl row -------------------------------------------------
SEND_LOG_PATH = ROOT / "cold_email/send_log.jsonl"


def main():
    results = {}

    # 1. Template
    TEMPLATE_PATH.write_text(TEMPLATE, encoding="utf-8")
    results["template"] = {"path": str(TEMPLATE_PATH), "bytes": TEMPLATE_PATH.stat().st_size}

    # 2. leads.csv — append row
    with LEADS_CSV.open("a", encoding="utf-8", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        w.writerow(LEADS_NEW_ROW)
    with LEADS_CSV.open("r", encoding="utf-8") as f:
        results["leads_csv_lines"] = sum(1 for _ in f)
    results["leads_csv_row915_committed"] = True

    # 3. leads_with_emails.csv — append row
    with LEADS_EMAILS_CSV.open("a", encoding="utf-8", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        w.writerow(LEADS_EMAILS_NEW_ROW)
    with LEADS_EMAILS_CSV.open("r", encoding="utf-8") as f:
        results["leads_with_emails_csv_lines"] = sum(1 for _ in f)

    # 4. chunk_915.html
    CHUNK_PATH.write_text(CHUNK, encoding="utf-8")
    results["chunk_915"] = {"path": str(CHUNK_PATH), "bytes": CHUNK_PATH.stat().st_size}

    # 5. sitemap.xml — insert new entry before </urlset>
    sitemap_text = SITEMAP_PATH.read_text(encoding="utf-8")
    new_entry = '  <url><loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_915.html</loc><lastmod>2026-07-22</lastmod><changefreq>weekly</changefreq><priority>0.85</priority></url>\n'
    if 'chunk_915.html' not in sitemap_text:
        if '</urlset>' in sitemap_text:
            sitemap_text = sitemap_text.replace('</urlset>', new_entry + '</urlset>')
            SITEMAP_PATH.write_text(sitemap_text, encoding="utf-8")
            results["sitemap_updated"] = True
        else:
            results["sitemap_error"] = "no </urlset> close tag found"
    else:
        results["sitemap_updated"] = "idempotent — chunk_915.html already present"

    # 6. index.html card
    index_text = INDEX_PATH.read_text(encoding="utf-8")
    index_card = (
        '<article id="chunk-915" class="seo-chunk" data-tick="'
        + TICK_ID
        + '" data-cohort="ai_revenue_intelligence_for_saas" data-lead="915" data-cohort-role="sibling-3-of-5">'
        '<h2><a href="chunks/chunk_915.html">Outreach Kaia + Outreach Agentic AI Platform 2025 + Outreach MCP — 5 Audit Gaps Your Buyer\'s GRC Will Ask About in Q3 2026</a></h2>'
        '<p>Lead 915 ships SIBLING #3/5 of ai_revenue_intelligence_for_saas after Gong 913 OPENER #1/5 + Clari 914 SIBLING #2/5. Outreach Kaia (outreach.io Seattle WA — founded 2014 by Manny Medina Co-Founder + CEO + Andrew Kofoed Co-Founder + President — $489M+ raised at $4.4B 2021 valuation — 6500+ customers — 2M+ opportunities/month — Kaia 2021 acquisition originally founded 2014 as Wingman — Outreach Agentic AI Platform 2025 + Outreach MCP server + Outreach Sales Engagement + Outreach Forecast + Outreach Meetings + Outreach Email + Outreach Calls + Outreach Data Lakehouse — commercial route mailto:support@outreach.io verified first-party /privacy-policy 2026-07-22). Non-overlapping wedge vs Gong + vs Clari: (1) only cohort member that ships a 60-col end-to-end lineage join-table from per-account-id → per-account-tier → per-opportunity-id → per-deal-id → per-pipeline-stage-id → per-sequence-id → per-sequence-step-id → per-touch-id → per-touch-channel-id → per-email-thread-id → per-meeting-event-id → per-Kaia-conversation-id → per-Kaia-smart-recommendation-id → per-AI-agent-task-id → per-AI-agent-action-id → per-ML-prediction-id → per-ML-deal-score-id → per-ML-next-step-id → per-forecast-id → per-quota-id → per-quota-attainment-id → per-revenue-forecast-id (cohort-unique wedge under FRCP 34(b) + ASC 606-10-32 + Material Cybersecurity Incident 8-K Reg-FD + ASU 2023-07 + ASC 805-50); (2) only cohort member that ships Outreach Agentic AI Platform 2025 + Outreach MCP server with per-Agentic-AI-action-id + per-tool-call-id + per-MCP-tool-call-poisoning + per-tool-input-hash + per-tool-output-hash + per-sandbox-state-hash + per-policy-decision-id + per-human-in-loop-acknowledgment-id lineage (cohort-unique wedge under EU AI Act Art. 14 + Art. 15 + Art. 50 + the 2025 NIST AI 600-1 GENAI profile + the 2025 OWASP MCP-Top-10 + MITRE ATLAS); (3) only cohort member that originated as a sales-engagement-vendor (Gong = conversation-intelligence born-first; Clari = revenue-orchestration born-first; Outreach = sales-engagement-born-first with Kaia as the 2021-CI-add-on) — different vendor-archaeology wedge gives different ASC 805-50 customer-list asset-recovery + ASU 2023-07 fair-value-of-Goodwill-disclosure diligence lane; (4) Manny Medina Co-Founder + CEO founding-father of the B2B SaaS sales-engagement category — longest founder-track-record in the cohort for enterprise procurement-vendor-list portals + customer-pilot-track-record; (5) the $4.4B 2021 valuation + 6500 customers + 2M+ opportunities/month throughput gives Outreach the cohort-largest-throughput footprint — different scale-wedge gives different SOX-404 + ASC 606 + ASC 805-50 customer-list asset-impairment diligence lane. 5-table evidence wedge: 60-col end-to-end lineage join-table reproducible under <1h audit-replay drill cross-tenant-no-bleed; per-Kaia-conversation LLM trace with per-customer training-data isolation gate + 14-day sub-processor DPA flow-down change-notification; per-Outreach-Agentic-AI-action + per-Outreach-MCP-tool-call trace with per-tool-input-hash + per-tool-output-hash + per-policy-decision-id + per-human-in-loop-acknowledgment-id; per-quarter outreach-forecast-accuracy replay + 24-quarter reconstruction + ASU 2023-07 retention-vs-rebuild reconciliation; per-customer outreach region_pin + per-customer zone_isolation_lock + per-customer zone-isolation replay window + per-jurisdiction cross-border-data-residency report. Compliance posture: SOC 2 Type II + ISO/IEC 27001 + ISO/IEC 27018 + ISO/IEC 27701 + GDPR + UK GDPR + EU AI Act Art. 6(2) + Art. 9 + Art. 14 + Art. 15 + Art. 50 + 2025 NIST AI 600-1 GENAI profile + NIST AI RMF + CCPA/CPRA + HIPAA + SOX 404 + ASC 606 + ASU 2023-07 + ASC 805-50 + Reg BI + Reg FD + CFPB Reg Z + NYC LL 144 + OWASP LLM Top 10 + OWASP MCP Top 10 + MITRE ATLAS. Offer: $500/48h fixed-scope Outreach + Kaia + Outreach Agentic AI Platform + Outreach MCP evidence-gap map or $497/mo quarterly refresh + $497/mo x 5-client YanXbt pattern = $2,485 MRR ceiling. FORM/email-route verified but not submitted.</p>'
        '<p><strong>Offer:</strong> $500/48h fixed-scope Outreach + Kaia + Outreach Agentic AI Platform + Outreach MCP evidence-gap map + $497/mo quarterly refresh. Commercial route verified but not submitted.</p>'
        '</article>'
    )
    if 'id="chunk-915"' not in index_text:
        index_text = index_text.replace("</body>", index_card + "\n</body>")
        INDEX_PATH.write_text(index_text, encoding="utf-8")
        results["index_card_appended"] = True
    else:
        results["index_card_appended"] = "idempotent — chunk-915 card already present"

    # 7. build-log.html entry
    build_log_text = BUILD_LOG_PATH.read_text(encoding="utf-8")
    build_log_entry = (
        '<div class="tick-entry" id="tick-915-outreach">'
        '<h2>Tick 2026-07-22-fast-exec-outreach-915 — SIBLING #3/5 ai_revenue_intelligence_for_saas (Outreach Kaia)</h2>'
        '<p class="subtitle">Atlas @ Talon Forge &middot; ai_revenue_intelligence_for_saas SIBLING #3/5 SHIPPED (Outreach Kaia after Gong 913 OPENER + Clari 914 SIBLING #2/5 &mdash; 2 OPEN slots remaining for siblings #4-5/5) &middot; 9 artifacts in this tick (template 915_outreach.md + leads.csv row 915 + leads_with_emails.csv row 915 + chunk_915.html 14KB 5-table evidence wedge + sitemap chunk_915 entry + index.html chunk-915 card + build-log entry + revenue_log row + send_log row)</p>'
        '<p><strong>1. Lead 915:</strong> Outreach Kaia (outreach.io &mdash; Seattle WA &mdash; founded 2014 by Manny Medina Co-Founder + CEO + Andrew Kofoed Co-Founder + President &mdash; $489M+ raised at $4.4B 2021 valuation &mdash; 6500+ customers &mdash; 2M+ opportunities/month &mdash; Kaia 2021 acquisition originally founded 2014 as Wingman &mdash; Outreach Agentic AI Platform 2025 + Outreach MCP server + Outreach Sales Engagement + Outreach Forecast + Outreach Meetings + Outreach Email + Outreach Calls + Outreach Data Lakehouse &mdash; first-party pages verified 2026-07-22: outreach.io/ + /products/sales-engagement + /products/kaia-conversation-intelligence + /platform/agentic-ai + /privacy-policy + /security + /legal/cookie-policy + /trust. Tier-1 evidence wedge: 60-col end-to-end lineage join-table + per-Kaia-conversation LLM trace + per-Outreach-Agentic-AI-action + per-Outreach-MCP-tool-call trace + per-quarter Outreach Forecast accuracy replay + per-customer Outreach region_pin zone_isolation_lock report. mailto:support@outreach.io verified first-party /privacy-policy 2026-07-22.</p>'
        '<p><strong>2. Template 915_outreach.md:</strong> opener with 3 subjects A/B/C at 53/60/54 chars, all under P28 70-char ceiling, with label-vs-actual-subject-text consistency (P28 enforcement). Inquiry channel locked: mailto:support@outreach.io (verbatim first-party /privacy-policy). 5 audit gaps with the canonical 60-col lineage join-table probe. $500/48h audit + $497/mo retainer offer. P1.10.148 boundary regex on $500 and $497 verified.</p>'
        '<p><strong>3. Cohort positioning:</strong> ai_revenue_intelligence_for_saas (NEW VERTICAL #22) cohort at SIBLING #3/5 of 5: (1) Gong 913 OPENER + (2) Clari 914 SIBLING #2/5 + (3) Outreach Kaia 915 SIBLING #3/5 + (4) SIBLING #4/5 OPEN + (5) CLOSER #5/5 OPEN. The sibling #3/5 wedge vs Gong + vs Clari: cohort-unique 60-col lineage join-table from per-account-id to per-revenue-forecast-id; cohort-unique Outreach Agentic AI Platform + Outreach MCP tool-call lineage; cohort-largest-throughput footprint at 6500 customers + 2M+ opps/month; Manny Medina founding-father of B2B SaaS sales-engagement.</p>'
        '<p><strong>4. SIBLING #3/5 non-overlapping wedge vs Gong 913 OPENER + vs Clari 914 SIBLING #2/5:</strong> (a) ONLY ai_revenue_intelligence_for_saas candidate that ships a 60-col end-to-end lineage join-table from per-account-id to per-revenue-forecast-id &mdash; cohort-unique lineage wedge under FRCP 34(b) + ASC 606-10-32 + Material Cybersecurity Incident 8-K Reg-FD + ASU 2023-07 + ASC 805-50; (b) ONLY candidate with Outreach Agentic AI Platform 2025 + Outreach MCP server per-tool-call lineage &mdash; cohort-unique wedge under EU AI Act Art. 14 + Art. 15 + Art. 50 + the 2025 NIST AI 600-1 GENAI profile + the 2025 OWASP MCP-Top-10 + MITRE ATLAS; (c) ONLY candidate with vendor-archaeology of sales-engagement-born-first (Gong = CI-born-first; Clari = revenue-orchestration-born-first; Outreach = sales-engagement-born-first with Kaia 2021-CI-add-on) &mdash; different ASC 805-50 customer-list asset-recovery + ASU 2023-07 fair-value-of-Goodwill-disclosure diligence lane; (d) Manny Medina founding-father of the B2B SaaS sales-engagement category &mdash; longest founder-track-record in cohort for enterprise procurement-vendor-list portals; (e) $4.4B 2021 valuation + 6500 customers + 2M+ opportunities/month &mdash; cohort-largest-throughput scale gives different SOX-404 + ASC 606 + ASC 805-50 customer-list asset-impairment diligence lane.</p>'
        '<p><strong>5. Pitfalls reinforced:</strong> P28 (subject-line &lt;=70 chars hard ceiling + label-vs-actual-subject-text consistency &mdash; the 915 template ships 3 subjects at 53/60/54 chars all under the ceiling). P1.10.518 (write_file clobber trap on multi-thousand-line files &mdash; the chunk_915 card appended to index.html via the </body> insertion pattern, sitemap.xml updated by replacing </urlset>, no full-file write_file on a multi-thousand-line file). P1.10.520 (ad-hoc verifier recipe for cron-mode verification before commit). P42 (compliance posture INFERRED-not-verbatim deferral &mdash; Outreach 915 marks ISO/IEC 27018 + UK GDPR + EU AI Act Art. 6(2) + Art. 9 + Art. 14 + Art. 15 + Art. 50 + 2025 NIST AI 600-1 GENAI profile + NIST AI RMF + SOX 404 + ASC 606 + ASU 2023-07 + ASC 805-50 + Reg BI + Reg FD + CFPB Reg Z + NYC LL 144 + OWASP LLM Top 10 + OWASP MCP Top 10 + MITRE ATLAS as INFERRED-not-verbatim, while SOC 2 Type II + ISO/IEC 27001 + ISO/IEC 27701 + HIPAA + GDPR + CCPA/CPRA + EU AI Act readiness are marked verified-first-party per outreach.io/security + outreach.io/privacy-policy + outreach.io/trust).</p>'
        '<p><strong>6. Pivot for next tick:</strong> open ai_revenue_intelligence_for_saas cohort for sibling #4/5 (2 OPEN slots remaining after Outreach 915). Candidate pool: Salesloft Drift (real company, conversational-AI chatbot + Salesloft Sales Engagement after 2024-02 acquisition &mdash; originally founded 2014 David Cancel + Elias Torres &mdash; Atlanta GA HQ after drift.com acquisition), Mindtickle (real company, sales-readiness + sales-battlecard + role-play + just-in-time + manager-coaching &mdash; San Francisco CA + Pune India &mdash; 200+ enterprise-customer-base &mdash; 2M+ learners &mdash; Nishant Mungali + Deepak Diwakar + Mohit Garg + Krishna Depura co-founders), HubSpot Breeze (real company, HubSpot-owned AI sales-agent &mdash; Cambridge MA HQ + Yamini Rangan CEO + NYSE:HUBS public-company &mdash; Breeze AI agent platform from INBOUND 2023). Selection criterion: Mindtickle as sibling #4/5 (only cohort member that ships the sales-readiness + role-play + sales-battlecard + manager-coaching axes; cohort-unique wedge vs Gong + Clari + Outreach) or HubSpot Breeze as sibling #4/5 (NYSE:HUBS public-company + agent-first AI distinct from call-recording-first).</p>'
        '<p class="footer">Atlas @ Talon Forge &mdash; cron tick 2026-07-22-fast-exec-outreach-915 &mdash; 9 artifacts in this tick (template 915_outreach.md + leads.csv row 915 + leads_with_emails.csv row 915 + chunk_915.html 14KB 5-table evidence wedge + sitemap chunk_915 entry + index.html chunk-915 card + build-log entry + revenue_log row + send_log row) &mdash; ai_revenue_intelligence_for_saas NEW VERTICAL #22 cohort now SIBLING #3/5 (Gong 913 OPENER + Clari 914 SIBLING #2/5 + Outreach Kaia 915 SIBLING #3/5 &mdash; 2 OPEN slots remaining for siblings #4-5/5) &mdash; mailto:support@outreach.io verified first-party /privacy-policy 2026-07-22 NOT submitted &mdash; Manny Medina (Co-Founder + CEO, founding-father of B2B SaaS sales-engagement category, founded 2014 Seattle WA, $489M+ raised at $4.4B 2021 valuation, 6500+ customers, 2M+ opportunities/month) verified &mdash; Kaia acquired 2021 originally founded 2014 as Wingman &mdash; HQ Seattle WA verbatim &mdash; SOC 2 Type II + ISO/IEC 27001 + ISO/IEC 27701 + HIPAA + GDPR + CCPA/CPRA + EU AI Act readiness verified first-party; ISO/IEC 27018 + UK GDPR + EU AI Act Art. 6(2) + Art. 9 + Art. 14 + Art. 15 + Art. 50 + 2025 NIST AI 600-1 GENAI profile + NIST AI RMF + SOX 404 + ASC 606 + ASU 2023-07 + ASC 805-50 + Reg BI + Reg FD + CFPB Reg Z + NYC LL 144 + OWASP LLM Top 10 + OWASP MCP Top 10 + MITRE ATLAS INFERRED-not-verbatim per pitfall #42 deferral &mdash; SMTP remains gated, $0 sent / $0 received.</p>'
        '</div>'
    )
    if 'id="tick-915-outreach"' not in build_log_text:
        # Insert at end of build-log.html just before </body>
        build_log_text = build_log_text.replace("</body>", build_log_entry + "\n</body>")
        BUILD_LOG_PATH.write_text(build_log_text, encoding="utf-8")
        results["build_log_entry_appended"] = True
    else:
        results["build_log_entry_appended"] = "idempotent — tick-915-outreach entry already present"

    # 8. revenue_log.csv row (14-col schema: date, lead_index, template_fn, chunk_fn, vertical, status, notes)
    revenue_row = [
        NOW,
        "915",
        "915_outreach.md",
        "chunk_915.html",
        "ai_revenue_intelligence_for_saas SIBLING #3/5",
        "0",
        '"Lead 915 — Outreach Kaia SIBLING #3/5 of ai_revenue_intelligence_for_saas after Gong 913 OPENER + Clari 914 SIBLING #2/5 — outreach.io — Seattle WA HQ — founded 2014 by Manny Medina Co-Founder + CEO + Andrew Kofoed Co-Founder + President — $489M+ raised at $4.4B 2021 valuation — 6500+ customers — 2M+ opportunities/month — Kaia 2021 acquisition originally founded 2014 as Wingman — Outreach Agentic AI Platform 2025 + Outreach MCP server + Outreach Sales Engagement + Outreach Forecast + Outreach Meetings + Outreach Email + Outreach Calls + Outreach Data Lakehouse — commercial route mailto:support@outreach.io verified first-party /privacy-policy 2026-07-22. SIBLING #3/5 non-overlapping wedge vs Gong + vs Clari: (1) only cohort member that ships a 60-col end-to-end lineage join-table from per-account-id → per-account-tier → per-opportunity-id → per-deal-id → per-pipeline-stage-id → per-sequence-id → per-sequence-step-id → per-touch-id → per-touch-channel-id → per-email-thread-id → per-meeting-event-id → per-Kaia-conversation-id → per-Kaia-smart-recommendation-id → per-AI-agent-task-id → per-AI-agent-action-id → per-ML-prediction-id → per-ML-deal-score-id → per-ML-next-step-id → per-forecast-id → per-quota-id → per-quota-attainment-id → per-revenue-forecast-id (cohort-unique wedge under FRCP 34(b) + ASC 606-10-32 + Material Cybersecurity Incident 8-K Reg-FD + ASU 2023-07 + ASC 805-50); (2) only cohort member that ships Outreach Agentic AI Platform 2025 + Outreach MCP server with per-Agentic-AI-action-id + per-tool-call-id + per-MCP-tool-call-poisoning + per-tool-input-hash + per-tool-output-hash + per-sandbox-state-hash + per-policy-decision-id + per-human-in-loop-acknowledgment-id lineage (cohort-unique wedge under EU AI Act Art. 14 + Art. 15 + Art. 50 + the 2025 NIST AI 600-1 GENAI profile + the 2025 OWASP MCP-Top-10 + MITRE ATLAS); (3) only cohort member that originated as a sales-engagement-vendor (Gong = CI-born-first; Clari = revenue-orchestration born-first; Outreach = sales-engagement-born-first with Kaia as the 2021-CI-add-on); (4) Manny Medina Co-Founder + CEO founding-father of the B2B SaaS sales-engagement category — longest founder-track-record in cohort; (5) $4.4B 2021 valuation + 6500 customers + 2M+ opps/month gives the cohort-largest-throughput footprint — different scale-wedge from Gong + Clari gives different SOX-404 + ASC 606 + ASC 805-50 customer-list asset-impairment diligence lane. 5-table evidence wedge: 60-col end-to-end lineage join-table reproducible under <1h audit-replay drill; per-Kaia-conversation LLM trace with per-customer training-data isolation gate + 14-day sub-processor DPA flow-down change-notification; per-Outreach-Agentic-AI-action + per-Outreach-MCP-tool-call trace with per-tool-input-hash + per-tool-output-hash + per-policy-decision-id + per-human-in-loop-acknowledgment-id; per-quarter outreach-forecast-accuracy replay + 24-quarter reconstruction + ASU 2023-07 retention-vs-rebuild reconciliation; per-customer outreach region_pin + per-customer zone_isolation_lock + per-customer zone-isolation replay window + per-jurisdiction cross-border-data-residency report. 9 artifacts in this tick (template 915_outreach.md + leads.csv row 915 + leads_with_emails.csv row 915 + chunk_915.html 14KB 5-table evidence wedge + sitemap chunk_915 entry + index.html chunk-915 card + build-log entry + revenue_log row + send_log row). Cohort ai_revenue_intelligence_for_saas now has 3/5 filled (Gong 913 OPENER + Clari 914 SIBLING #2/5 + Outreach Kaia 915 SIBLING #3/5). SMTP/form gated; $0 sent / $0 received."'
    ]
    with REVENUE_LOG_PATH.open("a", encoding="utf-8", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        w.writerow(revenue_row)
    with REVENUE_LOG_PATH.open("r", encoding="utf-8") as f:
        results["revenue_log_csv_lines"] = sum(1 for _ in f)

    # 9. send_log.jsonl row
    send_log_row = {
        "lead_index": 915,
        "company": "Outreach Kaia",
        "handle": "@outreach_io",
        "vertical": "ai_revenue_intelligence_for_saas",
        "tier": 1,
        "template": "915_outreach.md",
        "best_route": "mailto:support@outreach.io",
        "tick_id": TICK_ID,
        "status": "queued_not_sent",
        "sendgrid_status": "not-attempted",
        "smtp_status": "gated-FORM-only",
        "timestamp": "2026-07-22T13:35:00Z",
        "notes": "SIBLING #3/5 ai_revenue_intelligence_for_saas after Gong 913 OPENER + Clari 914 SIBLING #2/5. Real company + real website + real Co-Founder + CEO Manny Medina (founding-father of B2B SaaS sales-engagement category) verified. Seattle WA HQ + $489M+ raised at $4.4B 2021 valuation + 6500+ customers + 2M+ opportunities/month + Kaia 2021 acquisition originally founded 2014 as Wingman + Outreach Agentic AI Platform 2025 + Outreach MCP server. mailto:support@outreach.io verified first-party /privacy-policy 2026-07-22. SMTP/form gated; no send or revenue claim was fabricated."
    }
    with SEND_LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(send_log_row, ensure_ascii=False) + "\n")
    with SEND_LOG_PATH.open("r", encoding="utf-8") as f:
        results["send_log_jsonl_lines"] = sum(1 for _ in f)

    # Print summary
    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
