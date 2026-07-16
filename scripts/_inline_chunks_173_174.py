"""Insert chunk-173 + chunk-174 inline summary into index.html before EOF."""
from pathlib import Path
import sys

IDX = Path(r"C:\Users\Potts\projects\atlas-store\index.html")
INLINE = Path(r"C:\Users\Potts\AppData\Local\Temp\chunks_inline.html")

text = IDX.read_text(encoding="utf-8")
inline = INLINE.read_text(encoding="utf-8")

# Insert AFTER the LAST </article> close (the chunk-100 close at line 16465)
last_close = text.rfind("</article>")
if last_close == -1:
    print("NO </article> FOUND")
    sys.exit(1)

# Position right after </article> + the newline that follows it
insert_at = last_close + len("</article>") + 1  # after </article>\n

new_text = text[:insert_at] + "\n" + inline + text[insert_at:]
IDX.write_text(new_text, encoding="utf-8")
print(f"Wrote index.html ({len(new_text)} bytes, was {len(text)}, +{len(new_text) - len(text)} bytes)")

# Verify both anchors present
print('chunk-173 in index:', 'id="chunk-173"' in new_text)
print('chunk-174 in index:', 'id="chunk-174"' in new_text)
print('chunk-100 still in index:', 'id="chunk-100"' in new_text)
# Confirm both </article> closes follow
chunk173_pos = new_text.find('id="chunk-173"')
chunk174_pos = new_text.find('id="chunk-174"')
chunk100_pos = new_text.find('id="chunk-100"')
print(f"positions: chunk-100={chunk100_pos}, chunk-173={chunk173_pos}, chunk-174={chunk174_pos}")
print("order OK (100 < 173 < 174):", chunk100_pos < chunk173_pos < chunk174_pos)