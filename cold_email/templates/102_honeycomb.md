# 102_honeycomb.md — Honeycomb.io (lead 108)

**Vertical:** ai_observability (complementary to Arize — generic o11y vs. LLM-native)
**Tier:** 1 (Fortune-class buyers, EU residency requirements)
**To:** sales@honeycomb.io (founder route: charity@honeycomb.io, liz@honeycomb.io)
**From:** founders@talonforgehq.com
**Pattern:** 5-question audit opener — different from template 101 (Arize) because Honeycomb is the underlying o11y layer that LLM-trace vendors (Arize/Phoenix/Langfuse/Helicone) all export to via OTLP, so the audit question is "what's the evidentiary posture of the layer *below* the LLM-trace layer?"

---

**Subject:** Honeycomb + EU AI Act Article 12 evidence — 5 questions before the Aug 2026 deadline

Hi Honeycomb team,

I've been working with a handful of AI-agent vendors on SOC 2 + EU AI Act evidence maps, and Honeycomb comes up every time as the canonical store-and-query layer — Arize Phoenix, Langfuse, Helicone, and most in-house stacks all export their LLM/tool-call spans to Honeycomb via OTLP. So the audit posture of Honeycomb itself is now in scope for every regulated buyer's QSA cycle.

Five questions I can't answer from public material — all phrased as the SOC 2 / EU AI Act auditor would phrase them:

1. **Immutable WORM export.** When a regulated buyer (HIPAA, FedRAMP Moderate, EU AI Act high-risk) needs to produce trace data for a 7-year audit retention window, can Honeycomb export spans to an immutable / WORM-compatible sink (S3 Object Lock, GCS Bucket Lock, Azure Blob Immutable Blob) with cryptographic hash-chaining? I see S3/GCS/Azure exports in the docs but don't see the immutability layer documented.

2. **Multi-region EU-only residency.** For EU AI Act Article 12 + GDPR data-residency buyers, can a Honeycomb dataset be pinned to a single region (eu-west-1, eu-central-1) with documented no-replication-outside-region guarantees? Customer-configured multi-region replication is great for HA but is the wrong default for EU residency.

3. **Span-level PII redaction at ingest.** If an LLM-trace span contains a PII payload (an end-user email address, phone, SSN-equivalent) before the redaction layer runs, does Honeycomb's ingest pipeline offer a redaction hook (envoy filter, OTel processor) — or does the caller have to redact before sending? The latter is the industry default but the former is what EU regulators are starting to expect under AI Act Annex III §2.

4. **Trace-to-billing join-table.** For a SOC 2 CC7.2 / CC8.1 audit, can a Honeycomb tenant reconstruct "every LLM tool-call span joined to the Stripe charge that funded it, joined to the end-user session that triggered it"? This is the join-table every auditor asks for and most Honeycomb tenants hand-build it.

5. **Honeycomb-on-Honeycomb self-audit posture.** If Honeycomb itself went through a SOC 2 Type II audit tomorrow, can the auditor verify "every customer-facing tool-call Honeycomb made was logged with the same evidence guarantees we promise customers"? This is the Arize-on-Arize / Vanta-on-Vanta pattern — auditors are starting to ask it of every observability vendor.

Happy to scope this as a $500 / 48h audit deliverable: a SOC 2 + EU AI Act evidence map for Honeycomb's existing export / residency / ingest layer, with the 5 questions above mapped 1:1 to Common Criteria CC7.2 / CC8.1 + EU AI Act Articles 12/13/14, and a working sample query for the trace-to-billing join-table. Or a 30-min call if you'd rather walk through it first.

— Atlas

P.S. — If the right person is Charity (CTO) or Liz (principal engineer), happy to route direct. The audit questions above are the same shape we just sent Arize (template 101) — different vendor, same evidentiary gaps.

---

**Word count:** ~430 (3-line cold-email pattern preserved: context + 5 questions + close + P.S.)
**Pattern cross-references:** 101_arize (LLM-native observability), 98_sierra / 99_cognigy / 100_cresta (CX-AI vendors whose auditors inspect Honeycomb), chunk_37 (Arize audit chunk — same evidentiary framework), chunk_36 (SOC 2 evidence for AI tool calls).