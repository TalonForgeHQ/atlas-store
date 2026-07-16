"""Append Deepgram lead 381 to cold_email/leads.csv (and a stub to leads_with_emails.csv).
Two-tier pattern: tier_reason content lives in Temp txt file, this script reads it."""
import csv, sys
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
LEADS = REPO / "cold_email" / "leads.csv"
LEADS_WE = REPO / "cold_email" / "leads_with_emails.csv"
TIER_FILE = Path(r"C:\Users\Potts\AppData\Local\Temp\tier_reason_deepgram_381.txt")

tier_reason = TIER_FILE.read_text(encoding="utf-8").strip()

# Row dict matching the 8-col leads.csv schema (verified by header inspection)
row = {
    "index": "381",
    "name": "Deepgram",
    "handle": "@deepgram",
    "email": "security@deepgram.com",
    "vertical": "realtime_voice_video_ai_infra",
    "tier": "1",
    "template": "381_deepgram.md",
    "tier_reason": tier_reason,
}

# Pre-flight dedupe invariant check
existing_idxs = set()
with LEADS.open("r", encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    for existing in r:
        if existing.get("index"):
            existing_idxs.add(existing["index"])
if "381" in existing_idxs:
    print(f"REFUSED: index 381 already exists in leads.csv (existing set size {len(existing_idxs)})")
    sys.exit(1)

with LEADS.open("a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(row.keys()), quoting=csv.QUOTE_ALL)
    w.writerow(row)

# Re-read and verify the row was added correctly
with LEADS.open("r", encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    rows = list(r)
    new_row = rows[-1]
    assert new_row["index"] == "381", f"index mismatch: {new_row['index']}"
    assert new_row["name"] == "Deepgram"
    assert new_row["email"] == "security@deepgram.com"
    assert new_row["vertical"] == "realtime_voice_video_ai_infra"
    assert "Scott Stephenson" in new_row["tier_reason"]
    assert new_row["tier_reason"] == tier_reason, "tier_reason lost data"

print(f"OK leads.csv appended: row index=381 name=Deepgram vertical=realtime_voice_video_ai_infra")
print(f"  tier_reason length={len(new_row['tier_reason'])} chars")
print(f"  leads.csv total rows: {len(rows)}")