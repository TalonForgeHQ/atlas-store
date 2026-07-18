# Cold outreach — Memberstack

**To:** support@memberstack.com
**Cc:** partnerships@memberstack.com
**From:** Atlas (Talon Forge LLC) — atlas@talonforge.io
**Subject:** 48-hour audit for Memberstack's AI-gated memberships + AI-managed members ($500 fixed)

---

Hi Tyler and Duncan,

Memberstack's first-party surfaces now document AI-gated memberships, AI-gated content, and AI-managed members on top of Webflow auth and Stripe payments. Your live help-center article describes AI-gated content and memberships, and your About page still describes Memberstack as the Y Combinator–backed auth and payments layer for 50,000+ Webflow sites, with Tyler Bell and Duncan Hamra as co-founders and SOC 2 certification.

That makes the evidence trail more consequential than a normal Webflow component: a recommendation can gate or ungate paid content, mutate membership state, or push a Stripe-side action.

I run a fixed-price, 48-hour AI-agent audit for creator platforms. For Memberstack I would test five questions:

1. Can one record reconstruct **member request → Memberstack tenant → Webflow site → AI-gated content rule → prompt/model/version → recommendation → Stripe subscription or payment-intent → Webflow mutation → member event**?
2. For AI-managed members, can one trace **operator prompt → retrieved member history → generated action → human approval → Memberstack object mutation → Stripe side effect**, including rollback when an AI action was wrong?
3. Can hostile Webflow page text, member uploads, connected-tool content, or Stripe metadata inject instructions into the AI-gating or AI-managed-members pipeline?
4. Do tenant and Webflow-site boundaries prevent one Memberstack customer's members, payment data, gating rules, or Stripe connection from entering another tenant's retrieval or model context?
5. Can Memberstack produce immutable incident evidence linking model/prompt changes, retries, partial failures, human approval, deletion, and per-run cost without stitching together unrelated logs?

The deliverable is a prioritized gap map, reproducible failure cases, and an implementation-ready evidence schema mapped to SOC 2 CC6.1 / CC7.2, EU AI Act Articles 12 and 14, GDPR Article 28, PCI DSS 4.0 Requirement 3, ISO 42001, NIST AI RMF, and OWASP LLM Top 10.

**Price:** $500 fixed. **Delivery:** 48 hours. If this belongs with Trust, Security, Legal, or the AI product owner, a redirect is enough.

— Atlas
Talon Forge LLC
atlas@talonforge.io

P.S. I used public first-party Memberstack surfaces only: the About page identifies Tyler Bell and Duncan Hamra as co-founders and the SOC 2 / YC-backed / 50,000+ Webflow-sites claim; the Contact page exposes support@memberstack.com and partnerships@memberstack.com; and the live help-center documents AI-gated content and memberships plus the AI-managed-members flow.
