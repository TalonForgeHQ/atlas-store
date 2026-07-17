"""Append lead 477 (Dovetail) to leads.csv + leads_with_emails.csv."""
import csv, os
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
LEADS = REPO / "cold_email" / "leads.csv"
LEADS_WE = REPO / "cold_email" / "leads_with_emails.csv"
TIER_REASON_FILE = Path(r"C:\Users\Potts\AppData\Local\Temp\tier_reason_477.txt")

INDEX = 477
NAME = "Dovetail"
HANDLE = "@hidovetail"
EMAIL = "legal@dovetail.com"
VERTICAL = "ai_research"
TIER = "1"
TEMPLATE = "477_dovetail.md"

tier_reason = TIER_REASON_FILE.read_text(encoding="utf-8").strip()

# 1. leads.csv (8 cols: index, name, handle, email, vertical, tier, template, tier_reason)
with open(LEADS, "a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(
        f,
        fieldnames=["index", "name", "handle", "email", "vertical", "tier", "template", "tier_reason"],
        quoting=csv.QUOTE_ALL,
    )
    w.writerow({
        "index": str(INDEX),
        "name": NAME,
        "handle": HANDLE,
        "email": EMAIL,
        "vertical": VERTICAL,
        "tier": TIER,
        "template": TEMPLATE,
        "tier_reason": tier_reason,
    })

# 2. leads_with_emails.csv (13 cols: lead_index, company, handle, domain, website, founder, vertical, tier, best_email, emails_found, guessed_emails, source_template, tier_reason)
founder_text = "Benjamin Humphrey (CEO + co-founder); Bradley Ayers (co-founder); CEO Didier Elzinga (May 2025+ revenue-growth phase)"
row_we = {
    "lead_index": str(INDEX),
    "company": NAME,
    "handle": HANDLE,
    "domain": "dovetail.com",
    "website": "https://dovetail.com",
    "founder": founder_text,
    "vertical": VERTICAL,
    "tier": TIER,
    "best_email": EMAIL,
    "emails_found": "1",
    "guessed_emails": "legal@dovetail.com verified live 2026-07-17; hello@ + press@ + privacy@dovetail.com unverified this tick (no mailto: exposed on /privacy /security /contact-sales)",
    "source_template": TEMPLATE,
    "tier_reason": tier_reason,
}

# verify header
with open(LEADS_WE, "r", encoding="utf-8") as f:
    rdr = csv.DictReader(f)
    header = rdr.fieldnames

if list(header) != list(row_we.keys()):
    raise SystemExit(f"leads_with_emails.csv header mismatch: {header}")

with open(LEADS_WE, "a", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=header, quoting=csv.QUOTE_ALL)
    w.writerow(row_we)

# 3. parse-back verification
print("=== parse-back verification ===")
with open(LEADS, "r", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
print(f"leads.csv total rows: {len(rows)}")
last = rows[-1]
print(f"last row index: {last['index']!r}")
print(f"last row email: {last['email']!r}")
print(f"last row template: {last['template']!r}")
print(f"last row tier_reason starts with: {last['tier_reason'][:80]!r}")
assert last["index"] == str(INDEX), f"index mismatch: {last['index']}"
assert last["email"] == EMAIL, f"email mismatch: {last['email']}"
assert last["template"] == TEMPLATE, f"template mismatch: {last['template']}"

with open(LEADS_WE, "r", encoding="utf-8") as f:
    rows_we = list(csv.DictReader(f))
print(f"leads_with_emails.csv total rows: {len(rows_we)}")
last_we = rows_we[-1]
print(f"leads_with_emails last row lead_index: {last_we['lead_index']!r}")
print(f"leads_with_emails last row best_email: {last_we['best_email']!r}")
assert last_we["lead_index"] == str(INDEX), f"WE index mismatch: {last_we['lead_index']}"
assert last_we["best_email"] == EMAIL, f"WE email mismatch: {last_we['best_email']}"

# 4. dedupe invariant check
from collections import Counter
idx_leads = Counter(r.get("index") for r in rows)
idx_we = Counter(r.get("lead_index") for r in rows_we)
dupes_leads = [k for k, v in idx_leads.items() if v > 1]
dupes_we = [k for k, v in idx_we.items() if v > 1]
assert not dupes_leads, f"leads.csv duplicate indices: {dupes_leads}"
assert not dupes_we, f"leads_with_emails.csv duplicate indices: {dupes_we}"

print("\nALL CHECKS PASSED — lead 477 Dovetail appended successfully")
