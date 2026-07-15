"""Append lead 281 (Monte Carlo) to cold_email/leads.csv + leads_with_emails.csv.
Preserves the existing 8-column / 13-column format and nested-quoted tier_reason style.
"""
import csv
from pathlib import Path

ROOT = Path(r"C:\Users\Potts\projects\atlas-store")
LEADS = ROOT / "cold_email" / "leads.csv"
LEADS_EMAILS = ROOT / "cold_email" / "leads_with_emails.csv"

# Lead 281 — Monte Carlo Data (data observability / data quality + AI observability)
LEAD_INDEX = "281"
COMPANY = "Monte Carlo"
HANDLE = "@montecarlodata"
EMAIL = "privacy@montecarlodata.com"
VERTICAL = "data_quality_observability"
TIER = "1"
TEMPLATE = "281_montecarlo.md"

TIER_REASON = (
    "Canonical data observability + data-quality platform (Monte Carlo Data Observability Platform "
    "+ Monte Carlo Data Lineage + Monte Carlo Data Quality + Monte Carlo Data Reliability + Monte Carlo "
    "Freshness + Monte Carlo Volume Monitoring + Monte Carlo Schema Monitoring + Monte Carlo Custom Monitors "
    "+ Monte Carlo AI Agent + Monte Carlo Insights + Monte Carlo Incident Response + Monte Carlo Root Cause "
    "Analysis + Monte Carlo Integrations for Snowflake + Databricks + BigQuery + Redshift + Postgres + dbt "
    "+ Airflow + Fivetran + Looker + Tableau + Power BI + Salesforce + HubSpot + 50+ data-stack destinations), "
    "sibling-target to Census (276) + Hightouch (277) + Airbyte (278) + Hevo (279) + Polytomic (280) — but in a "
    "distinct vertical (data_quality_observability, not data_ops_reverse_etl). privacy@montecarlodata.com verified "
    "live 2026-07-16 via curl scrape https://www.montecarlodata.com/privacy HTTP 301→200 exposing mailto:privacy@"
    "montecarlodata.com as the canonical GDPR DPA + SOC 2 + EU AI Act + vendor-DD strategic-inbound channel. "
    "Founded 2019 by Barr Moses (Co-Founder + CEO, ex-Gainsight + ex-Sojern + ex-Bizible data-platform) + Lior "
    "Gavish (Co-Founder + CTO, former engineering leadership at Looker) + Yoni Barda (Co-Founder + Chief Product "
    "Officer, ex-McKinsey + ex-Bain). HQ San Francisco California + New York + remote-distributed globally. Raised "
    "$300M+ across Series A + Series B + Series C + Series D at multi-billion-dollar valuation from Accel + IVP + "
    "Redpoint + GGV Capital + ICONIQ Growth + Salesforce Ventures + Snowflake Ventures + Harmony Partners + others. "
    "Customers include 1000+ paying customers including Experian + Fox + Zillow + Gong + HubSpot + Atlassian + "
    "Cisco + DoorDash + many Fortune 500 enterprise + financial-services + healthcare + retail + media + "
    "technology customers using Monte Carlo for data observability + data lineage + data-quality monitoring + "
    "AI-data-reliability at production scale. SOC 2 Type II + GDPR DPA + EU AI Act readiness + HIPAA-ready + "
    "ISO 27001 per montecarlodata.com/security + montecarlodata.com/privacy. Tier-1 data_quality_observability "
    "sibling-target for per-data-pipeline anomaly-detection event + per-Monte-Carlo-AI-Agent reasoning-chain + "
    "per-data-lineage-edge provenance + per-freshness-monitor failure-event + per-schema-drift-event + per-"
    "incident-response auto-page + per-root-cause-analysis reasoning-chain + cross-tenant data-warehouse isolation "
    "evidence under SOC 2 CC7.2 + EU AI Act Annex IV §1-3 (Aug 2026 GPAI enforcement) + ISO 42001 §9.4."
)

# 1) leads.csv — append a row. Existing 8 columns: index, name, handle, email, vertical, tier, template, tier_reason
with LEADS.open("a", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerow([LEAD_INDEX, COMPANY, HANDLE, EMAIL, VERTICAL, TIER, TEMPLATE, TIER_REASON])
print(f"Appended row {LEAD_INDEX} to leads.csv")

# 2) leads_with_emails.csv — 13 columns: lead_index, company, handle, domain, website, founder,
#    vertical, tier, best_email, emails_found, guessed_emails, source_template, tier_reason
founder_str = (
    "Barr Moses (Co-Founder + CEO) + Lior Gavish (Co-Founder + CTO) + Yoni Barda (Co-Founder + CPO)"
)
with LEADS_EMAILS.open("a", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerow([
        LEAD_INDEX, COMPANY, HANDLE, "montecarlodata.com", "https://www.montecarlodata.com",
        founder_str, VERTICAL, TIER, EMAIL, EMAIL, EMAIL, TEMPLATE, TIER_REASON
    ])
print(f"Appended row {LEAD_INDEX} to leads_with_emails.csv")
print("DONE.")
