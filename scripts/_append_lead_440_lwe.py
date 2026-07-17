"""Append Lead 440 Cresta to leads_with_emails.csv (13-col schema, DIFFERENT from leads.csv)."""
import csv, sys
from pathlib import Path

CSV = Path("cold_email/leads_with_emails.csv")
TIER_REASON_FILE = Path("C:/Users/Potts/AppData/Local/Temp/tier_reason_440_cresta.txt")

tier_reason = TIER_REASON_FILE.read_text(encoding="utf-8").strip()

with CSV.open("r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    header = reader.fieldnames

print(f"header ({len(header)}): {header}")

existing = [int(r["lead_index"]) for r in rows if r["lead_index"].isdigit()]
new_index = max(existing) + 1
print(f"rows={len(rows)}, last lead_index={max(existing)}, using index=440 (matches leads.csv index 440)")

# Override: assign lead_index=440 to match leads.csv's index 440
new_index = 440
assert str(new_index) not in existing

new_row = {
    "lead_index": str(new_index),
    "company": "Cresta",
    "handle": "@cresta",
    "domain": "cresta.ai",
    "website": "https://cresta.ai/",
    "founder": "Tim Shi (Co-Founder) + Zayd Enam (Co-Founder) + Sebastian Thrun (Co-Founder, ex-Stanford AI Lab) + Ping Wu (CEO since 2023, ex-Google CCAI co-founder)",
    "vertical": "voice_agents",
    "tier": "1",
    "best_email": "team@cresta.ai",
    "emails_found": "1",
    "guessed_emails": "team@cresta.ai | cresta-privacy@cresta.ai | ping@cresta.ai | tim@cresta.ai | zayd@cresta.ai | sales@cresta.ai | support@cresta.ai",
    "source_template": "440_cresta.md",
    "tier_reason": tier_reason,
}

with CSV.open("a", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=header, quoting=csv.QUOTE_ALL)
    writer.writerow(new_row)

with CSV.open("r", encoding="utf-8", newline="") as f:
    rows2 = list(csv.DictReader(f))

print(f"after: {len(rows2)} rows, last lead_index={rows2[-1]['lead_index']}, last company={rows2[-1]['company']}")

# Verify last entry fields
last = rows2[-1]
expected_keys = {"lead_index", "company", "handle", "domain", "website", "founder", "vertical", "tier", "best_email", "emails_found", "guessed_emails", "source_template", "tier_reason"}
assert set(last.keys()) == expected_keys, f"keys mismatch: {set(last.keys())} vs {expected_keys}"
print(f"keys match: {set(last.keys()) == expected_keys}")

# Dedupe
from collections import Counter
dupes = [k for k, v in Counter(r["lead_index"] for r in rows2).items() if v > 1]
print(f"dupes: {dupes}")
assert not dupes, f"DUPLICATES: {dupes}"
print("OK: leads_with_emails.csv updated with lead_index 440")
