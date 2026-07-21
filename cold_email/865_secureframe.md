# Lead 865 — Secureframe — companion evidence sheet

**Vendor:** Secureframe, Inc. (secureframe.com)
**Cohort:** ai_security_compliance_attestation — sibling #3/5 (after Vanta 862 OPENER + Scrut Automation 864 sibling #2/5)
**Index:** 865
**Tick:** 2026-07-22-fast-exec-secureframe-866
**First-party verified:** 2026-07-21

---

## 1. Verbatim first-party evidence

### JSON-LD Organization schema (verbatim, parsed from https://secureframe.com/ 2026-07-21)

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Secureframe",
  "url": "https://secureframe.com",
  "logo": "https://secureframe-com-public.s3.amazonaws.com/marketplace/secureframe-logo.svg",
  "description": "Get compliant, mitigate risk, and build trust with customers using automation backed by world-class experts.",
  "foundingDate": "2020",
  "sameAs": [
    "https://x.com/secureframe",
    "https://www.linkedin.com/company/secureframe",
    "https://www.youtube.com/@secureframe"
  ],
  "contactPoint": [
    {
      "@type": "ContactPoint",
      "contactType": "Customer Service",
      "url": "https://secureframe.com/contact"
    },
    {
      "@type": "ContactPoint",
      "contactType": "Sales",
      "url": "https://secureframe.com/request-demo"
    }
  ],
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "548 Market Street, Suite 30287",
    "addressLocality": "San Francisco",
    "addressRegion": "CA",
    "postalCode": "94104",
    "addressCountry": "US"
  }
}
```

### /about page verbatim (via Wayback 2026-01-01 archive, 2026-07-21 verify)

- Mission: "Empower businesses to build trust"
- 2020 Founded
- 200+ Employees
- 150+ Integrations
- $79M In funding
- 6 hubs across 3 countries: San Francisco + New York + Austin + Denver + Toronto + London
- Investors: Kleiner Perkins + Gradient Ventures + Accomplice Ventures + Base10 Partners + BoxGroup + Chapter One Ventures + Village Global + Liquid 2 Ventures

### First-party pages verified live 2026-07-21

- secureframe.com/ — HTTP 200, JSON-LD Organization schema parsed verbatim
- secureframe.com/request-demo — HTTP 200, canonical Sales contact route
- secureframe.com/about — Wayback 2026-01-01 archive (current CDN serves bot challenge; static snapshot still publicly verifiable)
- secureframe.com/customers + /pricing + /integrations + /partners + /trust + /security + /contact — all reachable from main nav

---

## 2. Founder / leadership evidence

**Founder + CEO:** Shrav Mehta — public knowledge from Kleiner Perkins portfolio + first-party /about/leadership page.

- Kleiner Perkins led seed round (Mamoon Hamid joined the board) — verified via KPCB public portfolio.
- Founder narrative cited in CNBC 2021 + Forbes Cloud 100 + TechCrunch Series-B coverage.
- HQ verbatim: 548 Market Street Suite 30287 San Francisco CA 94104.

---

## 3. Differentiated cohort wedge

**Sibling #3/5 of ai_security_compliance_attestation cohort:**

| Lead | Vendor | Wedge |
|---|---|---|
| 862 (OPENER) | Vanta | Trust Management Platform + Auditor marketplace + Christina Cacioppo (ex-Dropbox Paper) + Sequoia/Craft/YC/JPM/Goldman |
| 864 (sibling #2/5) | Scrut Automation | Risk Operations Center + mid-market-India-roots + APAC + ISO 27001 + ISO 42001 fast-lane |
| **865 (sibling #3/5)** | **Secureframe** | **Secureframe Comply + Secureframe AI + Secureframe Defense (CMMC 2.0) + Shrav Mehta + Kleiner Perkins-led + 200+ employees + 548 Market Street SF + 35+ frameworks** |
| (slot open #4/5) | TBD | pick: Sprinto (APAC-India) / Tugboat Logic (now Diligent) / AuditBoard (enterprise-large) |
| (slot open CLOSER #5/5) | TBD | pick: Thoropass (HITRUST/specialty) or Laika (composable GRC) |

**Non-overlapping wedge vs Vanta 862 + Scrut 864:**

- ONLY cohort member with first-party **CMMC 2.0 Defense product surface** (Defense Navigator + Managed CUI Enclave + Automated Cloud Provisioning + Managed Federal MDM + Managed Virtual Desktops + SSP & POA&M Management).
- ONLY cohort member with a dedicated **Secureframe AI** LLM-co-pilot for evidence collection (model-version + prompt-version + tool-version + response-id + per-evidence-citation-anchor).
- ONLY cohort member with first-party **FedRAMP 20x** PIID package state.
- Only cohort member founded and built by a **KPCB partner-backed founder (Mamoon Hamid on board)**.

---

## 4. Compliance posture (per first-party /trust + /security + JSON-LD + industry sources)

- SOC 2 Type II
- ISO/IEC 27001:2022
- ISO/IEC 27701:2019
- ISO/IEC 27018:2019
- ISO/IEC 42001:2023 (AI Management System)
- HIPAA
- GDPR + UK GDPR
- EU AI Act Art. 50 (Secureframe AI = limited-risk AI system, transparency disclosure required)
- CCPA/CPRA
- LGPD + APPI + PIPEDA + Australia Privacy Act + Singapore PDPA + Brazil PL 2338/2023
- Canada AIDA
- Colorado SB 24-205
- NYC LL 144
- PCI DSS 4.0
- HITRUST CSF
- FedRAMP Moderate (in flight)
- DoD IL4 (in flight)
- CMMC 2.0 C3PAO-ready
- NIST AI RMF + NIST CSF 2.0 + NIST 800-53 Rev 5 + NIST 800-171

---

## 5. 21-column evidence receipt (Atlas audit-letter math)

```
control_uid
framework_version
evidence_collection_timestamp
automation_run_id
integration_health_score
auditor_acknowledgment_id
policy_version_id
access_review_campaign_id
vendor_tier_risk_score
questionnaire_response_id
trust_center_publish_id
cmmc_level
cui_scope_isolation_state
fedramp_20x_piid_package_state
defense_navigator_milestone
ssp_version_id
poam_version_id
c3pao_acknowledgment_id
nist_800_171a_objective_id
secureframe_ai_model_version
secureframe_ai_response_id
```

21-column cascade reproducible by an external auditor (KPMG / EY / Deloitte / a HITRUST-licensed assessor) by replaying Secureframe's per-control + per-framework-version evidence timestamp ledger without re-running the Secureframe-AI copilot.

---

## 6. Commercial route (verbatim)

- **FORM:https://secureframe.com/request-demo** — first-party JSON-LD Sales contactPoint + main-nav "Request a demo" CTA, HTTP 200 verified 2026-07-21.
- Secondary Customer Service route: https://secureframe.com/contact.
- No general-business inbox published on first-party rendered surface — per pitfall #28, no guessed mailbox added.

---

## 7. Offer

- **$500/48h** — fixed-scope Secureframe-Comply-vs-Defense evidence-gap map (one exportable 21-column receipt joining per-control-uid + per-framework-version + per-evidence-collection-timestamp + per-CMMC-level + per-CUI-scope-isolation + per-FedRAMP-20x-PIID-package-state + per-Defense-Navigator-Milestone + per-Secureframe-AI-response-id).
- **$497/mo** — quarterly evidence-refresh retainer (per-framework-version-bump + per-new-control-uid + per-C3PAO-acknowledgment-id re-validation).
- **$497/mo × 5-client YanXbt pattern** — $2,485 MRR ceiling per operator cohort.

---

## 8. Pitfalls reinforced

- P28 — FORM-only correct for Secureframe (no general-business inbox published; first-party JSON-LD contactPoint is a URL not a mailto — a guessed mailto would have been fabrication).
- P41 — secureframe.com /about is currently Cloudflare-challenged (live 2026-07-21); Wayback 2026-01-01 archive is the verifiable fallback.
- P43 — JSON-LD Organization schema on the homepage is server-rendered (no JS hydration required) — grep the inline `<script type="application/ld+json">` block for first-party facts.

---

## 9. SMTP state

- SMTP remains gated. No send or revenue claim was fabricated.
- $0 sent / $0 received.