"""Append lead 190 (SambaNova Systems) to cold_email/leads.csv and leads_with_emails.csv.

Pattern: idempotent, reproduces lead-row append if rerun.
"""
import csv

LEADS_CSV = r"C:\Users\Potts\projects\atlas-store\cold_email\leads.csv"
LEADS_WITH_EMAILS_CSV = r"C:\Users\Potts\projects\atlas-store\cold_email\leads_with_emails.csv"

TIER_REASON = "Canonical AI-chip + dataflow-as-a-service vendor (RDU + SN40L + SN40 + SN10 + Samba-1 + Samba-CoE + Composable Intelligence + enterprise on-prem inference). privacy@sambanova.ai directly verified live 2026-07-12 via curl scrape https://www.sambanova.ai/privacy-policy HTTP 200. Founded 2017 Palo Alto by Kunle Olukotun (Stanford) + Christopher Re + Rodrigo Liang (CEO). Raised $1.1B+ at $5B+ valuation. Customers include US DOE Argonne + Lawrence Livermore national labs + DOD + Lockheed Martin + NEC + NTT Data + DigitalOcean + Stanford + Harvard + Memorial Sloan Kettering. SOC 2 Type II + ISO 27001 + GDPR DPA + EU AI Act readiness. 5th ai_infra vertical sibling in pipeline. Distinct because SambaNova is the ONLY AI-chip vendor that ships programmable dataflow (RDU) + open-source foundation-model stack (Samba-CoE) + enterprise on-prem deployment + air-gapped DoD/DoE patterns + per-tenant model/hardware isolation. 5 audit gaps: 14-col per-inference-call provenance join-table per SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4 + Samba-CoE training-data transparency per Art. 53(d) + cross-tenant RDU isolation-evidence + WORM cost-attribution per Annex III 4."

new_row = [
    "190",
    "SambaNova Systems",
    "@SambaNovaAI",
    "privacy@sambanova.ai",
    "ai_infra",
    "1",
    "278_sambanova.md",
    TIER_REASON,
]

# 1. Append to leads.csv (idempotent)
with open(LEADS_CSV, newline='', encoding="utf-8") as f:
    rows = list(csv.reader(f))
existing_indices = {row[0] for row in rows[1:] if row}
if "190" in existing_indices:
    print("[skip] lead 190 already in leads.csv")
else:
    with open(LEADS_CSV, "a", newline='', encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(new_row)
    print(f"[ok] appended lead 190 ({new_row[1]}) to leads.csv")

# 2. Append to leads_with_emails.csv (idempotent)
with open(LEADS_WITH_EMAILS_CSV, newline='', encoding="utf-8") as f:
    werows = list(csv.reader(f))
print(f"leads_with_emails.csv current rows: {len(werows) - 1}")
if werows:
    print(f"leads_with_emails.csv header: {werows[0]}")
existing_wer_indices = {row[0] for row in werows[1:] if row}
if "190" in existing_wer_indices:
    print("[skip] lead 190 already in leads_with_emails.csv")
else:
    with open(LEADS_WITH_EMAILS_CSV, "a", newline='', encoding="utf-8") as f:
        w = csv.writer(f)
        # Match schema of leads_with_emails.csv; truncate tier_reason to keep row lean
        w.writerow([new_row[0], new_row[1], new_row[2], new_row[3], new_row[4], new_row[5], new_row[6], TIER_REASON])
    print(f"[ok] appended lead 190 ({new_row[1]}) to leads_with_emails.csv")

print("Done.")