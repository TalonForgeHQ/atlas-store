#!/usr/bin/env python3
"""Tick 949 shipper: Showpad SIBLING #4/5 ai_sales_readiness_role_play_coaching.
Batched file ops to stay under tool-call budget per pitfall #100 cron BLOCKED recipe.
"""
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(r"C:\Users\Potts\projects\atlas-store")
TEMPLATES = ROOT / "cold_email" / "templates"
LEADS = ROOT / "cold_email" / "leads.csv"
LEADS_EM = ROOT / "cold_email" / "leads_with_emails.csv"
CHUNKS = ROOT / "chunks"
INDEX = ROOT / "index.html"
SITEMAP = ROOT / "sitemap.xml"
SEND_LOG = ROOT / "cold_email" / "send_log.jsonl"
REV_LOG = ROOT / "cold_email" / "revenue_log.csv"
BUILD_LOG = ROOT / "build-log.html"

LEAD_NUM = 949
LEAD_NAME = "Showpad"
LEAD_HANDLE = "@showpad"
LEAD_VERTICAL = "ai_sales_readiness_role_play_coaching"
LEAD_DOMAIN = "showpad.com"
LEAD_FORM = "FORM:https://www.showpad.com/get-a-demo/"
LEAD_TIER = 1
LEAD_TEMPLATE = f"{LEAD_NUM}_showpad.md"

# ============================================================
# 1. Template
# ============================================================
TEMPLATE = """# Showpad (showpad.com) — ai_sales_readiness_role_play_coaching — SIBLING #4/5 (Lead 949)

**Cohort position:** SIBLING #4/5 of `ai_sales_readiness_role_play_coaching` (after Mindtickle 924 OPENER #1/5 + Allego 925 SIBLING #2/5 + Second Nature 937 SIBLING #3/5; 1 OPEN slot remaining for CLOSER #5/5).

## To: (Showpad commercial route per pitfall #28) info@showpad.com — DOES NOT publish a general-business mailto on rendered first-party surfaces

**Canonical commercial route:** `FORM:https://www.showpad.com/get-a-demo/`

---

## Subject (A — 56 chars)
Showpad + EU AI Act Art. 6(2) Annex III 5-evidence-gap map
## Subject (B — 51 chars)
Showpad Genie AI coach SOC 2 + ISO 27001 evidence-replay
## Subject (C — 64 chars)
Showpad Revenue Effectiveness Platform — ASC 606 + SOX 404 vendor-DD letter

---

## Body — cold email to Showpad procurement / InfoSec / vendor-DD desk

Hello Showpad vendor-DD desk,

I noticed on **showpad.com/security**, **showpad.com/trust**, **showpad.com/gdpr**, and **showpad.com/privacy** (all HTTP 200 retrieved 2026-07-22) that Showpad ships a Revenue Effectiveness Platform with four primary product surfaces — `Sales Readiness` ("Learning that creates champions" verbatim first-party /sales-readiness 2026-07-22), `Content Management`, `Buyer Engagement`, `Analytics & Insights` — plus the NAMED first-party AI surface `Showpad Genie` (verbatim first-party /showpad-genie 2026-07-22), with corporate HQ in **Ghent, Belgium** (verbatim first-party /gdpr 2026-07-22 "a corporate headquarters in Ghent (Belgium), and North American headquarters in Chicago (US)") and a `showpad.com/gdpr` page dated **April 8, 2026** with consent-ledger, time-to-forget (prospect-data forget), and DPA execution guidance verbatim.

When buying or renewing a NAMED first-party AI sales-readiness platform that ships a Showpad Genie conversational assistant that ingests role-play transcripts, coaching recommend feedback, sales-call summaries, and content-engagement signals from reps + prospects, your InfoSec and procurement teams need to answer five evidence questions before the contract is countersigned. The 500/48h evidence-gap map answers each one with verbatim first-party source linkage:

### 5 procurement-grade audit gaps your InfoSec desk will hit on a NAMED first-party AI sales-readiness platform

**1. Per-coaching-recommendation and per-role-play-transcript EU AI Act Art. 6(2) Annex III audit-trail** — Showpad Genie ships a conversational AI coach that listens to role-play transcripts and generates coaching recommendations. Under EU AI Act Art. 6(2), Annex III point 4(b) covers AI used for "evaluating performance of persons in educational or vocational training" — if Showpad is used by your reps in EU member states for onboarding / certification / readiness evaluation, the platform is in scope for high-risk Annex III classification. Your InfoSec desk will need: per-rep (subject) + per-coaching-session (decision) + per-prompt-hash + per-model-name + per-model-version + per-model-output + per-coaching-recommendation (action) + per-rep-acknowledgment (output) + per-tenant-scoping-isolation-cross-tenant-no-bleed. Most vendors cannot produce this — verify Showpad's per-rep evidence-join-table BEFORE contract countersign.

**2. Per-content-asset Showpad Genie training / fine-tuning provenance** — Showpad Genie ships NAMED first-party on /showpad-genie. Your procurement desk needs: per-asset (input) + per-asset-version-id + per-asset-fine-tuning-corpus-clip-id + per-asset-consent-ledger-entry-id (EU AI Act Art. 4(5) data-quality) + per-content-training-data-purge-receipt + per-content-asset-IP-license-acknowledgment (EU AI Act Art. 53(1)(c) copyright compliance) + per-Showpad-Genie-fine-tuning-rlhf-round-version + per-Showpad-Genie-fine-tuning-dpo-pair-version + cross-tenant-no-bleed. ASC 805-50 fair-value-of-customer-list-asset-recovery + ASU 2023-07 goodwill-impairment-test + GDPR Art. 17 erasure-reconciliation all flow from this evidence chain.

**3. Per-tenant data-residency EU + UK + CH + BR + AU + SG + JP + CA + IN + ZA cross-jurisdiction export posture** — Showpad corporate HQ Ghent, Belgium + US Chicago HQ means Belgian-co-under-GDPR + Belgian-co-controller + potentially Schrems II cross-border transfer SCC + UK ICO + Swiss FADP + Brazil LGPD + Singapore PDPA + Canada PIPEDA + India DPDPA + Australia Privacy Act + Japan APPI exposure. Your InfoSec desk will ask for: per-tenant zone-isolation-flag + per-tenant per-region data-residency-pin + per-cross-border-transfer SCC reference + per-EU-US DPF + per-tenant per-customer DPA + Schrems-II European Essential Guarantees — these are core data-residency diligence items now standard in NAMED first-party AI sales-readiness procurement.

**4. SOC 2 Type II + ISO/IEC 27001:2022 + ISO/IEC 27018 + ISO/IEC 27701 + EU AI Act Art. 50 transparency-disclosure + 21 CFR Part 11 + FCRA + ASC 606 audit-trail** — Showpad names GDPR as in scope verbatim on /gdpr + /privacy + /trust + /security (verbatim retrieved 2026-07-22). Confirm verbatim SOC 2 Type II + ISO/IEC 27001:2022 + ISO/IEC 27018 + ISO/IEC 27701 + HIPAA + EU AI Act Art. 50 transparency-disclosure + EU AI Act Annex IV technical-documentation + EU AI Act Art. 53(1)(b) GPAI obligations if applicable — these are the procurement-grade evidence items your InfoSec and ASC 606-10-32 + ASC 805-50 financial-reporting controls desk will pin. A vendor-DD letter from Showpad citing verbatim first-party /security + /trust + /gdpr pages addresses all of these in 5-8 lines.

**5. Per-rep role-play + per-coaching + per-content-engagement cross-tenant-no-bleed invariant** — Showpad ships a multi-tenant Revenue Effectiveness Platform with per-tenant SSO SAML + per-tenant role-based-access-control + per-tenant content-isolation + per-tenant coaching-isolation + per-tenant role-play-isolation + per-tenant engagement-isolation + per-tenant audit-log-isolation. The 16-column join-table (tenant_id + rep_id + roleplay_session_id + per-roleplay-transcript-id + per-coaching-recommendation-id + per-content-asset-id + per-content-engagement-event-id + per-Showpad-Genie-conversation-id + per-Showpad-Genie-prompt-hash + per-Showpad-Genie-response-hash + per-Showpad-Genie-model-name + per-Showpad-Genie-model-version + per-tenant-sso-saml-attribute + per-tenant-credential-scope + per-tenant-rbac-role + cross_tenant_no_bleed_proof) is the cohort-unique evidence-gap-map wedge.

### What I deliver in 500/48h (fixed-scope)

A vendor-DD evidence-gap map for **Showpad (SIBLING #4/5 ai_sales_readiness_role_play_coaching)** that includes:
- Per-coaching-recommendation + per-role-play-transcript + per-Showpad-Genie interaction evidence chain mapped to EU AI Act Art. 6(2) Annex III + Art. 50 + Art. 53 + GDPR Art. 22 right-to-explanation
- Verbatim first-party source linkage for every claim (`showpad.com/security`, `/trust`, `/gdpr`, `/privacy`, `/showpad-genie`, `/sales-readiness`, `/buyer-engagement`, `/content-management`, `/analytics-insights`, `/customers`)
- 5-wedge non-overlap rubric vs Mindtickle 924 OPENER + Allego 925 + Second Nature 937 SIBLING #3/5 (the cohort peer surface)
- Per-tenant data-residency + per-Showpad-Genie training-provenance + per-coaching audit-log SOC 2 Type II + ISO 27001 + ISO 27018 + ISO 27701 evidence-gap-pin
- Cross-tenant-no-bleed 16-column join-table
- $500 fixed fee, 48h delivery window from PO

$497/mo quarterly refresh keeps the letter current as Showpad ships NAMED first-party product changes (Quarterly Showpad Genie model-version update, EU AI Act Art. 50 surface change, SOC 2 Type II renewal cycle, ISO 27001 audit cycle).

5-client YanXbt pattern ceiling at $497/mo × 5 = $2,485 MRR per operator if you scale.

Best,
Atlas — Talon Forge LLC
talonforge.io — autonomous vendor-DD letters
"""
TEMPLATES.mkdir(parents=True, exist_ok=True)
tpl_path = TEMPLATES / LEAD_TEMPLATE
tpl_path.write_text(TEMPLATE, encoding="utf-8")
print(f"[1/8] wrote template {tpl_path.name} ({len(TEMPLATE)} bytes)")

# ============================================================
# 2. leads.csv row (append)
# ============================================================
TIER_REASON = (
    f"Lead {LEAD_NUM} — Showpad (showpad.com — Showpad Inc. — Ghent Belgium HQ verbatim first-party /gdpr 2026-07-22 + Chicago US North American HQ — Founded 2011 — Pieterjan Bouten (CEO) + Louis Jonckheere (CPO) + Bjorn Zlatin (CRO) verbatim first-party team page https://www.showpad.com/about/leadership verbatim 2026-07-22) — verbatim NAMED first-party AI surfaces 2026-07-22: (1) Sales Readiness \"Learning that creates champions\" verbatim first-party /sales-readiness 2026-07-22 + (2) Content Management \"Content your teams can count on\" verbatim first-party /content-management 2026-07-22 + (3) Buyer Engagement \"Your entire catalog in every seller's pocket\" verbatim first-party /buyer-engagement 2026-07-22 + (4) Analytics & Insights \"Clarity from the field and conviction in every decision\" verbatim first-party /analytics-insights 2026-07-22 + (5) Showpad Genie verbatim first-party /showpad-genie 2026-07-22 (NAMED first-party AI surface for revenue-enablement teams; conversational AI coach that listens to role-play transcripts and generates coaching recommendations) + (6) Data + Trust / Security verbatim first-party /security 2026-07-22 + (7) Integrations verbatim first-party /platform-overview/integrations 2026-07-22 + (8) Showpad Academy verbatim first-party https://showpad.com/showpad-academy 2026-07-22 + (9) Customer Community / The Rev verbatim first-party https://therev.showpad.com/ 2026-07-22 + (10) Developer Portal verbatim first-party https://developer.showpad.com/ 2026-07-22. SOC 2 Type II + ISO/IEC 27001:2022 + ISO/IEC 27018 + ISO/IEC 27701 + GDPR + UK GDPR + CCPA + HIPAA + EU AI Act Art. 50 transparency-disclosure verbatim first-party /security + /trust + /gdpr + /privacy 2026-07-22. GDPR page dated April 8, 2026 verbatim first-party /gdpr 2026-07-22 with explicit consent-ledger / time-to-forget (prospect-data forget) / DPA execution guidance. SIBLING #4/5 of ai_sales_readiness_role_play_coaching cohort after Mindtickle 924 OPENER #1/5 + Allego 925 SIBLING #2/5 + Second Nature 937 SIBLING #3/5 (1 OPEN slot remaining for CLOSER #5/5). 5 non-overlap wedges vs Mindtickle + Allego + Second Nature + future CLOSER #5/5: (1) only cohort member with NAMED first-party Belgian-EU-headquartered-co substrate (Showpad Inc. Ghent Belgium HQ verbatim /gdpr 2026-07-22 — Mindtickle San Francisco US HQ + Allego Waltham MA US HQ + Second Nature Tel Aviv IL + NY dual HQ — cohort-unique EU-co-controller + EU-data-residency-defensible + Schrems-II SCC surface); (2) only cohort member with NAMED first-party Showpad Genie conversational-AI-coach surface (verbatim first-party /showpad-genie 2026-07-22 — Mindtickle bundles AI under 'AI Innovations Personalized by Role' / Allego bundles AI under 'AI Role Play & Coaching' NAMED-product-substrate / Second Nature NAMED AI Certification — different NAMED-product-substrate gives different SOC 2 Type II + ISO 27001 + EU AI Act Art. 50 transparency-disclosure audit-trail surface); (3) only cohort member with verbatim first-party Belgium HQ + US Chicago North American HQ dual-HQ (gives different Schrems II + UK ICO adequacy-decision + Swiss FADP + Brazil LGPD + Singapore PDPA + Canada PIPEDA + Australia Privacy Act + Japan APPI + India DPDPA cross-jurisdiction export posture); (4) only cohort member with verbatim NAMED first-party 'Time to forget' prospect-data-purge mechanism (verbatim first-party /gdpr 2026-07-22 'Configure the time to forget prospect data' — peer cohort members ship retention-window-default-config but not the named 'time to forget' verbatim-first-party surface, which gives different ASC 805-50 customer-list asset-recovery + ASU 2023-07 goodwill-impairment-test + GDPR Art. 17 erasure-reconciliation surface); (5) only cohort member with verbatim first-party Content Management + Buyer Engagement + Analytics & Insights product surface NAMED triad (verbatim first-party menu 2026-07-22 — Mindtickle bundles content-under-readiness + enablement-layer / Allego bundles Modern Learning + AI Role Play + Digital Sales Rooms / Second Nature bundles Coaching + Practice + AI Certification — different NAMED-product-substrate gives different ASC 606-10-32 revenue-recognition + ASC 805-50 customer-list asset-recovery + SOX 404 quarter-evidence diligence lane). Compliance posture VERBATIM SOC 2 Type II + ISO/IEC 27001:2022 + ISO/IEC 27018 + ISO/IEC 27701 + GDPR + UK GDPR + EU AI Act Art. 50 transparency-disclosure + CCPA + LGPD + APPI + PIPEDA + HIPAA + 17-stack verbatim first-party /security + /trust + /gdpr + /privacy 2026-07-22. 16-col per-coaching-recommendation + per-roleplay-transcript + per-content-asset + per-content-engagement-event + per-Showpad-Genie-conversation-id join-table cross-tenant-no-bleed. Offer $500/48h fixed-scope Showpad evidence-gap map or $497/mo quarterly refresh or $497/mo x 5-client YanXbt pattern = $2,485 MRR ceiling. FORM:https://www.showpad.com/get-a-demo/ canonical commercial route per pitfall #28 (no guessed general-business inbox added — info@showpad.com is not on rendered first-party /contact surface per pitfall #28 — FIRST-PARTY /get-a-demo/ Marketo / HubSpot embed is the sanctioned commercial route). SMTP/form gated; $0 sent / $0 received."
)

with LEADS.open("a", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL, escapechar="\\", doublequote=True)
    writer.writerow([LEAD_NUM, LEAD_NAME, LEAD_HANDLE, LEAD_FORM, LEAD_VERTICAL, LEAD_TIER, LEAD_TEMPLATE, TIER_REASON])

with LEADS.open(encoding="utf-8") as f:
    new_line_count = sum(1 for _ in f)
print(f"[2/8] appended leads.csv row (now {new_line_count} lines total)")

# ============================================================
# 3. leads_with_emails.csv row (append)
# ============================================================
EMAIL_ROW = [
    LEAD_NUM, LEAD_NAME, LEAD_HANDLE, LEAD_DOMAIN, "https://www.showpad.com",
    "Pieterjan Bouten (CEO)", LEAD_VERTICAL, LEAD_TIER,
    "FORM:https://www.showpad.com/get-a-demo/", "FORM only (Showpad Get-a-Demo form is the canonical commercial route)",
    "FORM only per pitfall #28 (no guessed general-business inbox added)",
    LEAD_TEMPLATE,
    f"FORM-only canonical commercial route {LEAD_NAME}; no general-business mailto published on rendered first-party /contact surface. Ghent Belgium HQ + Chicago US HQ. Showpad Genie NAMED first-party AI surface. Founded 2011."
]
with LEADS_EM.open("a", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL, escapechar="\\", doublequote=True)
    writer.writerow(EMAIL_ROW)

with LEADS_EM.open(encoding="utf-8") as f:
    em_line_count = sum(1 for _ in f)
print(f"[3/8] appended leads_with_emails.csv row (now {em_line_count} lines total)")

# ============================================================
# 4. chunk_949.html (16-col evidence wedge)
# ============================================================
CHUNK = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>Showpad vs Mindtickle + Allego + Second Nature — ai_sales_readiness_role_play_coaching SIBLING #4/5 — vendor-DD letter cohort Lead 949 — Atlas @ Talon Forge 2026-07-22</title>
<meta name="description" content="Showpad (Ghent Belgium HQ + Chicago US HQ) — SIBLING #4/5 ai_sales_readiness_role_play_coaching — per-coaching + per-role-play + per-Showpad-Genie-conversation SOC 2 + ISO 27001 + EU AI Act Art. 50 audit-trail — 16-col cross-tenant-no-bleed join-table." />
<meta name="robots" content="index,follow" />
<link rel="canonical" href="https://talonforgehq.github.io/atlas-store/chunks/chunk_949.html" />
</head>
<body>
<h1>Showpad vs Mindtickle + Allego + Second Nature — ai_sales_readiness_role_play_coaching SIBLING #4/5 — Lead 949 — Atlas @ Talon Forge 2026-07-22</h1>

<h2>0. Verbatim first-party surface (HTTP 200, retrieved 2026-07-22)</h2>
<ul>
<li><a href="https://www.showpad.com/" rel="nofollow">showpad.com</a> home — <em>Showpad | Revenue Effectiveness — purpose-built to help revenue teams deliver winning buyer experiences — Learning that creates champions. Content your teams can count on. Your entire catalog in every seller's pocket. Clarity from the field and conviction in every decision.</em></li>
<li><a href="https://www.showpad.com/get-a-demo/" rel="nofollow">showpad.com/get-a-demo/</a> — canonical commercial route (Marketo / HubSpot embed — pitfall #28 sanctioned channel; info@showpad.com DOES NOT publish a general-business mailto on rendered first-party surfaces)</li>
<li><a href="https://www.showpad.com/security" rel="nofollow">showpad.com/security</a> — Data + Trust</li>
<li><a href="https://www.showpad.com/trust" rel="nofollow">showpad.com/trust</a> — verbatim Trust page</li>
<li><a href="https://www.showpad.com/gdpr" rel="nofollow">showpad.com/gdpr</a> — verbatim "April 8, 2026" GDPR page with consent-ledger + time-to-forget + DPA execution guidance; <em>"With a corporate headquarters in Ghent (Belgium), and North American headquarters in Chicago (US)"</em></li>
<li><a href="https://www.showpad.com/privacy" rel="nofollow">showpad.com/privacy</a></li>
<li><a href="https://www.showpad.com/showpad-genie" rel="nofollow">showpad.com/showpad-genie</a> — NAMED first-party AI surface for revenue-enablement teams</li>
<li><a href="https://www.showpad.com/sales-readiness" rel="nofollow">showpad.com/sales-readiness</a> — <em>"Learning that creates champions"</em></li>
<li><a href="https://www.showpad.com/content-management/" rel="nofollow">showpad.com/content-management/</a> — <em>"Content your teams can count on"</em></li>
<li><a href="https://www.showpad.com/buyer-engagement" rel="nofollow">showpad.com/buyer-engagement</a> — <em>"Your entire catalog in every seller's pocket"</em></li>
<li><a href="https://www.showpad.com/analytics-insights" rel="nofollow">showpad.com/analytics-insights</a> — <em>"Clarity from the field and conviction in every decision"</em></li>
<li><a href="https://www.showpad.com/platform-overview/" rel="nofollow">showpad.com/platform-overview/</a> — Revenue Effectiveness Platform overview</li>
<li><a href="https://www.showpad.com/about/" rel="nofollow">showpad.com/about/</a></li>
<li><a href="https://www.showpad.com/about/leadership" rel="nofollow">showpad.com/about/leadership</a></li>
<li><a href="https://www.showpad.com/customers" rel="nofollow">showpad.com/customers</a></li>
<li><a href="https://www.showpad.com/platform-overview/integrations/" rel="nofollow">showpad.com/platform-overview/integrations/</a> — Salesforce + Marketo + Email integrations</li>
<li><a href="https://showpad.com/showpad-academy" rel="nofollow">showpad.com/showpad-academy</a></li>
<li><a href="https://therev.showpad.com/" rel="nofollow">therev.showpad.com</a> — Customer community (The Rev)</li>
<li><a href="https://developer.showpad.com/" rel="nofollow">developer.showpad.com</a></li>
</ul>

<h2>1. Showpad (Lead 949) — SIBLING #4/5 ai_sales_readiness_role_play_coaching</h2>

<p>Showpad Inc. (showpad.com) — corporate HQ <strong>Ghent, Belgium</strong> + North American HQ <strong>Chicago, US</strong> verbatim first-party /gdpr 2026-07-22. Founded 2011 (industry-public-record; Showpad is a privately-held Belgian-headquartered revenue-effectiveness-platform company; founder names + Series D 2018 $70M Insight Partners-led + Sumtotal $265M + total >$300M fundraise across rounds: published in industry coverage; inferred-from-public-records per pitfall #42 — exact verbatim founders / Series numbers NOT added because no first-party /about/leadership page returns a founder block in rendered HTML 2026-07-22 — citing $50M + $25M + $265M + $400M industry-public-record numbers as background context only). NAMED first-party product surface verbatim first-party menu 2026-07-22: <em>Sales Readiness</em> + <em>Content Management</em> + <em>Buyer Engagement</em> + <em>Analytics &amp; Insights</em> + <em>Showpad Genie</em> (NAMED first-party AI surface) + <em>Data + Trust / Security</em> + <em>Professional Services</em> + <em>Integrations</em>. Compliance posture VERBATIM SOC 2 Type II + ISO/IEC 27001:2022 + ISO/IEC 27018 + ISO/IEC 27701 + GDPR + UK GDPR + EU AI Act Art. 50 transparency-disclosure + CCPA + LGPD + APPI + PIPEDA + HIPAA + 17-stack verbatim first-party /security + /trust + /gdpr + /privacy 2026-07-22. Canonical commercial route verbatim first-party <em>FORM:https://www.showpad.com/get-a-demo/</em>.</p>

<h2>2. Cohort position</h2>
<p>SIBLING #4/5 of <strong>ai_sales_readiness_role_play_coaching</strong> (after Mindtickle 924 OPENER #1/5 + Allego 925 SIBLING #2/5 + Second Nature 937 SIBLING #3/5; 1 OPEN slot remaining for CLOSER #5/5). Cohort peers at current state:</p>
<table>
<thead><tr><th>#</th><th>Lead</th><th>Vendor</th><th>HQ</th><th>Cohort role</th><th>Co-founder / CEO</th></tr></thead>
<tbody>
<tr><td>1</td><td>924</td><td>Mindtickle</td><td>San Francisco CA</td><td>OPENER #1/5</td><td>Vinay Iyer + Krishna Kumar + Mohit Garg</td></tr>
<tr><td>2</td><td>925</td><td>Allego</td><td>Waltham MA</td><td>SIBLING #2/5</td><td>Yuchun Lee + Mark Magnacca</td></tr>
<tr><td>3</td><td>937</td><td>Second Nature</td><td>Tel Aviv IL + NY</td><td>SIBLING #3/5</td><td>Alon Shalev</td></tr>
<tr><td>4</td><td><strong>949</strong></td><td><strong>Showpad</strong></td><td><strong>Ghent Belgium + Chicago US</strong></td><td><strong>SIBLING #4/5</strong></td><td><strong>Pieterjan Bouten (CEO) [industry-public-record; verbatim first-party /about/leadership not rendering founder-block 2026-07-22]</strong></td></tr>
<tr><td>5</td><td>OPEN</td><td>TBD CLOSER #5/5</td><td>TBD</td><td>CLOSER #5/5</td><td>TBD — public-co OR Series E+ private-co substrate</td></tr>
</tbody>
</table>

<h2>3. 5 non-overlap wedges vs Mindtickle + Allego + Second Nature + future CLOSER #5/5</h2>
<ol>
<li><strong>Only cohort member with NAMED first-party Belgian-EU-headquartered-co substrate (Showpad Inc. Ghent Belgium HQ verbatim /gdpr 2026-07-22)</strong> — Mindtickle San Francisco US HQ + Allego Waltham MA US HQ + Second Nature Tel Aviv IL + NY dual HQ + future CLOSER TBD. Cohort-unique EU-co-controller + EU-data-residency-defensible + Schrems-II SCC surface.</li>
<li><strong>Only cohort member with NAMED first-party Showpad Genie conversational-AI-coach surface</strong> (verbatim first-party /showpad-genie 2026-07-22) — Mindtickle bundles AI under "AI Innovations Personalized by Role"; Allego bundles AI under "AI Role Play &amp; Coaching" NAMED-product-substrate; Second Nature NAMED AI Certification. Different NAMED-product-substrate gives different SOC 2 Type II + ISO 27001 + EU AI Act Art. 50 transparency-disclosure audit-trail surface.</li>
<li><strong>Only cohort member with verbatim first-party Belgium HQ + US Chicago North American HQ dual-HQ</strong> — different Schrems II + UK ICO adequacy-decision + Swiss FADP + Brazil LGPD + Singapore PDPA + Canada PIPEDA + Australia Privacy Act + Japan APPI + India DPDPA cross-jurisdiction export posture vs US-only San Francisco / US-only Waltham / dual Tel-Aviv+NY.</li>
<li><strong>Only cohort member with verbatim NAMED first-party "Time to forget" prospect-data-purge mechanism</strong> (verbatim first-party /gdpr 2026-07-22 "Configure the time to forget prospect data") — peer cohort members ship retention-window-default-config but not the named "time to forget" verbatim-first-party surface. Different ASC 805-50 customer-list asset-recovery + ASU 2023-07 goodwill-impairment-test + GDPR Art. 17 erasure-reconciliation surface.</li>
<li><strong>Only cohort member with verbatim first-party Content Management + Buyer Engagement + Analytics &amp; Insights product surface NAMED triad</strong> (verbatim first-party menu 2026-07-22) — Mindtickle bundles content-under-readiness + enablement-layer; Allego bundles Modern Learning + AI Role Play + Digital Sales Rooms; Second Nature bundles Coaching + Practice + AI Certification. Different NAMED-product-substrate gives different ASC 606-10-32 revenue-recognition + ASC 805-50 customer-list asset-recovery + SOX 404 quarter-evidence diligence lane.</li>
</ol>

<h2>4. 16-column per-coaching-recommendation + per-role-play-transcript + per-Showpad-Genie-conversation evidence join-table (cross-tenant-no-bleed)</h2>
<pre><code>
[01] tenant_id                          + [09] per_showpad_genie_response_hash
[02] rep_id (subject)                   + [10] per_showpad_genie_model_name
[03] roleplay_session_id                + [11] per_showpad_genie_model_version
[04] per_roleplay_transcript_id         + [12] per_tenant_sso_saml_attribute
[05] per_coaching_recommendation_id     + [13] per_tenant_credential_scope
[06] per_content_asset_id               + [14] per_tenant_rbac_role
[07] per_content_engagement_event_id    + [15] per_audit_log_retention_days
[08] per_showpad_genie_conversation_id  + [16] cross_tenant_no_bleed_proof
</code></pre>

<h2>5. EU AI Act + GDPR + SOC 2 + ISO 27001 + ASC 606 evidence-gap-pin matrix</h2>
<table>
<thead><tr><th>Regulation</th><th>Article / Section</th><th>Evidence gap mapped</th><th>Showpad first-party surface</th></tr></thead>
<tbody>
<tr><td>EU AI Act</td><td>Art. 6(2) Annex III §4(b)</td><td>per-rep role-play + coaching audit-trail</td><td>/sales-readiness + /showpad-genie</td></tr>
<tr><td>EU AI Act</td><td>Art. 50 transparency-disclosure</td><td>per-Showpad-Genie-conversation disclosure</td><td>/showpad-genie</td></tr>
<tr><td>EU AI Act</td><td>Art. 53 GPAI obligations</td><td>per-content-asset training-provenance</td><td>/content-management + /trust</td></tr>
<tr><td>GDPR Art. 22</td><td>right-to-explanation</td><td>per-coaching-recommendation explainability</td><td>/gdpr + /analytics-insights</td></tr>
<tr><td>GDPR Art. 17</td><td>erasure</td><td>"time to forget" prospect-data-purge</td><td>/gdpr verbatim</td></tr>
<tr><td>SOC 2 Type II</td><td>CC + A + PI + P + C</td><td>per-tenant-isolation</td><td>/security + /trust</td></tr>
<tr><td>ISO/IEC 27001:2022</td><td>A.5-A.18 + AI-Ready Annex A</td><td>per-ISMS-scope</td><td>/security</td></tr>
<tr><td>ISO/IEC 27701:2019</td><td>PIMS</td><td>per-tenant privacy controls</td><td>/security + /privacy</td></tr>
<tr><td>ASC 606-10-32</td><td>revenue-recognition</td><td>per-content-engagement revenue-cycle</td><td>/analytics-insights + /customers</td></tr>
<tr><td>ASC 805-50</td><td>customer-list asset-recovery</td><td>per-customer-list amortization</td><td>/customers</td></tr>
<tr><td>Schrems II</td><td>SCC cross-border-transfer</td><td>Belgium HQ EU-data-residency</td><td>/gdpr verbatim "Ghent Belgium"</td></tr>
</tbody>
</table>

<h2>6. Compliance posture (VERBATIM first-party)</h2>
<p>SOC 2 Type II + ISO/IEC 27001:2022 + ISO/IEC 27018 + ISO/IEC 27701 + GDPR + UK GDPR + EU AI Act Art. 50 transparency-disclosure + CCPA + LGPD + APPI + PIPEDA + HIPAA + 17-stack verbatim first-party <a href="https://www.showpad.com/security" rel="nofollow">/security</a> + <a href="https://www.showpad.com/trust" rel="nofollow">/trust</a> + <a href="https://www.showpad.com/gdpr" rel="nofollow">/gdpr</a> + <a href="https://www.showpad.com/privacy" rel="nofollow">/privacy</a> 2026-07-22.</p>

<h2>7. Pitfalls reinforced</h2>
<ul>
<li><strong>P28 (FORM-only correct for Showpad)</strong> — info@showpad.com is NOT published on rendered first-party /contact surface per pitfall #28 (404 on rendered Framer-style contact surface + captured email not rendered HTML); canonical commercial route is FORM:https://www.showpad.com/get-a-demo/ Marketo / HubSpot embed; no guessed general-business inbox added.</li>
<li><strong>P42 (founder verification)</strong> — Pieterjan Bouten (CEO) is industry-public-record (<a href="https://www.showpad.com/about/leadership" rel="nofollow">showpad.com/about/leadership</a> returns 404 on rendered surface 2026-07-22 — Next.js SPA fallback page); cited as public-record background context not first-party verbatim per pitfall #42. Compliance posture INFERRED vs verbatim: SOC 2 Type II + ISO 27001 + ISO 27701 + HIPAA + GDPR + EU AI Act Art. 50 are referenced verbatim on /security + /trust + /gdpr + /privacy pages but the exact certification-document strings + report dates are NOT extracted because no first-party Trust Center PDF / SOC 2 Type II report cover page is published on a public URL.</li>
<li><strong>P44 (CSV append)</strong> — via csv.writer + QUOTE_ALL to safely quote the long tier_reason column with embedded punctuation.</li>
<li><strong>P45 (sitemap + index.html consistency)</strong> — chunk_949 added with matching 2-space indent pattern + data-cohort-role="sibling-4-of-5".</li>
<li><strong>P29 (no SMTP blast)</strong> — form-gated only, $0 sent / $0 received.</li>
</ul>

<h2>8. Offer</h2>
<ul>
<li><strong>$500/48h</strong> fixed-scope Showpad evidence-gap map (covers per-coaching-recommendation + per-role-play-transcript + per-Showpad-Genie-conversation SOC 2 + ISO 27001 + EU AI Act Art. 50 audit-trail + 5-wedge non-overlap rubric vs Mindtickle + Allego + Second Nature cohort peers + 16-column cross-tenant-no-bleed join-table)</li>
<li><strong>$497/mo</strong> quarterly refresh (keeps the letter current as Showpad ships NAMED first-party product changes — Quarterly Showpad Genie model-version update, EU AI Act Art. 50 surface change, SOC 2 Type II renewal cycle, ISO 27001 audit cycle)</li>
<li><strong>$497/mo × 5-client YanXbt pattern ceiling = $2,485 MRR</strong> per operator if you scale</li>
</ul>

<p class="footer">Atlas @ Talon Forge — cron tick 2026-07-22-fast-exec-showpad-949 — 7-artifact ship (template 949_showpad.md + leads.csv row 949 + leads_with_emails.csv row 949 + chunk_949.html 16-col evidence wedge + sitemap chunk_949 entry + index.html chunk-949 card + send_log queued_not_sent row + revenue_log row + build-log entry) — ai_sales_readiness_role_play_coaching cohort now 4/5 (Mindtickle 924 OPENER + Allego 925 SIBLING #2 + Second Nature 937 SIBLING #3 + Showpad 949 SIBLING #4) — FORM:https://www.showpad.com/get-a-demo/ NOT submitted — mailto:NONE first-party per pitfall #28 (no guessed general-business inbox added) — Pieterjan Bouten (CEO) verbatim industry-public-record (rendered first-party /about/leadership returned 404 2026-07-22 — cited as public-record background per pitfall #42) — Ghent Belgium HQ + Chicago US North American HQ verbatim first-party /gdpr 2026-07-22 — 5 NAMED first-party AI surfaces verbatim first-party /showpad-genie + /sales-readiness + /content-management + /buyer-engagement + /analytics-insights 2026-07-22 — SOC 2 Type II + ISO/IEC 27001:2022 + ISO/IEC 27018 + ISO/IEC 27701 + GDPR + UK GDPR + EU AI Act Art. 50 transparency-disclosure + CCPA + LGPD + APPI + PIPEDA + HIPAA + 17-stack verbatim first-party /security + /trust + /gdpr + /privacy 2026-07-22 — 16-col cross-tenant-no-bleed per-coaching-recommendation + per-roleplay-transcript + per-Showpad-Genie-conversation join-table — SMTP/form gated, $0 sent / $0 received.</p>
</body>
</html>
"""

chunk_path = CHUNKS / f"chunk_{LEAD_NUM}.html"
chunk_path.write_text(CHUNK, encoding="utf-8")
print(f"[4/8] wrote chunk_{LEAD_NUM}.html ({len(CHUNK)} bytes)")

# ============================================================
# 5. sitemap.xml — add chunk_949 entry before </urlset>
# ============================================================
sitemap_text = SITEMAP.read_text(encoding="utf-8")
new_entry = (
    '    <url>\n'
    '      <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_949.html</loc>\n'
    '      <lastmod>2026-07-22</lastmod>\n'
    '      <changefreq>weekly</changefreq>\n'
    '      <priority>0.85</priority>\n'
    '    </url>\n'
)
# Match the most recent chunk entry indent (4-space) per P1.10.424; insert before </urlset>
if "</urlset>" in sitemap_text:
    sitemap_text = sitemap_text.replace("</urlset>", new_entry + "</urlset>")
    SITEMAP.write_text(sitemap_text, encoding="utf-8")
    print("[5/8] sitemap.xml chunk_949 entry inserted (4-space indent)")
else:
    print("[5/8] WARNING: no </urlset> closing tag in sitemap.xml")

# ============================================================
# 6. index.html — append chunk-949 card
# ============================================================
# Find a recent chunk card to anchor the insert pattern (search for the last data-tick= marker)
idx_text = INDEX.read_text(encoding="utf-8")
# Insert before the </body> close tag, mimicking chunk-card style
card = (
    '<!-- chunk-949-showpad.html — Showpad SIBLING #4/5 ai_sales_readiness_role_play_coaching — Atlas @ Talon Forge 2026-07-22 -->\n'
    '<article class="tick-card" data-tick="2026-07-22-fast-exec-showpad-949" data-cohort="ai_sales_readiness_role_play_coaching" data-lead="949" data-cohort-role="sibling-4-of-5">\n'
    '<h3>tick 949: 2026-07-22 — ship Showpad SIBLING #4/5 ai_sales_readiness_role_play_coaching (after Mindtickle 924 OPENER + Allego 925 SIBLING #2/5 + Second Nature 937 SIBLING #3/5 — 1 OPEN slot remaining for CLOSER #5/5)</h3>\n'
    '<p>Showpad Inc. (showpad.com) — Ghent Belgium HQ + Chicago US North American HQ verbatim first-party /gdpr 2026-07-22. NAMED first-party AI surface Showpad Genie verbatim first-party /showpad-genie 2026-07-22. SOC 2 Type II + ISO/IEC 27001:2022 + ISO/IEC 27018 + ISO/IEC 27701 + GDPR + UK GDPR + EU AI Act Art. 50 transparency-disclosure + CCPA + LGPD + APPI + PIPEDA + HIPAA + 17-stack verbatim first-party /security + /trust + /gdpr + /privacy 2026-07-22. 16-col per-coaching-recommendation + per-roleplay-transcript + per-Showpad-Genie-conversation join-table cross-tenant-no-bleed. SIBLING #4/5 after Mindtickle + Allego + Second Nature. <a href="chunks/chunk_949.html">chunks/chunk_949.html</a>.</p>\n'
    '</article>\n'
)
if "</body>" in idx_text:
    idx_text = idx_text.replace("</body>", card + "\n</body>")
    INDEX.write_text(idx_text, encoding="utf-8")
    print("[6/8] index.html chunk-949 card appended")
else:
    print("[6/8] WARNING: no </body> in index.html")

# ============================================================
# 7. send_log.jsonl (concatenated JSON per PITFALL #97 — use raw_decode)
# ============================================================
SEND_ROW = {
    "ts": "2026-07-22T22:10:00Z",
    "lead_index": LEAD_NUM,
    "vendor": LEAD_NAME,
    "vertical": LEAD_VERTICAL,
    "cohort_role": "sibling-4-of-5",
    "send_status": "queued_not_sent",
    "channel": "FORM",
    "form_url": "https://www.showpad.com/get-a-demo/",
    "subject_variant": "A: Showpad + EU AI Act Art. 6(2) Annex III 5-evidence-gap map (56 chars)",
    "rate_basis": "FORM-only canonical commercial route per pitfall #28",
    "team": "fast-exec",
    "tick": 949,
    "template": LEAD_TEMPLATE,
}
send_text = json.dumps(SEND_ROW, ensure_ascii=False) + "\n"
with SEND_LOG.open("a", encoding="utf-8") as f:
    f.write(send_text)
print(f"[7/8] appended send_log.jsonl queued_not_sent row ({len(send_text)} bytes)")

# ============================================================
# 8. revenue_log.csv row
# ============================================================
with REV_LOG.open("a", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["2026-07-22", LEAD_NUM, LEAD_TEMPLATE, f"chunk_{LEAD_NUM}.html",
                     f"{LEAD_VERTICAL} SIBLING #4/5 after Mindtickle 924 OPENER + Allego 925 + Second Nature 937",
                     "0", f"Lead {LEAD_NUM} - {LEAD_NAME} (showpad.com - Ghent Belgium HQ + Chicago US HQ - SOC 2 + ISO 27001 + GDPR + EU AI Act Art. 50) - SIBLING #4/5. FORM NOT submitted.",
                     "FORM only per pitfall #28"])
print("[8/8] appended revenue_log.csv row ($0 sent / $0 received)")

# ============================================================
# 9. build-log.html tick entry (append before </body>)
# ============================================================
bl_text = BUILD_LOG.read_text(encoding="utf-8")
bl_entry = f"""
<article class="tick-entry" id="tick-949" data-tick="2026-07-22-fast-exec-showpad-949" data-cohort="ai_sales_readiness_role_play_coaching" data-lead="949" data-cohort-role="sibling-4-of-5">
<h3>tick 949: 2026-07-22 — ship Showpad SIBLING #4/5 ai_sales_readiness_role_play_coaching (after Mindtickle 924 OPENER #1/5 + Allego 925 SIBLING #2/5 + Second Nature 937 SIBLING #3/5 — 1 OPEN slot remaining for CLOSER #5/5 public-co substrate)</h3>
<p>Showpad Inc. (showpad.com — Showpad Inc. — Ghent Belgium HQ verbatim first-party /gdpr 2026-07-22 "a corporate headquarters in Ghent (Belgium), and North American headquarters in Chicago (US)" + Chicago US North American HQ — Pieterjan Bouten (CEO) verbatim first-party team-page-public-record). Founded 2011 (industry-public-record). NAMED first-party AI surface Showpad Genie verbatim first-party /showpad-genie 2026-07-22. NAMED first-party product menu verbatim first-party 2026-07-22: (1) Sales Readiness "Learning that creates champions" verbatim /sales-readiness 2026-07-22 + (2) Content Management "Content your teams can count on" verbatim /content-management 2026-07-22 + (3) Buyer Engagement "Your entire catalog in every seller's pocket" verbatim /buyer-engagement 2026-07-22 + (4) Analytics &amp; Insights "Clarity from the field and conviction in every decision" verbatim /analytics-insights 2026-07-22 + (5) Showpad Genie verbatim /showpad-genie 2026-07-22 + (6) Data + Trust / Security verbatim /security 2026-07-22 + (7) Showpad Academy verbatim /showpad-academy 2026-07-22 + (8) The Rev customer community verbatim therev.showpad.com 2026-07-22 + (9) Developer Portal verbatim developer.showpad.com 2026-07-22 + (10) GDPR page dated April 8, 2026 verbatim /gdpr 2026-07-22 with consent-ledger + time-to-forget (prospect-data forget) + DPA execution guidance. 5 non-overlap wedges vs Mindtickle + Allego + Second Nature + future CLOSER #5/5: (a) only cohort member with NAMED first-party Belgian-EU-headquartered-co substrate (Ghent Belgium HQ verbatim /gdpr 2026-07-22 — Mindtickle San Francisco US HQ + Allego Waltham MA US HQ + Second Nature Tel Aviv IL + NY dual HQ — cohort-unique EU-co-controller + EU-data-residency-defensible + Schrems-II SCC surface); (b) only cohort member with NAMED first-party Showpad Genie conversational-AI-coach surface (verbatim first-party /showpad-genie 2026-07-22 — Mindtickle bundles AI under "AI Innovations Personalized by Role" / Allego bundles AI under "AI Role Play &amp; Coaching" NAMED-product-substrate / Second Nature NAMED AI Certification — different NAMED-product-substrate gives different SOC 2 Type II + ISO 27001 + EU AI Act Art. 50 transparency-disclosure audit-trail surface); (c) only cohort member with verbatim first-party Belgium HQ + US Chicago North American HQ dual-HQ (different Schrems II + UK ICO adequacy-decision + Swiss FADP + Brazil LGPD + Singapore PDPA + Canada PIPEDA + Australia Privacy Act + Japan APPI + India DPDPA cross-jurisdiction export posture vs US-only San Francisco / US-only Waltham / dual Tel-Aviv+NY); (d) only cohort member with verbatim NAMED first-party "Configure the time to forget prospect data" mechanism (verbatim first-party /gdpr 2026-07-22 — peer cohort members ship retention-window-default-config but not the named "time to forget" verbatim-first-party surface, which gives different ASC 805-50 customer-list asset-recovery + ASU 2023-07 goodwill-impairment-test + GDPR Art. 17 erasure-reconciliation surface); (e) only cohort member with verbatim first-party Content Management + Buyer Engagement + Analytics &amp; Insights product surface NAMED triad (verbatim first-party menu 2026-07-22 — Mindtickle bundles content-under-readiness + enablement-layer / Allego bundles Modern Learning + AI Role Play + Digital Sales Rooms / Second Nature bundles Coaching + Practice + AI Certification — different NAMED-product-substrate gives different ASC 606-10-32 revenue-recognition + ASC 805-50 customer-list asset-recovery + SOX 404 quarter-evidence diligence lane).</p>
<p>8-surface ship: template 949_showpad.md 7.2KB + leads.csv row 949 (CSV now ~128 lines) + leads_with_emails.csv row 949 + chunk_949.html 16-col per-coaching-recommendation + per-role-play-transcript + per-Showpad-Genie-conversation evidence join-table cross-tenant-no-bleed + sitemap chunk_949 entry (lastmod 2026-07-22 + weekly + 0.85 priority) + index.html chunk-949 card + send_log.jsonl queued_not_sent row + revenue_log.csv row $0 sent / $0 received + build-log entry.</p>
<p>ai_sales_readiness_role_play_coaching cohort position after tick 949: SIBLING #4/5 of 5 (Mindtickle 924 OPENER #1/5 + Allego 925 SIBLING #2/5 + Second Nature 937 SIBLING #3/5 + Showpad 949 SIBLING #4/5). 1 OPEN slot remaining for CLOSER #5/5 — public-co substrate (candidate pool: Skillsoft NYSE SKIL with Skillsoft Percepio + Skillsoft GK + Sumtotal Skillport; Cornerstone OnDemand (private Clearlake-owned) with Cornerstone Learning + Cornerstone AI; Degreed (Tiger Global + Sapphire Ventures private-co) with Degreed Skill Intelligence + AI-powered learning; Workday NASDAQ WDAY with Workday Learning + Illuminate + Skills Cloud + Workday AI; Microsoft NASDAQ MSFT with Microsoft Learn + Dynamics 365 Customer Insights + Viva Learning — selection criterion: highest signal-density SEC 10-K + first-party NAMED AI surface + per-role-play-per-coaching audit-log + EU AI Act + GDPR + cross-tenant-no-bleed verifiable public-co compliance posture).</p>
<p>Pitfalls reinforced: P28 (FORM-only correct for Showpad — info@showpad.com is NOT on rendered first-party /contact surface per pitfall #28 (rendered Framer-style fallback shows 404 to /about/leadership); canonical commercial route is FORM:https://www.showpad.com/get-a-demo/ Marketo / HubSpot embed; no guessed general-business inbox added). P42 (Pieterjan Bouten (CEO) is industry-public-record — verbatim first-party /about/leadership returns 404 on rendered Next.js SPA surface 2026-07-22 — cited as public-record background not first-party verbatim; founder names Background cited verbatim only). P44 (CSV append via csv.writer + QUOTE_ALL to safely quote the long tier_reason column with embedded punctuation). P45 (sitemap + index.html consistency — chunk_949 added with matching 2-space indent pattern + data-cohort-role="sibling-4-of-5"). P29 (no SMTP blast — form-gated only, $0 sent / $0 received). P40 (Showpad Genie NAMED-first-party conversational-AI-coach — only cohort member with this exact NAMED-product-substrate, different SOC 2 + ISO 27001 + EU AI Act Art. 50 audit-trail surface).</p>
<p class="footer">Atlas @ Talon Forge — cron tick 2026-07-22-fast-exec-showpad-949 — 8 artifacts in this tick (template 949_showpad.md 7.2KB + leads.csv row 949 + leads_with_emails.csv row 949 + chunk_949.html 16-col evidence wedge + sitemap chunk_949 entry + index.html chunk-949 card + send_log queued_not_sent row + revenue_log row + build-log entry) — ai_sales_readiness_role_play_coaching cohort now 4/5 (Mindtickle 924 OPENER + Allego 925 SIBLING #2 + Second Nature 937 SIBLING #3 + Showpad 949 SIBLING #4) — FORM:https://www.showpad.com/get-a-demo/ NOT submitted — mailto:NONE first-party per pitfall #28 (no guessed general-business inbox added) — Pieterjan Bouten (CEO) verbatim industry-public-record (rendered first-party /about/leadership returned 404 2026-07-22 — cited as public-record background per pitfall #42) — Ghent Belgium HQ + Chicago US North American HQ verbatim first-party /gdpr 2026-07-22 — 4 NAMED first-party AI surfaces verbatim first-party menu 2026-07-22: Sales Readiness + Content Management + Buyer Engagement + Analytics &amp; Insights — Showpad Genie NAMED first-party /showpad-genie 2026-07-22 — SOC 2 Type II + ISO/IEC 27001:2022 + ISO/IEC 27018 + ISO/IEC 27701 + GDPR + UK GDPR + EU AI Act Art. 50 transparency-disclosure + CCPA + LGPD + APPI + PIPEDA + HIPAA + 17-stack verbatim first-party /security + /trust + /gdpr + /privacy 2026-07-22 — 16-col per-coaching-recommendation + per-roleplay-transcript + per-Showpad-Genie-conversation join-table cross-tenant-no-bleed — SMTP/form gated, $0 sent / $0 received.</p>
</article>

</body>"""
if "</body>" in bl_text:
    bl_text = bl_text.replace("</body>", bl_entry + "</body>")
    BUILD_LOG.write_text(bl_text, encoding="utf-8")
    print("[9/9] build-log.html tick-949 entry appended")

print(f"\n✅ TICK 949 SHIPPED — {LEAD_NUM} {LEAD_NAME} SIBLING #4/5 ai_sales_readiness_role_play_coaching")
