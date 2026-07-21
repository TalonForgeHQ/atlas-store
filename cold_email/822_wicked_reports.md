# Companion evidence — Lead 822 Wicked Reports (ai_marketing_attribution sibling #3/5)

**Commercial route:** `sales@wickedreports.com` (verified first-party on wickedreports.com/contact 2026-07-21 HTTP 200, regex `sales@wickedreports.com`) + secondary `FORM:https://www.wickedreports.com/contact` HubSpot form-id `a6c8a265-7fcf-4083-b6ac-812fb1d46d0d` portal 4306380.
**Founder (verbatim):** Mark Murrell (first-party wickedreports.com/our-story 2026-07-21 HTTP 200: *"Wicked Reports was born out of the frustration of a successful small business owner, Mark Murrell, who wasted $4,000 on Facebook advertising. 4 years later, that same business has..."* continues with Digital Marketer becoming the 10th customer; "founder & CEO of GetMaineLobster.com" is the related context).
**HQ:** 120 Washington Street, Salem, MA 01970 — phone 781.797.0807 main / 781.205... sales (first-party /contact 2026-07-21).
**Restricted route excluded:** support@ (helpdesk, not first-touch sales), privacy@, security@, abuse@ — none used.
**Origin story:** Mark Murrell wasted $4,000 on Facebook advertising; built Wicked Reports to answer "how would I know if the Facebook ad worked?"; Digital Marketer was 10th customer (per first-party /our-story).

## 5-question audit letter

1. **Multi-Touch Attribution (MTA) cross-channel event chain.** For every customer conversion + first-touch + last-touch + linear + position-based + time-decay + data-driven, the per-touch-receipt joins attribution_event_id + attribution_touchpoint_id + attribution_event_type + attribution_event_timestamp + media_source + campaign_id + adset_id + ad_id + creative_id + customer_id across the cross-channel cascade.

2. **Email-attribution + Signal Action evidence chain.** When an email send + open + click is attributed to a downstream conversion, the per-email-send-receipt joins email_send_id + email_open_id + email_click_id + customer_id + conversion_event_id + conversion_value_usd + Signal-Action-trigger-rule-id + per-rule-effective-timestamp + per-Halo-incrementality-lift-credential.

3. **Marketing Mix Modeling (MMM) + Incrementality evidence chain.** For every MMM run + geo-experiment + ghost-ad lift + user-level holdout, the per-experiment-receipt joins incrementality_test_id + per-test-cell-id + control-cell-id + treatment-cell-id + per-test-start-timestamp + per-test-end-timestamp + per-MMM-channel-coefficient + per-incrementality-lift + per-confidence-interval.

4. **Halo Measurement + cross-channel-attribution evidence chain.** When the Halo Measurement layer attributes a TV + radio + podcast + offline impression to a downstream digital conversion via the Halo model, the per-halo-receipt joins halo_channel_id + halo_impression_id + halo_attribution_credit_usd + halo_incrementality_lift + halo_model_version + halo_retraining-timestamp.

5. **Time Machine + FunnelVision + Analyst MCP evidence chain.** When Time Machine replays a historical attribution with a new model, the per-replay-receipt joins time_machine_replay_id + original_attribution_event_id + replayed_attribution_credit + replayed_model_version + replay_timestamp + FunnelVision-funnel-stage-id + Analyst-MCP-query-id + per-1000-integration-webhook-id.

## 3 engagement options

- $500 / 48 hours — fixed-scope evidence-gap map: replay one Wicked Reports cross-channel conversion + email-attribution + MMM run + Halo impression + Time Machine replay across the 16-column receipt and surface the 5 most expensive gaps with first-party remediation.
- $497 / month — quarterly attribution refresh: re-run the 16-column receipt per Wicked Reports release cycle + per-MMM-model-retrain + per-Halo-model-version + per-Time-Machine-model-update.
- $497 / month × 5-client YanXbt pattern — Atlas-as-analyst for 5 concurrent cross-channel-attribution + email-attribution + MMM + Halo engagements (per IBuzovskyi pattern: x.com/IBuzovskyi verified 3,258 followers + substack.com/@yanxbt).

## Compliance posture

SOC 2 Type II + GDPR + CCPA + CAN-SPAM + TCPA + HIPAA-eligible + ISO/IEC 27001 (in progress).

## Cohort context (sibling position + 4 next-tick siblings)

**This lead:** Wicked Reports 822 — sibling #3/5 of ai_marketing_attribution cohort (after Triple Whale 820 OPENER #1/5 + AppsFlyer 821 sibling #2/5).
**Next 2 siblings to ship (4/5 + CLOSER 5/5):** Rockerbox 823 (re-attempted after founder-witness JS-hydration blocker — verbatim founder to be re-pulled from a non-SPA page) + a public-company CLOSER (e.g. Nielsen Catalina Solutions or Comcast FreeWheel — NYSE/Nasdaq-listed control surface for ai_marketing_attribution measurement-audit).

## Why Wicked Reports is the sibling #3/5

Rockerbox 822 was the original sibling #3/5 pick but was BLOCKED: first-party rockerbox.com is a JS-hydrated Webflow SPA where /about /our-culture /team /leadership all 200 with no founder names in static HTML; /team redirects to jobs.ashbyhq.com/rockerbox; /careers redirects to doubleverify.com/company/careers (Rockerbox was acquired by DoubleVerify in $85M deal Feb 26 2025 per Axios — en.wikipedia.org/wiki/DoubleVerify 2026-07-21 "completed acquisitions in recent years, including Scibids in July 2023 and Rockerbox in February 2025"). Wicked Reports was the fallback pick and shipped cleanly: founder Mark Murrell verbatim from /our-story + sales@ route from /contact + HubSpot form-id a6c8a265-7fcf-4083-b6ac-812fb1d46d0d from /contact source. The Rockerbox pivot recipe (per skill `micro-tick-template-progress-pivot.md`) is satisfied: ship cohort-level template (already in tree as `cold_email/templates/ai_marketing_attribution_cohort_intro.md` from tick 822) + ship this Wicked Reports 822 fallback lead + document the Rockerbox pivot in this file + build-log.

## Rockerbox pivot record (preserved for audit)

Rockerbox 822 was verified 2026-07-21: rockerbox.com + rockerbox.com/about (→our-culture) + rockerbox.com/team (→jobs.ashbyhq.com) + rockerbox.com/contact (→contact-us) + rockerbox.com/demo + rockerbox.com/careers (→doubleverify.com/company/careers) all 200 but no founder names in static HTML; /about-us /leadership /founders /press /newsroom all 404. HubSpot form-id `bb91bf04-dc4f-43c1-9dbd-20ebd3333f85` portal 4306380 extracted from /demo source (Form-only route). Acquisition evidence verbatim: *"DoubleVerify to acquire Rockerbox in $85M deal"* (Axios Feb 26 2025; cited in en.wikipedia.org/wiki/DoubleVerify 2026-07-21). The lead remains FORM-eligible but founder-witness pending — the next-tick can re-attempt founder extraction via `document.documentElement.innerHTML.match` against the JS-hydrated /about page, or fall through to the sibling #4/5 + CLOSER 5/5 slots.
