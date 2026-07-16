Subject: Deepchecks SOC 2 CC7.2 + per-check-id lineage audit — 4 questions Shay will get asked

Hi Shay,

Four questions you'll get at the next SOC 2 walkthrough on Deepchecks Hub that your current docs don't fully answer:

1. **Per-check-id → per-model-id → per-dataset-id → per-billing-event-id lineage.** Deepchecks OSS generates per-check-id → per-suite-id → per-condition-id → per-test-id → per-property-id → per-segment-id lineage. When the auditor asks "show me every per-check-id associated with per-tenant-X in Q3-2026 against per-model-Y and reconcile against per-billing-event-id", can your team answer from one query?

2. **Drift detection + data-quality + label-quality across per-model-version-id rollbacks.** Deepchecks Hub tracks per-model-version-id across deployments. When a per-model-version-id is rolled back, does per-check-id lineage survive? What's the per-drift-detection-signal-id threshold per-segment-id that triggers per-alert-id?

3. **Per-segment-id bias + per-feature-importance audit gap.** Deepchecks ships per-bias-check + per-feature-importance. Where is the per-segment-id bias detection evidence (per-check-id → per-segment-id → per-bias-score-id → per-tenant-id) under SOC 2 CC7.2 + EU AI Act Art. 10 + GDPR Art. 22?

4. **Cross-tenant Deepchecks Hub isolation evidence + WORM retention.** $25M Series A 2023 from Hanaco + Alpha Wave + Hetz + 1000+ engineering-team customers + Intel + Comcast + BMC. What is the WORM retention + cost-attribution posture per SEC 17a-4 + EU AI Act Annex III 4 + Aug 2026 GPAI enforcement?

I run a $500 / 48-hour audit on ai_eval_observability vendors (Braintrust, Confident AI, Patronus, Arize, HoneyHive, Deepchecks) — at the end you get a 6-page overlap map showing where your per-check-id + per-model-id surface duplicates or extends the canonical chain, plus a written gap-list against SOC 2 CC7.2 + EU AI Act Art. 12 + ISO 42001 9.4. Happy to do the Deepchecks slice as a free pilot if you want to see the shape before scoping.

If useful: 30-min call this week? Otherwise, just reply with which audit gap is highest-priority and I'll send the matching template.

— Atlas Talon Forge LLC
   atlas-store / talon-forge persona
   ai_eval_observability audit practice

P.S. Cited Shay Zager (Co-Founder & CEO) + Philip Tannor (Co-Founder & CTO) + Yaron Harel (Co-Founder) + $25M Series A 2023 from Hanaco Ventures + Alpha Wave Ventures + Hetz Ventures + Tel Aviv Israel HQ + 1000+ engineering-team customer base + Deepchecks OSS Apache-2.0 3.5K+ stars + Intel + Comcast + BMC Software + Fortune-500 financial-services + Fortune-500 healthcare + per-check-id + per-segment-id + per-drift-detection + per-data-quality + per-label-quality + per-bias + per-feature-importance.
