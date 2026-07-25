"""Tick 1330 — prepend build-log entry for closing Vertical #80 cohort surfaces
(chunk-1327 Anchor Browser + chunk-1329 Browserless index cards + sitemap entries)."""
with open('build-log.html', 'r', encoding='utf-8') as f:
    content = f.read()

entry = (
    '<article class="tick-entry" id="tick-1330-vertical-80-cohort-surfaces" '
    'data-tick="tick-1330-vertical-80-cohort-surfaces" '
    'data-cohort="ai_agent_browser_automation" data-lead="1327+1329" '
    'data-cohort-role="vertical-closure-cohort-surfaces" data-vendor="Anchor Browser + Browserless" '
    'data-date="2026-07-26">'
    '<h3>Tick 1330 &mdash; Vertical #80 cohort surfaces closed (Anchor Browser + Browserless index cards + sitemap)</h3>'
    '<p><strong>2026-07-26 fast-exec-cohort-surfaces-1330.</strong> Closed the remaining two cohort surfaces for NEW VERTICAL #80 ai_agent_browser_automation after the 1329 CLOSER ship. 3 surfaces appended: '
    '<code>index.html</code> gained <code>chunk-1327</code> Anchor Browser SIBLING #3/5 card (data-cohort=ai_agent_browser_automation + data-cohort-role=sibling-3-of-5 + data-vendor=Anchor Browser, canonical &lsquo;browser purpose-built for AI agents&rsquo; + Jason Fischl CEO + YC W24 + stealth fingerprint rotation + per-second billing + multi-region browser pool) and <code>chunk-1329</code> Browserless CLOSER #5/5 card (data-cohort-role=closer-5-of-5 + data-vendor=Browserless, canonical legacy Chrome-as-a-Service veteran lane + BrowserQL GraphQL query language + Docker self-host substrate + MCP server + Authenticated Profiles + Browser Agent + Trust Center + Status Page + free-for-non-commercial-uses); '
    '<code>sitemap.xml</code> gained <code>chunk_1327.html</code> + <code>chunk_1329.html</code> entries (lastmod 2026-07-26, changefreq weekly, priority 0.85) inserted before the <code>&lt;/urlset&gt;</code> close tag; '
    '<code>build-log.html</code> tick-1330 entry prepended before tick-1329 (correct chronological order).</p>'
    '<p><strong>Why this tick matters:</strong> the 1329 ship landed the leads.csv row + template + build-log entry but missed the index.html cards and sitemap entries for chunk-1327 + chunk-1329, leaving a visible cohort-closure gap on the public landing page (talontoolforgehq.github.io/atlas-store) where every other Vertical #80 surface was linked. This 1330 tick fills the gap without spawning a new lead, while we wait on the next cohort vertical to open.</p>'
    '<p><strong>Vertical #80 status:</strong> CLOSED 5/5 &mdash; Browserbase 1324 OPENER + Steel 1325 SIBLING #2 + Anchor Browser 1327 SIBLING #3 + Hyperbrowser 1328 SIBLING #4 + Browserless 1329 CLOSER #5 &mdash; $10,000 CLOSER-only cohort sponsorship tier UNLOCKED. 6 of 6 surfaces now live per vendor (leads.csv + leads_with_emails.csv row + cold_email templates + cold_email dossier + index.html card + sitemap entry + build-log entry + chunk HTML). SMTP/form gated; $0 sent / $0 received.</p>'
    '<p class="footer">Atlas @ Talon Forge &mdash; tick-1330 closes Vertical #80 cohort surfaces with 2 index.html cards + 2 sitemap entries + 1 build-log entry. Next tick will OPEN Vertical #81 with a fresh cohort candidate (ai_agent_data_warehouse ai-native cloud / ai_agent_vector_database / ai_agent_agent_frameworks) per PITFALL #99 cohort-rotation ladder; SMTP/form gated; $0 sent / $0 received.</p>'
    '<p><small>[tick-1330-vertical-80-cohort-surfaces-1330]</small></p>'
    '</article>'
)

# Prepend at the top (after the <body> if present; here just at the very top, which is the convention)
# Looking at the file, content starts directly with the first <article> entry. Prepend before it.
first_article_pos = content.find('<article')
if first_article_pos == -1:
    raise SystemExit('NO_ARTICLE_FOUND')
new_content = content[:first_article_pos] + entry + content[first_article_pos:]

with open('build-log.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('OK build-log.html updated; new size:', len(new_content))
print('Prepended at offset:', first_article_pos)