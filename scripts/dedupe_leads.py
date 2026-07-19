"""Dedupe leads.csv — keep last occurrence of each index (preserves most-recent correct write)."""
from pathlib import Path
import csv

LEADS = Path(r"C:\Users\Potts\projects\atlas-store\cold_email\leads.csv")
text = LEADS.read_text(encoding="utf-8")

rows = list(csv.reader(text.splitlines()))
header = rows[0]
data = rows[1:]
print(f"Total rows: {len(data)}")

# Keep LAST occurrence of each index
seen = {}
for i, r in enumerate(data):
    if r and r[0]:
        seen[r[0]] = i  # overwrites earlier occurrences

keep_indices = sorted(seen.values())
kept = [data[i] for i in keep_indices]
dupes_removed = len(data) - len(kept)
print(f"Duplicates removed: {dupes_removed}")
print(f"Kept rows: {len(kept)}")

# Re-write with csv.writer + QUOTE_MINIMAL (matches original style for tier_reason)
out_lines = [",".join(header)]
for r in kept:
    out_lines.append(",".join(r))

LEADS.write_text("\n".join(out_lines) + "\n", encoding="utf-8")
print(f"[OK] leads.csv deduped: {len(data)} -> {len(kept)} rows")

# Verify
import csv as csv2
verify = list(csv2.DictReader(open(LEADS, encoding="utf-8")))
ids = [r["index"] for r in verify if r.get("index")]
from collections import Counter
dupes = [(k, v) for k, v in Counter(ids).items() if v > 1]
print(f"Post-dedupe verification: {len(ids)} rows, dupes={dupes}")