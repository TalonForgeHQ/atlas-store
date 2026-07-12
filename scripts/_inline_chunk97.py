import sys
from pathlib import Path

INDEX = r"C:\Users\Potts\projects\atlas-store\index.html"
CHUNK = r"C:\Users\Potts\projects\atlas-store\_chunks\chunk_97.html"

index_text = Path(INDEX).read_text(encoding="utf-8")
chunk_text = Path(CHUNK).read_text(encoding="utf-8")

assert "chunk_97.html" not in index_text, "chunk_97 already inlined"
assert index_text.endswith("</section>") or index_text.endswith("</section>\n"), "index.html ending changed"

# Strip the <section ... class="chunk"> wrapper from chunk since we want to inline the contents
# Actually we want to keep the <section> wrapper - just append directly
prefix = "\n\n<!-- chunk_97.html — Galileo Evaluate + Observe + Protect + Agent Observability EU AI Act Aug 2026 Audit-Target Prep 2026 -->\n<!-- Generated 2026-07-12 Tick 104 -->\n"
suffix = "\n"

new_text = index_text + prefix + chunk_text.strip() + suffix

# Verify the chunk content survived the read
assert "galileo-rag-hallucination-llm-evaluation-eu-ai-act-audit-prep" in chunk_text
assert "Galileo Evaluate" in chunk_text
assert "team@galileo.ai" in chunk_text

Path(INDEX).write_text(new_text, encoding="utf-8")

# Parse-back verify
verify_text = Path(INDEX).read_text(encoding="utf-8")
assert "chunk_97" in verify_text
assert "team@galileo.ai" in verify_text
assert "galileo-rag-hallucination-llm-evaluation-eu-ai-act-audit-prep" in verify_text
print(f"OK: chunk_97 inlined into index.html (was {len(index_text)} bytes, now {len(verify_text)} bytes)")
