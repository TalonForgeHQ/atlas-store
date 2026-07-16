"""Append lead 340 Cursor to leads.csv (8-col schema) + leads_with_emails.csv (13-col schema)."""
from pathlib import Path
import csv

REPO = Path("C:/Users/Potts/projects/atlas-store")
LEADS_CSV = REPO / "cold_email" / "leads.csv"
LEADS_WITH_EMAILS_CSV = REPO / "cold_email" / "leads_with_emails.csv"

with open("C:/Users/Potts/AppData/Local/Temp/tick1748Z_lead340.txt", "r", encoding="utf-8") as f:
    payload = f.read().strip()

# Parse payload into 8-col dict: index,name,handle,email,vertical,tier,template,tier_reason
# payload is the csv-wrapped row: "340","Cursor", ... ,"tier_reason..."
# Use csv module to parse it back
import io
sample_row = next(csv.reader(io.StringIO(payload)))
# sample_row has 8 elements: index, name, handle, email, vertical, tier, template, tier_reason
print(f"Parsed payload: {len(sample_row)} fields")
print(f"  index={sample_row[0]}, name={sample_row[1]}, handle={sample_row[2]}, email={sample_row[3]}, vertical={sample_row[4]}, tier={sample_row[5]}, template={sample_row[6]}")
print(f"  tier_reason[:120]={sample_row[7][:120]}")

leads_row = {
    "index": sample_row[0],
    "name": sample_row[1],
    "handle": sample_row[2],
    "email": sample_row[3],
    "vertical": sample_row[4],
    "tier": sample_row[5],
    "template": sample_row[6],
    "tier_reason": sample_row[7],
}

# leads.csv: append with DictWriter
with LEADS_CSV.open("r", encoding="utf-8", newline="") as f:
    rdr = csv.DictReader(f)
    fieldnames = rdr.fieldnames
    print(f"leads.csv fieldnames: {fieldnames}")
    existing_count = sum(1 for _ in rdr)

with LEADS_CSV.open("a", encoding="utf-8", newline="") as f:
    wr = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    wr.writerow(leads_row)
print(f"OK: appended lead {leads_row['index']} {leads_row['name']} to leads.csv (was {existing_count} rows)")

# Verify: parse back
with LEADS_CSV.open("r", encoding="utf-8", newline="") as f:
    rdr = csv.DictReader(f)
    rows = list(rdr)
last = rows[-1]
assert last["index"] == leads_row["index"], f"last index mismatch: {last['index']} != {leads_row['index']}"
assert last["email"] == leads_row["email"], f"email mismatch"
print(f"verify: leads.csv now has {len(rows)} rows, last = {last['index']} {last['name']} ({last['email']})")

# leads_with_emails.csv: 13-col schema
with LEADS_WITH_EMAILS_CSV.open("r", encoding="utf-8", newline="") as f:
    rdr = csv.DictReader(f)
    we_fieldnames = rdr.fieldnames
print(f"leads_with_emails.csv fieldnames: {we_fieldnames}")

we_row = {
    "lead_index": leads_row["index"],
    "company": leads_row["name"],
    "handle": leads_row["handle"],
    "domain": "cursor.com",
    "website": "cursor.com",
    "founder": "Michael Truell + Sualeh Asif + Arvid Lunnemark + Aman Sanger (Co-Founders, ex-MIT CSAIL)",
    "vertical": leads_row["vertical"],
    "tier": leads_row["tier"],
    "best_email": leads_row["email"],
    "emails_found": leads_row["email"],
    "guessed_emails": "",
    "source_template": leads_row["template"],
    "tier_reason": leads_row["tier_reason"],
}
with LEADS_WITH_EMAILS_CSV.open("a", encoding="utf-8", newline="") as f:
    wr = csv.DictWriter(f, fieldnames=we_fieldnames, quoting=csv.QUOTE_ALL)
    wr.writerow(we_row)
print(f"OK: appended lead {we_row['lead_index']} {we_row['company']} to leads_with_emails.csv")

with LEADS_WITH_EMAILS_CSV.open("r", encoding="utf-8", newline="") as f:
    rdr = csv.DictReader(f)
    rows_we = list(rdr)
last_we = rows_we[-1]
assert last_we["lead_index"] == we_row["lead_index"]
print(f"verify: leads_with_emails.csv now has {len(rows_we)} rows, last = {last_we['lead_index']} {last_we['company']} ({last_we['best_email']})")

# Dedupe invariant check (no duplicate indices)
from collections import Counter
leads_dupes = [k for k, c in Counter(r.get("index") for r in rows).items() if c > 1]
we_dupes = [k for k, c in Counter(r.get("lead_index") for r in rows_we).items() if c > 1]
print(f"leads.csv dupes: {leads_dupes}")
print(f"leads_with_emails.csv dupes: {we_dupes}")
assert not leads_dupes, f"DUPES in leads.csv: {leads_dupes}"
assert not we_dupes, f"DUPES in leads_with_emails.csv: {we_dupes}"
print("OK: zero duplicate indices in either file")
