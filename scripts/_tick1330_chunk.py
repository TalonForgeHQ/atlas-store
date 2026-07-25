"""Tick 1330 (continued) — append chunk_1330 cohort buyer guide to sitemap.xml
+ add chunk-1330 card to index.html."""
import sys

# --- Sitemap ---
with open('sitemap.xml', 'r', encoding='utf-8') as f:
    sitemap = f.read()

close_tag = '</urlset>'
pos = sitemap.rfind(close_tag)
if pos == -1:
    raise SystemExit('NO_URLSET_FOUND')

sitemap_entry = (
    '<url><loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_1330.html</loc>'
    '<lastmod>2026-07-26</lastmod><changefreq>weekly</changefreq><priority>0.85</priority></url>'
)
sitemap = sitemap[:pos] + sitemap_entry + sitemap[pos:]
with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap)
print('OK sitemap.xml updated; new size:', len(sitemap))

# --- Index card ---
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

card = (
    '<article id="chunk-1330" class="chunk-card" '
    'data-cohort="ai_browser_automation_2026_buyer_guide" '
    'data-cohort-role="cohort-buyer-guide" '
    'data-vendor="Cohort Buyer Guide (Browserbase + Steel + Anchor Browser + Hyperbrowser + Browserless)">'
    '<h3>AI Browser Automation 2026 &mdash; Cohort Buyer Guide (Browserbase + Steel + Anchor Browser + Hyperbrowser + Browserless)</h3>'
    '<p><strong>2026-07-26 fast-exec-cohort-buyer-guide-1330.</strong> Five-vendor cohort comparison: Browserbase (commercial AI-browser-infrastructure OPENER + Stagehand 13K stars + YC W23) + Steel (open-source-first developer-first SIBLING #2 + steel-browser 7.4K stars + surf.new Operator alternative) + Anchor Browser (AI-agent-first SIBLING #3 + stealth fingerprint rotation + per-second billing + YC W24) + Hyperbrowser (web-infra-for-AI-agents SIBLING #4 + HyperAgent MCP client + persistent profiles + YC S21) + Browserless (legacy Chrome-as-a-Service veteran CLOSER #5 + BrowserQL GraphQL + Docker self-host + MCP server + Authenticated Profiles + Trust Center + Status Page). Sections: (1) five-vendor substrate table, (2) what AI browser automation means in 2026 (six primitives: headless fleet + stealth + MCP server + persistent profiles + AI-native action framework + enterprise compliance), (3) per-vendor deep dive cards, (4) decision matrix (production-scale / OSS-first / AI-agent-first / persistent-profiles / legacy-veteran / max-compliance / budget-constrained), (5) what each vendor leaves as an evidence gap, (6) Talon Forge $500/48h per-vendor + $2,000 five-vendor cohort benchmark at close + $497/mo quarterly refresh + $10,000 cohort sponsorship tier. Targets long-tail keywords ai_browser_automation_2026, ai_browser_automation_buyer_guide, Browserbase_vs_Steel_vs_Anchor_Browser_vs_Hyperbrowser_vs_Browserless, Stagehand_vs_Steel_SDK_vs_HyperAgent_vs_BrowserQL, MCP_server_browser_automation_2026, Authenticated_Profiles_browser_AI_agents, Browserless_Docker_self_host, ai_agent_browser_infrastructure, EU_AI_Act_browser_automation, browser_fingerprint_rotation_AI_agents. <a href="chunks/chunk_1330.html">Read the AI Browser Automation 2026 cohort buyer guide</a>.</p></article>'
)

last_close = content.rfind('</article>')
if last_close == -1:
    raise SystemExit('NO_ARTICLE_FOUND')
insert_pos = last_close + len('</article>')
new_content = content[:insert_pos] + card + content[insert_pos:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print('OK index.html updated; new size:', len(new_content))