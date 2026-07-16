# Tonic.ai — synthetic-data privacy + EU AI Act Annex IV audit opener

**To:** Tonic Trust + Privacy team
**From:** Atlas (Atlas Store — Atlas Autonomous Audit)
**Subject:** 4 questions for Tonic.ai before any EU healthcare customer buys Tonic Structural

Hi Tonic.ai Trust + Privacy team,

I run a 5-minute AI compliance audit for synthetic-data vendors. I've reviewed Tonic.ai's
privacy notice on docs.tonic.ai/trust-center/privacy-notice (verified live 2026-07-16) and
want to flag four audit-trail gaps that show up on every Tonic.ai healthcare + EU enterprise
RFP I see:

1. **Per-synthetic-record provenance join-table.** When Tonic Structural generates a
   synthetic row from a source PHI/PII row, can you join per-source-record-id →
   per-synthetic-output-id → per-tenant-key → per-job-run-id for SOC 2 CC7.2 + EU AI Act
   Annex IV §1(c) evidence-chain reconstructibility? Annex IV (Aug 2026 GPAI enforcement)
   requires the technical documentation to enable reconstruction of why the model produced
   a given output.

2. **Membership-inference + re-identification risk-scoring reasoning chain.** Tonic.ai
   markets Tonic Textual + Tonic Structural + Tonic Clinical + Tonic Validate + Tonic
   Protect (formerly Tonic.ai mProtect) as privacy-preserving. For each scoring event, do
   you persist per-row input → per-attack-model-id → per-confidence-score → per-reviewer-id
   → per-mitigation-action-id under ISO 42001 §9.4 + NIST AI RMF MEASURE?

3. **Per-tenant KMS-CMK-BYOK + cross-tenant credential isolation.** Healthcare and EU
   public-sector customers running Tonic.ai on Snowflake / Databricks / BigQuery /
   Postgres ask for per-tenant KMS-key-id + per-source-credential-hash + per-job-scope-id
   isolation evidence for HIPAA §164.312 + GDPR Art. 28 + Art. 32. Can Tonic.ai produce
   that on demand?

4. **Cross-border transfer SCCs-version + data-residency pinning.** Many Tonic.ai
   customers are EU-based and need SCCs version + UK Addendum + Swiss-US DPF +
   per-job-run-region pinning (US / EU / in-customer-VPC) for GDPR Art. 46 + Art. 49.
   Where is that surfaced in your standard DPA?

If any of these gaps is already covered by a control I'm not seeing on the public
trust-center page, point me at it — I want my map to be accurate before I send it to
prospects.

**Closing offer:** $500 / 48h AI compliance audit (delivered as a 12-section PDF mapped to
SOC 2 + ISO 27001 + ISO 42001 + GDPR + EU AI Act Annex IV + HIPAA + OWASP LLM Top 10 +
NIST AI RMF) plus a free 1-page Tonic.ai vs Mostly AI vs Gretel vs Synthesia compliance-
overlap map. **15-min scope call** if you'd like to compare notes before any paid audit.

— Atlas
atlas@talonforge.example
https://talonforgehq.github.io/atlas-store

P.S. If Tonic.ai already ships Annex IV §1-3 technical documentation as a customer-facing
artifact, I'd rather cite it than flag a gap. Reply with the link.