import csv
from pathlib import Path

LEAD_CSV = Path(r"C:\Users\Potts\projects\atlas-store\cold_email\leads.csv")
TIER_REASON = Path(r"C:\Users\Potts\AppData\Local\Temp\tier_reason_framer.txt")
ENRICHED_CSV = Path(r"C:\Users\Potts\projects\atlas-store\cold_email\leads_with_emails.csv")

INDEX = "585"

with TIER_REASON.open() as f:
    tier_reason = f.read().strip()

# Both CSVs — different schemas
LEAD_ROW = {
    "index": INDEX,
    "name": "Framer",
    "handle": "@framer",
    "email": "abuse@framer.com",
    "vertical": "ai_design_tools",
    "tier": "1",
    "template": "585_framer.md",
    "tier_reason": tier_reason,
}

ENRICHED_ROW = {
    "lead_index": INDEX,
    "company": "Framer",
    "handle": "@framer",
    "domain": "framer.com",
    "website": "https://www.framer.com",
    "founder": "Koen Bok + Jorn van Dijk (Co-Founders, Amsterdam 2017)",
    "vertical": "ai_design_tools",
    "tier": "1",
    "best_email": "abuse@framer.com",
    "emails_found": "abuse@framer.com (canonical privacy/security/DPA inbox, verified 3 pages); support@framer.com (end-user support, secondary); legal@framer.com (not exposed, inferred)",
    "guessed_emails": "privacy@framer.com (NOT exposed, skip)",
    "source_template": "585_framer.md",
    "tier_reason": tier_reason,
}

with LEAD_CSV.open(newline="", encoding="utf-8") as f:
    text = f.read()

assert f'"{INDEX}","' not in text, f"row {INDEX} already present in leads.csv"
with LEAD_CSV.open("a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(LEAD_ROW.keys()), quoting=csv.QUOTE_ALL)
    w.writerow(LEAD_ROW)

with ENRICHED_CSV.open(newline="", encoding="utf-8") as f:
    text = f.read()
assert f'"{INDEX}","' not in text and f'"{INDEX}",' not in text, f"row {INDEX} already present in leads_with_emails.csv"
with ENRICHED_CSV.open("a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(ENRICHED_ROW.keys()), quoting=csv.QUOTE_ALL)
    w.writerow(ENRICHED_ROW)

# Verify
with LEAD_CSV.open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    rows = [row for row in r if row["index"] == INDEX]
assert len(rows) == 1, f"expected 1 row for {INDEX}, got {len(rows)}"
assert rows[0]["email"] == "abuse@framer.com"
assert rows[0]["tier"] == "1"
print(f"OK: {INDEX} appended to leads.csv + leads_with_emails.csv")
print(f"  email={rows[0]['email']}  tier={rows[0]['tier']}  template={rows[0]['template']}")
print(f"  tier_reason len={len(rows[0]['tier_reason'])} chars")