"""Append Lead 400 Braintrust to leads.csv + leads_with_emails.csv."""
import csv
import os
import sys
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
LEADS_CSV = REPO / "cold_email" / "leads.csv"
LEADS_WITH_EMAILS_CSV = REPO / "cold_email" / "leads_with_emails.csv"
TIER_REASON_FILE = Path(r"C:\Users\Potts\AppData\Local\Temp\tier_reason_400_braintrust.txt")

INDEX = "400"
NAME = "Braintrust"
HANDLE = "@braintrust"
EMAIL = "hello@braintrust.dev"
VERTICAL = "ai_eval_observability"
TIER = "1"
TEMPLATE = "400_braintrust.md"

tier_reason = TIER_REASON_FILE.read_text(encoding="utf-8").strip()

# --- leads.csv ---
with LEADS_CSV.open("r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    header = reader.fieldnames
    rows = list(reader)

assert header == ["index", "name", "handle", "email", "vertical", "tier", "template", "tier_reason"], f"Unexpected leads.csv header: {header}"

# Pre-flight dedupe check
existing_idxs = {r["index"] for r in rows}
assert INDEX not in existing_idxs, f"Index {INDEX} already exists in leads.csv"

new_row = {
    "index": INDEX,
    "name": NAME,
    "handle": HANDLE,
    "email": EMAIL,
    "vertical": VERTICAL,
    "tier": TIER,
    "template": TEMPLATE,
    "tier_reason": tier_reason,
}
rows.append(new_row)

with LEADS_CSV.open("w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=header, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(rows)

print(f"leads.csv: appended index={INDEX} {NAME}, total rows now {len(rows)}")

# --- leads_with_emails.csv ---
with LEADS_WITH_EMAILS_CSV.open("r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    header2 = reader.fieldnames
    rows2 = list(reader)

assert "lead_index" in header2, f"Unexpected leads_with_emails.csv header: {header2}"

existing_idxs2 = {r["lead_index"] for r in rows2}
assert INDEX not in existing_idxs2, f"Index {INDEX} already exists in leads_with_emails.csv"

new_row2 = {
    "lead_index": INDEX,
    "company": NAME,
    "handle": HANDLE,
    "domain": "braintrust.dev",
    "website": "https://www.braintrust.dev/",
    "founder": "Ankur Goyal (Founder & CEO); Bryan Helmig (CTO & Co-Founder); Ion Stoica (Co-Founder)",
    "vertical": VERTICAL,
    "tier": TIER,
    "best_email": EMAIL,
    "emails_found": "hello@braintrust.dev",
    "guessed_emails": "",
    "source_template": TEMPLATE,
    "tier_reason": tier_reason,
}
rows2.append(new_row2)

with LEADS_WITH_EMAILS_CSV.open("w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=header2, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(rows2)

print(f"leads_with_emails.csv: appended lead_index={INDEX} {NAME}, total rows now {len(rows2)}")

# --- parse-back verification ---
with LEADS_CSV.open("r", encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    rows_back = list(r)
last = rows_back[-1]
assert last["index"] == INDEX, f"parse-back failed: last index is {last['index']}"
assert last["name"] == NAME
assert last["email"] == EMAIL
assert last["tier_reason"].startswith("Lead 400"), f"tier_reason truncation: starts with {last['tier_reason'][:30]!r}"
assert "Ankur Goyal" in last["tier_reason"], "tier_reason missing founder name"
print(f"parse-back OK: leads.csv last row index={last['index']} {last['name']} {len(last['tier_reason'])} chars")

with LEADS_WITH_EMAILS_CSV.open("r", encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    rows_back2 = list(r)
last2 = rows_back2[-1]
assert last2["lead_index"] == INDEX
assert last2["best_email"] == EMAIL
assert last2["domain"] == "braintrust.dev"
print(f"parse-back OK: leads_with_emails.csv last row lead_index={last2['lead_index']} {last2['company']} {len(last2['tier_reason'])} chars")

print("DONE")