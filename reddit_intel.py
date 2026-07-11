#!/usr/bin/env python3
"""Get subreddit subscriber counts and posting rules via Reddit JSON."""
import json, urllib.request

subs = [
    ("SideProject", "https://www.reddit.com/r/SideProject/about.json"),
    ("IMadeThis", "https://www.reddit.com/r/IMadeThis/about.json"),
    ("Entrepreneur", "https://www.reddit.com/r/Entrepreneur/about.json"),
    ("ChatGPT", "https://www.reddit.com/r/ChatGPT/about.json"),
    ("ClaudeAI", "https://www.reddit.com/r/ClaudeAI/about.json"),
    ("AI_Agents", "https://www.reddit.com/r/AI_Agents/about.json"),
    ("automation", "https://www.reddit.com/r/automation/about.json"),
    ("LocalLLaMA", "https://www.reddit.com/r/LocalLLaMA/about.json"),
    ("singularity", "https://www.reddit.com/r/singularity/about.json"),
    ("OpenAI", "https://www.reddit.com/r/OpenAI/about.json"),
    ("AnthropicAI", "https://www.reddit.com/r/AnthropicAI/about.json"),
    ("LangChain", "https://www.reddit.com/r/LangChain/about.json"),
    ("indiehackers", "https://www.reddit.com/r/indiehackers/about.json"),
    ("SaaS", "https://www.reddit.com/r/SaaS/about.json"),
    ("startups", "https://www.reddit.com/r/startups/about.json"),
]

results = []
for name, url in subs:
    req = urllib.request.Request(url, headers={"User-Agent": "Atlas-Bot/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            d = json.loads(r.read())
        data = d.get("data", {})
        subs_count = data.get("subscribers", 0)
        title = data.get("title", "")
        desc = data.get("description", "")[:200].replace("\n", " ")
        results.append((name, subs_count, title, desc))
    except Exception as e:
        results.append((name, 0, f"ERR: {e}", ""))

results.sort(key=lambda x: -x[1])
print(f"{'Subreddit':<20} {'Subscribers':<12} Public Description")
print("-" * 100)
for name, subs, title, desc in results:
    print(f"r/{name:<18} {subs:>10,}  {title[:30]}")
    if desc:
        print(f"  {desc[:150]}")