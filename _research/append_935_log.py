#!/usr/bin/env python3
"""Append build-log tick-935 entry to build-log.html."""
from pathlib import Path

REPO = Path("C:/Users/Potts/projects/atlas-store")
build_log_path = REPO / "build-log.html"
new_entry_path = REPO / "_research" / "build_935_log.html"

build_log = build_log_path.read_text(encoding="utf-8")
new_entry = new_entry_path.read_text(encoding="utf-8").strip()

# Find the last </div> at end of file (tick-934 closing) and insert new entry AFTER it
last_div_pos = build_log.rfind("</div>")
insert_pos = last_div_pos + len("</div>") + 1  # +1 for the \n

new_build_log = build_log[:insert_pos] + "\n" + new_entry + "\n" + build_log[insert_pos:]

build_log_path.write_text(new_build_log, encoding="utf-8")
print(f"OK build-log.html updated. New size: {len(new_build_log)} bytes (+{len(new_build_log) - len(build_log)})")
# Verify the chunk_935 reference and tick-935 marker are in the file
assert "tick-935" in new_build_log
assert "StackAI" in new_build_log
assert "ai_agent_operations" in new_build_log
print("All assertions pass: tick-935 + StackAI + ai_agent_operations present")