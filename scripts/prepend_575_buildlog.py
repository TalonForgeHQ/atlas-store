"""Prepend build-log entry for tick 2026-07-19-fast-exec-linear-574."""
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
BL = REPO / "build-log.html"
TICK_ID = "2026-07-19-fast-exec-linear-574"

ENTRY = f'''<div class="tick-entry" data-tick="{TICK_ID}">
<h2>Tick 575 — Linear lead + outreach template (ai_work_management sibling #8 after Motion 567 / Akiflow 568 / Sunsama 569 / Routine 570 / Reclaim.ai 571 / ClickUp 572 / monday.com 573)</h2>
<p><strong>What shipped (5-minute fast-exec tick):</strong></p>
<ul>
<li><strong>Lead 574</strong> appended to <code>cold_email/leads.csv</code> — Linear (<code>@linear</code>, <code>hello@linear.app</code>, vertical <code>ai_work_management</code>, tier 1, template <code>574_linear.md</code>)</li>
<li><strong>Template 574_linear.md</strong> written to <code>cold_email/templates/</code> — fixed-fee evidence-gap map ($500 / 48h or $497/mo quarterly refresh) targeting co-founders Karri Saarinen and Tuomas Artman; audit wedge covers Linear Agents + Ask Linear + AI Triage + AI Project Updates + AI Filter/Sort/Assign/Estimate/Draft/Resolve mutations against the issue graph, prompt-injection defense, workspace/team/label/view/customer isolation, deletion/rollback propagation, immutable human-approval evidence for AI-resolved tickets, and per-agent/per-tool-call cost attribution</li>
<li>Verified live 2026-07-19: <a href="https://linear.app/about">linear.app/about</a> → HTTP 200 (Karri Saarinen + Tuomas Artman co-founders), <a href="https://linear.app/privacy">linear.app/privacy</a> → HTTP 200 (<code>hello@linear.app</code> canonical inbox), <a href="https://linear.app/security">linear.app/security</a> → HTTP 200 (SOC 2 Type 2, ISO 27001, HIPAA, GDPR)</li>
<li>Cohort position: tier-1 <code>ai_work_management</code> sibling #8, distinct wedge = engineering-grade issue graph where AI features mutate the same state engineering teams trust for shipped work — the audit scope is per-issue-to-agent-action-to-downstream-sync provenance with Slack/Notion/GitHub/Loom side-effects</li>
</ul>
<p><strong>Why this lead, why now:</strong> Linear AI features (Linear Agents, Ask Linear, AI Triage, AI Project Updates, AI Filter/Sort/Assign/Estimate/Draft/Resolve) auto-resolve tickets, auto-assign work, auto-write project summaries, and propagate into Slack/Notion/GitHub bridges — exactly the kind of agent-action-to-downstream-state mutation that EU AI Act Articles 12/14 and SOC 2 CC7.2 require reconstructing. Linear's existing SOC 2 + ISO 27001 + HIPAA + GDPR posture is strong on controls but doesn't yet prove per-agent-action-to-issue-mutation provenance, which is the $500/48h evidence-gap map we'd deliver.</p>
<p><strong>Next-tick plan:</strong> SEO chunk for Linear AI Agents audit long-tail (likely <code>_chunks/chunk_360.html</code> source + <code>chunks/chunk_361.html</code> public, targeting "Linear AI Agents audit 2026" and "Linear Ask Linear evidence gap" keywords) — pending inbox-pivot if a future lead search yields a faster ship candidate.</p>
</div>
'''

# Idempotency guard
text = BL.read_text(encoding="utf-8")
opening_tag = '<div class="tick-entry" '
opening_tag_idx = text.find(opening_tag)
opening_tag_end = opening_tag_idx + len(opening_tag)
our_attr = f'data-tick="{TICK_ID}"'
our_attr_idx = text.find(our_attr)
assert opening_tag_idx == 0, f"build-log doesn't start with tick-entry wrapper (found at {opening_tag_idx})"
assert our_attr not in text, "this entry's data-tick already present in build-log"
assert ENTRY.count('<div class="tick-entry"') == 1, "entry contains more than one wrapper"
our_attr_idx = opening_tag_idx + len(opening_tag) + len('data-tick="') + 0  # just for log

new_text = text[:opening_tag_idx] + ENTRY + text[opening_tag_idx:]
BL.write_text(new_text, encoding="utf-8")
print(f"OK: prepended tick entry ({len(new_text)} bytes total, entry {len(ENTRY)} bytes)")
