"""Quick first-party check for Concord CLM (lead 941 candidate)."""
import re
import json

files = [
    "_research/concord_horizon.html",
    "_research/concord_pricing.html",
    "_research/concord_security.html",
    "_research/concord_contact_app.html",
    "_research/concord_home.html",
    "_research/concord_features.html",
    "_research/concord_ai.html",
]
for f in files:
    print("\n===", f, "===")
    with open(f) as fp:
        html = fp.read()
    descs = re.findall(r'<meta[^>]+name="description"[^>]+content="([^"]+)"', html)
    print("DESC:", descs[:2])
    ftr = re.findall(r"&copy;\s*\d{4}[^<]{0,80}|©\s*\d{4}[^<]{0,80}|Copyright[^<]{0,80}", html)
    print("FOOTER:", ftr[:3])
    prices = re.findall(r"\$[\d,]+(?:\.\d{2})?(?:/mo|\s*/mo|/user|/seat)?", html)
    print("PRICE:", prices[:8])
    orgs = re.findall(r"<script[^>]+application/ld\+json[^>]*>(.+?)</script>", html, re.DOTALL)
    for i, m in enumerate(orgs[:1]):
        if "Concord" in m:
            print(f"JSON-LD {i}:", m[:800])

# Pricing summary
import re as r2
with open("_research/concord_pricing.html") as f: html = f.read()
prices = r2.findall(r"(?:Plan|plan|Starter|Business|Enterprise|Free|Demo)[^<]{0,80}|\$\d[\d,]*(?:\.\d{2})?(?:[^<]{0,40})?", html)
out = []
for p in prices[:30]:
    if "Plan" in p or "Free" in p or "$" in p or "mo" in p:
        out.append(p[:100])
print("\n--- PRICING HITS ---")
for x in out: print(x)
