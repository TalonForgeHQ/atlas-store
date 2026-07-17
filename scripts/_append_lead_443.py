"""One-shot helper for tick 2026-07-17. Append lead 443 Cognigy to BOTH CSVs.
Reads tier_reason from temp file to avoid heredoc Python quoting trap.
"""
import csv, pathlib, sys

ROOT = pathlib.Path(r"C:\Users\Potts\projects\atlas-store")
LEADS = ROOT / "cold_email" / "leads.csv"
LEADS_EM = ROOT / "cold_email" / "leads_with_emails.csv"
TIER_TXT = pathlib.Path(r"C:\Users\Potts\AppData\Local\Temp\tier_reason_443_cognigy.txt")

tier_reason = TIER_TXT.read_text(encoding="utf-8").strip()

# Schema A: cold_email/leads.csv (8 cols)
row_a = ["443", "Cognigy", "@cognigy", "info@cognigy.com", "voice_agents", "1", "443_cognigy.md", tier_reason]

# Schema B: cold_email/leads_with_emails.csv (13 cols)
# lead_index, company, handle, domain, website, founder, vertical, tier, best_email, emails_found, guessed_emails, source_template, tier_reason
row_b = ["443", "Cognigy", "@cognigy", "cognigy.com", "https://www.cognigy.com/",
         "Philipp Heltewig + Sascha Poggemann + Benjamin Mayr (ex-DT + SAP + Avaya)",
         "voice_agents", "1", "info@cognigy.com", "info@cognigy.com",
         "info@cognigy.com|contact@cognigy.com|hello@cognigy.com|press@cognigy.com",
         "443_cognigy.md", tier_reason]

# --- leads.csv ---
header_a, rows_a = [], []
with LEADS.open("r", encoding="utf-8", newline="") as f:
    rdr = csv.reader(f)
    header_a = next(rdr)
    for r in rdr:
        rows_a.append(r)
# dedupe invariant
idx_a_col = header_a.index("index")
existing_a = {r[idx_a_col] for r in rows_a if len(r) > idx_a_col}
if "443" in existing_a:
    print(f"LEADS: index 443 already exists, skipping append")
else:
    with LEADS.open("a", encoding="utf-8", newline="") as f:
        wr = csv.writer(f, quoting=csv.QUOTE_ALL)
        wr.writerow(row_a)
    print(f"LEADS: appended row for 443 Cognigy (rows {len(rows_a)} -> {len(rows_a)+1})")

# --- leads_with_emails.csv ---
header_b, rows_b = [], []
with LEADS_EM.open("r", encoding="utf-8", newline="") as f:
    rdr = csv.reader(f)
    header_b = next(rdr)
    for r in rdr:
        rows_b.append(r)
idx_b_col = header_b.index("lead_index")
existing_b = {r[idx_b_col] for r in rows_b if len(r) > idx_b_col}
if "443" in existing_b:
    print(f"LEADS_EM: lead_index 443 already exists, skipping append")
else:
    with LEADS_EM.open("a", encoding="utf-8", newline="") as f:
        wr = csv.writer(f, quoting=csv.QUOTE_ALL)
        wr.writerow(row_b)
    print(f"LEADS_EM: appended row for 443 Cognigy (rows {len(rows_b)} -> {len(rows_b)+1})")

# --- parse-back verification ---
print("--- VERIFY (parse-back) ---")
with LEADS.open("r", encoding="utf-8", newline="") as f:
    rdr = csv.DictReader(f)
    rows = list(rdr)
    assert rows[-1]["index"] == "443", f"leads.csv last row index mismatch: {rows[-1]['index']}"
    assert "Cognigy" in rows[-1]["name"], f"leads.csv last row name mismatch: {rows[-1]['name']}"
    assert rows[-1]["email"] == "info@cognigy.com", f"leads.csv last row email mismatch"
    assert "Philipp Heltewig" in rows[-1]["tier_reason"], f"leads.csv tier_reason missing Philipp"
    print(f"  leads.csv last row: index={rows[-1]['index']} name={rows[-1]['name']} email={rows[-1]['email']}")
    print(f"  tier_reason length: {len(rows[-1]['tier_reason'])} chars")
    print(f"  row count: {len(rows)}")

with LEADS_EM.open("r", encoding="utf-8", newline="") as f:
    rdr = csv.DictReader(f)
    rows = list(rdr)
    assert rows[-1]["lead_index"] == "443", f"leads_with_emails.csv last row lead_index mismatch"
    assert rows[-1]["company"] == "Cognigy"
    assert rows[-1]["best_email"] == "info@cognigy.com"
    print(f"  leads_with_emails.csv last row: lead_index={rows[-1]['lead_index']} company={rows[-1]['company']} best_email={rows[-1]['best_email']}")
    print(f"  row count: {len(rows)}")

# --- dedupe invariant ---
from collections import Counter
def check_dedup(path, col):
    with path.open("r", encoding="utf-8", newline="") as f:
        rdr = csv.DictReader(f)
        cnt = Counter(r.get(col) for r in rdr)
    dupes = {k: v for k, v in cnt.items() if v > 1}
    if dupes:
        print(f"  DEDUPE FAIL {path.name}: {dupes}")
        sys.exit(1)
    print(f"  DEDUPE OK {path.name}: all indices unique ({len(cnt)} unique keys)")

check_dedup(LEADS, "index")
check_dedup(LEADS_EM, "lead_index")

print("OK")
