"""Prepend a Variant C build-log entry for the Linear 56 template-backfill tick."""
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
BL = REPO / "build-log.html"

TICK_ID = "2026-07-18-fast-exec-linear-56-template-backfill"
ANCHOR = '<div class="tick-entry" data-tick="'

NEW_ENTRY = f'''<div class="tick-entry" data-tick="{TICK_ID}">
<h2>Fast Execution — Linear 56 template backfill</h2>
<p><strong>Artifact:</strong> shipped the missing <code>cold_email/templates/56_linear.md</code> for the existing verified Linear lead (b2b_saas Tier-1, Lead 56). Live first-party re-checks on 2026-07-18 confirmed <code>linear.app/about</code> (1.7MB server-rendered) and <code>linear.app/privacy</code> (1.7MB server-rendered, exposing canonical <code>hello@linear.app</code> via privacy contact pattern). The founder-personalized offer covers cross-workspace agent provenance, prompt and classifier change control, customer-data residency + prompt-injection defense across customer comments / attachments / webhook payloads, workspace-scoped tenant isolation + customer-PII redaction (emails + internal URLs + customer names in issue text), and WORM-capable incident evidence + rate-limit forensics at <strong>$500 / 48 hours</strong>.</p>
<p><strong>Progress:</strong> template inventory 487→488 and missing lead-template gaps 11→10. Reuses the verified Voiceflow 427 template shape (5-audit-question scaffold + procurement-ready gap map mapped to SOC 2 CC6.1 + CC7.2, EU AI Act Art. 12/14/15, GDPR Art. 28, ISO 42001, NIST AI RMF, OWASP LLM Top 10, MITRE ATLAS, ISO 27701) but retargeted to Linear's AI triage, AI auto-label, duplicate detection, customer-impact summary, and customer-data residency surface. Co-founders named correctly (Tuomas Artman CTO + Karri Saarinen).</p>
<p><strong>Pivot:</strong> fresh-lead research would have burned the inbox-verify budget (Patreon / TUNE / Buy Me a Coffee / Refersion SPA-wall traps from prior tick), so backfilled a verified Tier-1 lead with a missing template. Linear is canonical issue-tracking with AI agents ingesting customer intent, customer priority, and customer SLA context — the audit stakes are higher than a chat-only agent because misfiring AI labels propagate into customer-facing status pages and customer escalation queues.</p>
</div>
'''

text = BL.read_text(encoding="utf-8")
assert ANCHOR in text, "build-log.html missing canonical Variant C anchor"
anchor_idx = text.find(ANCHOR)
assert anchor_idx == 0, f"build-log.html top-of-file is not the canonical Variant C wrapper; first anchor at {anchor_idx}"

new_count = text.count(f'data-tick="{TICK_ID}"')
assert new_count == 0, f"build-log.html already contains tick id {TICK_ID}; abort to avoid double-prepend"

text = text[:anchor_idx] + NEW_ENTRY + text[anchor_idx:]
BL.write_text(text, encoding="utf-8")

final_count = text.count(f'data-tick="{TICK_ID}"')
print(f"PREPEND OK; data-tick count == {final_count}; build-log.html size now {len(text):,} bytes")