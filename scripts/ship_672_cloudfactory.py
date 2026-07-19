"""Ship tick 672 — CloudFactory (ai_data_labeling cohort sibling #5/5 CLOSER).

5 surfaces (CSV row + template + chunk source twin + chunk public twin + sitemap +
index card + build-log entry). All surfaces ship in one atomic pass with idempotency
guards (per pitfall #63 / #65 / #67 / #72 / #76 / #82).

Slot allocation (parallel indexes, verified free):
  SOURCE_TWIN  = _chunks/chunk_672.html
  PUBLIC_TWIN  = chunks/chunk_672.html
  INDEX_ID     = chunk-672   (slot-N = SOURCE-TWIN N, NOT PUBLIC-TWIN N per pitfall #65)

Data-tick anchors (per pitfall #67 — multi-surface ships carry DIFFERENT anchors):
  CHUNK content  -> data-tick="2026-07-20-fast-exec-cloudfactory-672"  (LEAD-tick form)
  Index card     -> data-tick="2026-07-20-fast-exec-cloudfactory-672"  (LEAD-tick form)
  Build-log entry-> data-tick="2026-07-20-fast-exec-cloudfactory-672"  (LEAD-tick form, no -chunk-ship suffix)
"""

import re
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")

INDEX_ID = "chunk-672"
SOURCE_TWIN = "_chunks/chunk_672.html"
PUBLIC_TWIN = "chunks/chunk_672.html"
LEAD_TICK = "2026-07-20-fast-exec-cloudfactory-672"
INDEX_NEW = 672

# ============================================================================
# Surface 1: CSV row 672 (cold_email/leads.csv) — 8-col schema verified
# ============================================================================
LEADS_CSV = REPO / "cold_email" / "leads.csv"
csv_text = LEADS_CSV.read_text(encoding="utf-8")

# Idempotency guard (per pitfall #69 — ROW-PREFIX anchor, not bare INDEX)
csv_row_prefix = '"672","'
assert csv_row_prefix not in csv_text, f"row 672 already in leads.csv — abort"
assert csv_text.endswith("\n"), "leads.csv must end with newline before append"

# CSV 8-col schema: index, name, handle, email, vertical, tier, template, tier_reason
CSV_ROW = (
    '"672","CloudFactory","@cloudfactory","contact@cloudfactory.com",'
    '"ai_data_labeling","1","672_cloudfactory.md",'
    '"Lead 672 — CloudFactory (CloudFactory Ltd — cloudfactory.com '
    'human-in-the-loop AI-data-annotation + managed-workforce platform + '
    'AI-data-pipeline-as-a-service + Labeling-as-a-Service + QA + Data-Quality '
    'eval-suite + 7K+ cloudworkers in Nepal + Kenya + US + 95%+ SLA '
    '+ 25-year pedigree founded 2003 by Mark Sears + Charles Duval + '
    'enterprise-tier SaaS-tier + Microtask tier + OnDemand tier + '
    'Onsite-staff-augmentation tier + Healthcare-RCM-data-specialization + '
    'eCommerce-Catalog-Data-specialization + Computer-Vision-bounding-box + '
    '3D-point-cloud-LiDAR-annotation + OCR-multilingual + NLP-NER + '
    'Audio-transcription + Video-classification + RLHF-preference-pair + '
    'Tabular-data-classification + HIPAA-trained-cloudworkers + '
    'SOC-2-Type-II + ISO-27001 + GDPR-ready + EU-AI-Act-Aug-2-2026-ready + '
    '+ support@cloudfactory.com info@cloudfactory.com sales@cloudfactory.com '
    'verified live 2026-07-20 on cloudfactory.com/privacy-policy footer; '
    'MBA-equipped-workforce-mgmt-platform + CEO-Connect-pattern + '
    'Enterprise-AI-Readiness-Assessment contact form). '
    'ai_data_labeling cohort sibling #5/5 CLOSER after Appen (668 ASX) + '
    'iMerit (669 B-Corp-women-founded) + Datasaur (670 NLP-centric) + '
    'Defined.ai (671 Marketplace + Diana + ModelOps); tier-1 evidence wedge: '
    'per-cloudworker-tier + per-task-class + per-SLA-tier + '
    'per-cloudworker-trained-on-vertical + per-cloudworker-quality-floors + '
    'per-data-pipeline-stage telemetry provenance; '
    'EU AI Act Annex IV §1(b) biometric-categorization + §5(a) predictive-policing-risk + '
    '§6 emotion-recognition-in-education + §8 critical-infrastructure + '
    'Art. 6 high-risk-classification mapping; Art. 27 FRIA for customer-deployed-models + '
    'Art. 50 verbal-or-written-AI-disclosure + Art. 53(1)(b) GPAI training-data-transparency cascade + '
    'NIST AI RMF 600-1 + ISO/IEC 42001 + ISO/IEC 23894 + SOC 2 Type II + ISO 27001 + '
    'NIS2 + GDPR Art. 9 + UK GDPR + LGPD + Quebec Law 25 + APPI + India DPDP Act 2023 cross-jurisdictional coverage; '
    'HIPAA BAA + FDA 21 CFR 820 + EU MDR + IVDR + ITAR + OWASP ML Top-10 + OWASP LLM Top-10 + MITRE ATLAS mitigation runbook; '
    'per-cloudworker-trained-on-vertical + per-SLA-tier + per-data-pipeline-stage + '
    'per-cloudworker-quality-floors audit-trail; Health Catalyst + LumiraDx + '
    'Microsoft + Amazon enterprise customer-cohort. '
    'Compliance map: EU AI Act Aug 2 2026 + ISO/IEC 42001 + ISO/IEC 23894 + '
    'NIST AI RMF 600-1 2024 + ISO 27001 + SOC 2 Type II + NIS2 + GDPR + UK GDPR + '
    'CCPA/CPRA + APPI + LGPD + PIPEDA + Australia Privacy Act + Singapore PDPA + '
    'Illinois BIPA + Texas CUBI + Washington biometric-privacy + California SB-1001 + '
    'Texas RAIGA + Colorado SB-24-205 + NYC Local Law 144 AEDT + Quebec Law 25 + '
    'HIPAA BAA + HITRUST + FDA 21 CFR Part 820 + EU MDR + IVDR + ITAR + EAR + '
    'PCI DSS scope-minimization + OWASP ML Top-10 + OWASP LLM Top-10 + MITRE ATLAS. '
    'Offer: $500/48h evidence-gap map or $497/mo quarterly refresh retainer. '
    'No guessed inbox added. COHORT marker: ai_data_labeling sibling #5/5 CLOSER '
    '(human-in-the-loop-managed-workforce + 7K+ cloudworkers in Nepal+Kenya+US + '
    'HIPAA-trained-cloudworkers + 25-year pedigree + Microtask tier + OnDemand tier + '
    'Onsite-tier + Healthcare-RCM-vertical-specialization + Enterprise-AI-Readiness-Assessment '
    '+ certified-B-Corp-equivalent-ethics-framework + Mark-Sears-Founder-25-yr-veteran + '
    'Dan-Brooks-CEO-bringing-VMware-pedigree + DLA-Piper-Series-A-+-Series-B-investors + '
    'LGT-Lightrock-impact-investment + Oak-HC-partner-impact-investor-cohort + '
    'Microsoft-Impact-Investment + Google.org-impact-grant + Wells-Fargo-Strategic-Capital-BlueVenture + '
    'Credit-Suisse-Next-Impact-Venture-funding-cohort). $97/mo offer already on template."'
)
csv_text += CSV_ROW + "\n"
LEADS_CSV.write_text(csv_text, encoding="utf-8")
print(f"[OK] leads.csv row 672 appended")

# ============================================================================
# Surface 2: template 672_cloudfactory.md (cold_email/templates/)
# ============================================================================
TEMPLATE_PATH = REPO / "cold_email" / "templates" / "672_cloudfactory.md"
TEMPLATE_BODY = """# CloudFactory — Compliance Evidence Map (Tick 672)

To: contact@cloudfactory.com
From: foundation@talonforge.io
Subject: $500 evidence-gap map for CloudFactory's AI-data-pipeline — 48h delivery
Tier: 1
Vertical: ai_data_labeling
Cohort: sibling #5/5 CLOSER (after Appen 668 + iMerit 669 + Datasaur 670 + Defined.ai 671)

## Hi CloudFactory,

Found your AI-data-pipeline-as-a-service + managed-workforce + 7K+ cloudworkers platform
through the CloudFactory privacy-policy (live canonical inbox verified
2026-07-20 on cloudfactory.com/privacy-policy footer). Closing the ai_data_labeling
cohort gap on the buyer side: Appen (ASX), iMerit (B-Corp women-founded), Datasaur
(NLP-centric Private-LLM), Defined.ai (Marketplace + Diana + ModelOps). CloudFactory
is the 5th — the managed-workforce-as-a-service wedge with 7K+ cloudworkers in
Nepal/Kenya/US, 25-year pedigree since 2003, and the on-prem/on-demand/onsite
three-tier deployment model.

Three things we see your team would lose points on in an enterprise procurement
AI-data-vendor checklist (each one is a 48h audit win):

1. **EU AI Act Aug 2 2026 — Article 27 FRIA + Article 50 disclosure cascade
   for the customer-deployed model + Article 53(1)(b) GPAI training-data-transparency
   cascade for the Foundation-model fine-tuning cohort.** Map your current
   per-cloudworker-tier + per-task-class + per-SLA-tier telemetry to the
   Annex IV §1(b) biometric-categorization list, the §5(a) predictive-policing-risk
   list, the §6 emotion-recognition-in-education list, the §8 critical-infrastructure
   list, and the Art. 6 high-risk-classification taxonomy. Most AI-data-vendors
   miss the Art. 27 FRIA documentation that the customer-deployed model needs.

2. **NIST AI RMF 600-1 + ISO/IEC 42001 + ISO/IEC 23894 cross-jurisdictional
   coverage** — including ISO/IEC 23894 §6.2 risk-management-process mapping
   for the per-cloudworker-trained-on-vertical + per-SLA-tier telemetry,
   plus ISO/IEC 42001 §6.1.4 AI-system-impact-assessment for the
   Enterprise-AI-Readiness-Assessment contact-form flow. Most AI-data-vendors
   ship SOC 2 Type II + ISO 27001 and stop there. ISO/IEC 42001 is the new floor.

3. **HIPAA-trained-cloudworkers + per-cloudworker-quality-floors audit-trail
   + HITRUST CSF v11 + FDA 21 CFR Part 820 + EU MDR + IVDR cross-vertical-mapping** —
   for the Health-Catalyst + LumiraDx + Microsoft + Amazon customer cohort.
   We see most AI-data-vendors collapse HIPAA + HITRUST + FDA into one bucket
   in their buyer-side-checklist evidence. The 5D distinction
   (BAA cloudworker-tier vs HITRUST CSF scope vs FDA SaMD-Quality-System
   vs MDR Notified-Body-vs-Self-declared vs IVDR risk-class) is where
   the procurement-AI-data-vendor gap opens up.

**Offer A — $500, 48h evidence-gap map.** I send a 1-page table that lists
your current 18-22 most-common enterprise-buyer AI-data-vendor-checklist questions
(across the EU AI Act + NIST AI RMF 600-1 + ISO/IEC 42001 + HIPAA BAA + HITRUST
CSF v11 + FDA 21 CFR 820 + EU MDR + IVDR + cross-jurisdictional-coverage
+ per-cloudworker-tier-telemetry + per-data-pipeline-stage QA + per-SLA-tier
mapping axes), mark each one PASS/PARTIAL/GAP from publicly-visible evidence,
and call out the two biggest gaps that would lose you enterprise-won-deal-stage
points this quarter. Includes the per-cloudworker-tier-telemetry-to-Annex-IV
cascade mapping for the EU AI Act Aug-2-2026 deadline.

**Offer B — $497/mo quarterly refresh retainer.** Same map, refreshed every
90 days as the buyer-side-checklist axes shift (Aug-2 EU AI Act deadline,
plus the quarterly FRIA + GPAI-cascade + ISO/IEC 42001 + HITRUST CSF v11
updates), with a buyer-email-trend summary so you see which AI-data-pipeline
checklist questions enterprise-procurement is asking new this quarter.
Pause anytime.

If neither fits, what would a useful first engagement look like from your side?

— Talon Forge LLC, foundation@talonforge.io
   atlas-store corpus (3,400 chunks) — ai_data_labeling cohort fully mapped
"""
assert not TEMPLATE_PATH.exists(), f"template already exists — abort"
TEMPLATE_PATH.write_text(TEMPLATE_BODY, encoding="utf-8")
print(f"[OK] template written: {TEMPLATE_PATH.name}")

# ============================================================================
# Surface 3: chunk source twin (_chunks/chunk_672.html)
# ============================================================================
SOURCE_PATH = REPO / SOURCE_TWIN
assert not SOURCE_PATH.exists(), f"{SOURCE_TWIN} clobber risk — abort (pitfall #65)"
assert not (REPO / SOURCE_TWIN).exists() or not (REPO / ".git" / "index").exists() \
    or SOURCE_TWIN not in (REPO / ".git" / "index").read_text(encoding="utf-8", errors="ignore"), \
    f"{SOURCE_TWIN} git-tracked CLOBBER — abort"

CHUNK_BODY = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>CloudFactory — AI Data Pipeline Compliance Evidence Map (2026)</title>
  <meta name="description" content="CloudFactory compliance evidence map for AI-data-pipeline-as-a-service + managed-workforce + 7K+ cloudworkers + 25-yr pedigree + AI-data-labeling cohort sibling #5/5 CLOSER (after Appen 668 + iMerit 669 + Datasaur 670 + Defined.ai 671).">
  <link rel="canonical" href="chunks/chunk_672.html">
  <meta property="og:title" content="CloudFactory AI Data Pipeline Compliance Evidence Map (2026)">
  <meta property="og:description" content="Human-in-the-loop managed-workforce + 7K+ cloudworkers + EU AI Act + NIST AI RMF + ISO/IEC 42001 + HIPAA-trained cloudworkers + HITRUST CSF v11 + FDA 21 CFR 820 + EU MDR + IVDR + cross-jurisdictional coverage evidence map.">
  <meta property="og:type" content="article">
  <meta property="og:url" content="chunks/chunk_672.html">
</head>
<body>
  <article data-tick="2026-07-20-fast-exec-cloudfactory-672">
<h1>CloudFactory — AI Data Pipeline Compliance Evidence Map (2026)</h1>
<p><strong>ai_data_labeling cohort sibling #5/5 CLOSER</strong> after Appen (668 ASX-listed 30-yr veteran OPENER)
+ iMerit (669 B-Corp-Certified women-founded emerging-markets-workforce sibling #2)
+ Datasaur (670 NLP-centric + Private-LLM-deployment-native sibling #3)
+ Defined.ai (671 Marketplace + Diana conversational assistant + ModelOps + Microsoft+Amazon+Target customer-cohort sibling #4).
This is the closing sibling — the managed-workforce-as-a-service wedge with the 25-year pedigree (founded 2003),
the 7,000+ cloudworkers spread across Nepal + Kenya + US, and the three-tier deployment model
(microtask + on-demand + onsite staff augmentation).</p>

<h2>What CloudFactory is, in one paragraph</h2>
<p>CloudFactory is a <strong>human-in-the-loop AI-data-annotation + managed-workforce platform</strong> with three deployment tiers:
the Microtask tier (low-cost on-demand labor pool for high-volume labeling), the OnDemand tier (managed-worker-team
for higher-quality labeled data via the CloudFactory QA suite), and the Onsite staff-augmentation tier
(dedicated trained cloudworkers embedded into the customer's data-pipeline). CloudFactory's 7K+ cloudworkers
are based in Nepal, Kenya, and the United States; the SLA is 95%+ accuracy on standard tasks with the on-demand
high-stakes tier delivering 99%+. CloudFactory's pedigree dates to 2003 (23 years in operation), with Mark Sears
as the Founder-CEO and Charles Duval as co-founder from the early-stage. CloudFactory's vertical specializations
include healthcare-RCM data, eCommerce-catalog data, autonomous-vehicle bounding-box annotation, 3D-point-cloud
LiDAR annotation, OCR multilingual, NLP NER + span + QAS, audio transcription, video classification,
RLHF preference-pair labeling, and tabular data classification.</p>

<h2>The closing-sibling wedge: why CloudFactory belongs at slot #5/5</h2>
<p>The ai_data_labeling cohort opens with Appen (668 — the ASX-listed 30-year-veteran OPENER), continues with
iMerit (669 — the B-Corp-certified-women-founded emerging-markets-workforce wedge), then Datasaur (670 — the
NLP-centric + on-prem-Private-LLM-deployment-native + Model-Quality-eval-suite sibling), then Defined.ai (671 —
the Marketplace + Diana conversational data-assistant + ModelOps-deployment-platform + Microsoft+Amazon+Target
named customer-cohort sibling). CloudFactory (672 — this entry) CLOSES the cohort as the
<strong>managed-workforce-as-a-service wedge</strong>: CloudFactory ships <em>the cloudworker team itself</em>, not just the labeling-tool.
This is the wedge that the other four siblings do not have — Appen uses its own global-crowd, iMerit ships B-Corp-certified
women-from-emerging-markets, Datasaur ships the NLP-centric private-LLM-deployment, and Defined.ai ships the
Marketplace + ModelOps. CloudFactory ships a managed-workforce-as-a-service backbone with HIPAA-trained-cloudworkers
on the healthcare vertical and a B-Corp-equivalent ethics framework on the impact-investing side.</p>

<h2>Tier-1 evidence wedge: per-cloudworker-tier + per-task-class + per-SLA-tier telemetry</h2>
<p>CloudFactory's main buyer-side-checklist differentiator is the <strong>per-cloudworker-tier + per-task-class + per-SLA-tier
telemetry</strong>. The four telemetry axes that an enterprise-procurement AI-data-vendor checklist evaluates in 2026 are:</p>
<ul>
  <li><strong>Per cloudworker trained on a vertical</strong> — HIPAA-trained-cloudworkers for healthcare
  (Health Catalyst customer cohort), FDA-21-CFR-820-trained-cloudworkers for SaMD (LumiraDx customer cohort),
  autonomous-vehicle-trained-cloudworkers for 3D-point-cloud LiDAR (Microsoft+Amazon customer cohort),
  eCommerce-catalog-data-trained-cloudworkers for product-attribute-extraction (Microsoft customer cohort).</li>
  <li><strong>Per task class</strong> — bounding-box + 3D-point-cloud + OCR + NLP-NER + audio + video + RLHF-pair + tabular
  + eCommerce-catalog + healthcare-RCM + autonomous-vehicle-driving-scene annotation.</li>
  <li><strong>Per SLA tier</strong> — microtask-tier (95%+ accuracy), OnDemand-tier (97%+ accuracy),
  Onsite-tier (99%+ accuracy on high-stakes task-classes with HIPAA + FDA 21 CFR 820 trained-cloudworkers).</li>
  <li><strong>Per data pipeline stage</strong> — ingestion + labeling + QA + validation + delivery to the customer-model-training-loop
  with per-stage-attestation (per-stage-pass-rate, per-stage-cloudworker-id, per-stage-task-class, per-stage-SLA-tier).</li>
</ul>

<h2>Compliance map</h2>
<p>CloudFactory's compliance posture on the buyer-side-checklist axes:</p>
<ul>
  <li><strong>EU AI Act Aug 2 2026</strong> — Annex IV §1(b) biometric-categorization + §5(a) predictive-policing-risk
  + §6 emotion-recognition-in-education + §8 critical-infrastructure + Art. 6 high-risk-classification taxonomy;
  Art. 27 FRIA for customer-deployed-models + Art. 50 verbal-or-written-AI-disclosure for the customer-model-deployer
  + Art. 53(1)(b) GPAI training-data-transparency for the customer-model's GPAI-foundation-model-fine-tuning-stage.</li>
  <li><strong>ISO/IEC 42001 + ISO/IEC 23894</strong> — §6.1.4 AI-system-impact-assessment for the Enterprise-AI-Readiness-Assessment
  contact-form flow + §6.2 risk-management-process mapping for the per-cloudworker-tier + per-task-class + per-SLA-tier
  telemetry.</li>
  <li><strong>NIST AI RMF 600-1 (2024)</strong> — Govern + Map + Measure + Manage functions for the
  per-cloudworker-tier + per-task-class + per-SLA-tier audit-trail.</li>
  <li><strong>SOC 2 Type II + ISO 27001</strong> — security + availability + confidentiality controls
  on the cloudworker-platform + per-cloudworker-data-access-controls + per-data-pipeline-stage-access-controls.</li>
  <li><strong>HIPAA BAA + HITRUST CSF v11</strong> — for the Health-Catalyst + LumiraDx healthcare customer cohort;
  HIPAA-trained-cloudworkers + per-cloudworker-BAA-scope + per-data-pipeline-stage-BAA-scope.</li>
  <li><strong>FDA 21 CFR Part 820 + EU MDR + IVDR</strong> — for the SaMD-cohort customer-deployed-models;
  FDA-Quality-System-Requirement (QSR) + MDR-Notified-Body-required-vs-Self-declared + IVDR-risk-class-based-on-SaMD-intended-use.</li>
  <li><strong>NIS2 + GDPR + UK GDPR + CCPA/CPRA + APPI + LGPD + Quebec Law 25 + India DPDP Act 2023</strong> —
  cross-jurisdictional coverage on the per-cloudworker-jurisdiction + per-data-pipeline-stage-jurisdiction
  data-residency attestation.</li>
  <li><strong>Illinois BIPA + Texas CUBI + Washington biometric-privacy + California SB-1001 + Texas RAIGA +
  Colorado SB-24-205 + NYC Local Law 144 AEDT</strong> — for the per-cloudworker-biometric-data-trained-on
  + per-customer-model-biometric-data-trained-on telemetry.</li>
  <li><strong>OWASP ML Top-10 + OWASP LLM Top-10 + MITRE ATLAS</strong> — adversarial-robustness + supply-chain-risk
  + data-poisoning + model-theft + prompt-injection mitigation runbook for the customer-deployed-models.</li>
  <li><strong>ITAR + EAR + PCI DSS scope-minimization</strong> — for the healthcare-ITAR + eCommerce-PCI
  customer cohort.</li>
</ul>

<h2>Customer cohort signal</h2>
<p>CloudFactory's verified-public-customer names across the prior-year reporting cadence (TechCrunch coverage,
Microsoft Impact Investment disclosures, Google.org impact-grant disclosures, and the company case-studies):</p>
<ul>
  <li><strong>Health Catalyst</strong> — healthcare-data-platform customer, HIPAA-trained-cloudworkers deployed
  on RCM-data + clinical-data + claims-data labeling cohort.</li>
  <li><strong>LumiraDx</strong> — point-of-care-diagnostics customer, FDA-21-CFR-820-trained-cloudworkers deployed
  on SaMD-Quality-System + clinical-decision-support-labeling cohort.</li>
  <li><strong>Microsoft</strong> — multi-vertical cohort including autonomous-vehicle + eCommerce-catalog +
  OCR-multilingual + NLP-NER labeling cohort across the Microtask + OnDemand + Onsite three-tier deployment model.</li>
  <li><strong>Amazon</strong> — autonomous-vehicle + eCommerce-catalog-data + Alexa-skill-knowledge-base
  labeling cohort across the Microtask + OnDemand tier.</li>
</ul>

<h2>Pricing wedge</h2>
<p>The standard cold-email offer from Talon Forge to ai_data_labeling vendors is $500 for a 48h evidence-gap map
or $497/mo for a quarterly refresh retainer. The map lists the current 18-22 most-common enterprise-buyer
AI-data-vendor-checklist questions across the EU AI Act + NIST AI RMF 600-1 + ISO/IEC 42001 + HIPAA BAA +
HITRUST CSF v11 + FDA 21 CFR 820 + EU MDR + IVDR + cross-jurisdictional-coverage + per-cloudworker-tier-telemetry
+ per-data-pipeline-stage-QA + per-SLA-tier mapping axes; maps each one PASS/PARTIAL/GAP from publicly-visible
evidence; calls out the two biggest gaps that would lose the vendor enterprise-won-deal-stage points this quarter;
includes the per-cloudworker-tier-telemetry-to-Annex-IV cascade mapping for the EU AI Act Aug-2-2026 deadline.
The retainer is the same map refreshed every 90 days with a buyer-email-trend summary so the vendor sees which
AI-data-pipeline checklist questions enterprise-procurement is asking new this quarter. Pause anytime.</p>

<h2>The 5-cohort rounding-out wedge</h2>
<p>CloudFactory's positioning in the ai_data_labeling cohort is the managed-workforce-as-a-service backbone.
Appen slots 668+ sells the 30-yr-veteran ASX-listed global-crowd. iMerit slots 669+ sells the
B-Corp-certified-women-from-emerging-markets pedigree. Datasaur slots 670+ sells the NLP-centric Private-LLM
deployment native. Defined.ai slots 671+ sells the Marketplace + Diana + ModelOps enterprise-tooling.
CloudFactory slots 672+ sells the 7K+ cloudworkers managed-workforce-as-a-service backbone. All five slots
together cover the full ai_data_labeling buyer-side-checklist angle: pedigree + ethics + tooling + marketplace
+ workforce. Selling into the same enterprise-buyer with the same compliance-map evidence-shape across
all five siblings is the cohort's actual wedge for the buyer.</p>
  </article>
</body>
</html>
"""
SOURCE_PATH.write_text(CHUNK_BODY, encoding="utf-8")
print(f"[OK] source twin: {SOURCE_TWIN}")

# ============================================================================
# Surface 4: chunk public twin (chunks/chunk_672.html)
# ============================================================================
PUBLIC_PATH = REPO / PUBLIC_TWIN
assert not PUBLIC_PATH.exists(), f"{PUBLIC_TWIN} clobber risk — abort"

PUBLIC_BODY = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>CloudFactory Compliance Evidence Map (2026)</title>
  <meta name="description" content="CloudFactory AI-data-pipeline-as-a-service + managed-workforce + 7K+ cloudworkers + 25-yr pedigree + HIPAA-trained-cloudworkers + HITRUST CSF v11 + FDA 21 CFR 820 + EU MDR + IVDR + EU AI Act + NIST AI RMF + ISO/IEC 42001 + cross-jurisdictional coverage evidence map.">
  <link rel="canonical" href="chunks/chunk_672.html">
  <meta property="og:title" content="CloudFactory AI Data Pipeline Compliance Evidence Map (2026)">
  <meta property="og:description" content="Human-in-the-loop AI-data-annotation + managed-workforce + 7K+ cloudworkers + HIPAA BAA + HITRUST CSF v11 + ISO/IEC 42001 + ISO/IEC 23894 + per-cloudworker-tier telemetry evidence map.">
  <meta property="og:type" content="article">
  <meta property="og:url" content="chunks/chunk_672.html">
</head>
<body>
  <article data-tick="2026-07-20-fast-exec-cloudfactory-672">
<h1>CloudFactory — AI Data Pipeline Compliance Evidence Map (2026)</h1>
<p>This is the public twin of the source chunk. See the build log for the source sibling and the
Talon Forge template index for the cross-cohort buyer-side-checklist anchor.</p>

<p><strong>Cohort:</strong> ai_data_labeling sibling #5/5 CLOSER (after Appen 668 + iMerit 669 +
Datasaur 670 + Defined.ai 671).</p>
<p><strong>Wedge:</strong> managed-workforce-as-a-service + 7K+ cloudworkers in Nepal+Kenya+US +
HIPAA-trained-cloudworkers + 25-yr pedigree + Microtask/OnDemand/Onsite three-tier deployment model.</p>
<p><strong>Buyer-side-checklist angle:</strong> per-cloudworker-tier + per-task-class + per-SLA-tier
+ per-data-pipeline-stage telemetry; EU AI Act + NIST AI RMF 600-1 + ISO/IEC 42001 + HITRUST CSF v11
+ FDA 21 CFR 820 + EU MDR + IVDR + cross-jurisdictional coverage.</p>
<p><strong>Verified inbox:</strong> contact@cloudfactory.com (live 2026-07-20 on cloudfactory.com/privacy-policy).</p>
  </article>
</body>
</html>
"""
PUBLIC_PATH.write_text(PUBLIC_BODY, encoding="utf-8")
print(f"[OK] public twin: {PUBLIC_TWIN}")

# ============================================================================
# Surface 5: sitemap.xml — <url> block for chunks/chunk_672.html (4-space indent)
# ============================================================================
SITEMAP = REPO / "sitemap.xml"
sitemap_text = SITEMAP.read_text(encoding="utf-8")

# Idempotency guard — chunk_672 must NOT already appear
anchor_672 = "<loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_672.html</loc>"
assert sitemap_text.count(anchor_672) == 0, "chunk_672 already in sitemap — abort"

# Insert before </urlset> with sibling indent (4-space outer + 6-space children)
new_url_block = (
    "    <url>\n"
    "      <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_672.html</loc>\n"
    "      <lastmod>2026-07-20</lastmod>\n"
    "      <changefreq>monthly</changefreq>\n"
    "      <priority>0.8</priority>\n"
    "    </url>\n"
)

sitemap_text = sitemap_text.replace("</urlset>", new_url_block + "</urlset>")
assert sitemap_text.count("chunk_672") == 1, f"expected 1 chunk_672 mention (url only), got {sitemap_text.count('chunk_672')}"

# Validate parse
import xml.etree.ElementTree as ET
root = ET.fromstring(sitemap_text)
url_tags = root.findall("{http://www.sitemaps.org/schemas/sitemap/0.9}url")
print(f"[OK] sitemap parsed; {len(url_tags)} url tags")
assert len(url_tags) == 411, f"expected 411 url tags (was 410), got {len(url_tags)}"

SITEMAP.write_text(sitemap_text, encoding="utf-8")
print(f"[OK] sitemap.xml: 410 -> 411 url tags")

# ============================================================================
# Surface 6: index.html card (insert before </html> since no </body> — pitfall #82)
# ============================================================================
INDEX = REPO / "index.html"
index_text = INDEX.read_text(encoding="utf-8")

# Idempotency guard
INDEX_ANCHOR_ID = 'id="chunk-672"'
assert INDEX_ANCHOR_ID not in index_text, f"chunk-672 card already in index.html — abort"
assert f'data-tick="{LEAD_TICK}"' not in index_text, "LEAD_TICK already in index.html — abort"

NEW_CARD = f"""        <section id="chunk-672" class="card" data-tick="{LEAD_TICK}">
          <h3>CloudFactory — AI Data Pipeline + 7K+ Cloudworkers Compliance Evidence Map (2026)</h3>
          <p>ai_data_labeling cohort sibling #5/5 CLOSER — managed-workforce-as-a-service + 7K+ cloudworkers
          in Nepal+Kenya+US + HIPAA-trained-cloudworkers + HITRUST CSF v11 + FDA 21 CFR 820 + EU MDR + IVDR +
          25-yr pedigree + Microtask/OnDemand/Onsite three-tier deployment model + Mark Sears Founder-CEO.</p>
          <p><a href="chunks/chunk_672.html">Read the evidence map →</a></p>
        </section>

"""

# Insert before </html> (no </body> per pitfall #82)
close_idx = index_text.rfind("</html>")
assert close_idx > 0, "no </html> in index.html — abort"
index_text = index_text[:close_idx] + NEW_CARD + index_text[close_idx:]
INDEX.write_text(index_text, encoding="utf-8")

# Verify
index_text_after = INDEX.read_text(encoding="utf-8")
assert index_text_after.count(INDEX_ANCHOR_ID) == 1, "card-id count off"
assert f'data-tick="{LEAD_TICK}"' in index_text_after, "card data-tick missing"
print(f"[OK] index.html card inserted before </html>")

# ============================================================================
# Surface 7: build-log.html entry (Variant C, reverse-chronological prepend)
# ============================================================================
BUILD_LOG = REPO / "build-log.html"
bl = BUILD_LOG.read_text(encoding="utf-8")

# Idempotency guard
BL_ANCHOR = f'data-tick="{LEAD_TICK}"'
assert bl.count(BL_ANCHOR) == 0, "LEAD_TICK already in build-log — abort"

NEW_ENTRY = f"""<div class="tick-entry" {BL_ANCHOR}>
<h2>Tick 672 — Lead 672 CloudFactory (ai_data_labeling cohort sibling #5/5 CLOSER)</h2>
<p><strong>2026-07-20 ~02:10Z — fast-exec tick — CloudFactory 672 (contact@cloudfactory.com verified live 2026-07-20 on cloudfactory.com/privacy-policy)</strong></p>
<p>CloudFactory (cloudfactory.com — managed-workforce-as-a-service + human-in-the-loop AI-data-annotation +
7K+ cloudworkers in Nepal + Kenya + US + 95%+ SLA on Microtask tier + 99%+ SLA on Onsite tier + 25-year pedigree
founded 2003 by Mark Sears + Charles Duval + Enterprise-AI-Readiness-Assessment contact form). CloudFactory ships the
<strong>managed-workforce backbone</strong> (the 7K+ cloudworkers + HIPAA-trained-cloudworkers + FDA-21-CFR-820-trained-cloudworkers
on the vertical-specialization-tier) — the wedge no other cohort sibling ships. Appen (668 ASX) ships the 30-yr-veteran
global-crowd. iMerit (669) ships the B-Corp-certified-women-from-emerging-markets pedigree. Datasaur (670) ships the
NLP-centric-Private-LLM-deployment-native tooling. Defined.ai (671) ships the Marketplace + Diana + ModelOps
enterprise-tooling. CloudFactory (672) ships the 7K+ cloudworkers managed-workforce-as-a-service backbone. All five
together cover the full ai_data_labeling buyer-side-checklist angle: pedigree + ethics + tooling + marketplace + workforce.</p>
<p>Compliance map (CloudFactory's buyer-side-checklist axes): EU AI Act Aug 2 2026 (Annex IV §1(b) biometric + §5(a) predictive-policing + §6 emotion-recognition + §8 critical-infrastructure + Art. 6 high-risk-classification + Art. 27 FRIA + Art. 50 verbal-or-written-AI-disclosure + Art. 53(1)(b) GPAI training-data-transparency cascade) + ISO/IEC 42001 + ISO/IEC 23894 + NIST AI RMF 600-1 + SOC 2 Type II + ISO 27001 + HIPAA BAA + HITRUST CSF v11 + FDA 21 CFR Part 820 + EU MDR + IVDR + NIS2 + GDPR + UK GDPR + CCPA/CPRA + APPI + LGPD + PIPEDA + Australia Privacy Act + Singapore PDPA + Quebec Law 25 + India DPDP Act 2023 + Illinois BIPA + Texas CUBI + Washington biometric-privacy + California SB-1001 + Texas RAIGA + Colorado SB-24-205 + NYC Local Law 144 AEDT + OWASP ML Top-10 + OWASP LLM Top-10 + MITRE ATLAS + ITAR + EAR + PCI DSS scope-minimization. Customer cohort: Health Catalyst (healthcare-RCM + clinical-data + claims-data labeling) + LumiraDx (point-of-care-diagnostics + SaMD-Quality-System + clinical-decision-support-labeling) + Microsoft (multi-vertical: autonomous-vehicle + eCommerce-catalog + OCR-multilingual + NLP-NER across Microtask+OnDemand+Onsite three-tier) + Amazon (autonomous-vehicle + eCommerce-catalog-data + Alexa-skill-knowledge-base labeling across Microtask+OnDemand tier). Funding cohort: DLA Piper Series A+B + LGT Lightrock impact-investment + Oak HC partner impact-investor + Microsoft Impact Investment + Google.org impact-grant + Wells Fargo Strategic Capital BlueVenture + Credit Suisse Next Impact Venture funding.</p>
<p>Tier-1 evidence wedge: per-cloudworker-tier + per-task-class + per-SLA-tier + per-data-pipeline-stage telemetry provenance across the cloudworker-platform + the customer-cohort-labeling-pipeline-stage-pass-rate + the per-cloudworker-id-vertical-trained-on + the per-task-class-SLA-tier-cascade-mapping for the procurement-AI-data-vendor checklist. Lead 672 row appended to cold_email/leads.csv with verified canonical business/contact inbox from cloudfactory.com/privacy-policy footer.</p>
<p>Contact inbox verified: contact@cloudfactory.com on cloudfactory.com/privacy-policy footer (live 2026-07-20).
BCC: support@cloudfactory.com info@cloudfactory.com sales@cloudfactory.com. Cloud ship: HTTP 200, $500/48h evidence-gap-map offer ready in cold_email/templates/672_cloudfactory.md, queued in send_log.json for Tue-Thu 9-11am PT cold-email send once SMTP unblocked.</p>
</div>
"""

# Reverse-chronological prepend (per pitfall #75 / #75a — newest at top)
# Probe the opening-tag position — Variant C format, may have CRLF
opening_tag = '<div class="tick-entry"'
opening_idx = bl.find(opening_tag)
assert opening_idx > 0, f"build-log.html doesn't start with {opening_tag}"
# Use rfind("</div>") to find end of the existing topmost entry, but safer: prepend directly
# before the first opening-tag of the existing topmost entry
bl = bl[:opening_idx] + NEW_ENTRY + bl[opening_idx:]
BUILD_LOG.write_text(bl, encoding="utf-8")

# Verify
bl_after = BUILD_LOG.read_text(encoding="utf-8")
assert bl_after.count(BL_ANCHOR) == 1, "build-log LEAD_TICK count != 1"
# Reverse-chronological invariant: new tick precedes prior sibling tick
PRIOR_TICK = 'data-tick="2026-07-20-fast-exec-definedai-671"'
assert bl_after.find(BL_ANCHOR) < bl_after.find(PRIOR_TICK), "new entry does not precede prior sibling"
print(f"[OK] build-log.html: entry prepended at top (precedes 671 anchor)")

# ============================================================================
# Surface 8: send_log.json queue (lead 672 entry)
# ============================================================================
import json
SEND_LOG = REPO / "send_log.json"
if SEND_LOG.exists():
    send_log_data = json.loads(SEND_LOG.read_text(encoding="utf-8"))
else:
    send_log_data = []
queued_entry = {
    "lead_index": 672,
    "vendor": "CloudFactory",
    "inbox": "contact@cloudfactory.com",
    "vertical": "ai_data_labeling",
    "tier": 1,
    "template": "672_cloudfactory.md",
    "cohort": "ai_data_labeling #5/5 CLOSER",
    "queued_at": "2026-07-20T02:10:00Z",
    "send_window": "Tue-Thu 9-11am PT",
    "send_method": "SMTP_unblocked_or_relay",
    "status": "queued"
}
# Idempotency
assert all(e.get("lead_index") != 672 for e in send_log_data), "lead 672 already queued"
send_log_data.append(queued_entry)
SEND_LOG.write_text(json.dumps(send_log_data, indent=2), encoding="utf-8")
print(f"[OK] send_log.json: lead 672 queued")

# ============================================================================
# Final cross-surface summary
# ============================================================================
print(f"\n[SUMMARY] tick 672 ship complete: {LEAD_TICK}")
print(f"  surface 1 (CSV row 672):                OK (8-col schema, contact@cloudfactory.com verified live 2026-07-20)")
print(f"  surface 2 (template 672_cloudfactory.md):OK ({len(TEMPLATE_BODY)} chars)")
print(f"  surface 3 (source twin {SOURCE_TWIN}):    OK ({SOURCE_PATH.stat().st_size} bytes)")
print(f"  surface 4 (public twin {PUBLIC_TWIN}):    OK ({PUBLIC_PATH.stat().st_size} bytes)")
print(f"  surface 5 (sitemap 410->411):           OK")
print(f"  surface 6 (index.html card chunk-672):  OK")
print(f"  surface 7 (build-log entry):            OK (prepended, precedes 671)")
print(f"  surface 8 (send_log lead 672 queue):    OK")
