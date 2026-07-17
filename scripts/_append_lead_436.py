"""Append Lead 436 (ElevenLabs) to BOTH leads.csv (8-col) and leads_with_emails.csv (13-col).
Two-schema append pattern — atlas-store cron recipe.
"""
import csv
from pathlib import Path

REPO = Path("C:/Users/Potts/projects/atlas-store")
LEADS_CSV = REPO / "cold_email" / "leads.csv"
LEADS_WITH_EMAILS_CSV = REPO / "cold_email" / "leads_with_emails.csv"
TIER_REASON_FILE = Path("C:/Users/Potts/AppData/Local/Temp/elevenlabs_tier_reason.txt")

INDEX = "436"
NAME = "ElevenLabs"
HANDLE = "@elevenlabs"
EMAIL = "thor@elevenlabs.io"
VERTICAL = "voice_agents"
TIER = "1"
TEMPLATE_FILE = "436_elevenlabs.md"

# Read tier_reason
tier_reason = TIER_REASON_FILE.read_text(encoding="utf-8").strip()

# --- leads.csv (8 cols) ---
LEADS_CSV.parent.mkdir(parents=True, exist_ok=True)
file_exists_8col = LEADS_CSV.exists()
with open(LEADS_CSV, "a", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["index", "name", "handle", "email", "vertical", "tier", "template", "tier_reason"],
        quoting=csv.QUOTE_ALL,
    )
    if not file_exists_8col:
        writer.writeheader()
    writer.writerow({
        "index": INDEX,
        "name": NAME,
        "handle": HANDLE,
        "email": EMAIL,
        "vertical": VERTICAL,
        "tier": TIER,
        "template": TEMPLATE_FILE,
        "tier_reason": tier_reason,
    })

# Verify leads.csv
with open(LEADS_CSV, "r", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
print(f"leads.csv rows={len(rows)} last_index={rows[-1]['index']} last_email={rows[-1]['email']}")
assert rows[-1]["index"] == INDEX
assert rows[-1]["name"] == NAME
assert rows[-1]["email"] == EMAIL
assert len(rows[-1]["tier_reason"]) >= 5000, f"tier_reason too short: {len(rows[-1]['tier_reason'])}"

# --- leads_with_emails.csv (13 cols) ---
# lead_index, company, handle, domain, website, founder, vertical, tier, best_email, emails_found, guessed_emails, source_template, tier_reason
DOMAIN = "elevenlabs.io"
WEBSITE = "https://elevenlabs.io"
FOUNDER = "Mati Staniszewski + Piotr Dabkowski"
EMAILS_FOUND = "thor@elevenlabs.io;developers@elevenlabs.io;legal@elevenlabs.io"
GUESSED_EMAILS = ""
SOURCE_TEMPLATE = "436_elevenlabs.md"

file_exists_13col = LEADS_WITH_EMAILS_CSV.exists()
with open(LEADS_WITH_EMAILS_CSV, "a", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["lead_index", "company", "handle", "domain", "website", "founder",
                    "vertical", "tier", "best_email", "emails_found", "guessed_emails",
                    "source_template", "tier_reason"],
        quoting=csv.QUOTE_ALL,
    )
    if not file_exists_13col:
        writer.writeheader()
    writer.writerow({
        "lead_index": INDEX,
        "company": NAME,
        "handle": HANDLE,
        "domain": DOMAIN,
        "website": WEBSITE,
        "founder": FOUNDER,
        "vertical": VERTICAL,
        "tier": TIER,
        "best_email": EMAIL,
        "emails_found": EMAILS_FOUND,
        "guessed_emails": GUESSED_EMAILS,
        "source_template": SOURCE_TEMPLATE,
        "tier_reason": tier_reason,
    })

# Verify leads_with_emails.csv
with open(LEADS_WITH_EMAILS_CSV, "r", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
print(f"leads_with_emails.csv rows={len(rows)} last_lead_index={rows[-1]['lead_index']} last_best_email={rows[-1]['best_email']}")
assert rows[-1]["lead_index"] == INDEX
assert rows[-1]["best_email"] == EMAIL
assert rows[-1]["founder"] == FOUNDER

# Dedupe invariant check (Counter on each schema's index column)
from collections import Counter
with open(LEADS_CSV, "r", encoding="utf-8") as f:
    rows_8 = list(csv.DictReader(f))
with open(LEADS_WITH_EMAILS_CSV, "r", encoding="utf-8") as f:
    rows_13 = list(csv.DictReader(f))

dupes_8 = [k for k, c in Counter(r["index"] for r in rows_8).items() if c > 1]
dupes_13 = [k for k, c in Counter(r["lead_index"] for r in rows_13).items() if c > 1]
print(f"dupes: leads.csv={dupes_8}, leads_with_emails.csv={dupes_13}")
assert not dupes_8, f"leads.csv has duplicate indices: {dupes_8}"
assert not dupes_13, f"leads_with_emails.csv has duplicate lead_index: {dupes_13}"

print("OK Lead 436 ElevenLabs appended to BOTH CSVs, dedupe invariant clean")
