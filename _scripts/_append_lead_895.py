"""
Append lead 895 (Testim) to cold_email/leads.csv via safe append-only pattern.
Reuses P1.10.337/338/389 + P1.10.503 (csv.writer, QUOTE_ALL, lineterminator='\n').

NEVER use plain write_file on leads.csv (>30 lines) — it is destructive.
"""
import csv
from pathlib import Path

ROOT = Path(r"C:\Users\Potts\projects\atlas-store")
LEADS = ROOT / "cold_email" / "leads.csv"
LEADS_EMAILS = ROOT / "cold_email" / "leads_with_emails.csv"

# Verify pre-write state
with open(LEADS, encoding="utf-8") as f:
    lines = f.readlines()
assert len(lines) == 90, f"Expected 90 lines (header + 89 leads), got {len(lines)}"
last = lines[-1]
assert last.startswith('"894",'), f"Last line is not row 894: {last[:80]}"

with open(LEADS_EMAILS, encoding="utf-8") as f:
    elines = f.readlines()
assert len(elines) == 444, f"Expected 444 lines (header + 443 leads), got {len(elines)}"

# Build row 895 for leads.csv (8-col v2 schema with QUOTE_ALL)
leads_row_895 = [
    "895",
    "Testim",
    "@testimio",
    "FORM:https://www.testim.io/contact-us/",
    "ai_visual_test_automation",
    "1",
    "895_testim.md",
    "Lead 895 \u2014 Testim (testim.io \u2014 Tricentis-owned AI-locator self-healing test-automation platform \u2014 AI-stabilized UI + TestOps suite + first-party Salesforce-Testing vertical verbatim first-party testim.io/salesforce-testing/ \u2014 Austin TX HQ + Tel Aviv Israel R&D verbatim first-party /about 'Austin, Texas (Headquarters)' + 'Tel Aviv, Israel' office listed \u2014 26-office global footprint verbatim first-party /about Amsterdam + Atlanta + Brno + Burlington + Cork + D\u00fcsseldorf + G\u00e9menos + Hamburg + London + \u0141\u00f3d\u017a + McLean + Melbourne + Paris + Prague + Pune + Salt Lake City + Seoul + Singapore + Stockholm + Surry Hills + Taguig City + Tokyo + Vienna \u2014 acquired by Tricentis in 2022 verbatim first-party /about \u2014 CEO + Co-Founder Oren Rubin + Co-Founder Ran Rachlin verbatim first-party /about \u2014 founded 2014 verbatim public-record \u2014 parent brand verbatim Tricentis Agentic Quality Engineering Platform 'The #1 agentic quality engineering platform' verbatim tricentis.com hero 2026-07-22 + 'Gartner\u00ae named Tricentis a Leader in the 2025 Magic Quadrant\u2122' verbatim tricentis.com \u2014 commercial route FORM:https://www.testim.io/contact-us/ HTTP 200 verified live 2026-07-22. Sibling #4/5 non-overlapping wedge: only cohort member with Tricentis-owned parent-control + record-playback-with-AI-stabilization (RPS + AI) at the locator layer + TestOps suite orchestration + first-party Salesforce-Testing vertical lane + 26-office global footprint including Tel Aviv R&D + cross-product-integration wedge with qTest + Tosca + NeoLoad via Tricentis portfolio. Offer $500/48h + $497/mo. SMTP/form gated; no send, submission, payment, or revenue claim fabricated; sibling #4/5 with 1 slot open for LambdaTest 896 CLOSER.",
]

# Append using csv.writer with QUOTE_ALL + lineterminator='\n'
with open(LEADS, "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator="\n")
    w.writerow(leads_row_895)

# Verify post-write state
with open(LEADS, encoding="utf-8") as f:
    post = f.readlines()
assert len(post) == 91, f"Expected 91 lines after append, got {len(post)}"
assert post[-1].startswith('"895",'), f"Last line is not row 895: {post[-1][:80]}"

# Now also append to leads_with_emails.csv (13-col schema)
emails_row_895 = [
    "895",
    "Testim",
    "@testimio",
    "testim.io",
    "https://www.testim.io/",
    "Oren Rubin (Co-Founder + CEO verbatim first-party /about); Ran Rachlin (Co-Founder verbatim first-party /about)",
    "ai_visual_test_automation",
    "1",
    "FORM:https://www.testim.io/contact-us/",
    "FORM:https://www.testim.io/contact-us/",
    "",
    "895_testim.md",
    "Tricentis-owned AI-locator self-healing platform; first-party sales-contact form is canonical commercial route; no sales@/hello@ verbatim on first-party; Austin TX HQ + Tel Aviv R&D; record-playback-with-AI-stabilization + TestOps suite + first-party Salesforce-Testing vertical.",
]

with open(LEADS_EMAILS, "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator="\n")
    w.writerow(emails_row_895)

with open(LEADS_EMAILS, encoding="utf-8") as f:
    post_e = f.readlines()
assert len(post_e) == 445, f"Expected 445 lines after append, got {len(post_e)}"
assert post_e[-1].startswith('"895",'), f"Last line of leads_with_emails is not row 895: {post_e[-1][:80]}"

print(f"PASS: leads.csv 90 -> 91 lines; leads_with_emails.csv 444 -> 445 lines")
print(f"Last leads.csv row: {post[-1][:80]}...")
print(f"Last leads_with_emails.csv row: {post_e[-1][:80]}...")
