import csv
from pathlib import Path

csv_path = Path(r"C:\Users\Potts\projects\atlas-store\cold_email\leads.csv")
tier_path = Path(r"C:\Users\Potts\AppData\Local\Temp\tick75_retool_tier.txt")

tier_reason = tier_path.read_text(encoding="utf-8").strip()

row = {
    "index": "177",
    "company": "Retool",
    "twitter": "@retool",
    "email": "support@retool.com",
    "vertical": "low_code_backend",
    "send": "1",
    "template_id": "257_retool.md",
    "tier_reason": tier_reason,
}

# Verify existing header
with csv_path.open("r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
    last_row = None
    for r in reader:
        last_row = r

print(f"Header has {len(header)} columns: {header}")
print(f"Last row index: {last_row[0]} (parsed cols: {len(last_row)})")

# Append using csv.writer for safety with quoting
with csv_path.open("a", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerow([row["index"], row["company"], row["twitter"], row["email"],
                     row["vertical"], row["send"], row["template_id"], row["tier_reason"]])

# Parse-back verification
with csv_path.open("r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    rows = list(reader)
print(f"Total rows now: {len(rows)}")
print(f"Row 177 columns: {len(rows[-1])}")
assert len(rows[-1]) == 8, f"Expected 8 columns, got {len(rows[-1])}"
assert rows[-1][0] == "177"
assert "Retool" in rows[-1][1]
assert "support@retool.com" in rows[-1][3]
assert "David Hsu" in rows[-1][7]
assert "Sequoia" in rows[-1][7]
assert "415M" in rows[-1][7]
print("OK: row 177 parsed cleanly with 8 cols and required tokens")
