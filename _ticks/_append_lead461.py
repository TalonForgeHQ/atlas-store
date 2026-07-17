"""Append Lead 461 Domino to leads_with_emails.csv (mirrors leads.csv row)."""
import csv

PATH = r"C:\Users\Potts\projects\atlas-store\cold_email\leads_with_emails.csv"

# Read header
with open(PATH, "r", encoding="utf-8", newline="") as f:
    rdr = csv.reader(f)
    header = next(rdr)
    rows = list(rdr)

# Guard against double-add
if any(r and r[0] == "461" for r in rows):
    print("ALREADY_PRESENT")
    raise SystemExit(0)

new_row = [
    "461",
    "Domino Data Lab",
    "@DominoDataLab",
    "dominodatalab.com",
    "https://www.dominodatalab.com/",
    "Nick Elprin (Co-Founder + CEO + ex-NYTimes + ex-Consors Capital + ex-Bridgewater + ex-Lehman Brothers + Harvard + Princeton + ex-Bloomberg)",
    "ml_ops",
    "1",
    "privacy@dominodatalab.com",
    "privacy@dominodatalab.com",
    "privacy@dominodatalab.com",
    "461_domino.md",
    "Lead 461 - Domino Data Lab ml_ops Tier-1 incumbent #1 NEW VERTICAL (data_catalog cohort saturated at Collibra 458 + Alation 459 + Atlan 460). Founded 2013 SF by Nick Elprin. $243M Series F 2024 (Coatue + Nvidia). 600+ enterprise incl. AstraZeneca + Bayer + Allstate + Moodys + ByteDance + Dell. 11M+ models managed. SOC 2 Type II + ISO 27001 + ISO 27701 + ISO 42001 + GDPR DPA + CCPA/CPRA + HIPAA + PCI DSS + NIST AI RMF + EU AI Act 2026 readiness + Aug 2026 GPAI enforcement + Schrems II + India DPDP Act 2023. 35+ col provenance join-table (per-model-id → per-training-data-id → per-feature-id → per-LLM-call-id → per-RAG-retrieval-id → per-Agent-id → per-tool-call-id → per-tenant-id).",
]

with open(PATH, "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(new_row)

print("APPENDED")
