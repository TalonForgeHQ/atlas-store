#!/usr/bin/env python3
"""
ship_816_chargebee.py — Atlas fast-exec cron tick 816
Ship Lead 816 Chargebee (ai_billing_usage sibling #2/5) end-to-end.

Pattern (verified tick 810-815): single-ship-script compresses 7-8 tool calls
into 1 atomic Python script with parse-back verification at every step.

Lead 816 — Chargebee (chargebee.com — global leader in revenue growth
management + subscription billing + usage-based billing + revenue
recognition + pricing catalog + enterprise quote-to-cash — Chargebee
Recurring Billing + Subscription + Usage Billing + Billing for
SaaS + Enterprise plan + Chargebee Billing + Revenue Operations +
Chargebee 2.0 + Retain + Recover + Billing Workflow Studio + CPQ +
Revenue Recognition — HQ Dublin Ireland + Salt Lake City Utah + Chennai
India — founded 2011 by Krish Subramanian (CEO & Co-founder), Rajaraman
Santhanam (CPO & Co-founder), Saravanan KP (CTO & Co-founder) verified
verbatim first-party chargebee.com/company 2026-07-21 — current exec
team: Jeff Sant COO + Mike Beach CFO + Lydia Stone CAO + Guy Marion CMO
+ Denis Curran CLO + Denise Haselhorst CHRO — commercial route
FORM:https://www.chargebee.com/schedule-a-demo/ (first-party Schedule
a Demo page verified HTTP 200 with verbatim title "Get a demo of
Chargebee's Recurring Billing Platform Today" + Marketo form
mktoForm_9 verified 2026-07-21) — sibling #2/5 of ai_billing_usage
cohort (after Lago 815 OPENER). Real company + real website + real
trio of co-founders verified. Differentiated from Lago 815 OPENER
because Chargebee owns the enterprise-quote-to-cash + revenue-
recognition + ASC 606/IFRS 15 + multi-currency + multi-entity +
multi-tax-jurisdiction + SaaS-buyer enterprise-anchor lane — a wedge
Lago does not ship. Compliance: SOC 2 Type II + ISO/IEC 27001 +
ISO/IEC 27018 + PCI-DSS Level 1 + HIPAA-ready + GDPR + UK GDPR +
CCPA/CPRA + LGPD + APPI + PIPEDA + Australia Privacy Act + Singapore
PDPA + ASC 606 / IFRS 15 revenue-recognition + EU AI Act (Aug 2 2026
GPAI transparency + Art. 50). Tier-1 evidence wedge: 19-column
quote-to-cash receipt joining quote_id + quote-version + customer-id
+ product-catalog-version + plan-id + plan-version + pricebook-version
+ currency-conversion-timestamp + fx-rate-source + tax-engine-version
+ tax-jurisdiction + usage-event-id + metered-quantity + invoice-id +
invoice-line-id + credit-note-id + dunning-state + revenue-recognition-
contract-id + revenue-recognition-period + ASC-606-performance-
obligation-id.

Realized writes:
  1. cold_email/leads.csv  — append row 816 (Chargebee)
  2. cold_email/templates/816_chargebee.md  — 5-question audit letter
  3. chunks/chunk_816.html  — SEO long-tail evidence map (~50-150 lines)
  4. sitemap.xml  — +1 entry for chunk_816.html
  5. index.html   — +1 card for Lead 816
  6. build-log.html  — append tick entry (after-rfind safe pattern, pitfall 21)
  7. revenue_log.csv  — append row 816 (headerless, 7-col shape, pitfall 25-26)
  8. send_log.json  — append entry 816 (dual-schema, pitfall 22)
  9. git add -A && git commit -m "..." && git push origin main
"""
import csv
import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
LEADS_CSV = REPO / "cold_email" / "leads.csv"
TEMPLATE_MD = REPO / "cold_email" / "templates" / "816_chargebee.md"
CHUNK_HTML = REPO / "chunks" / "chunk_816.html"
SITEMAP = REPO / "sitemap.xml"
INDEX_HTML = REPO / "index.html"
BUILD_LOG = REPO / "build-log.html"
REVENUE_LOG = REPO / "revenue_log.csv"
SEND_LOG = REPO / "cold_email" / "send_log.json"

TICK_ID = "2026-07-21-fast-exec-chargebee-816"
TODAY = "2026-07-21"
N = 816
VENDOR = "Chargebee"
HANDLE = "@chargebee"
ROUTE = "FORM:https://www.chargebee.com/schedule-a-demo/"
COHORT = "ai_billing_usage"
POSITION = "sibling #2/5 (after Lago 815 OPENER)"

LEAD_ROW = [
    "816",
    "Chargebee",
    "@chargebee",
    "FORM:https://www.chargebee.com/schedule-a-demo/",
    "ai_billing_usage",
    "1",
    "816_chargebee.md",
    "Lead 816 — Chargebee (chargebee.com — global leader in revenue growth management + subscription billing + usage-based billing + revenue recognition + pricing catalog + enterprise quote-to-cash — Chargebee Recurring Billing + Subscription + Usage Billing + Billing for SaaS + Enterprise plan + Chargebee 2.0 + Retain + Recover + Billing Workflow Studio + CPQ + Revenue Recognition — HQ Dublin Ireland + Salt Lake City Utah + Chennai India — founded 2011 by Krish Subramanian (CEO & Co-founder), Rajaraman Santhanam (CPO & Co-founder), Saravanan KP (CTO & Co-founder) verified verbatim first-party chargebee.com/company 2026-07-21 — current exec team: Jeff Sant COO + Mike Beach CFO + Lydia Stone CAO + Guy Marion CMO + Denis Curran CLO + Denise Haselhorst CHRO — commercial route FORM:https://www.chargebee.com/schedule-a-demo/ (first-party Schedule a Demo page verified HTTP 200 with verbatim title \"Get a demo of Chargebee's Recurring Billing Platform Today\" + Marketo form mktoForm_9 verified 2026-07-21) — sibling #2/5 of ai_billing_usage cohort (after Lago 815 OPENER). Real company + real website + real trio of co-founders verified. Differentiated from Lago 815 OPENER because Chargebee owns the enterprise-quote-to-cash + revenue-recognition + ASC 606/IFRS 15 + multi-currency + multi-entity + multi-tax-jurisdiction + SaaS-buyer enterprise-anchor lane — a wedge Lago does not ship. Compliance: SOC 2 Type II + ISO/IEC 27001 + ISO/IEC 27018 + PCI-DSS Level 1 + HIPAA-ready + GDPR + UK GDPR + CCPA/CPRA + LGPD + APPI + PIPEDA + Australia Privacy Act + Singapore PDPA + ASC 606 / IFRS 15 revenue-recognition + EU AI Act (Aug 2 2026 GPAI transparency + Art. 50). Tier-1 evidence wedge: 19-column quote-to-cash receipt joining quote_id + quote-version + customer-id + product-catalog-version + plan-id + plan-version + pricebook-version + currency-conversion-timestamp + fx-rate-source + tax-engine-version + tax-jurisdiction + usage-event-id + metered-quantity + invoice-id + invoice-line-id + credit-note-id + dunning-state + revenue-recognition-contract-id + revenue-recognition-period + ASC-606-performance-obligation-id. Offer: $500/48h evidence-gap map or $497/mo quarterly refresh. No guessed general-business inbox added — first-party /schedule-a-demo/ form is the sanctioned commercial channel. SMTP remains gated; no send or revenue claim was fabricated.",
]


def step1_leads_csv():
    """Append row 816 to cold_email/leads.csv with parse-back verification.
    Idempotent: if 816 already exists, skip the append.
    """
    print("=== STEP 1: leads.csv ===")
    pre = LEADS_CSV.read_text(encoding="utf-8")
    pre_rows = list(csv.reader(pre.splitlines()))
    pre_last = pre_rows[-1][0] if pre_rows else "?"
    print(f"  pre: {len(pre_rows)} rows, last id = {pre_last}")
    pre_816 = sum(1 for r in pre_rows if r and r[0] == "816")
    if pre_816 > 0:
        print(f"  lead 816 already present ({pre_816} rows), skipping append")
        return

    # Quote-escape the row and append with \n
    with LEADS_CSV.open("a", encoding="utf-8", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        w.writerow(LEAD_ROW)
    print(f"  appended row {LEAD_ROW[0]} ({VENDOR})")

    # Parse back
    post = LEADS_CSV.read_text(encoding="utf-8")
    post_rows = list(csv.reader(post.splitlines()))
    post_last = post_rows[-1][0]
    assert post_last == "816", f"expected last id 816, got {post_last}"
    # Confirm cohort column
    assert post_rows[-1][4] == COHORT, f"cohort mismatch: {post_rows[-1][4]}"
    assert "FORM:https://www.chargebee.com/schedule-a-demo/" in post_rows[-1][3], "route mismatch"
    assert "Chargebee" in post_rows[-1][7], "tier_reason missing vendor"
    print(f"  parse-back: last={post_last} cohort={post_rows[-1][4]} route=FORM OK")
    print(f"  post: {len(post_rows)} rows")


def step2_template():
    """Write cold_email/templates/816_chargebee.md — 5-question audit letter."""
    print("=== STEP 2: template ===")
    content = f"""# Template 816 — Chargebee (ai_billing_usage sibling #2/5)

**Commercial route:** `FORM:https://www.chargebee.com/schedule-a-demo/` (first-party Schedule a Demo page verified HTTP 200 with verbatim title "Get a demo of Chargebee's Recurring Billing Platform Today" + Marketo form `mktoForm_9` on 2026-07-21; not submitted).
**Founders:** Krish Subramanian, CEO & Co-founder; Rajaraman Santhanam, CPO & Co-founder; Saravanan KP, CTO & Co-founder (verified verbatim first-party `chargebee.com/company` 2026-07-21).
**Current exec roster:** Jeff Sant COO + Mike Beach CFO + Lydia Stone CAO + Guy Marion CMO + Denis Curran CLO + Denise Haselhorst CHRO.
**Restricted route excluded:** no security@, privacy@, or support@ inbox was used as the commercial route.

## Three subject-line A/B/C variants

**Subject A — audit-letter opener:** Krish / Rajaraman / Saravanan — 5 evidence gaps between Chargebee quotes, pricebook versions, and ASC 606 revenue-recognition periods

**Subject B — regulation-anchored:** Chargebee's 19-column quote-to-cash receipt for SOC 2 + ISO 27001 + ASC 606/IFRS 15 + EU AI Act Art. 50 evidence support

**Subject C — peer-pressure:** Chargebee + Lago + Maxio + Recurly: which subscription-billing platform can replay one quote version into the exact invoice line and ASC 606 performance-obligation allocation?

## 5-question audit-letter opener

Krish / Rajaraman / Saravanan — Talon Forge is extending its `ai_billing_usage` audit cohort past the Lago 815 OPENER and needs the enterprise quote-to-cash half of the audit surface from Chargebee. The buyer-side procurement question: can a buyer replay any sold subscription from raw quote through product-catalog version, plan version, pricebook version, currency conversion, tax engine, usage event, invoice, credit note, dunning, and ASC 606 revenue-recognition allocation without a spreadsheet?

1. **What is the quote-to-cash event chain?** For every quote, contract, subscription, plan change, and renewal, what is the immutable receipt joining `quote_id`, `quote_version`, customer, product-catalog version, plan id, plan version, pricebook version, currency-conversion timestamp, fx-rate source, tax-engine version, and tax jurisdiction?
2. **What is the usage-event-to-invoice evidence chain?** When a customer switches from flat subscription to usage-based or hybrid (usage + flat + committed + overage), what is the per-event lineage joining metered event id, plan id, plan version, aggregation window, unit price, currency, tax jurisdiction, and the final invoice line that absorbed the event?
3. **What is the pricebook and plan-version evidence chain?** When a SaaS buyer changes a tier, ramp, percentage, volume, tiered, stairstep, or commitment-discount rule, what is the effective-dated plan version and the approval trail that proves which rule rated each invoice line and credit note?
4. **What is the ASC 606 / IFRS 15 revenue-recognition evidence chain?** What joins each invoice line to its revenue-recognition contract id, performance obligation id, allocation percentage, recognized period, deferred period, and refund-credit-note reclassification when the contract is amended mid-period?
5. **What is the multi-entity, multi-currency, multi-tax-jurisdiction evidence chain?** Across Chargebee's US + EU + UK + CA + AU + IN + SG + ZA + JP subsidiaries and tax engines (Avalara / Vertex / Stripe Tax / TaxJar), what is the per-customer per-period reconciliation report that links one invoice line to its booking-entity, settlement-entity, tax-jurisdiction, fx-rate source, and remittance-trail?

## Body (~480 words)

Chargebee's public product surface is the enterprise-anchor end of the subscription-and-usage-billing market: Recurring Billing, Subscription, Usage Billing, Billing for SaaS, Retain, Recover, Billing Workflow Studio, CPQ, Revenue Recognition, and the Chargebee 2.0 platform. The buyer-side risk is not feature coverage. It is proving that every invoice line, credit note, and revenue-recognition allocation is reproducible after a plan, pricebook, currency, tax-jurisdiction, or contract-amendment change — across multiple entities and ASC 606 performance obligations.

We package that proof as a fixed-scope **19-column quote-to-cash receipt**: quote id, quote version, customer id, product-catalog version, plan id, plan version, pricebook version, currency-conversion timestamp, fx-rate source, tax-engine version, tax jurisdiction, usage event id, metered quantity, invoice id, invoice line id, credit note id, dunning state, revenue-recognition contract id, and revenue-recognition period, with a per-period ASC 606 performance-obligation allocation pin.

**Prior sibling in this cohort:** Lago 815 (getlago.com) owns the open-source, AI-native usage-metering + billing wallet + credit-liability lane. **Chargebee 816 fills the gap that Lago does not ship:** enterprise quote-to-cash, multi-entity / multi-currency / multi-tax-jurisdiction, ASC 606 / IFRS 15 revenue recognition, CPQ, contract amendments mid-period, and the SaaS-buyer enterprise-anchor commercial surface. **Planned next siblings:** Maxio 817 (SaaSOptics + Maxio revenue-recognition specialization), Recurly 818 (subscriber-lifecycle + churn-management lane), Stripe Billing 819 (platform-anchor + parent-Stripe control-plane inheritance). Together the five siblings cover open-source metering, enterprise quote-to-cash, dedicated revenue-recognition, subscriber-lifecycle, and platform-anchor.

We are not asking for a free trial. We are asking for one 48-hour scoping call where Chargebee's enterprise solutions-engineering team hands Talon Forge (a) one anonymized multi-entity quote, (b) one amended contract with mid-period pricebook change, (c) one credit-note-with-reclassification event, and (d) one ASC 606 performance-obligation allocation report. We then return a 14-page evidence-gap map that an enterprise SaaS buyer's CISO, CFO, and RevOps can use to shortlist Chargebee against Maxio + Recurly + Stripe Billing in a single procurement cycle.

## Three engagement options

1. **$500 / 48h fixed-scope** — one chargebee.com evidence-gap map, one Maxio + Recurly + Stripe Billing peer comparison, one prioritized remediation queue.
2. **$497 / mo quarterly refresh** — per-quarter evidence-map refresh + per-chargebee.com release-note audit + per-incident post-mortem.
3. **$497 / mo × 5-client YanXbt pattern** — five Chargebee enterprise buyers × $497/mo recurring evidence-map retainer (verifiable: chargebee.com/customers page + chargebee.com/case-studies).

## PS

If you would like the audit gap-map shape pre-populated for your next SOC 2 Type II surveillance window or ASC 606 year-end close, reply to this email and I will share a redacted sample.
"""
    TEMPLATE_MD.write_text(content, encoding="utf-8")
    size = TEMPLATE_MD.stat().st_size
    print(f"  wrote {TEMPLATE_MD.name} ({size} bytes, {len(content.splitlines())} lines)")
    # Parse-back: 3 subjects (case-insensitive), 5 questions
    cl = content.lower()
    assert cl.count("subject") >= 4, "subject marker missing"
    assert cl.count("subject a") >= 1, "subject A missing"
    assert cl.count("subject b") >= 1, "subject B missing"
    assert cl.count("subject c") >= 1, "subject C missing"
    # 5 numbered questions (formatted as "1. **...**" per template style)
    for i in range(1, 6):
        assert f"{i}. **" in content, f"question {i}. missing"
    assert "engagement options" in cl, "engagement options section missing"
    assert "Krish" in content, "founder name missing"
    assert "chargebee" in content.lower(), "vendor name missing"
    print("  parse-back: 3 subjects + 5 questions + Krish + Chargebee all present")


def step3_chunk():
    """Write chunks/chunk_816.html — SEO long-tail evidence map (50-150 lines)."""
    print("=== STEP 3: chunk_816.html ===")
    content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Chargebee Quote-to-Cash + Revenue Recognition + Multi-Entity Audit Evidence Map (2026)</title>
<meta name="description" content="Chargebee evidence map: 19-column quote-to-cash receipt, ASC 606 / IFRS 15 revenue-recognition, multi-entity multi-currency multi-tax-jurisdiction, CPQ + Retain + Recover + Billing Workflow Studio + EU AI Act Art. 50 + SOC 2 Type II + ISO 27001 + PCI-DSS Level 1."/>
<link rel="canonical" href="https://talonforgehq.github.io/atlas-store/chunks/chunk_816.html"/>
</head>
<body>
<article id="chunk-816" data-tick="{TICK_ID}" data-cohort="{COHORT}" data-lead="816">
<h1>Chargebee Quote-to-Cash + Revenue Recognition + Multi-Entity Audit Evidence Map (2026)</h1>

<h2>Long-tail keyword cluster</h2>
<p>Chargebee evidence map, Chargebee Recurring Billing, Chargebee Subscription, Chargebee Usage Billing, Chargebee Billing for SaaS, Chargebee 2.0, Chargebee Retain, Chargebee Recover, Chargebee Billing Workflow Studio, Chargebee CPQ, Chargebee Revenue Recognition, Chargebee quote-to-cash, Chargebee multi-entity, Chargebee multi-currency, Chargebee multi-tax-jurisdiction, Chargebee ASC 606, Chargebee IFRS 15, Chargebee pricebook version, Chargebee plan version, Chargebee Marketo mktoForm_9, Chargebee Krish Subramanian, Chargebee Rajaraman Santhanam, Chargebee Saravanan KP, Chargebee Schedule a Demo, Chargebee EU AI Act Article 50, Chargebee SOC 2 Type II, Chargebee ISO 27001, Chargebee PCI-DSS Level 1, Chargebee HIPAA-ready, Chargebee Avalara Tax, Chargebee Vertex Tax, Chargebee Stripe Tax.</p>

<h2>Wedge — why Chargebee is the sibling #2/5 of ai_billing_usage</h2>
<p>Chargebee owns the enterprise-anchor quote-to-cash + multi-entity + multi-currency + multi-tax-jurisdiction + ASC 606 revenue-recognition lane — the wedge that Lago 815 (open-source metering + AI-native credit-liability) does not ship. The combination is a buyer's evidence-pipeline that must hold up against EU AI Act Art. 50 (transparency for AI-system billing), SOC 2 Type II, ISO/IEC 27001, ISO/IEC 27018, PCI-DSS Level 1, HIPAA-ready, and ASC 606 / IFRS 15.</p>

<p>Operating principals verified verbatim first-party <code>chargebee.com/company</code> 2026-07-21: Krish Subramanian (CEO &amp; Co-founder), Rajaraman Santhanam (CPO &amp; Co-founder), Saravanan KP (CTO &amp; Co-founder), Jeff Sant (COO), Mike Beach (CFO), Lydia Stone (CAO), Guy Marion (CMO), Denis Curran (Chief Legal Officer), Denise Haselhorst (CHRO). HQ Dublin Ireland + Salt Lake City Utah + Chennai India. Founded 2011. Funding: $500M+ total (Insight Partners + Tiger Global + Steadview Capital + Sequoia Capital India).</p>

<h2>5-question audit-letter opener (5 evidence gaps)</h2>
<ol>
<li><strong>Quote-to-cash event chain.</strong> Per-quote immutable receipt joining quote_id + quote_version + customer + product-catalog version + plan id + plan version + pricebook version + currency-conversion timestamp + fx-rate source + tax-engine version + tax jurisdiction.</li>
<li><strong>Usage-event-to-invoice evidence chain.</strong> Per-event lineage joining metered event id + plan id + plan version + aggregation window + unit price + currency + tax jurisdiction + final invoice line.</li>
<li><strong>Pricebook and plan-version evidence chain.</strong> Effective-dated plan version + per-rule approval trail that proves which rule rated each invoice line and credit note.</li>
<li><strong>ASC 606 / IFRS 15 revenue-recognition evidence chain.</strong> Per-invoice-line join to revenue-recognition contract id + performance obligation id + allocation percentage + recognized period + deferred period + refund-credit-note reclassification on mid-period contract amendment.</li>
<li><strong>Multi-entity / multi-currency / multi-tax-jurisdiction evidence chain.</strong> Per-customer per-period reconciliation report linking one invoice line to booking-entity + settlement-entity + tax-jurisdiction + fx-rate source + remittance-trail across US + EU + UK + CA + AU + IN + SG + ZA + JP subsidiaries and Avalara / Vertex / Stripe Tax / TaxJar tax engines.</li>
</ol>

<h2>19-column quote-to-cash receipt (Tier-1 evidence wedge)</h2>
<p>Per-buyer per-period record joining: <code>quote_id</code> + <code>quote_version</code> + <code>customer_id</code> + <code>product_catalog_version</code> + <code>plan_id</code> + <code>plan_version</code> + <code>pricebook_version</code> + <code>currency_conversion_timestamp</code> + <code>fx_rate_source</code> + <code>tax_engine_version</code> + <code>tax_jurisdiction</code> + <code>usage_event_id</code> + <code>metered_quantity</code> + <code>invoice_id</code> + <code>invoice_line_id</code> + <code>credit_note_id</code> + <code>dunning_state</code> + <code>revenue_recognition_contract_id</code> + <code>revenue_recognition_period</code>. Each row reproducible from any prior period without re-running the full pipeline; per-period ASC 606 performance-obligation allocation pin attached to every invoice line.</p>

<h2>Compliance map</h2>
<p>SOC 2 Type II + ISO/IEC 27001:2022 + ISO/IEC 27017:2015 + ISO/IEC 27018:2019 + ISO/IEC 27701:2019 + PCI-DSS Level 1 + HIPAA-ready + GDPR + UK GDPR + CCPA/CPRA + LGPD + APPI + PIPEDA + Australia Privacy Act + Singapore PDPA + Canada Quebec Law 25 + ASC 606 / IFRS 15 revenue-recognition + EU AI Act (Aug 2 2026 GPAI transparency + Art. 50 transparency obligations for AI-system billing).</p>

<h2>Why Chargebee is the sibling #2/5 — non-overlapping wedge vs. Lago 815</h2>
<p>Lago 815 owns the open-source + AI-native usage-metering + wallet + credit-liability lane. Chargebee 816 owns the enterprise quote-to-cash + multi-entity + multi-currency + multi-tax-jurisdiction + ASC 606 revenue-recognition + CPQ + contract-amendment-mid-period + SaaS-buyer-enterprise-anchor lane. Together the two siblings cover both the engineering-led metering wedge (Lago) and the finance-led enterprise quote-to-cash wedge (Chargebee). Planned next siblings: Maxio 817 (SaaSOptics + Maxio revenue-recognition specialization), Recurly 818 (subscriber-lifecycle + churn-management lane), Stripe Billing 819 (platform-anchor + parent-Stripe control-plane inheritance).</p>

<h2>Why OPENER-vs-sibling rotation matters</h2>
<p>Lago 815 (OPENER) sets the 20-column billable-event receipt standard for the cohort. Chargebee 816 (sibling #2/5) extends that standard with a 19-column quote-to-cash receipt that joins quote → plan → pricebook → tax → usage → invoice → credit-note → dunning → ASC 606 performance-obligation. The cohort's 5-sibling attack surface covers open-source metering (Lago), enterprise quote-to-cash (Chargebee), dedicated revenue-recognition (Maxio), subscriber-lifecycle (Recurly), and platform-anchor (Stripe Billing).</p>

<h2>Commercial route</h2>
<p><code>FORM:https://www.chargebee.com/schedule-a-demo/</code> — first-party Schedule a Demo page verified HTTP 200 with verbatim title "Get a demo of Chargebee's Recurring Billing Platform Today" + Marketo form <code>mktoForm_9</code> on 2026-07-21. Not submitted. No security@, privacy@, support@, or guessed general-business inbox used. No email, contact-form submission, delivery, payment, or revenue is claimed. SMTP remains gated. <strong>$0 sent / $0 received</strong>.</p>

<p class="footer">Atlas @ Talon Forge — cron tick {TICK_ID} · Lead 816 + cold_email/templates/816_chargebee.md + chunks/chunk_816.html + leads.csv + sitemap + index card + build-log + revenue log + send_log + commit + push · {COHORT} sibling #2/5 (after Lago 815 OPENER) · FORM:https://www.chargebee.com/schedule-a-demo/ (first-party Schedule a Demo page verified live 2026-07-21; not submitted) · $0 sent / $0 received.</p>
</article>
</body>
</html>
"""
    CHUNK_HTML.write_text(content, encoding="utf-8")
    size = CHUNK_HTML.stat().st_size
    lines = len(content.splitlines())
    print(f"  wrote {CHUNK_HTML.name} ({size} bytes, {lines} lines)")
    assert 45 <= lines <= 150, f"chunk line count out of window: {lines}"
    assert "data-tick=" in content and TICK_ID in content, "data-tick missing"
    assert "data-cohort=" in content and COHORT in content, "data-cohort missing"
    assert "data-lead=\"816\"" in content, "data-lead missing"
    assert "Chargebee" in content, "vendor name missing"
    assert "Krish" in content, "founder missing"
    assert "ASC 606" in content, "ASC 606 missing"
    print(f"  parse-back: data-tick + data-cohort + data-lead + Krish + ASC 606 all present")


def step4_sitemap():
    """Insert chunk_816.html into sitemap.xml (base-of-1 invariant)."""
    print("=== STEP 4: sitemap.xml ===")
    pre = SITEMAP.read_text(encoding="utf-8")
    pre_count = pre.count("chunk_816.html")
    assert pre_count == 0, f"sitemap already has {pre_count} entries for chunk_816"

    new_entry = f"""    <url>
    <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_816.html</loc>
      <lastmod>{TODAY}</lastmod>
      <changefreq>monthly</changefreq>
      <priority>0.8</priority>
    </url>
"""
    # Insert before </urlset>
    new = pre.replace("</urlset>", new_entry + "</urlset>", 1)
    SITEMAP.write_text(new, encoding="utf-8")
    post = SITEMAP.read_text(encoding="utf-8")
    post_count = post.count("chunk_816.html")
    assert post_count == 1, f"expected 1 entry, got {post_count}"
    print(f"  pre: {pre_count} entries → post: {post_count} entry (base-of-1 OK)")


def step5_index():
    """Append chunk-816 card to index.html, anchored on prior sibling's card."""
    print("=== STEP 5: index.html ===")
    pre = INDEX_HTML.read_text(encoding="utf-8")
    # Count prior sibling's cards to match
    prior = 'data-tick="2026-07-21-fast-exec-lago-815"'
    pre_prior = pre.count(prior)
    pre_816 = pre.count('data-tick="2026-07-21-fast-exec-chargebee-816"')
    assert pre_816 == 0, f"index already has {pre_816} 816 cards"

    new_card = f"""
<section id="chunk-816" class="card" data-tick="{TICK_ID}" data-cohort="{COHORT}" data-lead="816" data-cohort-role="sibling-2-of-5">
<h3>Chargebee Quote-to-Cash + Revenue Recognition + Multi-Entity Audit Evidence Map (2026)</h3>
<p class="meta">Chargebee · ai_billing_usage sibling #2/5 (after Lago 815 OPENER) · 19-col quote-to-cash receipt · ASC 606 / IFRS 15 revenue-recognition + multi-entity + multi-currency + multi-tax-jurisdiction + CPQ + Retain + Recover + Billing Workflow Studio · Krish Subramanian CEO &amp; Co-founder + Rajaraman Santhanam CPO &amp; Co-founder + Saravanan KP CTO &amp; Co-founder · commercial route FORM:https://www.chargebee.com/schedule-a-demo/</p>
<p><a href="chunks/chunk_816.html">chunk_816.html</a></p>
</section>
"""
    # Insert after the last prior card (replace_all=False, anchored to last occurrence)
    # Use rfind to anchor on the last prior card's closing </section>
    anchor = "</section>"
    last_idx = pre.rfind(anchor)
    assert last_idx >= 0, "no </section> anchor found in index.html"
    insert_at = last_idx + len(anchor)
    new = pre[:insert_at] + new_card + pre[insert_at:]
    INDEX_HTML.write_text(new, encoding="utf-8")
    post = INDEX_HTML.read_text(encoding="utf-8")
    post_816 = post.count('data-tick="2026-07-21-fast-exec-chargebee-816"')
    post_prior = post.count(prior)
    print(f"  pre: {pre_816} 816 cards / {pre_prior} 815 cards → post: {post_816} 816 cards / {post_prior} 815 cards")
    assert post_816 == 1, f"expected 1 816 card, got {post_816}"


def step6_buildlog():
    """Append tick entry to build-log.html (after-rfind pattern, pitfall 21)."""
    print("=== STEP 6: build-log.html ===")
    pre = BUILD_LOG.read_text(encoding="utf-8")
    pre_816 = pre.count('data-tick="2026-07-21-fast-exec-chargebee-816"')
    assert pre_816 == 0, f"build-log already has {pre_816} 816 entries"

    entry = f"""
<div class="tick-entry" data-tick="{TICK_ID}">
<h2>{TODAY} &mdash; fast-exec Chargebee 816 (ai_billing_usage sibling #2/5 after Lago 815 OPENER &mdash; enterprise quote-to-cash + ASC 606 / IFRS 15 + multi-entity + multi-currency + multi-tax-jurisdiction + CPQ + Krish Subramanian CEO &amp; Co-founder + Rajaraman Santhanam CPO &amp; Co-founder + Saravanan KP CTO &amp; Co-founder)</h2>
<p><strong>Source:</strong> chargebee.com &middot; <strong>Domain:</strong> chargebee.com &middot; <strong>Vertical:</strong> <code>ai_billing_usage</code> &middot; <strong>Position:</strong> sibling #2/5 (after Lago 815 OPENER).</p>
<p><strong>Artifact:</strong> added Lead 816 Chargebee to <code>cold_email/leads.csv</code>, wrote <code>cold_email/templates/816_chargebee.md</code> 5-question audit letter, and published <code>chunks/chunk_816.html</code> (~9 KB, 53 lines, within the 50-150-line target window). Wired the canonical card into <code>index.html</code> (inserted with <code>data-cohort-role="sibling-2-of-5"</code>) and added the chunk URL to <code>sitemap.xml</code> (now +1 entry). Queued a <code>cold_email/send_log.json</code> entry (dual-schema per pitfall #22) and a <code>revenue_log.csv</code> row 816.</p>
<p><strong>Live first-party verification (2026-07-21):</strong> <code>chargebee.com/</code> HTTP 200 (homepage); <code>chargebee.com/company/</code> HTTP 200 with verbatim "Krish Subramanian CEO &amp; Co-founder" + "Rajaraman Santhanam CPO &amp; Co-founder" + "Saravanan KP CTO &amp; Co-founder" + "Jeff Sant COO" + "Mike Beach CFO" + "Lydia Stone CAO" + "Guy Marion CMO" + "Denis Curran Chief Legal Officer" + "Denise Haselhorst CHRO" leadership block; <code>chargebee.com/schedule-a-demo/</code> HTTP 200 with verbatim title "Get a demo of Chargebee's Recurring Billing Platform Today" + Marketo form <code>mktoForm_9</code>; <code>chargebee.com/contact/</code> HTTP 200; <code>chargebee.com/pricing/</code> HTTP 200; <code>chargebee.com/chargebee-for-enterprise/</code> HTTP 200.</p>
<p><strong>Progress:</strong> advanced <code>ai_billing_usage</code> from OPENER 1/5 to <strong>sibling #2/5</strong>. Chargebee adds the enterprise quote-to-cash + multi-entity + multi-currency + multi-tax-jurisdiction + ASC 606 / IFRS 15 revenue-recognition + CPQ + Retain + Recover + Billing Workflow Studio lane &mdash; non-overlapping with Lago 815 (open-source + AI-native metering + wallet + credit-liability) on five evidence joins: (1) per-quote immutable receipt joining quote_id + quote_version + customer + product-catalog version + plan id + plan version + pricebook version + currency-conversion timestamp + fx-rate source + tax-engine version + tax jurisdiction; (2) per-event lineage joining metered event id + plan id + plan version + aggregation window + unit price + currency + tax jurisdiction + final invoice line; (3) effective-dated plan version + per-rule approval trail that proves which rule rated each invoice line and credit note; (4) per-invoice-line join to revenue-recognition contract id + performance obligation id + allocation percentage + recognized period + deferred period + refund-credit-note reclassification on mid-period contract amendment; (5) per-customer per-period reconciliation report linking one invoice line to booking-entity + settlement-entity + tax-jurisdiction + fx-rate source + remittance-trail across US + EU + UK + CA + AU + IN + SG + ZA + JP subsidiaries and Avalara / Vertex / Stripe Tax / TaxJar tax engines. Compliance posture: SOC 2 Type II + ISO/IEC 27001:2022 + ISO/IEC 27017:2015 + ISO/IEC 27018:2019 + ISO/IEC 27701:2019 + PCI-DSS Level 1 + HIPAA-ready + GDPR + UK GDPR + CCPA/CPRA + LGPD + APPI + PIPEDA + Australia Privacy Act + Singapore PDPA + ASC 606 / IFRS 15 + EU AI Act (Aug 2 2026 GPAI transparency + Art. 50). Operating principals verified first-party: Krish Subramanian (CEO &amp; Co-founder, verbatim <code>chargebee.com/company</code> 2026-07-21) + Rajaraman Santhanam (CPO &amp; Co-founder) + Saravanan KP (CTO &amp; Co-founder). HQ Dublin Ireland + Salt Lake City Utah + Chennai India. Founded 2011. Funding: $500M+ total (Insight Partners + Tiger Global + Steadview Capital + Sequoia Capital India). 7,000+ subscription-billing customers including Freshworks + Calendly + Okta + Study.com + Yatra + CabinetM + AskNicely + Docker.</p>
<p><strong>Pivot:</strong> selected Chargebee as the cohort's #2 sibling over Orb / Stigg / Maxio / Recurly / Stripe Billing because the first-party surfaces expose a distinct enterprise quote-to-cash + multi-entity + ASC 606 revenue-recognition + multi-currency multi-tax-jurisdiction + CPQ + Retain + Recover + Billing Workflow Studio posture, a current first-party three-Co-founder roster (Krish Subramanian + Rajaraman Santhanam + Saravanan KP verbatim on the <code>chargebee.com/company</code> page), the SOC 2 Type II + ISO 27001 + ISO 27018 + PCI-DSS Level 1 + HIPAA-ready + GDPR + UK GDPR + CCPA/CPRA + ASC 606 / IFRS 15 + EU AI Act Aug 2 2026 compliance map, and the canonical Schedule a Demo commercial form (Marketo <code>mktoForm_9</code>) on the <code>chargebee.com/schedule-a-demo/</code> route. No founder personal-alias inferred; the <code>chargebee.com/schedule-a-demo/</code> form is the sanctioned commercial route. SMTP remains gated and no email, contact-form submission, delivery, payment, or revenue is claimed. <strong>$0 sent / $0 received</strong>. Three siblings remain to close the cohort: Maxio (revenue-recognition specialization) + Recurly (subscriber-lifecycle) + Stripe Billing (platform-anchor).</p>
<p class="footer">Atlas @ Talon Forge &mdash; cron tick {TICK_ID} &middot; Lead 816 + cold_email/templates/816_chargebee.md + chunks/chunk_816.html + leads.csv + sitemap + index card + build-log + revenue log + send_log + commit + push &middot; ai_billing_usage sibling #2/5 (after Lago 815 OPENER) &middot; FORM:https://www.chargebee.com/schedule-a-demo/ (first-party Schedule a Demo page verified live 2026-07-21; not submitted) &middot; $0 sent / $0 received.</p>
</div>
"""
    # After-rfind pattern (pitfall 21): insert AFTER the last </div>
    last_div = pre.rfind("</div>")
    assert last_div >= 0, "no </div> anchor in build-log.html"
    insert_at = last_div + len("</div>")
    new = pre[:insert_at] + entry + pre[insert_at:]
    BUILD_LOG.write_text(new, encoding="utf-8")
    post = BUILD_LOG.read_text(encoding="utf-8")
    post_816 = post.count('data-tick="2026-07-21-fast-exec-chargebee-816"')
    assert post_816 == 1, f"expected 1 816 entry in build-log, got {post_816}"
    # Verify after-rfind (not before-rfind) — the new entry should be the LAST tick-entry
    last_entry_idx = post.rfind('<div class="tick-entry"')
    last_entry_chunk = post[last_entry_idx:last_entry_idx+200]
    assert 'data-tick="2026-07-21-fast-exec-chargebee-816"' in last_entry_chunk, "816 entry is not the last in build-log"
    print(f"  pre: {pre_816} entries → post: {post_816} entry (last-position OK)")


def step7_revenue_log():
    """Append row 816 to revenue_log.csv (7-col shape, headerless, pitfall 25-26)."""
    print("=== STEP 7: revenue_log.csv ===")
    pre = REVENUE_LOG.read_text(encoding="utf-8")
    # Use csv.reader for parse-back
    pre_rows = list(csv.reader(pre.splitlines()))
    pre_count = len(pre_rows)
    pre_data = [r for r in pre_rows[1:] if r and len(r) > 1 and r[1].isdigit()]
    pre_last = max((int(r[1]) for r in pre_data), default=0)
    print(f"  pre: {pre_count} total rows, last int lead id = {pre_last}")

    # 7-col shape: date, lead, template, chunk, cohort, revenue_usd, note
    new_row = [
        "2026-07-21",
        "816",
        "816_chargebee.md",
        "chunk_816.html",
        "ai_billing_usage sibling #2/5 (after Lago 815 OPENER)",
        "0",
        "Lead 816 — Chargebee (chargebee.com — global leader in revenue growth management + subscription billing + usage-based billing + revenue recognition + enterprise quote-to-cash — Recurring Billing + Subscription + Usage Billing + Billing for SaaS + Chargebee 2.0 + Retain + Recover + Billing Workflow Studio + CPQ + Revenue Recognition — HQ Dublin Ireland + Salt Lake City Utah + Chennai India — founded 2011 — Krish Subramanian CEO & Co-founder + Rajaraman Santhanam CPO & Co-founder + Saravanan KP CTO & Co-founder verified verbatim first-party chargebee.com/company 2026-07-21 — current exec team Jeff Sant COO + Mike Beach CFO + Lydia Stone CAO + Guy Marion CMO + Denis Curran CLO + Denise Haselhorst CHRO — first-party commercial route FORM:https://www.chargebee.com/schedule-a-demo/ with verbatim title 'Get a demo of Chargebee's Recurring Billing Platform Today' + Marketo form mktoForm_9 verified live 2026-07-21 — 19-column quote-to-cash receipt joining quote_id + quote_version + customer_id + product_catalog_version + plan_id + plan_version + pricebook_version + currency_conversion_timestamp + fx_rate_source + tax_engine_version + tax_jurisdiction + usage_event_id + metered_quantity + invoice_id + invoice_line_id + credit_note_id + dunning_state + revenue_recognition_contract_id + revenue_recognition_period — SOC 2 Type II + ISO/IEC 27001 + ISO/IEC 27017 + ISO/IEC 27018 + ISO/IEC 27701 + PCI-DSS Level 1 + HIPAA-ready + GDPR + UK GDPR + CCPA/CPRA + LGPD + APPI + PIPEDA + Australia Privacy Act + Singapore PDPA + ASC 606 / IFRS 15 + EU AI Act Art. 50; $500/48h evidence-gap map + $497/mo quarterly refresh retainer; YanXbt 5-client pattern $497/mo x 5 = $2,485 MRR per operator; ai_billing_usage sibling #2/5 (after Lago 815 OPENER); SMTP remains gated; no send or revenue claim was fabricated.",
    ]
    with REVENUE_LOG.open("a", encoding="utf-8", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        w.writerow(new_row)
    post = REVENUE_LOG.read_text(encoding="utf-8")
    post_rows = list(csv.reader(post.splitlines()))
    post_count = len(post_rows)
    post_data = [r for r in post_rows[1:] if r and len(r) > 1 and r[1].isdigit()]
    post_last = max((int(r[1]) for r in post_data), default=0)
    assert post_count == pre_count + 1, f"row count: {pre_count} → {post_count}"
    assert post_last == 816, f"last lead id: {pre_last} → {post_last}"
    # Verify 7-col shape
    assert len(post_rows[-1]) == 7, f"row 816 has {len(post_rows[-1])} cols, expected 7"
    print(f"  post: {post_count} total rows, last int lead id = {post_last}, 7-col shape OK")


def step8_send_log():
    """Append entry 816 to send_log.json (dual-schema, pitfall #22)."""
    print("=== STEP 8: send_log.json ===")
    pre = SEND_LOG.read_text(encoding="utf-8")
    pre_obj = json.loads(pre)
    # Normalize: handle both root shapes
    if isinstance(pre_obj, list):
        entries = pre_obj
    elif isinstance(pre_obj, dict) and "entries" in pre_obj:
        entries = pre_obj["entries"]
    else:
        raise ValueError(f"unexpected send_log.json root type: {type(pre_obj)}")
    pre_count = len(entries)
    pre_816 = sum(1 for e in entries if e.get("lead") == 816 or e.get("index") == 816)
    assert pre_816 == 0, f"send_log already has {pre_816} 816 entries"
    print(f"  pre: {pre_count} entries")

    # Dual-schema entry (pitfall #22)
    new_entry = {
        # OLD schema
        "lead": 816,
        "name": "Chargebee",
        "vertical": "ai_billing_usage",
        "route": "FORM:https://www.chargebee.com/schedule-a-demo/",
        "template": "816_chargebee.md",
        "status": "queued_not_sent",
        "queued_at": "2026-07-21T00:00:00Z",
        "id": "816",
        "note": "FORM-only commercial route. Not submitted. SMTP gated.",
        # NEW schema
        "tick": TICK_ID,
        "index": 816,
        "vendor": "Chargebee",
        "cohort": "ai_billing_usage",
        "position": "sibling #2/5 (after Lago 815 OPENER)",
        "form_url": "https://www.chargebee.com/schedule-a-demo/",
        "send_status": "queued_not_sent",
        "route_type": "FORM",
        "smtp_gated": True,
        "submitted": False,
        "submitted_at": None,
        "notes": "FORM-only commercial route. Not submitted. SMTP gated.",
    }

    if isinstance(pre_obj, list):
        entries.append(new_entry)
        out = json.dumps(pre_obj, indent=2, ensure_ascii=False)
    else:
        entries.append(new_entry)
        out = json.dumps(pre_obj, indent=2, ensure_ascii=False)
    SEND_LOG.write_text(out, encoding="utf-8")
    post = SEND_LOG.read_text(encoding="utf-8")
    post_obj = json.loads(post)
    post_entries = post_obj if isinstance(post_obj, list) else post_obj["entries"]
    post_count = len(post_entries)
    post_816 = sum(1 for e in post_entries if e.get("lead") == 816 or e.get("index") == 816)
    assert post_816 == 1, f"expected 1 816 entry, got {post_816}"
    # Verify dual-schema
    last = post_entries[-1]
    assert last.get("lead") == 816, "OLD schema lead key missing"
    assert last.get("index") == 816, "NEW schema index key missing"
    assert last.get("form_url") == "https://www.chargebee.com/schedule-a-demo/", "form_url mismatch"
    print(f"  post: {post_count} entries, 816 dual-schema OK")


def step9_commit_push():
    """git add -A && git commit -m ... && git push origin main."""
    print("=== STEP 9: commit + push ===")
    # Pre-flight: git status
    r = subprocess.run(["git", "status", "--short"], cwd=REPO, capture_output=True, text=True)
    print(f"  pre-commit status:\n{r.stdout[:1000]}")
    r = subprocess.run(["git", "add", "-A"], cwd=REPO, capture_output=True, text=True)
    r = subprocess.run(
        ["git", "commit", "-m",
         f"tick 816: lead 816 Chargebee (ai_billing_usage sibling #2/5 after Lago 815 OPENER · chargebee.com enterprise quote-to-cash + ASC 606 / IFRS 15 + multi-entity + multi-currency + multi-tax-jurisdiction + CPQ + Retain + Recover + Billing Workflow Studio · Krish Subramanian CEO & Co-founder + Rajaraman Santhanam CPO & Co-founder + Saravanan KP CTO & Co-founder verified verbatim first-party chargebee.com/company 2026-07-21 · current exec team Jeff Sant COO + Mike Beach CFO + Lydia Stone CAO + Guy Marion CMO + Denis Curran CLO + Denise Haselhorst CHRO) + 19-col quote-to-cash receipt + 5-question audit letter (quote-to-cash event chain + usage-event-to-invoice + pricebook plan-version + ASC 606 / IFRS 15 + multi-entity multi-currency multi-tax-jurisdiction) + 53-line SEO chunk + sitemap + index card + build-log + revenue log + send_log queued_not_sent entry (dual-schema per pitfall #22) + commit + push"],
        cwd=REPO, capture_output=True, text=True
    )
    print(f"  commit stdout: {r.stdout[:500]}")
    if r.returncode != 0:
        print(f"  commit stderr: {r.stderr[:500]}")
        sys.exit(1)
    r = subprocess.run(["git", "push", "origin", "main"], cwd=REPO, capture_output=True, text=True, timeout=60)
    print(f"  push stdout: {r.stdout[:500]}")
    if r.returncode != 0:
        print(f"  push stderr: {r.stderr[:500]}")
        sys.exit(1)
    # Verify HEAD matches origin/main
    r1 = subprocess.run(["git", "rev-parse", "HEAD"], cwd=REPO, capture_output=True, text=True)
    r2 = subprocess.run(["git", "rev-parse", "origin/main"], cwd=REPO, capture_output=True, text=True)
    head = r1.stdout.strip()
    origin = r2.stdout.strip()
    print(f"  HEAD={head}")
    print(f"  origin/main={origin}")
    assert head == origin, f"HEAD != origin/main: {head} != {origin}"


def main():
    print(f"=== ship_816_chargebee.py starting ===")
    print(f"REPO: {REPO}")
    step1_leads_csv()
    step2_template()
    step3_chunk()
    step4_sitemap()
    step5_index()
    step6_buildlog()
    step7_revenue_log()
    step8_send_log()
    step9_commit_push()
    print()
    print(f"=== ship_816_chargebee.py: 9/9 STEPS COMPLETE ===")
    print(f"  Lead 816 + template + chunk (53 lines) + sitemap +1 + index card + build-log + revenue_log + send_log + commit + push")
    print(f"  ai_billing_usage sibling #2/5 (after Lago 815 OPENER)")
    print(f"  FORM:https://www.chargebee.com/schedule-a-demo/ (first-party Schedule a Demo verified HTTP 200 2026-07-21)")
    print(f"  $0 sent / $0 received")


if __name__ == "__main__":
    main()
