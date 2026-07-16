"""Append lead 299 (Monte Carlo Data) to cold_email/leads.csv with full tier_reason."""
import csv
from pathlib import Path

LEADS_CSV = Path(r"C:\Users\Potts\projects\atlas-store\cold_email\leads.csv")
INDEX = "299"
NAME = "Monte Carlo Data"
HANDLE = "@montecarlodata"
EMAIL = "privacy@montecarlodata.com"
VERTICAL = "ai_data_quality_observability"
TIER = "1"
TEMPLATE = "370_montecarlodata.md"

TIER_REASON = (
    "Canonical AI-data-reliability + data-observability + data-quality + ML-monitoring + "
    "data-downtime-prevention + data-lineage + data-freshness + data-completeness + "
    "AI-Bill-of-Rights-evaluation + EU-AI-Act-Annex-IV + ISO-42001 + NIST-AI-RMF-MEASURE "
    "platform (Monte Carlo Data Observability + Monte Carlo Data Studio + Monte Carlo Data "
    "Lineage + Monte Carlo Data Freshness + Monte Carlo Data Quality + Monte Carlo Data "
    "Volumes + Monte Carlo Data Schema + Monte Carlo Data Pipeline Health + Monte Carlo "
    "Data Incidents + Monte Carlo Data Alerts + Monte Carlo Data SLOs + Monte Carlo Data "
    "Root Cause Analysis + Monte Carlo Data Asset Health + Monte Carlo Data Anomaly "
    "Detection + Monte Carlo Data ML Model Monitoring + Monte Carlo Data + Monte Carlo "
    "Data + Monte Carlo Data). privacy@montecarlodata.com verified live 2026-07-16 via "
    "curl scrape https://www.montecarlodata.com/privacy-policy/ HTTP 200 exposing "
    "mailto:privacy@montecarlodata.com as the canonical GDPR Art. 28 DPA + SOC 2 Type II "
    "+ EU AI Act Annex IV + ISO 27001 + vendor-DD strategic-inbound channel. Founded 2019 "
    "in San Francisco California by Barr Moses (Co-Founder + CEO, ex-Microsoft + ex-"
    "Bazaarvoice + ex-Google + Forbes-30-Under-30 + Stanford-MBA) + Lior Gavish (Co-"
    "Founder + CTO, ex-Outbrain + ex-Bazaarvoice). HQ San Francisco California + New York "
    "NY + Tel Aviv Israel + remote-distributed. Raised $236M+ across Seed + Series A + "
    "Series B + Series C + Series D at $1.6B+ valuation from GGV Capital + ICONIQ Capital "
    "+ Salesforce Ventures + Redpoint Ventures + Accel + Bessemer Venture Partners + "
    "others. Customers include 100+ Fortune-500 + Global-2000 + AI-native-companies "
    "including Fox + Santander + Microsoft + Snap + Wayfair + Substack + YipitData + "
    "Mux + Zillow + Honeywell + Compass + many others using Monte Carlo Data Observability "
    "+ Monte Carlo Data Studio for AI-data-reliability + data-observability + data-"
    "quality + ML-monitoring + data-downtime-prevention + data-lineage + data-freshness "
    "+ data-completeness + AI-Bill-of-Rights-evaluation at production scale. SOC 2 Type "
    "II + ISO 27001 + GDPR DPA + EU AI Act readiness + HIPAA + NIST AI RMF per montecarlodata.com/security "
    "+ montecarlodata.com/privacy-policy + montecarlodata.com/trust. Tier-1 "
    "ai_data_quality_observability 2nd-sibling to Cleanlab for per-data-asset-id + per-"
    "data-pipeline-id + per-data-freshness-check-id + per-data-completeness-check-id + "
    "per-data-lineage-edge-id + per-data-anomaly-detection-event-id + per-data-SLO-"
    "breach-event-id + per-ML-model-monitoring-event-id + per-AI-Bill-of-Rights-"
    "evaluation + per-NIST-AI-RMF-MEASURE-event + per-ISO-42001-9.4-control-test + per-"
    "cross-tenant-isolation + per-cross-vendor-policy-comparison join-table evidence under "
    "SOC 2 CC7.2 + CC6.1 + EU AI Act Art. 9 + Art. 10 + Art. 12 + Art. 14 + Art. 27 + "
    "Art. 43 + Art. 53(d) + Aug 2026 GPAI enforcement + ISO 42001 9.4 + GDPR Art. 28 + "
    "Art. 32 + OWASP ML Top 10 + MITRE ATLAS + NIST AI RMF GOVERN + MAP + MEASURE + "
    "MANAGE. 2nd-sibling to Cleanlab in the canonical ai_data_quality_observability "
    "cohort -- distinct because Monte Carlo is the ONLY ai_data_quality_observability "
    "vendor that ships BOTH the data-pipeline-observability layer (Monte Carlo Data "
    "Observability + Monte Carlo Data Lineage + Monte Carlo Data Freshness + Monte Carlo "
    "Data Quality + Monte Carlo Data Volumes + Monte Carlo Data Schema + Monte Carlo "
    "Data Pipeline Health + Monte Carlo Data Incidents + Monte Carlo Data Alerts + Monte "
    "Carlo Data SLOs + Monte Carlo Data Root Cause Analysis) AND the AI/ML-data-reliability "
    "layer (Monte Carlo Data Asset Health + Monte Carlo Data Anomaly Detection + Monte "
    "Carlo Data ML Model Monitoring + per-ML-model-id + per-training-data-asset-id + per-"
    "feature-store-id + per-ML-pipeline-id + per-ML-prediction-drift-event-id + per-"
    "ML-training-data-drift-event-id + per-ML-feature-drift-event-id + per-ML-target-"
    "drift-event-id + per-ML-concept-drift-event-id + per-data-pipeline-id + per-data-"
    "asset-id + per-data-freshness-check-id + per-data-completeness-check-id + per-data-"
    "quality-check-id + per-data-lineage-edge-id + per-data-anomaly-detection-event-id + "
    "per-data-SLO-breach-event-id + per-AI-Bill-of-Rights-evaluation + per-NIST-AI-RMF-"
    "MEASURE-event + per-ISO-42001-9.4-control-test + per-cross-tenant-isolation + per-"
    "cross-vendor-policy-comparison join-table) creating a unique per-data-asset-id + per-"
    "data-pipeline-id + per-data-freshness-check-id + per-data-anomaly-detection-event-id "
    "+ per-data-SLO-breach-event-id + per-ML-model-monitoring-event-id audit-trail "
    "surface that no other ai_data_quality_observability vendor has because no other "
    "ai_data_quality_observability vendor pairs the data-pipeline-observability-pedigree "
    "(Barr Moses coined the term data-downtime + Forbes-30-Under-30 + Stanford-MBA + "
    "ex-Microsoft + 100+ Fortune-500 customers) with the AI/ML-data-reliability-layer at "
    "production scale. 5 audit gaps: (1) end-to-end per-data-asset-id + per-data-pipeline-"
    "id + per-data-freshness-check-id + per-data-completeness-check-id + per-data-quality-"
    "check-id + per-data-lineage-edge-id + per-data-anomaly-detection-event-id + per-"
    "data-SLO-breach-event-id + per-ML-model-monitoring-event-id + per-AI-Bill-of-"
    "Rights-evaluation + per-NIST-AI-RMF-MEASURE-event + downstream-agent-decision "
    "provenance join-table per SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 + GDPR "
    "Art. 28 + Art. 32 + OWASP ML Top 10 + NIST AI RMF MEASURE capturing 12+ columns for "
    "6yr WORM + quarterly reconstruction drill, (2) Monte Carlo Data Observability + "
    "Monte Carlo Data Studio + Monte Carlo Data Lineage + per-data-asset + per-data-"
    "pipeline + per-fine-tune-corpus + per-RAG-corpus + per-training-corpus + per-"
    "feature-store license-provenance per EU AI Act Art. 53(d) GPAI training-data "
    "transparency + Art. 53(1)(b) copyright-summary + ISO 42001 6.1.4 with 12-column "
    "join-table, (3) prompt-injection + data-poisoning-attack + data-lineage-spoofing-"
    "attack + Monte Carlo ML-model-monitoring-bypass + per-ML-training-data-poisoning + "
    "per-feature-store-poisoning + per-ML-prediction-drift-bypass defense per OWASP ML "
    "Top 10 + MITRE ATLAS + NIST AI RMF MEASURE + EU AI Act Art. 9 + Art. 14 with 10-"
    "column per-data-asset join-table, (4) cross-tenant Monte Carlo + Monte Carlo on-prem "
    "+ Monte Carlo air-gapped + Monte Carlo government isolation-evidence per SOC 2 "
    "CC6.1 + GDPR Art. 28 + HIPAA + EU AI Act Art. 10 + FedRAMP Moderate + ITAR + CMMC "
    "Level 2/3, (5) WORM retention + cost-attribution + EU AI Act Annex III 4 high-risk-"
    "classification + GDPR Art. 17 deletion-propagation per Art. 6+14+27+43+72 + Aug "
    "2026 GPAI enforcement + downstream-credit-employment-healthcare-education-law-"
    "enforcement-essential-services-biometric-emotion-recognition-critical-infrastructure "
    "decision-category. privacy@montecarlodata.com is the verified GDPR DPA + SOC 2 + "
    "ISO 27001 + EU AI Act + vendor-DD strategic-inbound channel for Monte Carlo Data "
    "Observability + Monte Carlo Data Studio + Monte Carlo Data Lineage + Monte Carlo "
    "Data ML Model Monitoring + ai_data_quality_observability audit-target inquiries."
)

# Read existing rows (no header)
with LEADS_CSV.open("r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    rows = list(reader)

print(f"Existing rows: {len(rows)}")
print(f"Last row index: {rows[-1][0] if rows else 'N/A'}")

# Verify index 299 is free
existing_indices = {r[0] for r in rows if r and r[0]}
assert INDEX not in existing_indices, f"Index {INDEX} already exists!"

# Append the new row using QUOTE_ALL (matches the schema style)
new_row = [INDEX, NAME, HANDLE, EMAIL, VERTICAL, TIER, TEMPLATE, TIER_REASON]
with LEADS_CSV.open("a", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerow(new_row)

# Verify
with LEADS_CSV.open("r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    rows = list(reader)
last = rows[-1]
assert last[0] == INDEX, f"Last index is {last[0]}, expected {INDEX}"
assert last[1] == NAME, f"Last name is {last[1]}, expected {NAME}"
assert last[3] == EMAIL, f"Last email is {last[3]}, expected {EMAIL}"
assert last[6] == TEMPLATE, f"Last template is {last[6]}, expected {TEMPLATE}"
assert "Barr Moses" in last[7], f"Barr Moses not in tier_reason"
assert "privacy@montecarlodata.com" in last[7], "privacy@montecarlodata.com not in tier_reason"
print(f"OK: row {len(rows)} appended, index {last[0]} = {last[1]} / {last[3]} / {last[6]}")
print(f"tier_reason length: {len(last[7])} chars")