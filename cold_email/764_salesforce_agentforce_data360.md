# Lead 764 — Salesforce Agentforce + Data 360 evidence brief

**Company:** Salesforce, Inc.  
**Website:** https://www.salesforce.com/  
**Founder verified:** Marc Benioff — Chair, CEO & Co-Founder  
**Commercial route:** `FORM:https://www.salesforce.com/data/contact/data-360/`  
**Vertical:** `ai_data_intelligence_agents` sibling #4/5

## First-party verification — 2026-07-21

1. `https://www.salesforce.com/agentforce/` returned HTTP 200 and resolved to Salesforce's regional Agentforce page. Its metadata describes Agentforce as the AI agent platform for building and customising autonomous AI agents with Salesforce ecosystem integration.
2. The Agentforce page explains that agents use trusted CRM and external Data 360 context, operate within set guardrails, escalate complex work to humans, use Agent Builder, invoke Flow automation, connect through MuleSoft APIs, and execute Apex or JavaScript business logic.
3. The same page identifies the Atlas Reasoning Engine as the component that decomposes a prompt into tasks, evaluates each step, and proposes a plan through completion.
4. `https://www.salesforce.com/data/` returned HTTP 200 with the title `Data 360 (Formerly Data Cloud) | Salesforce`; first-party content joins Data 360 to Agentforce and describes structured and unstructured data plus zero-copy connectivity.
5. `https://www.salesforce.com/company/leadership/bios/bio-benioff/` returned HTTP 200 and resolved to `https://www.salesforce.com/company/marc-benioff-bio/`; the canonical first-party bio identifies Marc Benioff as `Chair, CEO & Co-Founder` and states that Benioff founded Salesforce in 1999.
6. `https://www.salesforce.com/data/free-trial/contact-data-360/` returned HTTP 200 and resolved to `https://www.salesforce.com/data/contact/data-360/`. The resulting first-party page title is `Ready to learn more about Data 360? | Salesforce`, exposes a Contact Sales path, and contains first name, last name, company, and business-contact form fields.

## Buyer-facing evidence wedge

Salesforce adds the CRM-native data-to-action control plane to the cohort:

`user/session + profile/permission set -> Data 360 source/data space/zero-copy connection -> identity resolution/harmonized profile -> Agentforce agent/subagent/topic/instruction/action version -> Atlas reasoning plan -> Flow/Apex/MuleSoft action -> guardrail/policy decision -> CRM or external-system mutation -> human escalation/evaluation -> export/deletion receipt`

That wedge is non-overlapping with Databricks 761's lakehouse and Unity Catalog, Snowflake 762's warehouse-native Cortex Threads/Runs, and Palantir 763's ontology/branch/merge control plane. Salesforce owns the CRM-native seam where harmonized customer data becomes an autonomous action across sales, service, marketing, commerce, Flow, Apex, and MuleSoft.

## Route-safety decision

Use only `FORM:https://www.salesforce.com/data/contact/data-360/`. No general-business inbox was verified, so no address is guessed. Privacy, legal, security, abuse, support, press, careers, and investor routes are excluded. This cron tick stages collateral only: no form submission, email, delivery, meeting, payment, or revenue is claimed.

## Offer

- $500 fixed-scope, 48-hour evidence-gap map
- Optional $497/month quarterly refresh
- Scope: five joins across Data 360 context, Agentforce reasoning/action lineage, authorization and guardrails, human oversight/evaluation, and export/deletion evidence
