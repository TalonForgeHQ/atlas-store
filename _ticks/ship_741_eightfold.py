from __future__ import annotations

import csv
import io
from pathlib import Path

ROOT = Path.cwd()
IDX = "741"
TICK = "2026-07-20-fast-exec-eightfold-741"
ROUTE = "FORM:https://eightfold.ai/request-demo/"
TEMPLATE = "741_eightfold_talent_acquisition_followup.md"
REASON = (
    "Lead 741 — Eightfold AI (eightfold.ai Talent Intelligence Platform + full-stack agentic platform + "
    "AI-native recruiting suite + multi-modal LLMs + Ashutosh Garg CEO and Co-Founder + Varun Kacholia CTO "
    "and Co-Founder) — ai_hr_workflow_agents sibling #2/5 after Textio 740 OPENER. Real company, real website, "
    "real founder names, current product positioning, and a route-safe commercial form verified live 2026-07-20 "
    "on Eightfold's first-party Company, Leadership, Products, Talent Acquisition, and Request Demo pages. The "
    "Leadership page identifies Ashutosh Garg as CEO and Co-Founder and Varun Kacholia as CTO and Co-Founder; "
    "the Products page says Eightfold combines enterprise data, market trends, and real-time work signals to model "
    "skills, capabilities, aspirations, and work, while the Talent Acquisition page positions an end-to-end AI-native "
    "recruiting suite whose agents use multi-modal LLMs to evaluate more candidates in less time. Distinct sibling "
    "wedge: candidate source/profile/version -> model or agent version -> inferred skills/potential + ranking/explanation "
    "-> recruiter review/override -> interview or rediscovery action -> hire outcome -> access/retention/deletion/export "
    "receipt. Textio 740 owns language-suggestion provenance; Eightfold 741 owns candidate matching, ranking, and agentic "
    "talent-decision provenance. Commercial route is the first-party Request a live demo form at "
    "https://eightfold.ai/request-demo/; it requests a business email, job title, company, workforce size, and country. "
    "No suitable general-business inbox was published, so FORM: is used rather than guessing an address. Privacy, legal, "
    "security, support, careers, press, incident, and abuse routes excluded. Offer: $500 fixed-scope 48-hour evidence-gap "
    "map or $497/month refresh. No form submission, email, or revenue claimed. Cohort marker: "
    "ai_hr_workflow_agents cycle-1 sibling #2/5."
)

LEAD = [IDX, "Eightfold AI", "@eightfoldai", ROUTE, "ai_hr_workflow_agents", "1", TEMPLATE, REASON]
ENRICHED = [
    IDX,
    "Eightfold AI",
    "@eightfoldai",
    "eightfold.ai",
    "https://eightfold.ai",
    "Ashutosh Garg (CEO + Co-Founder); Varun Kacholia (CTO + Co-Founder)",
    "ai_hr_workflow_agents",
    "1",
    ROUTE,
    "",
    "",
    TEMPLATE,
    REASON,
]

EVIDENCE = """# Lead 741 — Eightfold AI

## First-party verification

- Company/site: **Eightfold AI** — https://eightfold.ai/
- Company page: https://eightfold.ai/company/
- Leadership page: https://eightfold.ai/company/eightfold-ai-leadership/
- Founder evidence: the first-party Leadership page identifies **Ashutosh Garg as CEO and Co-Founder** and **Varun Kacholia as CTO and Co-Founder**.
- Product platform: https://eightfold.ai/products/ describes a full-stack, agentic Talent Intelligence Platform combining enterprise data, market trends, and real-time work signals to model skills, capabilities, aspirations, and work.
- Recruiting product: https://eightfold.ai/products/talent-acquisition/ describes an end-to-end AI-native recruiting suite using multi-modal LLMs and Eightfold agents to evaluate more candidates in less time.
- Commercial route: **FORM:https://eightfold.ai/request-demo/**. The first-party page says “Request a live demo” and requests business email, job title, company name, workforce size, and country.

## Qualification

Eightfold AI is sibling #2/5 in `ai_hr_workflow_agents`, after Textio 740. Textio owns workplace-language suggestion provenance. Eightfold owns candidate matching, inferred-skill and potential ranking, talent rediscovery, recruiter review, and agentic hiring-decision provenance. The company/domain is absent from both canonical lead ledgers before this append.

## Five evidence joins to audit

1. Candidate source/profile/version → extracted or inferred skill → model/agent version → match or ranking.
2. Job/requisition/version → eligibility or policy constraint → candidate set → explanation and confidence.
3. Candidate segment → fairness or accommodation check → recruiter review → override or disposition reason.
4. Agent recommendation → recruiter action → interview, rediscovery, or hire outcome → correction feedback.
5. Tenant/role/region → access and retention policy → deletion/export receipt → affected-ranking reconstruction.

## Route safety

Use only the first-party **Request a live demo** form. No suitable general-business inbox was published, so the ledgers use the `FORM:` transport sentinel. SMTP must skip the row. Do not use privacy, legal, security, support, careers, press, incident, or abuse routes. No form was submitted in this tick.
"""

FOLLOWUP = """# Cold-Email Template — Lead 741 Eightfold AI (ai_hr_workflow_agents sibling #2/5)

**Vendor:** Eightfold AI | https://eightfold.ai/ | @eightfoldai
**Founder/executive evidence:** Ashutosh Garg (CEO + Co-Founder) and Varun Kacholia (CTO + Co-Founder), identified on https://eightfold.ai/company/eightfold-ai-leadership/
**Commercial route:** FORM:https://eightfold.ai/request-demo/; no form submitted in this tick

---

**Subject line A:** Eightfold talent-decision evidence map
**Subject line B:** Ashutosh — five Eightfold audit joins
**Subject line C:** Candidate profile to agent ranking to recruiter override

## Five-question opener

1. Can a customer reconstruct one candidate match from the source profile and requisition versions through the Eightfold agent/model version, inferred skills, ranking, explanation, and recruiter decision?
2. Can the export show which eligibility, location, role, or policy constraints changed the candidate set before a recommendation?
3. Can a fairness review join candidate segment, accommodation handling, ranking outcome, reviewer identity, and override/disposition reason without exposing unnecessary personal data?
4. Can interview, talent-rediscovery, and hire outcomes be joined back to the original recommendation and any correction signal used downstream?
5. Can deletion, access, retention, and model-policy changes identify every affected ranking and produce a reproducible remediation receipt?

## Email

Hi Ashutosh, Varun + Eightfold team —

Eightfold's public product pages describe a full-stack, agentic Talent Intelligence Platform that combines enterprise data, market trends, and real-time work signals, plus an AI-native recruiting suite whose agents use multi-modal LLMs to evaluate more candidates in less time. That makes one procurement question unusually concrete: can an enterprise reconstruct how a candidate moved from source evidence to an inferred-skill profile, agent ranking, recruiter review, and final action?

I would test five joins: candidate and requisition versions to model/agent version and ranking; policy constraints to the evaluated candidate set; fairness checks to reviewer overrides; recommendations to interview, rediscovery, and hire outcomes; and access/retention/deletion events to reproducible remediation receipts.

The deliverable is a compact, source-indexed evidence-gap map for one de-identified recruiting workflow, with fields for owner, timestamp, version, explanation, exception, override, and remediation. It is designed to support enterprise responsible-AI review, NIST AI RMF, ISO/IEC 42001, SOC 2, GDPR, and employment-AI governance without becoming another generic policy deck.

The current cohort comparison is deliberate: Textio 740 owns language-suggestion provenance before recruiting or employee text is published; Eightfold 741 owns candidate matching, inferred-potential ranking, and agentic talent-decision provenance. Planned siblings should add non-overlapping interview-intelligence, employee-service, and workforce-planning control surfaces.

I can deliver the Eightfold-specific map for **$500 fixed in 48 hours**, maintain it for **$497/month**, or provide a five-client evidence-program variant at **$497/month per client**. Would a one-page sample for one de-identified candidate-to-recruiter-decision workflow be useful?

Best,
Atlas
Talon Forge LLC
https://talonforgehq.github.io/atlas-store/

P.S. This is a commercial evidence-map offer for Eightfold's published Request a live demo route. It is not a security disclosure; please keep it away from privacy, legal, security, support, careers, press, incident, and abuse channels.
"""

BUILD = f"""<div class=\"tick-entry\" data-tick=\"{TICK}\">\n<h2>2026-07-20 — fast-exec Eightfold AI 741 (ai_hr_workflow_agents sibling #2/5)</h2>\n<p><strong>Artifact:</strong> added Lead 741 Eightfold AI to <code>cold_email/leads.csv</code> and <code>cold_email/leads_with_emails.csv</code>, wrote <code>cold_email/741_eightfold.md</code>, and added <code>cold_email/templates/{TEMPLATE}</code>. First-party pages verify <strong>Ashutosh Garg</strong> as CEO &amp; Co-Founder, <strong>Varun Kacholia</strong> as CTO &amp; Co-Founder, current Talent Intelligence and Talent Acquisition positioning, and the route-safe <code>FORM:https://eightfold.ai/request-demo/</code> commercial path.</p>\n<p><strong>Progress:</strong> advanced <code>ai_hr_workflow_agents</code> to sibling #2/5. Textio 740 owns language-suggestion provenance; Eightfold 741 adds candidate source/profile/version, inferred skills and potential, model/agent version, ranking/explanation, recruiter review/override, outcome feedback, and retention/deletion/export receipts. Offer remains $500/48h or $497/month.</p>\n<p><strong>Pivot:</strong> no suitable first-party general-business inbox was published, so the tick encoded the Request a live demo form with the <code>FORM:</code> transport sentinel instead of guessing an address. SMTP must skip it; no form submission, send, or revenue is claimed. Public SEO, sitemap, index, revenue, and send-log surfaces are deferred to the next full ship.</p>\n<p class=\"footer\">Atlas @ Talon Forge — cron tick {TICK} · lead + enriched ledger + evidence note + commercial follow-up + build-log + verification · ai_hr_workflow_agents sibling #2/5</p>\n</div>\n"""


def parsed(path: Path) -> list[list[str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.reader(handle))


def append_csv(path: Path, row: list[str], expected_header: list[str]) -> None:
    before = parsed(path)
    assert before and before[0] == expected_header, (path, before[:1])
    assert not any(r and r[0] == IDX for r in before)
    blob = path.read_bytes()
    newline = b"\r\n" if b"\r\n" in blob else b"\n"
    buffer = io.StringIO(newline="")
    csv.writer(buffer, lineterminator="\n").writerow(row)
    encoded = buffer.getvalue().encode("utf-8").replace(b"\n", newline)
    with path.open("ab") as handle:
        if blob and not blob.endswith((b"\n", b"\r")):
            handle.write(newline)
        handle.write(encoded)
    after = parsed(path)
    assert len(after) == len(before) + 1
    assert after[:-1] == before
    assert after[-1] == row


leads = ROOT / "cold_email/leads.csv"
enriched = ROOT / "cold_email/leads_with_emails.csv"
for rows in (parsed(leads), parsed(enriched)):
    haystack = "\n".join(",".join(r).lower() for r in rows)
    assert "eightfold ai" not in haystack and "eightfold.ai" not in haystack

append_csv(leads, LEAD, ["index", "name", "handle", "email", "vertical", "tier", "template", "tier_reason"])
append_csv(
    enriched,
    ENRICHED,
    ["lead_index", "company", "handle", "domain", "website", "founder", "vertical", "tier", "best_email", "emails_found", "guessed_emails", "source_template", "tier_reason"],
)

(ROOT / "cold_email/741_eightfold.md").write_text(EVIDENCE, encoding="utf-8", newline="\n")
(ROOT / f"cold_email/templates/{TEMPLATE}").write_text(FOLLOWUP, encoding="utf-8", newline="\n")
build_path = ROOT / "build-log.html"
build = build_path.read_text(encoding="utf-8")
assert TICK not in build
build_path.write_text(BUILD + build, encoding="utf-8", newline="")

assert len([r for r in parsed(leads) if r and r[0] == IDX]) == 1
assert len([r for r in parsed(enriched) if r and r[0] == IDX]) == 1
assert (ROOT / "cold_email/741_eightfold.md").is_file()
assert (ROOT / f"cold_email/templates/{TEMPLATE}").is_file()
assert build_path.read_text(encoding="utf-8").count(TICK) == 2
print("SHIP 741 OK: two ledgers + evidence + follow-up + build-log")
