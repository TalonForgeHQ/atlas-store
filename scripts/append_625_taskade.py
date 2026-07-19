"""Append lead 625 (Taskade) to both CSVs. Uses csv.writer with QUOTE_MINIMAL."""
import csv
import sys
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
TIER_REASON = REPO.parent.parent.joinpath("AppData", "Local", "Temp", "taskade_content.txt").read_text(encoding="utf-8").strip()

LEADS_CSV = REPO / "cold_email" / "leads.csv"
ENRICHED_CSV = REPO / "cold_email" / "leads_with_emails.csv"

INDEX = 625
NAME = "Taskade"
HANDLE = "@taskade"
EMAIL = "support@taskade.com"
VERTICAL = "ai_agent_builder"
TIER = "1"
TEMPLATE = "625_taskade.md"

# Pre-flight guards
assert '"' not in TIER_REASON, "tier_reason contains unescaped quote"

# Verify row 625 not already in leads.csv
leads_text = LEADS_CSV.read_text(encoding="utf-8")
assert f'{INDEX},' not in leads_text or f'"{INDEX}",' in leads_text, f"Row {INDEX} already in leads.csv"
# Use bare-integer prefix (atlas uses QUOTE_MINIMAL on integer indices)
assert f'{INDEX},' not in leads_text, f"Row {INDEX} already in leads.csv"

# Append to leads.csv
with open(LEADS_CSV, "a", newline="", encoding="utf-8") as f:
    w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    w.writerow([INDEX, NAME, HANDLE, EMAIL, VERTICAL, TIER, TEMPLATE, TIER_REASON])
print(f"[OK] leads.csv: row {INDEX} appended")

# Append to leads_with_emails.csv (13-col schema)
enriched_text = ENRICHED_CSV.read_text(encoding="utf-8")
assert f"{INDEX}," not in enriched_text, f"Row {INDEX} already in leads_with_emails.csv"

# Build 13-col row
domain = "taskade.com"
website = "https://www.taskade.com"
founder = "John Xie (Co-Founder + CEO; Stan Chang Co-Founder + CTO)"
enriched_row = [
    INDEX, NAME, HANDLE, domain, website, founder,
    VERTICAL, TIER, EMAIL, "1", "", TEMPLATE, TIER_REASON
]
with open(ENRICHED_CSV, "a", newline="", encoding="utf-8") as f:
    w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    w.writerow(enriched_row)
print(f"[OK] leads_with_emails.csv: row {INDEX} appended")

# Verify parse-back
import csv as _csv
with open(LEADS_CSV, "r", encoding="utf-8") as f:
    rows = list(_csv.DictReader(f))
matches = [r for r in rows if r.get("index") == str(INDEX)]
assert len(matches) == 1, f"Expected 1 match, got {len(matches)}"
assert matches[0]["name"] == NAME
assert matches[0]["email"] == EMAIL
print(f"[OK] leads.csv parse-back PASS — row {INDEX} = {NAME} / {EMAIL} / {VERTICAL}")

with open(ENRICHED_CSV, "r", encoding="utf-8") as f:
    rows = list(_csv.DictReader(f))
matches = [r for r in rows if r.get("lead_index") == str(INDEX)]
assert len(matches) == 1, f"Expected 1 enriched match, got {len(matches)}"
print(f"[OK] leads_with_emails.csv parse-back PASS — row {INDEX}")

# Count rows
with open(LEADS_CSV, "r", encoding="utf-8") as f:
    lc = sum(1 for _ in f) - 1
with open(ENRICHED_CSV, "r", encoding="utf-8") as f:
    ec = sum(1 for _ in f) - 1
print(f"[OK] leads.csv total rows: {lc}")
print(f"[OK] leads_with_emails.csv total rows: {ec}")
