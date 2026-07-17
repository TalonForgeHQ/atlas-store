import pathlib

REPO = pathlib.Path(r"C:\Users\Potts\projects\atlas-store")
INDEX = REPO / "index.html"
INLINE = pathlib.Path(r"C:\Users\Potts\AppData\Local\Temp\chunks_257_258_259_260_inline.html")

text = INDEX.read_text(encoding="utf-8")
inline_text = INLINE.read_text(encoding="utf-8")

# Strip the wrapping <!DOCTYPE>/<html>/<head>/<body> from the inline block
# since we're splicing into an existing index.html that's already structured.
# Find the inner body content between <body...> and </body>.
import re
m = re.search(r"<body[^>]*>(.*?)</body>", inline_text, re.S | re.I)
if not m:
    raise SystemExit("ERROR: no body in inline file")
inner = m.group(1).strip()

# Insert before </html> in index.html
if "</html>" not in text:
    raise SystemExit("ERROR: no </html> in index.html")
# We want the new sections to go BEFORE </html>; the existing chunk-256
# section sits right before </html>.
new_text = text.replace("</html>", inner + "\n</html>", 1)
INDEX.write_text(new_text, encoding="utf-8")

# Verify the splice
verify_text = INDEX.read_text(encoding="utf-8")
for chunk_id in ["chunk-257", "chunk-258", "chunk-259", "chunk-260"]:
    cnt = verify_text.count(f'id="{chunk_id}"')
    print(f"  {chunk_id}: {cnt} match(es) in index.html")
assert verify_text.endswith("</html>")
assert "chunk-260" in verify_text
print(f"OK index.html: {len(text)} -> {len(verify_text)} bytes (+{len(verify_text)-len(text)})")