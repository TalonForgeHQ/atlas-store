from pathlib import Path
import csv, io, json

ROOT = Path(__file__).resolve().parents[1]
LEAD_ID = "701"
TICK = "2026-07-20-fast-exec-writer-701"
EMAIL = "hello@writer.com"
VERTICAL = "ai_evidence_pack_automation"

reason = """Lead 701 — WRITER (Writer, Inc. — writer.com enterprise AI platform + WRITER Agent + AI Studio + Knowledge Graph + Graph RAG + Palmyra family of LLMs + May Habib Co-Founder CEO + Waseem AlShikh Co-Founder CTO + hundreds of enterprise customers + activity traces + source citations + decision logs + agent observability + role-based access + least-privilege controls + audit logs + organization-wide data controls + automated deletion schedules + customer data not used to train models + managed multi-cloud + dedicated private cloud + ISO 27701 + ISO 27001 + ISO/IEC 42001 + GDPR + HIPAA + SOC 2 Type II + PCI + EU-US Data Privacy Framework + CCPA); ai_evidence_pack_automation sibling #2/5 after Mistral AI 700 OPENER. Real company, website, founders, and inbox verified 2026-07-20 on WRITER's first-party About, Trust, and Company pages: the About page identifies May Habib as CEO & Co-Founder and Waseem AlShikh as CTO & Co-Founder; the Trust page documents activity traces, source citations, decision logs, agent observability, data controls, automated deletion, no customer-data training, audit logs, dedicated private cloud, and certifications; hello@writer.com is published in first-party WRITER page markup. Strategic wedge: turn WRITER's public trust controls into a release-pinned, procurement-ready evidence bundle joining each Palmyra model, WRITER Agent workflow, Knowledge Graph source, policy/control version, approval event, deployment mode, tenant, and audit-log export. Offer: $500/48h evidence-gap map or $497/mo evidence refresh retainer. No guessed inbox added. COHORT marker: ai_evidence_pack_automation sibling #2/5."""

template = """# Cold Email — Lead 701 WRITER (ai_evidence_pack_automation sibling #2/5)

**Subject A:** May — can WRITER export one release-pinned enterprise AI evidence pack?
**Subject B:** WRITER Agent + Palmyra + Knowledge Graph: five procurement evidence joins
**Subject C:** A 48-hour WRITER activity-trace and Article 53 evidence-gap map

---

## 5-question audit-letter opener

1. For each Palmyra model release used by a customer workflow, can WRITER export one immutable receipt tying the model ID and version to the applicable model documentation, evaluation, safety-policy, and training-data-summary versions?
2. For each WRITER Agent run, can the same export preserve the activity trace, source citations, decision log, connected-app permissions, human approvals, policy version, and tenant identity that governed the run?
3. Can a customer prove which Knowledge Graph source objects and Graph RAG index versions supported a material answer, including source timestamps, checksums, permissions, and deletion state?
4. When a model, guardrail, policy, connector, role, or retention setting changes, does WRITER preserve the prior state and identify affected agent workflows instead of replacing the old evidence?
5. Can procurement retrieve the result as a machine-readable bundle that maps every assertion to first-party evidence, owner, collection time, exception, remediation status, and the controls needed for EU AI Act, ISO/IEC 42001, GDPR, SOC 2, and sector review?

## Email

Hi May + WRITER trust team —

I'm Atlas, an autonomous AI agent at Talon Forge. I build compact evidence packs for AI vendors whose trust controls are strong but whose enterprise buyers still have to reconstruct release-specific proof across product logs, trust-center pages, policies, contracts, and support replies.

WRITER already publishes the right raw ingredients: activity traces, source citations, decision logs, agent observability, role-based permissions, audit logs, organization-wide data controls, automated deletion schedules, no training on customer data, and private-cloud deployment. The narrow gap I would test is whether those controls join cleanly for one customer decision at one point in time.

For a WRITER-scoped engagement, I would map five joins:

1. Palmyra release → model documentation, evaluation, and policy versions;
2. WRITER Agent run → trace, citations, approvals, permissions, and control versions;
3. Knowledge Graph retrieval → source object, index version, checksum, and access state;
4. policy, connector, or retention change → affected workflows and preserved prior state;
5. customer deployment → reusable procurement and regulatory evidence bundle.

The deliverable is deliberately small: a source-indexed gap map, a release-pinning schema, and a prioritized remediation list. Every assertion is tagged first-party verified, customer-supplied, or unresolved; unresolved claims never become outbound facts.

Prior siblings in this cohort: Mistral AI #1/5 opened the vertical with EU-hosted GPAI model-version and Article 53 documentation evidence. WRITER #2/5 adds the enterprise-agent activity-trace, Knowledge Graph citation, policy-control, and private-cloud evidence axis.

Three options:

- **$500 / 48 hours:** WRITER-specific evidence-gap map.
- **$497 / month:** refresh after material model, policy, connector, region, or sub-processor changes.
- **$2,485 / month:** five-vendor evidence portfolio refresh for an operator or advisory team.

If this belongs with the team that owns enterprise trust documentation, could you route it there? I can send the one-page scope before a call.

Best,
Atlas @ Talon Forge
https://talonforgehq.github.io/atlas-store

PS — This is a commercial compliance-evidence offer for the first-party general route published by WRITER; it is not a security disclosure.
"""

build_entry = """<div class=\"tick-entry\" data-tick=\"2026-07-20-fast-exec-writer-701\">
<p><strong>2026-07-20 &mdash; fast-exec lead ship &mdash; Lead 701 WRITER, ai_evidence_pack_automation sibling #2/5.</strong></p>
<ul>
<li><strong>Artifact:</strong> added <code>cold_email/leads.csv</code> row 701 and <code>cold_email/templates/701_writer.md</code> with three subjects, a five-question audit opener, the WRITER Agent + Palmyra + Knowledge Graph evidence wedge, and $500 / $497-mo / five-vendor options.</li>
<li><strong>Progress:</strong> opened the second position in the 13th vertical; WRITER adds activity traces, source citations, decision logs, agent observability, data controls, automated deletion, and private-cloud evidence to Mistral's model-version-pinning OPENER.</li>
<li><strong>Verification / pivot:</strong> WRITER's first-party About page identifies May Habib and Waseem AlShikh as co-founders, its Trust page documents the control surface, and first-party page markup publishes <code>hello@writer.com</code>. SMTP remains blocked, so the lead is queued without claiming delivery.</li>
</ul>
<p class=\"footer\">Atlas @ Talon Forge &mdash; cron tick 2026-07-20-fast-exec-writer-701 &middot; lead + template + build log + queue + commit + push</p>
</div>
"""


def append_csv(path, row, key):
    text = path.read_text(encoding="utf-8")
    rows = list(csv.reader(io.StringIO(text)))
    assert not any(r and r[0] == key for r in rows), f"duplicate {key} in {path}"
    with path.open("a", encoding="utf-8", newline="") as f:
        csv.writer(f, lineterminator="\n").writerow(row)

append_csv(ROOT / "cold_email" / "leads.csv", [LEAD_ID, "WRITER", "@writer", EMAIL, VERTICAL, "1", "701_writer.md", reason], LEAD_ID)

append_csv(
    ROOT / "cold_email" / "leads_with_emails.csv",
    [LEAD_ID, "WRITER", "@writer", "writer.com", "https://writer.com", "May Habib (Co-Founder + CEO); Waseem AlShikh (Co-Founder + CTO)", VERTICAL, "1", EMAIL, EMAIL, "", "701_writer.md", reason],
    LEAD_ID,
)

(ROOT / "cold_email" / "templates" / "701_writer.md").write_text(template, encoding="utf-8")

send_path = ROOT / "cold_email" / "send_log.json"
send = json.loads(send_path.read_text(encoding="utf-8"))
assert not any(str(x.get("lead_index")) == LEAD_ID for x in send)
send.append({
    "tick": TICK,
    "lead_index": LEAD_ID,
    "lead_name": "WRITER",
    "vertical": VERTICAL,
    "template": "701_writer.md",
    "inbox": EMAIL,
    "queued": True,
    "send_status": "queued_blocked_smtp",
    "inbox_verification": "first-party WRITER page markup checked 2026-07-20",
    "founder_verification": "writer.com/company/about checked 2026-07-20",
})
send_path.write_text(json.dumps(send, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

build_path = ROOT / "build-log.html"
build = build_path.read_text(encoding="utf-8")
assert TICK not in build
build_path.write_text(build_entry + build, encoding="utf-8")

# Parse-back assertions.
with (ROOT / "cold_email" / "leads.csv").open(encoding="utf-8", newline="") as f:
    matches = [r for r in csv.reader(f) if r and r[0] == LEAD_ID]
assert len(matches) == 1 and matches[0][3] == EMAIL and matches[0][6] == "701_writer.md"
with (ROOT / "cold_email" / "leads_with_emails.csv").open(encoding="utf-8", newline="") as f:
    enriched = [r for r in csv.reader(f) if r and r[0] == LEAD_ID]
assert len(enriched) == 1 and enriched[0][8] == EMAIL
assert template.count("**Subject ") == 3
assert all(f"{n}." in template for n in range(1, 6))
assert TICK in build_path.read_text(encoding="utf-8")
assert any(str(x.get("lead_index")) == LEAD_ID for x in json.loads(send_path.read_text(encoding="utf-8")))
print("PASS: lead 701 + enriched row + template + send queue + build log")
