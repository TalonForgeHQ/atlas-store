import csv, sys, pathlib

REPO = pathlib.Path(r"C:\Users\Potts\projects\atlas-store")
TIER_REASON_FILE = pathlib.Path(r"C:\Users\Potts\AppData\Local\Temp\tier_reason_429_retell.txt")
tier_reason = TIER_REASON_FILE.read_text(encoding="utf-8").strip()

# leads.csv (8 cols)
LEADS_CSV = REPO / "cold_email" / "leads.csv"
with LEADS_CSV.open("r", encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
existing_idxs = [r["index"] for r in rows]
print(f"leads.csv: {len(rows)} rows, max index={max(int(i) for i in existing_idxs)}")

INDEX = "429"
NAME = "Retell AI"
HANDLE = "@retellai"
EMAIL = "rogers@retellai.com"
VERTICAL = "voice_agents"
TIER = "1"
TEMPLATE = "429_retell.md"

new_row = {
    "index": INDEX,
    "name": NAME,
    "handle": HANDLE,
    "email": EMAIL,
    "vertical": VERTICAL,
    "tier": TIER,
    "template": TEMPLATE,
    "tier_reason": tier_reason,
}
assert INDEX not in existing_idxs, f"DUPE: {INDEX} already in leads.csv"
with LEADS_CSV.open("a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(new_row.keys()), quoting=csv.QUOTE_ALL)
    w.writerow(new_row)

# Verify
with LEADS_CSV.open("r", encoding="utf-8", newline="") as f:
    rows2 = list(csv.DictReader(f))
last = rows2[-1]
assert last["index"] == INDEX
assert last["name"] == NAME
assert last["email"] == EMAIL
assert last["tier_reason"].startswith(f"Lead {INDEX} - Retell AI")
print(f"OK leads.csv: {len(rows)} -> {len(rows2)} rows, last={last['index']} ({last['name']})")

# leads_with_emails.csv (13 cols)
LW_CSV = REPO / "cold_email" / "leads_with_emails.csv"
with LW_CSV.open("r", encoding="utf-8", newline="") as f:
    rows_lw = list(csv.DictReader(f))
existing_lw_idxs = [r["lead_index"] for r in rows_lw]
print(f"leads_with_emails.csv: {len(rows_lw)} rows, max lead_index={max(int(i) for i in existing_lw_idxs)}")

new_lw = {
    "lead_index": INDEX,
    "company": NAME,
    "handle": HANDLE,
    "domain": "retellai.com",
    "website": "https://www.retellai.com/",
    "founder": "Bing Zuo (CEO) + Tortank (CTO) + Siddhant (founding engineer)",
    "vertical": VERTICAL,
    "tier": TIER,
    "best_email": EMAIL,
    "emails_found": "1",
    "guessed_emails": "rogers@retellai.com | support@retellai.com | founders@retellai.com",
    "source_template": TEMPLATE,
    "tier_reason": tier_reason,
}
assert INDEX not in existing_lw_idxs, f"DUPE: {INDEX} already in leads_with_emails.csv"
with LW_CSV.open("a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(new_lw.keys()), quoting=csv.QUOTE_ALL)
    w.writerow(new_lw)

# Verify
with LW_CSV.open("r", encoding="utf-8", newline="") as f:
    rows_lw2 = list(csv.DictReader(f))
last_lw = rows_lw2[-1]
assert last_lw["lead_index"] == INDEX
assert last_lw["company"] == NAME
assert last_lw["best_email"] == EMAIL
print(f"OK leads_with_emails.csv: {len(rows_lw)} -> {len(rows_lw2)} rows, last={last_lw['lead_index']} ({last_lw['company']})")

print("DEDUPE OK")
print(f"  leads.csv: 8 cols, last idx {last['index']} ({last['name']})")
print(f"  leads_with_emails.csv: 13 cols, last idx {last_lw['lead_index']} ({last_lw['company']})")