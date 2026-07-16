"""Append lead 283 (MindBridge) to BOTH leads.csv (8-col) and leads_with_emails.csv (13-col).
Uses csv.DictWriter with the CORRECT field-name list per file (two-schema trap avoidance).
"""
import csv
from pathlib import Path

LEADS_CSV = Path(r"C:\Users\Potts\projects\atlas-store\cold_email\leads.csv")
LE_CSV = Path(r"C:\Users\Potts\projects\atlas-store\cold_email\leads_with_emails.csv")
TXT = Path(r"C:\Users\Potts\AppData\Local\Temp\tier_reason_283.txt")
TPL_DIR = Path(r"C:\Users\Potts\projects\atlas-store\cold_email\templates")

# Read tier_reason
tier_reason = TXT.read_text(encoding="utf-8").strip()

# === LEADS.CSV (8 cols) ===
leads_fields = ["index", "name", "handle", "email", "vertical", "tier", "template", "tier_reason"]
leads_row = {
    "index": "283",
    "name": "MindBridge",
    "handle": "@MindBridgeAI",
    "email": "privacy@mindbridge.ai",
    "vertical": "ai_finance_audit",
    "tier": "1",
    "template": "283_mindbridge.md",
    "tier_reason": tier_reason,
}

# Pre-flight: check 283 is free
with open(LEADS_CSV) as f:
    existing = list(csv.DictReader(f))
existing_idxs = [r["index"] for r in existing]
assert "283" not in existing_idxs, f"leads.csv already has 283"
assert len(existing_idxs) == len(set(existing_idxs)), f"leads.csv has dupes: {existing_idxs}"
print(f"Pre-flight OK: leads.csv has {len(existing)} rows, no dupes, 283 free")

with open(LEADS_CSV, "a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=leads_fields, quoting=csv.QUOTE_ALL)
    w.writerow(leads_row)

# Verify
with open(LEADS_CSV) as f:
    rows = list(csv.DictReader(f))
assert rows[-1]["index"] == "283"
assert rows[-1]["name"] == "MindBridge"
assert len(set(r["index"] for r in rows)) == len(rows), "DUPES after append!"
print(f"leads.csv OK: {len(rows)} rows, last={rows[-1]['index']} ({rows[-1]['name']})")

# === LEADS_WITH_EMAILS.CSV (13 cols — DIFFERENT SCHEMA) ===
le_fields = [
    "lead_index", "company", "handle", "domain", "website", "founder",
    "vertical", "tier", "best_email", "emails_found", "guessed_emails",
    "source_template", "tier_reason",
]
le_row = {
    "lead_index": "283",
    "company": "MindBridge",
    "handle": "@MindBridgeAI",
    "domain": "mindbridge.ai",
    "website": "https://www.mindbridge.ai",
    "founder": "Stephen DeWitt (CEO, ex-Halogen + ex-Saba + ex-SumTotal + ex-Open Text); Eli Fathi (Co-Founder, ex-DMR Consulting); Solon Angel (Co-Founder + CSO, ex-Interset + ex-IBM DE + ex-DMR)",
    "vertical": "ai_finance_audit",
    "tier": "1",
    "best_email": "privacy@mindbridge.ai",
    "emails_found": "2",
    "guessed_emails": "hello@mindbridge.ai",
    "source_template": "283_mindbridge.md",
    "tier_reason": tier_reason,
}

# Pre-flight: check 283 is free
with open(LE_CSV) as f:
    le_existing = list(csv.DictReader(f))
le_idxs = [r["lead_index"] for r in le_existing]
assert "283" not in le_idxs, f"leads_with_emails.csv already has 283"
assert len(le_idxs) == len(set(le_idxs)), f"leads_with_emails.csv has dupes: {le_idxs}"
print(f"Pre-flight OK: leads_with_emails.csv has {len(le_existing)} rows, no dupes, 283 free")

with open(LE_CSV, "a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=le_fields, quoting=csv.QUOTE_ALL)
    w.writerow(le_row)

# Verify
with open(LE_CSV) as f:
    le_rows = list(csv.DictReader(f))
assert le_rows[-1]["lead_index"] == "283"
assert le_rows[-1]["company"] == "MindBridge"
assert len(set(r["lead_index"] for r in le_rows)) == len(le_rows), "DUPES after append!"
print(f"leads_with_emails.csv OK: {len(le_rows)} rows, last={le_rows[-1]['lead_index']} ({le_rows[-1]['company']})")

print("\n=== BOTH FILES ALIGNED AT 283 ===")
print(f"leads.csv: {len(rows)} rows, max={max(int(r['index']) for r in rows)}")
print(f"leads_with_emails.csv: {len(le_rows)} rows, max={max(int(r['lead_index']) for r in le_rows)}")