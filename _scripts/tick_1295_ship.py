#!/usr/bin/env python3
"""Tick 1295 — append tl;dv SIBLING #4/5 of NEW VERTICAL #73 ai_agent_meeting_intelligence.

Preserves the CSV-with-quoted-rows format used by leads.csv (each row is wrapped
in outer double-quotes with internal fields comma-separated, single quotes inside
verbatim first-party copy). Also appends a row to leads_with_emails.csv.
"""
import csv, os, re

ROOT = r"C:\Users\Potts\projects\atlas-store"
LEADS = os.path.join(ROOT, "cold_email", "leads.csv")
LEADS_EMAILS = os.path.join(ROOT, "cold_email", "leads_with_emails.csv")
DOSSIER = os.path.join(ROOT, "cold_email", "1295_tldv_ai_agent_meeting_intelligence.md")

# Read the dossier and extract the long note string
with open(DOSSIER, "r", encoding="utf-8") as f:
    note = f.read().strip()

# Build the row tuple matching leads.csv columns (CSV format string-style)
# Header was: id,company,handle,email_or_form,vertical,sibling_pos,filename,notes
# But the file is not standard csv — each row is wrapped in "..." with quoted fields inside.
# We replicate that exact format by emitting a single line that starts with "1295","tl;dv",...,
# ends with "[tick-1295-tldv-ai-agent-meeting-intelligence-sibling-4-1295]"
row_inner = (
    '"1295",'
    '"tl;dv",'
    '"@tldv_io",'
    '"mailto:support@tldv.io",'
    '"ai_agent_meeting_intelligence",'
    '"4",'
    '"1295_tldv_ai_agent_meeting_intelligence.md",'
    f'"{note}"'
)
# The whole line is wrapped in outer quotes (with embedded quotes already there)
new_leads_line = row_inner + "\n"

# Append to leads.csv (file already ends with newline)
with open(LEADS, "a", encoding="utf-8", newline="") as f:
    f.write(new_leads_line)
print(f"[OK] appended to {LEADS}")

# Now leads_with_emails.csv — this one IS a standard CSV (header row, 8 rows).
# Its columns: id,company,handle,email_or_form,vertical,sibling_pos,vertical_sibling_role,template,enrichment,notes
email_row = [
    "1295",
    "tl;dv",
    "@tldv_io",
    "mailto:support@tldv.io",
    "ai_agent_meeting_intelligence",
    "4",
    "sibling-4-of-5",
    "1295_tldv_ai_agent_meeting_intelligence.md",
    "first-party tldv.io home + pricing 2026-07-25",
    "SIBLING #4/5 ai_agent_meeting_intelligence; 2M+ users + 4.7 G2 + Made-in-Germany + Anthropic partnership + EU AI Act compliance + Golden Kitty Award Product Hunt + 'NO BOT VISIBLE TO OTHER PARTICIPANTS' verbatim tldv.io 2026-07-25; $0 sent / $0 received SMTP/form gated",
]

with open(LEADS_EMAILS, "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(email_row)
print(f"[OK] appended to {LEADS_EMAILS}")

# Verify
with open(LEADS, "r", encoding="utf-8") as f:
    rows = [l for l in f if l.strip()]
print(f"leads.csv row count: {len(rows)}")
print(f"last id in leads.csv: {rows[-1][:40]}")

with open(LEADS_EMAILS, "r", encoding="utf-8") as f:
    r = csv.reader(f)
    erows = list(r)
print(f"leads_with_emails.csv row count: {len(erows)}")
print(f"last id in leads_with_emails.csv: {erows[-1][0]}")
