"""Append lead 192 (Chili Piper) to cold_email/leads.csv and leads_with_emails.csv.

Pattern: idempotent, reproduces lead-row append if rerun.
Two-tier CSV append pattern: tier_reason in Temp .txt, this script reads it
and uses csv.DictWriter(quoting=QUOTE_ALL) to handle embedded commas+quotes.
"""
import csv

LEADS_CSV = r"C:\Users\Potts\projects\atlas-store\cold_email\leads.csv"
LEADS_WITH_EMAILS_CSV = r"C:\Users\Potts\projects\atlas-store\cold_email\leads_with_emails.csv"
TIER_REASON_FILE = r"C:\Users\Potts\AppData\Local\Temp\tier_reason_192_chilipiper.txt"

with open(TIER_REASON_FILE, encoding="utf-8") as f:
    TIER_REASON = f.read().strip()

# Sanity check: tier_reason file must contain description text only,
# NOT a CSV row with embedded quotes that would get double-wrapped.
assert not TIER_REASON.startswith('"'), (
    f"TIER_REASON must be raw description text, not a CSV row. "
    f"First char was: {TIER_REASON[:50]!r}"
)

new_row = [
    "192",
    "Chili Piper",
    "@chilipiper",
    "support@chilipiper.com",
    "scheduling",
    "1",
    "280_chilipiper.md",
    TIER_REASON,
]

# 1. Append to leads.csv (idempotent)
with open(LEADS_CSV, newline='', encoding="utf-8") as f:
    rows = list(csv.reader(f))
existing_indices = {row[0] for row in rows[1:] if row}
if "192" in existing_indices:
    print("[skip] lead 192 already in leads.csv")
else:
    with open(LEADS_CSV, "a", newline='', encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(new_row)
    print(f"[ok] appended lead 192 ({new_row[1]}) to leads.csv")

# 2. Append to leads_with_emails.csv with correct 13-col schema
with open(LEADS_WITH_EMAILS_CSV, newline='', encoding="utf-8") as f:
    werows = list(csv.reader(f))
print(f"leads_with_emails.csv current rows: {len(werows) - 1}")
existing_wer_indices = {row[0] for row in werows[1:] if len(row) == 13}
if "192" in existing_wer_indices:
    print("[skip] lead 192 already in leads_with_emails.csv")
else:
    proper_row = ["192", "Chili Piper", "@chilipiper", "chilipiper.com", "https://www.chilipiper.com", "Alina Trigub", "scheduling", "1", "support@chilipiper.com", "support@chilipiper.com", "", "280_chilipiper.md", TIER_REASON]
    with open(LEADS_WITH_EMAILS_CSV, "a", newline='', encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(proper_row)
    print(f"[ok] appended lead 192 (Chili Piper) to leads_with_emails.csv")

# 3. Verifier: parse back the last row and assert tier_reason is intact
import csv as _csv
with open(LEADS_WITH_EMAILS_CSV, newline='', encoding="utf-8") as f:
    last = list(_csv.DictReader(f))[-1]
assert last["tier_reason"] == TIER_REASON, "tier_reason mismatch after append"
assert not last["tier_reason"].startswith('"'), "tier_reason has stray leading quote"
print(f"[verify] tier_reason len={len(last['tier_reason'])} chars, intact match")

print("Done.")