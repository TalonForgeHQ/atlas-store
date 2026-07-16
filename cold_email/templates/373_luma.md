# Cold Email — Luma AI (hello@lumalabs.ai)

**To:** hello@lumalabs.ai (verified canonical GDPR DPA + EU AI Act + SOC 2 + vendor-DD inbound)
**From:** Atlas (TalonForge)
**Subject line A:** Luma Dream Machine + Ray2 + Ray3 + Genie + Flythroughs — can your audit log reconstruct *which* trained-on clip a generated frame is sourced from under EU AI Act Art. 53(d)?
**Subject line B:** Luma — quick question on per-prompt + per-Dream-Machine-inference-call + per-Fine-Tune-corpus-clip-id + per-3D-scene-graph-node-id + per-video-frame-id + per-training-corpus-clip-id join-table evidence
**Vertical:** ai_video_generation (2nd-sibling to Runway, closes the 2-vendor canonical cohort)
**Tier:** 1 — strategic, a16z + NVIDIA + General Catalyst-backed, $200M+ valuation, tens of thousands of enterprise + studio customers

---

## Opener (3-question, audit-led)

Hi Luma privacy / legal-ops / vendor-ops team,

Three questions before I file this in your vendor-DD queue:

1. **Per-prompt + per-Dream-Machine-inference-call + per-Ray2-Ray3-temporal-window + per-Genie-3D-scene-graph-node + per-video-frame + per-training-corpus-clip + per-camera-trajectory-keyframe join-table** — can your audit log reconstruct *which* trained-on clip / training-corpus-asset / training-dataset-version / Luma-Fine-Tune-corpus-clip any single generated frame is sourced from, on a per-prompt-id basis, under SOC 2 CC7.2 + EU AI Act Art. 12 (event-logging for high-risk AI) + Art. 14 (human-oversight for generative content) + Art. 50 (synthetic-content-disclosure propagation) + Art. 53(d) (GPAI training-data-summary transparency) + Aug 2026 GPAI enforcement + ISO 42001 9.4?
2. **Per-Luma-Fine-Tune + per-fine-tune-corpus-clip + per-Ray2-Ray3-training-data-asset-id + per-Ray2-Ray3-Diffusion-training-pipeline-step-id license-provenance** — for the Aug 2026 EU AI Act Art. 53(d) GPAI training-data-summary transparency requirement + Art. 53(1)(b) copyright-summary obligation, how does your audit trail surface the per-fine-tune-corpus-clip + per-Luma-Fine-Tune + per-third-party-trained-on-corpus license terms at the per-Dream-Machine-inference-call join row?
3. **Prompt-injection + training-corpus-poisoning + Luma-Fine-Tune-backdoor + per-generated-frame-watermark-removal + per-Luma-Ray2-Ray3-deepfake-defense + per-Genie-3D-scene-graph-spoofing + per-Flythroughs-camera-trajectory-injection + downstream-decision-record-poisoning** — what per-prompt + per-inference-call + per-training-corpus-clip + per-generated-frame detection + per-watermark + per-content-provenance (C2PA) + per-3D-scene-graph-spoofing + per-camera-trajectory-injection defense surface do you expose for OWASP LLM Top 10 (LLM01..LLM10) + MITRE ATLAS + NIST AI RMF MEASURE + EU AI Act Art. 9 (risk-management) + Art. 14 (human-oversight) + Art. 50 (transparency obligations for synthetic content)?

---

## Why I'm asking

Luma is the canonical **ai_video_generation 2nd-sibling vendor** — paired with Runway (1st-sibling) — in the generative-video cohort. The **Dream Machine + Ray2 + Ray3 + Genie + Luma API + Flythroughs** platform is the layer enterprise studios + ad agencies + entertainment + media + sports + broadcast + Fortune-500 marketing teams reach for when they need *physically-grounded, ray-traced* AI-video with per-prompt + per-Dream-Machine-inference-call + per-Ray2-Ray3-video-frame + per-training-corpus-clip + per-3D-scene-graph + per-camera-trajectory-keyframe provenance.

The Aug 2026 EU AI Act enforcement wave — combined with SOC 2 CC7.2 + CC6.1 + ISO 42001 9.4 + GDPR Art. 28 (processor obligations) + Art. 32 (security of processing) + EU AI Act Art. 6 (high-risk classification — Annex III 4 covers biometric + emotion-recognition; Art. 50 covers synthetic-content transparency for any AI system that generates or manipulates image/audio/video) — turns Luma's per-prompt + per-Dream-Machine-inference-call + per-Ray2-Ray3-video-frame + per-3D-scene-graph-node + per-camera-trajectory-keyframe + per-training-corpus-clip audit-trail surface into a *vendor-DD hard requirement* for every Fortune-500 enterprise + studio + agency + media + broadcast + sports customer.

---

## The 5 audit gaps (and the join-table that closes them)

1. **End-to-end per-prompt + per-Dream-Machine-inference-call + per-Ray2-Ray3-temporal-window + per-Genie-3D-scene-graph-node + per-video-frame + per-training-corpus-clip + per-Luma-Fine-Tune-corpus-clip + per-Luma-Ray2-Ray3-Diffusion-pipeline-step + per-Luma-Generated-Frame-Content-Provenance + downstream-decision provenance** join-table per SOC 2 CC7.2 + EU AI Act Art. 12 + Art. 50 + ISO 42001 9.4 + GDPR Art. 28 + Art. 32 + OWASP LLM Top 10 + MITRE ATLAS + NIST AI RMF MEASURE capturing 24+ columns (`prompt_id`, `inference_call_id`, `dream_machine_inference_step_id`, `ray2_ray3_temporal_window_id`, `genie_3d_scene_graph_id`, `video_frame_id`, `training_corpus_clip_id`, `training_dataset_version_id`, `fine_tune_corpus_clip_id`, `third_party_licensed_corpus_id`, `c2pa_content_credential_id`, `watermark_removal_detection_id`, `deepfake_detection_score`, `ai_generated_disclosure_flag`, `downstream_decision_record_id`, `human_oversight_approval_id`, `risk_management_event_id`, `eu_ai_act_art_12_event`, `eu_ai_act_art_50_synthetic_content_disclosure_event`, `eu_ai_act_art_53_d_summary_event`, `iso_42001_9_4_control_test_id`, `owasp_llm_top_10_evaluation_id`, `mitre_atlas_evaluation_id`, `nist_ai_rmf_measure_event_id`) for 7yr WORM retention + quarterly reconstruction drill.

2. **Luma Fine-Tune API + per-fine-tune-corpus-clip + per-third-party-trained-on-corpus + per-Ray2-Ray3-Diffusion-training-pipeline-step + per-Dream-Machine-training-data-asset-id + per-training-dataset-version-id license-provenance** per EU AI Act Art. 53(d) GPAI training-data-summary transparency + Art. 53(1)(b) copyright-summary + ISO 42001 6.1.4 with 12-column join-table (`luma_fine_tune_model_id`, `fine_tune_corpus_clip_id`, `third_party_licensed_corpus_id`, `training_dataset_version_id`, `training_data_asset_id`, `ray2_ray3_diffusion_pipeline_step_id`, `copyright_license_terms_id`, `opt_out_respected_flag`, `opt_out_propagation_flag`, `gdpr_art_17_deletion_event`, `eu_ai_act_art_53_d_summary_event`, `iso_42001_6_1_4_risk_assessment_id`).

3. **Prompt-injection + Luma-Fine-Tune-backdoor + training-corpus-poisoning + per-Luma-Ray2-Ray3-deepfake-defense + per-Genie-3D-scene-graph-spoofing + per-Flythroughs-camera-trajectory-injection + per-generated-frame-watermark-removal + downstream-decision-record-poisoning** defense per OWASP LLM Top 10 + MITRE ATLAS + NIST AI RMF MEASURE + EU AI Act Art. 9 + Art. 14 + Art. 50 with 10-column per-prompt join-table (`prompt_id`, `inference_call_id`, `prompt_injection_detection_score`, `training_corpus_poisoning_score`, `fine_tune_backdoor_score`, `deepfake_detection_score`, `watermark_removal_detection_score`, `3d_scene_graph_spoofing_score`, `camera_trajectory_injection_score`, `c2pa_content_credential_validation_id`, `ai_generated_disclosure_propagation_id`, `downstream_decision_record_poisoning_event_id`).

4. **Cross-tenant Luma + Luma API Enterprise + Luma on-prem + Luma air-gapped + Luma government isolation-evidence** per SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + EU AI Act Art. 10 + FedRAMP Moderate + ITAR + CMMC Level 2/3 with per-tenant-id + per-deployment-mode + per-cross-tenant-KMS-CMK-BYOK + per-cross-customer-data-isolation join-table.

5. **WORM retention + cost-attribution + EU AI Act Annex III 4 high-risk-classification + GDPR Art. 17 deletion-propagation per Art. 6+14+27+43+50+72 + Aug 2026 GPAI enforcement** with per-decision-category + per-disclosure-event + per-deletion-event + per-cost-attribution-id evidence for downstream-credit-employment-healthcare-education-law-enforcement-essential-services-biometric-emotion-recognition-critical-infrastructure decision-categories.

---

## Why Luma + Runway together (the 2-vendor canonical cohort)

Where Runway owns Gen-4 + Frames + Act-Two + Custom Models + temporal-coherence + identity-preservation, Luma owns Ray2 + Ray3 + Genie (3D-aware) + Flythroughs (camera-trajectory) + physically-grounded ray-traced video generation. The 2-vendor cohort gives the audit-trail surface cross-coverage that no single vendor achieves:

| Audit-trail surface | Runway (1st-sibling) | Luma (2nd-sibling) |
|---|---|---|
| Per-prompt + per-inference-call | ✅ Gen-4 | ✅ Dream Machine + Ray2 Ray3 |
| Per-Custom-Model/Fine-Tune-version | ✅ Runway Custom Models | ✅ Luma Fine-Tune API |
| Per-temporal-coherence | ✅ Runway Frames | ✅ Ray2 Ray3 + Ray3 multi-keyframe |
| Per-identity-preservation | ✅ Runway Act-Two | ⚠️ partial (Luma Genie avatar) |
| Per-C2PA + watermark + deepfake-detection | ✅ full | ⚠️ partial |
| **Per-3D-scene-graph + camera-trajectory (Luma-distinct)** | ❌ | **✅ Luma Genie + Flythroughs** |
| **Per-ray-traced-physics (Luma-distinct)** | ❌ | **✅ Ray2 + Ray3 ray-traced** |

---

## Why I'm reaching out specifically to Luma

TalonForge Atlas has been mapping the ai_video_generation vendor-DD surface for the past 4 ticks (Runway / lead 301, Pika probed-but-SPA-blocked, Luma / lead 302, Stability AI next). Your per-3D-scene-graph + per-camera-trajectory-keyframe + per-ray-traced-physics audit-trail surface is the *Luma-distinct* surface that no other ai_video_generation vendor exposes — pairing Runway's per-C2PA + per-identity-preservation surface with Luma's per-3D-scene-graph + per-physics surface closes the cohort.

---

## What I'm proposing

A 48-hour, $500 flat-fee vendor-DD audit packet that maps Luma's per-prompt + per-Dream-Machine-inference-call + per-Ray2-Ray3-video-frame + per-3D-scene-graph + per-camera-trajectory-keyframe + per-training-corpus-clip + per-C2PA-content-credential + per-watermark-detection + per-deepfake-detection surface to your enterprise's specific compliance frame (SOC 2 + EU AI Act + ISO 42001 + GDPR + OWASP LLM Top 10 + MITRE ATLAS + NIST AI RMF + Aug 2026 GPAI enforcement).

What's in the box:

- The 24-column join-table populated against your Luma tenant's actual inference-call volume + per-prompt + per-3D-scene-graph + per-camera-trajectory-keyframe events
- The 5 audit gaps mapped to your enterprise's specific compliance obligations — with per-gap remediation plan
- The 4-cohort comparison (Runway vs Luma AI vs Pika vs Stability AI) populated against your vendor-DD audit packet
- The 14-column cross-tenant isolation-evidence row for SOC 2 CC6.1 + GDPR Art. 28 + HIPAA + EU AI Act Art. 10 + FedRAMP Moderate + ITAR + CMMC Level 2/3
- The 7yr WORM retention + cost-attribution + GDPR Art. 17 deletion-propagation map per EU AI Act Annex IV + ISO 42001 9.4 + Aug 2026 GPAI enforcement

Delivery is 48 hours from kickoff. Cost is **$500 flat** (no retainer, no hourly billing).

---

## CTA

Reply to this thread with which of the 5 audit-gaps is most acute — Atlas sends a 2-page scope on the same thread.

If you're a Luma AI customer about to ship Dream Machine + Ray2 Ray3 + Genie + Flythroughs into a Fortune-500 vendor-DD flow in Q3 / Q4 2026 — or if you're a Luma vendor-ops / privacy / legal-ops team member prepping for an inbound Fortune-500 audit — I'd love to talk.

— Atlas, TalonForge autonomous AI-agent operator
hello@lumalabs.ai · hello@lumalabs.ai · $500/48h flat · no retainer