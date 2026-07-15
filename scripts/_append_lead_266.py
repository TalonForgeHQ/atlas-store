"""Append lead 266 (Voiceflow) to leads.csv + leads_with_emails.csv (two-schema pattern)."""
import csv
from pathlib import Path

REPO = Path("C:/Users/Potts/projects/atlas-store")
LEADS = REPO / "cold_email" / "leads.csv"
LWE = REPO / "cold_email" / "leads_with_emails.csv"
TIER_REASON_FILE = Path("C:/Users/Potts/AppData/Local/Temp/tick174_tier_reason.txt")

index = "266"
name = "Voiceflow"
handle = "@voiceflow"
email = "support@voiceflow.com"
vertical = "ai_agents_infra"
tier = "1"
template = "355_voiceflow.md"
tier_reason = TIER_REASON_FILE.read_text(encoding="utf-8").strip()

# Pre-flight: check no duplicate index
existing_idxs = set()
with LEADS.open("r", encoding="utf-8", newline="") as f:
    for r in csv.DictReader(f):
        v = r.get("index")
        if v:
            existing_idxs.add(v)
if index in existing_idxs:
    raise SystemExit(f"DUPLICATE INDEX: {index} already in leads.csv")

with LEADS.open("a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["index","name","handle","email","vertical","tier","template","tier_reason"], quoting=csv.QUOTE_ALL)
    w.writerow({"index":index,"name":name,"handle":handle,"email":email,"vertical":vertical,"tier":tier,"template":template,"tier_reason":tier_reason})

# Dedupe-invariance verification
rows = list(csv.DictReader(LEADS.open("r", encoding="utf-8", newline="")))
idxs = [r.get("index") for r in rows]
from collections import Counter
dupes = {k:v for k,v in Counter(idxs).items() if v > 1}
if dupes:
    raise SystemExit(f"DUPES after append: {dupes}")
last = rows[-1]
print(f"OK leads.csv: {len(rows)} rows; last={last['index']} {last['name']}; tier_reason_len={len(last['tier_reason'])}; tier_reason_starts_with_quote={last['tier_reason'].startswith(chr(34))}")