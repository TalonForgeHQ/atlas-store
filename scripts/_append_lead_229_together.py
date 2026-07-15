"""Append lead 229 (Together AI) to BOTH leads.csv and leads_with_emails.csv with strict schema discipline."""
import csv
import sys
from pathlib import Path

REPO = Path("C:/Users/Potts/projects/atlas-store")
TIER_REASON_FILE = Path("C:/Users/Potts/AppData/Local/Temp/tier_reason_229_together.txt")
tier_reason = TIER_REASON_FILE.read_text(encoding="utf-8").strip()
# guard: tier_reason must be a single field value, not a CSV row
assert not tier_reason.startswith('"'), f"tier_reason file looks like a CSV row, not a field value: starts with {tier_reason[:20]!r}"
assert "," not in tier_reason[:5], f"tier_reason file appears to start with CSV fields, not a description"

# leads.csv schema: 8 cols
leads_csv = REPO / "cold_email/leads.csv"
leads_row = {
    "index": "229",
    "name": "Together AI",
    "handle": "@togetherai",
    "email": "privacy@together.ai",
    "vertical": "ai_infra",
    "tier": "1",
    "template": "318_together.md",
    "tier_reason": tier_reason,
}

# leads_with_emails.csv schema: 13 cols
emails_csv = REPO / "cold_email/leads_with_emails.csv"
emails_row = {
    "lead_index": "228",  # next free in leads_with_emails.csv (max=227 Pinecone)
    "company": "Together AI",
    "handle": "@togetherai",
    "domain": "together.ai",
    "website": "https://www.together.ai",
    "founder": "Vipul Ved Prakash (CEO, ex-Apple + CloudGenix co-founder) + Ce Zhang (CTO, UChicago CS + Catalyst) + Percy Liang (Chief Scientist, Stanford CRFM + HAI) + Pratyush Kukreti + Daoyuan Wu",
    "vertical": "ai_infra",
    "tier": "1",
    "best_email": "privacy@together.ai",
    "emails_found": "privacy@together.ai",
    "guessed_emails": "",
    "source_template": "318_together.md",
    "tier_reason": tier_reason,
}

# Pre-flight: read both file headers and confirm exact column names
for path, expected_first in [(leads_csv, "index"), (emails_csv, "lead_index")]:
    with path.open(encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
    print(f"[{path.name}] header={header}")
    assert header[0] == expected_first, f"unexpected first column: {header[0]}"

# Pre-flight: dedupe invariant — no row already has the new index
for path, idx_col in [(leads_csv, "index"), (emails_csv, "lead_index")]:
    with path.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    existing_idxs = [r.get(idx_col) for r in rows]
    print(f"[{path.name}] {len(rows)} rows, first 5 idxs={existing_idxs[:5]}, last 5 idxs={existing_idxs[-5:]}")
    print(f"   checking {leads_row['index']!r} in leads: {leads_row['index'] in existing_idxs}")
    print(f"   checking {emails_row['lead_index']!r} in emails: {emails_row['lead_index'] in existing_idxs}")
    if path.name == "leads.csv":
        assert leads_row["index"] not in existing_idxs, f"leads.csv already has index 229 — abort"
    else:
        assert emails_row["lead_index"] not in existing_idxs, f"leads_with_emails.csv already has lead_index 228 — abort"
    print(f"[{path.name}] no duplicate for new index, dedupe invariant clean")

# Append both files
for path, row, fieldnames in [
    (leads_csv, leads_row, ["index", "name", "handle", "email", "vertical", "tier", "template", "tier_reason"]),
    (emails_csv, emails_row, ["lead_index", "company", "handle", "domain", "website", "founder", "vertical", "tier", "best_email", "emails_found", "guessed_emails", "source_template", "tier_reason"]),
]:
    with path.open("a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writerow(row)
    print(f"[{path.name}] wrote index={row.get('index') or row.get('lead_index')}")

# Post-flight: re-parse BOTH files and verify the new row is present, schema is intact, no duplicate
print("\n=== POST-FLIGHT VERIFICATION ===")
for path, idx_col, expected_idx in [(leads_csv, "index", "229"), (emails_csv, "lead_index", "228")]:
    with path.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    last = rows[-1]
    assert last[idx_col] == expected_idx, f"last row index mismatch: expected {expected_idx}, got {last[idx_col]}"
    assert last.get("tier_reason"), "tier_reason missing on new row"
    assert not last["tier_reason"].startswith('"'), f"tier_reason starts with quote (parse-back broken): {last['tier_reason'][:20]!r}"
    idxs = [r.get(idx_col) for r in rows]
    assert len(idxs) == len(set(idxs)), f"DUPLICATE indices found in {path.name}"
    print(f"[{path.name}] OK: {len(rows)} rows, last {idx_col}={last[idx_col]}, tier_reason={len(last['tier_reason'])} chars, no duplicates")

print("\nLEAD 229 (Together AI) APPENDED CLEANLY TO BOTH FILES")
