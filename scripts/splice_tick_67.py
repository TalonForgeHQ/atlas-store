#!/usr/bin/env python
"""Splice Tick 67 block into build-log.html BEFORE the first existing <div class="tick">."""
import sys, shutil
NEW_BLOCK_PATH = r"C:\Users\Potts\AppData\Local\Temp\tick_67_block.html"
BUILD_LOG_PATH = r"C:\Users\Potts\projects\atlas-store\build-log.html"

# Backup
shutil.copy2(BUILD_LOG_PATH, BUILD_LOG_PATH + ".tick67.bak")

with open(NEW_BLOCK_PATH, "r", encoding="utf-8") as f:
    new_block = f.read()
print(f"NEW_BLOCK_LEN: {len(new_block)} chars")

with open(BUILD_LOG_PATH, "r", encoding="utf-8") as f:
    content = f.read()
print(f"ORIGINAL_LEN: {len(content)} chars")

idx = content.find('<div class="tick">')
if idx == -1:
    print("ERROR: no anchor found")
    sys.exit(1)
print(f"SPLICE_AT: {idx}")

new_content = content[:idx] + new_block + "\n" + content[idx:]
with open(BUILD_LOG_PATH, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"NEW_LEN: {len(new_content)} chars")
anchor = '<div class="tick">'
print(f"TICKS: {new_content.count(anchor)}")