"""Append lead 462 Databricks to leads_with_emails.csv (13-col schema)."""
import csv
from pathlib import Path

REPO = Path("C:/Users/Potts/projects/atlas-store")
CSV = REPO / "cold_email" / "leads_with_emails.csv"
TIER = REPO.parent.parent / "AppData/Local/Temp/lead_462_tier_reason.txt"

tier_reason = TIER.read_text(encoding="utf-8").strip()

row = [
    "462",
    "Databricks",
    "@databricks",
    "databricks.com",
    "https://www.databricks.com/",
    "Ali Ghodsi (Co-Founder + CEO + UC Berkeley AMPLab + Swedish) + Matei Zaharia (Co-Founder + CTO + creator Apache Spark + UC Berkeley Asst Professor + ACM Doctoral Dissertation Award 2014) + Reynold Xin (Co-Founder + Apache Spark PMC) + Patrick Wendell (Co-Founder + Apache Spark PMC) + Andy Konwinski (Co-Founder + Apache Spark PMC + VP Engineering) + Arsalan Tavakoli-Shirazi (Co-Founder + Apache Spark PMC)",
    "ml_ops",
    "1",
    "privacy@databricks.com",
    "privacy@databricks.com",
    "privacy@databricks.com",
    "462_databricks.md",
    tier_reason,
]

with CSV.open("a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(
        f,
        fieldnames=[
            "lead_index", "company", "handle", "domain", "website", "founder",
            "vertical", "tier", "best_email", "emails_found", "guessed_emails",
            "source_template", "tier_reason",
        ],
        quoting=csv.QUOTE_ALL,
    )
    w.writerow(dict(zip([
        "lead_index", "company", "handle", "domain", "website", "founder",
        "vertical", "tier", "best_email", "emails_found", "guessed_emails",
        "source_template", "tier_reason",
    ], row)))

# Verify by reading back
with CSV.open("r", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
last = rows[-1]
print(f"APPENDED leads_with_emails.csv: lead_index={last['lead_index']}, company={last['company']}, founder_col_idx=5, len={len(rows)}")
assert last["lead_index"] == "462"
assert last["company"] == "Databricks"
assert "Ali Ghodsi" in last["founder"]
assert "Matei Zaharia" in last["founder"]
assert "Apache Spark" in last["tier_reason"]
print("VERIFY leads_with_emails.csv: PASS")
