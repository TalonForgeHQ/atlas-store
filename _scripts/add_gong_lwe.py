"""Append lead 913 (Gong.io) to leads_with_emails.csv."""
import csv

row = [
    "913",
    "Gong.io",
    "@Gong_io",
    "gong.io",
    "https://www.gong.io",
    "Amit Bendov (CEO, founded 2015, Tel Aviv) verified Wikipedia + first-party /about",
    "ai_revenue_intelligence_for_saas",
    "1",
    "FORM:https://www.gong.io/contact-sales",
    "",
    "",
    "913_gong.md",
    "Gong commercial route is first-party Contact-Sales FORM only — sales@gong.io NOT publicly published; Gong appears in Fortune 500 procurement-vendor-list portals but the Direct-Customer-inquiry form at /contact-sales is the sanctioned commercial channel. No guessed general-business inbox added.",
]

with open(r"C:\Users\Potts\projects\atlas-store\cold_email\leads_with_emails.csv", "a", newline='', encoding="utf-8") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerow(row)

with open(r"C:\Users\Potts\projects\atlas-store\cold_email\leads_with_emails.csv", "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
print(f"Last 200 chars: {lines[-1][-200:]}")
