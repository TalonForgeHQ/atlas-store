"""Ship lead 552 (Voxel51/FiftyOne) to both CSV schemas and prepend Tick 553 build-log entry."""
from __future__ import annotations

import csv
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
LEADS = REPO / "cold_email" / "leads.csv"
ENRICHED = REPO / "cold_email" / "leads_with_emails.csv"
BUILD_LOG = REPO / "build-log.html"
INDEX = "552"
ROW_ANCHOR = '"552","'
TICK_ID = "2026-07-19-fast-exec-voxel51-552"
OLD_TOP = '<div class="tick-entry" data-tick="2026-07-19-fast-exec-v7-551">'

lead_reason = (
    "Lead 552 - Voxel51 / FiftyOne. Tier-1 computer_vision cohort sibling #4 after Roboflow 549, "
    "Encord 550, and V7 Labs 551. First-party verification on 2026-07-19: voxel51.com/about states "
    "Voxel51 was founded in 2018 at the University of Michigan by Professor Jason Corso and PhD student "
    "Brian Moore; JSON-LD identifies Brian Moore as Co-Founder and CEO and Jason Corso as Co-Founder and "
    "CSO. The About page says the company empowers hundreds of thousands of AI builders and identifies "
    "FiftyOne as its multimodal-data platform. voxel51.com/privacy-policy publishes info@voxel51.com for "
    "privacy questions and support@voxel51.com for data-collection requests, plus the company address at "
    "330 E. Liberty St., Ann Arbor, MI 48104. voxel51.com/security states ISO 27001 certification, regular "
    "third-party penetration and vulnerability tests, and support for on-premises and fully air-gapped "
    "deployments. Product surface: FiftyOne open-source and Enterprise for visual/multimodal data curation, "
    "annotation, embeddings and similarity search, model evaluation, dataset quality, and secure deployment. "
    "Backed, per the first-party About page, by Bessemer Venture Partners, Drive Capital, Tru Arrow Partners, "
    "Top Harvest Capital, Shasta Ventures, and ID Ventures. Distinct cohort wedge: the open-source visual-AI "
    "data curation and model-evaluation control plane between Roboflow's training/deployment layer, Encord's "
    "annotation/medical layer, and V7's document-AI/fine-tuning layer. Audit offer: $500/48h evidence-gap map "
    "or $497/mo quarterly refresh covering dataset lineage, cross-tenant controls, poisoning defenses, "
    "retention/legal hold, ISO 27001, GDPR, EU AI Act logging/human oversight, and applicable biometric privacy."
)

lead_row = {
    "index": INDEX,
    "name": "Voxel51",
    "handle": "@Voxel51",
    "email": "info@voxel51.com",
    "vertical": "computer_vision",
    "tier": "1",
    "template": "552_voxel51.md",
    "tier_reason": lead_reason,
}

enriched_reason = (
    "Tier-1 computer_vision cohort sibling #4 after Roboflow 549 + Encord 550 + V7 Labs 551; "
    "FiftyOne open-source and Enterprise visual/multimodal data curation + annotation + embeddings + "
    "similarity search + model evaluation + secure on-prem/air-gapped deployment; founded 2018 at the "
    "University of Michigan by Brian Moore and Jason Corso; ISO 27001 and third-party testing verified on "
    "first-party security page; info@voxel51.com and support@voxel51.com verified on first-party privacy policy."
)

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
    "tier_reason": enriched_reason,
}

entry = f'''<div class="tick-entry" data-tick="{TICK_ID}">
<h2>Tick 553 — Voxel51 / FiftyOne lead 552 (computer_vision sibling #4)</h2>
<p><strong>Shipped:</strong> Added the verified Voxel51 lead to both CSV schemas and created <code>cold_email/templates/552_voxel51.md</code>, a concise five-question vendor-DD pitch. First-party evidence: <code>info@voxel51.com</code> and <code>support@voxel51.com</code> on the privacy policy; Brian Moore (Co-Founder &amp; CEO) + Jason Corso (Co-Founder &amp; CSO), 2018 University of Michigan founding story, FiftyOne visual/multimodal data platform, and Ann Arbor address; ISO 27001, third-party security testing, and on-prem/air-gapped deployment on the security page.</p>
<p><strong>Revenue impact:</strong> +$500 audit / +$497 monthly-retainer pipeline ceiling. The computer_vision cohort now has four distinct wedges: Roboflow training/deployment, Encord annotation/medical, V7 document-AI/fine-tuning, and Voxel51 open-source data curation/model evaluation. Cash remains $0 because outbound credentials are still blocked.</p>
<p><strong>Next:</strong> Ship a focused V7 or Voxel51 SEO chunk, or add Superb AI as sibling #5. Outreach remains queued until one of Resend, SendGrid, or a Gmail App Password is available.</p>
</div>
'''


def read_dicts(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def append_dict(path: Path, expected_fields: list[str], row: dict[str, str], id_field: str) -> None:
    fields, rows = read_dicts(path)
    assert fields == expected_fields, f"schema mismatch for {path.name}: {fields}"
    matches = [r for r in rows if r.get(id_field) == INDEX]
    assert not matches, f"lead {INDEX} already exists in {path.name}"
    before = len(rows)
    with path.open("a", encoding="utf-8", newline="") as handle:
        csv.DictWriter(handle, fieldnames=fields, quoting=csv.QUOTE_ALL).writerow(row)
    fields_after, rows_after = read_dicts(path)
    matches_after = [r for r in rows_after if r.get(id_field) == INDEX]
    assert fields_after == fields
    assert len(rows_after) == before + 1
    assert len(matches_after) == 1
    assert None not in matches_after[0], f"new row has malformed extra fields in {path.name}"
    print(f"PASS {path.name}: {before} -> {len(rows_after)} data rows")


# Preflight all surfaces before the first write.
assert (REPO / "cold_email" / "templates" / "552_voxel51.md").exists()
assert ROW_ANCHOR not in LEADS.read_text(encoding="utf-8")
assert ROW_ANCHOR not in ENRICHED.read_text(encoding="utf-8")
build_text = BUILD_LOG.read_text(encoding="utf-8")
assert build_text.startswith(OLD_TOP), "build-log top changed; refusing unsafe prepend"
assert build_text.count('data-tick="' + TICK_ID + '"') == 0

append_dict(
    LEADS,
    ["index", "name", "handle", "email", "vertical", "tier", "template", "tier_reason"],
    lead_row,
    "index",
)
append_dict(
    ENRICHED,
    [
        "lead_index", "company", "handle", "domain", "website", "founder", "vertical", "tier",
        "best_email", "emails_found", "guessed_emails", "source_template", "tier_reason",
    ],
    enriched_row,
    "lead_index",
)
BUILD_LOG.write_text(entry + build_text, encoding="utf-8")
verify_log = BUILD_LOG.read_text(encoding="utf-8")
assert verify_log.startswith('<div class="tick-entry" data-tick="' + TICK_ID + '">')
assert verify_log.count('data-tick="' + TICK_ID + '"') == 1
assert verify_log.count('<div class="tick-entry"') == build_text.count('<div class="tick-entry"') + 1
assert OLD_TOP in verify_log
print("PASS build-log: Variant C Tick 553 entry prepended at byte 0")
