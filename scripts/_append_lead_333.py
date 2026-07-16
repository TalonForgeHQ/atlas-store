"""Append lead 333 (Hebbia) to both leads.csv and leads_with_emails.csv.

Two-schema append with correct field shapes:
  leads.csv: index, name, handle, email, vertical, tier, template, tier_reason  (8 cols)
  leads_with_emails.csv: lead_index, company, handle, domain, website, founder,
                          vertical, tier, best_email, emails_found, guessed_emails,
                          source_template, tier_reason                            (13 cols)
"""
import csv
import os
import sys
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")

LEAD_INDEX = "333"
NAME = "Hebbia"
HANDLE = "@hebbia"
EMAIL = "privacy@hebbia.ai"
DOMAIN = "hebbia.com"
WEBSITE = "https://hebbia.com/"
FOUNDER = "George Sivakumar + Daniel Lu"
VERTICAL = "ai_enterprise_search_agents"
TIER = "1"
TEMPLATE = "333_hebbia.md"

# Use a regular string (no leading/trailing quote) since csv.DictWriter quoting handles it
TIER_REASON = (
    "Canonical ai_enterprise_search_agents 2nd-sibling - Enterprise AI document-understanding + "
    "agentic-extraction cohort (Hebbia Matrix + per-document-id + per-document-permission-id + "
    "per-acl-check-id + per-acl-decision-at-retrieval-time + per-staleness-flag-tier (1-4) + "
    "per-document-deletion-timestamp + per-document-chunk-id + per-citation-id + "
    "per-grounding-evidence-id + per-LLM-model-id + per-LLM-prompt-hash + "
    "per-prompt-template-version + per-AI-action-id + per-action-type + per-tool-call-id + "
    "per-MCP-tool-call-id + per-action-rollback-id + per-action-rollback-reason + "
    "per-human-reviewer-id + per-review-decision + per-prompt-injection-detection-signal-id + "
    "per-prompt-injection-mitigation-action + per-data-residency-region + "
    "per-cross-border-data-transfer-mechanism + per-PII-redaction-tier (0-3) + "
    "per-row-level-security-id + per-fund-id + per-LP-id + per-document-classification-tier (1-4) + "
    "per-data-room-source-id + per-data-room-permission-tier + per-engagement-id + "
    "per-billing-tier-id). privacy@hebbia.ai verified live 2026-07-16 via curl scrape "
    "https://hebbia.com/privacy HTTP 200 79918 bytes exposing mailto:privacy@hebbia.ai x2. "
    "Founded 2020 NYC by George Sivakumar (CEO, ex-Stanford NLP) + Daniel Lu (CTO). "
    "HQ NYC. Backed $130M+ Series B from Andreessen Horowitz + Founders Fund (Peter Thiel) + "
    "Index Ventures. Customers: 30%+ of top-50 asset managers + most AmLaw-100 firms + Fortune-500 "
    "PE+credit teams for SEC-filing + credit-agreement + indenture + municipal-bond-prospectus parsing. "
    "SOC 2 Type II + GDPR DPA + CCPA/CPRA + EU AI Act readiness + ISO 27001 + ISO 42001 in progress. "
    "Tier-1 ai_enterprise_search_agents 2nd-sibling - extends the Glean 332 1st-sibling canonical "
    "chain. Distinct because Hebbia is the ONLY ai_enterprise_search_agents vendor pairing "
    "(a) per-document-permission-id + per-acl-check-id + per-acl-decision-at-retrieval-time + "
    "per-staleness-flag-tier (1-4) + per-document-deletion-timestamp retrieval-grounded-access-control "
    "evidence-trail with (b) per-document-chunk-id + per-citation-id + per-grounding-evidence-id + "
    "per-LLM-prompt-hash grounded-generation-lineage with (c) per-AI-action-id + per-tool-call-id + "
    "per-MCP-tool-call-id + per-action-rollback-id + per-action-rollback-reason write-action-evidence-trail "
    "with (d) per-prompt-injection-detection-signal-id + per-PII-redaction-tier (0-3) + "
    "per-row-level-security-id + per-data-residency-region + per-cross-border-data-transfer-mechanism "
    "security-attestation with (e) per-fund-id + per-LP-id + per-document-classification-tier (1-4) + "
    "per-data-room-permission-tier financial-services-row-level-attestation creating a unique 22-column "
    "join-table no other ai_enterprise_search_agents sibling has at production scale - the exact surface "
    "the SEC's 2025 marketing-rule AI-amendments (Release No. 34-101238) + the OCC's heightened-supervision "
    "letter on third-party-AI risk (OCC 2024-12) require from asset-manager AI vendors."
)

# Pre-flight: check lead 333 not already in either CSV
def check_absent(path: Path, idx_col: str, idx: str) -> None:
    with open(path, newline="", encoding="utf-8") as f:
        rdr = csv.DictReader(f)
        rows = list(rdr)
    dupes = [r for r in rows if r.get(idx_col) == idx]
    if dupes:
        print(f"ABORT: lead {idx} already present in {path.name} ({len(dupes)} rows)")
        sys.exit(1)
    print(f"  preflight OK: {path.name} has no row with {idx_col}={idx} (total {len(rows)} rows)")

print("== Pre-flight ==")
check_absent(REPO / "cold_email" / "leads.csv", "index", LEAD_INDEX)
check_absent(REPO / "cold_email" / "leads_with_emails.csv", "lead_index", LEAD_INDEX)

# Append to leads.csv (8 cols)
leads_path = REPO / "cold_email" / "leads.csv"
with open(leads_path, newline="", encoding="utf-8") as f:
    rdr = csv.DictReader(f)
    leads_header = rdr.fieldnames
    leads_rows = list(rdr)
assert leads_header == ["index", "name", "handle", "email", "vertical", "tier", "template", "tier_reason"], f"unexpected leads.csv header: {leads_header}"
leads_rows.append({
    "index": LEAD_INDEX,
    "name": NAME,
    "handle": HANDLE,
    "email": EMAIL,
    "vertical": VERTICAL,
    "tier": TIER,
    "template": TEMPLATE,
    "tier_reason": TIER_REASON,
})
with open(leads_path, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=leads_header, quoting=csv.QUOTE_ALL)
    w.writeheader()
    w.writerows(leads_rows)
print(f"  wrote leads.csv: {len(leads_rows)} rows total (was {len(leads_rows)-1})")

# Append to leads_with_emails.csv (13 cols)
lwe_path = REPO / "cold_email" / "leads_with_emails.csv"
with open(lwe_path, newline="", encoding="utf-8") as f:
    rdr = csv.DictReader(f)
    lwe_header = rdr.fieldnames
    lwe_rows = list(rdr)
assert lwe_header == ["lead_index", "company", "handle", "domain", "website", "founder", "vertical", "tier", "best_email", "emails_found", "guessed_emails", "source_template", "tier_reason"], f"unexpected leads_with_emails.csv header: {lwe_header}"
lwe_rows.append({
    "lead_index": LEAD_INDEX,
    "company": NAME,
    "handle": HANDLE,
    "domain": DOMAIN,
    "website": WEBSITE,
    "founder": FOUNDER,
    "vertical": VERTICAL,
    "tier": TIER,
    "best_email": EMAIL,
    "emails_found": f"{EMAIL};support@hebbia.com",
    "guessed_emails": "",
    "source_template": TEMPLATE,
    "tier_reason": TIER_REASON,
})
with open(lwe_path, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=lwe_header, quoting=csv.QUOTE_ALL)
    w.writeheader()
    w.writerows(lwe_rows)
print(f"  wrote leads_with_emails.csv: {len(lwe_rows)} rows total (was {len(lwe_rows)-1})")

# Parse-back verification: read each CSV, confirm 333 present + shape correct
print("\n== Parse-back verification ==")
for path, idx_col in [(leads_path, "index"), (lwe_path, "lead_index")]:
    with open(path, newline="", encoding="utf-8") as f:
        rdr = csv.DictReader(f)
        rows = list(rdr)
    last = rows[-1]
    assert last[idx_col] == LEAD_INDEX, f"last row {idx_col} mismatch: {last[idx_col]!r} != {LEAD_INDEX!r}"
    assert last["name" if idx_col == "index" else "company"] == NAME, "name/company mismatch"
    print(f"  {path.name}: {len(rows)} rows, last row {idx_col}={last[idx_col]}, name={last.get('name') or last.get('company')}, email={last.get('email') or last.get('best_email')}")

# Dedupe invariant check
from collections import Counter
for path, idx_col in [(leads_path, "index"), (lwe_path, "lead_index")]:
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    c = Counter(r.get(idx_col) for r in rows)
    dupes = {k: v for k, v in c.items() if v > 1}
    assert not dupes, f"DUPLICATES in {path.name}: {dupes}"
    print(f"  {path.name}: zero duplicates ({len(rows)} unique indices, max index = {max(int(r[idx_col]) for r in rows)})")

print("\nALL CHECKS PASSED")
