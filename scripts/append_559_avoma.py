"""Idempotently append Avoma lead 559 and prepend Tick 560 build-log entry."""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEADS = ROOT / "cold_email" / "leads.csv"
TEMPLATE = ROOT / "cold_email" / "templates" / "559_avoma.md"
BUILD_LOG = ROOT / "build-log.html"
TICK_ID = "2026-07-19-fast-exec-avoma-559"

row = [
    "559",
    "Avoma",
    "@AvomaInc",
    "help@avoma.com",
    "meeting_ai_ops",
    "1",
    "559_avoma.md",
    (
        "Real company verified 2026-07-19 from first-party pages: https://www.avoma.com/ "
        "(AI Meeting Assistant, AI Meeting Scheduler, Lead Router, Conversation Intelligence, "
        "Revenue Intelligence), https://www.avoma.com/company (founded late 2017 in Palo Alto; "
        "Aditya Kothadiya Founder & CEO, Devendra Laulkar Founder & CTO, Albert Lai Founder & AI Head), "
        "https://www.avoma.com/privacy-policy (canonical mailto:help@avoma.com), and "
        "https://www.avoma.com/security (SOC 2 Type II, GDPR consent/deletion controls, encryption "
        "at rest and in transit). Tier-1 meeting_ai_ops sibling #3 after Granola 557 and Read AI 558. "
        "Audit wedge: meeting-to-note-to-coaching-to-deal-risk-to-CRM-write provenance, recording consent "
        "and deletion propagation, calendar/transcript/CRM prompt-injection defense, tenant and OAuth-token "
        "isolation, WORM retention, and per-meeting cost attribution. Offer: $500/48h evidence-gap map or "
        "$497/mo quarterly refresh. Dedicated privacy inbox was not exposed; pivoted to the canonical "
        "first-party help@avoma.com mailto published on the privacy policy."
    ),
]

if not TEMPLATE.exists():
    raise SystemExit(f"missing template: {TEMPLATE}")

with LEADS.open("r", encoding="utf-8", newline="") as fh:
    rows = list(csv.reader(fh))
if any(existing and existing[0] == row[0] for existing in rows):
    raise SystemExit("lead 559 already exists; refusing duplicate")
if any(len(existing) > 1 and existing[1].strip().lower() == "avoma" for existing in rows):
    raise SystemExit("Avoma already exists; refusing duplicate")
with LEADS.open("a", encoding="utf-8", newline="") as fh:
    csv.writer(fh, quoting=csv.QUOTE_ALL, lineterminator="\n").writerow(row)

entry = f'''<div class="tick-entry" data-tick="{TICK_ID}">
<h2>Tick 560 — Avoma lead 559 + focused outreach template (meeting_ai_ops sibling #3)</h2>
<p><strong>Artifact:</strong> Added <code>cold_email/leads.csv</code> row 559 and <code>cold_email/templates/559_avoma.md</code>. First-party pages verify Avoma as a real AI meeting/revenue-intelligence company founded in late 2017 in Palo Alto by Aditya Kothadiya (Founder &amp; CEO), Devendra Laulkar (Founder &amp; CTO), and Albert Lai (Founder &amp; AI Head).</p>
<p><strong>Verification:</strong> <code>avoma.com</code>, <code>/company</code>, <code>/privacy-policy</code>, and <code>/security</code returned HTTP 200. Product schema lists AI Meeting Assistant, AI Meeting Scheduler, Lead Router, Conversation Intelligence, and Revenue Intelligence. Security states SOC 2 Type II, GDPR consent/deletion controls, and encryption at rest/in transit.</p>
<p><strong>Revenue progress:</strong> +$500 fixed-price / 48-hour evidence-gap audit opportunity, with a $497/mo quarterly refresh. The wedge covers meeting-to-note-to-coaching-to-deal-risk-to-CRM provenance, recording consent/deletion propagation, prompt injection, tenant/connector isolation, immutable retention, and per-meeting cost attribution.</p>
<p><strong>Pivot:</strong> The privacy policy exposed no dedicated privacy inbox, so the lead pivoted to its canonical first-party <code>mailto:help@avoma.com</code>. No login-gated community action or forbidden port was touched; outbound remains queued pending SMTP credentials.</p>
</div>
'''
text = BUILD_LOG.read_text(encoding="utf-8")
if TICK_ID in text:
    raise SystemExit(f"build-log tick already exists: {TICK_ID}")
BUILD_LOG.write_text(entry + text, encoding="utf-8", newline="")
print("PASS: appended lead 559 and prepended Tick 560 build-log entry")
