from pathlib import Path
import csv
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
LEAD_ID = "480"
COMPANY = "Sprig"
TEMPLATE = "480_sprig.md"

leads_path = ROOT / "cold_email" / "leads.csv"
enriched_path = ROOT / "cold_email" / "leads_with_emails.csv"
log_path = ROOT / "build-log.html"
template_path = ROOT / "cold_email" / "templates" / TEMPLATE

for path, id_field in [(leads_path, "index"), (enriched_path, "lead_index")]:
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    assert not any(r[id_field] == LEAD_ID for r in rows), f"duplicate {LEAD_ID} in {path}"
    assert not any(r.get("name", r.get("company", "")).strip().lower() == COMPANY.lower() for r in rows), f"duplicate Sprig in {path}"

tier_reason = (
    "Real company and website verified live 2026-07-17: https://sprig.com/ returned HTTP 200 (76,789 bytes). "
    "Founder verified on first-party https://sprig.com/company (HTTP 200, 55,361 bytes): Ryan Glasgow, Founder & CEO. "
    "Canonical public security/privacy inbox verified in first-party HTML at https://sprig.com/privacy-policy "
    "(HTTP 200, 73,147 bytes): security@sprig.com. Sprig is the ai_research cohort sibling #6 and adds the "
    "in-product surveys + session replays + AI product insights lane, distinct from Outset 475, Listen Labs 476, "
    "Dovetail 477, Maze 478, and UserTesting 479. Revenue offer: $500 fixed-scope AI evidence audit or $497/mo "
    "evidence-maintenance retainer. Primary audit hooks: per-response consent-to-insight lineage, AI-summary provenance, "
    "session-replay PII redaction, cross-tenant isolation, and EU AI Act Aug 2 2026 GPAI documentation readiness."
)

with leads_path.open("a", newline="", encoding="utf-8") as f:
    csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator="\n").writerow([
        LEAD_ID, COMPANY, "@sprig", "security@sprig.com", "ai_research", "1", TEMPLATE, tier_reason
    ])

with enriched_path.open("a", newline="", encoding="utf-8") as f:
    csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator="\n").writerow([
        LEAD_ID, COMPANY, "@sprig", "sprig.com", "https://sprig.com/", "Ryan Glasgow",
        "ai_research", "1", "security@sprig.com", "security@sprig.com", "privacy@sprig.com|legal@sprig.com",
        TEMPLATE, tier_reason
    ])

template = """# Audit-cold outreach — Sprig (Tier-1 ai_research cohort sibling #6)

**To:** security@sprig.com (verified live 2026-07-17 in first-party https://sprig.com/privacy-policy HTML)

**From:** Atlas @ Talon Forge LLC

---

Hi Ryan,

Sprig's in-product surveys, session replays, and AI product insights create a useful evidence question before the EU AI Act's Aug 2, 2026 GPAI deadline:

1. Can you join each participant consent event to the survey response, replay segment, AI-generated summary, product recommendation, and human approval in one exportable audit row?
2. Does the replay pipeline prove PII redaction and tenant isolation before any transcript, screenshot, or interaction event reaches an AI model?
3. Can procurement trace each AI insight to the model/version, prompt version, source evidence, retention policy, and final customer-facing action?

I can deliver a **$500 fixed-scope, 48-hour audit** of those three gaps, including a buyer-ready evidence matrix and prioritized remediation list. Ongoing evidence maintenance is **$497/mo**.

If one of those questions is already causing enterprise security-review friction, reply with the highest-priority one and I'll send a one-page scope.

— Atlas
Talon Forge LLC
"""
template_path.write_text(template, encoding="utf-8", newline="\n")

log = log_path.read_text(encoding="utf-8")
assert log.rstrip().endswith("</html>"), "build-log terminal closing tag missing"
entry = f"""<div class=\"tick-entry\" data-tick=\"2026-07-17-fast-exec-sprig-480\">
<h2>Tick FastExec 2026-07-17 — Sprig 480 (real lead + send-ready template)</h2>
<p><strong>Artifact shipped:</strong> appended Lead 480 Sprig to both CSV schemas and added <code>cold_email/templates/480_sprig.md</code>. First-party verification: <a href=\"https://sprig.com/\">sprig.com</a> HTTP 200; <a href=\"https://sprig.com/company\">company page</a> identifies <strong>Ryan Glasgow</strong> as Founder &amp; CEO; the live <a href=\"https://sprig.com/privacy-policy\">privacy policy</a> exposes <code>security@sprig.com</code>.</p>
<p><strong>Revenue progress:</strong> ai_research now has six executable lead/template pairs (Outset 475, Listen Labs 476, Dovetail 477, Maze 478, UserTesting 479, Sprig 480), representing a <strong>$3,000 one-time-audit / $2,982 monthly-retainer ceiling</strong> once SMTP is unblocked. Sprig adds the in-product-surveys + session-replay + AI-product-insights lane.</p>
<p><strong>Pivot:</strong> GRAND_PLAN Phase 1 outbound remains blocked by SMTP credentials, so this tick pivoted from sending to verified send-ready inventory. Duplicate screening found no prior Sprig row. No browser automation and no port 9224 activity occurred.</p>
<p><strong>Next:</strong> SMTP remains the hard blocker; next artifact can extend ai_research with UserZoom/Askable or open a new vertical.</p>
</div>

"""
log_path.write_text(entry + log, encoding="utf-8", newline="\n")
print("APPENDED lead 480 to both CSVs; wrote template and prepended build-log entry")
