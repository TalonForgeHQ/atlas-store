import csv, os, sys
from pathlib import Path

CSV_PATH = r"C:\Users\Potts\projects\atlas-store\cold_email\leads_with_emails.csv"

# Read existing rows
with open(CSV_PATH, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

print(f"Current state: {len(rows)} rows, fields: {fieldnames}")
print(f"Last row index: {rows[-1].get('lead_index', '?')}")

# Traceloop (199)
new_row_199 = {
    "lead_index": "199",
    "company": "Traceloop",
    "handle": "@traceloop",
    "domain": "traceloop.com",
    "website": "https://www.traceloop.com",
    "founder": "Nir Gazit (CEO)",
    "vertical": "ai_agents_infra",
    "tier": "1",
    "best_email": "nir@traceloop.com",
    "emails_found": "nir@traceloop.com",
    "guessed_emails": "",
    "source_template": "243_traceloop.md",
    "tier_reason": "Canonical OpenTelemetry-native LLM-observability + OpenLLMetry Apache-2.0 SDK + Traceloop Hub OSS gateway + on-prem/air-gapped deployment + Dynatrace + IBM Instana enterprise partnerships + custom evaluators + auto quality gates platform. nir@traceloop.com (CEO Nir Gazit) directly verified live 2026-07-12 via curl scrape https://www.traceloop.com/contact-us exposing mailto:nir@traceloop.com as the canonical CEO-direct strategic-inbound channel for ai_agents_infra audit-target inquiries. Founded 2022 Tel Aviv by Nir Gazit (CEO, ex-Taboola + ex-Outbrain data-platform lead). HQ Tel Aviv Israel. Raised $7M seed led by Y Combinator + backed by Olivier Pomel (Datadog CEO) + a cohort of observability-leader angels.",
}

# Galileo (200)
new_row_200 = {
    "lead_index": "200",
    "company": "Galileo",
    "handle": "@rungalileo",
    "domain": "galileo.ai",
    "website": "https://www.galileo.ai",
    "founder": "Vikram Chatterji (CEO) + Yash Sheth + Atindriyo Sanyal",
    "vertical": "ai_infra",
    "tier": "1",
    "best_email": "team@galileo.ai",
    "emails_found": "team@galileo.ai|team@galileo.io",
    "guessed_emails": "",
    "source_template": "286_galileo.md",
    "tier_reason": "Canonical RAG-hallucination-detection + LLM-evaluation + LLM-observability platform (Galileo Evaluate + Galileo Observe + Galileo Protect + Galileo Agent Observability + Galileo Chat + Galileo for RAG + Galileo Lens + Galileo Studio + Galileo Pulse). team@galileo.ai + team@galileo.io both directly verified live 2026-07-12 via curl scrape https://www.galileo.ai/privacy-policy HTTP 200 409796 bytes exposing mailto:team@galileo.ai + mailto:team@galileo.io. Founded 2021 NYC by Vikram Chatterji (CEO, ex-Apple Siri ML lead) + Yash Sheth + Atindriyo Sanyal. HQ NYC. Raised $68M Series B led by Insight Partners + joined by Datadog Ventures + ServiceNow Ventures + SentinelOne + BMW i Ventures.",
}

# Check both indices are absent
existing_indices = {r.get("lead_index", "") for r in rows}
assert "199" not in existing_indices, "199 already present"
assert "200" not in existing_indices, "200 already present"

rows.append(new_row_199)
rows.append(new_row_200)

with open(CSV_PATH, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    w.writeheader()
    for r in rows:
        w.writerow(r)

# Parse-back verify
with open(CSV_PATH, "r", encoding="utf-8", newline="") as f:
    parsed = list(csv.DictReader(f))

print(f"OK: appended 199 + 200, file now has {len(parsed)} rows")
print(f"  Row 199 best_email: {parsed[-2]['best_email']}")
print(f"  Row 200 best_email: {parsed[-1]['best_email']}")
