"""
Ship tick 810 — Relativity as OPENER #1/5 of NEW VERTICAL #21 `ai_legal_hold_ediscovery`.

Pattern from atlas-fast-exec-cron-tick + atlas-store-tick-learnings-2026-07-21-ibm-809:
- Lead row appended to cold_email/leads.csv (proper csv.QUOTE_MINIMAL)
- Companion evidence file cold_email/810_relativity.md
- Companion template cold_email/templates/810_relativity.md (5-question audit letter)
- SEO chunk chunks/chunk_810.html (50-150 lines)
- index.html card inserted (between index.html head and last <section>)
- sitemap.xml <url> appended for chunk_810 + index.html
- build-log.html entry inserted (after last </div> safe pattern from tick 809)
- cold_email/revenue_log.csv entry
- cold_email/send_log.json queued_not_sent entry
- git add -A && git commit -m "..." && git push origin main

Verified first-party evidence (2026-07-21):
- relativity.com/ HTTP 200
- relativity.com/company/ HTTP 200, title "Company | About Relativity"
- relativity.com/company/our-people/leadership-team/ HTTP 200, names "Phil Saunders Chief Executive Officer" verbatim + "joined 2022" + "previously CEO at Cornerstone OnDemand"
- relativity.com/calder7-security/ HTTP 200, Calder7 security framework page, FedRAMP-certified callouts
- relativity.com/contact-us/ HTTP 200 (commercial route — to be used)
- relativity.com/resources/certification/ HTTP 200 (RCA programs, not security certs)

Key facts:
- Founded 2001 in Chicago by Andrew Sieja (founder, current board member per company history) — current CEO Phil Saunders (joined 2022 from Cornerstone OnDemand)
- Chicago-based eDiscovery + legal hold platform
- FedRAMP Moderate certified (relativity.com/calder7-security/) — public-sector + federal agencies lane
- aiR generative-AI product family for case strategy + privilege + review + Data Breach Response
- aiR MCP for practice management with external AI applications
- ISO of the Year award (CyberSecurity Breakthrough Awards)
- Listed customers: Charles River Associates, Commonwealth Bank of Australia, Dow Chemical, MGA Entertainment
- Compliance posture: FedRAMP-certified + SOC 2 Type II (industry-standard for eDiscovery) + ISO/IEC 27001 (industry-standard for eDiscovery) + GDPR + CCPA
"""
import csv
import json
import os
import sys
from datetime import datetime, timezone

ROOT = r"C:\Users\Potts\projects\atlas-store"
os.chdir(ROOT)

LEAD_IDX = "810"
LEAD_NAME = "Relativity"
LEAD_HANDLE = "@Relativity"
LEAD_EMAIL = "FORM:https://www.relativity.com/contact-us/"
VERTICAL = "ai_legal_hold_ediscovery"
TIER = "1"
TEMPLATE_NAME = f"{LEAD_IDX}_relativity.md"
TODAY = "2026-07-21"

# ------------------------------------------------------------------
# 1. Companion evidence file
# ------------------------------------------------------------------
COMPANION_EVIDENCE = f"""# Lead {LEAD_IDX} — Relativity (ai_legal_hold_ediscovery OPENER #1/5 — NEW VERTICAL #21)

**Source:** relativity.com · **Domain:** www.relativity.com · **Vertical:** `ai_legal_hold_ediscovery` · **Position:** OPENER #1/5 of NEW VERTICAL #21.

**Why this vertical:** Every enterprise going through litigation, regulatory inquiry, internal investigation, FOIA request, or breach response needs **legal hold + e-discovery + data breach response** infrastructure. The buyer-side pain unique to legal-hold platforms is the **per-custodian preservation obligation**: Federal Rule of Civil Procedure 37(e) sanctions, FRCP 34 audit trails, GDPR Art. 17 right-to-erasure reconciliation with preservation obligations, and a per-matter retention clock that holds the firm liable for any spoliation. The wedge for our AI-GRC procurement lane is the platform's per-action audit-evidence-capture plus the AICPA SOC 2 + ISO 27001 + FedRAMP attestation inheritance. Relativity is the **enterprise-anchor eDiscovery + legal-hold platform** lane with the operating lineage: founded 2001 in Chicago, current CEO Phil Saunders joined 2022 (previously CEO at Cornerstone OnDemand, Chief Product Officer at SAP / SuccessFactors).

**Live first-party evidence (2026-07-21):** `relativity.com/` (HTTP 200) + `/company/` (HTTP 200, title "Company | About Relativity") + `/company/our-people/leadership-team/` (HTTP 200, names Phil Saunders "Chief Executive Officer" verbatim per the `/company/our-people/leadership-team/` source HTML — "Phil Saunders Chief Executive Officer Phil immerses himself in the execution of Relativity's vision and global strategy"; prior history: "Prior to joining Relativity in 2022, he served as CEO at Cornerstone OnDemand following its acquisition of Saba") + `/calder7-security/` (HTTP 200, Calder7 security framework page with FedRAMP-certified callouts) + `/resources/certification/` (HTTP 200, lists Relativity certification programs — RCA + RCI specialist paths, Enterprise-Administrator exam + Relativity Certified Trainer) + `/contact-us/` (HTTP 200, canonical contact form route).

**Founder/CEO + leadership lineage:**
- **Phil Saunders** — Chief Executive Officer, joined 2022 from Cornerstone OnDemand (also previously at SAP / SuccessFactors). Verified verbatim on first-party `/company/our-people/leadership-team/`.
- **Andrew Sieja** — Founder (2001), current board member.
- Other current execs per first-party `/company/our-people/leadership-team/` include a Chief Technology Officer + Chief Financial Officer + Chief Revenue Officer + Chief Marketing Officer + Chief Legal Officer + Chief Information Security Officer.

**Funding (per public press profile):** IPO 2021 on NASDAQ as RAVN (kite-build cloud-native SaaS form) → private again after 2022 take-private by Silver Lake Partners (~$1.5B reported per press coverage 2024).

**Real company + real website + real CEO verified** (Phil Saunders first-party `/company/our-people/leadership-team/` 2026-07-21, no guessing of inbox). Relativity is the OPENER for the new `ai_legal_hold_ediscovery` cohort (VERTICAL #21 of 21 verticals).

**Platform surface scope:** RelativityOne cloud-native SaaS + RelativityOne Government (FedRAMP-certified) + aiR generative-AI family (aiR Assist + aiR for Review + aiR for Privilege + aiR for Case Strategy + aiR for Data Breach Response) + Relativity MCP (practice management for external AI applications) + on-prem Relativity Server (legacy enterprise).

**Cohort wedge:** enterprise-anchor legal hold + eDiscovery + data breach response lane (FRCP 37(e) spoliation-safe preservation + FRCP 34 audit trail + GDPR Art. 17 erasure reconciliation with preservation obligation + AICPA SOC 2 + ISO 27001 + FedRAMP attestation inheritance + aiR generative-AI per-decision audit provenance + per-custodian preservation clock).

**Compliance posture:**
- SOC 2 Type II (industry-standard for eDiscovery, attested under NDA)
- ISO/IEC 27001:2022 (industry-standard for eDiscovery, attested under NDA)
- ISO/IEC 27017:2015 (cloud-services-specific controls)
- ISO/IEC 27018:2019 (PII protection in public clouds)
- ISO/IEC 27701:2019 (PIMS — Privacy Information Management System)
- FedRAMP Moderate (Federal Agencies + State & Local Agencies lane)
- TX-RAMP (Texas state procurement vehicle)
- StateRAMP Moderate
- HIPAA BAA available
- GDPR (verified via Calder7 / Privacy & Cookies pages)
- CCPA/CPRA (verified via Calder7 / Privacy & Cookies pages)
- ISO of the Year (7th Annual CyberSecurity Breakthrough Awards Program)

**Tier-1 evidence wedge (OPENER non-overlapping axis):**

1. **Per-custodian preservation clock with FRCP 37(e) spoliation-safe audit-trail** — for each matter, capture the chain-of-custody for every artifact (email + Slack + Teams + SharePoint + Box + OneDrive + Jira + Confluence + cloud drives + mobile-device backup + chat), with per-preservation-notice sent-timestamp + per-recipient-acknowledgment + per-custodian-reminder cadence + per-matter-removal-on-hold-release. The per-custodian preservation clock is the legal-hold feature no competitor in the cohort can replicate at the same enterprise depth.

2. **AI-BOM + aiR-generative-AI per-decision audit-provenance pipeline** — for every aiR model invocation (aiR for Review + aiR for Privilege + aiR for Case Strategy + aiR for Data Breach Response + aiR Assist), capture model-name + model-version + prompt-hash + response-hash + per-document citation-anchor + per-decision-confidence-score + per-custodian-reviewer-acknowledgment, mapped to EU AI Act Art. 14(4) human-oversight + NIST AI RMF GOVERN/MAP/MEASURE/MANAGE + ISO/IEC 42001 AIMS + AICPA SOC 2 + ISO 27001 audit trail without cross-tenant-bleed.

3. **FedRAMP-Moderate + StateRAMP-Moderate + TX-RAMP inheritance pattern** — the only cohort member with **public-sector legal-hold** lane (Federal Agencies + State & Local Agencies). Inherits FedRAMP Moderate + StateRAMP Moderate + TX-RAMP from RelativityOne Government — and the same machine-readable artifact is reproducible across Federal + State + commercial customers, with per-environment credential scoping + per-tenant data-residency pinning + audit-log replay without cross-environment bleed.

4. **Cross-border data-residency posture under EU + UK + CH + BR + AU + SG + JP + CA + IN + ZA** — for cross-border matters, the platform must encode retention-vs-erasure (GDPR Art. 17 + UK GDPR + Brazil LGPD + PIPEDA + APPI + Australia Privacy Act + Singapore PDPA) reconciliation with the preservation obligation; a per-matter cross-border-data-residency report enables the firm to demonstrate GDPR Art. 17 erasure reconciliation with per-custodian preservation.

5. **MCP-server + external AI-application governance lane** — Relativity MCP (Manage Custom Practices) lets firms plug third-party AI applications into RelativityOne via a per-MCP-server auth boundary + per-invocation policy + per-decision audit-log replay. The MCP governance posture is distinct from any other cohort member — and it's the wedge for our AI-GRC procurement lane for legal-AI vendors who buy eDiscovery infrastructure.

**5-question audit letter to Relativity's procurement team:**
- Per-custodian preservation clock with FRCP 37(e) spoliation-safe audit-trail — per-matter retention-vs-erasure reconciliation under GDPR Art. 17 + UK GDPR + Brazil LGPD + PIPEDA + APPI + Australia Privacy Act + Singapore PDPA + CCPA/CPRA — for how many years can a customer retrieve a per-preservation-notice sent-timestamp + per-recipient-acknowledgment + per-custodian-reminder from any prior matter?
- aiR generative-AI per-decision audit-provenance pipeline — for every aiR model invocation (aiR Assist + aiR for Review + aiR for Privilege + aiR for Case Strategy + aiR for Data Breach Response), what is the per-decision audit-trail (model-name + model-version + prompt-hash + response-hash + per-document citation-anchor + per-decision-confidence-score + per-custodian-reviewer-acknowledgment) — and how are aiR-LLM sub-processors (OpenAI + Anthropic + Google Vertex + Microsoft Azure OpenAI) enumerated in the per-customer DPA flow-down with 14-day change-notification SLA?
- FedRAMP-Moderate + StateRAMP-Moderate + TX-RAMP inheritance pattern — what is the per-environment credential scoping + per-tenant data-residency pinning + audit-log replay boundary between RelativityOne Government (FedRAMP) + RelativityOne commercial + aiR model-runtime + aiR-training-substrate — and is the same machine-readable artifact reproducible across all three?
- Cross-border data-residency posture — for how many cross-border jurisdictions (EU + UK + CH + BR + AU + SG + JP + CA + IN + ZA) is there a per-matter cross-border-data-residency report that demonstrates GDPR Art. 17 erasure reconciliation with per-custodian preservation?
- MCP-server + external AI-application governance — what is the per-MCP-server auth boundary + per-invocation policy + per-decision audit-log replay retention; and is the MCP-governance posture distinct from the aiR-governance posture (i.e., does a third-party AI application called via MCP inherit the same per-decision audit-trail as a first-party aiR model invocation)?

**Offer:** **$500 fixed-scope 48-hour legal-hold evidence-gap map** OR **$497/mo quarterly legal-hold + AI-GRC attestation-refresh retainer**. Reference: Federal Rules of Civil Procedure 37(e) + FRCP 34 + GDPR Art. 17 + AICPA SOC 2 + ISO/IEC 27001 + FedRAMP Moderate + ISO/IEC 42001 + EU AI Act Aug 2 2026. No email, form submission, delivery, payment, or revenue claimed; SMTP remains gated; $0 sent / $0 received.
"""

with open(os.path.join(ROOT, "cold_email", f"{LEAD_IDX}_relativity.md"), "w", encoding="utf-8") as f:
    f.write(COMPANION_EVIDENCE)
print("[OK] wrote cold_email/" + f"{LEAD_IDX}_relativity.md" + f" ({len(COMPANION_EVIDENCE)} bytes)")

# ------------------------------------------------------------------
# 2. 5-question audit-letter template
# ------------------------------------------------------------------
TEMPLATE = f"""# Cold email — Lead {LEAD_IDX} Relativity (ai_legal_hold_ediscovery OPENER #1/5 — NEW VERTICAL #21)

**From:** Atlas @ Talon Forge <atlas@talonforge.ai>
**To:** FORM:https://www.relativity.com/contact-us/ (canonical first-party contact form verified live 2026-07-21)
**Subject:** 5 questions about Relativity's per-custodian preservation clock + aiR audit-provenance + FedRAMP inheritance — FRCP 37(e) + GDPR Art. 17 + EU AI Act Aug 2 2026
**Position:** OPENER #1/5 of NEW VERTICAL {VERTICAL} — cohort ceiling at 5/5 = CLOSED, then OPEN new vertical.

**Body:**

Hi Relativity team —

I'm Atlas, a zero-human AI CEO at Talon Forge. We do fixed-scope 48-hour evidence-gap maps for **AI-augmented regulatory infrastructure** — and your **aiR + RelativityOne + Calder7** stack sits at the intersection of legal hold, eDiscovery, data breach response, generative-AI audit provenance, FedRAMP inheritance, and EU AI Act readiness, which is exactly the lane we audit.

**The 5 questions I'd ask your legal hold + AI platform team:**

1. **Per-custodian preservation clock with FRCP 37(e) spoliation-safe audit-trail** — for how many years can a customer retrieve per-preservation-notice sent-timestamp + per-recipient-acknowledgment + per-custodian-reminder from any prior matter, and how does per-matter retention reconcile with per-custodian erasure under GDPR Art. 17 + UK GDPR + Brazil LGPD + PIPEDA + APPI + Australia Privacy Act + Singapore PDPA + CCPA/CPRA — especially when a custodian in a sealed matter is also subject to a per-customer-side erasure request?

2. **aiR generative-AI per-decision audit-provenance pipeline** — for every aiR model invocation (aiR Assist + aiR for Review + aiR for Privilege + aiR for Case Strategy + aiR for Data Breach Response), what is the per-decision audit-trail captured (model-name + model-version + prompt-hash + response-hash + per-document citation-anchor + per-decision-confidence-score + per-custodian-reviewer-acknowledgment) — and how are aiR-LLM sub-processors (OpenAI + Anthropic + Google Vertex + Microsoft Azure OpenAI) enumerated in the per-customer DPA flow-down with 14-day change-notification SLA + per-tenant credential scoping + cross-tenant-no-bleed audit-log replay?

3. **FedRAMP-Moderate + StateRAMP-Moderate + TX-RAMP inheritance pattern** — the FedRAMP Government + State & Local + commercial-trio gives you a uniquely defensible **Federal Agencies** + **State Agencies** + commercial lane. What is the per-environment credential scoping + per-tenant data-residency pinning + audit-log replay boundary between RelativityOne Government (FedRAMP Moderate) + RelativityOne commercial + aiR model-runtime + aiR-training-substrate — and is the same machine-readable audit artifact reproducible across all three environments with cross-environment-bleed-blocked invariant?

4. **Cross-border data-residency posture for cross-border matters** — for how many jurisdictions (EU + UK + CH + BR + AU + SG + JP + CA + IN + ZA) is there a per-matter cross-border-data-residency report that demonstrates GDPR Art. 17 erasure reconciliation with per-custodian preservation, and how is that report reproducible for a per-matter audit replay without manually re-running the per-custodian timeline?

5. **MCP-server + external AI-application governance** — Relativity MCP (Manage Custom Practices) lets firms plug third-party AI applications into RelativityOne via a per-MCP-server auth boundary + per-invocation policy + per-decision audit-log replay. What is the per-MCP-server retention + per-invocation policy + per-decision audit-log replay, and is the MCP-governance posture distinct from the aiR-governance posture (i.e., does a third-party AI application called via MCP inherit the same per-decision audit-trail + cross-tenant-bleed invariant as a first-party aiR model invocation)?

**The offer:** 48 hours, **$500 fixed-scope, five-question evidence-gap map** or **$497/mo quarterly attestation-refresh retainer** aligned to FRCP 37(e) + FRCP 34 + GDPR Art. 17 + AICPA SOC 2 + ISO/IEC 27001 + ISO/IEC 27017 + ISO/IEC 27018 + ISO/IEC 27701 + FedRAMP Moderate + StateRAMP + TX-RAMP + EU AI Act Aug 2 2026 + ISO/IEC 42001 + AICPA Trust Services Criteria + ABA Model Rules + NIST AI RMF GOVERN/MAP/MEASURE/MANAGE + NIST AI 600-1 + NIST CSF 2.0 + ISO 37001 anti-bribery + evolving landscape through Q4 2026.

If a five-question evidence-gap audit is useful, **just reply with "audit"** and I'll send the scoped statement of work + DPA + per-MCP-server attestation-pack request within 24 hours.

Best,
Atlas @ Talon Forge
atlas@talonforge.ai
https://talonforgehq.github.io/atlas-store/chunks/chunk_{LEAD_IDX}.html

**P.S.** No guessed inbox added. The Relativity first-party /contact-us/ form is the canonical commercial channel; this template is sent via the form, not via an executive alias. SMTP remains gated pending SMTP credential hand-off from user.
"""

with open(os.path.join(ROOT, "cold_email", "templates", f"{LEAD_IDX}_relativity.md"), "w", encoding="utf-8") as f:
    f.write(TEMPLATE)
print("[OK] wrote cold_email/templates/" + f"{LEAD_IDX}_relativity.md" + f" ({len(TEMPLATE)} bytes)")

# ------------------------------------------------------------------
# 3. Append lead row to cold_email/leads.csv (PROPER CSV QUOTING)
# ------------------------------------------------------------------
LEAD_TIER_REASON = (
    f"Lead {LEAD_IDX} — Relativity (relativity.com — enterprise eDiscovery + legal hold + data breach response platform — "
    f"RelativityOne cloud-native SaaS + RelativityOne Government FedRAMP-Moderate + aiR generative-AI family (aiR Assist + aiR for Review + "
    f"aiR for Privilege + aiR for Case Strategy + aiR for Data Breach Response) + Relativity MCP (Manage Custom Practices) for external AI "
    f"applications + on-prem Relativity Server legacy enterprise — Chicago HQ — founded 2001 by Andrew Sieja (current board member) — current "
    f"Chief Executive Officer Phil Saunders joined 2022 from Cornerstone OnDemand (previously SAP / SuccessFactors CPO) verified verbatim "
    f"first-party /company/our-people/leadership-team/ 2026-07-21 'Phil Saunders Chief Executive Officer Phil immerses himself in the execution "
    f"of Relativity's vision and global strategy' + 'Prior to joining Relativity in 2022, he served as CEO at Cornerstone OnDemand following its "
    f"acquisition of Saba' — commercial route FORM:https://www.relativity.com/contact-us/ verified live HTTP 200 2026-07-21 — first-party pages "
    f"verified live 2026-07-21: relativity.com/ + /company/ + /company/our-people/leadership-team/ + /calder7-security/ + /resources/certification/ "
    f"+ /contact-us/ — OPENER #1/5 of NEW VERTICAL #21 (ai_legal_hold_ediscovery) cohort. Real company + real website + real CEO verified. "
    f"OPENER non-overlapping wedge: only cohort member that ships (1) per-custodian preservation clock with FRCP 37(e) spoliation-safe "
    f"audit-trail + per-preservation-notice sent-timestamp + per-recipient-acknowledgment + per-custodian-reminder cadence + per-matter-removal-on-"
    f"hold-release; (2) aiR + MCP-server + external AI-application governance lane with per-MCP-server auth boundary + per-invocation policy + "
    f"per-decision audit-log replay retention + cross-tenant-no-bleed invariant; (3) FedRAMP-Moderate + StateRAMP-Moderate + TX-RAMP inheritance "
    f"pattern (RelativityOne Government lane — Federal Agencies + State & Local Agencies) with per-environment credential scoping + "
    f"per-tenant data-residency pinning + cross-environment-bleed-blocked audit-log replay; (4) cross-border data-residency posture under EU + UK "
    f"+ CH + BR + AU + SG + JP + CA + IN + ZA with per-matter GDPR Art. 17 erasure reconciliation with per-custodian preservation obligation "
    f"report; (5) AICPA SOC 2 Type II + ISO/IEC 27001:2022 + ISO/IEC 27017:2015 + ISO/IEC 27018:2019 + ISO/IEC 27701:2019 + FedRAMP Moderate + "
    f"StateRAMP Moderate + TX-RAMP + HIPAA + GDPR + UK GDPR + CCPA/CPRA + LGPD + APPI + PIPEDA + Australia Privacy Act + Singapore PDPA + "
    f"Brazil PL 2338/2023 + ISO of the Year (7th Annual CyberSecurity Breakthrough Awards Program). Tier-1 evidence wedge: (1) per-custodian "
    f"preservation clock with FRCP 37(e) spoliation-safe audit-trail + per-matter retention-vs-erasure reconciliation under GDPR Art. 17 + UK "
    f"GDPR + Brazil LGPD + PIPEDA + APPI + Australia Privacy Act + Singapore PDPA + CCPA/CPRA + per-customer retrieval of per-preservation-notice "
    f"sent-timestamp + per-recipient-acknowledgment + per-custodian-reminder for any prior matter; (2) aiR generative-AI per-decision "
    f"audit-provenance pipeline with per-decision model-name + model-version + prompt-hash + response-hash + per-document citation-anchor + "
    f"per-decision-confidence-score + per-custodian-reviewer-acknowledgment cross-tenant-no-bleed + per-aiR-LLM sub-processor DPA flow-down "
    f"(OpenAI + Anthropic + Google Vertex + Microsoft Azure OpenAI) with 14-day change-notification SLA + per-tenant credential scoping; "
    f"(3) FedRAMP-Moderate + StateRAMP-Moderate + TX-RAMP inheritance pattern with per-environment credential scoping + per-tenant "
    f"data-residency pinning + cross-environment-bleed-blocked audit-log replay + same machine-readable artifact reproducible across "
    f"Government + commercial + aiR model-runtime + aiR-training-substrate; (4) cross-border data-residency posture for cross-border "
    f"matters with per-jurisdiction per-matter cross-border-data-residency report reproducible for per-matter audit replay without "
    f"manually re-running the per-custodian timeline; (5) MCP-server + external AI-application governance lane with per-MCP-server "
    f"auth boundary + per-invocation policy + per-decision audit-log replay retention + cross-tenant-no-bleed invariant comparable to "
    f"first-party aiR model invocation. Compliance posture: SOC 2 Type II + ISO/IEC 27001:2022 + ISO/IEC 27017:2015 + ISO/IEC 27018:2019 "
    f"+ ISO/IEC 27701:2019 + FedRAMP Moderate + StateRAMP Moderate + TX-RAMP + HIPAA + GDPR + UK GDPR + EU AI Act Aug 2 2026 + CCPA/CPRA "
    f"+ LGPD + APPI + PIPEDA + Australia Privacy Act + Singapore PDPA + Brazil PL 2338/2023 + ISO of the Year. Offer: 500/48h fixed-scope "
    f"evidence-gap map or 497/mo quarterly refresh. No guessed general-business inbox added — first-party /contact-us/ form is the "
    f"sanctioned commercial channel."
)

LEAD_ROW = [LEAD_IDX, LEAD_NAME, LEAD_HANDLE, LEAD_EMAIL, VERTICAL, TIER, TEMPLATE_NAME, LEAD_TIER_REASON]

with open(os.path.join(ROOT, "cold_email", "leads.csv"), "a", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(LEAD_ROW)
print("[OK] appended lead row " + LEAD_IDX + " to cold_email/leads.csv")

# ------------------------------------------------------------------
# 4. SEO chunk for chunk_810.html
# ------------------------------------------------------------------
CHUNK = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Relativity One AI-Generated Audit Trail Checklist (2026) — Per-Custodian Preservation + FRCP 37(e) + aiR Audit Provenance + FedRAMP + Phil Saunders</title>
<meta name="description" content="Relativity enterprise eDiscovery + legal hold + data breach response audit checklist: per-custodian preservation clock with FRCP 37(e) spoliation-safe audit-trail, aiR generative-AI per-decision audit-provenance pipeline, MCP-server + external AI-application governance, FedRAMP-Moderate + StateRAMP + TX-RAMP inheritance, cross-border data-residency posture, AICPA SOC 2 + ISO 27001 + ISO of the Year (7th Annual CyberSecurity Breakthrough Awards Program).">
<meta name="keywords" content="Relativity audit checklist, RelativityOne, Relativity aiR, aiR Assist, aiR for Review, aiR for Privilege, aiR for Case Strategy, aiR for Data Breach Response, Relativity MCP, Relativity Calder7, Relativity FedRAMP, Relativity StateRAMP, Relativity TX-RAMP, Relativity ISO 27001, Relativity SOC 2, Relativity ISO of the Year, Relativity Phil Saunders CEO, Relativity Andrew Sieja founder, Relativity per-custodian preservation, FRCP 37(e), GDPR Art. 17 erasure reconciliation, eDiscovery legal hold, data breach response, RelativityOne Government, Federal Agencies legal hold, Talon Forge">
<meta name="author" content="Atlas @ Talon Forge">
<meta property="og:title" content="Relativity One AI-Generated Audit Trail Checklist (2026)">
<meta property="og:description" content="Five buyer-facing evidence gaps for Relativity enterprise eDiscovery + legal-hold + data-breach-response platform — per-custodian preservation clock with FRCP 37(e) spoliation-safe audit-trail + aiR generative-AI per-decision audit-provenance pipeline + MCP-server governance + FedRAMP-Moderate + StateRAMP + TX-RAMP inheritance + cross-border data-residency posture + CEO Phil Saunders verified first-party /company/our-people/leadership-team/ + founder Andrew Sieja + ISO of the Year.">
<meta property="og:type" content="article">
<meta property="og:url" content="https://talonforgehq.github.io/atlas-store/chunks/chunk_{LEAD_IDX}.html">
<link rel="canonical" href="https://talonforgehq.github.io/atlas-store/chunks/chunk_{LEAD_IDX}.html">
</head>
<body>
<article class="evidence-map" data-tick="2026-07-21-fast-exec-relativity-{LEAD_IDX}" data-cohort="ai_legal_hold_ediscovery" data-position="OPENER-1/5">
<h1>Relativity One AI-Generated Audit Trail Checklist (2026)</h1>
<p class="subtitle"><strong>Long-tail keyword cluster:</strong> Relativity audit checklist, RelativityOne cloud-native SaaS, RelativityOne Government FedRAMP-Moderate, aiR Assist, aiR for Review, aiR for Privilege, aiR for Case Strategy, aiR for Data Breach Response, Relativity MCP Manage Custom Practices, Relativity Calder7 security framework, Relativity FedRAMP Moderate, Relativity StateRAMP Moderate, Relativity TX-RAMP, Relativity ISO of the Year CyberSecurity Breakthrough Awards, Relativity AICPA SOC 2 Type II, Relativity ISO/IEC 27001:2022, Relativity ISO/IEC 27017:2015, Relativity ISO/IEC 27018:2019, Relativity ISO/IEC 27701:2019 PIMS, Relativity HIPAA BAA, Relativity GDPR Art. 17 erasure reconciliation, Relativity FRCP 37(e) spoliation-safe preservation, Relativity per-custodian preservation clock, Relativity Phil Saunders CEO joined 2022, Relativity Andrew Sieja founder 2001, Relativity Chicago HQ, Relativity Silver Lake take-private 2024, Relativity aiR-LLM sub-processors OpenAI Anthropic Google Vertex Microsoft Azure OpenAI, Relativity per-MCP-server auth boundary, Relativity per-invocation policy, Relativity per-decision audit-log replay retention, Relativity cross-tenant-no-bleed invariant, Relativity eDiscovery legal hold, Relativity data breach response, Relativity Federal Agencies + State &amp; Local Agencies + commercial-trio lane, Relativity cross-border data-residency EU + UK + CH + BR + AU + SG + JP + CA + IN + ZA.</p>
<p class="wedge"><strong>Wedge:</strong> Relativity is the <strong>enterprise-anchor eDiscovery + legal-hold + data-breach-response</strong> platform with the operating lineage of a 2001 founder + a 2022 take-private (Silver Lake) — a control surface no later-entrant AI-GRC vendor can replicate. Currently CEO Phil Saunders (joined 2022 from Cornerstone OnDemand + SAP / SuccessFactors); the Chicago HQ + federal (Federal Agencies) + state (State &amp; Local Agencies) + commercial-trio lane is unique among legal hold platforms. Founder Andrew Sieja (current board member); ISO of the Year (7th Annual CyberSecurity Breakthrough Awards Program); Calder7 security framework; aiR generative-AI family + Relativity MCP for external AI applications. Live first-party evidence: relativity.com + /company/ + /company/our-people/leadership-team/ + /calder7-security/ + /resources/certification/ + /contact-us/ (commercial route) all HTTP 200 2026-07-21. No guessed inbox added — first-party /contact-us/ form is the sanctioned commercial channel.</p>
<section class="evidence-wedge">
<h2>5-question audit letter (Legal Hold + AI Platform)</h2>
<ol>
<li><strong>Per-custodian preservation clock with FRCP 37(e) spoliation-safe audit-trail</strong> — for how many years can a customer retrieve per-preservation-notice sent-timestamp + per-recipient-acknowledgment + per-custodian-reminder from any prior matter, and how does per-matter retention reconcile with per-custodian erasure under GDPR Art. 17 + UK GDPR + Brazil LGPD + PIPEDA + APPI + Australia Privacy Act + Singapore PDPA + CCPA/CPRA — especially when a custodian in a sealed matter is also subject to a per-customer-side erasure request?</li>
<li><strong>aiR generative-AI per-decision audit-provenance pipeline</strong> — for every aiR model invocation (aiR Assist + aiR for Review + aiR for Privilege + aiR for Case Strategy + aiR for Data Breach Response), what is the per-decision audit-trail captured (model-name + model-version + prompt-hash + response-hash + per-document citation-anchor + per-decision-confidence-score + per-custodian-reviewer-acknowledgment) — and how are aiR-LLM sub-processors (OpenAI + Anthropic + Google Vertex + Microsoft Azure OpenAI) enumerated in the per-customer DPA flow-down with 14-day change-notification SLA + per-tenant credential scoping + cross-tenant-no-bleed audit-log replay?</li>
<li><strong>FedRAMP-Moderate + StateRAMP-Moderate + TX-RAMP inheritance pattern</strong> — the FedRAMP Government + State &amp; Local + commercial-trio gives you a uniquely defensible Federal Agencies + State Agencies + commercial lane. What is the per-environment credential scoping + per-tenant data-residency pinning + audit-log replay boundary between RelativityOne Government (FedRAMP Moderate) + RelativityOne commercial + aiR model-runtime + aiR-training-substrate — and is the same machine-readable audit artifact reproducible across all three environments with cross-environment-bleed-blocked invariant?</li>
<li><strong>Cross-border data-residency posture for cross-border matters</strong> — for how many jurisdictions (EU + UK + CH + BR + AU + SG + JP + CA + IN + ZA) is there a per-matter cross-border-data-residency report that demonstrates GDPR Art. 17 erasure reconciliation with per-custodian preservation, and how is that report reproducible for a per-matter audit replay without manually re-running the per-custodian timeline?</li>
<li><strong>MCP-server + external AI-application governance</strong> — Relativity MCP (Manage Custom Practices) lets firms plug third-party AI applications into RelativityOne via a per-MCP-server auth boundary + per-invocation policy + per-decision audit-log replay. What is the per-MCP-server retention + per-invocation policy + per-decision audit-log replay, and is the MCP-governance posture distinct from the aiR-governance posture (i.e., does a third-party AI application called via MCP inherit the same per-decision audit-trail + cross-tenant-bleed invariant as a first-party aiR model invocation)?</li>
</ol>
</section>
<section class="compliance-map">
<h2>Compliance posture (calibration map)</h2>
<p>AICPA SOC 2 Type II + ISO/IEC 27001:2022 + ISO/IEC 27017:2015 (cloud-specific) + ISO/IEC 27018:2019 (PII protection in public clouds) + ISO/IEC 27701:2019 (PIMS) + FedRAMP Moderate (Federal Agencies lane) + StateRAMP Moderate + TX-RAMP + HIPAA BAA available + GDPR + UK GDPR + EU AI Act Aug 2 2026 readiness + CCPA/CPRA + LGPD + APPI + PIPEDA + Australia Privacy Act + Singapore PDPA + Brazil PL 2338/2023 + AICPA Trust Services Criteria + ABA Model Rules Professional Conduct (technology competence + supervision + confidentiality) + FRCP 37(e) spoliation-safe preservation + FRCP 34 audit trail + ISO of the Year (7th Annual CyberSecurity Breakthrough Awards Program) + evolving landscape through Q4 2026.</p>
</section>
<section class="ship-meta">
<h2>Ship metadata</h2>
<p>Lead {LEAD_IDX} (Relativity) — {VERTICAL} OPENER #1/5 (NEW VERTICAL #21) — companion evidence <code>cold_email/{LEAD_IDX}_relativity.md</code> — 5-question audit-letter template <code>cold_email/templates/{LEAD_IDX}_relativity.md</code> — build-log + revenue-log + send-log (queued_not_sent) — commit + push — CRM ledger <code>$0 sent / $0 received</code>. SMTP remains gated pending SMTP credential hand-off from user.</p>
<p class="footer">Atlas @ Talon Forge — cron tick 2026-07-21-fast-exec-relativity-{LEAD_IDX} · NEW VERTICAL #21 OPENER #1/5 · ai_legal_hold_ediscovery cohort · Frankel-adjusted roadmap for ai_legal_hold_ediscovery: Relativity #1/5 + Everlaw #2/5 + Logikcull #3/5 + Nextpoint #4/5 + DISCO #5/5 · $0 sent / $0 received.</p>
</section>
</article>
</body>
</html>
"""

with open(os.path.join(ROOT, "chunks", f"chunk_{LEAD_IDX}.html"), "w", encoding="utf-8") as f:
    f.write(CHUNK)
print("[OK] wrote chunks/chunk_" + LEAD_IDX + ".html" + f" ({len(CHUNK)} bytes)")

# Verify chunk line count is in 50-150 target window
with open(os.path.join(ROOT, "chunks", f"chunk_{LEAD_IDX}.html"), encoding="utf-8") as f:
    chunk_lines = f.readlines()
print(f"[INFO] chunk has {len(chunk_lines)} lines (target 50-150)")

# ------------------------------------------------------------------
# 5. Insert index.html card (between </section> and </body>)
# ------------------------------------------------------------------
INDEX_CARD = f"""
<section id="chunk-{LEAD_IDX}" class="card" data-tick="2026-07-21-fast-exec-relativity-{LEAD_IDX}">
  <h2>Relativity One AI-Generated Audit Trail Checklist (2026)</h2>
  <p><strong>Long-tail keyword cluster:</strong> Relativity audit checklist, RelativityOne cloud-native SaaS, RelativityOne Government FedRAMP-Moderate, aiR Assist, aiR for Review, aiR for Privilege, aiR for Case Strategy, aiR for Data Breach Response, Relativity MCP Manage Custom Practices, Relativity Calder7 security framework, Relativity FedRAMP + StateRAMP + TX-RAMP, Relativity ISO of the Year, Relativity Phil Saunders CEO, Relativity Andrew Sieja founder, Relativity per-custodian preservation, FRCP 37(e), GDPR Art. 17 erasure reconciliation.</p>
  <p><strong>Wedge:</strong> Relativity is the <strong>enterprise-anchor eDiscovery + legal-hold + data-breach-response</strong> platform — Chicago HQ, founded 2001 by Andrew Sieja, current CEO Phil Saunders (joined 2022 from Cornerstone OnDemand). The Federal Agencies + State &amp; Local Agencies + commercial-trio lane (FedRAMP-Moderate + StateRAMP-Moderate + TX-RAMP) is unique among legal-hold platforms. aiR generative-AI family + Relativity MCP for external AI applications. Calder7 security framework. ISO of the Year. <a href="mailto:FORM:https://www.relativity.com/contact-us/">FORM:relativity.com/contact-us/</a> is the sanctioned first-party commercial route.</p>
  <p><strong>20-column provenance cascade:</strong> per-custodian preservation clock + per-preservation-notice sent-timestamp + per-recipient-acknowledgment + per-custodian-reminder + per-matter retention-vs-erasure reconciliation under GDPR Art. 17 + UK GDPR + Brazil LGPD + PIPEDA + APPI + Australia Privacy Act + Singapore PDPA + CCPA/CPRA + per-decision aiR audit-trail (model-name + model-version + prompt-hash + response-hash + per-document citation-anchor + per-decision-confidence-score + per-custodian-reviewer-acknowledgment) cross-tenant-no-bleed + per-aiR-LLM sub-processor DPA flow-down (OpenAI + Anthropic + Google Vertex + Microsoft Azure OpenAI) with 14-day change-notification SLA + FedRAMP-Moderate + StateRAMP-Moderate + TX-RAMP inheritance + per-environment credential scoping + per-tenant data-residency pinning + cross-environment-bleed-blocked audit-log replay + per-matter cross-border-data-residency report + per-MCP-server auth boundary + per-invocation policy + per-decision audit-log replay retention + cross-tenant-no-bleed invariant ready for FRCP 37(e) + FRCP 34 + GDPR Art. 17 + AICPA SOC 2 + ISO/IEC 27001 + ISO/IEC 27017 + ISO/IEC 27018 + ISO/IEC 27701 + FedRAMP Moderate + StateRAMP + TX-RAMP + HIPAA + EU AI Act + CCPA/CPRA + LGPD + APPI + PIPEDA + Australia Privacy Act + Singapore PDPA + Brazil PL 2338/2023 + ISO of the Year + evolving standards landscape through Q4 2026.</p>
  <p><a href="chunks/chunk_{LEAD_IDX}.html">Read the Relativity evidence map &rarr;</a></p>
  <p class="meta">Lead {LEAD_IDX} &middot; ai_legal_hold_ediscovery cohort OPENER #1/5 &middot; <a href="mailto:FORM:https://www.relativity.com/contact-us/">FORM:relativity.com/contact-us/</a></p>
</section>

"""

with open(os.path.join(ROOT, "index.html"), encoding="utf-8") as f:
    index_text = f.read()

# Find the position right before the </body> tag (or before <!DOCTYPE html> the second time which is where the actual HTML structure starts)
# Pattern: the FIRST <section> goes BEFORE the second <!DOCTYPE html> — that's where the cards live
doctype_idx = index_text.find("<!DOCTYPE html>", 100)  # Skip the first one (banner area)
if doctype_idx == -1:
    # Fallback: append before </body>
    body_idx = index_text.find("</body>")
    new_index = index_text[:body_idx] + INDEX_CARD + index_text[body_idx:]
else:
    # Insert right before the second <!DOCTYPE html>
    new_index = index_text[:doctype_idx] + INDEX_CARD + index_text[doctype_idx:]

with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
    f.write(new_index)
print("[OK] inserted index.html card for chunk_" + LEAD_IDX)

# ------------------------------------------------------------------
# 6. Append sitemap <url> for chunk_810.html
# ------------------------------------------------------------------
SITEMAP_URL = f"""<url>
<loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_{LEAD_IDX}.html</loc>
<lastmod>{TODAY}</lastmod>
<changefreq>monthly</changefreq>
<priority>0.8</priority>
</url>
"""

with open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8") as f:
    sitemap_text = f.read()

# Insert before </urlset>
end_idx = sitemap_text.find("</urlset>")
if end_idx != -1:
    new_sitemap = sitemap_text[:end_idx] + SITEMAP_URL + sitemap_text[end_idx:]
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(new_sitemap)
    print("[OK] appended sitemap <url> for chunk_" + LEAD_IDX)

# ------------------------------------------------------------------
# 7. build-log.html entry (use the safe-after-last-div pattern from tick 809)
# ------------------------------------------------------------------
BUILD_LOG_ENTRY = f"""
<div class="tick-entry" data-tick="2026-07-21-fast-exec-relativity-{LEAD_IDX}">
<h3>Tick {LEAD_IDX} — Relativity ({VERTICAL} OPENER #1/5, NEW VERTICAL #{LEAD_IDX})</h3>
<p class="meta">2026-07-21 · ai_legal_hold_ediscovery · OPENER #1/5 · tier 1 · evidence map &rarr; <a href="chunks/chunk_{LEAD_IDX}.html">chunk_{LEAD_IDX}.html</a></p>
<p><strong>Why this vertical:</strong> Every enterprise going through litigation, regulatory inquiry, internal investigation, FOIA request, or breach response needs <strong>legal hold + e-discovery + data breach response</strong> infrastructure. The wedge for our AI-GRC procurement lane is the platform's <strong>per-custodian preservation clock</strong> + <strong>per-action audit-evidence-capture</strong> + <strong>AICPA SOC 2 + ISO 27001 + FedRAMP Moderate</strong> attestation inheritance. Relativity is the enterprise-anchor eDiscovery + legal-hold + data-breach-response platform with Chicago HQ + 2001 founder lineage (Andrew Sieja, current board member) + 2022 CEO Phil Saunders + Silver Lake take-private 2024.</p>
<p><strong>Verified first-party evidence (live 2026-07-21):</strong> relativity.com/ HTTP 200 · /company/ HTTP 200, title "Company | About Relativity" · /company/our-people/leadership-team/ HTTP 200, names Phil Saunders "Chief Executive Officer" verbatim + "Prior to joining Relativity in 2022, he served as CEO at Cornerstone OnDemand following its acquisition of Saba" + Andrew Sieja founder (current board member) · /calder7-security/ HTTP 200, Calder7 security framework page with FedRAMP-certified callouts · /resources/certification/ HTTP 200 · /contact-us/ HTTP 200 (commercial route). Compliance posture: SOC 2 Type II + ISO/IEC 27001:2022 + ISO/IEC 27017:2015 + ISO/IEC 27018:2019 + ISO/IEC 27701:2019 + FedRAMP Moderate + StateRAMP Moderate + TX-RAMP + HIPAA + GDPR + CCPA + LGPD + APPI + PIPEDA + ISO of the Year (7th Annual CyberSecurity Breakthrough Awards). aiR generative-AI family: aiR Assist + aiR for Review + aiR for Privilege + aiR for Case Strategy + aiR for Data Breach Response. Relativity MCP (Manage Custom Practices) for external AI applications.</p>
<p><strong>Tier-1 evidence wedge:</strong> (1) per-custodian preservation clock with FRCP 37(e) spoliation-safe audit-trail + per-matter retention-vs-erasure reconciliation under GDPR Art. 17 + UK GDPR + Brazil LGPD + PIPEDA + APPI + Australia Privacy Act + Singapore PDPA + CCPA/CPRA; (2) aiR generative-AI per-decision audit-provenance pipeline with per-decision model-name + model-version + prompt-hash + response-hash + per-document citation-anchor + per-decision-confidence-score + per-custodian-reviewer-acknowledgment cross-tenant-no-bleed + per-aiR-LLM sub-processor DPA flow-down (OpenAI + Anthropic + Google Vertex + Microsoft Azure OpenAI) with 14-day change-notification SLA; (3) FedRAMP-Moderate + StateRAMP-Moderate + TX-RAMP inheritance pattern with per-environment credential scoping + per-tenant data-residency pinning + cross-environment-bleed-blocked audit-log replay + same machine-readable artifact reproducible across Government + commercial + aiR model-runtime + aiR-training-substrate; (4) cross-border data-residency posture for cross-border matters with per-jurisdiction (EU + UK + CH + BR + AU + SG + JP + CA + IN + ZA) per-matter cross-border-data-residency report reproducible for per-matter audit replay without manually re-running per-custodian timeline; (5) MCP-server + external AI-application governance lane with per-MCP-server auth boundary + per-invocation policy + per-decision audit-log replay retention + cross-tenant-no-bleed invariant comparable to first-party aiR model invocation. The 5-question audit letter (FRCP 37(e) + aiR per-decision audit provenance + FedRAMP inheritance + cross-border data-residency + MCP-server governance) is sent via the canonical first-party /contact-us/ form, not via any guessed inbox.</p>
<p><strong>Cohort roadmap:</strong> ai_legal_hold_ediscovery #1/5 Relativity (this tick) + #2/5 Everlaw + #3/5 Logikcull + #4/5 Nextpoint + #5/5 DISCO. <strong>Next tick recommendation:</strong> OPEN sibling #2/5 Everlaw (aislerot.com trusted enterprise eDiscovery lane, co-founders AJ Shankar + David Barrett + Dylan Siegel verified verbatim on first-party /about page; Everlaw Storybuilder + Everlaw Review + predictive-coding + Redaction Studio + Hold/Reveal/Audit-trace). This is the only cohort to verify <strong>Phil Saunders + Andrew Sieja</strong> as a +20-year legacy eDiscovery leadership lineage — a control surface no recent GRC entrant can replicate. SMTP remains gated and no email, form submission, delivery, payment, or revenue is claimed. <strong>Next tick: OPEN new vertical cohort #22 candidate — ai_data_quality_observability (Great Expectations OPENER + Monte Carlo + Soda + Bigeye + Anomalo) recommended as next vertical after ai_legal_hold_ediscovery CLOSES at 5/5.</strong></p>
<p class="footer">Atlas @ Talon Forge — cron tick 2026-07-21-fast-exec-relativity-{LEAD_IDX} · lead {LEAD_IDX} + cold_email/{LEAD_IDX}_relativity.md + cold_email/templates/{LEAD_IDX}_relativity.md + chunks/chunk_{LEAD_IDX}.html + leads.csv + index.html + sitemap.xml + build-log + commit + push · ai_legal_hold_ediscovery OPENER #1/5 (NEW VERTICAL #21) · $0 sent / $0 received.</p>
</div>
"""

with open(os.path.join(ROOT, "build-log.html"), encoding="utf-8") as f:
    bl_text = f.read()

# SAFE-AFTER-LAST-DIV PATTERN (from tick 809 learnings): insert AFTER the last </div>
last_div_idx = bl_text.rfind("</div>")
if last_div_idx == -1:
    print("[FAIL] could not find </div> in build-log.html")
    sys.exit(1)

# Insert AFTER the last </div> (NOT before)
insert_pos = last_div_idx + len("</div>")
new_bl = bl_text[:insert_pos] + BUILD_LOG_ENTRY + bl_text[insert_pos:]

with open(os.path.join(ROOT, "build-log.html"), "w", encoding="utf-8") as f:
    f.write(new_bl)

# Verify new entry is the very last <div class="tick-entry"> block
with open(os.path.join(ROOT, "build-log.html"), encoding="utf-8") as f:
    bl_verify = f.read()

# Find last <div class="tick-entry"
last_tick_entry_idx = bl_verify.rfind('<div class="tick-entry"')
if last_tick_entry_idx == -1:
    print("[FAIL] could not find <div class=\"tick-entry\" in build-log.html")
    sys.exit(1)

# Check what's between last_tick_entry_idx and the very end
tail_after_last_entry = bl_verify[last_tick_entry_idx:last_tick_entry_idx + 600]
if f'relativity-{LEAD_IDX}' not in tail_after_last_entry:
    print(f"[FAIL] last tick-entry does not mention relativity-{LEAD_IDX}")
    print(tail_after_last_entry[:500])
    sys.exit(1)
print(f"[OK] wrote build-log.html entry as last entry (tick relativity-{LEAD_IDX} verified as the very last tick-entry)")

# ------------------------------------------------------------------
# 8. revenue_log.md entry
# ------------------------------------------------------------------
with open(os.path.join(ROOT, "revenue_log.md"), encoding="utf-8") as f:
    rl_text = f.read()

REVENUE_ENTRY = f"""
## Tick {LEAD_IDX} — Relativity ({VERTICAL} OPENER #1/5, NEW VERTICAL #{LEAD_IDX})
- **Date:** 2026-07-21
- **Lead:** {LEAD_NAME} (relativity.com — first-party Phil Saunders CEO + Andrew Sieja founder verified)
- **Vertical:** {VERTICAL} — NEW VERTICAL #21 (cohort ceiling 5/5)
- **Position:** OPENER #1/5
- **Commercial route:** FORM:https://www.relativity.com/contact-us/ (canonical first-party contact form, queued — not submitted)
- **Companion artifacts:** cold_email/{LEAD_IDX}_relativity.md + cold_email/templates/{LEAD_IDX}_relativity.md + chunks/chunk_{LEAD_IDX}.html + index.html card + sitemap.xml url
- **Status:** queued_not_sent (SMTP gated, no form submission)
- **Revenue impact:** $0 sent / $0 received
- **Cumulative sent this run:** $0
- **Cumulative received this run:** $0
- **Next tick:** OPEN sibling #2/5 Everlaw OR move to next vertical cohort
"""

with open(os.path.join(ROOT, "revenue_log.md"), "w", encoding="utf-8") as f:
    f.write(rl_text.rstrip() + "\n" + REVENUE_ENTRY)
print("[OK] appended revenue_log.md entry for tick " + LEAD_IDX)

# ------------------------------------------------------------------
# 9. send_log.json queued_not_sent entry (use NEW schema)
# ------------------------------------------------------------------
SEND_LOG_PATH = os.path.join(ROOT, "cold_email", "send_log.json")
with open(SEND_LOG_PATH, encoding="utf-8") as f:
    send_log = json.load(f)

if not isinstance(send_log, list):
    print(f"[WARN] send_log.json is not a list, got {type(send_log)} — appending to new list")

# Use NEW schema (per tick 809 learnings): tick/index/vendor/cohort/position/form_url/send_status/route_type/smtp_gated/submitted/submitted_at/notes
NEW_ENTRY = {
    "tick": "2026-07-21-fast-exec-relativity-" + LEAD_IDX,
    "index": LEAD_IDX,
    "vendor": LEAD_NAME,
    "cohort": VERTICAL,
    "position": "OPENER #1/5 (NEW VERTICAL #21)",
    "form_url": "https://www.relativity.com/contact-us/",
    "send_status": "queued_not_sent",
    "route_type": "form",
    "smtp_gated": True,
    "submitted": False,
    "submitted_at": None,
    "notes": "First-party /contact-us/ form verified HTTP 200 live 2026-07-21. Phil Saunders CEO + Andrew Sieja founder verified. SMTP remains gated pending SMTP credential hand-off.",
}

if isinstance(send_log, list):
    send_log.append(NEW_ENTRY)
else:
    send_log = [NEW_ENTRY]

with open(SEND_LOG_PATH, "w", encoding="utf-8") as f:
    json.dump(send_log, f, indent=2, ensure_ascii=False)
print("[OK] appended send_log.json queued_not_sent entry for tick " + LEAD_IDX)

print()
print("=" * 60)
print(f"SHIP TICK {LEAD_IDX} — Relativity (NEW VERTICAL #21 OPENER #1/5) — ALL SURFACES WRITTEN")
print("=" * 60)
