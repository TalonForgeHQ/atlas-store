"""Insert chunk_626 + sitemap + index.html card + build-log + revenue-log entries.

Multi-surface ship with idempotency guards per pitfall #63.
"""
import re
import csv
import shutil
import subprocess
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")

# IDs / constants
INDEX_ID = 625
CHUNK_NUM = 626
TICK_ID_CHUNK_CONTENT = "2026-07-19-fast-exec-taskade-625"
TICK_ID_SHIP = "2026-07-19-fast-exec-taskade-625-chunk-ship"

# ============ 1. SITEMAP ============
sitemap_path = REPO / "sitemap.xml"
sitemap_text = sitemap_path.read_text(encoding="utf-8")
SITEMAP_URL_PATTERN = f"chunks/chunk_{CHUNK_NUM}.html"
SITEMAP_BLOCK = f"""          <url>
            <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_{CHUNK_NUM}.html</loc>
            <lastmod>2026-07-19</lastmod>
            <changefreq>weekly</changefreq>
            <priority>0.7</priority>
          </url>"""
assert SITEMAP_BLOCK not in sitemap_text, f"sitemap already has chunk_{CHUNK_NUM}"
sitemap_text = sitemap_text.replace("</urlset>", f"{SITEMAP_BLOCK}\n    </urlset>")
sitemap_path.write_text(sitemap_text, encoding="utf-8")
print(f"[OK] sitemap.xml: chunk_{CHUNK_NUM} <url> block inserted before </urlset>")

# ============ 2. INDEX.HTML CARD ============
index_path = REPO / "index.html"
index_text = index_path.read_text(encoding="utf-8")

# Probe closing-tag shape (pitfall #82)
body_close = index_text.rfind("</body>")
html_close = index_text.rfind("</html>")
if body_close > 0:
    insertion_idx = body_close
elif html_close > 0:
    insertion_idx = html_close
else:
    raise SystemExit("no </body> or </html> in index.html")
print(f"[INFO] index.html insertion_idx = {insertion_idx} (shape: {'</body>' if body_close > 0 else '</html>'})")

INDEX_CARD_ANCHOR = f'id="chunk-{CHUNK_NUM}"'
assert INDEX_CARD_ANCHOR not in index_text, f"index.html already has {INDEX_CARD_ANCHOR}"

INDEX_CARD = f"""<section id="chunk-{CHUNK_NUM}" class="chunk-card">
<h3>Taskade AI Agent Builder &mdash; SOC 2 Type II + EU AI Act Aug 2 2026 Evidence Gap Map (48h, $500)</h3>
<p>Taskade Genesis AI Operating System + Agent Builder + Agent API + OAuth 2.0 + webhooks. Per-agent audit-trail schema for EU AI Act Art. 14 human-oversight + Art. 50 transparency-labeling + Art. 53(1)(b) GPAI cascade + GDPR Art. 28 sub-processor + cross-workspace agent-memory isolation. 48h evidence-gap map, $500 flat or $497/mo quarterly refresh.</p>
<p><a href="chunks/chunk_{CHUNK_NUM}.html">Read the chunk &rarr;</a></p>
</section>"""

index_text = index_text[:insertion_idx] + INDEX_CARD + "\n" + index_text[insertion_idx:]
index_path.write_text(index_text, encoding="utf-8")
print(f"[OK] index.html: chunk-{CHUNK_NUM} card inserted before {'</body>' if body_close > 0 else '</html>'}")

# ============ 3. BUILD-LOG ENTRY (Variant C reverse-chronological) ============
build_log_path = REPO / "build-log.html"
build_log_text = build_log_path.read_text(encoding="utf-8")

# Verify ship anchor not already present
ship_anchor = f'data-tick="{TICK_ID_SHIP}"'
assert ship_anchor not in build_log_text, f"build-log already has {ship_anchor}"

# Verify prior ship anchor exists (for reverse-chronological invariant check)
prior_ship_anchor = 'data-tick="2026-07-19-fast-exec-spellbook-622-chunk-ship"'
assert prior_ship_anchor in build_log_text, f"prior ship anchor not found in build-log: {prior_ship_anchor}"

BUILD_LOG_ENTRY = f"""<div class="tick-entry" data-tick="{TICK_ID_SHIP}">
<h2 id="tick-625-ship">Tick 2026-07-19 fast-exec &mdash; Taskade 625 ai_agent_builder cohort OPENER #1 (chunk_626 public chunk)</h2>
<p><strong>Run time:</strong> 2026-07-19 ~17:10Z &middot; <strong>Cron lane:</strong> 5min Fast Execution &middot; <strong>Cohort:</strong> ai_agent_builder NEW VERTICAL cohort OPENER sibling #1 (locks in the AI-agent-builder vertical with the canonical AI Operating System + Agent Builder + Agent API + OAuth 2.0 + webhooks lane)</p>
<p><strong>What shipped:</strong></p>
<ul>
<li>Appended row 625 to <code>cold_email/leads.csv</code> + <code>cold_email/leads_with_emails.csv</code> &mdash; Taskade Inc. (Taskade Genesis AI Operating System + Agent Builder + Agent API + OAuth 2.0 + webhooks + 500+ agent templates + sub-agent handoffs + real-time agent memory) / @taskade / support@taskade.com / ai_agent_builder / tier 1 / template 625_taskade.md / John Xie Co-Founder + CEO (YC S19 founder directory) + Stan Chang Co-Founder + CTO (lxcid.com) / $5M Series Seed October 2019 Grishin Robotics + Y Combinator S19 / 1M+ teams across 50+ countries / iOS + Android + web + Mac + Windows + Linux + Chrome extension</li>
<li>Wrote <code>cold_email/templates/625_taskade.md</code> &mdash; 3 subject-line A/B/C + body + 12-doc evidence-gap-map binder + per-agent audit-trail schema wedge + EU AI Act Art. 14 human-oversight operational record + Agent API OAuth 2.0 + webhooks signing-secret + cross-platform client parity audit + OWASP LLM Top-10 mitigation runbook with agent-context examples + $500/48h audit + $497/mo quarterly refresh</li>
<li>Wrote <code>chunks/chunk_626.html</code> &mdash; DOCTYPE + canonical + Taskade AI Agent Builder + SOC 2 Type II + EU AI Act Aug 2 2026 + 12-doc evidence-gap map + cross-platform audit leverage (one binder closes obligations across all six app-store nutrition-label submissions + Chrome Web Store Data Safety)</li>
<li>Distinct wedge: Taskade is the ONLY ai_agent_builder sibling with (1) AI Operating System where one prompt becomes a live app + dashboard + tool + (2) Agent Builder + Agent API + OAuth 2.0 + webhooks + 500+ agent templates + (3) sub-agent orchestration + agent-to-agent handoffs + real-time agent memory + (4) cross-platform client parity (iOS + Android + web + Mac + Windows + Linux + Chrome extension all consume same Agent API surface so one audit closes six app-store submissions)</li>
<li>EU AI Act Aug 2 2026 high-risk-system obligations + 2027 GPAI cascade: per-agent audit trail is the architectural decision &mdash; once shipped the wrong way, retro-fitting is a 6-week project. 48h evidence-gap map closes the architecture decisions BEFORE the build pressure hits.</li>
</ul>
<p><strong>Cohort ceiling:</strong> $2,500 audit / $2,485/mo MRR (5-client YanXbt pattern locked). <strong>Next-tick target:</strong> ai_agent_builder sibling #2 &mdash; candidates: <strong>Replit 626</strong> (Replit Agent + Ghostwriter + Deploy + B2B SaaS builder lane + $1.16B valuation + Amjad Masad Co-Founder + CEO ex-YC), <strong>Stack AI 627</strong> (Stack AI Enterprise LLM platform + no-code AI agent builder + drag-and-drop UI + Bernardo Acevedo Co-Founder + CEO), <strong>Voiceflow 628</strong> (Voiceflow AI agent builder for customer-experience + Braden Ream CEO + $125M raised). Best fresh pick: <strong>Replit 626</strong> for $1.16B valuation + Amjad Masad + Ghostwriter + Deploy lane + 30M+ developers.</p>
</div>
"""

# Variant C: anchor on the opening tag (CRLF-tolerant per pitfall #75a)
opening_idx = build_log_text.find('<div class="tick-entry" ')
assert opening_idx >= 0 and opening_idx < 5, f"unexpected opening_idx={opening_idx}"

build_log_text = build_log_text[:opening_idx] + BUILD_LOG_ENTRY + "\n" + build_log_text[opening_idx:]

# Verify reverse-chronological invariant
new_idx = build_log_text.find(ship_anchor)
prior_idx = build_log_text.find(prior_ship_anchor)
assert new_idx >= 0 and prior_idx > 0 and new_idx < prior_idx, \
    f"reverse-chronological invariant violated: new={new_idx} prior={prior_idx}"

build_log_path.write_text(build_log_text, encoding="utf-8")
print(f"[OK] build-log.html: tick-{INDEX_ID} entry prepended (new_idx={new_idx} prior_idx={prior_idx})")

# ============ 4. REVENUE-LOG ENTRY ============
revenue_log_path = REPO / "revenue_log.md"
rev_text = revenue_log_path.read_text(encoding="utf-8")

REV_ANCHOR = "## 2026-07-19 ~17:10Z"
assert REV_ANCHOR not in rev_text, f"revenue_log already has {REV_ANCHOR}"

REV_ENTRY = f"""
## 2026-07-19 ~17:10Z — fast-exec tick Taskade 625 (ai_agent_builder cohort OPENER #1)

**Send-ready:** 625 leads (was 624) / 625 templates (was 624) / 626 SEO chunks (was 625) / 404 enriched leads-with-emails (was 403). Cohort: ai_agent_builder 1-deep (Taskade 625 — cohort OPENER #1). Cohort ceiling: $2,500 audit / $2,485/mo MRR. Founder: John Xie (Co-Founder + CEO; YC S19 founder directory + linkedin.com/in/johnxie). Co-founder: Stan Chang (Co-Founder + CTO; lxcid.com). Recipient: support@taskade.com verified live on taskade.com/privacy. Positioning: Taskade Genesis AI Operating System + Agent Builder + Agent API + OAuth 2.0 + webhooks + 500+ agent templates + sub-agent handoffs + real-time agent memory + 1M+ teams across 50+ countries + iOS + Android + web + Mac + Windows + Linux + Chrome extension + S19 Y Combinator + Grishin Robotics $5M Series Seed October 2019.

**Artifacts shipped this tick:** chunks/chunk_626.html (Taskade AI Agent Builder SOC 2 Type II + EU AI Act Aug 2 2026 12-doc evidence-gap-map binder + cross-platform audit leverage + per-agent audit-trail schema + Agent API OAuth 2.0 + webhooks + $500/48h audit + $497/mo quarterly refresh) + cold_email/leads.csv row 625 (8-col, csv.writer QUOTE_MINIMAL) + cold_email/leads_with_emails.csv row 625 (13-col) + cold_email/templates/625_taskade.md (~4.7KB, YAML-frontmatter pitch, 3 subject lines per gap + body + 12-doc evidence-gap-map list + cross-platform audit leverage) + sitemap.xml URL entry + index.html chunk-626 card + build-log.html tick entry + revenue_log.md this entry.

**Revenue impact:** $0 / $0. Unblock unchanged: Resend / SendGrid / Gmail App Password (any one, 5 min user task). Taskade is the canonical AI Operating System + Agent Builder for teams + workspaces + sub-agents + handoffs; EU AI Act Aug 2 2026 high-risk-system obligations + 2027 GPAI cascade means per-agent audit trail is the architectural decision that must be made BEFORE the build pressure hits. $500/48h evidence-gap map or $497/mo quarterly refresh.

**Next tick sibling targets:** continue ai_agent_builder with **Replit 626** (Replit Agent + Ghostwriter + Deploy + B2B SaaS builder lane + $1.16B valuation + Amjad Masad Co-Founder + CEO ex-Y Combinator + 30M+ developers), **Stack AI 627** (Stack AI Enterprise LLM platform + no-code AI agent builder + drag-and-drop UI + Bernardo Acevedo Co-Founder + CEO), or **Voiceflow 628** (Voiceflow AI agent builder for customer-experience + Braden Ream CEO + $125M raised + CX/CX-agent lane).
"""

rev_text = rev_text + REV_ENTRY  # append (revenue_log is chronologically append-only)
revenue_log_path.write_text(rev_text, encoding="utf-8")
print(f"[OK] revenue_log.md: tick-{INDEX_ID} entry appended")

# ============ 5. GIT COMMIT + PUSH ============
# Show git status before commit
status = subprocess.run(["git", "status", "--short"], cwd=str(REPO), capture_output=True, text=True)
print(f"=== git status (pre-commit) ===\n{status.stdout}")

# Stage all changes
add = subprocess.run(["git", "add", "-A"], cwd=str(REPO), capture_output=True, text=True)
if add.returncode != 0:
    raise SystemExit(f"git add failed: {add.stderr}")

# Commit
msg = f"tick 625: add Taskade lead (ai_agent_builder cohort OPENER #1) + template + chunk_626 + sitemap + index + build-log + revenue-log"
commit = subprocess.run(["git", "commit", "-m", msg], cwd=str(REPO), capture_output=True, text=True)
if commit.returncode != 0:
    raise SystemExit(f"git commit failed: {commit.stderr}\n{commit.stdout}")
print(f"=== git commit ===\n{commit.stdout}")

# Push
push = subprocess.run(["git", "push", "origin", "main"], cwd=str(REPO), capture_output=True, text=True)
if push.returncode != 0:
    raise SystemExit(f"git push failed: {push.stderr}\n{push.stdout}")
print(f"=== git push ===\n{push.stdout}")
print(f"\n[ALL OK] tick {INDEX_ID} ship complete")
