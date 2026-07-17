"""Append lead 462 Databricks to leads.csv (8-col schema)."""
import csv
from pathlib import Path

REPO = Path("C:/Users/Potts/projects/atlas-store")
CSV = REPO / "cold_email" / "leads.csv"
TIER = REPO.parent.parent / "AppData/Local/Temp/lead_462_tier_reason.txt"

tier_reason = TIER.read_text(encoding="utf-8").strip()

row = [
    "462",
    "Databricks",
    "@databricks",
    "privacy@databricks.com",
    "ml_ops",
    "1",
    "462_databricks.md",
    tier_reason,
]

with CSV.open("a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(
        f,
        fieldnames=["index", "name", "handle", "email", "vertical", "tier", "template", "tier_reason"],
        quoting=csv.QUOTE_ALL,
    )
    w.writerow(dict(zip(["index", "name", "handle", "email", "vertical", "tier", "template", "tier_reason"], row)))

# Verify by reading back
with CSV.open("r", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
last = rows[-1]
print(f"APPENDED leads.csv: index={last['index']}, name={last['name']}, email={last['email']}, len={len(rows)}")
assert last["index"] == "462"
assert last["name"] == "Databricks"
assert last["email"] == "privacy@databricks.com"
assert "Ali Ghodsi" in last["tier_reason"]
print("VERIFY leads.csv: PASS")
