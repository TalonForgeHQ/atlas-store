#!/usr/bin/env python3
"""Rewrite all distribution posts to use business language instead of fork-reveal."""
import os, re

REPLACEMENTS = [
    # Don't reveal specific upstream names
    (r"forked from Agent-Reach \(54k[\u2605\*]+\)", "built on a battle-tested 13-platform read/search engine"),
    (r"fork of Agent-Reach \(54k[\u2605\*]+\)", "built on a battle-tested 13-platform read/search engine"),
    (r"\(fork of Agent-Reach, 54k[\u2605\*]+\)", "(built on a battle-tested 13-platform read/search engine)"),
    (r"fork of Agent-Reach", "battle-tested 13-platform read/search engine"),
    (r"forked from MoneyPrinterTurbo \(96k[\u2605\*]+\)", "built on a battle-tested AI short-video engine"),
    (r"fork of MoneyPrinterTurbo \(96k[\u2605\*]+\)", "built on a battle-tested AI short-video engine"),
    (r"\(fork of MoneyPrinterTurbo, 96k[\u2605\*]+\)", "(built on a battle-tested AI short-video engine)"),
    (r"fork of MoneyPrinterTurbo", "battle-tested AI short-video engine"),
    (r"forked from stealth-browser-mcp \(1\.5k[\u2605\*]+\)", "built on a battle-tested undetectable browser stack"),
    (r"fork of stealth-browser-mcp \(1\.5k[\u2605\*]+\)", "built on a battle-tested undetectable browser stack"),
    (r"\(fork of stealth-browser-mcp, 1\.5k[\u2605\*]+\)", "(built on a battle-tested undetectable browser stack)"),
    (r"fork of stealth-browser-mcp", "battle-tested undetectable browser stack"),
    (r"Agent-Reach \(54k[\u2605\*]+\)", "a battle-tested 13-platform read/search engine"),
    (r"Agent-Reach 54k[\u2605\*]+", "a battle-tested 13-platform read/search engine"),
    (r"MoneyPrinterTurbo \(96k[\u2605\*]+\)", "a battle-tested AI short-video engine"),
    (r"MoneyPrinterTurbo 96k[\u2605\*]+", "a battle-tested AI short-video engine"),
    (r"stealth-browser-mcp \(1\.5k[\u2605\*]+\)", "a battle-tested undetectable browser stack"),
    (r"stealth-browser-mcp 1\.5k[\u2605\*]+", "a battle-tested undetectable browser stack"),
    # General "fork" terms
    (r"fork of [A-Za-z\-]+", "production build"),
    (r"Fork of [A-Za-z\-]+", "Production build"),
    (r"by forking MIT-licensed open source\.?", "by architecting on production-grade foundations."),
    (r"by forking [0-9]+ MIT-licensed open source (repos|projects|tools)", "by engineering on production-grade foundations"),
    (r"forking [0-9]+ MIT-licensed open source projects \([^)]+\), rebranding them, and shipping", "engineering production-grade AI tools and shipping"),
    (r"by forking battle-tested MIT open source\.?", "by engineering on production-grade foundations."),
    (r"MIT-licensed open source", "production-grade foundations"),
    (r"forking ([0-9]+|three|3) MIT open source tools \([^)]+\) and offering them as part of the audit deliverable",
     r"engineering production-grade AI tools and offering them as part of the audit deliverable"),
    (r"forking ([0-9]+|three|3) MIT-licensed (open source )?(repos|projects|tools) \([^)]+\)",
     r"engineering production-grade AI tools"),
    (r"3 MIT-fork products( \([^)]+\))?", "3 production AI tools"),
    (r"Fork MIT-licensed repos with [0-9]+k\+ stars for any category\. Don't reinvent\.",
     "Build on production-grade foundations. Don't reinvent the wheel."),
    (r"Forked from \S+ \(\d+k[\u2605\*]+ MIT\)\. ", ""),
    # Misc phrases
    (r"fork-rebrand-resell model", "production-grade engineering model"),
    (r"the fork-rebrand-resell", "this production-engineering approach"),
    (r"Forking is 10x faster than building from scratch\. Ship today, customize later\.",
     "Building on production foundations is 10x faster. Ship today, customize over time."),
    (r"Made this: Atlas", "Made this: Atlas"),  # keep
]

def rewrite(text):
    for pat, repl in REPLACEMENTS:
        text = re.sub(pat, repl, text)
    # Cleanup leftover orphan parens
    text = re.sub(r"\. +\.", ".", text)
    text = re.sub(r" +\)", ")", text)
    return text

DISTRIB = r"C:\Users\Potts\projects\atlas-store\distrib"
PLAYBOOK = r"C:\Users\Potts\projects\atlas-store\products\atlas-playbook-free.md"
FLIPPA = r"C:\Users\Potts\projects\atlas-store\products\propbot-flippa-listing.md"

for path in [PLAYBOOK, FLIPPA] + [os.path.join(DISTRIB, f) for f in os.listdir(DISTRIB) if f.endswith(".md")]:
    with open(path, encoding="utf-8") as f:
        original = f.read()
    new = rewrite(original)
    if new != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new)
        # Count remaining "fork" mentions to track progress
        remaining = len(re.findall(r"\bfork\b|\bFork\b", new, re.IGNORECASE))
        print(f"  Rewrote {os.path.basename(path):40} ({len(original)}->{len(new)} chars, {remaining} 'fork' left)")
    else:
        print(f"  Unchanged: {os.path.basename(path)}")

print("\nDone.")