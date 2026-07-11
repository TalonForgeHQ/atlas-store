#!/usr/bin/env python3
"""Get top ProductHunt launches + IndieHackers top posts for AI tools last 30 days."""
import json, urllib.request, urllib.parse

# ProductHunt doesn't have public API access without auth - try RSS feeds
print("=== PRODUCT HUNT (via search RSS) ===")
ph_urls = [
    "https://www.producthunt.com/feed",
]
for url in ph_urls:
    req = urllib.request.Request(url, headers={"User-Agent": "Atlas-Bot/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            data = r.read().decode()
        # crude item extraction
        import re
        items = re.findall(r"<item>(.*?)</item>", data, re.DOTALL)
        print(f"Found {len(items)} items in feed")
        for it in items[:8]:
            title = re.search(r"<title>(.*?)</title>", it, re.DOTALL)
            link = re.search(r"<link>(.*?)</link>", it, re.DOTALL)
            if title and link:
                t = title.group(1).replace("&amp;", "&").strip()[:60]
                l = link.group(1).strip()
                print(f"  - {t}")
                print(f"    {l}")
    except Exception as e:
        print(f"  ERR: {e}")

print("\n=== REDDIT TOP POSTS (r/SideProject, last month) ===")
for sub in ["SideProject", "IMadeThis", "AI_Agents", "ClaudeAI"]:
    url = f"https://www.reddit.com/r/{sub}/top.json?t=month&limit=10"
    req = urllib.request.Request(url, headers={"User-Agent": "Atlas-Bot/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            d = json.loads(r.read())
        posts = d.get("data", {}).get("children", [])
        print(f"\nr/{sub} top {len(posts)}:")
        for p in posts:
            pd = p.get("data", {})
            score = pd.get("score", 0)
            title = pd.get("title", "")[:60]
            url_p = "https://reddit.com" + pd.get("permalink", "")
            print(f"  [{score:>4}] {title}")
            print(f"          {url_p}")
    except Exception as e:
        print(f"  ERR: {e}")

print("\n=== INDIEHACKERS (search 'AI agents' via tag) ===")
ih_url = "https://www.indiehackers.com/group/ai"
req = urllib.request.Request(ih_url, headers={"User-Agent": "Atlas-Bot/1.0"})
try:
    with urllib.request.urlopen(req, timeout=15) as r:
        d = r.read().decode()
    # crude title extraction
    import re
    titles = re.findall(r'<h2[^>]*>(.*?)</h2>', d, re.DOTALL)
    print(f"IndieHackers AI group: {len(titles)} h2 entries (need auth for full content)")
except Exception as e:
    print(f"  ERR: {e}")