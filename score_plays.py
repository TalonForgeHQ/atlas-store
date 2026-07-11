"""
ATLAS BRAINSTORM SCORE — Pick the best 24h money play
Scoring: ROI/time, build effort, distribution friction, moat
"""

plays = [
    {
        "name": "FORGE: Fork MoneyPrinterTurbo → branded Atlas Video SaaS",
        "fork_target": "harry0703/MoneyPrinterTurbo (96k stars, MIT, AI video gen)",
        "build_hrs": 4,
        "price_point": "$99/mo subscription + $499 lifetime",
        "distribution": "TikTok (where the videos go) + ProductHunt launch + Twitter",
        "tam": "Huge - every content creator needs this",
        "moat": "Branding, custom UI, support, LLM fallback (use MiniMax)",
        "evidence": "96k stars upstream, short-form video economy = $50B TAM",
        "score": 0,
    },
    {
        "name": "AGENT-REACH PRO: Fork Agent-Reach → 'Atlas Web Eyes' premium",
        "fork_target": "Panniantong/Agent-Reach (54k stars, MIT)",
        "build_hrs": 3,
        "price_point": "$49/mo + $299 lifetime + $0 free tier",
        "distribution": "AI agent builder communities (Reddit r/ClaudeAI, r/LangChain, Discord)",
        "tam": "Every AI agent builder needs this",
        "moat": "Reliability/uptime SLA, hosted version, multi-provider LLM",
        "evidence": "Upstream has 54k stars, hosted version = recurring revenue",
        "score": 0,
    },
    {
        "name": "OUTREACH.AI: Fork OpenOutreach → 'Atlas Cold Email' SaaS",
        "fork_target": "eracle/OpenOutreach (2.3k stars, MIT) + sales-outreach-langgraph (338 stars)",
        "build_hrs": 6,
        "price_point": "$199/mo",
        "distribution": "Cold email agencies, indie founders on Twitter/IndieHackers",
        "tam": "B2B SaaS founders, agencies",
        "moat": "AI-personalization at scale, deliverability features",
        "evidence": "Smartlead/Instantly are 8-9 figure businesses doing exactly this",
        "score": 0,
    },
    {
        "name": "PATCHRIGHT-AS-A-SERVICE: Hosted undetected browser API",
        "fork_target": "Kaliiiiiiiiii-Vinyzu/patchright-python (1.4k stars, Apache-2.0)",
        "build_hrs": 8,
        "price_point": "$0.05/request, $99/mo for 5k requests",
        "distribution": "AI agent builders on Twitter, Reddit, Discord",
        "tam": "Anyone scraping at scale",
        "moat": "IP rotation, residential proxies, uptime",
        "evidence": "Browserless/ScrapeOps charge similar; $20M+ ARR category",
        "score": 0,
    },
    {
        "name": "TIKTOK FACTORY: Fork wkaisertexas/tiktok-uploader + ShortGPT",
        "fork_target": "wkaisertexas (753 stars, MIT) + ShortGPT",
        "build_hrs": 5,
        "price_point": "$49/mo, $299 lifetime",
        "distribution": "TikTok creators on Twitter, ProductHunt",
        "tam": "Faceless TikTok accounts, content agencies",
        "moat": "Auto-upload, multi-account, AI scripts",
        "evidence": "Faceless TikTok is a known $5k-$50k/mo niche",
        "score": 0,
    },
    {
        "name": "GUMROAD FUNNEL (Think Scale AI pattern)",
        "fork_target": "None - just bundle my own infra knowledge",
        "build_hrs": 2,
        "price_point": "$0 PWYW funnel + $49 paid playbook + $147 bundle",
        "distribution": "Twitter build-in-public + Gumroad SEO",
        "tam": "Anyone wanting to make money with AI",
        "moat": "Real proof (live Atlas), 24h updates",
        "evidence": "Think Scale AI: $20-80k/yr from this exact pattern",
        "score": 0,
    },
    {
        "name": "PROPBOT FLIPPA LISTING",
        "fork_target": "Anvil's propbot-ai spec (Kanban t_ab746f49)",
        "build_hrs": 1,
        "price_point": "$5,000-$50,000 asking",
        "distribution": "Flippa.com / Acquire.com",
        "tam": "Property managers, AI buyers",
        "moat": "Spec is detailed, market proven ($4.8k revenue comps)",
        "evidence": "Real Flippa comp: $4.8K revenue PM-AI at 43% margin",
        "score": 0,
    },
    {
        "name": "STEALTH SCRAPER: Fork stealth-browser-mcp",
        "fork_target": "vibheksoni/stealth-browser-mcp (1.5k stars, MIT)",
        "build_hrs": 4,
        "price_point": "$29/mo, $199 lifetime",
        "distribution": "AI agent builders, scraping communities",
        "tam": "Indie hackers, agencies",
        "moat": "MCP integration = native Claude/Cursor use",
        "evidence": "Anti-bot tools = $1M+ market with rising demand",
        "score": 0,
    },
]

# Scoring weights (24h focused)
weights = {
    "build_hrs": 0.30,        # lower = better (inverse)
    "evidence": 0.25,         # higher = better
    "distribution": 0.20,     # lower friction = better
    "moat": 0.15,             # higher = better
    "tam": 0.10,              # higher = better
}

def normalize(value, min_v, max_v, inverse=False):
    if max_v == min_v: return 0.5
    if inverse:
        return (max_v - value) / (max_v - min_v)
    return (value - min_v) / (max_v - min_v)

# Compute scores
for play in plays:
    # Lower build_hrs = better (inverse)
    build_score = 1.0 - (play["build_hrs"] / 10.0)
    ev_score = 1.0 if "100k" in play["evidence"] or "M+" in play["evidence"] or "20-80k" in play["evidence"] or "9 figure" in play["evidence"] else 0.7 if "TAM" in play["evidence"] or "market" in play["evidence"] else 0.5
    dist_score = 0.9 if "Twitter" in play["distribution"] or "Reddit" in play["distribution"] else 0.7
    moat_score = 0.9 if "branding" in play["moat"].lower() or "reliability" in play["moat"].lower() else 0.6
    tam_score = 0.9 if "Huge" in play["tam"] or "every" in play["tam"].lower() else 0.7

    total = (build_score * weights["build_hrs"] +
             ev_score * weights["evidence"] +
             dist_score * weights["distribution"] +
             moat_score * weights["moat"] +
             tam_score * weights["tam"])
    play["score"] = round(total, 3)
    play["breakdown"] = {"build": round(build_score,2), "evidence": ev_score, "dist": dist_score, "moat": moat_score, "tam": tam_score}

# Sort
plays.sort(key=lambda x: -x["score"])
print("\n=== RANKED PLAYS ===\n")
for i, p in enumerate(plays, 1):
    print(f"{i}. [{p['score']}] {p['name']}")
    print(f"   Build: {p['build_hrs']}h | Price: {p['price_point']}")
    print(f"   Score breakdown: {p['breakdown']}")
    print(f"   Distribution: {p['distribution']}")
    print()

print("\n=== TOP 3 EXECUTION PLAN ===\n")
top3 = plays[:3]
print(f"PARALLEL TRACK A: {top3[0]['name']}")
print(f"  - Fork upstream, brand as Atlas, deploy as SaaS")
print(f"  - Stripe price: {top3[0]['price_point']}")
print(f"  - Distribution: {top3[0]['distribution']}")
print()
print(f"PARALLEL TRACK B: {top3[1]['name']}")
print(f"  - Fork upstream, add hosted version")
print(f"  - Stripe price: {top3[1]['price_point']}")
print(f"  - Distribution: {top3[1]['distribution']}")
print()
print(f"PARALLEL TRACK C: {top3[2]['name']}")
print(f"  - {top3[2]['name']}")
print(f"  - Stripe price: {top3[2]['price_point']}")
print(f"  - Distribution: {top3[2]['distribution']}")