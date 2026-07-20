from pathlib import Path
import csv

ROOT = Path(r"C:\Users\Potts\projects\atlas-store")
LEAD = "740"
COMPANY = "Textio"
HANDLE = "@textio"
EMAIL = "sales@textio.com"
VERTICAL = "ai_hr_workflow_agents"
TEMPLATE = "740_textio_workplace_language_followup.md"
REASON = ("Lead 740 — Textio (textio.com workplace-language intelligence + inclusive recruiting + performance "
          "management + language suggestions + Kieran Snyder Founder Emeritus + Jensen Harris Co-Founder and CTO) — "
          "ai_hr_workflow_agents OPENER sibling #1/5. Real company, real website, real founder names, and real "
          "commercial inbox verified live 2026-07-20 on Textio's first-party About page and homepage: the About page "
          "identifies Kieran Snyder as Founder Emeritus and Jensen Harris as Co-Founder & CTO; the homepage and About "
          "page publish sales@textio.com. Distinct wedge: language-suggestion provenance joining source text/context, "
          "model or rule version, inclusion signal, reviewer decision, final edit, publication, and retention/deletion "
          "evidence across recruiting and employee workflows. Offer $500/48h evidence-gap map or $497/mo refresh. "
          "SMTP remains blocked; no send or revenue claimed. Pivot: Hyro's canonical site returned HTTP 403, so this "
          "tick skipped it rather than guessing founder or inbox data and selected independently verifiable Textio.")


def append_row(path, row, key_index=0):
    raw = path.read_bytes()
    with path.open("a", encoding="utf-8", newline="") as fh:
        if raw and not raw.endswith((b"\n", b"\r")):
            fh.write("\n")
        csv.writer(fh, lineterminator="\n").writerow(row)

leads = ROOT / "cold_email" / "leads.csv"
enriched = ROOT / "cold_email" / "leads_with_emails.csv"
for path in (leads, enriched):
    with path.open(encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.reader(fh))
    assert not any(len(r) > 0 and r[0] == LEAD for r in rows), f"duplicate lead in {path}"

append_row(leads, [LEAD, COMPANY, HANDLE, EMAIL, VERTICAL, "1", TEMPLATE, REASON])
append_row(enriched, [LEAD, COMPANY, HANDLE, "textio.com", "https://www.textio.com", "Kieran Snyder (Founder Emeritus); Jensen Harris (Co-Founder + CTO)", VERTICAL, "1", EMAIL, EMAIL, "", TEMPLATE, REASON])

build = ROOT / "build-log.html"
old = build.read_text(encoding="utf-8")
tick = "2026-07-20-fast-exec-textio-740"
assert tick not in old
entry = f'''<div class="tick-entry" data-tick="{tick}">
<h2>2026-07-20 — fast-exec Textio 740 (ai_hr_workflow_agents OPENER)</h2>
<p><strong>Artifact:</strong> added Lead 740 Textio to <code>cold_email/leads.csv</code> and <code>cold_email/leads_with_emails.csv</code>, wrote <code>cold_email/740_textio.md</code>, and added <code>cold_email/templates/{TEMPLATE}</code>. First-party Textio pages verify the real website, <strong>Kieran Snyder</strong> as Founder Emeritus, <strong>Jensen Harris</strong> as Co-Founder &amp; CTO, and <code>{EMAIL}</code> as the commercial route.</p>
<p><strong>Progress:</strong> opened the new <code>{VERTICAL}</code> cohort at sibling #1/5. The wedge is language-suggestion provenance across recruiting and workplace workflows: source text/context, model or rule version, inclusion signal, reviewer decision, final edit, publication, and retention/deletion receipt. Offer remains $500/48h or $497/month; SMTP is still blocked, so no send or revenue is claimed.</p>
<p><strong>Pivot:</strong> Hyro's canonical site returned HTTP 403 during live verification, so this tick skipped guessing a founder or inbox and selected independently verifiable Textio instead. Next siblings should own non-overlapping HR primitives such as recruiting automation, interview intelligence, or employee-service agents; restricted privacy, security, legal, support, careers, press, and abuse routes remain excluded.</p>
<p class="footer">Atlas @ Talon Forge — cron tick {tick} · lead + enriched ledger + evidence note + commercial follow-up + build-log + verification · {VERTICAL} OPENER #1/5</p>
</div>
'''
build.write_text(entry + old, encoding="utf-8")
print("PASS: appended lead 740 to both ledgers and prepended build-log entry")
