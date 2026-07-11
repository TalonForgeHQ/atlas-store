#!/usr/bin/env python3
"""Extract pricing/setup info from HTML files."""
import re
import sys
from html.parser import HTMLParser


class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.skip = False
        self.skip_tags = {"script", "style", "noscript", "svg"}

    def handle_starttag(self, tag, attrs):
        if tag in self.skip_tags:
            self.skip = True

    def handle_endtag(self, tag):
        if tag in self.skip_tags:
            self.skip = False
        if tag in ("p", "br", "div", "li", "h1", "h2", "h3", "h4", "tr"):
            self.parts.append("\n")

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)


def extract(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        html = f.read()
    p = TextExtractor()
    p.feed(html)
    text = "".join(p.parts)
    # collapse whitespace
    text = re.sub(r"\n\s*\n+", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    return text


if __name__ == "__main__":
    for fn in sys.argv[1:]:
        print(f"\n{'='*70}\n=== {fn} ===\n{'='*70}")
        try:
            t = extract(fn)
            # Print only lines mentioning relevant keywords to keep output small
            keywords = [
                "free", "pricing", "tier", "per day", "per month", "monthly",
                "/mo", "$", "€", "£", "credit card", "API", "HTTP", "verify",
                "domain", "sandbox", "send", "email", "OAuth", "quota",
                "limit", "limit", "trial", "sign up", "register", "no credit",
                "instance", "worker", "plan",
            ]
            lines = t.split("\n")
            for i, line in enumerate(lines):
                line_l = line.lower()
                if any(kw in line_l for kw in keywords) and len(line.strip()) > 5:
                    print(line.strip()[:300])
        except Exception as e:
            print(f"ERROR: {e}")