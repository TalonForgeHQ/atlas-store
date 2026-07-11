#!/usr/bin/env python
"""SAFE append-only lead 166 to leads.csv using a different strategy:
1. Open in 'rb' to find EOF position
2. Strip trailing newlines from current file
3. Append exactly one new line + clean lead 166 row, fully CSV-quoted

This avoids the bug where csv.DictWriter on existing quoted-format rows
caused nested quote-escape.
"""
import os
import sys

CSV_PATH = r"C:\Users\Potts\projects\atlas-store\cold_email\leads.csv"
TIER_REASON_PATH = r"C:\Users\Potts\AppData\Local\Temp\humanloop_tier_reason_166.txt"

# Read tier_reason
with open(TIER_REASON_PATH, "r", encoding="utf-8") as f:
    tier_reason = f.read().strip()

# Verify no lead 166 already
with open(CSV_PATH, "r", encoding="utf-8", errors="replace") as f:
    content = f.read()
if '"166"' in content:
    print("ABORT: lead 166 already in CSV")
    sys.exit(1)

# Build the new row using csv module on a single string buffer (no file rewrite)
import csv
import io
buf = io.StringIO()
writer = csv.writer(buf, quoting=csv.QUOTE_ALL)
writer.writerow([
    "166",
    "Humanloop",
    "@humanloop",
    "privacy@humanloop.com",
    "ai_agents_infra",
    "1",
    "246_humanloop.md",
    tier_reason,
])
new_row = buf.getvalue()
print(f"NEW_ROW_LEN: {len(new_row)} chars")
print(f"NEW_ROW_FIRST_200: {new_row[:200]}")
print(f"NEW_ROW_LAST_200: {new_row[-200:]}")

# Sanity: should NOT contain the buggy nested-quote pattern
if '","' in tier_reason:
    # tier_reason itself contains literal quote-comma-quote (probably fine if intentional)
    # but check for the bad pattern that indicates previous tier_reason corruption
    if tier_reason.startswith('"166"'):
        print("ERROR: tier_reason starts with quoted CSV row pattern - aborting")
        sys.exit(1)

# Open the CSV in append-binary mode to avoid any line-ending conversion
# First, check the last byte to see if file ends with newline
with open(CSV_PATH, "rb") as f:
    f.seek(0, os.SEEK_END)
    pos = f.tell()
    if pos == 0:
        print("ERROR: empty file")
        sys.exit(1)
    f.seek(pos - 1)
    last_byte = f.read(1)
print(f"LAST_BYTE: {last_byte}")

# Append the new row. If last byte is newline, just append the row.
# If not, prepend a newline first.
with open(CSV_PATH, "ab") as f:
    if last_byte != b"\n":
        f.write(b"\n")
    f.write(new_row.encode("utf-8"))
print("APPENDED.")

# Verify
with open(CSV_PATH, "r", encoding="utf-8", errors="replace") as f:
    lines = f.readlines()
print(f"FINAL_LINE_COUNT: {len(lines)}")
# Find the lead 166 row (last line that starts with "166",)
last_lines = [l for l in lines if l.startswith('"166",')]
print(f"LEAD_166_LINE_COUNT: {len(last_lines)}")
if last_lines:
    final_row = last_lines[-1]
    print(f"FINAL_ROW_LEN: {len(final_row)} chars")
    # Parse with csv
    import csv as csvmod
    rdr = csvmod.reader([final_row])
    parsed = next(rdr)
    print(f"PARSED_FIELDS: {len(parsed)}")
    print(f"PARSED_INDEX: {parsed[0]}")
    print(f"PARSED_NAME: {parsed[1]}")
    print(f"PARSED_EMAIL: {parsed[3]}")
    print(f"PARSED_VERTICAL: {parsed[4]}")
    print(f"PARSED_TEMPLATE: {parsed[6]}")
    print(f"PARSED_TIER_REASON_LEN: {len(parsed[7])} chars")
    if parsed[7].startswith('"166"'):
        print("ERROR: tier_reason STILL contains the nested-quoted row pattern")
        sys.exit(1)
    print("OK")