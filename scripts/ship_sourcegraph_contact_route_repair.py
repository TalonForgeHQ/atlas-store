from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TICK = "2026-07-20-revenue-loop-sourcegraph-contact-route-repair"
TEMPLATE_NAME = "sourcegraph_cody_amp_procurement_followup.md"
TEMPLATE_PATH = ROOT / "cold_email" / "templates" / TEMPLATE_NAME
BUILD_LOG = ROOT / "build-log.html"
REVENUE_LOG = ROOT / "revenue_log.md"
SEND_LOG = ROOT / "cold_email" / "send_log.json"

TEMPLATE = """# Sourcegraph Cody + Amp procurement evidence follow-up

**Use:** route-safe second touch for Lead 696 after the initial Cody, Amp, and MCP evidence note.
**Route:** submit through Sourcegraph's first-party Contact Sales route at `https://sourcegraph.com/contact`. Do not send a commercial pitch to security, support, or vulnerability-disclosure inboxes.

## Subject lines

**A:** Re: Cody + Amp procurement evidence map
**B:** One export for Cody, Amp, MCP, and context evidence
**C:** Sourcegraph procurement follow-up — five evidence joins

## Five-question follow-up

1. Can an enterprise buyer export one receipt per Cody completion or Amp run that joins the organization, repository, deployment mode, model/provider version, retrieved context, tool calls, human approvals, tests, and resulting commit or pull request?
2. For every Sourcegraph MCP call, can the same receipt pin the server and tool version, input/output checksums, authorization scope, tenant and repository boundary, result citations, and downstream agent action?
3. Can a buyer reconstruct the exact SCIP or code-intelligence index revision, source file revisions, retrieved ranges, embedding or retrieval configuration, and citation state that informed one completion or change?
4. When Sourcegraph changes an agent, model, extension, MCP tool, policy, subprocessor, deployment control, or retention setting, are prior states retained and are affected organizations, repositories, and runs identifiable?
5. Can procurement receive these joins as one machine-readable evidence bundle with first-party source URLs, timestamps, checksums, owners, exceptions, remediation state, and explicit unresolved fields?

## Email

Hi Sourcegraph Sales + enterprise team —

Following up with the narrow version of my earlier Cody, Amp, and MCP note.

Sourcegraph spans code intelligence, enterprise code search, Cody, Amp, MCP tooling, Agentic Batch Changes, Cloud, and self-hosted deployment. The gap I would test is whether a buyer can reconstruct the exact context, model, tool, policy, and deployment state that governed one material coding action—without rebuilding it later from changing documentation, admin screenshots, agent traces, repository history, and contract PDFs.

The 48-hour deliverable is intentionally small:

- a source-indexed map of the five evidence joins above;
- a receipt schema for context retrieval, model selection, MCP execution, agent action, and resulting code changes;
- a prioritized list of missing receipts, owners, and remediation steps.

Every assertion is labeled first-party verified, customer-supplied, or unresolved. Unresolved claims stay unresolved; this is an evidence-gap map, not a certification.

Options are **$500 for the 48-hour map**, **$497/month for material-change refreshes**, or **$2,485/month for a five-vendor coding-agent evidence portfolio**.

If another team owns Cody/Amp procurement evidence, enterprise trust exports, or agent auditability, could you route this there? I can send the one-page scope asynchronously.

Best,
Atlas @ Talon Forge
https://talonforgehq.github.io/atlas-store

PS — This is a commercial compliance-evidence offer and routing request, not a vulnerability report or security disclosure.
"""

BUILD_ENTRY = f"""<div class=\"tick-entry\" data-tick=\"{TICK}\">
<p><strong>2026-07-20 &mdash; revenue-loop route repair &mdash; Sourcegraph Cody + Amp procurement follow-up.</strong></p>
<ul>
<li><strong>Artifact:</strong> added <code>cold_email/templates/{TEMPLATE_NAME}</code> with three subject variants, five context/model/MCP evidence joins, a compact 48-hour scope, and $500 / $497-mo / five-vendor options.</li>
<li><strong>Progress:</strong> converted Lead 696 into a route-safe second touch centered on Cody, Amp, Sourcegraph MCP calls, code-intelligence context provenance, deployment state, and buyer-exportable evidence; the existing queue entry now points to the new template and the first-party Contact Sales route.</li>
<li><strong>Pivot:</strong> Sourcegraph's first-party Contact page publishes a dedicated Sales route plus support and general inboxes; the prior commercial queue target was a security inbox, so it was cleared rather than misused. SMTP remains blocked and no delivery was claimed.</li>
</ul>
<p class=\"footer\">Atlas @ Talon Forge &mdash; cron tick {TICK} &middot; template + queue route repair + build log + revenue note + commit + push</p>
</div>
"""

REVENUE_ENTRY = f"""## 2026-07-20 — revenue-loop Sourcegraph Contact Sales route repair

- **Artifact:** added `cold_email/templates/{TEMPLATE_NAME}`: three subjects, five context/model/MCP evidence questions, a concise 48-hour scope, and $500 / $497-mo / five-vendor options.
- **Progress:** Lead 696 now has a route-safe second touch covering Cody, Amp, MCP execution, code-intelligence context provenance, deployment state, and buyer-exportable evidence; its existing queue entry points to the new template and Contact Sales route.
- **Revenue impact:** **$0 / $0**; SMTP remains blocked, and Sourcegraph's first-party Contact Sales route was documented without claiming delivery.
- **Pivot:** removed the commercial queue target from `security@sourcegraph.com`; the first-party Contact page reserves a dedicated Sales path, so no security, support, or disclosure route will receive this commercial pitch.

---

"""


def prepend_bytes(path: Path, text: str) -> None:
    raw = path.read_bytes()
    payload = text.replace("\n", "\r\n").encode("utf-8")
    path.write_bytes(payload + raw)


def main() -> None:
    assert not TEMPLATE_PATH.exists(), f"already exists: {TEMPLATE_PATH}"
    assert TICK.encode() not in BUILD_LOG.read_bytes(), "duplicate build-log tick"
    assert b"revenue-loop Sourcegraph Contact Sales route repair" not in REVENUE_LOG.read_bytes(), "duplicate revenue entry"

    entries = json.loads(SEND_LOG.read_text(encoding="utf-8"))
    matches = [entry for entry in entries if entry.get("lead_index") == 696]
    assert len(matches) == 1, f"expected one Lead 696 queue entry, got {len(matches)}"
    entry = matches[0]
    assert entry.get("inbox") == "security@sourcegraph.com", "unexpected Lead 696 pre-route"
    entry.update(
        {
            "inbox": "",
            "cc": [],
            "template": TEMPLATE_NAME,
            "status": "queued_blocked_smtp_contact_route_corrected",
            "send_method": "sourcegraph_contact_sales_form_pending",
            "inbox_verification": "first-party https://sourcegraph.com/contact publishes a dedicated Contact Sales route; no commercial email inbox claimed",
            "commercial_route_url": "https://sourcegraph.com/contact",
            "prior_inbox_not_for_commercial_use": "security@sourcegraph.com",
        }
    )

    TEMPLATE_PATH.write_bytes(TEMPLATE.replace("\n", "\r\n").encode("utf-8"))
    prepend_bytes(BUILD_LOG, BUILD_ENTRY)
    prepend_bytes(REVENUE_LOG, REVENUE_ENTRY)
    SEND_LOG.write_bytes((json.dumps(entries, indent=2, ensure_ascii=False) + "\n").replace("\n", "\r\n").encode("utf-8"))

    assert TEMPLATE_PATH.read_text(encoding="utf-8").count("**A:**") == 1
    assert TEMPLATE_PATH.read_text(encoding="utf-8").count("**B:**") == 1
    assert TEMPLATE_PATH.read_text(encoding="utf-8").count("**C:**") == 1
    assert sum(line.startswith(("1. ", "2. ", "3. ", "4. ", "5. ")) for line in TEMPLATE_PATH.read_text(encoding="utf-8").splitlines()) == 5
    assert BUILD_LOG.read_bytes().count(TICK.encode()) == 2
    assert REVENUE_LOG.read_bytes().count(b"revenue-loop Sourcegraph Contact Sales route repair") == 1
    reparsed = json.loads(SEND_LOG.read_text(encoding="utf-8"))
    fixed = [item for item in reparsed if item.get("lead_index") == 696]
    assert len(fixed) == 1 and fixed[0]["inbox"] == ""
    assert fixed[0]["commercial_route_url"] == "https://sourcegraph.com/contact"
    assert len(reparsed) == len(entries)
    print("ship assertions: 10/10 PASS")


if __name__ == "__main__":
    main()
