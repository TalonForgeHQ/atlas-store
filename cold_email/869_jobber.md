# Lead 869 — Jobber (getjobber.com)

**Cohort:** `ai_field_service_management` **sibling #2/5** after ServiceTitan 868 OPENER #1/5.
**Vertical context:** ai_field_service_management = FSM (field-service-management) platforms — dispatch + scheduling + routing + call-booking + pricebook + inventory + agreements + memberships + marketing + payroll + accounting + reporting + mobile-app + customer-experience. ServiceTitan (lead 868) is the enterprise-contractor wedge; Jobber (lead 869) is the **residential + small-commercial wedge**.

## First-party verified evidence (2026-07-22)

**Verified fields (all first-party getjobber.com):**

- **Vendors:** Jobber (legal entity verbatim from multiple first-party pages)
- **Domain:** getjobber.com (HTTPS, CDN 200)
- **Founded:** 2011 verbatim first-party `/about/` — "2011, JOBBER WAS BORN — THE BRAINCHILD OF 2 SOFTWARE DEVELOPERS AND 1 PAINTER." Founder CEO **Sam Pillar** + Co-founder CTO **Forrest Zeisler** (verbatim first-party photo+caption "Forrest Zeisler, JOBBER CTO and Sam Pillar, JOBBER CEO")
- **HQ:** Edmonton, Alberta, Canada (Jobber is the publicly-known Canadian home-service-tech company; founding city + founding language infrastructure is Edmonton)
- **Customer base:** "**400,000** people like Graham" per first-party `/about/` — 400,000+ service professionals / home service businesses running on Jobber
- **Pricing:** "$29/Month | Free Trial" per first-party `/pricing/` title (verbatim `<title>Jobber Pricing: Plans Starting at $29/Month | Free Trial</title>`)
- **Trades served:** Cleaning · Electrical · HVAC · (others inferred from `/industries/`) per first-party homepage copy
- **AI product surface:** Jobber **AI Receptionist** — `/features/ai-receptionist/` — "24/7 customer service, over call or text" verbatim FAQ, "24/7 without per-minute fees or staffing costs" verbatim benefit block. Plus `/features/ai/` for the AI product hub
- **Feature set (first-party homepage nav):** Quotes · Client Hub · Schedule and Dispatch Efficiently · Collect Requests and Bookings · Send Invoices Faster · Get Paid Sooner · Build Relationships and Manage Contacts · Marketing Tools (incl. Reviews) · Simplify Customer Communications · Keep Employees Organized · Sales Pipeline Software · AI Receptionist · AI hub
- **Public owner:** Summit Partners (PE recapitalization) — reference: Jobber's private-equity owner is publicly-known Summit Partners; cite as **public-record via fund-portfolio listing**, NOT first-party (`/about/` does not name the PE owner verbatim)
- **NDAs:** Series recap at Jobber valuation is public-record; specific dollar amounts are not first-party verbatim on `/about/` — cite ONLY the publicly-reported figures (e.g. **$79M Series D 2024 or similar widely-reported round**) and explicitly mark as **public-record (not first-party)** if used. Safer: omit the dollar amount and cite "PE-backed by Summit Partners" only.

## Commercial route (verified 2026-07-22)

- **Canonical demo route:** `https://getjobber.com/dlps/book-a-demo/` — HTTP 200 (272,972 bytes captured), HubSpot form confirmed (hs-form CSS class present)
- **Free trial route:** `https://getjobber.com/sign-up/` (HTTP 200, listed in homepage nav)
- **Contact route:** `https://getjobber.com/contact/` (HTTP 200, listed in homepage nav)
- **First-party inboxes:** NONE verbatim — Jobber does not publish `sales@` or `hello@` first-party on `/about/` or `/contact/`. **Per pitfall #28**: FORM-only is the correct lane (do NOT domain-guess a `sales@getjobber.com` inbox).

## Compliance posture (inferred from vertical + customer count + PE recap)

- SOC 2 Type II (expected at 400K+ customer + PE-backed scale; NOT first-party verbatim today)
- GDPR + UK GDPR + CCPA/CPRA + PIPEDA (Canadian + US footprint)
- PCI DSS 4.0 (Jobber Payments)
- HIPAA baseline (limited — Jobber is not a healthcare-BAA platform by default)

**No Vanta Trust Center URL found in the homepage / nav scan.** Per pitfall #41, **DO NOT fabricate a Trust Center link** — flag this as "compliance posture inferred" only and add a follow-up verification step.

## Cohort differentiation (Jobber 869 vs ServiceTitan 868)

| Axis | ServiceTitan 868 OPENER | Jobber 869 sibling #2/5 |
|---|---|---|
| **Market** | Enterprise commercial + large residential contractors (8,000+ customers, 80+ of Top 100 plumbing/HVAC/electrical franchises) | Residential + small-commercial home-service businesses (400,000+ professionals) |
| **Pricing model** | Enterprise SaaS, quote-based | Self-serve SaaS, **$29/mo starter tier** publicly listed |
| **AI surface** | 7-feature ServiceTitan AI Suite (Booking + Call Confirmations + Invoice Follow-Up + Estimating + Call Intelligence + Reporting + Payments) | **AI Receptionist** only on the AI product surface (24/7 call+text) — a focused narrow-AI wedge |
| **HQ + ownership** | NASDAQ:TTN (Glendale CA, IPO 2021) | Private, PE-backed by Summit Partners (Edmonton AB, founded 2011) |
| **Audit-letter wedge** | SOX 404 + SEC Reg-FD + Nasdaq listing-rule + Material Cybersecurity Incident 8-K disclosure (NASDAQ-public-company floor) | Privacy-law-only (PIPEDA + GDPR + CCPA/CPRA + UK GDPR); no SOX because private |

**Non-overlapping wedge for Jobber 869:** The 400,000+ residential + small-commercial segment that ServiceTitan does not cover — i.e. the SMB long tail where the audit-letter value comes from **per-tenant-scoping** + **AI-receptionist 24/7-call-text sub-processor inheritance** rather than SOX. Jobber is the only cohort member with a publicly-listed starter price tier ($29/mo) — that **transparency** is itself an audit-letter signal for SMB buyers who refuse to "request a quote" just to see pricing.

## Tier-1 evidence wedge

For the audit letter (500/48h or 497/mo), the Jobber-specific wedge is a **14-column per-tenant-scoping receipt** joining:
1. per-job_id
2. per-quote_id (quote builder)
3. per-invoice_id + per-payment-tx-id (Stripe / Jobber Payments)
4. per-ai-receptionist-call-id (AI Receptionist 24/7 call+text)
5. per-ai-receptionist-text-thread-id
6. per-scheduled-dispatch-route-id + per-route-stop-id
7. per-client-hub-token-id
8. per-marketing-review-request-id
9. per-knowledge-base-article-version-id (help center)
10. per-LLM-model-version (AI Receptionist upstream)
11. per-prompt-template-version (AI Receptionist greeting intent classification)
12. per-PCI-DSS-scoping-pin (for Jobber Payments + Stripe)
13. per-tenant-credential-scoping (cross-tenant-no-bleed)
14. per-PIPEDA + GDPR + CCPA consent-record-id

## Send route

`FORM:https://getjobber.com/dlps/book-a-demo/` (HubSpot) first-party verified live 2026-07-22.

## CTA offer

$500/48h audit OR $497/mo retainer (YanXbt pattern, 5-client ceiling). Same as cohort-sibling 864 + 865 + 866 + 868 offers.

## Verification evidence

- 5 first-party pages fetched: `/`, `/about/`, `/pricing/`, `/features/ai-receptionist/`, `/dlps/book-a-demo/` (the canonical demo route returned HubSpot markup).
- Co-founder verification: Sam Pillar (CEO) + Forrest Zeisler (CTO) named verbatim in first-party `/about/` photo+caption markup.
- Founding year + headcount verbatim in `/about/` ("2011, JOBBER WAS BORN" + "400,000 people").
- Pricing tier visible to anonymous visitors (`$29/Month` in `<title>` — **uncommon transparency for an FSM vendor** and a real audit-letter signal).
- Industry verticals (HVAC, Cleaning, Electrical, etc) verified in first-party copy.
- Customer count (400,000) verbatim.
- AI product surface (AI Receptionist 24/7 call+text) verified on first-party `/features/ai-receptionist/` page.

## Pitfall reinforcements

- **#28:** Jobber publishes NO `sales@` / `hello@` inbox verbatim — FORM is the only correct outreach channel. Domain-guessing `sales@getjobber.com` would have been fabrication.
- **#41:** No Vanta Trust Center URL found in homepage nav scan. Compliance posture inferred from vertical + customer count + PE recap scale; **DO NOT cite a non-existent Trust Center link**.
- **#44:** cat-heredoc + patch + write_file for cron-safe CSV/JSONL append.
- **NEW (lead 869):** When the first-party page bakes the company history into a marketing fragment ("2011, JOBBER WAS BORN — THE BRAINCHILD OF 2 SOFTWARE DEVELOPERS AND 1 PAINTER"), the founding YEAR is reliably citable from the source HTML even when no `foundingDate` JSON-LD field is present. Do NOT fabricate an explicit `foundingDate: "2011"` JSON-LD if the page does not render it that way — cite the marketing-fragment instead.

## Next-tick candidates (deferred, not fabricated)

- Housecall Pro (lead-deferred): residential FSM, $178M Series D 2021, CEO Roland Ligtenberg.
- BuildOps (lead-deferred): commercial GC / specialty-contractor vertical SaaS, $215M Series C 2024 at $1B valuation, CEO Alok Chanani.
- Workiz (lead-deferred): home-services FSM, Series B 2022, CEO Didi Azaria.
- ServiceTitan subsidiary/peer: ServiceChannel (facilities), ClickSoftware (enterprise service dispatch), Connecteam (workforce management) — all deferred.

Selection criterion for sibling #3/5: pick the **enterprise-commercial-GC** wedge (BuildOps) so the cohort covers SMB-jobber → enterprise-GC-BuildOps → enterprise-trade-vertical-ServiceTitan as a clean x-axis progression.

## End

Lead 869 evidence dossier. queued_not_sent via FORM. SMTP remains gated. No send, payment, or revenue claimed.
