"""Atlas fast-exec tick 599: append lead 599 (Brave Search) to leads.csv + leads_with_emails.csv.
Sourced from cold_email/tier_reason_599_brave.md per two-tier pattern.
Pre-flight dedupe on BOTH CSVs (different index column names).
"""
import csv
import io
import sys
from pathlib import Path

ROOT = Path(r"C:\Users\Potts\projects\atlas-store")
LEADS_CSV = ROOT / "cold_email" / "leads.csv"
LWE_CSV = ROOT / "cold_email" / "leads_with_emails.csv"
TIER_TXT = ROOT / "cold_email" / "tier_reason_599_brave.md"
TARGET = "599"
COMPANY = "Brave Search"
HANDLE = "@brave"
EMAIL = "privacy@brave.com"
VERTICAL = "ai_search_answer_engines"
TIER = "1"
TEMPLATE = "599_brave.md"

TIER_REASON = TIER_TXT.read_text(encoding="utf-8").strip()
assert TIER_REASON.startswith("Real company + real website + real Brave Search"), "tier_reason prefix missing"


def dedupe_or_die(path: Path, idx_col: str, row_idx: str):
    if not path.exists():
        return
    with path.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    existing = [r.get(idx_col) for r in rows]
    if row_idx in existing:
        print(f"DUPE-FAIL: {path.name} already has {idx_col}={row_idx}")
        sys.exit(2)


dedupe_or_die(LEADS_CSV, "index", TARGET)
dedupe_or_die(LWE_CSV, "lead_index", TARGET)

# leads.csv: 8 cols index,name,handle,email,vertical,tier,template,tier_reason
with LEADS_CSV.open("a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    w.writerow([TARGET, COMPANY, HANDLE, EMAIL, VERTICAL, TIER, TEMPLATE, TIER_REASON])
print(f"OK leads.csv row {TARGET} ({COMPANY})")

# leads_with_emails.csv: 13 cols lead_index,company,handle,domain,website,founder,vertical,tier,best_email,emails_found,guessed_emails,source_template,tier_reason
with LWE_CSV.open("a", encoding="utf-8", newline="") as f:
    w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    w.writerow([
        TARGET, COMPANY, HANDLE, "brave.com", "https://brave.com/",
        "Brendan Eich (CEO + Co-Founder, JavaScript creator + Netscape + Mozilla co-founder + Firefox creator + Brave Software founder) + Brian Bondy (CTO + Co-Founder, ex-Mozilla + ex-Eich JavaScript team + Brave CTO since 2015)",
        VERTICAL, TIER, EMAIL,
        "privacy@brave.com|security@brave.com|press@brave.com|legal@brave.com|leo-support@brave.com",
        "privacy@|security@|press@|legal@|leo-support@",
        TEMPLATE, TIER_REASON,
    ])
print(f"OK leads_with_emails.csv row {TARGET}")

# Parse-back verification (sparse-ID aware)
with LEADS_CSV.open("r", encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
by_idx = {r["index"]: r for r in rows if r.get("index")}
assert TARGET in by_idx, f"FAIL: leads.csv missing {TARGET}"
r = by_idx[TARGET]
assert r["name"] == COMPANY
assert r["email"] == EMAIL
assert r["vertical"] == VERTICAL
assert r["tier"] == TIER
assert r["template"] == TEMPLATE
assert "Brendan Eich" in r["tier_reason"]
assert "Brave Search Goggles" in r["tier_reason"]
print(f"OK leads.csv parse-back row {TARGET}: name={r['name']} email={r['email']} vertical={r['vertical']} template={r['template']}")

with LWE_CSV.open("r", encoding="utf-8", newline="") as f:
    lwe_rows = list(csv.DictReader(f))
em_by_idx = {r["lead_index"]: r for r in lwe_rows if r.get("lead_index")}
assert TARGET in em_by_idx, f"FAIL: leads_with_emails.csv missing {TARGET}"
r2 = em_by_idx[TARGET]
assert r2["company"] == COMPANY
assert r2["best_email"] == EMAIL
assert r2["domain"] == "brave.com"
assert "Brendan Eich" in r2["founder"]
assert "Brave Search" in r2["founder"] or "Brian Bondy" in r2["founder"]
print(f"OK leads_with_emails.csv parse-back row {TARGET}: company={r2['company']} best_email={r2['best_email']} domain={r2['domain']} founder_len={len(r2['founder'])}")

# No duplicates anywhere
from collections import Counter
c1 = Counter(r["index"] for r in rows if r.get("index"))
c2 = Counter(r["lead_index"] for r in lwe_rows if r.get("lead_index"))
assert all(v == 1 for v in c1.values()), f"leads.csv dupes: {{k:v for k,v in c1.items() if v>1}}"
assert all(v == 1 for v in c2.values()), f"leads_with_emails.csv dupes: {{k:v for k,v in c2.items() if v>1}}"
print(f"OK no duplicates: leads.csv={len(rows)} rows / lwe.csv={len(lwe_rows)} rows")
print("DONE")
