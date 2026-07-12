#!/usr/bin/env python
"""Append MotherDuck row 186 to cold_email/leads.csv + leads_with_emails.csv (two-tier pattern)."""
import csv, sys, pathlib
from datetime import datetime

ROOT = pathlib.Path(r"C:/Users/Potts/projects/atlas-store")
TIER_REASON_FILE = pathlib.Path(r"C:/Users/Potts/AppData/Local/Temp/motherduck_tier_reason.txt")
INDEX = 186
COMPANY = "MotherDuck, Inc."
HANDLE = "@motherduck"
EMAIL = "info@motherduck.com"
TIER = "ai_data_warehouse"
TEMPLATE = "266_motherduck.md"

tier_reason = TIER_REASON_FILE.read_text(encoding="utf-8").strip()

# 8-col row for cold_email/leads.csv
row8 = {
    "index": str(INDEX),
    "company": COMPANY,
    "handle": HANDLE,
    "email": EMAIL,
    "tier": TIER,
    "approved": "1",
    "template": TEMPLATE,
    "tier_reason": tier_reason,
}

# 13-col row for cold_email/leads_with_emails.csv (extra enrich fields)
now = datetime.utcnow().isoformat() + "Z"
row13 = dict(row8)
row13.update({
    "verified_date": "2026-07-12",
    "verification_source": "https://motherduck.com/trust-and-security/ + curl scrape mailto:info@motherduck.com + mailto:security@motherduck.com + mailto:contact@gdprlocal.com",
    "page_authority": "60",
    "domain_authority": "55",
    "discovered_at": now,
})

leads_path = ROOT / "cold_email" / "leads.csv"
enriched_path = ROOT / "cold_email" / "leads_with_emails.csv"

LEADS_COLS = ["index", "company", "handle", "email", "tier", "approved", "template", "tier_reason"]
ENRICHED_COLS = LEADS_COLS + [
    "verified_date", "verification_source", "page_authority", "domain_authority", "discovered_at",
]

# 8-col leads.csv append (use QUOTE_ALL to handle commas in tier_reason)
with leads_path.open("a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=LEADS_COLS, quoting=csv.QUOTE_ALL)
    w.writerow(row8)
print(f"[OK] appended row {INDEX} -> {leads_path} (8 cols, tier_reason {len(tier_reason)} chars)")

# 13-col leads_with_emails.csv append
with enriched_path.open("a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=ENRICHED_COLS, quoting=csv.QUOTE_ALL)
    w.writerow(row13)
print(f"[OK] appended row {INDEX} -> {enriched_path} (13 cols)")

# Parse-back verification
import csv as _csv
with leads_path.open("r", encoding="utf-8", newline="") as f:
    rdr = _csv.DictReader(f)
    rows = list(rdr)
    last = rows[-1]
    print(
        f"[VERIFY] leads.csv last row: index={last['index']!r} company={last['company']!r} "
        f"email={last['email']!r} tier={last['tier']!r} template={last['template']!r} "
        f"tier_reason_chars={len(last['tier_reason'])} total_rows={len(rows)}"
    )
    assert last["index"] == str(INDEX), f"row index mismatch: expected {INDEX}, got {last['index']}"
    assert last["tier"] == "ai_data_warehouse", f"tier mismatch: {last['tier']}"
    print("[PASS] parse-back verification OK")

with enriched_path.open("r", encoding="utf-8", newline="") as f:
    rdr = _csv.DictReader(f)
    rows = list(rdr)
    last = rows[-1]
    assert last["index"] == str(INDEX), f"enriched row index mismatch: {last['index']}"
    assert last["tier"] == "ai_data_warehouse", f"enriched tier mismatch: {last['tier']}"
    print(f"[VERIFY] leads_with_emails.csv last row: index={last['index']!r} cols={len(list(rows[-1].keys()))} total_rows={len(rows)}")
    print("[PASS] enriched parse-back verification OK")
