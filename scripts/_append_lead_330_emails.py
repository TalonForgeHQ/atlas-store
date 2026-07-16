#!/usr/bin/env python3
"""Append lead 330 (Cognigy) to leads_with_emails.csv with the 13-col schema.
Schema: lead_index,company,handle,domain,website,founder,vertical,tier,best_email,emails_found,guessed_emails,source_template,tier_reason
"""
import csv
from pathlib import Path

REPO = Path("C:/Users/Potts/projects/atlas-store")
FILE = REPO / "cold_email" / "leads_with_emails.csv"
TICK_CONTENT = REPO / "_ticks" / "tick_cognigy_330.csv"

# Source row from leads.csv (we already appended there)
with (REPO / "cold_email" / "leads.csv").open("r", encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
lead_row = next(r for r in rows if r["index"] == "330")

# Build the 13-col row for leads_with_emails.csv
row = {
    "lead_index": lead_row["index"],
    "company": lead_row["name"],
    "handle": lead_row["handle"],
    "domain": "cognigy.com",
    "website": "https://www.cognigy.com/",
    "founder": "Philipp Heltewig + Sascha Poggemann",
    "vertical": lead_row["vertical"],
    "tier": lead_row["tier"],
    "best_email": "info@cognigy.com",
    "emails_found": "info@cognigy.com;DPO.Cognigy@twobirds.com",
    "guessed_emails": "",
    "source_template": "330_cognigy.md",
    "tier_reason": lead_row["tier_reason"],
}

# Verify header
with FILE.open("r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    header = reader.fieldnames
    existing_idxs = [r["lead_index"] for r in reader if r.get("lead_index")]

assert "330" not in existing_idxs, "duplicate lead_index 330 in leads_with_emails.csv"
assert list(row.keys()) == header, f"dict keys != header: {list(row.keys())} vs {header}"

# Append
with FILE.open("a", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=header, quoting=csv.QUOTE_ALL)
    writer.writerow(row)

# Parse-back verify
with FILE.open("r", encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
last = rows[-1]
assert last["lead_index"] == "330"
assert last["company"] == "Cognigy"
assert last["best_email"] == "info@cognigy.com"
assert "Philipp Heltewig" in last["founder"]
assert last["vertical"] == "ai_customer_support_agents"
assert "DPO.Cognigy@twobirds.com" in last["emails_found"]

# Dedupe invariant
from collections import Counter
dupes = [k for k, v in Counter(r["lead_index"] for r in rows).items() if v > 1]
assert not dupes, f"duplicate lead_indices: {dupes}"

print(f"OK: appended lead 330 (Cognigy) to leads_with_emails.csv. Total rows: {len(rows)}")
print(f"OK: dedupe invariant: 0 duplicates across all lead_index values")