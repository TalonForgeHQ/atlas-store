"""Append lead 470 (Parallel Web Systems) to cold_email/leads.csv.
Uses csv.DictWriter with QUOTE_ALL to match existing row format.
Pre-flight: confirms index 470 is not already in the CSV.
"""
import csv, sys
from pathlib import Path

CSV_PATH = Path('C:/Users/Potts/projects/atlas-store/cold_email/leads.csv')
NEW_LEAD_PATH = Path('C:/Users/Potts/AppData/Local/Temp/lead470.csv')

# Read existing
with CSV_PATH.open(newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    header = reader.fieldnames
    rows = list(reader)
    existing_idxs = [r['index'] for r in rows]

# Pre-flight dedupe
if '470' in existing_idxs:
    print(f"ABORT: index 470 already present (rows: {existing_idxs.count('470')})")
    sys.exit(1)

# Build the new row matching header
new_row_raw = NEW_LEAD_PATH.read_text(encoding='utf-8').strip()
# Parse the comma-separated 8 fields with csv
parsed = next(csv.reader([new_row_raw]))
print(f"Parsed new row: {len(parsed)} fields")
if len(parsed) != 8:
    print(f"ABORT: expected 8 fields, got {len(parsed)}")
    sys.exit(1)

# Write atomically: append to CSV with QUOTE_ALL
new_row = dict(zip(header, parsed))

with CSV_PATH.open('a', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=header, quoting=csv.QUOTE_ALL)
    writer.writerow(new_row)

# Verify: read back
with CSV_PATH.open(newline='', encoding='utf-8') as f:
    rows2 = list(csv.DictReader(f))
last = rows2[-1]
print(f"After append: total rows = {len(rows2)}")
print(f"Last row index: {last['index']}, name: {last['name']}, email: {last['email']}")
print(f"Header cols: {header}")