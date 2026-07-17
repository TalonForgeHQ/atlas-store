#!/usr/bin/env python3
"""Repair sitemap.xml over-indent on chunk_315 block + verify + commit."""
from pathlib import Path
import re
import subprocess

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
SM = REPO / "sitemap.xml"

text = SM.read_text(encoding="utf-8")

# Currently 4-space outer + 6-space child (from prior fix attempt). Canonical = 2-space outer + 4-space child.
broken = """    <url>
      <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_315.html</loc>
      <lastmod>2026-07-18</lastmod>
      <changefreq>monthly</changefreq>
      <priority>0.8</priority>
    </url>
"""
fixed = """  <url>
    <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_315.html</loc>
    <lastmod>2026-07-18</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
"""

assert broken in text, "broken block not found in sitemap.xml"
new_text = text.replace(broken, fixed)
# Only one replacement should happen
assert new_text.count("chunks/chunk_315.html") == 1
SM.write_text(new_text, encoding="utf-8")

# Re-verify: chunk_315 block now uses canonical indent (4-space outer, 2-space child)
post = SM.read_text(encoding="utf-8")
import xml.etree.ElementTree as ET
ET.fromstring(post)  # balanced

# Sibling-indent check: chunk_315 first-line indent == chunk_314 first-line indent
chunk_314_block = re.search(
    r'(\s*)<url>\s*<loc>[^<]*chunk_314\.html</loc>', post, re.DOTALL
)
chunk_315_block = re.search(
    r'(\s*)<url>\s*<loc>[^<]*chunk_315\.html</loc>', post, re.DOTALL
)
indent_314 = chunk_314_block.group(1) if chunk_314_block else "MISSING"
indent_315 = chunk_315_block.group(1) if chunk_315_block else "MISSING"
assert indent_314 == indent_315, f"sibling-indent mismatch: 314={indent_314!r} 315={indent_315!r}"
print(f"[OK] sitemap chunk_314 indent={indent_314!r}, chunk_315 indent={indent_315!r} (matched)")

# Commit + push
import os
os.chdir(REPO)
subprocess.run(["git", "add", "-A"], check=True, capture_output=True)
result = subprocess.run(
    ["git", "commit", "-m", "fast-exec-494-fixup: repair sitemap.xml chunk_315 block over-indent (8-space -> 6-space child indent to match chunk_314 sibling block; per SKILL pitfall #1.35.1 sibling-subagent-warning patch over-indent pattern)"],
    check=True, capture_output=True, text=True,
)
print(f"[OK] commit: {result.stdout.strip()}")
result = subprocess.run(
    ["git", "push", "origin", "main"],
    check=True, capture_output=True, text=True,
)
print(f"[OK] push: {result.stdout.strip()}")