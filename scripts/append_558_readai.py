#!/usr/bin/env python3
"""Append Read AI lead 558 to cold_email/leads.csv with row-prefix guard."""
import csv
import io
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
CSV_PATH = REPO / "cold_email" / "leads.csv"
TXT_PATH = Path(r"C:\Users\Potts\AppData\Local\Temp\tier_reason_558.txt")
INDEX = "558"

# Pre-flight guard: row-prefix anchor (pitfall #69)
csv_text = CSV_PATH.read_text(encoding="utf-8")
assert f'"{INDEX}","' not in csv_text, f"row {INDEX} already exists"

tier_reason = TXT_PATH.read_text(encoding="utf-8").strip()
assert len(tier_reason) > 1000, "tier_reason too short"

row = ["558", "Read AI", "@readai", "privacy@read.ai", "meeting_ai_ops", "1",
       "558_read_ai.md", tier_reason]

# Append
with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    w.writerow(row)

# Parse-back verification
with open(CSV_PATH, "r", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
matches = [r for r in rows if r["index"] == INDEX]
assert len(matches) == 1, f"expected 1 row match, got {len(matches)}"
m = matches[0]
assert m["name"] == "Read AI"
assert m["email"] == "privacy@read.ai"
assert m["vertical"] == "meeting_ai_ops"
assert m["tier"] == "1"
print(f"OK: row {INDEX} appended, parse-back verified, len(tier_reason)={len(tier_reason)}")
