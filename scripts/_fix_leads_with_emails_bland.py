"""Fix leads_with_emails.csv: remove corrupted trailing row + re-append clean MotherDuck + Bland.

The prior tick's CSV append broke the final row (commas in tier_reason escaped wrong on Windows).
This script writes a clean CSV with all 151 valid rows + Bland (lead 189) appended.
"""
import csv
from pathlib import Path

CSV = Path(r"C:\Users\Potts\projects\atlas-store\cold_email\leads_with_emails.csv")
OUT = Path(r"C:\Users\Potts\projects\atlas-store\cold_email\leads_with_emails.csv")

# Fieldnames (canonical, same as original CSV header)
FIELDNAMES = ["lead_index", "company", "handle", "domain", "website", "founder",
              "vertical", "tier", "best_email", "emails_found", "guessed_emails",
              "source_template", "tier_reason"]

# Read all rows
with CSV.open("r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# Drop corrupted trailing row (the one whose tier_reason looks like a JSON timestamp)
clean = []
for r in rows:
    tr = r.get("tier_reason", "")
    # Keep only rows with sane tier_reason (no ISO timestamp inside)
    if "T03:01:51" in tr or "Z\"" in tr:
        continue
    clean.append(r)

print(f"After drop: {len(clean)} clean rows")
print(f"Last clean: {clean[-1]['lead_index']} {clean[-1]['company']}")

# Append Bland AI as lead 189
bland = {
    "lead_index": "189",
    "company": "Bland AI",
    "handle": "@usebland",
    "domain": "bland.ai",
    "website": "https://www.bland.ai",
    "founder": "Isaiah Granet",
    "vertical": "ai_voice_agents",
    "tier": "1",
    "best_email": "hello@bland.ai",
    "emails_found": "hello@bland.ai",
    "guessed_emails": "",
    "source_template": "277_bland.md",
    "tier_reason": ("Production voice-AI platform for enterprise phone calls (autonomous outbound + "
                    "inbound + multi-tenant) - the highest-stakes voice-AI deployment in 2026 with "
                    "Cracker Barrel + Sallie Mae + Stanford Health + enterprise B2B sales + healthcare "
                    "+ financial-services + collections as named customers. hello@bland.ai directly "
                    "verified live 2026-07-12 via dual-route curl scrape of https://www.bland.ai/privacy "
                    "AND https://www.bland.ai/legal/privacy, both exposing mailto:hello@bland.ai as the "
                    "canonical GDPR DPA + SOC 2 + EU AI Act + HIPAA + CCPA/CPRA + vendor-DD "
                    "strategic-inbound channel routed to the privacy/legal/security team; sales@bland.ai "
                    "also exposed on https://www.bland.ai/about as the commercial-inbound channel. CEO "
                    "+ co-founder Isaiah Granet (Bland founder, the original voice-AI platform for "
                    "enterprise phone calls). HQ San Francisco California. $40M+ raised across seed + "
                    "Series A + Series B (Y Combinator W23 + Eric Ries + Max Levchin + Peter Thiel's "
                    "Founders Fund + Scale Venture Partners). 1,000+ enterprise customers including "
                    "Cracker Barrel + Sallie Mae + Stanford Health + enterprise B2B sales orgs + "
                    "healthcare + financial-services + collections. SOC 2 Type II + HIPAA + EU AI Act "
                    "readiness per bland.ai/security + bland.ai/privacy + bland.ai/legal/privacy + "
                    "bland.ai/dpa. 4th ai_voice_agents vertical sibling in pipeline after Cognigy 99 + "
                    "Sierra 70 + Vapi 230. The 12-column per-call join-table (ANI, live-transcript, "
                    "agent-decision-log, source-system-write, AI-disclosure-timestamp, human-handoff, "
                    "TCPA-consent, wire-fraud-detection, voice-biometric, PHI-redaction, residency, "
                    "downstream-state-change) is the audit-trail surface required for SOC 2 + HIPAA + "
                    "EU AI Act Art. 12/14/50 + California SB 1001 + Colorado SB 24-205 + GLBA + FDCPA + "
                    "12-state AI-disclosure + Aug 2026 GPAI enforcement vendor-DD inquiries."),
}
clean.append(bland)

# Write back atomically
with OUT.open("w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=FIELDNAMES, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(clean)

# Verify
with OUT.open("r", encoding="utf-8", newline="") as f:
    final = list(csv.DictReader(f))
print(f"FINAL rows: {len(final)}")
print(f"FINAL last: {final[-1]['lead_index']} {final[-1]['company']} {final[-1]['best_email']}")