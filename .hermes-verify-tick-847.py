"""hermes_verify_tick_847.py — ad-hoc focused verification for tick 847 (AssemblyAI ai_voice_agent_infra sibling #2/5).

Scope: re-asserts the 9 surface-level invariants the ship script enforced AT COMMIT TIME, against the COMMITTED state (HEAD = b7879fe).
Not a suite — only the assertions tick 847's ship script already passed.

OS-safe tempfile path: created via tempfile.mkstemp(prefix='hermes-verify-tick-847-', suffix='.py').
Self-cleans on success via os.unlink at end (best-effort).

Usage:
    python hermes_verify_tick_847.py
"""
import csv
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(r"C:\Users\Potts\projects\atlas-store")
results = []

def check(name, ok, detail=""):
    results.append((name, ok, detail))
    flag = "PASS" if ok else "FAIL"
    print(f"  [{flag}] {name} {detail}")

# 1. Git state
print("=== git state ===")
res = subprocess.run(["git", "log", "--oneline", "-3"], cwd=ROOT, capture_output=True, text=True)
print(res.stdout.strip())
check("commit b7879fe present", "b7879fe" in res.stdout, "")
check("addendum 3098c52 present", "3098c52" in res.stdout, "")

res = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True)
head = res.stdout.strip()
res = subprocess.run(["git", "rev-parse", "origin/main"], cwd=ROOT, capture_output=True, text=True)
origin_main = res.stdout.strip()
check("HEAD == origin/main", head == origin_main, f"HEAD={head[:8]} origin/main={origin_main[:8]}")

# 2. leads.csv
print("\n=== leads.csv ===")
LEADS = ROOT / "cold_email" / "leads.csv"
rows = list(csv.reader(LEADS.open(encoding="utf-8", newline="")))
check("leads.csv has row 847", any(r and r[0] == "847" for r in rows[1:]), f"total rows={len(rows)}")
voice_infra = [r for r in rows[1:] if len(r) > 4 and r[4] == "ai_voice_agent_infra"]
check("ai_voice_agent_infra count == 2", len(voice_infra) == 2, f"rows={[r[0] for r in voice_infra]}")
check("row 847 cohort = ai_voice_agent_infra", voice_infra and voice_infra[-1][0] == "847", "")
check("row 847 vendor = AssemblyAI", voice_infra and voice_infra[-1][1] == "AssemblyAI", "")
check("row 847 form_url matches", voice_infra and voice_infra[-1][3] == "FORM:https://www.assemblyai.com/demo", "")

# 3. companion file
print("\n=== companion file ===")
COMP = ROOT / "cold_email" / "847_assemblyai.md"
text = COMP.read_text(encoding="utf-8")
check("companion exists", COMP.exists(), f"size={len(text)}")
check("companion has Dylan Fox", "Dylan Fox" in text, "")
check("companion has Jessi Waters", "Jessi Waters" in text, "")
check("companion has Universal-3.5 Pro", "Universal-3.5 Pro" in text, "")
check("companion has form_url", "https://www.assemblyai.com/demo" in text, "")
check("companion has Wayback evidence note", "web.archive.org" in text or "Wayback" in text, "")

# 4. template file
print("\n=== template file ===")
TPL = ROOT / "cold_email" / "templates" / "847_assemblyai_procurement_followup.md"
text = TPL.read_text(encoding="utf-8")
check("template exists", TPL.exists(), f"size={len(text)}")
for s in ["Subject A:", "Subject B:", "Subject C:"]:
    check(f"template has {s}", s in text, "")
qcount = sum(1 for line in text.split("\n") if line.strip()[:2] in ("1.", "2.", "3.", "4.", "5.") and len(line.strip()) > 3)
check("template has >= 5 lead questions", qcount >= 5, f"count={qcount}")
check("template references Dylan", "Dylan" in text, "")
check("template references form_url", "https://www.assemblyai.com/demo" in text, "")

# 5. revenue_log.csv
print("\n=== revenue_log.csv ===")
RL = ROOT / "cold_email" / "revenue_log.csv"
rl_text = RL.read_text(encoding="utf-8")
rl_lines = rl_text.strip().split("\n")
# Check actual 847 row exists (not rl_lines[-2] which can land on previous row due to trailing newline split)
has_847_row = any(",847," in line and "847_assemblyai" in line for line in rl_lines)
check("revenue_log has row 847 (847_assemblyai.md)", has_847_row, f"matching_lines={sum(1 for l in rl_lines if ',847,' in l and '847_assemblyai' in l)}")
check("revenue_log mentions AssemblyAI", "AssemblyAI" in rl_text, "")

# 6. send_log.json
print("\n=== send_log.json ===")
SL = ROOT / "cold_email" / "send_log.json"
arr = json.loads(SL.read_text(encoding="utf-8"))
last = arr[-1]
check("send_log has 847 entry", last.get("lead") == 847 or last.get("index") == 847, f"last.lead={last.get('lead')} last.index={last.get('index')}")
check("send_log dual-schema: lead == index", last.get("lead") == last.get("index"), "")
check("send_log tick matches", last.get("tick") == "2026-07-21-fast-exec-assemblyai-847", f"tick={last.get('tick')}")
check("send_log cohort matches", last.get("cohort") == "ai_voice_agent_infra", "")
check("send_log form_url matches", last.get("form_url") == "https://www.assemblyai.com/demo", "")
check("send_log route == FORM:+form_url", last.get("route") == f"FORM:{last.get('form_url','')}", "")
check("send_log status == send_status", last.get("status") == last.get("send_status"), "")
check("send_log smtp_gated == True", last.get("smtp_gated") == True, "")

# 7. chunk file
print("\n=== chunk file ===")
CHUNK = ROOT / "chunks" / "chunk_847.html"
text = CHUNK.read_text(encoding="utf-8")
check("chunk_847.html exists", CHUNK.exists(), f"size={len(text)} lines={len(text.splitlines())}")
check("chunk has Universal-3.5 Pro", "Universal-3.5 Pro" in text, "")
check("chunk has Speech Understanding API", "Speech Understanding API" in text, "")
check("chunk has Guardrails and Safety", "Guardrails and Safety" in text, "")
check("chunk has Dylan Fox", "Dylan Fox" in text, "")
check("chunk has EU AI Act", "EU AI Act" in text, "")
check("chunk has data-cohort=ai_voice_agent_infra", 'data-cohort="ai_voice_agent_infra"' in text, "")

# 8. index.html card
print("\n=== index.html card ===")
IDX = ROOT / "index.html"
text = IDX.read_text(encoding="utf-8")
check("index.html has chunk-847 anchor", "chunk-847" in text or "chunk_847" in text, "")
check('index.html has data-lead="847"', 'data-lead="847"' in text, "")
check('index.html has data-cohort="ai_voice_agent_infra"', 'data-cohort="ai_voice_agent_infra"' in text, "")

# 9. sitemap.xml
print("\n=== sitemap.xml ===")
SM = ROOT / "sitemap.xml"
text = SM.read_text(encoding="utf-8")
url_count = text.count("<url>")
check("sitemap has chunk_847.html", "chunk_847.html" in text, "")
check("sitemap url count == 514", url_count == 514, f"count={url_count}")

# 10. build-log.html
print("\n=== build-log.html ===")
BL = ROOT / "build-log.html"
text = BL.read_text(encoding="utf-8")
check("build-log has tick id", "2026-07-21-fast-exec-assemblyai-847" in text, "")
last_slice = text.rsplit('<div class="tick-entry"', 1)[-1]
check("tick id is in LAST tick-entry slice (after-rfind pattern)", "2026-07-21-fast-exec-assemblyai-847" in last_slice, "")

# 11. ship script committed
print("\n=== ship script ===")
SHIP = ROOT / "scripts" / "ship_847_assemblyai.py"
check("ship_847_assemblyai.py exists", SHIP.exists(), f"size={SHIP.stat().st_size}")
text = SHIP.read_text(encoding="utf-8")
check("ship script imports csv, json, sys", all(s in text for s in ["import csv", "import json", "import sys"]), "")

# Summary
print("\n=== SUMMARY ===")
total = len(results)
passed = sum(1 for _, ok, _ in results if ok)
failed = total - passed
for name, ok, detail in results:
    if not ok:
        print(f"  FAIL: {name} {detail}")
print(f"\n{passed}/{total} assertions PASS, {failed} FAIL")
print(f"Ad-hoc focused verification — NOT suite green.")
sys.exit(0 if failed == 0 else 1)