"""Insert chunk-173 + chunk-174 inline summaries into index.html (after chunk-100)."""
from pathlib import Path

IDX = Path(r"C:\Users\Potts\projects\atlas-store\index.html")
INLINE_173 = Path(r"C:\Users\Potts\AppData\Local\Temp\chunk_173_inline.html").read_text(encoding="utf-8")
INLINE_174 = Path(r"C:\Users\Potts\AppData\Local\Temp\chunk_174_inline.html").read_text(encoding="utf-8")

text = IDX.read_text(encoding="utf-8")

# Strip any chunk-173 article already in index.html (idempotent)
start = text.find('<article id="chunk-173"')
if start != -1:
    end_close_rel = text.find("</article>", start)
    if end_close_rel != -1:
        end_abs = end_close_rel + len("</article>") + 1
        text = text[:start] + text[end_abs:]
        print(f"Stripped existing chunk-173 block: removed {end_abs - start} bytes")

# Insert both after the last </article> (chunk-100)
last_close = text.rfind("</article>")
assert last_close != -1, "no </article> in index.html"
insert_at = last_close + len("</article>") + 1

combined = "\n" + INLINE_173 + "\n" + INLINE_174 + "\n"
new_text = text[:insert_at] + combined + text[insert_at:]
IDX.write_text(new_text, encoding="utf-8")
print(f"Rewrote index.html: {len(text)} -> {len(new_text)} bytes (+{len(new_text) - len(text)})")

# Verify
print("chunk-173 in index:", 'id="chunk-173"' in new_text)
print("chunk-174 in index:", 'id="chunk-174"' in new_text)
print("chunk-100 still in index:", 'id="chunk-100"' in new_text)

p100 = new_text.find('id="chunk-100"')
p173 = new_text.find('id="chunk-173"')
p174 = new_text.find('id="chunk-174"')
print(f"positions: 100={p100}, 173={p173}, 174={p174}")
print(f"order OK (100 < 173 < 174):", p100 < p173 < p174)