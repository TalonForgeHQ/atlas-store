"""Prepend Tick 174 build-log entry (Variant B — anchor on <div class="tick"> at position 0)."""
from pathlib import Path
LOG = Path("C:/Users/Potts/projects/atlas-store/build-log.html")
NEW_ENTRY = Path("C:/Users/Potts/AppData/Local/Temp/tick174_buildlog_entry.txt").read_text(encoding="utf-8")

content = LOG.read_text(encoding="utf-8")
assert content.startswith('<div class="tick">'), "Variant-B expected; head was: " + repr(content[:50])

# Verify exactly one wrapper in new entry (not double-wrapped)
wrapper_count = NEW_ENTRY.count('<div class="tick">')
assert wrapper_count == 1, "expected 1 wrapper, got " + str(wrapper_count)

idx = content.find('<div class="tick">')
new_content = content[:idx] + NEW_ENTRY + content[idx:]
LOG.write_text(new_content, encoding="utf-8")

# Verify the prepend landed correctly
after = LOG.read_text(encoding="utf-8")
assert after.startswith(NEW_ENTRY), "new entry not at position 0"
assert after[len(NEW_ENTRY):].startswith('<div class="tick">'), "Tick 173 not preserved at top"
# Verify newest-first invariant: Tick 174 before Tick 173
t174_pos = after.find("[Tick 174]")
t173_pos = after.find("[Tick 173]")
assert 0 < t174_pos < t173_pos, "ordering broken: t174=" + str(t174_pos) + " t173=" + str(t173_pos)
print("OK build-log.html: t174@" + str(t174_pos) + " < t173@" + str(t173_pos) + "; total " + str(len(after)) + " bytes")