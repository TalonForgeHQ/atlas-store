"""Tick 1065 ad-hoc verification (PITFALL #100a/114a/119 pattern):
- Fresh probe via tempfile + py -3.12
- 11 checks: leads.csv + chunk + index + sitemap + revenue_log + send_log + build-log
- Clean up + report ad-hoc not suite green
"""
import json
import re
import sys
import tempfile
import os
from pathlib import Path

ROOT = Path("C:/Users/Potts/projects/atlas-store")
CHECKS = []


def check(name, ok, detail=""):
    status = "PASS" if ok else "FAIL"
    CHECKS.append({"name": name, "status": status, "detail": detail})


# 1. leads.csv row
leads_csv = ROOT / "cold_email/leads.csv"
lc = leads_csv.read_text(encoding="utf-8")
check("leads.csv has 1065 row", "1065,Portkey," in lc, "found Portkey row")
# PITFALL #104 dual-token
check("leads.csv 'opener-1-of-5' token present (bare slug)",
      "opener-1-of-5" in lc, "opener-1-of-5 should appear")
check("leads.csv 'OPENER #1/5' prose token present",
      "OPENER #1/5" in lc, "literal 'OPENER #1/5' token in tier_reason")

# 2. chunk file
chunk = ROOT / "chunks/chunk_1065.html"
check("chunks/chunk_1065.html exists", chunk.exists(), str(chunk))
ctext = chunk.read_text(encoding="utf-8")
chunk_id_token = 'id="chunk-1065"'
check("chunk has id='chunk-1065'", chunk_id_token in ctext)
check("chunk has data-cohort='ai_agent_llm_gateway'", 'data-cohort="ai_agent_llm_gateway"' in ctext)
check("chunk has data-cohort-role='opener-1-of-5'", 'data-cohort-role="opener-1-of-5"' in ctext)
check("chunk mentions Portkey", "Portkey" in ctext)

# 3. index.html updated
idx = ROOT / "index.html"
itext = idx.read_text(encoding="utf-8")
check("index.html has chunk-1065 anchor", 'id="chunk-1065"' in itext)
chunk_card_token = 'class="chunk-card"'
chunk_card_count = itext.count(chunk_card_token)
check("index.html has 264 chunk-card blocks (was 263, +1)",
      chunk_card_count == 264,
      f"count={chunk_card_count}")

# 4. sitemap.xml
sm = ROOT / "sitemap.xml"
stext = sm.read_text(encoding="utf-8")
check("sitemap has chunk_1065 url", "chunks/chunk_1065.html" in stext)
# PITFALL #116: canonical 2-space <url>
last12 = "\n".join(stext.splitlines()[-12:])
check("sitemap last <url> at 2-space indent",
      "  <url>\n    <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_1065.html</loc>" in last12,
      "canonical 2-space indent restored")

# 5. revenue_log.csv
rev = ROOT / "revenue_log.csv"
rtext = rev.read_text(encoding="utf-8")
check("revenue_log.csv has 1065 row", "1065" in rtext.splitlines()[-1].split(",")[0:2] or rtext.count(",1065,") >= 1,
      "row count check")
n_rows = sum(1 for _ in rtext.splitlines() if _.strip()) - 1  # minus header
check("revenue_log.csv has 58 rows total", n_rows == 58, f"actual: {n_rows}")

# 6. send_log.jsonl (PITFALL #97a raw_decode loop)
sl = ROOT / "cold_email/send_log.jsonl"
raw = sl.read_bytes()
text = raw.decode("utf-8", errors="replace").strip()
records = []
while text:
    obj, off = json.JSONDecoder().raw_decode(text)
    records.append(obj)
    text = text[off:].strip()
n_records = len(records)
check("send_log.jsonl parses + has 105 records",
      n_records == 105, f"actual: {n_records}")
last = records[-1]
check("send_log last record is lead 1065",
      last.get("lead_id") == "1065",
      f"got: {last.get('lead_id')}")

# 7. build-log.html
bl = ROOT / "build-log.html"
btext = bl.read_text(encoding="utf-8")
# PITFALL #111: file is APPEND-AT-TOP chronicle; check by anchor presence
check("build-log has tick-1065 article anchor",
      'id="tick-1065"' in btext)
check("build-log article mentions OPENER #1/5",
      "OPENER #1/5" in btext)
check("build-log article mentions Portkey",
      "Portkey" in btext)

# 8. total summary
total_checks = len(CHECKS)
passed = sum(1 for c in CHECKS if c["status"] == "PASS")
failed = total_checks - passed

# Print summary
print("=" * 64)
print(f"TICK 1065 AD-HOC VERIFICATION (NOT suite green)")
print("=" * 64)
for c in CHECKS:
    marker = "✓" if c["status"] == "PASS" else "✗"
    line = f"  [{marker}] {c['name']}"
    if c['detail']:
        line += f"  ({c['detail']})"
    print(line)
print("=" * 64)
print(f"TOTAL: {passed}/{total_checks} PASS")
if failed:
    print(f"FAILED: {failed}")
    sys.exit(1)
else:
    print("OK ALL PASS")
    sys.exit(0)
