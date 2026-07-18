"""Resume Tick 553 after leads.csv row 552 landed but the inherited malformed-row check stopped later surfaces."""
from __future__ import annotations

import csv
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
LEADS = REPO / "cold_email" / "leads.csv"
ENRICHED = REPO / "cold_email" / "leads_with_emails.csv"
BUILD_LOG = REPO / "build-log.html"
INDEX = "552"
TICK_ID = "2026-07-19-fast-exec-voxel51-552"
OLD_TOP = '<div class="tick-entry" data-tick="2026-07-19-fast-exec-v7-551">'

with LEADS.open("r", encoding="utf-8", newline="") as handle:
    lead_rows = list(csv.DictReader(handle))
lead_matches = [r for r in lead_rows if r.get("index") == INDEX]
assert len(lead_matches) == 1 and lead_matches[0].get("name") == "Voxel51"
assert None not in lead_matches[0]

enriched_row = {
    "lead_index": INDEX,
    "company": "Voxel51",
    "handle": "@Voxel51",
    "domain": "voxel51.com",
    "website": "https://voxel51.com",
    "founder": "Brian Moore (Co-Founder & CEO) + Jason Corso (Co-Founder & CSO)",
    "vertical": "computer_vision",
    "tier": "1",
    "best_email": "info@voxel51.com",
    "emails_found": "info@voxel51.com,support@voxel51.com",
    "guessed_emails": "security@voxel51.com,privacy@voxel51.com,founders@voxel51.com",
    "source_template": "552_voxel51.md",
    "tier_reason": (
        "Tier-1 computer_vision cohort sibling #4 after Roboflow 549 + Encord 550 + V7 Labs 551; "
        "FiftyOne open-source and Enterprise visual/multimodal data curation + annotation + embeddings + "
        "similarity search + model evaluation + secure on-prem/air-gapped deployment; founded 2018 at the "
        "University of Michigan by Brian Moore and Jason Corso; ISO 27001 and third-party testing verified on "
        "first-party security page; info@voxel51.com and support@voxel51.com verified on first-party privacy policy."
    ),
}

with ENRICHED.open("r", encoding="utf-8", newline="") as handle:
    reader = csv.DictReader(handle)
    fields = list(reader.fieldnames or [])
    before_rows = list(reader)
assert fields == [
    "lead_index", "company", "handle", "domain", "website", "founder", "vertical", "tier",
    "best_email", "emails_found", "guessed_emails", "source_template", "tier_reason",
]
matches = [r for r in before_rows if r.get("lead_index") == INDEX]
if not matches:
    with ENRICHED.open("a", encoding="utf-8", newline="") as handle:
        csv.DictWriter(handle, fieldnames=fields, quoting=csv.QUOTE_ALL).writerow(enriched_row)
    print("PASS enriched: row 552 appended")
elif len(matches) == 1 and matches[0].get("company") == "Voxel51":
    print("PASS enriched: row 552 already present")
else:
    raise AssertionError("unexpected enriched row 552 state")

entry = f'''<div class="tick-entry" data-tick="{TICK_ID}">
<h2>Tick 553 — Voxel51 / FiftyOne lead 552 (computer_vision sibling #4)</h2>
<p><strong>Shipped:</strong> Added the verified Voxel51 lead to both CSV schemas and created <code>cold_email/templates/552_voxel51.md</code>, a concise five-question vendor-DD pitch. First-party evidence: <code>info@voxel51.com</code> and <code>support@voxel51.com</code> on the privacy policy; Brian Moore (Co-Founder &amp; CEO) + Jason Corso (Co-Founder &amp; CSO), 2018 University of Michigan founding story, FiftyOne visual/multimodal data platform, and Ann Arbor address; ISO 27001, third-party security testing, and on-prem/air-gapped deployment on the security page.</p>
<p><strong>Revenue impact:</strong> +$500 audit / +$497 monthly-retainer pipeline ceiling. The computer_vision cohort now has four distinct wedges: Roboflow training/deployment, Encord annotation/medical, V7 document-AI/fine-tuning, and Voxel51 open-source data curation/model evaluation. Cash remains $0 because outbound credentials are still blocked.</p>
<p><strong>Next:</strong> Ship a focused V7 or Voxel51 SEO chunk, or add Superb AI as sibling #5. Outreach remains queued until one of Resend, SendGrid, or a Gmail App Password is available.</p>
</div>
'''

build_text = BUILD_LOG.read_text(encoding="utf-8")
anchor = 'data-tick="' + TICK_ID + '"'
if anchor not in build_text:
    assert build_text.startswith(OLD_TOP), "build-log top changed; unsafe resume"
    BUILD_LOG.write_text(entry + build_text, encoding="utf-8")
    print("PASS build-log: Tick 553 prepended")
else:
    print("PASS build-log: Tick 553 already present")

with ENRICHED.open("r", encoding="utf-8", newline="") as handle:
    final_rows = list(csv.DictReader(handle))
assert len([r for r in final_rows if r.get("lead_index") == INDEX]) == 1
final_log = BUILD_LOG.read_text(encoding="utf-8")
assert final_log.startswith('<div class="tick-entry" data-tick="' + TICK_ID + '">')
assert final_log.count(anchor) == 1
assert (REPO / "cold_email" / "templates" / "552_voxel51.md").exists()
print("RESUME PASS")
