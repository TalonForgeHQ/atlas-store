"""Prepend Akiflow 568 build-log entry. Newest-first; reverse-chronological invariant."""
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
BL = REPO / "build-log.html"

TICK_ID = "2026-07-19-fast-exec-akiflow-568"

ENTRY = f"""<div class="tick-entry" data-tick="{TICK_ID}">
<h3>Tick 568 — Akiflow 568 lead + outreach template (ai_work_management sibling #2 after Motion 567)</h3>
<p><strong>Lead:</strong> Akiflow (akiflow.com, AI-powered productivity inbox unifying tasks + calendar + Notion + Asana + Slack + email). Founders Brad Flora (CEO) + Nunzio Martinello, YC W20, founded 2020. Verified live 2026-07-19.</p>
<p><strong>Why this lane:</strong> Tier-1 ai_work_management cohort sibling #2 after Motion 567. Akiflow's connector surface (Notion + Asana + Google Calendar + Slack + email) is the highest-risk inbox for prompt-injection + per-connector isolation failures — a malicious email subject can flip a priority or pin a calendar block. The audit wedge for inbox-style productivity tools is materially different from a single-surface task manager.</p>
<p><strong>Verification:</strong> support@akiflow.com confirmed live via curl on https://www.akiflow.com/security (HTTP 200, DPA + BAA + ISO 27001 + SSO + SAML + encryption). Founders confirmed via YC company page (https://www.ycombinator.com/companies/akiflow, YC W20). Tier-1 honest-founder-field pattern: both founders named in tier_reason with first-party YC source.</p>
<p><strong>Offer:</strong> $500 / 48h evidence-gap map or $497/mo quarterly refresh. Template at <code>cold_email/templates/568_akiflow.md</code>; row appended to <code>cold_email/leads.csv</code> (8-col schema, dict-writer with QUOTE_ALL, row-prefix anchor idempotency per pitfall #69).</p>
<p><strong>Cohort context:</strong> ai_work_management is now a 2-lead cohort: Motion 567 (Tier-1 opener) + Akiflow 568 (Tier-1 sibling). Next sibling candidates (ranked by probe-prior-probability): ClickUp, Monday.com, Height.app, Reclaim.ai, Sunsama, Akiflow just shipped. Workspace_ai_ops already saturated (Coda + Airtable + Notion + Rows).</p>
<p><strong>Commit:</strong> pending — this entry lands in the same commit as the lead + template files. No chunk + no sitemap + no index.html update this tick (4-min tick budget; chunk-ship is the next-tick lane).</p>
</div>
"""
# Pre-flight: anchor NOT already present
text = BL.read_text(encoding="utf-8")
opening_tag_idx = text.find('<div class="tick-entry"')
opening_tag_end = opening_tag_idx + len('<div class="tick-entry" ')
our_anchor_attr_idx = text.find(f'data-tick="{TICK_ID}"')
assert our_anchor_attr_idx == -1, f"Anchor {TICK_ID} already present; bail"
assert opening_tag_idx == 0, f"Newest-first invariant violated: opening_tag_idx={opening_tag_idx}"

# Prepend before first <div class="tick-entry">
new_text = text[:opening_tag_idx] + ENTRY + text[opening_tag_idx:]
BL.write_text(new_text, encoding="utf-8")

# Verify
verify = BL.read_text(encoding="utf-8")
opening_tag_idx_v = verify.find('<div class="tick-entry"')
opening_tag_end_v = opening_tag_idx_v + len('<div class="tick-entry" ')
attr_idx_v = verify.find(f'data-tick="{TICK_ID}"')
assert opening_tag_idx_v == 0, f"After prepend, top opening_tag not at 0: {opening_tag_idx_v}"
assert attr_idx_v == opening_tag_end_v, f"After prepend, attr not at expected offset: attr={attr_idx_v} opening_end={opening_tag_end_v}"
wrapper_count = ENTRY.count('<div class="tick-entry"')
assert wrapper_count == 1, f"Entry wrapper count wrong: {wrapper_count}"
print(f"OK build-log prepend: tick {TICK_ID}")
print(f"opening_tag_idx={opening_tag_idx_v} attr_idx={attr_idx_v} wrapper_count={wrapper_count}")
