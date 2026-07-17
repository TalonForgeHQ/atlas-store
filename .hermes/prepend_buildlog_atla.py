import pathlib, sys

BL = pathlib.Path(r"C:\Users\Potts\projects\atlas-store\build-log.html")
NEW = pathlib.Path(r"C:\Users\Potts\projects\atlas-store\.hermes\prepend_atla.md").read_text(encoding="utf-8")

text = BL.read_text(encoding="utf-8")
assert NEW.endswith("</div>"), f"new entry must end with </div>, got last 50 chars: {NEW[-50:]!r}"
assert NEW.startswith('<div class="tick-entry" data-tick="2026-07-17-0801Z">'), f"new entry must start with data-tick anchor: {NEW[:80]!r}"

# Reverse-chronological: prepend BEFORE the FIRST existing tick entry
anchor = '<div class="tick-entry" data-tick="2026-07-17-0745Z">'
idx = text.find(anchor)
assert idx >= 0, f"topmost anchor not found; got {idx}"
assert NEW.count('<div class="tick-entry"') == 1, f"new entry must have exactly one wrapper"

if idx == 0:
    # topmost is the same anchor — prepend at byte 0, no preceding bytes
    new_text = NEW + "\n" + text
else:
    new_text = text[:idx] + NEW + "\n" + text[idx:]
BL.write_text(new_text, encoding="utf-8")
print(f"prepended (idx={idx}), new file size: {len(new_text)}")
