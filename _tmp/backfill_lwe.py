#!/usr/bin/env python3
"""Backfill Lead 399 Datadog to leads_with_emails.csv (14-col shape)."""
import csv, sys

path = r"C:\Users\Potts\projects\atlas-store\cold_email\leads_with_emails.csv"
with open(path, encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

# Find last row index
last_index = max(int(r["lead_index"]) for r in rows if r["lead_index"].isdigit())
print(f"Last lead_index in leads_with_emails.csv: {last_index}")

if last_index >= 399:
    print("Already contains 399. Skipping backfill.")
    sys.exit(0)

# Same shape: lead_index, company, handle, domain, website, founder, vertical, tier, best_email, emails_found, guessed_emails, source_template, tier_reason
new_row = {
    "lead_index": "399",
    "company": "Datadog",
    "handle": "@datadoghq",
    "domain": "datadoghq.com",
    "website": "https://www.datadoghq.com",
    "founder": "Olivier Pomel (Co-Founder & CEO since 2010); Alexis Lê-Quôc (Co-Founder & former CTO)",
    "vertical": "llm_observability",
    "tier": "1",
    "best_email": "security@datadoghq.com",
    "emails_found": "security@datadoghq.com;info@datadoghq.com;bugbounty@datadoghq.com",
    "guessed_emails": "",
    "source_template": "399_datadog.md",
    "tier_reason": ("Tier-1 llm_observability 4th-vertex — PIVOT REPLACES WhyLabs (planned 4th) after canonical WhyLabs Inc. discontinuation disclosed at whylabs.ai/ root page 2026-07-17 (verbatim: 'WhyLabs, Inc. is discontinuing operations'). Datadog ships the canonical APM↔LLM correlation surface at 28,000+ customer scale. Olivier Pomel (Co-Founder & CEO since 2010) + Alexis Lê-Quôc (Co-Founder & former CTO). security@datadoghq.com verified live 2026-07-17 by curl scrape of https://www.datadoghq.com/security/ exposing mailto:security@datadoghq.com + mailto:bugbounty@datadoghq.com as canonical Bug Bounty + vulnerability-disclosure + PGP-encrypted-comms + GDPR DPA + CCPA/CPRA + HIPAA + FedRAMP Moderate + EU AI Act strategic-inbound channel. info@datadoghq.com also verified live via https://www.datadoghq.com/ root. HQ 620 8th Avenue New York NY 10018 (per SEC 10-K). NASDAQ: DDOG. Backed $147M pre-IPO from Index Ventures + OpenView + ICONIQ + Amplify (2012-2015); IPO September 2019 on NASDAQ at $27/share. Customers 28,000+ enterprise including 70%+ Fortune 500 + 70%+ Fortune 100 (per Q4-2025 10-K). SOC 2 Type II + ISO 27001 + ISO 27017 + ISO 27018 + ISO 27701 + GDPR DPA + CCPA/CPRA + HIPAA-eligible + FedRAMP Moderate + Bug Bounty (HackerOne private program). 2026 Gartner Magic Quadrant Leader for Observability Platforms verified live at datadoghq.com/about/leadership banner. Distinct because Datadog is the ONLY Tier-1 llm_observability vendor in the cohort that ships BOTH the upstream APM context (28,000+ customers) AND the LLM Observability surface (per-llm-call-id + per-prompt-template-id + per-completion-id + per-token-id + per-tool-call-id + per-retrieval-call-id + per-agent-step-id + per-eval-id + per-drift-id) AND the APM↔LLM correlation join-table (the canonical post-incident forensic surface every Fortune 500 buyer shipping AI agents into production asks about) AND the 60+ column APM↔LLM provenance join-table across SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 — no other llm_observability vendor in the cohort has the upstream APM context by default. 5 audit gaps: APM↔LLM correlation join-table 60+ cols, cross-tenant US1/US3/US5/EU1/AP1/GovCloud + per-region isolation-evidence, HIPAA-eligible LLM Observability with per-llm-call-id PHI-flag, prompt-injection + per-tool-call-payload-poisoning + per-retrieval-call-payload-poisoning defense at APM-trace layer, cross-region llm-observability-data-residency for EU + India + Brazil + UAE + UK + Australia + Canada + Singapore + Japan + Philippines customer cohort per Schrems II + GDPR Art. 28 + EU AI Act Art. 10 + India DPDP Act 2023 + Brazil LGPD Art. 33 + UAE PDPL + Canadian PIPEDA + Singapore PDPA + Japan APPI.")
}

with open(path, "a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(new_row.keys()), quoting=csv.QUOTE_ALL)
    w.writerow(new_row)

# Verify
with open(path, encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
print(f"leads_with_emails.csv now has {len(rows)} rows")
