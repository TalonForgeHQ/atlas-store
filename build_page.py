#!/usr/bin/env python3
"""Build atlas-store index.html by concatenating numeric chunk_*.html files."""
import os
import re
from glob import glob

OUT = r"C:\Users\Potts\projects\atlas-store\index.html"
DIR = os.path.dirname(OUT)
CHUNKS = os.path.join(DIR, "_chunks")
os.makedirs(CHUNKS, exist_ok=True)


def chunk_num(path):
    name = os.path.basename(path)
    match = re.fullmatch(r"chunk_(\d+)\.html", name)
    return int(match.group(1)) if match else 10**9

chunk_files = sorted(glob(os.path.join(CHUNKS, "chunk_*.html")), key=chunk_num)
parts = []
for p in chunk_files:
    with open(p, encoding="utf-8") as f:
        parts.append(f.read())

with open(OUT, "w", encoding="utf-8") as f:
    f.write("".join(parts))

print(f"Wrote {os.path.getsize(OUT)} bytes from {len(parts)} chunks")
