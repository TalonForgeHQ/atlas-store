"""Append Reclaim.ai lead row (index 215) to leads.csv + leads_with_emails.csv."""
import csv
import os
from pathlib import Path

REPO = Path("C:/Users/Potts/projects/atlas-store")
TIER_REASON = (Path(os.environ["TEMP"]) / "tier_reason_215_reclaim.txt").read_text(encoding="utf-8").strip()

# --- leads.csv (8 cols) ---
leads_path = REPO / "cold_email" / "leads.csv"
with leads_path.open("r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    fieldnames = reader.fieldnames

assert "index" in fieldnames, f"leads.csv missing 'index' col, got {fieldnames}"
indices = [r["index"] for r in rows]
assert "215" not in indices, "index 215 already present in leads.csv"

new_row = {
    "index": "215",
    "name": "Reclaim.ai",
    "handle": "@reclaimai",
    "email": "privacy@reclaim.ai",
    "vertical": "b2b_saas",
    "tier": "1",
    "template": "303_reclaim.md",
    "tier_reason": TIER_REASON,
}
assert not new_row["tier_reason"].startswith('"'), "tier_reason must be raw field value, not CSV row"

with leads_path.open("a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    w.writerow(new_row)

# parse-back verify
with leads_path.open("r", encoding="utf-8", newline="") as f:
    rows = csv.DictReader(f)
    last = list(rows)[-1]
assert last["index"] == "215", f"append failed: last index = {last['index']}"
assert last["email"] == "privacy@reclaim.ai", f"email mismatch: {last['email']}"
assert last["tier_reason"].startswith("Canonical AI-calendar"), f"tier_reason wrapped wrong: {last['tier_reason'][:50]}"

# --- leads_with_emails.csv (13 cols) ---
lwe_path = REPO / "cold_email" / "leads_with_emails.csv"
with lwe_path.open("r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    lwe_rows = list(reader)
    lwe_fields = reader.fieldnames

assert lwe_fields[0] == "lead_index", f"leads_with_emails.csv first col is {lwe_fields[0]}, expected lead_index"
assert "215" not in [r["lead_index"] for r in lwe_rows], "lead_index 215 already present in leads_with_emails.csv"

lwe_row = {
    "lead_index": "215",
    "company": "Reclaim.ai",
    "handle": "@reclaimai",
    "domain": "reclaim.ai",
    "website": "https://reclaim.ai",
    "founder": "Henry Shapiro",
    "vertical": "b2b_saas",
    "tier": "1",
    "best_email": "privacy@reclaim.ai",
    "emails_found": "1",
    "guessed_emails": "privacy@reclaim.ai",
    "source_template": "303_reclaim.md",
    "tier_reason": TIER_REASON,
}
with lwe_path.open("a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lwe_fields, quoting=csv.QUOTE_ALL)
    w.writerow(lwe_row)

# parse-back verify both files
for path, idx_col in [(leads_path, "index"), (lwe_path, "lead_index")]:
    with path.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    assert rows[-1][idx_col] == "215", f"{path.name} last row idx != 215"
    dupes = {idx_col: 0}
    from collections import Counter
    counts = Counter(r.get(idx_col) for r in rows)
    dups = {k: v for k, v in counts.items() if v > 1}
    assert not dups, f"{path.name} has duplicate indices: {dups}"

print(f"OK: leads.csv now {len(rows)+1 if False else 'appended'} rows (last idx 215)")
print(f"OK: leads_with_emails.csv appended (last lead_index 215)")
print(f"OK: tier_reason starts: {TIER_REASON[:60]}...")