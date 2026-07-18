"""Idempotently append tl;dv lead 563 and prepend Tick 565 build-log entry."""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEADS = ROOT / "cold_email" / "leads.csv"
TEMPLATE = ROOT / "cold_email" / "templates" / "563_tldv.md"
BUILD_LOG = ROOT / "build-log.html"
TICK_ID = "2026-07-19-fast-exec-tldv-563"

row = [
    "563",
    "tl;dv",
    "@tldv_io",
    "marketing@tldv.io",
    "meeting_ai_ops",
    "2",
    "563_tldv.md",
    (
        "Real company and real website verified 2026-07-19 from first-party pages. https://tldv.io/ "
        "returned HTTP 200 and documents Google Meet + Zoom + Microsoft Teams recording, transcription, "
        "AI notes, multi-meeting insights, sales coaching, CRM updates, and follow-ups. "
        "https://tldv.io/privacy/ returned HTTP 200, identifies Tldx Solutions GmbH, publishes the canonical "
        "first-party marketing@tldv.io inbox, and states customer recordings, transcripts, notes, files, "
        "and other content are not used to train or fine-tune foundation models. "
        "https://tldv.io/imprint/ returned HTTP 200 and names Raphael Allstadt, Carlo Thissen, and Allan "
        "Bettarel as company representatives under HRB 23730 at Amtsgericht Aachen. "
        "https://tldv.io/features/security-commitment/ returned HTTP 200 and states SOC 2 Type II, "
        "ISO 27001-class infrastructure, encryption, GDPR compliance, and Europe-or-US AI hosting. "
        "Tier-2 meeting_ai_ops cohort sibling #7 after Granola 557 + Read AI 558 + Avoma 559 + Fellow.ai "
        "560 + MeetGeek 561 + Sembly AI 562 because the verified first-party pages name legal representatives "
        "but do not explicitly label them founders. Audit wedge: meeting-to-recording-to-transcript-to-AI-note "
        "or multi-meeting-insight-to-sales-coaching-to-CRM-write provenance, consent/deletion propagation, "
        "prompt-injection defense, tenant/connector/Europe-US isolation, model-training-restriction evidence, "
        "WORM retention, and per-meeting cost attribution. Offer: $500/48h evidence-gap map or $497/mo "
        "quarterly refresh."
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
        print("NO-OP: lead 563 and Tick 565 already exist")
        raise SystemExit(0)
    raise SystemExit("conflicting lead 563 exists; refusing mutation")
if any(len(existing) > 1 and existing[1].strip().lower() in {"tl;dv", "tldv"} for existing in rows):
    raise SystemExit("tl;dv already exists; refusing duplicate")
raw = LEADS.read_bytes()
with LEADS.open("a", encoding="utf-8", newline="") as fh:
    if raw and not raw.endswith((b"\n", b"\r")):
        fh.write("\n")
    csv.writer(fh, quoting=csv.QUOTE_ALL, lineterminator="\n").writerow(row)

entry = f'''<div class="tick-entry" data-tick="{TICK_ID}">
<h2>Tick 565 — tl;dv lead 563 + focused outreach template (meeting_ai_ops sibling #7)</h2>
<p><strong>Artifact:</strong> Added <code>cold_email/leads.csv</code> row 563 and <code>cold_email/templates/563_tldv.md</code>. First-party pages verify tl;dv / Tldx Solutions GmbH as a real AI meeting platform and identify Raphaël Allstadt, Carlo Thissen, and Allan Bettarel as company representatives.</p>
<p><strong>Verification:</strong> <code>tldv.io</code>, <code>/privacy/</code>, <code>/imprint/</code>, and <code>/features/security-commitment/</code> returned HTTP 200. The product covers Google Meet, Zoom, and Teams capture; transcription; AI notes; multi-meeting insights; sales coaching; and CRM follow-up. Privacy publishes <code>marketing@tldv.io</code> and a no-customer-content foundation-model-training commitment; Security states SOC 2 Type II and Europe-or-US AI hosting.</p>
<p><strong>Revenue progress:</strong> +$500 fixed-price / 48-hour evidence-gap audit opportunity, with a $497/mo quarterly refresh. The wedge covers meeting-to-recording-to-transcript-to-insight-to-coaching-to-CRM-write provenance, consent/deletion propagation, spoken/calendar/CRM prompt injection, tenant/connector/regional isolation, model-training restriction evidence, WORM retention, and per-meeting cost attribution.</p>
<p><strong>Pivot:</strong> tl;dv was previously skipped because first-party pages did not explicitly label the named company representatives as founders. This tick preserved that distinction and shipped an honest Tier-2 row instead of fabricating founder titles; it also pivoted from the guessed <code>/security/</code> path (HTTP 403) to the live first-party <code>/features/security-commitment/</code> page (HTTP 200). No login-gated community action or forbidden port was touched; outbound remains queued pending SMTP credentials.</p>
</div>
'''
text = BUILD_LOG.read_text(encoding="utf-8")
if TICK_ID in text:
    raise SystemExit(f"build-log tick already exists: {TICK_ID}")
BUILD_LOG.write_text(entry + text, encoding="utf-8", newline="")
print("PASS: appended lead 563 and prepended Tick 565 build-log entry")
