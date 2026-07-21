#!/usr/bin/env python3
"""Ship Atlas tick 815: Lago opens the ai_billing_usage cohort."""
from __future__ import annotations

import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("C:/Users/Potts/projects/atlas-store")
INDEX = 815
VENDOR = "Lago"
HANDLE = "@getlago"
VERTICAL = "ai_billing_usage"
TICK = "2026-07-21-fast-exec-lago-815"
ROUTE = "FORM:https://getlago.com/book-a-demo"
FORM_URL = "https://getlago.com/book-a-demo"
TEMPLATE_NAME = "815_lago.md"
CHUNK_NAME = "chunk_815.html"
CHUNK_URL = "https://talonforgehq.github.io/atlas-store/chunks/chunk_815.html"
DATE = "2026-07-21"
QUEUED_AT = datetime.now(timezone.utc).isoformat()

LEADS = ROOT / "cold_email/leads.csv"
TEMPLATE_PATH = ROOT / f"cold_email/templates/{TEMPLATE_NAME}"
EVIDENCE_PATH = ROOT / "cold_email/815_lago.md"
CHUNK_PATH = ROOT / f"chunks/{CHUNK_NAME}"
SITEMAP = ROOT / "sitemap.xml"
INDEX_HTML = ROOT / "index.html"
BUILD_LOG = ROOT / "build-log.html"
REVENUE_CSV = ROOT / "cold_email/revenue_log.csv"
REVENUE_MD = ROOT / "revenue_log.md"
SEND_LOG = ROOT / "cold_email/send_log.json"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def csv_rows(path: Path) -> list[list[str]]:
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.reader(f))


def append_csv(path: Path, row: list[str]) -> None:
    raw = path.read_bytes()
    with path.open("a", encoding="utf-8", newline="") as f:
        if raw and not raw.endswith((b"\n", b"\r")):
            f.write("\n")
        csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator="\n").writerow(row)


# A completed rerun must be a mutation-free no-op.
completed = (
    any(r and r[0] == str(INDEX) for r in csv_rows(LEADS)[1:])
    and TEMPLATE_PATH.exists()
    and EVIDENCE_PATH.exists()
    and CHUNK_PATH.exists()
    and read(SITEMAP).count(CHUNK_NAME) == 1
    and read(INDEX_HTML).count(f'data-tick="{TICK}"') == 1
    and read(BUILD_LOG).count(f'data-tick="{TICK}"') == 1
    and any(len(r) > 1 and r[1] == str(INDEX) for r in csv_rows(REVENUE_CSV) if r)
    and read(REVENUE_MD).count("fast-exec tick Lago 815") == 1
)
if completed:
    print(f"COMPLETED_NOOP tick {INDEX}: all production anchors already present")
    sys.exit(0)

# Preflight: either complete or fully absent. Never continue from a partial cascade.
assert not any(r and r[0] == str(INDEX) for r in csv_rows(LEADS)[1:]), "lead 815 already exists partially"
for p in (TEMPLATE_PATH, EVIDENCE_PATH, CHUNK_PATH):
    assert not p.exists(), f"partial artifact already exists: {p}"
assert CHUNK_NAME not in read(SITEMAP), "partial sitemap anchor exists"
assert f'data-tick="{TICK}"' not in read(INDEX_HTML), "partial index anchor exists"
assert f'data-tick="{TICK}"' not in read(BUILD_LOG), "partial build-log anchor exists"
assert TICK not in read(REVENUE_MD), "partial revenue-log marker exists"
assert not any(len(r) > 1 and r[1] == str(INDEX) for r in csv_rows(REVENUE_CSV)[1:] if r), "partial revenue CSV row exists"

TIER_REASON = (
    "Lead 815 — Lago (getlago.com — open-source, AI-native billing infrastructure for usage metering, "
    "billing and invoicing, entitlements, cash collection, revenue analytics, embedded white-label billing, "
    "hybrid plans, multi-product pricing, prepaid credits, minimum commitments, progressive and graduated "
    "pricing, real-time flexible auditable billing for AI, enterprise, fintech/banks, and IoT/telco — company "
    "leadership verified first-party 2026-07-21 on getlago.com/about-us: Anh-Tho Chuong, CEO and co-founder; "
    "Raffi Sarkissian, CPO and co-founder — commercial route FORM:https://getlago.com/book-a-demo verified "
    "first-party HTTP 200 with canonical title 'Book a Demo' and description 'Schedule a personalized demo "
    "of Lago's open-source billing platform' — first-party security page verifies SOC 2 Type II, GDPR, "
    "regular third-party penetration tests, role-based access controls, encrypted data in transit and at rest, "
    "and transparent version-controlled security patches for self-hosting — first-party pricing page verifies "
    "Open Source, Lago Cloud, and Enterprise deployment surfaces — GitHub source route verified from the "
    "first-party site at github.com/getlago/lago — OPENER #1/5 of NEW VERTICAL ai_billing_usage after the prior "
    "ai_legal_hold_ediscovery cohort closed 5/5 at DISCO 814. Real company + real website + real founders + "
    "sanctioned commercial demo route verified. OPENER non-overlapping wedge: (1) event-to-meter-to-wallet-to-"
    "invoice lineage for token, GPU-second, API-call, storage-byte, and credit-based AI usage; (2) immutable "
    "pricing-version receipt covering package, volume, graduated, percentage, minimum-commitment, prepaid-credit, "
    "and hybrid subscription-plus-usage changes; (3) open-source/self-hosted versus Lago Cloud versus Enterprise "
    "control inheritance with customer-managed deployment boundaries and version-controlled security patches; "
    "(4) customer-wallet and prepaid-credit liability reconciliation across top-ups, grants, expirations, voids, "
    "refunds, and invoice application; (5) finance-grade invoice finalization, tax-field, credit-note, dunning, "
    "and revenue-analytics evidence joined to the exact metered event and pricing-plan version. Tier-1 evidence "
    "wedge: a 20-column billable-event receipt joining event_id + customer_id + external_subscription_id + "
    "metric_code + event_timestamp + ingestion_timestamp + idempotency_key + deduplication_result + quantity + "
    "aggregation_window + pricing_plan_version + pricing_model + unit_price + currency + wallet_transaction_id + "
    "credit_balance_before + credit_balance_after + invoice_id + invoice_line_id + correction_credit_note_id. "
    "Audit map: SOC 2 CC6/CC7/CC8 + GDPR Art. 5/25/30/32 + ISO/IEC 27001 + ASC 606/IFRS 15 evidence support + "
    "EU AI Act Art. 12 record keeping for AI-service billing telemetry + PCI-scope minimization through payment-"
    "provider tokenization boundaries. Offer: $500/48h evidence-gap map or $497/mo quarterly refresh. No guessed "
    "inbox added; security@getlago.com is a restricted vulnerability-reporting route and is explicitly excluded. "
    "The first-party Book a Demo form is the commercial route. It was not submitted; no send_log event, delivery, "
    "payment, or revenue is claimed."
)

append_csv(LEADS, [str(INDEX), VENDOR, HANDLE, ROUTE, VERTICAL, "1", TEMPLATE_NAME, TIER_REASON])
rows = csv_rows(LEADS)
target = [r for r in rows[1:] if r and r[0] == str(INDEX)]
assert len(target) == 1 and len(target[0]) == len(rows[0]) == 8
assert target[0][1:7] == [VENDOR, HANDLE, ROUTE, VERTICAL, "1", TEMPLATE_NAME]

TEMPLATE = f'''# Template 815 — Lago (ai_billing_usage OPENER #1/5)

**Commercial route:** `{ROUTE}` (first-party Book a Demo page verified HTTP 200 on 2026-07-21; not submitted).
**Leadership:** Anh-Tho Chuong, CEO & co-founder; Raffi Sarkissian, CPO & co-founder (first-party `getlago.com/about-us`).
**Restricted route excluded:** `security@getlago.com` is for vulnerability reports, not commercial outreach.

## Three subject-line A/B/C variants

**Subject A — audit-letter opener:** Anh-Tho / Raffi — 5 evidence gaps between Lago usage events, prepaid credits, pricing versions, and finalized invoices

**Subject B — regulation-anchored:** Lago's 20-column billable-event receipt for SOC 2 + GDPR + ASC 606 / IFRS 15 evidence support

**Subject C — peer-pressure:** Lago + Metronome + Orb: which billing platform can replay one AI token event into the exact wallet debit and invoice line?

## 5-question audit-letter opener

Anh-Tho / Raffi — Talon Forge is opening an `ai_billing_usage` audit cohort around one procurement question: can a buyer replay any billed AI event from raw usage through rating, credits, invoice, and correction without a spreadsheet?

1. **What is the event-to-meter evidence chain?** For every token, GPU-second, API call, storage byte, or custom event, what is the immutable receipt joining `event_id`, customer, metric, event time, ingestion time, idempotency key, duplicate decision, aggregation window, and rated quantity?
2. **What is the pricing-version evidence chain?** When a team changes package, volume, graduated, percentage, minimum-commitment, prepaid-credit, or hybrid pricing, what is the effective-dated plan version and approval trail that proves which rule rated each event?
3. **What is the wallet and credit-liability evidence chain?** What joins grants, paid top-ups, promotional credits, expirations, voids, refunds, and invoice applications to `credit_balance_before`, `credit_balance_after`, the source event, and the accounting period?
4. **What is the deployment-boundary evidence chain?** Across Open Source/self-hosted, Lago Cloud, and Enterprise, what proves version, tenant boundary, role-based access, encryption, security-patch state, and whether billing data crossed the contracted control boundary?
5. **What is the invoice-correction evidence chain?** What joins the final invoice line to its rated events, pricing version, tax fields, payment-provider reference, credit note, reissued invoice, dunning state, and revenue-analytics snapshot?

## Body (~440 words)

Lago's public product surface is unusually strong for this problem: usage metering, billing and invoicing, entitlements, cash collection, revenue analytics, embedded billing, AI-specific token/GPU/credit models, self-hosting, and a managed cloud all sit under one platform. The buyer-side risk is not feature coverage. It is proving that every amount is reproducible after pricing, usage, or a customer contract changes.

We package that proof as a fixed-scope **20-column billable-event receipt**: event ID, customer ID, external subscription ID, metric code, event timestamp, ingestion timestamp, idempotency key, deduplication result, quantity, aggregation window, pricing-plan version, pricing model, unit price, currency, wallet transaction ID, credit balance before, credit balance after, invoice ID, invoice-line ID, and correction-credit-note ID.

That receipt creates three commercial outcomes. Product engineering gets a deterministic replay path for disputed usage. Finance gets a bridge from source events to invoices, credits, and period reporting. Procurement gets evidence it can map to SOC 2 change/access controls, GDPR data-accountability requirements, and revenue-recognition support under ASC 606 or IFRS 15 without claiming that the billing platform itself performs the customer's accounting judgment.

Lago is the OPENER because the open-source/self-hosted surface adds a control boundary that closed SaaS-only billing vendors cannot copy. A buyer can inspect the source and own deployment, but that creates a second audit question: which version, patch, configuration, and extension produced the bill? The same receipt must survive Lago Cloud, Enterprise, and self-hosted deployments without silently changing event identity or pricing semantics.

First-party evidence checked on 2026-07-21: `getlago.com/` describes open-source metering and usage-based billing; `/about-us` names Anh-Tho Chuong as CEO & co-founder and Raffi Sarkissian as CPO & co-founder; `/book-a-demo` is the sanctioned commercial route; `/security` states SOC 2 Type II and GDPR posture and publishes `security@getlago.com` only for vulnerability reporting; `/pricing` distinguishes Open Source, Lago Cloud, and Enterprise surfaces.

## Prior cohort and planned siblings

The prior `ai_legal_hold_ediscovery` cohort closed at DISCO 814. This new vertical does not reuse its legal-hold wedge. Planned `ai_billing_usage` siblings are Metronome, Orb, Stripe Billing, and a public-company billing/revenue-recognition CLOSER selected on first-party evidence.

## 3 engagement options

1. **$500/48h evidence-gap map:** the 20-column receipt, five-question audit letter, and one disputed-invoice replay.
2. **$497/mo quarterly refresh:** pricing-model, metering, wallet, security-boundary, and invoice-correction diffs every quarter.
3. **$497/mo × 5-client cohort:** one shared benchmark across Lago plus four non-overlapping usage-billing siblings.

## PS CTA

Reply through the existing Lago commercial channel with “send the receipt” and we will return the scoped 20-column map. The form has not been submitted in this tick; no delivery or revenue is claimed.
'''
write(TEMPLATE_PATH, TEMPLATE)
assert all(x in TEMPLATE for x in ("Subject A", "Subject B", "Subject C", "## 5-question", "$500/48h", "$497/mo"))
assert TEMPLATE.lower().count("what is the") >= 5

EVIDENCE = f'''---
index: {INDEX}
vendor: Lago
vertical: {VERTICAL}
position: OPENER #1/5
route: {ROUTE}
submitted: false
ceo: Anh-Tho Chuong
cofounder: Raffi Sarkissian
verified: {DATE}
---

# Lead 815 — Lago

## First-party identity proof

- `https://getlago.com/` — HTTP 200; open-source billing infrastructure with Usage Metering, Billing & Invoicing, Entitlements, Cash Collection, Revenue Analytics, Lago Embedded, and Lago AI.
- `https://getlago.com/about-us` — HTTP 200; JSON-LD and rendered leadership cards name **Anh-Tho Chuong — CEO & co-founder at Lago** and **Raffi Sarkissian — CPO & co-founder at Lago**.
- `https://getlago.com/book-a-demo` — HTTP 200; canonical **Book a Demo** commercial page, with the first-party description “Schedule a personalized demo of Lago's open-source billing platform.”
- `https://getlago.com/security` — HTTP 200; states SOC 2 Type II, GDPR, regular third-party penetration testing, and version-controlled open-source security updates. The published `security@getlago.com` route is vulnerability-only and excluded from sales outreach.
- `https://getlago.com/pricing` — HTTP 200; distinguishes Open Source, Lago Cloud, and Enterprise offers.
- `https://github.com/getlago/lago` — linked directly by the first-party site as the source repository.

## Cohort decision

Lago opens `ai_billing_usage` at **OPENER #1/5** after `ai_legal_hold_ediscovery` closed 5/5 at DISCO 814. The wedge is non-overlapping: billable-event lineage, pricing-version provenance, wallet/credit liability, deployment-boundary inheritance, and invoice-correction replay.

## 20-column provenance cascade

1. `event_id`
2. `customer_id`
3. `external_subscription_id`
4. `metric_code`
5. `event_timestamp`
6. `ingestion_timestamp`
7. `idempotency_key`
8. `deduplication_result`
9. `quantity`
10. `aggregation_window`
11. `pricing_plan_version`
12. `pricing_model`
13. `unit_price`
14. `currency`
15. `wallet_transaction_id`
16. `credit_balance_before`
17. `credit_balance_after`
18. `invoice_id`
19. `invoice_line_id`
20. `correction_credit_note_id`

## Commercial-safety status

`{ROUTE}` is a first-party commercial demo form. It was **not submitted**. No guessed inbox was added; `security@getlago.com` remains excluded. No send_log event, delivery, payment, or revenue is claimed. **$0 sent / $0 received.**
'''
write(EVIDENCE_PATH, EVIDENCE)

CHUNK = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Lago usage-based billing audit trail — token events, prepaid credits, pricing versions, and invoice replay | Atlas @ Talon Forge</title>
<meta name="description" content="A 20-column billable-event receipt for Lago usage metering, hybrid pricing, prepaid credits, wallets, invoices, and credit notes. Maps event-to-invoice lineage to SOC 2, GDPR, ASC 606 and IFRS 15 evidence support.">
<meta name="keywords" content="Lago usage based billing audit trail, Lago AI token billing, prepaid credits wallet reconciliation, usage metering invoice replay, pricing version provenance, open source billing controls, self hosted billing audit, SOC 2 billing evidence, GDPR usage telemetry, ASC 606 usage billing evidence, IFRS 15 usage billing, $500 48h evidence gap map">
<link rel="canonical" href="{CHUNK_URL}">
<meta property="og:title" content="Lago: the 20-column billable-event receipt">
<meta property="og:description" content="Replay one AI usage event through pricing, wallet credits, invoice finalization, and correction.">
<meta property="og:type" content="article">
<meta property="og:url" content="{CHUNK_URL}">
</head>
<body>
<article id="chunk-815" data-tick="{TICK}" data-cohort="{VERTICAL}" data-lead="815" data-position="OPENER #1/5">
<h1>Lago usage-based billing audit trail: from AI token event to wallet debit, invoice line, and credit note</h1>
<p><strong>Long-tail keyword cluster:</strong> Lago usage-based billing audit trail · Lago AI token billing · Lago GPU-second metering · Lago prepaid credits · Lago wallet reconciliation · hybrid pricing audit · graduated pricing version · invoice-line event replay · open-source billing control boundary · self-hosted billing version evidence · SOC 2 billing change control · GDPR usage telemetry · ASC 606 usage-billing evidence support · IFRS 15 invoice evidence · disputed usage invoice replay · $500/48h billing evidence-gap map · $497/mo billing control refresh.</p>
<h2>Why Lago opens the ai_billing_usage cohort</h2>
<p>Lago combines open-source usage metering, billing and invoicing, entitlements, cash collection, revenue analytics, embedded billing, and AI-oriented token/GPU/credit models. Its self-hosted, Lago Cloud, and Enterprise surfaces make it the strongest OPENER: the audit trail must preserve event identity and pricing semantics while the deployment owner changes.</p>
<p>First-party leadership proof is explicit: <strong>Anh-Tho Chuong — CEO &amp; co-founder</strong> and <strong>Raffi Sarkissian — CPO &amp; co-founder</strong> appear on <code>getlago.com/about-us</code>. The Book a Demo page is the commercial route. The security inbox is excluded because the security page limits it to vulnerability reporting.</p>
<h2>The five-question audit-letter wedge</h2>
<ol>
<li><strong>Event-to-meter:</strong> can any token, GPU-second, API-call, or storage event be replayed with its timestamp, idempotency key, duplicate decision, aggregation window, and rated quantity?</li>
<li><strong>Pricing version:</strong> which effective-dated package, volume, graduated, percentage, commitment, credit, or hybrid rule priced that event?</li>
<li><strong>Wallet liability:</strong> which grant, paid top-up, expiration, void, refund, or invoice application changed the credit balance?</li>
<li><strong>Deployment boundary:</strong> which Open Source, Lago Cloud, or Enterprise version, patch, role policy, and encryption boundary processed the data?</li>
<li><strong>Invoice correction:</strong> which source events, plan version, tax fields, payment reference, credit note, and reissued invoice explain the final amount?</li>
</ol>
<h2>The 20-column billable-event receipt</h2>
<table>
<thead><tr><th>#</th><th>Field</th><th>Audit purpose</th></tr></thead>
<tbody>
<tr><td>1–4</td><td>event_id · customer_id · external_subscription_id · metric_code</td><td>Stable source identity</td></tr>
<tr><td>5–8</td><td>event_timestamp · ingestion_timestamp · idempotency_key · deduplication_result</td><td>Timing and duplicate defense</td></tr>
<tr><td>9–13</td><td>quantity · aggregation_window · pricing_plan_version · pricing_model · unit_price</td><td>Deterministic rating replay</td></tr>
<tr><td>14–17</td><td>currency · wallet_transaction_id · credit_balance_before · credit_balance_after</td><td>Wallet and credit-liability bridge</td></tr>
<tr><td>18–20</td><td>invoice_id · invoice_line_id · correction_credit_note_id</td><td>Finalization and correction chain</td></tr>
</tbody>
</table>
<h2>Compliance and finance-evidence map</h2>
<p>The receipt supports a buyer's SOC 2 access/change/monitoring evidence, GDPR accountability for usage telemetry, ISO/IEC 27001 control evidence, EU AI Act Article 12 record-keeping where AI-service telemetry is in scope, and invoice-to-source support used in ASC 606 or IFRS 15 workflows. It does not replace the customer's accounting judgment, tax engine, or auditor.</p>
<h2>Open source is an audit advantage and a control obligation</h2>
<p>Inspectable source and self-hosting reduce vendor opacity. They also require version proof: commit/release, patch state, extensions, deployment configuration, and migration history must join the billable-event receipt. Otherwise two customers can run “Lago” yet produce materially different billing behavior.</p>
<h2>Commercial route and engagement options</h2>
<p><strong>$500/48h:</strong> one 20-column receipt, five-question audit letter, and disputed-invoice replay. <strong>$497/mo:</strong> quarterly metering, pricing, wallet, deployment, and correction-control refresh. <strong>$497/mo × 5 clients:</strong> a shared benchmark across Lago and four non-overlapping usage-billing siblings.</p>
<p>The verified commercial route is <code>{ROUTE}</code>. It was not submitted. No email, form submission, delivery, payment, or revenue is claimed.</p>
<h2>Cohort position</h2>
<p><code>{VERTICAL}</code> is <strong>OPEN at 1/5</strong>. Planned siblings are Metronome, Orb, Stripe Billing, and a public-company billing/revenue-recognition CLOSER chosen from first-party evidence. The prior legal-hold cohort remains closed at DISCO 814.</p>
<p class="footer">Atlas @ Talon Forge — cron tick {TICK} · Lead 815 + evidence + template + chunk + sitemap + index + build/revenue logs · FORM-only route not submitted · $0 sent / $0 received.</p>
</article>
</body>
</html>
'''
write(CHUNK_PATH, CHUNK)
assert CHUNK.count("<li>") == 5 and CHUNK.count("<tr>") == 6
assert all(x in CHUNK for x in ("Anh-Tho Chuong", "Raffi Sarkissian", "20-column", ROUTE))

sitemap = read(SITEMAP)
SITEMAP_BLOCK = f'''  <url>
    <loc>{CHUNK_URL}</loc>
    <lastmod>{DATE}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
'''
assert sitemap.count("</urlset>") == 1
write(SITEMAP, sitemap.replace("</urlset>", SITEMAP_BLOCK + "</urlset>", 1))
assert read(SITEMAP).count(CHUNK_NAME) == 1

CARD = f'''
<section id="chunk-815" class="card" data-tick="{TICK}" data-cohort="{VERTICAL}" data-lead="815" data-cohort-role="opener-1-of-5">
  <h2>Lago usage-based billing audit trail: one AI token event to wallet debit, invoice line, and credit note</h2>
  <p><strong>Long-tail keyword cluster:</strong> Lago token billing, Lago usage metering audit trail, prepaid credits reconciliation, pricing-version provenance, self-hosted billing controls, invoice correction replay, SOC 2 billing evidence, ASC 606 / IFRS 15 evidence support.</p>
  <p><strong>Vendor:</strong> Lago · <strong>Leadership:</strong> Anh-Tho Chuong, CEO &amp; co-founder; Raffi Sarkissian, CPO &amp; co-founder · <strong>Route:</strong> <code>{ROUTE}</code> (not submitted).</p>
  <p><strong>Wedge:</strong> 20-column billable-event receipt joining source event, idempotency/dedup, aggregation, pricing-plan version, wallet transaction, credit balances, invoice line, and correction credit note across Open Source/self-hosted, Lago Cloud, and Enterprise.</p>
  <p><a class="btn" href="chunks/{CHUNK_NAME}">Read the Lago evidence map</a> <a class="btn" href="cold_email/815_lago.md">Companion evidence</a> <a class="btn" href="cold_email/templates/{TEMPLATE_NAME}">Template 815_lago.md</a></p>
  <p class="cohort-marker">{VERTICAL} <strong>OPEN at 1/5</strong> after DISCO 814 closed ai_legal_hold_ediscovery at 5/5.</p>
</section>
'''
index_text = read(INDEX_HTML)
prior_start = index_text.find('<section id="chunk-814"')
assert prior_start >= 0
prior_close = index_text.find("</section>", prior_start)
assert prior_close >= 0
insert_at = prior_close + len("</section>")
write(INDEX_HTML, index_text[:insert_at] + "\n\n" + CARD + index_text[insert_at:])
assert read(INDEX_HTML).count(f'data-tick="{TICK}"') == 1

BUILD_ENTRY = f'''

<div class="tick-entry" data-tick="{TICK}">
<p><strong>Cron tick {TICK} — Lead 815 Lago opens ai_billing_usage at OPENER #1/5.</strong> Appended the verified form-only lead to <code>cold_email/leads.csv</code>; wrote <code>cold_email/815_lago.md</code> and <code>cold_email/templates/815_lago.md</code>; published <code>chunks/chunk_815.html</code>; wired one index card and one sitemap URL.</p>
<p><strong>First-party proof:</strong> <code>getlago.com/about-us</code> names Anh-Tho Chuong as CEO &amp; co-founder and Raffi Sarkissian as CPO &amp; co-founder; <code>/book-a-demo</code> is the commercial route; <code>/security</code> states SOC 2 Type II + GDPR and limits <code>security@getlago.com</code> to vulnerability reports; <code>/pricing</code> distinguishes Open Source, Lago Cloud, and Enterprise.</p>
<p><strong>Revenue progress:</strong> opened a non-overlapping billing vertical with a 20-column event-to-invoice receipt and staged $500/48h + $497/mo offers. The Book a Demo form was not submitted, so no <code>send_log.json</code> event was fabricated. SMTP remains gated. <strong>$0 sent / $0 received.</strong></p>
<p><strong>Pivot:</strong> chose Lago over Metronome and Orb because Lago's first-party About page provides exact founder roles, its Book a Demo route is explicit, and open-source/self-hosted + cloud deployment creates a distinct audit-control wedge. Next siblings: Metronome, Orb, Stripe Billing, then a public-company CLOSER.</p>
<p class="footer">Atlas @ Talon Forge — Lead 815 + template + evidence + SEO chunk + sitemap + index + build/revenue logs + commit/push · {VERTICAL} OPEN at 1/5 · FORM-only route not submitted.</p>
</div>'''
build = read(BUILD_LOG)
write(BUILD_LOG, build.rstrip() + BUILD_ENTRY + "\n")
last = read(BUILD_LOG).rsplit('<div class="tick-entry"', 1)[-1]
assert f'data-tick="{TICK}"' in last

rrows = csv_rows(REVENUE_CSV)
# This long-running ledger is headerless. New rows use the canonical seven-column
# shape; one legacy lead-802 row is over-wide, so validate the intended append
# schema without rewriting or normalizing unrelated historical data.
assert rrows and all(len(r) == 7 for r in rrows if r and len(r) != 14)
assert any(len(r) == 14 and len(r) > 1 and r[1] == "802" for r in rrows)
append_csv(REVENUE_CSV, [DATE, str(INDEX), TEMPLATE_NAME, CHUNK_NAME, f"{VERTICAL} OPENER #1/5", "0", "Lago OPENER: first-party founders + Book a Demo route + 20-column billable-event receipt; form not submitted; no send_log event; $0 sent / $0 received."])
rtarget = [r for r in csv_rows(REVENUE_CSV)[1:] if len(r) > 1 and r[1] == str(INDEX)]
assert len(rtarget) == 1 and len(rtarget[0]) == 7

REVENUE_ENTRY = f'''

---

## 2026-07-21 — fast-exec tick Lago 815 ({VERTICAL} OPENER #1/5)

- **Artifact:** Lead 815, companion evidence, 5-question template, 20-column SEO audit map, sitemap URL, index card, and build-log receipt.
- **First-party proof:** Anh-Tho Chuong (CEO & co-founder) + Raffi Sarkissian (CPO & co-founder) on `getlago.com/about-us`; `getlago.com/book-a-demo` is the commercial route; `getlago.com/security` verifies SOC 2 Type II + GDPR and excludes its security inbox from sales use.
- **Revenue impact:** $500/48h evidence-gap map + $497/mo refresh staged. FORM-only route not submitted; no send event; **$0 sent / $0 received**.
- **Next:** extend `{VERTICAL}` with Metronome or Orb as sibling #2/5 after first-party founder and commercial-route proof.
'''
write(REVENUE_MD, read(REVENUE_MD).rstrip() + REVENUE_ENTRY + "\n")

# FORM-only commercial-route invariant: no send event until an actual verified submission.
send_entries = json.loads(read(SEND_LOG))
assert isinstance(send_entries, list)
assert not any(str(e.get("lead") or e.get("index")) == str(INDEX) or e.get("tick") == TICK for e in send_entries)

# Final parse-back across the full cascade.
assert TEMPLATE_PATH.stat().st_size > 4000
assert EVIDENCE_PATH.stat().st_size > 2000
assert CHUNK_PATH.stat().st_size > 6000
assert read(SITEMAP).count(CHUNK_NAME) == 1
assert read(INDEX_HTML).count(f'data-tick="{TICK}"') == 1
assert read(BUILD_LOG).count(f'data-tick="{TICK}"') == 1
assert read(REVENUE_MD).count("fast-exec tick Lago 815") == 1
print(
    "SHIP_OK tick=815 vendor=Lago cohort=ai_billing_usage position=OPENER#1/5 "
    f"lead_rows={len(csv_rows(LEADS)) - 1} template_bytes={TEMPLATE_PATH.stat().st_size} "
    f"evidence_bytes={EVIDENCE_PATH.stat().st_size} chunk_bytes={CHUNK_PATH.stat().st_size} "
    "sitemap_count=1 index_count=1 build_count=1 send_log_count=0"
)
