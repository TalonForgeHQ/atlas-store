Subject: When the auditor asks "who logs your LLM calls?" — the Arize-on-Arize audit gap

Hi Jason / Aparna,

Congrats on the Series C. I've been digging into how the AI observability
layer shows up in SOC 2 audits for agent-platform customers, and there's
a specific audit angle that maps to Arize in a way it doesn't map to
Datadog or Honeycomb — the "who watches the watchmen" problem.

The 5 questions that come up at customer SOC 2 audits when Arize is the
observability layer (not generic observability questions):

1. **Immutable export of traces to a WORM bucket.** Arize Phoenix OSS
   stores spans in Postgres + S3 by default, both mutable. When the
   buyer's regulated customer (a HIPAA-covered entity, a FedRAMP-Moderate
   agency, or an EU AI Act high-risk deployer) asks for tamper-evident
   evidence of the LLM call graph from March 15, your answer needs to be
   "yes, exported to S3 Object Lock in Compliance mode + replicated to
   Glacier with a 7-year retention class" — not "we have S3 backups."
   SOC 2 CC7.2 + EU AI Act Article 12 (logging) both require evidence
   integrity, not just evidence existence.

2. **Prompt-version pinning + lineage to evaluation.** When a model
   behaves differently on April 1 than March 1, the auditor wants
   the SHA of the prompt template + the model version + the
   evaluation-set commit SHA + which customer traffic was processed
   with which combination. Phoenix's `evals` API has the lineage, but
   the export to a SOC 2 evidence format (CSV+JSON to WORM) is a
   customer-side script, not a one-click Arize feature.

3. **Cross-tenant trace isolation evidence.** Arize's multi-tenancy is
   logical (row-level security), not physical (separate Postgres +
   separate S3 prefix per tenant). For EU AI Act Annex III high-risk
   systems + GDPR Schrems II cross-border transfers, some buyers need
   per-tenant EU-only residency — i.e. Arize EU on Arize EU storage,
   not Arize US with EU-data-at-rest encryption. The auditor will ask
   for the network path diagram + the encryption-at-rest certificate +
   the key-custody chain.

4. **Drift-detection evidence at the audit boundary.** Arize's drift
   detection is world-class for the customer, but the audit requires
   "what did you do when drift was detected?" — i.e. the action
   join-table that links "drift alert fired at T" to "model was rolled
   back at T+2h" to "which customers were affected between T and T+2h."
   This is the same tool-call join-table question we surface for
   customer-service-AI vendors, but it lands harder at Arize because
   Arize is the source of truth.

5. **The "Arize on Arize" question — does Arize audit itself with the
   same rigor?** When a Fortune-500 buyer's CISO asks "what's your
   evidence that YOUR observability platform doesn't itself have an
   SOC 2 gap?" the answer needs to be a public SOC 2 Type II report
   + a public EU AI Act conformity assessment summary + a public
   penetration-test summary. The current arize.com/security page has
   the SOC 2 logo but not the underlying report, and that's the gap
   most CISOs I've talked to flag.

The 30-minute meeting ask: walk through which of these 5 gaps is
already on Arize's 2026 roadmap (Q3-Q4 2026) vs. which is a
net-new commitment. If 3 of 5 are roadmap-confirmed, the rest is a
48-hour audit scoping exercise on our side — $500 flat, full deliverable
is a 25-page SOC 2 + EU AI Act evidence map for Arize Phoenix OSS +
Arize Enterprise.

P.S. We work with 4 of the 6 other observability-adjacent vendors in
the pipeline (the customer-service-AI leads 104-106 use Arize as a
trace source, which is why this question keeps coming up). The pattern
that's working at those customers is a sidecar-export from Arize to a
WORM bucket + a SHA-pinned eval-set export, both of which can be
wrapped into a 25-page deliverable.

Best,
Atlas (Talon Forge LLC)
talonforge.ai / @TalonForgeHQ