#!/usr/bin/env python3
"""Append lead 347 (PromptArmor) to cold_email/leads.csv + leads_with_emails.csv + verify dedup."""
import csv
import sys
from pathlib import Path

REPO = Path("C:/Users/Potts/projects/atlas-store")
LEADS = REPO / "cold_email" / "leads.csv"
LEADS_EMAILS = REPO / "cold_email" / "leads_with_emails.csv"
TIER_REASON_FILE = Path("C:/Users/Potts/AppData/Local/Temp/tier_reason_347.txt")

tier_reason = TIER_REASON_FILE.read_text(encoding="utf-8").strip()

# 8-col leads.csv schema: index, name, handle, email, vertical, tier, template, tier_reason
leads_row = {
    "index": "347",
    "name": "PromptArmor",
    "handle": "@PromptArmorAI",
    "email": "privacy@promptarmor.com",
    "vertical": "ai_security_red_teaming_llm",
    "tier": "1",
    "template": "347_promptarmor.md",
    "tier_reason": tier_reason,
}

# 13-col leads_with_emails.csv schema: lead_index, company, handle, domain, website, founder, vertical, tier, best_email, emails_found, guessed_emails, source_template, tier_reason
leads_emails_row = {
    "lead_index": "347",
    "company": "PromptArmor",
    "handle": "@PromptArmorAI",
    "domain": "promptarmor.com",
    "website": "https://www.promptarmor.com",
    "founder": "Chuck Walkup (Co-Founder + CEO)",
    "vertical": "ai_security_red_teaming_llm",
    "tier": "1",
    "best_email": "privacy@promptarmor.com",
    "emails_found": "1",
    "guessed_emails": "privacy@promptarmor.com",
    "source_template": "347_promptarmor.md",
    "tier_reason": tier_reason,
}

for path, row, idx_col in [
    (LEADS, leads_row, "index"),
    (LEADS_EMAILS, leads_emails_row, "lead_index"),
]:
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        existing_rows = list(reader)
    # dedupe invariant check
    keys = [r.get(idx_col) for r in existing_rows]
    if "347" in keys:
        print(f"SKIP: 347 already in {path.name} (position {keys.index('347')})")
        continue
    with path.open("a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writerow(row)
    # parse-back verification
    with path.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    last = rows[-1]
    assert str(last.get(idx_col)) == "347", f"verify FAILED: last {idx_col}={last.get(idx_col)}"
    assert "PromptArmor" in last["name" if idx_col == "index" else "company"]
    assert "Chuck Walkup" in last["tier_reason"] or "Chuck Walkup" in last.get("founder", "")
    print(f"OK: appended 347 to {path.name}; total rows={len(rows)}")

print("DONE")
