from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
template = root / "cold_email" / "templates" / "openai_article53_followup.md"
chunk = root / "chunks" / "chunk_700.html"
build = root / "build-log.html"

checks = []
def check(name, condition):
    checks.append((name, bool(condition)))

text = template.read_text(encoding="utf-8")
chunk_text = chunk.read_text(encoding="utf-8")
build_text = build.read_text(encoding="utf-8")

check("template exists", template.is_file())
check("three subjects", all(f"**{x}:" in text for x in "ABC"))
check("five audit questions", len(re.findall(r"(?m)^[1-5]\. ", text)) >= 5)
check("$500 offer", "$500 / 48 hours" in text)
check("$497 offer", "$497 / month" in text)
check("commercial routing guard", "Do not route this offer to `disclosure@openai.com`" in text)
check("no fabricated sales inbox", not re.search(r"(?:sales|enterprise|compliance|privacy|support)@openai\.com", text, re.I))
check("chunk verified inbox", "press@mistral.ai is the verified public inbox" in chunk_text)
check("chunk stale citation removed", "Contact + Compliance inbox: compliance@mistral.ai" not in chunk_text)
check("build tick", 'data-tick="2026-07-20-fast-exec-openai-article53-followup"' in build_text)
check("build artifact", "openai_article53_followup.md" in build_text)
check("build pivot", "security-disclosure-only" in build_text)

for name, ok in checks:
    print(f"{'PASS' if ok else 'FAIL'} {name}")
print(f"RESULT {sum(ok for _, ok in checks)}/{len(checks)}")
raise SystemExit(0 if all(ok for _, ok in checks) else 1)
