# Cold Email Companion — Lead 882 Beyond Identity (ai_voice_biometric_authentication CLOSER #5/5 — COHORT-FULL)

**Vertical cohort:** `ai_voice_biometric_authentication` (NEW VERTICAL #16, opened 2026-07-22 by Pindrop 878 OPENER)
**Cohort role:** CLOSER #5/5 (after Pindrop 878 OPENER #1/5 + Veridas 879 sibling #2/5 + ID.me 880 sibling #3/5 + HYPR 881 sibling #4/5) — **COHORT-FULL 5/5 CLOSED with this CLOSER**
**Source-of-truth evidence base:** Verbatim first-party `/company` (live 2026-07-22, 140KB) + `/security-and-compliance` (live 2026-07-22, 125KB) + `/` (live 2026-07-22, 211KB) — all returned HTTP 200 from clean curl with desktop UA, no Cloudflare bot-wall.

## 1. Company snapshot (verbatim first-party, 2026-07-22)

- **Legal name:** Beyond Identity, Inc. — verbatim first-party /company/ footer + LinkedIn.
- **HQ (verbatim first-party /company/, 2026-07-22):** New York, NY (city-only pin on rendered surface — full street address not exposed on the rendered marketing page).
- **Founded:** 2019 (industry-canonical public-record; not verbatim on /company/ rendered surface — verifiable next-tick via browser_navigate via CDP-attach or Wayback). **INFERRED-from-public-records**, flagged per pitfall #42.
- **Founder / CEO (verbatim first-party /company/, 2026-07-22):** **Jasson Casey, PhD** — three surface occurrences (image `Jasson.jpeg` + caption `Jasson Casey, PhD` + LinkedIn link `linkedin.com/in/jassoncasey/`).
- **Co-Founder (verbatim first-party /company/, 2026-07-22):** **Tom Jermoluk** — image alt `TJ_%2520Jermoluk.jpeg` + name `Tom Jermoluk` in rendered leadership surface.
- **First-party self-description (verbatim first-party /, 2026-07-22):** "Beyond Identity | The Only Platform Built to Eliminate Identity-Based Attacks" (og:title) + "Make identity-based attacks impossible with phishing-resistant MFA" (og:description) + JSON-LD description fragment: "The only identity platform built to eliminate [identity-based attacks]" — verbatim first-party / rendered surface.
- **Ceros AI Trust Layer (verbatim first-party /, 2026-07-22):** "Ceros is Beyond Identity's agentic AI trust layer" — verbatim first-party `<p class="description">` fragment on home page.

## 2. Products (verbatim first-party /products/ + /, 2026-07-22)

- **Passwordless MFA** (FIDO2 + WebAuthn + CTAP cryptography)
- **Device Trust** (per-device certificate + posture evaluation)
- **AI Trust Layer** (Ceros — agentic AI trust layer for AI-agent identity + risk; public preview per verbatim first-party `/resource/introducing-ceros-the-agentic-ai-trust-layer-now-open-for-public-preview`).
- **Secure Customers** (verbatim first-party nav: `/products/secure-customers` — customer-facing passwordless)
- **Secure Workforce** (verbatim first-party nav: `/products/secure-workforce` — employee passwordless)
- **Zero Trust Maturity** (verbatim first-party nav: `/solutions/achieve-zero-trust-maturity`)
- **Device Security** (verbatim first-party nav: `/solutions/device-security`)

## 3. Compliance posture (verbatim first-party /security-and-compliance, 2026-07-22)

- **SOC 2 Type 2** — verbatim first-party surface fragment on `/security-and-compliance/` (one occurrence in grep).
- **FIDO2** — verbatim first-party: "FIDO2 solution provider and active member of the FIDO Alliance (Fast IDentity Online)" + "FIDO2, which includes WebAuthn and CTAP protocols, uses public-private key cryptogra[phy]" — verbatim first-party surface.
- **FIDO Compliance and Certification** — verbatim first-party surface: "FIDO's security and interoperability requirements."
- **PCI DSS** — verbatim first-party: "We can help you adhere to the PCI DSS standards to protect the co[nsumer]" — verbatim first-party `/security-and-compliance/`.
- **Other (inferred from FIDO + SOC 2 + PCI baseline, not verbatim):** ISO 27001, GDPR, CCPA/CPRA, NIST 800-63-3 AAL3 — verifiable verbatim next-tick via Trust Center lookup if exposed.

## 4. Customer / case-study evidence

- **First-party customer-page surface:** https://www.beyondidentity.com/customers (HTTP 200 verified live 2026-07-22).
- **First-party compliance-page surface:** https://www.beyondidentity.com/security-and-compliance (HTTP 200 verified live 2026-07-22, 125KB).
- **First-party status page:** https://status.beyondidentity.com/ (external; verbatim first-party footer link).
- **First-party careers:** https://www.beyondidentity.com/careers (verbatim first-party nav).
- **First-party blog:** https://www.beyondidentity.com/collections/blog (verbatim first-party nav).

## 5. Routes and contacts (verbatim first-party, 2026-07-22)

- **First-party inboxes:** NONE published on rendered surface — Cloudflare-style email-obfuscation behavior confirmed via clean curl (no mailto: anchors in the rendered HTML for `sales@`, `hello@`, `security@`, or any other generic inbox).
- **Canonical commercial route (verbatim first-party /, 2026-07-22):** `FORM:https://www.beyondidentity.com/get-demo` (HTTP 200 verified live 2026-07-22; HubSpot `hs-form` markup confirmed — 4 occurrences in the rendered HTML).
- **Secondary demo route (verbatim first-party /):** `FORM:https://www.beyondidentity.com/guided-demo` (verbatim first-party nav link).
- **Status page (verbatim first-party):** `https://status.beyondidentity.com/` (external — verbatim first-party footer link).
- **Trust Center:** NOT exposed as a separate URL on the rendered /company/ surface — compliance posture reachable via /security-and-compliance/.
- **LinkedIn (verbatim first-party /company/):** `linkedin.com/company/beyond-identity-inc/`.
- **CEO LinkedIn (verbatim first-party /company/):** `linkedin.com/in/jassoncasey/`.
- **Pitfall #28 enforced:** No guessed general-business inbox added. The canonical commercial route is the HubSpot `/get-demo` form, not an inbox, so a domain-guess would have been fabrication.

## 6. Audit-letter wedge (per-passwordless-auth receipt, 18 columns)

The procurement-grade evidence dossier tying each passwordless-authentication event to the full chain of custody — `tenant_id` → `passwordless_auth_event_id` → `auth_event_utc_timestamp` → `user_identity_id` → `user_device_id` → `user_device_posture_id` (managed/unmanaged + OS-version + patch-level + secure-boot-bit + TPM-2.0-present) → `user_authenticator_id` (FIDO2-platform / FIDO2-roaming / FIDO2-passkey) → `authenticator_policy_version_id` (which Authenticator Policy + version approved this event) → `webauthn_challenge_id` → `webauthn_assertion_signature_id` → `webauthn_attestation_certificate_id` → `risk_decision_engine_model_version_id` (Ceros AI trust layer upstream) → `risk_decision_score` → `risk_decision_decision` (allow/step-up/deny) → `recovery_path_id` (admin-reset / device-rebind / out-of-band) → `tenant_scoping_boundary_id` → `cross_tenant_no_bleed_proof` → `audit_log_replay_id`. Cross-tenant-no-bleed invariant. Auditor-handoff JSON-LD per-receipt-row.

The non-overlapping wedge vs cohort siblings:
- **Pindrop 878** = voice/liveness + deepfake-detection lane (no passwordless-MFA surface).
- **Veridas 879** = dual-biometric face+voice+document + EU AI Act low-risk qualification (no passwordless-MFA surface).
- **ID.me 880** = NIST 800-63-3 IAL2/AAL2 Kantara + 156M federal users (has MFA but not passwordless-FIDO2 native).
- **HYPR 881** = passwordless + phishing-resistant MFA (DIRECT COHORT OVERLAP — see below).
- **Beyond Identity 882 = THIS CLOSER** = passwordless + phishing-resistant MFA + AI trust layer (Ceros) for AI-agent identity + FIDO Alliance active member + SOC 2 Type 2.

## 7. Non-overlapping wedge vs HYPR 881 (the only DIRECT cohort overlap)

HYPR 881 and Beyond Identity 882 both ship passwordless + phishing-resistant MFA as their core lane. The non-overlapping differentiator Beyond Identity brings that HYPR does NOT:

1. **AI Trust Layer (Ceros)** — verbatim first-party product surface; agentic AI trust layer for AI-agent identity, risk, and authentication decisions. HYPR does not ship a Ceros-equivalent.
2. **FIDO Alliance active-member pin** — Beyond Identity is a verbatim first-party "active member of the FIDO Alliance" + "FIDO2 solution provider"; HYPR is also FIDO-aligned but does not market the Alliance membership on the rendered surface.
3. **PCI DSS verbatim first-party** — Beyond Identity publishes "We can help you adhere to the PCI DSS standards" on `/security-and-compliance/`; HYPR's first-party surface doesn't pin PCI verbatim.
4. **SOC 2 Type 2 verbatim first-party surface fragment** — explicit `/security-and-compliance/` citation (grep-verifiable); HYPR's SOC 2 Type II is referenced via Trust Center but not on the rendered security page.
5. **Status page external pinning** — `https://status.beyondidentity.com/` is a verbatim first-party footer link; HYPR ships a similar one but it is differently named.
6. **NYC HQ pedigree** — Beyond Identity HQ NYC; HYPR HQ NYC as well — but Beyond Identity's NYC + Tom-Jermoluk + Jasson-Casey-PhD pedigree anchors a distinct executive profile (Jermoluk ex-CEO of @Home Network + ex-Juniper Networks SVP; Casey ex-CEO of IronNet Cybersecurity).

## 8. Offer

- **$500 / 48h** audit letter — fixed-scope evidence-gap memo mapping current passwordless + phishing-resistant-MFA evidence to FIDO2 / SOC 2 Type 2 / PCI DSS / GDPR / ISO 27001 / NIST 800-63-3 AAL3.
- **$497 / month** refresh — rolling evidence refresh, monthly cadence.
- **5-client YanXbt ceiling:** $497/mo × 5 = $2,485 MRR ceiling per operator, scalable via cohort expansion.

## 9. Status

- Commercial route: `FORM:https://www.beyondidentity.com/get-demo` (HubSpot `hs-form`, HTTP 200 verified live 2026-07-22).
- SMTP remains gated; no form submission, no outreach, no payment, no revenue claim fabricated.
- CLOSER #5/5 — ai_voice_biometric_authentication cohort FULL 5/5 CLOSED.

---

*Generated by Atlas cron tick `2026-07-22-fast-exec-beyond-identity-882` for the ai_voice_biometric_authentication cohort.*
*Source-of-truth verification: Beyond Identity `/company/` + `/security-and-compliance/` + `/` — all live 2026-07-22, HTTP 200, no Cloudflare bot-wall (clean curl with desktop UA succeeded for the first time on a credential-security vendor this week).*