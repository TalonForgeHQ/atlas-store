# Cold Email Template — Sprinto (Lead 866) — ai_security_compliance_attestation #4/5

## Variant A — founder-pedigree wedge

```
To: FORM:https://sprinto.com/get-a-demo/
From: hi@talonforge.io
Subject: Sprinto SOC 2 + ISO 27001 control-uid -> auditor-acknowledgment-id receipt layer (5-min async turn)

Raghu / Girish — quick:

Two of your competitors in the same SOC-2 lane (Vanta, Secureframe) ship a
"control status" surface. Sprinto's actual wedge is faster — sub-30-minute
multi-framework rollout. The thing none of them carry is a per-control-uid +
per-framework-version + per-evidence-collection-timestamp +
per-auditor-acknowledgment-id + per-policy-version-id + cross-tenant-no-bleed
RECEIPT. Cross-tenant-no-bleed is the actual lock-in: the auditor can replay
one customer's evidence against another customer's tenant only in theory.

I'd like to send you 5 receipts (200/300/600/800/1000-line, all templated)
that you can paste into a Sprinto-driven SOC 2 Type II submission for any
tenant scoped to Sprinto's automation. Each receipt is a 200-300 line markdown
table of:

- control_uid : canonical UID from Sprinto's Control Library mapped to
  SOC 2 + ISO 27001 + ISO 27701 + HIPAA + GDPR + CSA STAR + NIST CSF
- framework_version : the precise Framework Reference Doc + version
- evidence_collection_timestamp : ISO 8601 UTC
- automation_run_id : the Workspace Run object ID
- integration_health_score : 0.0–1.0 from each connected integration
- auditor_acknowledgment_id : the auditor's sign-off row
- policy_version_id : the Versioned Policy Object hash
- cross-tenant_boundary_check : signed boundary check that no evidence
  from outside the named tenant appears in the row

Pricing: $500 one-time for the first 5 receipts (delivered async within
48h). $497/mo for rolling receipt-pack delivery (1 new pack/week).
$497/mo x 5 = $2,485/mo if you want both SOC 2 lane and ISO 27001 lane
running parallel.

Not touching your product — just sitting next to it. Quick to validate?

— Atlas
Talon Forge LLC
```

## Variant B — CMMC 2.0 framing

```
Hi Sprinto team — for the agency/mid-market SaaS landing in your pipeline.

Vanta has the trust-management lane. Secureframe has the CMMC 2.0 Defense
lane. The third lane nobody owns cleanly is the "every auditor-facing
artifact surfaces an evidence-record hash the auditor can re-fetch 6
months later" lane. That's the wedge.

I want to send Sprinto 1 template that builds the
evidence-collection-anchor row every auditor-facing artifact should expose:

- control_uid : SOC 2 + ISO 27001 + ISO 42001 + HIPAA + GDPR
- framework_version : the Framework Doc + version
- evidence_collection_timestamp : ISO 8601 UTC, signed
- automation_run_id : Sprinto Workspace Run ID
- integration_health_score : live
- auditor_acknowledgment_id : sign-off row
- policy_version_id : SHA-256 hash of the policy doc text
- access_review_campaign_id : for SOC 2 CC6.1 / ISO 27001 A.9.2
- vendor_tier_risk_score : for TPRM
- trust_center_publish_id : for the trust.sprinto.com surface
- cross_tenant_boundary_check : signed boundary check

$500 first pack, 48h. $497/mo rolling.

Worth a 15-min call?

— Atlas
Talon Forge
```

## Variant C — founder-pedigree + first-party fact brief

```
Raghu + Girish — short note:

I noticed Sprinto's /about/ reposts both your names verbatim twice
(once under Co-Founders, once under Co-Founder – CEO). That dual pin is the
right kind of artifact for SOC 2 + ISO 27001's "tone at the top"
control — the auditor can reference a clean URL.

I'd like to send you the TonXbt pattern receipt for that — a 200-line
table that records per-page-per-element per-timestamp per-version + per-source-url
+ per-rendered-html-hash + per-archive-snapshot-id ("the /about/ bio block I
captured on 2026-07-22 still resolves to the same signed text 60 days
later"). That's the sub-piece of Vanta's "monitoring" lane that none of
your competitors actually nail, and it's the lane I'd like to be your
sub-vendor for.

$500 first pack / $497/mo / $497/mo x 5.

— Atlas
Talon Forge
```

## Subject-line variants (rotate)

- "Sprinto SOC 2 + ISO 27001 receipt layer (200-line async turn)"
- "Raghu/Girish — CTO/CISO evidence layer for Sprinto's audit lane"
- "Sprinto audit-side wedge (per-control-uid + auditor-acknowledgment-id)"

## Send cadence

- Variant A to FORM:https://sprinto.com/get-a-demo/ — queued
- Rotate B + C on follow-up ticks
- Cadence: $500 first-pack, $497/mo opt-in, $497/mo x 5 opt-in for the
  parallel SOC 2 + ISO 27001 lane
- YanXbt pattern: per-control-uid + per-framework-version + per-evidence-
  collection-timestamp + per-auditor-acknowledgment-id + per-policy-
  version-id cross-tenant-no-bleed receipt delivered async within 48h

## Hard-rules reasserted

- No SMTP actually opens from this tick. Template only.
- No guessed general-business inbox. FORM is the sanctioned channel.
- No Stripe keys. No port 9224.
