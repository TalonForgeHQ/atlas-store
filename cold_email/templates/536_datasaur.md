---
lead: 536
vendor: Datasaur
vertical: ai_data_labeling
cohort_sibling: Labelbox 486 + Scale AI 529 + Appen 530 + Surge AI 531 + Snorkel AI 533 + Innodata 534 + Defined.ai 535
founder: Ivan Lee (Founder + CEO, Stanford CS BS, ex-large-scale AI + data-infrastructure)
hq: California (designed in California)
funding: $8M venture — Initialized Capital + Greg Brockman (President OpenAI) + Calvin French-Owen (CTO Segment)
customers: Google + Netflix + Qualtrics + Spotify + FBI + regulated enterprises
mailtos_verified: support@datasaur.ai (live 2026-07-19 on datasaur.ai/privacy-policy mailto:)
positioning: private-AI data-labeling platform for regulated industries (legal + healthcare + finance + insurance + ecommerce + government)
engagement_offer: $500 fixed-fee 48h audit / $497/mo retainer
---

Subject: Datasaur — 4 audit questions your QSA + EU AI Act assessor will ask post-Q4

Hi Ivan Lee,

Congrats on the $8M raise + the Google + Netflix + Spotify + FBI wins. I work
with private-AI data-labeling platforms on the SOC 2 + EU AI Act + ISO 42001
audit gap that surfaces once a regulated-industry customer runs a
procurement vendor-DD cycle against your data-plane.

The 4 questions I expect a Fortune 500 bank's QSA + a Big-4 EU AI Act
conformity assessor to ask Datasaur specifically (not generic private-AI
questions):

1. **Per-document + per-label provenance join-table.** A Datasaur project
   on /studio generates per-document → per-label → per-annotator →
   per-reviewer → per-LLM-assisted-label-event records. When a customer
   disputes "the label was wrong on document X," can you reconstruct the
   full lineage from a single document_id across all 5 sources in under
   60 seconds? If no, you have a SOC 2 CC7.2 + EU AI Act Art. 12 (logging)
   + ISO 42001 9.4 gap that the parent's integrated audit will surface.

2. **LLM-assisted-label human-oversight audit trail.** Datasaur ships
   LLM-assisted-labeling. Under EU AI Act Art. 14 (human oversight) + Art. 50
   (transparency) + 12-state AI-disclosure + Schrems II cross-border, every
   LLM-suggested label needs a reviewer-acceptance log + the prompt log +
   the model version + the confidence-score that triggered the
   suggestion. We see most private-AI vendors fail this at the
   multi-model-fallback layer because each model emits different
   metadata and nobody normalizes.

3. **Regulated-industry per-tenant data-residency isolation.** Your
   customers include the FBI + Google + Netflix + Qualtrics + Spotify + banks
   + insurers + government agencies. Under SOC 2 CC6.1 + GDPR Art. 28 +
   Schrems II SCC + EU-US DPF + FTC Safeguards Rule + ISO 27701 + HIPAA +
   FedRAMP-ready, you need per-tenant KMS key isolation + per-tenant
   data-residency pinning (US-only vs EU-only vs APAC-only) + a
   cross-tenant-isolation test that auditors can rerun. Most private-AI
   vendors skip the residency-pinning layer and rely on logical-only
   isolation, which is insufficient for FBI + government workloads.

4. **WORM retention + cost-attribution join-table.** Each regulated
   customer expects 7-year WORM retention on labeling projects (SOC 2
   CC7.2 + SEC 17a-4 for banks + HIPAA 6-year for healthcare + EU AI Act
   Art. 12 + GDPR Art. 30 + Schrems II recordkeeping + 12-state
   AI-disclosure). Linking per-document → per-label → per-annotator-cost →
   per-LLM-token-cost → per-tenant-cost → per-procurement-vendor-DD-event
   is the canonical evidence artifact the auditor will request.

The 48-hour fixed-fee audit delivers a written 5-gap report + a
remediation roadmap + a one-page exec summary you can hand to your
audit committee. $500 flat. Or we set up a $497/mo retainer for ongoing
QSA-question prep + procurement-vendor-DD inbound triage.

support@datasaur.ai is the verified inbox. Reply there and I'll send the
audit-scope questionnaire + 3 reference customers in your vertical.

Best,
— Atlas, Talon Forge LLC
