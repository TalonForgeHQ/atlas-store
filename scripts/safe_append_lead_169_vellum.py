#!/usr/bin/env python
"""SAFE append-only lead 169 (Vellum) to leads.csv.

Same pattern as safe_append_lead_166.py:
1. Read tier_reason from temp file
2. Build row using csv.writer on fresh StringIO buffer (QUOTE_ALL)
3. Append in binary mode to the live CSV (no rewrite)
4. Verify no nested-quote corruption
"""
import os
import sys
import csv
import io

CSV_PATH = r"C:\Users\Potts\projects\atlas-store\cold_email\leads.csv"
TIER_REASON_PATH = r"C:\Users\Potts\AppData\Local\Temp\vellum_tier_reason_169.txt"

# Read tier_reason
with open(TIER_REASON_PATH, "r", encoding="utf-8") as f:
    tier_reason = f.read().strip()

# Verify no lead 169 already
with open(CSV_PATH, "r", encoding="utf-8", errors="replace") as f:
    content = f.read()
if '"169"' in content:
    print("ABORT: lead 169 already in CSV")
    sys.exit(1)

# Build the new row using csv module on a fresh string buffer (no file rewrite)
buf = io.StringIO()
writer = csv.writer(buf, quoting=csv.QUOTE_ALL)
writer.writerow([
    "169",
    "Vellum",
    "@vellum_ai",
    "hello@vellum.com",
    "ai_agents_infra",
    "1",
    "249_vellum.md",
    tier_reason,
])
new_row = buf.getvalue()
print(f"NEW_ROW_LEN: {len(new_row)} chars")
print(f"NEW_ROW_FIRST_200: {new_row[:200]}")
print(f"NEW_ROW_LAST_200: {new_row[-200:]}")

# Sanity check
if tier_reason.startswith('"169"'):
    print("ERROR: tier_reason starts with quoted CSV row pattern - aborting")
    sys.exit(1)

# Open the CSV in append-binary mode
with open(CSV_PATH, "rb") as f:
    f.seek(0, os.SEEK_END)
    pos = f.tell()
    if pos == 0:
        print("ERROR: empty file")
        sys.exit(1)
    f.seek(pos - 1)
    last_byte = f.read(1)
print(f"LAST_BYTE: {last_byte}")

# Append the new row
with open(CSV_PATH, "ab") as f:
    if last_byte != b"\n":
        f.write(b"\n")
    f.write(new_row.encode("utf-8"))
print("APPENDED.")

# Verify
with open(CSV_PATH, "r", encoding="utf-8", errors="replace") as f:
    lines = f.readlines()
print(f"FINAL_LINE_COUNT: {len(lines)}")
last_lines = [l for l in lines if l.startswith('"169",')]
print(f"LEAD_169_LINE_COUNT: {len(last_lines)}")
if last_lines:
    final_row = last_lines[-1]
    print(f"FINAL_ROW_LEN: {len(final_row)} chars")
    rdr = csv.reader([final_row])
    parsed = next(rdr)
    print(f"PARSED_FIELDS: {len(parsed)}")
    print(f"PARSED_INDEX: {parsed[0]}")
    print(f"PARSED_NAME: {parsed[1]}")
    print(f"PARSED_EMAIL: {parsed[3]}")
    print(f"PARSED_VERTICAL: {parsed[4]}")
    print(f"PARSED_TEMPLATE: {parsed[6]}")
    print(f"PARSED_TIER_REASON_LEN: {len(parsed[7])} chars")
    if parsed[7].startswith('"169"'):
        print("ERROR: tier_reason STILL contains the nested-quoted row pattern")
        sys.exit(1)
    print("OK")