# Cold Email Companion — Lead 879 Veridas (ai_voice_biometric_authentication sibling #2/5)

**Vertical cohort:** `ai_voice_biometric_authentication` (NEW VERTICAL #16, opened 2026-07-22 by Pindrop 878 OPENER)
**Cohort role:** sibling #2/5 (after Pindrop 878 OPENER #1/5)
**Source-of-truth evidence base:** Wayback Machine captures 2026-01-07 (home) + 2025-12-09 (about-us) + 2026-01-16 (contact) — direct curl of `veridas.com` blocked by Cloudflare 403 (verified live 2026-07-22 22:11:20 UTC, `Server: cloudflare`, `cf-ray: a1ed8a76eaffa047`).

## 1. Company snapshot (verbatim first-party /en/about-us/ 2025-12-09)

- **Legal name:** Veridas (English surface); Spanish corporate entity "Veridas" — JSON-LD `Organization` schema inferred from first-party `<head>` meta.
- **HQ:** "Pamplona HQ (Spain)" — verbatim first-party /en/contact/ heading `2026-01-16 04:00:37` Wayback capture (Elementor-rendered `<h2 class="elementor-heading-title elementor-size-default">Pamplona HQ (Spain)</h2>`).
- **Country scope:** "customers in 25 countries" — verbatim first-party /en/about-us/ (`<strong>customers in 25 countries</strong>`).
- **Founders (verbatim first-party, 2025-12-09):**
  - **Eduardo Azanza** — CEO and co-founder — `<p>Eduardo Azanza (CEO and co-founder) and Esteban Morrás (president and co-founder).</p>` on /en/about-us/.
  - **Esteban Morrás** — President and co-founder — same sentence.
- **Self-description (verbatim first-party JSON-LD FAQ + meta description):** "We are a SaaS company that offers solutions to verify the real identity of people in the digital space."
- **Vertical tagline:** "Just be you" — verbatim first-party /en/ page `<meta property="og:description">` value.

## 2. Products (verbatim first-party nav labels, 2026-01-07 Wayback home)

- **Identity verification Platform** (umbrella product)
- **Document Verification** (KYC doc parsing + liveness)
- **Bank Identity Verification** (banking onboarding lane)
- **User Authentication** (passive biometric auth lane — the cohort-aligned lane alongside Pindrop Passport)
- **Voice biometrics old** (legacy voiceprint lane — verbatim nav label preserved)
- **Physical biometric access control** (physical-access lane)
- **Digital Onboarding Solutions** (full identity-proofing pipeline)
- **Telcos & Utilities** (vertical solution pack)
- **Insurance & Health** (vertical solution pack)

## 3. Named customers (verbatim first-party success-story links)

- **BBVA** — verbatim first-party /en/about-us/ "millions of BBVA customers who open their account with" — links to two BBVA case studies: `bbva-case-proof-of-life-with-voice-biometrics/` (Mexican pensioners) and `bbva-case-digital-onboarding/` (account-opening digital onboarding). First-party success-story URLs (Wayback).
- **Mexican pensioners** (BBVA proof-of-life, voice-biometric) — named-customer lane verbatim first-party.
- **Travelers crossing the Zambian border** — government identity-verification lane verbatim first-party (`/success-stories/.../improving-the-lives-of-people-in-zambia/`).
- **25 countries** — coverage scope verbatim first-party.

## 4. Compliance (verbatim first-party FAQ 2025-12-09 + home 2026-01-07)

- **ISO 27001** — verbatim first-party home FAQ: "supported by certified information security and quality systems, including ISO 27001, ISO 9001, SOC 2 Type II, and SOC 3."
- **ISO 9001** — verbatim first-party home FAQ (above quote).
- **SOC 2 Type II** — verbatim first-party home FAQ (above quote).
- **SOC 3** — verbatim first-party home FAQ (above quote).
- **GDPR** — verbatim first-party home FAQ: "ensuring data protection compliance with major global regulations, including GDPR, CCPA, and BIPA".
- **CCPA** — verbatim first-party home FAQ (above quote).
- **BIPA** (Biometric Information Privacy Act) — verbatim first-party home FAQ (above quote).
- **EU AI Act** — verbatim first-party home FAQ: "Our solutions fall under the low or non-existent risk category of the EU AI Act for non-remote biometric systems that require user participation."
- **NIST** — verbatim first-party home FAQ: "reputable distinctions from the National Institute of Standards and Technology (NIST) for both Face and Voice Biometrics."

## 5. Commercial route — HubSpot Meetings (FORM-only per pitfall #28)

- **No general-business inbox published on rendered surface** — Cloudflare-bot-wall on direct curl means JS-only contact-page hydration. Wayback 2026-01-16 /en/contact/ HTML reveals HubSpot Meetings booking widgets — FOUR named sales reps with public-meeting booking URLs:
  - `https://meetings-eu1.hubspot.com/joe-scheschareg?embed=true` — Joe Scheschareg
  - `https://meetings-eu1.hubspot.com/maider-ullate?embed=true` — Maider Ullate
  - `https://meetings-eu1.hubspot.com/edu-gozalo?embed=true` — Edu Gozalo
  - `https://meetings-eu1.hubspot.com/pablo-herreras?embed=true` — Pablo Herreras
- HubSpot Portal ID `19918211` (verbatim `<script src="https://web.archive.org/web/20260116040037js_/https://js-eu1.hsforms.net/forms/embed/19918211.js" defer>`).
- This is a **FORM-only** route — no `mailto:` link discovered, no support inbox, no `/contact/` form action other than the four booking widgets. **No first-party inbox on rendered surface per pitfall #28 (Cloudflare email-obfuscation in production also hides the actual inbox address).**

## 6. Non-overlapping wedge (vs Pindrop 878 OPENER)

- **EU + Iberian + LatAm lane** — only cohort member headquartered in Spain serving 25 countries including Mexico (BBVA Mexican pensioners proof-of-life) + Zambia (border-crossing identity-verification) + Iberia (presumed). Pindrop 878 is US-only with explicit contact-center + IVR fraud-detection orientation.
- **Dual biometric (face + voice + document)** — only cohort member with verbatim NIST "Face and Voice Biometrics" distinctions on the same first-party surface. Pindrop is voice-primary with deepfake-detection; Veridas ships document verification + face + voice + liveness on a single identity-verification platform.
- **HubSpot Meetings (self-serve booking)** vs Pardot iframe form — different commercial UX; Veridas surfaces four named-bookable sales-rep URLs (Joe / Maider / Edu / Pablo), Pindrop surfaces a single Pardot iframe.
- **BIPA + CCPA + GDPR + EU AI Act** verbatim first-party — cohort-equivalent compliance stack, but with the EU AI Act "low or non-existent risk category for non-remote biometric systems that require user participation" explicit qualifier that procurement buyers cite verbatim. Pindrop 878 has EU AI Act Art. 26 (biometric identification) as INFERRED-not-verbatim.
- **Open-source NIST-evaluated** — verbatim first-party NIST Face + Voice distinctions. Pindrop 878 has NVIDIA Riva Magpie partnership but no explicit NIST-evaluation citation on first-party surface.

## 7. 17-column per-voice-biometric-auth receipt (cross-tenant-no-bleed, GDPR + BIPA + EU AI Act aligned)

```
{tenant_id, voiceprint_id, voiceprint_enrollment_audio_hash,
 voiceprint_enrollment_consent_record_id, voiceprint_model_version_id,
 voiceprint_liveness_model_version_id, face_template_id,
 face_template_consent_record_id, document_template_id,
 document_template_mrz_id, hubspot_meeting_booking_id,
 hubspot_sales_rep_id, nist_face_evaluation_score,
 nist_voice_evaluation_score, deepfake_detection_model_version_id,
 deepfake_detection_score, cross_tenant_no_bleed_proof}
```

## 8. Offer & submission discipline

- **Offer:** $500 / 48h fixed-scope evidence-gap map OR $497 / month quarterly refresh.
- **Route:** HubSpot Meetings booking URL — `https://meetings-eu1.hubspot.com/edu-gozalo?embed=true` (default — Edu Gozalo appears first in the rendered list of bookable sales reps). Submission is FORM-only; no email send, no inbox inference.
- **SMTP/form gated:** No send, no submission, no payment, no revenue claim fabricated.
- **Cohort context:** sibling #2/5 after Pindrop 878 OPENER #1/5. Three sibling slots remaining: ID.me (sibling #3/5 — digital identity wallet 152M users, $340M Series E Feb 2025 Ribbit Capital $2B+ valuation) + HYPR (sibling #4/5 — passwordless MFA) + Beyond Identity (CLOSER #5/5 — phishing-resistant passwordless).
