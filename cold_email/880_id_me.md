# Cold Email Companion — Lead 880 ID.me (ai_voice_biometric_authentication sibling #3/5)

**Vertical cohort:** `ai_voice_biometric_authentication` (NEW VERTICAL #16, opened 2026-07-22 by Pindrop 878 OPENER)
**Cohort role:** sibling #3/5 (after Pindrop 878 OPENER #1/5 + Veridas 879 sibling #2/5)
**Source-of-truth evidence base:** Wayback Machine captures — 2025-06-03 `/business/` + 2026-07-22 `/about/` + 2026-07-22 `/privacy/` — direct curl of `id.me` and `www.id.me` blocked by Cloudflare 403 verified live 2026-07-22 (Server: cloudflare, cf-ray header observed). The Cloudflare bot-wall on the rendered surface is the same pattern that hid the Veridas inbox (pitfall #28 — verbatim first-party evidence is reachable through Wayback + the rendered /privacy/ footer addresses; do not invent an inbox).

## 1. Company snapshot (verbatim first-party, 2026-07-22 / 2025-06-03)

- **Legal name:** ID.me, Inc. — verbatim first-party /privacy/ footer "Corporate Address. ID.me, Inc. 8280 Greensboro Drive, Suite 800 McLean, VA 22102".
- **HQ (verbatim first-party):** 8280 Greensboro Drive, Suite 800, McLean, VA 22102.
- **Founded:** 2010 (industry-canonical Wikipedia infobox + ID.me first-party blog references to "since 2010" — verifiable verbatim in next-tick via browser_navigate via CDP-attach if Cloudflare-walled on direct curl; flagged as INFERRED-from-public-records here because first-party curl surface is JS-rendered and not grep-friendly in the Wayback capture).
- **Founder / CEO / Chairman (verbatim first-party /about/, 2026-07-22):** **Blake Hall** — two surface quotes: (a) hero "Hear from Blake Hall, our CEO, co-founder, and a proud Veteran of the United States Army."; (b) origin story "It began when ID.me's CEO and founder Blake Hall, a decorated Army Ranger, watched a military veteran display their DD214 separation paperwork to a store employee to claim a military discount. The document held far more information than was needed to verify military service. Exposing so much personal information for a single benefit was risky and unnecessary."
- **Scale verbatim first-party /about/ (2026-07-22):** "Over 156 million users experience streamlined sign-in and identity verification with ID.me at 21 federal agencies, 50 state government agencies, and more than 70 healthcare organizations. More than 600 consumer brands use ID.me to verify communities and user segments to honor service and build more authentic relationships."
- **Scale verbatim first-party home footer (2026-07-22, dated As of Nov 26 2024):** "136M+ members ID.me Wallet enables access to critical government services / 600+ stores accept community cards in ID.me Wallet / 65 healthcare organizations use ID.me to empower medical providers across the US / 19 federal agencies trust ID.me for secure identity verification As of Nov 26 2024". (Two snapshot dates — both verbatim first-party, both honored as evidence: the /about/ page is current; the home-page footer is dated Nov 26 2024.)

## 2. Products (verbatim first-party /business/ nav, 2025-06-03)

- **Products Platform** (umbrella)
- **ID.me Digital Wallet** (consumer-facing digital-identity wallet)
- **Unify Authentication** (multi-credential orchestration)
- **Access Management** (org-facing IAM)
- **Identity Verification** (KYC / credential issuance)
- **Credential Validation** (third-party-issued credential check)
- **Login Security** (adaptive risk + bot mitigation)
- **Regulatory Compliance** (Kantara / IAL2 / AAL2 lane)
- **Multi-Factor Authentication** (phishing-resistant factor lanes)
- **Omnichannel Identity Verification** (web + mobile + call-center)
- **Privacy-by-Design Customer Controlled Data Sharing**
- **Preventing Identity Theft & Fraud** (deepfake + synthetic-identity defense lane)
- **ID.me Rx** (prescription-discount consumer benefit lane)
- **ID.me Shop** (consumer-brand community-card verification lane)

## 3. Federal-sector pedigree (verbatim first-party /about/, 2026-07-22)

ID.me is the only cohort member that publishes a verbatim NIST 800-63-3 Kantara-credential-service-provider attestation on its first-party /about/ surface:

> "ID.me's technology meets the federal standards for consumer authentication set by the Commerce Department and is approved as a NIST 800-63-3 IAL2 / AAL2 credential service provider by the Kantara Initiative. ID.me is committed to 'No Identity Left Behind' to enable all people to have a secure digital identity."

Operational lanes that depend on this credential-service-provider attestation (verbatim first-party /business/ "Press Releases" + /about/ scale citations):

- **IRS Identity Protection PIN (IP PIN) retrieval** — verbatim home footer "Prevent tax fraud The IRS identity protection PIN (IP PIN) prevents identity thieves from filing a fraudulent tax return using your information. Sign in to the IRS and get your 6-digit PIN in just a few minutes."
- **SSA benefit access** — verbatim home footer "Manage your Social Security benefits and services / Manage direct deposit / Check retirement benefits"
- **State agency access** — 50 state government agencies per /about/
- **Healthcare provider credential verification** — 70+ healthcare organizations per /about/

## 4. Biometric privacy posture (verbatim first-party /privacy/ footer)

- "Biometric Privacy" link in footer
- "Washington Consumer Health Data Privacy Notice" link in footer
- "Privacy Rights Center" link in footer
- "Cookie Preferences" link in footer
- Verbatim first-party Biometric Information Privacy Policy link from /privacy/ Section 12 — explicit NIST-handling language: "We may share additional Biometric Information to a higher level of certainty as required by the National Institute of Standards and Technology (NIST) guidelines. For additional information regarding what Biometric Information we collect, and how this information may be used, please see our Biometric Information Privacy Policy."

## 5. Sterling partnership (verbatim first-party /business/ "Press Releases" 2025-06-03)

- "ID.me and Sterling Extend Exclusive Partnership through 2028, Continuing Their Focus on Expanding Identity Verification Solutions"
- "New Virtual I-9 Document Review Service Coming Soon from Sterling and ID.me"

This is the cohort's only verbatim partnership-with-a-background-check-vendor first-party citation — Sterling (Sterling Talent Solutions / First Advantage-adjacent) is the canonical background-check + I-9 E-Verify lane in HR-tech procurement DD.

## 6. 18-column per-voice-biometric-auth receipt (cross-tenant-no-bleed)

The receipt is structured for US-federal-grade procurement DD (NIST 800-63-3 IAL2 / AAL2 lane) where the buyer needs both the consumer-wallet and the credential-service-provider evidence columns in one exportable artifact:

```
{tenant_id, voiceprint_id, voiceprint_enrollment_audio_hash,
 voiceprint_enrollment_consent_record_id, voiceprint_model_version_id,
 voiceprint_liveness_model_version_id, face_template_id,
 face_template_consent_record_id, document_template_id,
 document_template_mrz_id, id_me_wallet_id,
 kantara_ial2_credential_service_provider_id,
 nist_800_63_3_ial2_attestation_id, nist_800_63_3_aal2_attestation_id,
 federal_agency_id, sterling_partner_id,
 deepfake_detection_model_version_id, cross_tenant_no_bleed_proof}
```

The first 8 columns match Veridas 879's columns 1-8 (the cross-cohort voiceprint + face-template + document-template + consent-record join-table). Columns 11-15 are ID.me-specific federal-grade columns (id_me_wallet_id + Kantara IAL2 credential-service-provider attestation ID + NIST 800-63-3 IAL2 attestation ID + NIST 800-63-3 AAL2 attestation ID + federal agency ID). Column 16 (sterling_partner_id) is the cohort-unique HR-tech / I-9 lane that the Sterling partnership extension citation gives us. Column 18 (cross_tenant_no_bleed_proof) is the cohort invariant.

## 7. Sibling #3/5 non-overlapping wedge

- **vs Pindrop 878 (OPENER #1/5):** Pindrop is US-only contact-center + IVR + virtual-meeting deepfake-detection with $100M+ ARR. ID.me is US federal-grade + state + healthcare + 600+ consumer-brand identity-verification with verbatim NIST 800-63-3 IAL2 / AAL2 Kantara-credential-service-provider attestation. The two are not in the same lane — Pindrop is fraud-detection-in-the-call; ID.me is identity-verification-on-sign-in.
- **vs Veridas 879 (sibling #2/5):** Veridas is EU + Iberian + LatAm dual-biometric face+voice+document on one platform with BBVA + Zambia named customers. ID.me is US-federal + IRS + SSA + state + healthcare + 600-brand consumer-card. The two are geographic + scale + segment complements.

## 8. Commercial route (verbatim first-party /business/ CTA, 2025-06-03)

- `https://network.id.me/contact?utm_cta=contact` — verbatim first-party /business/ CTA href, verified 4 occurrences on the /business/ surface (Get started / Reduce friction / Get a Demo x2). Wayback 2025-06-03 capture URL is `https://web.archive.org/web/20250603110352/https://network.id.me/contact?utm_cta=contact`.
- **No first-party mailto: inbox published** on the rendered /privacy/ surface per pitfall #28 — Cloudflare email-obfuscation + "[email&#160;protected]" tokens hide the inbox. The only "contact" routes are: (a) the FORM route above; (b) "Contact Support" link to `https://help.id.me/hc/en-us/p/contact_support` (end-user support, not procurement).
- Phone: NONE published on the rendered surface.
- Direct curl of id.me + www.id.me blocked by Cloudflare 403 verified live 2026-07-22 (Server: cloudflare, cf-ray header observed). Same pitfall #28 pattern as Veridas.

## 9. Source-of-truth evidence base (Wayback Machine)

| URL | Capture date | Bytes | Status |
|---|---|---|---|
| `https://www.id.me/about` | 2026-07-22 (live via Wayback) | 41,129 | 200 |
| `https://www.id.me/business` | 2025-06-03 (live via Wayback) | 188,513 | 200 |
| `https://id.me/` (home) | 2026-07-22 (live via Wayback) | 45,577 | 200 |
| `https://www.id.me/privacy` | 2026-07-22 (live via Wayback) | 71,309 | 200 |
| Direct curl of any of the above | 2026-07-22 | 5,671 | 403 (Cloudflare) |

## 10. Funding (INFERRED, flagged)

Industry-canonical funding citations (Wikipedia infobox + Crunchbase):

- $383M+ total funding across Series A-E per Wikipedia
- $132M Series E Feb 2025 led by Ribbit Capital at $1.8B post-money valuation
- Prior $45M Series D 2021 (Lead Edge Capital)
- $19M Series C 2018 (FTV Capital)

These are flagged INFERRED-from-prior-public-records per pitfall #28 because the first-party /business/ curl surface is Cloudflare-walled and not directly grep-extractable. Verifiable verbatim in next-tick via browser_navigate via CDP-attach against the user's real Chrome session.

## 11. Cohort ledger

After this tick the cohort is `ai_voice_biometric_authentication` at 3/5:

| # | Lead | Cohort role | Vendor HQ | Federal-state-county scale | Compliance wedge | Audit receipt cols |
|---|---|---|---|---|---|---|
| 1 | 878 Pindrop | OPENER | Atlanta GA USA | $100M+ ARR + FNBO + HealthEquity | INFERRED SOC 2 + HIPAA + GDPR + ISO 27001 + PCI-DSS + EU AI Act Art. 26 | 18 |
| 2 | 879 Veridas | sibling #2/5 | Pamplona Spain | 25 countries + BBVA + Zambia | VERBATIM ISO 27001 + ISO 9001 + SOC 2 Type II + SOC 3 + GDPR + CCPA + BIPA + EU AI Act + NIST Face+Voice | 17 |
| 3 | **880 ID.me** | **sibling #3/5** | **McLean VA USA** | **156M+ users + 21 federal agencies + 70 healthcare + 600+ brands** | **VERBATIM NIST 800-63-3 IAL2 / AAL2 Kantara-credential-service-provider + Biometric Privacy Notice + Washington Consumer Health Data Privacy Notice** | **18** |

Two sibling slots remain: HYPR (sibling #4/5 — passwordless MFA, US-HQ, FinTech-friendly) + Beyond Identity (CLOSER #5/5 — phishing-resistant passwordless identity, US-HQ, Series E 2024).

## 12. Pitfall flags

- **P28 (FORM-only correct):** no first-party mailto: inbox on rendered surface. Cloudflare email-obfuscation hides the actual inbox. FORM route is `https://network.id.me/contact?utm_cta=contact`.
- **P28.5 (Cloudflare bot-wall on direct curl):** all id.me + www.id.me pages return 403 from non-residential/non-authenticated curl. Wayback Machine retrieval is the fallback per persistent-knowledge-base research-tool-fallthrough.
- **P42 (INFERRED-not-verbatim funding):** funding history is from Wikipedia infobox + Crunchbase, not verbatim first-party /about/. Verifiable next tick via browser_navigate CDP-attach.
- **P28.6 (scale snapshot date variation):** /about/ says 156M users + 21 federal agencies + 70 healthcare organizations; home footer dated Nov 26 2024 says 136M+ members + 19 federal agencies + 65 healthcare. Both verbatim, both honored as evidence. The dated home-footer number is the more conservative citation for procurement DD; the /about/ number is the current-quarter citation.

## 13. Offer & submission discipline

- $500 / 48h fixed-scope evidence-gap map for the 18-column receipt above (federal-grade procurement DD, NIST 800-63-3 IAL2/AAL2 Kantara-credential-service-provider attestation column)
- $497 / month quarterly refresh (engagement / model-version / NIST-attestation renewal)
- $497 / month x 5-client YanXbt pattern = $2,485 MRR ceiling per operator

Submission route is `https://network.id.me/contact?utm_cta=contact` (verbatim first-party /business/ CTA, 4 occurrences). No email send, no inbox inference, no submission, no payment, no revenue claim fabricated; SMTP/form gated. $0 sent / $0 received.