#!/usr/bin/env python
"""Splice Tick 69 block into build-log.html BEFORE the first existing <div class="tick">.
This is the verified "write-then-splice" pattern from the subagent-driven-development skill.
"""
import sys
NEW_BLOCK_PATH = r"C:\Users\Potts\AppData\Local\Temp\tick_69_block.html"
BUILD_LOG_PATH = r"C:\Users\Potts\projects\atlas-store\build-log.html"
BACKUP_PATH = BUILD_LOG_PATH + ".tick69.bak"

# Backup first
import shutil
shutil.copy2(BUILD_LOG_PATH, BACKUP_PATH)
print(f"BACKUP: {BACKUP_PATH}")

# Read new block
with open(NEW_BLOCK_PATH, "r", encoding="utf-8") as f:
    new_block = f.read()
print(f"NEW_BLOCK_LEN: {len(new_block)} chars")

# Read build-log
with open(BUILD_LOG_PATH, "r", encoding="utf-8") as f:
    content = f.read()
print(f"ORIGINAL_LEN: {len(content)} chars")

# Find FIRST <div class="tick"> — this is where we splice (reverse-chronological invariant)
idx = content.find('<div class="tick">')
if idx == -1:
    print("ERROR: no <div class=\"tick\"> anchor found")
    sys.exit(1)
print(f"SPLICE_AT: {idx}")

# Verify the new block starts with the comment marker
if not new_block.startswith("<!-- Tick 69 inline marker"):
    print("ERROR: new block missing Tick 69 marker")
    sys.exit(1)

# Verify the new block ends with <div class="tick"> (the splice point — opens the next tick block)
if not new_block.rstrip().endswith('<div class="tick">'):
    print(f"WARN: new block does NOT end with '<div class=\"tick\">' — last 80 chars: {new_block.rstrip()[-80:]}")

# Splice: content[:idx] + new_block + content[idx:]
new_content = content[:idx] + new_block + content[idx:]

# Write
with open(BUILD_LOG_PATH, "w", encoding="utf-8") as f:
    f.write(new_content)
print(f"NEW_LEN: {len(new_content)} chars")

# Verify: first <div class="tick"> should now be Tick 69
with open(BUILD_LOG_PATH, "r", encoding="utf-8") as f:
    verify = f.read()
new_idx = verify.find('<div class="tick">')
print(f"NEW_FIRST_TICK_INDEX: {new_idx}")
# Find the <h2> that follows
h2_idx = verify.find('<h2>', new_idx)
h2_end = verify.find('</h2>', h2_idx)
print(f"NEW_FIRST_TICK_H2: {verify[h2_idx+4:h2_end][:200]}")
# Count total <div class="tick"> blocks
import re
tick_count = len(re.findall(r'<div class="tick">', verify))
print(f"TOTAL_TICK_BLOCKS: {tick_count} (should be 57 = 56 existing + 1 new)")

# Cleanup: remove backup
import os
os.remove(BACKUP_PATH)
print("BACKUP_REMOVED")