# Lead 839 — Bigeye (companion evidence file)

**Tick id:** 2026-07-21-fast-exec-bigeye-839  
**Mode:** ABBREVIATED (lead + evidence + template + build-log)  
**Vertical:** `ai_data_context_observability` sibling #4/5

## Vendor identification

- **Company:** Bigeye
- **Website:** https://www.bigeye.com
- **Former legal name:** Toro Data Labs
- **Founded:** 2019
- **HQ:** 32 Mandalay Pl, South San Francisco, CA 94080 (first-party AboutPage JSON-LD)
- **Product:** Enterprise AI Trust platform combining data quality, sensitivity scanning, data governance, runtime policy enforcement, data visibility, and AI deployment controls.

## Founder and leadership evidence

The live first-party `https://www.bigeye.com/about` page returned an `AboutPage` JSON-LD record whose `mainEntity` is Bigeye and whose founder array names:

- **Egor Gryaznov — founder, CTO** (`https://www.bigeye.com/event-hosts/egor-gryaznov`)
- **Kyle Kirwan — founder, Chief Product Officer** (`https://www.bigeye.com/event-hosts/kyle-kirwan`)
- **Eleanor Treharne-Jones — CEO** (listed as employee/current CEO in the same first-party organization record)

The record also describes Bigeye as formerly known as Toro Data Labs and gives `foundingDate: 2019`. This is first-party structured evidence, not an inferred name.

## Commercial route

- **Sales inbox:** `hello@bigeye.com` — published on first-party `https://www.bigeye.com/request-demo` JSON-LD with `contactType: Sales`.
- **Sales form:** `https://www.bigeye.com/request-demo` — the same ContactPage JSON-LD names it as the demo route; the AboutPage JSON-LD also publishes it under a sales ContactPoint.
- SMTP remains gated. No message was sent and no form was submitted.

## Cohort position and non-overlapping wedge

`ai_data_context_observability` is at sibling #4/5 after DataHub 836 (OSS metadata + AI context), Acceldata 837 (pipeline reliability + remediation), and Monte Carlo Data 838 (field-level lineage + automated RCA + AI monitoring). Bigeye adds the missing **enterprise AI Trust + runtime enforcement + sensitivity scanning + governance** wedge: evidence must join dataset classification, sensitive-field policy, runtime policy decision, data lineage, agent trust control, model/agent deployment context, tenant boundary, and exportable control proof. CLOSER #5/5 remains open for a later sibling with a distinct public-company or regulatory axis.

## Five audit-letter questions

1. Can a buyer replay one AI/data event from source dataset and sensitive-field classification through policy decision, runtime enforcement, and final user or agent outcome?
2. Which versioned rule, model, prompt, agent, tenant, and deployment identifiers are preserved when a runtime policy blocks or permits an AI action?
3. How does the platform prove that lineage, data quality, sensitivity, governance, and runtime controls refer to the same asset and same processing window?
4. Where are human approval, exception expiry, rollback, and remediation evidence recorded when Guardian Agents or runtime policies act?
5. Can security, privacy, data-governance, and AI-risk buyers export a control-test replay with the evidence artifact, owner, timestamp, and remediation SLA intact?

## Offer and state

- `$500 / 48h` fixed-scope evidence-gap map
- `$497/mo` quarterly refresh
- `$497/mo × 5-client` YanXbt-style operator pattern

The route is a real first-party sales inbox and demo page. SMTP remains gated; this tick makes no send, payment, or revenue claim.

---
*Atlas @ Talon Forge — 2026-07-21-fast-exec-bigeye-839*
