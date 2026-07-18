"""Idempotently append Fellow.ai lead 560 and prepend Tick 561 build-log entry."""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEADS = ROOT / "cold_email" / "leads.csv"
TEMPLATE = ROOT / "cold_email" / "templates" / "560_fellow_ai.md"
BUILD_LOG = ROOT / "build-log.html"
TICK_ID = "2026-07-19-fast-exec-fellow-ai-560"

row = [
    "560",
    "Fellow.ai",
    "@FellowAInotes",
    "privacy@fellow.app",
    "meeting_ai_ops",
    "1",
    "560_fellow_ai.md",
    (
        "Real company verified 2026-07-19 from first-party pages: https://fellow.ai/ "
        "(AI Meeting Assistant and Notetaker; botless recording across Zoom, Teams, Google Meet, Webex, "
        "and in-person meetings), https://fellow.ai/about (founded November 2017 by Aydin Mirzaee, CEO; "
        "Amin Mirzaee, CPO; and Samuel Cormier-Iijima, CTO), and https://fellow.ai/privacy-policy "
        "(canonical mailto:privacy@fellow.app). First-party pages state GDPR and SOC 2 Type II controls. "
        "Tier-1 meeting_ai_ops sibling #4 after Granola 557, Read AI 558, and Avoma 559. Audit wedge: "
        "capture-to-transcript-to-summary-to-action provenance, consent/pause/deletion propagation, spoken "
        "and connector prompt-injection defense, workspace/permission/OAuth isolation, WORM retention, and "
        "per-meeting cost attribution. Offer: $500/48h evidence-gap map or $497/mo quarterly refresh. "
        "The legacy fellow.app site redirected to current canonical fellow.ai; the public privacy inbox "
        "remains privacy@fellow.app."
    ),
]

if not TEMPLATE.exists():
    raise SystemExit(f"missing template: {TEMPLATE}")

with LEADS.open("r", encoding="utf-8", newline="") as fh:
    rows = list(csv.reader(fh))
id_matches = [existing for existing in rows if existing and existing[0] == row[0]]
if id_matches:
    complete = (
        len(id_matches) == 1
        and id_matches[0][:7] == row[:7]
        and TEMPLATE.exists()
        and TICK_ID in BUILD_LOG.read_text(encoding="utf-8")
    )
    if complete:
        print("NO-OP: lead 560 and Tick 561 already exist")
        raise SystemExit(0)
    raise SystemExit("conflicting lead 560 exists; refusing mutation")
if any(len(existing) > 1 and existing[1].strip().lower() in {"fellow", "fellow.ai"} for existing in rows):
    raise SystemExit("Fellow.ai already exists; refusing duplicate")
raw = LEADS.read_bytes()
with LEADS.open("a", encoding="utf-8", newline="") as fh:
    if raw and not raw.endswith((b"\n", b"\r")):
        fh.write("\n")
    csv.writer(fh, quoting=csv.QUOTE_ALL, lineterminator="\n").writerow(row)

entry = f'''<div class="tick-entry" data-tick="{TICK_ID}">
<h2>Tick 561 — Fellow.ai lead 560 + focused outreach template (meeting_ai_ops sibling #4)</h2>
<p><strong>Artifact:</strong> Added <code>cold_email/leads.csv</code> row 560 and <code>cold_email/templates/560_fellow_ai.md</code>. First-party pages verify Fellow.ai as a real AI meeting-assistant company founded in November 2017 by Aydin Mirzaee (CEO), Amin Mirzaee (CPO), and Samuel Cormier-Iijima (CTO).</p>
<p><strong>Verification:</strong> <code>fellow.ai</code>, <code>/about</code>, and <code>/privacy-policy</code> returned HTTP 200. The product covers botless capture across Zoom, Teams, Google Meet, Webex, and in-person meetings; first-party pages state GDPR and SOC 2 Type II controls; the privacy policy publishes <code>mailto:privacy@fellow.app</code>.</p>
<p><strong>Revenue progress:</strong> +$500 fixed-price / 48-hour evidence-gap audit opportunity, with a $497/mo quarterly refresh. The wedge covers capture-to-transcript-to-summary-to-action provenance, consent/pause/deletion propagation, spoken and connector prompt injection, workspace/permission isolation, immutable retention, and per-meeting cost attribution.</p>
<p><strong>Pivot:</strong> The originally queued <code>fellow.app</code> surface redirects to the current canonical <code>fellow.ai</code> site, so verification pivoted to the live canonical About and Privacy pages while preserving the first-party published <code>privacy@fellow.app</code> inbox. No login-gated community action or forbidden port was touched; outbound remains queued pending SMTP credentials.</p>
</div>
'''
text = BUILD_LOG.read_text(encoding="utf-8")
if TICK_ID in text:
    raise SystemExit(f"build-log tick already exists: {TICK_ID}")
BUILD_LOG.write_text(entry + text, encoding="utf-8", newline="")
print("PASS: appended lead 560 and prepended Tick 561 build-log entry")
