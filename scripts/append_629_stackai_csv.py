"""Append lead 629 Stack AI to both CSVs with idempotency guards."""
import csv, io, sys
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
TIER_REASON = (Path(r"C:\Users\Potts\AppData\Local\Temp\tier_reason_629.txt").read_text(encoding="utf-8")).strip()
INDEX = "629"
LEAD_NAME = "Stack AI"
HANDLE = "@stackai"
EMAIL = "support@stack-ai.com"
VERTICAL = "ai_agent_builder"
TIER = "1"
TEMPLATE = "629_stackai.md"

# 8-col leads.csv
leads_path = REPO / "cold_email" / "leads.csv"
leads_text = leads_path.read_text(encoding="utf-8")
prefix = f'"{INDEX}","'
assert leads_text.count(prefix) == 0, f"row {INDEX} already present in leads.csv"

with leads_path.open("a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator="\n")
    w.writerow([INDEX, LEAD_NAME, HANDLE, EMAIL, VERTICAL, TIER, TEMPLATE, TIER_REASON])
print(f"[OK] leads.csv row {INDEX} appended")

# 13-col leads_with_emails.csv
lwe_path = REPO / "cold_email" / "leads_with_emails.csv"
lwe_text = lwe_path.read_text(encoding="utf-8")
assert lwe_text.count(f'"{INDEX}",') == 0, f"row {INDEX} already present in leads_with_emails.csv"

with lwe_path.open("a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
    w.writerow([
        INDEX, LEAD_NAME, HANDLE, "stack-ai.com",
        "https://www.stack-ai.com",
        "Bernardo Acevedo (Co-Founder + CEO; Roman Lutsyshyn Co-Founder + CTO)",
        VERTICAL, TIER, EMAIL, EMAIL, "",
        TEMPLATE, TIER_REASON,
    ])
print(f"[OK] leads_with_emails.csv row {INDEX} appended")