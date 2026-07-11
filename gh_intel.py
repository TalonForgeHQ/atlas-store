import os, json, urllib.request, urllib.error

with open(os.path.expanduser("~/Desktop/.env")) as f:
    for line in f:
        if line.startswith("GITHUB_TOKEN="):
            token = line.split("=",1)[1].strip()
            break

targets = [
    "harry0703/MoneyPrinterTurbo",
    "Panniantong/Agent-Reach",
    "RayVentura/ShortGPT",
    "oxylabs/oxylabs-ai-studio-py",
    "openai/openai-agents-python",
    "pydantic/pydantic-ai",
    "ComposioHQ/awesome-claude-skills",
    "vibheksoni/stealth-browser-mcp",
    "Kaliiiiiiiiii-Vinyzu/patchright-python",
    "ihuzaifashoukat/twitter-automation-ai",
]

for repo in targets:
    url = f"https://api.github.com/repos/{repo}"
    req = urllib.request.Request(url, headers={"Authorization": f"token {token}"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            d = json.loads(r.read())
        lic = d.get("license") or {}
        print(f"\n{d['full_name']}")
        print(f"  Stars: {d['stargazers_count']} | Forks: {d['forks_count']} | License: {lic.get('spdx_id','?')}")
        print(f"  Desc: {d.get('description','')[:100]}")
        print(f"  Updated: {d.get('updated_at','?')[:10]}")
        print(f"  Topics: {', '.join(d.get('topics',[]))[:80]}")
    except urllib.error.HTTPError as e:
        print(f"  {repo}: HTTP {e.code}")
    except Exception as e:
        print(f"  {repo}: ERR {e}")