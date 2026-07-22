# 926_honeycomb.md — Honeycomb (honeycomb.io)

## Subject options
- Honeycomb AI-trace + AI-feature audit-trail review
- A practical evidence map for Honeycomb OpenTelemetry + Honeycomb Intelligence + AI Policies
- Honeycomb: per-trace + per-AI-feature receipts across production observability

## Body

Hi there —

Honeycomb is the SaaS observability platform built around the concept that engineering teams deserve to see inside their production systems with high-cardinality, event-based observability rather than pre-aggregated metrics. Co-founded in 2016 by Christine Yen (CEO) and Charity Majors (CTO) (Wikipedia infobox + Honeycomb /about first-party 2026-07-22), headquartered in San Francisco, California, with a Series D funding history that totals $150M to-date (Wikipedia + TechCrunch corroboration 2023), Honeycomb is the canonical "wide-events / structured-tracing" reference architecture for engineering-led organizations.

We built a compact procurement review that maps five evidence gaps teams commonly need before scaling a Honeycomb + Honeycomb Intelligence + AI Policies fleet that touches OpenTelemetry ingest, the honeycomb.io query engine, query-API export, and the long tail of internal SIEM / data-warehouse destinations:

1. per-trace + per-AI-feature consent and retention evidence per Honeycomb span, AI-driven query suggestion, and Honeycomb Intelligence answer (OpenTelemetry + Honeycomb query-API + SIEM/warehouse destinations);
2. per-AI-feature provenance — which OpenTelemetry dataset, which query, which Honeycomb Intelligence prompt produced each AI-derived chart, alert, or trace summary, with the audit-trail row that authorized it;
3. join-tables between Honeycomb traces and the underlying service, deploy, or CI/CD record they touched, so a reviewer can replay a single high-cardinality query end-to-end;
4. role-based access and tenant isolation for cached Honeycomb trace data, AI-derived charts, and AI Policies audit-log export; and
5. reproducible review receipts for Honeycomb Intelligence runs and the per-customer AI Policies configuration that authorized each one.

Honeycomb ships the controls worth checking: GDPR + CCPA + CPRA + Colorado Privacy Act + Connecticut privacy law coverage verbatim first-party /privacy 2026-07-22 ("the California Consumer Privacy Act or \"CCPA,\" as well as the California Privacy Rights Act or \"CPRA\", Colorado consumers under the Colorado Privacy Act or \"CPA\", Connecticut consumers under..."), an enterprise observability surface built around OpenTelemetry (CNCF incubating project) and Trace + Span + Event semantics, NAMED first-party Honeycomb Intelligence + AI Policies surfaces verbatim first-party docs/security-compliance/compliance-and-data-privacy 2026-07-22, and a HubSpot form on the /get-a-demo page with portalId 5193039 + formId 4c457d32-e710-41df-9cf6-e9553f3331f8 + region na1 verbatim first-party /get-a-demo 2026-07-22. The gap we usually surface is the *audit replay* lane — proving which OpenTelemetry trace + which Honeycomb Intelligence query produced a given AI-derived chart or alert, and what AI Policies configuration authorized it, across a full quarter of mixed production + AI-feature activity.

Would a one-page version of that review be useful for the person who owns observability governance or platform security at Honeycomb?

Best,
Atlas
Talon Forge
