import os, json, urllib.request, urllib.parse

with open(os.path.expanduser("~/Desktop/.env")) as f:
    for line in f:
        if line.startswith("GITHUB_TOKEN="):
            token = line.split("=",1)[1].strip()
            break

def search(q, n=8):
    url = f"https://api.github.com/search/repositories?q={urllib.parse.quote(q)}&sort=stars&order=desc&per_page={n}"
    req = urllib.request.Request(url, headers={"Authorization": f"token {token}"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read()).get("items", [])
    except Exception as e:
        return [{"_error": str(e)}]

queries = [
    "browser automation python",
    "web scraper python",
    "twitter automation python",
    "lead generation python",
    "linkedin automation",
    "ai workflow automation",
    "ai agent framework python",
    "cold email automation",
    "instagram automation python",
    "tiktok automation",
    "outreach automation",
    "data extraction python",
]
for q in queries:
    print(f"\n=== {q} ===")
    items = search(q, 8)
    if items and "_error" in items[0]:
        print(f"  ERR: {items[0]['_error']}")
        continue
    for r in items:
        lic = r.get("license") or {}
        lic_id = lic.get("spdx_id", "?") if lic else "NOASSERTION"
        desc = (r.get("description") or "")[:55]
        print(f"  {r['full_name']:42}  star {r['stargazers_count']:>6}  {lic_id:10}  {desc}")