import csv
from pathlib import Path

ROOT = Path(r"C:\Users\Potts\projects\atlas-store")
INDEX = "744"
REASON = (
    "Lead 744 — Monica (monica.im multi-model browser and app AI assistant; founder Xiao Hong) — "
    "real company, real website, real founder, and first-party contact route verified 2026-07-20. "
    "Monica's current homepage describes an all-in-one assistant powered by GPT-5.5, Claude 4.7 Opus, "
    "Gemini 3.1 Pro, GPT Image 2, Sora 2, Nano Banana 2, and other models across chat, search, writing, "
    "document summaries, translation, code, image, and video workflows. The first-party Privacy Policy "
    "(last updated June 14, 2024; effective February 28, 2023) publishes contact@monica.im. Distinct evidence wedge: "
    "request/source context -> selected provider/model/version -> generated output -> user accept/edit/reject -> downstream "
    "destination -> retention/deletion receipt, plus browser/app permission and model-catalog change-management evidence. "
    "The public policy identifies the controller only as Monica / the Company; legal parent, registered jurisdiction, "
    "representative appointments, certifications, and product-risk classification remain verification questions rather than assumed facts. "
    "Offer: $500 fixed-scope 48-hour evidence-gap map or $497/month refresh. No email sent; SMTP remains gated."
)

repairs = [
    (
        ROOT / "cold_email" / "leads.csv",
        "index",
        {
            "index": INDEX,
            "name": "Monica",
            "handle": "@monicaim",
            "email": "contact@monica.im",
            "vertical": "ai_browser_extension",
            "tier": "1",
            "template": "744_monica_multi_llm_router_followup.md",
            "tier_reason": REASON,
        },
    ),
    (
        ROOT / "leads_with_emails.csv",
        "lead_index",
        {
            "lead_index": INDEX,
            "company": "Monica",
            "handle": "@monicaim",
            "domain": "monica.im",
            "website": "https://monica.im/",
            "founder": "Xiao Hong",
            "vertical": "ai_browser_extension",
            "tier": "1",
            "best_email": "contact@monica.im",
            "emails_found": "contact@monica.im",
            "guessed_emails": "",
            "source_template": "744_monica_multi_llm_router_followup.md",
            "tier_reason": REASON,
        },
    ),
]

for path, index_field, repaired_row in repairs:
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = reader.fieldnames
        rows = list(reader)
    cleaned_rows = []
    repaired_overflow = False
    for row in rows:
        extras = row.pop(None, None)
        if extras:
            repaired_overflow = True
            base = row.get("tier_reason", "")
            if base.startswith('"'):
                base = base[1:]
            merged = ",".join([base, *extras])
            if merged.endswith('"'):
                merged = merged[:-1]
            row["tier_reason"] = merged
            print(f"REPAIRED pre-existing CSV overflow in {path.name} row {row.get(index_field)}: {len(extras)} fields rejoined")
        cleaned_rows.append(row)
    rows = cleaned_rows
    matches = [position for position, row in enumerate(rows) if row.get(index_field) == INDEX]
    assert set(repaired_row) == set(fieldnames), f"{path.name}: schema mismatch"
    if not matches and not repaired_overflow:
        needs_newline = path.stat().st_size > 0 and path.read_bytes()[-1:] not in (b"\n", b"\r")
        with path.open("a", encoding="utf-8", newline="") as handle:
            if needs_newline:
                handle.write("\n")
            writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
            writer.writerow(repaired_row)
        print(f"APPENDED {path.name}: row {INDEX}, {len(fieldnames)} fields")
        continue
    if not matches:
        rows.append(repaired_row)
        action = "APPENDED"
    else:
        assert len(matches) == 1, f"{path.name}: expected one row {INDEX}, found {matches}"
        rows[matches[0]] = repaired_row
        action = "REPAIRED"
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(f"{action} {path.name}: row {INDEX}, {len(fieldnames)} fields")

(ROOT / "cold_email" / "tier_reason_744_monica.md").write_text(REASON + "\n", encoding="utf-8")
print("WROTE concise tier reason")
