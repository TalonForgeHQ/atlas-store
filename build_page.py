#!/usr/bin/env python3
"""Build atlas-store index.html by concatenating chunks from chunk files."""
import os

OUT = r"C:\Users\Potts\projects\atlas-store\index.html"
DIR = os.path.dirname(OUT)
CHUNKS = os.path.join(DIR, "_chunks")
os.makedirs(CHUNKS, exist_ok=True)

parts = []
for i in range(1, 19):
    p = os.path.join(CHUNKS, f"chunk_{i}.html")
    if os.path.exists(p):
        with open(p, encoding="utf-8") as f:
            parts.append(f.read())

with open(OUT, "w", encoding="utf-8") as f:
    f.write("".join(parts))

print(f"Wrote {os.path.getsize(OUT)} bytes from {len(parts)} chunks")
