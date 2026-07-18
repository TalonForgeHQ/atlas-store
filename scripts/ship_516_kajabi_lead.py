#!/usr/bin/env python3
"""Append verified Kajabi lead 516 to both CSV schemas and prepend build-log."""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = "516"
TICK = "2026-07-18-fast-exec-kajabi-516"
TEMPLATE = "516_kajabi.md"
SOURCE = ROOT / "cold_email" / "leads.csv"
ENRICHED = ROOT / "cold_email" / "leads_with_emails.csv"
BUILD_LOG = ROOT / "build-log.html"
TEMPLATE_PATH = ROOT / "cold_email" / "templates" / TEMPLATE

REASON = (
    "Real creator-business platform at https://www.kajabi.com. First-party Kajabi pages were "
    "verified live 2026-07-18: kajabi.com/about returned HTTP 200; the first-party Impact Summit "
    "article identifies Kenny Rueter as Kajabi's founder; kajabi.com/product/cofounder returned "
    "HTTP 200 and describes Kajabi Cofounder as an AI business partner; the live sitemap exposes "
    "the Kajabi MCP membership-team workflow; kajabi.com/policies/privacy returned HTTP 200 and "
    "exposes privacy@kajabi.com plus support@kajabi.com. Tier-1 ai_creator_economy sibling #5 "
    "after Patreon 512, Gumroad 513, Kit 514, and Substack 515. Audit wedge: creator request -> "
    "tenant -> Cofounder session -> retrieved context -> model/prompt version -> recommendation -> "
    "MCP tool call -> human approval -> Kajabi object mutation -> payment/message side effect, with "
    "prompt-injection, cross-tenant isolation, change control, rollback, deletion, WORM evidence, "
    "SOC 2 CC6.1/CC7.2, EU AI Act Articles 12/14, GDPR Article 28, ISO 42001, NIST AI RMF, and "
    "OWASP LLM Top 10 coverage."
)

SOURCE_ROW = {
    "index": INDEX,
    "name": "Kajabi",
    "handle": "@Kajabi",
    "email": "privacy@kajabi.com",
    "vertical": "ai_creator_economy",
    "tier": "1",
    "template": TEMPLATE,
    "tier_reason": REASON,
}

ENRICHED_ROW = {
    "lead_index": INDEX,
    "company": "Kajabi",
    "handle": "@Kajabi",
    "domain": "kajabi.com",
    "website": "https://www.kajabi.com",
    "founder": "Kenny Rueter",
    "vertical": "ai_creator_economy",
    "tier": "1",
    "best_email": "privacy@kajabi.com",
    "emails_found": "privacy@kajabi.com;support@kajabi.com",
    "guessed_emails": "",
    "source_template": TEMPLATE,
    "tier_reason": REASON,
}

ENTRY = f'''<div class="tick-entry" data-tick="{TICK}">
<h2>Fast Execution — Kajabi 516 verified lead + Cofounder/MCP template</h2>
<p><strong>Artifact:</strong> added Kajabi Lead 516 to both CSV schemas and shipped <code>cold_email/templates/516_kajabi.md</code>. Live first-party checks on 2026-07-18 confirmed <code>kajabi.com/about</code> (HTTP 200), a Kajabi Impact Summit article that identifies <strong>Kenny Rueter</strong> as Kajabi's founder, <code>kajabi.com/product/cofounder</code> describing Cofounder as an AI business partner, the live sitemap's Kajabi MCP membership-team case study, and <code>kajabi.com/policies/privacy</code> exposing canonical <code>privacy@kajabi.com</code> plus <code>support@kajabi.com</code>.</p>
<p><strong>Progress:</strong> the <code>ai_creator_economy</code> lane now has five executable lead/template pairs: Patreon 512, Gumroad 513, Kit 514, Substack 515, and Kajabi 516. The $500 / 48-hour offer targets creator-request → Cofounder context → model/prompt version → recommendation → MCP tool call → approval → Kajabi object mutation → payment/message-side-effect provenance, plus prompt-injection, tenant isolation, change control, rollback, deletion, WORM evidence, and per-run cost attribution. Realized revenue remains $0; SMTP credentials remain the outbound conversion gate.</p>
<p><strong>Pivot:</strong> the first-party Kajabi About page did not expose a founder name, so founder verification pivoted to Kajabi's own Impact Summit history article instead of relying on stale third-party profiles. The initial inbox scan also found no address on About; the first-party Privacy Notice exposed <code>privacy@kajabi.com</code> and <code>support@kajabi.com</code>, avoiding a guessed route. No social browser and no port 9224 were touched.</p>
</div>
'''


def append_row(path: Path, index_field: str, row: dict[str, str]) -> None:
    with path.open("r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        fieldnames = reader.fieldnames
        assert fieldnames, f"missing header: {path}"
        existing = list(reader)
    assert not any(r.get(index_field) == INDEX for r in existing), f"duplicate {INDEX} in {path}"
    assert set(row) == set(fieldnames), f"schema mismatch for {path}"
    with path.open("a", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, quoting=csv.QUOTE_ALL, lineterminator="\n")
        writer.writerow(row)


assert TEMPLATE_PATH.exists(), f"missing template: {TEMPLATE_PATH}"
assert f'data-tick="{TICK}"' not in BUILD_LOG.read_text(encoding="utf-8")
append_row(SOURCE, "index", SOURCE_ROW)
append_row(ENRICHED, "lead_index", ENRICHED_ROW)
BUILD_LOG.write_text(ENTRY + "\n" + BUILD_LOG.read_text(encoding="utf-8"), encoding="utf-8")
print("appended Kajabi 516 to both CSVs and prepended build-log")
