"""Tick 1065 POST-COMMIT re-verification (PITFALL #114a/119):
- Distinct OS-safe probe path with `hermes-verify-tick-1065-postcommit-` prefix
- Run against UNCHANGED shipped state at commit 3f8709d
- Ad-hoc, NOT suite green
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path("C:/Users/Potts/projects/atlas-store")
CHECKS = []


def check(name, ok, detail=""):
    status = "PASS" if ok else "FAIL"
    CHECKS.append({"name": name, "status": status, "detail": detail})


# 1. Clean working tree (PITFALL #98 cross-tick check)
import subprocess
status_run = subprocess.run(
    ["git", "status", "--short"],
    cwd=str(ROOT), capture_output=True, text=True,
)
clean_tree = status_run.stdout.strip() == ""
check("working tree is clean (post-commit)", clean_tree, status_run.stdout.strip() or "empty")

# 2. Latest commit is the tick identifier
log_run = subprocess.run(
    ["git", "log", "-1", "--format=%s"],
    cwd=str(ROOT), capture_output=True, text=True,
)
check("latest commit message contains tick 1065 identifier",
      "tick 1065" in log_run.stdout and "Portkey" in log_run.stdout,
      log_run.stdout.strip())

# 3. Parity per PITFALL #105/117: ahead>=1 OR behind==0
ahead_run = subprocess.run(
    ["git", "rev-list", "--count", "origin/main..HEAD"],
    cwd=str(ROOT), capture_output=True, text=True,
)
behind_run = subprocess.run(
    ["git", "rev-list", "--count", "HEAD..origin/main"],
    cwd=str(ROOT), capture_output=True, text=True,
)
ahead_n = int(ahead_run.stdout.strip() or "0")
behind_n = int(behind_run.stdout.strip() or "0")
check("parity per PITFALL #105/117 (ahead>=1 OR behind==0)",
      ahead_n >= 1 or behind_n == 0,
      f"ahead={ahead_n} behind={behind_n}")

# 4. Durable artifact presence + content checks (re-run against shipped state)
leads_csv = ROOT / "cold_email/leads.csv"
lc = leads_csv.read_text(encoding="utf-8")
check("leads.csv ships 1065 Portkey row", "1065,Portkey," in lc)
check("leads.csv bare slug opener-1-of-5 present", "opener-1-of-5" in lc)
check("leads.csv prose OPENER #1/5 present", "OPENER #1/5" in lc)

chunk = ROOT / "chunks/chunk_1065.html"
check("chunks/chunk_1065.html exists", chunk.exists())
ctext = chunk.read_text(encoding="utf-8")
chunk_id_token = 'id="chunk-1065"'
check("chunk has id='chunk-1065'", chunk_id_token in ctext)
cohort_token = 'data-cohort="ai_agent_llm_gateway"'
check("chunk has data-cohort='ai_agent_llm_gateway'", cohort_token in ctext)
role_token = 'data-cohort-role="opener-1-of-5"'
check("chunk has data-cohort-role='opener-1-of-5'", role_token in ctext)
check("chunk mentions Portkey", "Portkey" in ctext)
check("chunk mentions 200+ model providers wedge", "200+" in ctext)

idx = ROOT / "index.html"
itext = idx.read_text(encoding="utf-8")
check("index.html wires chunk-1065", 'id="chunk-1065"' in itext)

sm = ROOT / "sitemap.xml"
stext = sm.read_text(encoding="utf-8")
check("sitemap.xml has chunk_1065 url", "chunks/chunk_1065.html" in stext)
last12 = "\n".join(stext.splitlines()[-12:])
expected_indent = "  <url>\n    <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_1065.html</loc>"
check("sitemap canonical 2-space <url> indent (PITFALL #116)",
      expected_indent in last12)

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
check("send_log last record is lead 1065",
      records[-1].get("lead_id") == "1065",
      f"got: {records[-1].get('lead_id')}")

bl = ROOT / "build-log.html"
btext = bl.read_text(encoding="utf-8")
check("build-log has tick-1065 article anchor", 'id="tick-1065"' in btext)
check("build-log article mentions OPENER #1/5", "OPENER #1/5" in btext)
check("build-log article mentions Portkey", "Portkey" in btext)

# Summary
total = len(CHECKS)
passed = sum(1 for c in CHECKS if c["status"] == "PASS")
failed = total - passed

print("=" * 64)
print("TICK 1065 POST-COMMIT RE-VERIFICATION (NOT suite green)")
print("=" * 64)
for c in CHECKS:
    marker = "[OK]" if c["status"] == "PASS" else "[FAIL]"
    line = f"  {marker} {c['name']}"
    if c['detail']:
        line += f"  ({c['detail']})"
    print(line)
print("=" * 64)
print(f"TOTAL: {passed}/{total} PASS")
if failed:
    print(f"FAILED: {failed}")
    sys.exit(1)
else:
    print(f"OK ALL {total} PASS")
    sys.exit(0)
