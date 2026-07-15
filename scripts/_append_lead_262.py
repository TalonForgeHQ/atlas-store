"""Append lead 262 (Agiloft) to leads.csv and leads_with_emails.csv.
Two-tier pattern: long tier_reason in temp .txt, short dict in script.
"""
import csv
import io
import os
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
TIER_REASON_FILE = Path(r"C:\Users\Potts\AppData\Local\Temp\agiloft_tier_reason.txt")
tier_reason = TIER_REASON_FILE.read_text(encoding="utf-8").strip()

# ---- leads.csv (8 cols: index, name, handle, email, vertical, tier, template, tier_reason) ----
leads_path = REPO / "cold_email" / "leads.csv"
with leads_path.open("r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    header = list(reader.fieldnames)
    rows = list(reader)

last_idx = int(rows[-1]["index"]) if rows else 0
expected_idx = last_idx + 1
assert expected_idx == 262, f"expected 262, got {expected_idx}"

new_lead_row = {
    "index": "262",
    "name": "Agiloft",
    "handle": "@agiloft",
    "email": "privacy@agiloft.com",
    "vertical": "legal_ops",
    "tier": "1",
    "template": "351_agiloft.md",
    "tier_reason": tier_reason,
}
assert len(new_lead_row) == len(header) == 8, f"leads.csv schema mismatch: header={len(header)} dict={len(new_lead_row)}"

with leads_path.open("a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=header, quoting=csv.QUOTE_ALL)
    w.writerow(new_lead_row)

# Verify
with leads_path.open("r", encoding="utf-8", newline="") as f:
    rows_v = list(csv.DictReader(f))
assert rows_v[-1]["index"] == "262", f"leads.csv last row index != 262: {rows_v[-1]['index']}"
assert rows_v[-1]["name"] == "Agiloft"
assert rows_v[-1]["email"] == "privacy@agiloft.com"
assert len(rows_v[-1]["tier_reason"]) == len(tier_reason), "tier_reason length mismatch (corrupt?)"
# Dedupe invariant
from collections import Counter
idx_counts = Counter(r["index"] for r in rows_v)
dupes = {k: v for k, v in idx_counts.items() if v > 1}
assert not dupes, f"leads.csv has duplicate indices: {dupes}"
print(f"OK leads.csv appended row 262 Agiloft, total rows={len(rows_v)}, unique indices={len(idx_counts)}")

# ---- leads_with_emails.csv (13 cols) ----
lwe_path = REPO / "cold_email" / "leads_with_emails.csv"
with lwe_path.open("r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    header2 = list(reader.fieldnames)
    rows2 = list(reader)

last_idx2 = int(rows2[-1]["lead_index"]) if rows2 else 0
expected_idx2 = last_idx2 + 1
# Note: leads_with_emails.csv uses lead_index, may be on a different numbering
# but per the cron recipe appends one row per tick matching the leads.csv index

new_lwe_row = {
    "lead_index": "262",
    "company": "Agiloft",
    "handle": "@agiloft",
    "domain": "agiloft.com",
    "website": "https://www.agiloft.com",
    "founder": "Colin Earl (Founder + CEO)",
    "vertical": "legal_ops",
    "tier": "1",
    "best_email": "privacy@agiloft.com",
    "emails_found": "privacy@agiloft.com,marketing@agiloft.com",
    "guessed_emails": "privacy@agiloft.com,marketing@agiloft.com",
    "source_template": "351_agiloft.md",
    "tier_reason": tier_reason,
}
assert len(new_lwe_row) == len(header2) == 13, f"leads_with_emails.csv schema mismatch: header={len(header2)} dict={len(new_lwe_row)}"

with lwe_path.open("a", encoding="utf-8", newline="") as f:
    w2 = csv.DictWriter(f, fieldnames=header2, quoting=csv.QUOTE_ALL)
    w2.writerow(new_lwe_row)

# Verify
with lwe_path.open("r", encoding="utf-8", newline="") as f:
    rows2_v = list(csv.DictReader(f))
assert rows2_v[-1]["lead_index"] == "262"
assert rows2_v[-1]["company"] == "Agiloft"
assert rows2_v[-1]["best_email"] == "privacy@agiloft.com"

idx_counts2 = Counter(r["lead_index"] for r in rows2_v)
dupes2 = {k: v for k, v in idx_counts2.items() if v > 1}
assert not dupes2, f"leads_with_emails.csv has duplicate lead_index: {dupes2}"
print(f"OK leads_with_emails.csv appended row 262 Agiloft, total rows={len(rows2_v)}, unique indices={len(idx_counts2)}")