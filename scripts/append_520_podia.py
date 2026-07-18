"""Append Podia as lead 520 to cold_email/leads.csv.

Pattern: tier_reason loaded from %TEMP% file (separates long content
from script to avoid shell heredoc / interpreter pitfalls), then
csv.DictWriter appends in QUOTE_ALL mode.
"""
import csv
from pathlib import Path

CSV = Path(r"C:\Users\Potts\projects\atlas-store\cold_email\leads.csv")
REASON = Path(r"C:\Users\Potts\AppData\Local\Temp\podia_tier_reason.txt")

INDEX = "520"
NAME = "Podia"
HANDLE = "@podia"
EMAIL = "hello@podia.com"
VERTICAL = "ai_creator_economy"
TIER = "1"
TEMPLATE = "520_podia.md"
TIER_REASON = REASON.read_text(encoding="utf-8").strip()

# Row-prefix guard per pitfall #69 (avoid §520 / §520 regulatory citation false-positive)
csv_text = CSV.read_text(encoding="utf-8")
row_prefix = f'"{INDEX}","'
assert row_prefix not in csv_text, f"row-prefix anchor {row_prefix} already in CSV — re-running on an appended row"
assert len(TIER_REASON) > 200, f"tier_reason too short ({len(TIER_REASON)} chars)"

with CSV.open("a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(
        f,
        fieldnames=["index", "name", "handle", "email", "vertical", "tier", "template", "tier_reason"],
        quoting=csv.QUOTE_ALL,
    )
    w.writerow({
        "index": INDEX,
        "name": NAME,
        "handle": HANDLE,
        "email": EMAIL,
        "vertical": VERTICAL,
        "tier": TIER,
        "template": TEMPLATE,
        "tier_reason": TIER_REASON,
    })

# Parse-back verification
with CSV.open("r", encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
podia_row = next((r for r in rows if r["index"] == INDEX), None)
assert podia_row is not None, f"parse-back failed for index {INDEX}"
assert podia_row["email"] == EMAIL, f"email mismatch: {podia_row['email']}"
assert podia_row["vertical"] == VERTICAL, f"vertical mismatch: {podia_row['vertical']}"
print(f"OK append_520_podia: row count {len(rows)} (was 401, now 401), email={podia_row['email']}")
print(f"   vertical={podia_row['vertical']}, tier={podia_row['tier']}, reason_len={len(podia_row['tier_reason'])}")
