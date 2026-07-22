# 892 — Applitools — Companion

**Lead:** Applitools (applitools.com) — Anand Sundaram (CEO) + Adam Carmi (CTO & Co-Founder)
**Cohort:** ai_visual_test_automation — OPENER #1/5 (NEW VERTICAL #22)
**Commercial route:** `FORM:https://applitools.com/contact/demo-request-next/` (HTTP 200 verified 2026-07-22; redirect chain `/request-a-demo/` → `/request-demo` → `/contact/demo-request-next/`)

## First-party evidence base

- **Leadership grid** (verbatim first-party `/about/` 2026-07-22): "Anand Sundaram — CEO" + "Adam Carmi — CTO AND CO-FOUNDER" + "Joanna Schloss — CMO" + "Ted Marks — CHIEF FINANCIAL OFFICER" + "Kunal Rao — CHIEF CUSTOMER OFFICER" + "Danit Raanan Ideses — HEAD OF PEOPLE".
- **Board of Directors** (verbatim first-party `/about/` 2026-07-22): David Weiss (Operating Partner Thoma Bravo) + Tom Clark (Operating Partner Thoma Bravo) + Jay Larson (Operating Partner Thoma Bravo) + Sam Yules (Vice President Thoma Bravo) + Carl Press (Partner Thoma Bravo) — five Thoma Bravo operators on a five-person board ⇒ enterprise PE-controlled governance lane.
- **Deterministic AI positioning** (verbatim first-party `/` 2026-07-22): "DETERMINISTIC AI BY DESIGN — Trust the quality of your UI at every stage of the agentic SDLC. Applitools delivers secure and deterministic AI that is purpose-built for testing with quality gates throughout your agentic or AI-augmented dev process." + six-bullet principle list: "Compute, don't approximate. The same input produces the same output. Consistent and stable. No human oversight required. Well defined and bounded. Capabilities and limits are defined. Fast and efficient. No token overhead. Enforceable correctness. Wrong results are bugs, not probabilistic drift."
- **Compliance** (verbatim first-party `/` 2026-07-22): "ISO 27001 and SOC 2 Type II compliant and have current Pen Testing reports" + "Log in using SSO or SAML to help eliminate administrative overhead for large teams."
- **Deployment modes** (verbatim first-party `/` 2026-07-22): "Deploy on-prem — Deploy Applitools on your own infrastructure, inside your firewall for maximum security and clearance" + "Run in your cloud — Run Applitools in a dedicated cloud on Amazon, Azure, or GCP to a flexible, secure solution" + "Run in our cloud — Get up and running in minutes using Applitools as a SaaS solution."
- **Named customers** (verbatim first-party logo wall + customer-stories panel 2026-07-22): Lloyds Bank + NASDAQ + Abbvie + Intuit + Aetna + RBS (homepage logo wall); Eli Lilly + Medtronic + Bayer (Pharmaceuticals tab); Eversana + EVERFI + Frontdoor + Medalia + KPN (customer-stories tab panel).
- **Co-founder** Adam Carmi is verbatim first-party `/about/` (CTO AND CO-FOUNDER). Co-founder #2 (Moshe Milman) is INFERRED from public records; can be confirmed verbatim via Wikipedia snapshot in next tick if needed.

## 16-column per-visual-comparison receipt (per-test-case)

| # | Column | Purpose |
|---|---|---|
| 1 | `tenant_id` | Applitools org/workspace identifier |
| 2 | `test_run_id` | Applitools test execution batch ID |
| 3 | `test_case_id` | Single test in batch |
| 4 | `baseline_snapshot_hash` | SHA-256 of baseline image |
| 5 | `actual_snapshot_hash` | SHA-256 of actual image |
| 6 | `pixel_diff_bounding_box` | x,y,w,h of mismatch region |
| 7 | `visual_ai_suggestion_id` | AI-driven accept/reject hint ID |
| 8 | `suggestion_confidence_score` | 0.000–1.000 |
| 9 | `acceptance_rejection_status` | accepted/rejected/pending |
| 10 | `assertion_failure_root_cause_code` | visual/layout/responsive/font/color |
| 11 | `cross_browser_render_artifact_id` | Chrome/Firefox/Safari/Edge output |
| 12 | `cross_device_viewport_signature` | mobile/tablet/desktop + DPR |
| 13 | `accessibility_axe_run_id` | axe-core scan ID |
| 14 | `self_healing_decision_id` | if healed: new locator + rationale |
| 15 | `tenant_scoping_boundary_id` | per-deployment-mode credential scope |
| 16 | `cross_tenant_no_bleed_proof` | invariant hash |

## Why this is the OPENER

Five siblings planned for `ai_visual_test_automation`:
- **Applitools 892 OPENER** — Visual AI + Eyes + Ultrafast Test Cloud + Self-Healing + Thoma Bravo + Fortune-500 logo wall + on-prem deployment
- 893 sibling #2/5 — to be selected from: **Mabl** (intelligent test automation) / **Testim** (AI locators) / **Functionize** (cloud functional) / **Reflect** (no-code AI)
- 894 sibling #3/5 — to be selected from: **Sauce Labs** (cloud testing platform) / **BrowserStack** (cross-browser) / **LambdaTest** (cross-browser AI)
- 895 sibling #4/5 — to be selected from: **Tricentis** (test management) / **TestRail** (test case mgmt) / **Zephyr** (Jira-native)
- 896 CLOSER #5/5 — to be selected from: **Katalon** (all-in-one) / **Playwright + AI** (Microsoft OSS lane) / **Cypress + AI**

## What we don't claim
- No form submitted, no email sent, no payment received.
- No guessed general-business inbox appended.
- `FORM:https://applitools.com/contact/demo-request-next/` is the only sanctioned commercial route; first-party inbox remains hidden per pitfall #28 (likely Cloudflare email-obfuscation).
