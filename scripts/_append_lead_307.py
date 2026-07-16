"""Append lead 307 Together AI to both leads.csv + leads_with_emails.csv."""
import csv
import os
import sys
from pathlib import Path

REPO = Path("C:/Users/Potts/projects/atlas-store")
TIER_REASON_PATH = Path(os.environ["TEMP"]) / "tier_reason_307.txt"

tier_reason = TIER_REASON_PATH.read_text(encoding="utf-8").strip()

# --- leads.csv (8 cols) ---
leads_path = REPO / "cold_email" / "leads.csv"
with leads_path.open("a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(
        f,
        fieldnames=["index", "name", "handle", "email", "vertical", "tier", "template", "tier_reason"],
        quoting=csv.QUOTE_ALL,
    )
    w.writerow({
        "index": "307",
        "name": "Together AI",
        "handle": "@togethercompute",
        "email": "privacy@together.ai",
        "vertical": "ai_inference_platform",
        "tier": "1",
        "template": "307_together.md",
        "tier_reason": tier_reason,
    })

# Parse-back
with leads_path.open(encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
print(f"leads.csv: {len(rows)} rows, last_index={rows[-1]['index']}, name={rows[-1]['name']}")
print(f"tier_reason length: {len(rows[-1]['tier_reason'])} chars (expected: {len(tier_reason)})")
assert rows[-1]["tier_reason"] == tier_reason, "tier_reason roundtrip FAILED"
assert rows[-1]["index"] == "307", "index mismatch"

# --- leads_with_emails.csv (13 cols) ---
leads_emails_path = REPO / "cold_email" / "leads_with_emails.csv"
with leads_emails_path.open("a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(
        f,
        fieldnames=[
            "lead_index", "company", "handle", "domain", "website", "founder",
            "vertical", "tier", "best_email", "emails_found", "guessed_emails",
            "source_template", "tier_reason",
        ],
        quoting=csv.QUOTE_ALL,
    )
    w.writerow({
        "lead_index": "307",
        "company": "Together AI",
        "handle": "@togethercompute",
        "domain": "together.ai",
        "website": "https://www.together.ai",
        "founder": "Vipul Ved Prakash (Co-Founder + CEO, ex-Apple + Cloudflare + Topsy) + Zhangyang Wang (Co-Founder, ex-UT-Austin Professor of ML + co-author of DenseNAS + RepLKNet + RepVGG papers) + Pershing Wang (Co-Founder, ex-Facebook ML infra)",
        "vertical": "ai_inference_platform",
        "tier": "1",
        "best_email": "privacy@together.ai",
        "emails_found": "privacy@together.ai",
        "guessed_emails": "support@together.ai;legal@together.ai;security@together.ai;dpo@together.ai",
        "source_template": "307_together.md",
        "tier_reason": tier_reason,
    })

# Parse-back
with leads_emails_path.open(encoding="utf-8") as f:
    rows2 = list(csv.DictReader(f))
print(f"leads_with_emails.csv: {len(rows2)} rows, last_index={rows2[-1]['lead_index']}, company={rows2[-1]['company']}")
assert rows2[-1]["tier_reason"] == tier_reason, "leads_with_emails tier_reason roundtrip FAILED"
assert rows2[-1]["lead_index"] == "307", "leads_with_emails index mismatch"

print("OK lead 307 Together AI appended to BOTH CSVs.")