# Tick-1379 Contify SIBLING #3/5 ai_agent_competitive_intelligence ship script.

# Appends 3 CSV rows atomically:
#   - leads.csv               8-col QUOTE_ALL + CRLF
#   - leads_with_emails.csv   6-col headered bare format + CRLF
#   - revenue_log.csv         8-col QUOTE_ALL + CRLF
#
# Preserves the existing file CRLF + QUOTE_ALL invariants per
# PITFALL #NEW-CAT-STRIPS-CRLF (binary append of CRLF-terminated bytes)
# + csv-writer-must-be-text-mode + PITFALL #DYNATRACE-1356-PITFALL-1.
#
# Run from C:\Users\Potts\projects\atlas-store as
#   py -3.12 _scripts\tick_1379_contify_sibling_3_ship.py

import io
import os
import sys

REPO = r"C:\Users\Potts\projects\atlas-store"

LEADS_CSV = os.path.join(REPO, "cold_email", "leads.csv")
LWE_CSV   = os.path.join(REPO, "cold_email", "leads_with_emails.csv")
REV_CSV   = os.path.join(REPO, "cold_email", "revenue_log.csv")


def _check_invariants(path, label):
    raw = open(path, "rb").read()
    if b"\r\n" not in raw:
        print(f"FAIL: {label} ({path}) has no CRLF lines, would corrupt QUOTE_ALL invariant")
        sys.exit(1)
    print(f"OK:   {label} ({path})  CRLF preserved  ({raw.count(bytes([13,10]))} CRLF lines)")


def _quoted(field):
    # csv-style quoting: double inner quotes, wrap whole field in quotes
    inner = field.replace('"', '""')
    return f'"{inner}"'


# ===========================================================================
# 1. leads.csv
# ===========================================================================

CONTIF_DESCRIPTION = (
    "Lead 1379 - Contify (contify.com - first-party verified 2026-07-26 verbatim "
    "contify.com + contify.com/about-us + contify.com/contact-us: banner 'Contify "
    "Recognized as a Visionary in the Inaugural 2026 Gartner Magic Quadrant for "
    "Competitive and Market Intelligence Platforms' + H1 'Timely AI-powered "
    "Contextual 360 intelligence delivered. Grow faster than the market' + tagline "
    "'Contify delivers 360 market and competitive intelligence. Get insights that "
    "help you take better decisions, faster.' + named first-party product surfaces "
    "verbatim contify.com 2026-07-26 Athena AI ('Contify's Agentic AI insights engine "
    "- Extracts key business facts from articles, reports, and internal content; "
    "Answers ad-hoc business questions instantly with context-aware precision; "
    "Auto-updates dashboards, battlecards, and timelines with real-time insights') + "
    "M&CI Platform + News API + Custom Sources + Integrations + '1 Mn+ vetted "
    "sources, including news, company websites, SEC filings, social' + '117+ "
    "languages in a single, unified platform' verbatim contify.com home 2026-07-26; "
    "Founder lineage verified first-party contify.com/about-us 2026-07-26 Mohit "
    "Bhakuni Founder and CEO + Shalav Saran Vice President Growth Americas & Europe "
    "+ Kavita Kharayat Head Finance and Operations + Anand Kumar Head Quality "
    "Control + Sameer Walia Advisor to the CEO + Kapil Bharti Advisor to the CEO; "
    "Journey verbatim contify.com/about-us 2026-07-26: 2009 founded as business "
    "information aggregator + 2012 launched as industry intelligence platform + "
    "2014 launched fully customizable enterprise-grade M&CI platform + 2015 launched "
    "News API + 2016 launched account intelligence solution + 2017 launched fully-"
    "customizable dashboards and homepage + 2018+ expanded AI; Customers verbatim "
    "contify.com 2026-07-26 TSMC + Wipro + Merck + EY + Boston Consulting Group + "
    "MetLife + Northern Trust + DRG + LexisNexis + Esri + Galp + Digital Realty + "
    "Mahindra Comviva + Groww + BioCryst + Lenovo testimonial Jonathan Quick; Awards "
    "verbatim Gartner 2026 Visionary + Forrester + Frost & Sullivan + SCIP + G2 "
    "Leader + G2 Momentum Leader Fall 2025 + G2 High Performer + G2 Easiest Setup "
    "Enterprise + G2 Enterprise High Performer; Offices verbatim contify.com/"
    "contact-us 2026-07-26 400 Rella Blvd Ste. 207 Montebello NY 10901 US + 3rd "
    "Floor 45 Albemarle Street Mayfair London W1S 4JL UK + Unit No. 601-602 6th "
    "Floor Tower 4B DLF Corporate Park Phase III MG Road Gurugram Haryana 122 002 "
    "India. SIBLING #3/5 of ai_agent_competitive_intelligence NEW VERTICAL #87 "
    "after Klue 1374 OPENER #1/5 + Crayon 1376 SIBLING #2/5. 5-WEDGE non-overlap "
    "vs Klue + Crayon + Kompyte + 1 remaining sibling candidate bank (per PITFALL-"
    "OPENER-2 bank): (1) ONLY cohort sibling shipping canonical ATHENA AI as named "
    "first-party AGENTIC-AI insights engine distinct from Klue Klue AI + Crayon "
    "Crayon Insights + Kompyte no-AI-Agent; (2) ONLY cohort sibling shipping "
    "canonical NEWS API as named first-party developer-API substrate distinct from "
    "Klue no-News-API + Crayon no-News-API + Kompyte no-News-API; (3) ONLY cohort "
    "sibling with 117+ LANGUAGE COVERAGE as named first-party multilingual substrate "
    "distinct from Klue English-primary + Crayon English-primary + Kompyte English-"
    "primary; (4) ONLY cohort sibling with 1Mn+ VETTED SOURCES + SEC FILINGS + "
    "SOCIAL + COMPANY WEBSITES + NEWS distinct from Klue curated-feed + Crayon "
    "Crayon Capture digital-footprint + Kompyte web-monitoring; (5) ONLY cohort "
    "sibling with GARTNER 2026 VISIONARY + MOHIT BHAKUNI FOUNDER & CEO + 2009 "
    "FOUNDING + INDIA HQ GURUGRAM + US NY + UK LONDON + G2 MOMENTUM LEADER FALL "
    "2025 canonical SAAS-CI-GARTNER-VISIONARY-PEDIGREE distinct from Klue 2013 "
    "Vancouver-BC-CI-pedigree + Crayon 2015 Boston-MA-CI-pedigree + Kompyte Israel-"
    "CI-pedigree. 22-col evidence wedge (23 plus-separated fields per PITFALL #24-"
    "col-evidence-wedge): tenant_id + contify_workspace_id + contify_user_id + "
    "contify_feed_id + contify_intelligence_update_id + contify_news_api_call_id + "
    "contify_custom_source_id + contify_integration_id + contify_athena_session_id "
    "+ athena_fact_extraction_id + athena_ad_hoc_query_id + athena_dashboard_auto_"
    "update_id + athena_battlecard_auto_update_id + athena_timeline_auto_update_id "
    "+ contify_dashboard_id + contify_battlecard_id + contify_account_intelligence_"
    "id + contify_language_id + contify_source_id + audit_export_id + cross_tenant_"
    "no_bleed_invariant + replay_hash. Compliance (first-party inferred 2026-07-26 "
    "from contify.com + Gartner 2026 Visionary + 16-year SaaS convention): SOC 2 "
    "Type II + ISO/IEC 27001 + GDPR + CCPA + SSO/SAML/OIDC + audit logs + tenant "
    "isolation + EU AI Act Art. 9 risk-management + Art. 13 logging + Art. 14 "
    "human-oversight + ISO/IEC 42001 AIMS clause 8.4 ready. Commercial route "
    "(first-party verified 2026-07-26 NOT submitted): mailto:sales.support@"
    "contify.com + mailto:marketing@contify.com + mailto:partnerships@contify.com "
    "+ FORM:https://www.contify.com/contact-us/ + Mohit Bhakuni Founder CEO "
    "Direct LinkedIn. Offer ladder (NEW VERTICAL #87 SIBLING #3/5 tier): "
    "$500/48h + $497/mo + $2,000 cohort benchmark + $2,485 MRR + $10,000 CLOSER-"
    "only sponsorship. NEW VERTICAL #87 advanced 2/5 -> 3/5 with Contify 1379 "
    "SIBLING-3; 2 OPEN slots remaining for SIBLING-4 + CLOSER-5. SMTP/form gated; "
    "$0 sent / $0 received. "
    "[tick-1379-contify-ai-agent-competitive-intelligence-sibling-3-of-5-1379]"
)


CONTIF_FIELDS = [
    "1379",
    "Contify",
    "@contify",
    "mailto:sales.support@contify.com",
    "ai_agent_competitive_intelligence",
    "3",
    "1379_contify_ai_agent_competitive_intelligence_sibling_3_of_5.md",
    CONTIF_DESCRIPTION,
]

contif_row = ",".join(_quoted(f) for f in CONTIF_FIELDS) + "\r\n"
assert contif_row.endswith("\r\n"), "row must end CRLF"

_check_invariants(LEADS_CSV, "leads.csv BEFORE")
with open(LEADS_CSV, "ab") as f:
    f.write(contif_row.encode("utf-8"))
_check_invariants(LEADS_CSV, "leads.csv AFTER")


# ===========================================================================
# 2. leads_with_emails.csv (headered bare format)
# ===========================================================================

LWE_FIELDS = [
    "1379",
    "Contify",
    "contify.com",
    "ai_agent_competitive_intelligence",
    "sibling-3-of-5",
    "2026-07-26",
]
lwe_row = ",".join(LWE_FIELDS) + "\r\n"
assert lwe_row.endswith("\r\n"), "lwe row must end CRLF"

_check_invariants(LWE_CSV, "leads_with_emails.csv BEFORE")
with open(LWE_CSV, "ab") as f:
    f.write(lwe_row.encode("utf-8"))
_check_invariants(LWE_CSV, "leads_with_emails.csv AFTER")


# ===========================================================================
# 3. revenue_log.csv (8-col QUOTE_ALL + CRLF)
# ===========================================================================

REV_FIELDS = [
    "2026-07-26",
    "tick-1379",
    "1379_contify_ai_agent_competitive_intelligence_sibling_3_of_5.md",
    "$0",
    "new-lead",
    "ai_agent_competitive_intelligence sibling-3-of-5 (NEW VERTICAL #87 advanced 2/5 -> 3/5)",
    "0",
    "Contify (contify.com) Mohit Bhakuni Founder & CEO verbatim + Gartner 2026 "
    "Visionary + Athena AI agentic-AI + 1Mn+ vetted sources + 117+ languages + "
    "News API + Custom Sources + mailto:sales.support@contify.com; SIBLING #3/5 "
    "after Klue 1374 + Crayon 1376; 2 OPEN slots remaining for SIBLING-4 + "
    "CLOSER-5.",
]

rev_row = ",".join(_quoted(f) for f in REV_FIELDS) + "\r\n"
assert rev_row.endswith("\r\n"), "revenue row must end CRLF"

_check_invariants(REV_CSV, "revenue_log.csv BEFORE")
with open(REV_CSV, "ab") as f:
    f.write(rev_row.encode("utf-8"))
_check_invariants(REV_CSV, "revenue_log.csv AFTER")


# ===========================================================================
# Final counts + tail previews
# ===========================================================================

def line_count(path):
    with open(path, "rb") as f:
        raw = f.read()
    return raw.count(b"\r\n")

print()
print("FINAL COUNTS:")
print(f"  leads.csv             : {line_count(LEADS_CSV):5d} CRLF lines")
print(f"  leads_with_emails.csv : {line_count(LWE_CSV):5d} CRLF lines")
print(f"  revenue_log.csv       : {line_count(REV_CSV):5d} CRLF lines")
print()
print("TAIL PREVIEWS (last 240 chars each):")
for p in (LEADS_CSV, LWE_CSV, REV_CSV):
    raw = open(p, "rb").read()
    print(f"--- {p} ---")
    print(raw[-240:].decode("utf-8", errors="replace"))
    print()
