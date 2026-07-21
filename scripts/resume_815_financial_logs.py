#!/usr/bin/env python3
"""Resume only the two financial-log surfaces after tick 815's partial run."""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path("C:/Users/Potts/projects/atlas-store")
REVENUE_CSV = ROOT / "cold_email/revenue_log.csv"
REVENUE_MD = ROOT / "revenue_log.md"
SEND_LOG = ROOT / "cold_email/send_log.json"
INDEX = "815"
MARKER = "fast-exec tick Lago 815"


def rows() -> list[list[str]]:
    with REVENUE_CSV.open(encoding="utf-8", newline="") as f:
        return list(csv.reader(f))


def row_present() -> bool:
    return any(len(r) > 1 and r[1] == INDEX for r in rows() if r)


def marker_present() -> bool:
    return REVENUE_MD.read_text(encoding="utf-8").count(MARKER) == 1


if row_present() and marker_present():
    print("COMPLETED_NOOP resume_815_financial_logs: both surfaces already present")
    sys.exit(0)

assert not row_present(), "revenue CSV row exists but revenue Markdown marker is missing"
assert not marker_present(), "revenue Markdown marker exists but revenue CSV row is missing"

existing = rows()
assert existing and all(len(r) == 7 for r in existing if r and len(r) != 14), "unexpected revenue_log.csv shape"
assert any(len(r) == 14 and len(r) > 1 and r[1] == "802" for r in existing), "expected legacy lead-802 row"
raw = REVENUE_CSV.read_bytes()
with REVENUE_CSV.open("a", encoding="utf-8", newline="") as f:
    if raw and not raw.endswith((b"\n", b"\r")):
        f.write("\n")
    csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator="\n").writerow([
        "2026-07-21",
        INDEX,
        "815_lago.md",
        "chunk_815.html",
        "ai_billing_usage OPENER #1/5",
        "0",
        "Lago OPENER: first-party founders + Book a Demo route + 20-column billable-event receipt; form not submitted; no send_log event; $0 sent / $0 received.",
    ])

entry = '''

---

## 2026-07-21 — fast-exec tick Lago 815 (ai_billing_usage OPENER #1/5)

- **Artifact:** Lead 815, companion evidence, 5-question template, 20-column SEO audit map, sitemap URL, index card, and build-log receipt.
- **First-party proof:** Anh-Tho Chuong (CEO & co-founder) + Raffi Sarkissian (CPO & co-founder) on `getlago.com/about-us`; `getlago.com/book-a-demo` is the commercial route; `getlago.com/security` verifies SOC 2 Type II + GDPR and excludes its security inbox from sales use.
- **Revenue impact:** $500/48h evidence-gap map + $497/mo refresh staged. FORM-only route not submitted; no send event; **$0 sent / $0 received**.
- **Next:** extend `ai_billing_usage` with Metronome or Orb as sibling #2/5 after first-party founder and commercial-route proof.
'''
REVENUE_MD.write_text(REVENUE_MD.read_text(encoding="utf-8").rstrip() + entry + "\n", encoding="utf-8")

target = [r for r in rows() if len(r) > 1 and r[1] == INDEX]
assert len(target) == 1 and len(target[0]) == 7
assert marker_present()
send_entries = json.loads(SEND_LOG.read_text(encoding="utf-8"))
assert not any(str(e.get("lead") or e.get("index")) == INDEX or e.get("tick") == "2026-07-21-fast-exec-lago-815" for e in send_entries)
print("RESUME_OK tick=815 surfaces=revenue_log.csv+revenue_log.md send_log_count=0")