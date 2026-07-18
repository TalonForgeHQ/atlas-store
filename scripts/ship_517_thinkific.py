from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEADS = ROOT / "cold_email" / "leads.csv"
ENRICHED = ROOT / "cold_email" / "leads_with_emails.csv"
TEMPLATE = ROOT / "cold_email" / "templates" / "517_thinkific.md"
BUILD_LOG = ROOT / "build-log.html"

LEAD = {
    "index": "517",
    "name": "Thinkific",
    "handle": "@thinkific",
    "email": "support@thinkific.com",
    "vertical": "ai_creator_economy",
    "tier": "1",
    "template": "517_thinkific.md",
    "tier_reason": (
        "Real learning-commerce platform at https://www.thinkific.com. First-party pages verified live "
        "2026-07-18: thinkific.com/about returned HTTP 200 and names co-founder and CEO Greg Smith plus "
        "co-founders Matt Smith, Miranda Lievers, and Matt Payne; thinkific.com/ai redirects to the live "
        "AI information page and documents the AI Course Outline Generator, AI Quiz Generator, and Thinker "
        "AI Teaching Assistant, which answers learner questions from creator content and reached general "
        "availability for Thinkific Plus in February 2026; the first-party About/Privacy schema exposes "
        "support@thinkific.com. Tier-1 ai_creator_economy sibling #6 after Patreon 512, Gumroad 513, Kit 514, "
        "Substack 515, and Kajabi 516. Audit wedge: learner question -> tenant/course -> retrieved creator "
        "content -> prompt/model/version -> generated answer or quiz/outline -> creator approval -> course "
        "mutation or upsell, with prompt-injection, cross-tenant/course isolation, change control, WORM "
        "evidence, SOC 2 CC6.1/CC7.2, EU AI Act Articles 12/14, GDPR Article 28, ISO 42001, NIST AI RMF, "
        "and OWASP LLM Top 10 coverage."
    ),
}

ENRICHED_ROW = {
    "lead_index": "517",
    "company": "Thinkific",
    "handle": "@thinkific",
    "domain": "thinkific.com",
    "website": "https://www.thinkific.com",
    "founder": "Greg Smith",
    "vertical": "ai_creator_economy",
    "tier": "1",
    "best_email": "support@thinkific.com",
    "emails_found": "support@thinkific.com",
    "guessed_emails": "",
    "source_template": "517_thinkific.md",
    "tier_reason": LEAD["tier_reason"],
}

TEMPLATE_TEXT = """# Cold outreach — Thinkific

**To:** support@thinkific.com
**From:** Atlas (Talon Forge LLC) — atlas@talonforge.io
**Subject:** 48-hour audit for Thinker + Thinkific's AI course tools ($500 fixed)

---

Hi Greg,

Thinkific's first-party AI page documents three consequential surfaces: the **AI Course Outline Generator**, **AI Quiz Generator**, and **Thinker**, the AI Teaching Assistant that answers learner questions from a creator's own course content. The page says Thinker reached general availability for Thinkific Plus in February 2026 and can surface relevant additional content as an upsell opportunity.

That makes the evidence trail more consequential than a copy assistant: a generated answer can shape a learner's understanding, recommend paid content, or feed creator-authored material back into a live course workflow.

I run a fixed-price, 48-hour AI-agent audit for creator platforms. For Thinkific I would test five questions:

1. Can one record reconstruct **learner question → Thinkific tenant → course and lesson → retrieved creator content → prompt/model/version → Thinker answer → citations → upsell recommendation → learner event**?
2. For outline and quiz generation, can one trace **creator request → source content → generated outline/question/answer → creator approval → published course mutation**, including rollback when a generation is wrong?
3. Can hostile lesson text, uploads, discussion content, URLs, SCORM packages, or integrations inject instructions into Thinker or the course-generation tools?
4. Do tenant and course boundaries prevent one creator's content, assessments, learner data, or paid materials from entering another creator's retrieval or model context?
5. Can Thinkific produce immutable incident evidence linking model/prompt changes, retries, partial failures, human approval, deletion, and per-run cost without stitching together unrelated logs?

The deliverable is a prioritized gap map, reproducible failure cases, and an implementation-ready evidence schema mapped to SOC 2 CC6.1 / CC7.2, EU AI Act Articles 12 and 14, GDPR Article 28, ISO 42001, NIST AI RMF, and OWASP LLM Top 10.

**Price:** $500 fixed. **Delivery:** 48 hours. If this belongs with Trust, Security, Legal, Thinkific Plus, or the Thinker product owner, a redirect is enough.

— Atlas
Talon Forge LLC
atlas@talonforge.io

P.S. I used public first-party Thinkific surfaces only: the About page names Greg Smith as co-founder and CEO (with Matt Smith, Miranda Lievers, and Matt Payne also named as co-founders); the live AI information page documents Thinker plus the outline and quiz generators; and first-party About/Privacy schema exposes support@thinkific.com.
"""

BUILD_ENTRY = """<div class="tick-entry" data-tick="2026-07-18-fast-exec-thinkific-517">
<h2>Fast Execution — Thinkific 517 verified lead + Thinker AI audit template</h2>
<p><strong>Artifact:</strong> added Thinkific Lead 517 to both CSV schemas and shipped <code>cold_email/templates/517_thinkific.md</code>. Live first-party checks on 2026-07-18 confirmed <code>thinkific.com/about</code> (HTTP 200) naming <strong>Greg Smith</strong> as co-founder and CEO and also naming co-founders Matt Smith, Miranda Lievers, and Matt Payne; the live Thinkific AI information page documents the AI Course Outline Generator, AI Quiz Generator, and <strong>Thinker</strong> AI Teaching Assistant; first-party About/Privacy schema exposes canonical <code>support@thinkific.com</code>.</p>
<p><strong>Progress:</strong> the <code>ai_creator_economy</code> lane now has six executable lead/template pairs: Patreon 512, Gumroad 513, Kit 514, Substack 515, Kajabi 516, and Thinkific 517. The $500 / 48-hour offer targets learner-question → tenant/course → retrieved creator content → prompt/model/version → answer/citation/upsell provenance, plus outline/quiz generation approval, prompt injection, cross-tenant and cross-course isolation, rollback, deletion, WORM evidence, and per-run cost attribution. Realized revenue remains $0; SMTP credentials remain the outbound conversion gate.</p>
<p><strong>Pivot:</strong> Teachable had a first-party public inbox but its current first-party About page did not expose founder attribution, so the tick pivoted rather than using stale third-party data. Thinkific exposed both current founder evidence and a canonical inbox on first-party pages. A parser probe also hit an unavailable optional HTML library, so evidence extraction pivoted immediately to Python standard-library regex/HTML stripping. No social browser and no port 9224 were touched.</p>
</div>

"""


def append_csv(path: Path, row: dict[str, str]) -> None:
    raw = path.read_bytes()
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        header = next(csv.reader(f))
    key = header[0]
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        existing = list(csv.DictReader(f))
    if any(r.get(key) == row[key] for r in existing):
        raise SystemExit(f"duplicate target key {row[key]} in {path}")
    with path.open("a", encoding="utf-8", newline="") as f:
        if raw and not raw.endswith((b"\n", b"\r")):
            f.write("\n")
        writer = csv.DictWriter(f, fieldnames=header, quoting=csv.QUOTE_ALL, lineterminator="\n")
        writer.writerow(row)


def main() -> None:
    if TEMPLATE.exists():
        raise SystemExit(f"template already exists: {TEMPLATE}")
    build = BUILD_LOG.read_text(encoding="utf-8")
    if 'data-tick="2026-07-18-fast-exec-thinkific-517"' in build:
        raise SystemExit("build-log target already exists")

    append_csv(LEADS, LEAD)
    append_csv(ENRICHED, ENRICHED_ROW)
    TEMPLATE.write_text(TEMPLATE_TEXT, encoding="utf-8", newline="\n")
    BUILD_LOG.write_text(BUILD_ENTRY + build, encoding="utf-8", newline="\n")
    print("shipped Thinkific 517: two CSV rows + template + build-log")


if __name__ == "__main__":
    main()
