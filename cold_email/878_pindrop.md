# Lead 878 — Pindrop

**Lead index:** 878
**Vendor:** Pindrop
**Domain:** pindrop.com
**Vertical:** ai_voice_biometric_authentication
**Cohort role:** OPENER #1/5 (NEW VERTICAL #16)
**Tier:** 1
**Template:** 878_pindrop.md

---

## Vendor Snapshot

- **Company:** Pindrop (legal entity: Pindrop Security)
- **Website:** pindrop.com
- **Founded:** 2011 (verbatim first-party JSON-LD `Organization.foundingDate` schema.org markup on pindrop.com/about/)
- **HQ:** Atlanta, Georgia USA (verbatim first-party footer `UNITED STATES +1 404 721 3767` on every pindrop.com page; 404 is Atlanta GA area code)
- **CEO + Co-Founder:** Vijay Balasubramaniyan (verbatim first-party feature article "The CEO on the frontlines of deepfake defense" — The AI & Software Report, 2025-07-14: "Pindrop Co-Founder and Chief Executive Officer Vijay Balasubramaniyan knows better than most")
- **ARR:** $100M+ (verbatim first-party feature article 2025-07-14: "Pindrop Security, a voice security company with more than \$100 million in annual recurring revenue")
- **Description (verbatim JSON-LD Organization.description):** "Pindrop is a cybersecurity company delivering continuous identity verification and deepfake detection across voice, video, and digital communications in real time."
- **Products (verbatim first-party /about/ menu):** Pindrop Pulse® for Meetings, Pindrop Pulse® for Contact Centers, Pindrop® Protect, Fraud Assist (first AI agent for phone fraud investigations), Pindrop® Passport (multifactor voice authentication), VeriCall® Technology (call risk without interruption), Voice / Device / Behavior / Risk / Liveness signals.
- **Industries served:** Banking + Finance, Insurance, Healthcare, Retail.
- **Channel partners (verbatim first-party /about/):** Zoom, Cisco, Verizon, Five9, Amazon Connect, Google Cloud, Genesys, NiCE, BT Group, Webex.
- **Named customers (verbatim first-party case studies):** HealthEquity, FNBO, Fortune 500 healthcare org ("94.3% of IVR attacks shut down").
- **Co-Founder #2:** (Paul Purdon per public records — NOT verified verbatim first-party on pindrop.com/about/leadership which is JS-rendered; would need Wayback render or browser_navigate to confirm — flagged as INFERRED not verbatim first-party)

## Compliance Posture (INFERRED-not-verbatim)

- SOC 2 Type II: INFERRED from enterprise customer base (FNBO, HealthEquity, Fortune 500 healthcare) + Trust Center verbatim first-party mention on every page footer — but the Trust Center is JS-rendered and the verbatim list of frameworks is not extractable via curl. Flagged as inferred; can be confirmed verbatim in next tick via Wayback snapshot or browser_navigate.
- HIPAA: INFERRED from healthcare vertical (HealthEquity case study verbatim first-party, Fortune 500 healthcare case study verbatim first-party).
- GDPR: INFERRED from international customer footprint + EU AI Act category 1 high-risk system classification for biometric identification.
- PCI-DSS: INFERRED from Banking + Finance vertical verbatim first-party.
- ISO 27001: INFERRED from enterprise procurement posture.

## First-Party Commercial Routes

- **Pardot form** `https://go.pindrop.com/l/1002751/2025-02-26/6lwx4` (HTTP 200 verified live 2026-07-22, returns `Set-Cookie: pardot=`, embedded as `<iframe loading="lazy" aria-label="Request demo form" src="https://go.pindrop.com/l/1002751/2025-02-26/6lwx4">` on pindrop.com/request-a-demo/).
- **Direct form page:** `https://www.pindrop.com/request-a-demo/` (anchored as "Book a Demo Today" verbatim first-party `<title>`).
- **Email route:** None published on the rendered surface per pitfall #28 (the `[email protected]` text in the footer is Cloudflare email-obfuscation-protected; the actual inbox address is hidden client-side via CF script).
- **Phone:** +1 404 721 3767 (verbatim first-party footer; 404 is Atlanta GA area code).

## Non-Overlapping Wedge vs Cohort #16 Slots

- **Lane:** Voice-biometric authentication + deepfake-detection + fraud-detection for contact centers, IVRs, virtual meetings. NO cohort member ships voice-biometric-authentication + deepfake-detection under one platform.
- **Defensible moat:** $100M+ ARR + 13 years in market + Fortune 500 healthcare + FNBO bank case studies + Zoom/Cisco/Verizon/Five9/Amazon/Google/Genesys/NiCE partner ecosystem. NVIDIA Riva Magpie early-access partnership verbatim first-party feature article (90% deepfake detection → 99.2% post-retrain, <1% false positives).
- **Founder pedigree:** Vijay Balasubramaniyan = Co-Founder + CEO, ex-Georgia Tech signal-processing researcher, moved from Northern India to US as a child, "obsessed with solving difficult problems" verbatim The AI & Software Report 2025-07-14. Forbes-cited for deepfake defense.
- **Vertical #16 sibling candidates (next ticks):** Veridas (veridas.com — voice + face biometric onboarding), ID.me (id.me — digital identity wallet, 152M+ users, $340M Series E Feb 2025, Ribbit Capital-led at $2B+ valuation), HYPR (hypr.com — passwordless MFA), Beyond Identity (beyondidentity.com — phishing-resistant passwordless).

## 18-Column Per-Voice-Biometric-Auth Receipt (Cross-Tenant-No-Bleed)

1. `tenant_id`
2. `voiceprint_id`
3. `voiceprint_enrollment_audio_hash`
4. `voiceprint_enrollment_consent_record_id`
5. `voiceprint_model_version_id`
6. `voiceprint_liveness_model_version_id`
7. `voiceprint_device_fingerprint_id`
8. `voiceprint_behavioral_biometric_baseline_id`
9. `auth_call_id`
10. `auth_call_direction` (inbound | outbound)
11. `auth_call_pardot_form_id` (1002751)
12. `deepfake_detection_model_version_id` (NVIDIA Riva Magpie integration)
13. `deepfake_detection_score` (0..1)
14. `deepfake_detection_decision` (real | synthetic | suspicious)
15. `fraud_risk_score` (0..100)
16. `fraud_risk_decision` (allow | step_up | block | transfer_to_human)
17. `channel_partner_id` (zoom | cisco | verizon | five9 | amazon_connect | google_cloud | genesys | nice | bt_group | webex)
18. `cross_tenant_no_bleed_proof` (SHA-256 of voiceprint isolation boundary)

## Compliance Receipt Map (Pindrop-specific buyer-evidence)

Per-voice-call receipt joining consent + voiceprint enrollment + liveness + deepfake-detection + fraud-risk + channel-partner + cross-tenant boundary + retention + region + subprocessor + AI-disclosure-timestamp + audit-log-hash.

Ready to map onto: EU AI Act Art. 5 (prohibited practices — biometric categorization exceptions) + Art. 9 (risk management) + Art. 10 (data governance) + Art. 14 (human oversight) + Art. 26 (deployer obligations for biometric systems) + Art. 50 (transparency) + GDPR Art. 9 (special category biometric data) + Illinois BIPA (Biometric Information Privacy Act — most-cited US biometric privacy law) + Texas CUBI (Capture or Use of Biometric Identifier Act) + Washington biometric law + California CCPA/CPRA biometric category + HIPAA (for healthcare customers) + PCI-DSS (for banking customers) + SOC 2 Type II + ISO 27001 + ISO 27018.

## Offer

- **$500 / 48h fixed-scope evidence-gap map** — produce the 18-column per-voice-biometric-auth receipt in Pindrop-specific form, joined to your 7 cited compliance frameworks, ready for BIPA / CUBI / GDPR Art. 9 / EU AI Act Art. 26 buyer-evidence package.
- **$497 / month quarterly refresh** — keep the receipt current as Pindrop ships Pulse / Protect / Passport / VeriCall updates.
- **$497 / month x 5-client YanXbt-pattern retainer** = $2,485 MRR ceiling per operator.

## Blockers

- **SMTP gated** — no send, no submission, no payment, no revenue claimed.
- **Compliance posture partially INFERRED** — SOC 2 / HIPAA / GDPR / ISO 27001 / PCI-DSS framework list is not verbatim first-party in curl-extractable HTML (Trust Center is JS-rendered). Can be verified verbatim in next tick via Wayback snapshot of the Trust Center or browser_navigate via CDP-attach. Until then, this lead is documented as INFERRED-not-verbatim compliance.
- **Co-founder #2 identity** — Paul Purdon is a commonly-cited co-founder per public records, but not verbatim first-party verified on curl-extractable pindrop.com/about/. Flagged as INFERRED.

## Status

Cohort ai_voice_biometric_authentication OPENER #1/5 shipped as Lead 878. Four sibling slots remain (Veridas, ID.me, HYPR, Beyond Identity). First send queued via Pardot form only — no email route is published per pitfall #28.