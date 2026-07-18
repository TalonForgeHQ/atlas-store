"""Append Fathom 564 + Fireflies 565 to leads.csv with idempotency guards."""
import csv
import sys
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
CSV = REPO / "cold_email" / "leads.csv"
CONTENT_FILE = Path(r"C:\Users\Potts\AppData\Local\Temp\atlas_564_565_content.txt")

tier_reasons = CONTENT_FILE.read_text(encoding="utf-8").split("\n---\n")

rows = [
    {
        "index": "564",
        "name": "Fathom Analytics",
        "handle": "@fathom",
        "email": "privacy@fathom.video",
        "vertical": "meeting_ai_ops",
        "tier": "2",
        "template": "564_fathom.md",
        "tier_reason": tier_reasons[0].strip(),
    },
    {
        "index": "565",
        "name": "Fireflies.ai",
        "handle": "@firefliesai",
        "email": "support@fireflies.ai",
        "vertical": "meeting_ai_ops",
        "tier": "2",
        "template": "565_fireflies.md",
        "tier_reason": tier_reasons[1].strip(),
    },
]

csv_text = CSV.read_text(encoding="utf-8")
for r in rows:
    idx = r["index"]
    assert f'"{idx}","' not in csv_text, f"row {idx} already exists"

with open(CSV, "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), quoting=csv.QUOTE_ALL)
    for r in rows:
        w.writerow(r)

# Parse-back verification
with open(CSV, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    rows_back = list(reader)

assert len(rows_back) >= 2, f"expected >=2 rows total, got {len(rows_back)}"
for r in rows:
    matches = [x for x in rows_back if x["index"] == r["index"]]
    assert len(matches) == 1, f"row {r['index']} mismatch count={len(matches)}"
    assert matches[0]["email"] == r["email"]
    assert matches[0]["vertical"] == r["vertical"]

# Dedupe invariant
idxs = [r["index"] for r in rows_back]
from collections import Counter
dupes = [k for k, c in Counter(idxs).items() if c > 1]
assert not dupes, f"dupes: {dupes}"

print(f"OK: appended {len(rows)} rows, total={len(rows_back)}, no dupes")
