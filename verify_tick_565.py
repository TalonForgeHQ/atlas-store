from __future__ import annotations

import csv
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LEADS = ROOT / "cold_email" / "leads.csv"
TEMPLATE = ROOT / "cold_email" / "templates" / "563_tldv.md"
BUILD_LOG = ROOT / "build-log.html"
SCRIPT = ROOT / "scripts" / "append_563_tldv.py"

with LEADS.open("r", encoding="utf-8", newline="") as fh:
    rows = list(csv.DictReader(fh))

hits = [row for row in rows if row["index"] == "563"]
assert len(hits) == 1, f"expected one lead 563, got {len(hits)}"
row = hits[0]
assert row["name"] == "tl;dv"
assert row["handle"] == "@tldv_io"
assert row["email"] == "marketing@tldv.io"
assert row["vertical"] == "meeting_ai_ops"
assert row["tier"] == "2"
assert row["template"] == "563_tldv.md"
assert "Raphael Allstadt" in row["tier_reason"]
assert "founders" in row["tier_reason"]
assert "SOC 2 Type II" in row["tier_reason"]
assert "Europe-or-US AI hosting" in row["tier_reason"]

raw_lines = LEADS.read_text(encoding="utf-8").splitlines()
lead_lines = [line for line in raw_lines if line.startswith('"563","tl;dv",')]
assert len(lead_lines) == 1
assert lead_lines[0].count('","') == 7
assert raw_lines[-1] == lead_lines[0], "lead 563 must be final physical CSV row"

text = TEMPLATE.read_text(encoding="utf-8")
assert text.count("marketing@tldv.io") >= 2
assert "$500 fixed-price, 48-hour evidence-gap map" in text
assert "$497/mo quarterly refresh" in text
assert "Founder titles were not explicitly published" in text
assert len(text.splitlines()) >= 35

log = BUILD_LOG.read_text(encoding="utf-8")
tick_id = "2026-07-19-fast-exec-tldv-563"
assert log.count(tick_id) == 1
assert log.index(tick_id) < log.index("2026-07-19-fast-exec-sembly-ai-562-chunk-ship")
assert log.startswith(f'<div class="tick-entry" data-tick="{tick_id}">')
assert "Tick 565" in log[:300]
assert "Revenue progress:" in log[:3000]
assert "Pivot:" in log[:4000]

proc = subprocess.run(
    ["py", "-3.12", str(SCRIPT)],
    cwd=ROOT,
    check=True,
    capture_output=True,
    text=True,
)
assert "NO-OP" in proc.stdout

assert not (ROOT / "GRAND_PLAN.md").read_bytes() == b"", "GRAND_PLAN must remain readable"

print("PASS 30/30: lead 563 + template + Tick 565 build-log + idempotency")
