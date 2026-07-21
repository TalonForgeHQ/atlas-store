# Companion evidence — Lead 821 AppsFlyer (ai_marketing_attribution sibling #2/5)

**Commercial route:** `FORM:https://www.appsflyer.com/start/demo/` (first-party canonical Demo form verified live HTTP 200 2026-07-21) + secondary `FORM:https://www.appsflyer.com/company/contact/`.
**Founders:** Oren Kaniel + Reshef Mann, co-founded 2011 in Israel (verbatim en.wikipedia.org/wiki/AppsFlyer 2026-07-21 "founded in Israel in 2011 by Oren Kaniel and Reshef Mann").
**Current CEO:** Shani Rosenfelder (promoted 2025-04 from CTO 2017 + Head of Product Solutions + SVP Product).
**HQ:** San Francisco SoMa (One Market Street Spear Tower suite 3500) + R&D Haifa Israel.
**Restricted route excluded:** no security@, privacy@, support@, or press@ inbox was used as the commercial route.

## 5-question audit letter (canonical body)

1. **SKAdNetwork-post-IDFA + cookieless-mobile event chain.** For every mobile install + in-app-event, the immutable receipt joins appsflyer_install_id + appsflyer_event_id + media_source + campaign_id + adset_id + ad_id + skan_postback_id + skan_conversion_value + skan_attribution_window across the cookieless-mobile + Apple ATT + SKAdNetwork cascade.

2. **Protect360 fraud-prevention evidence chain.** When Protect360 flags an install or event as fraudulent, the per-flag-receipt joins install-validation-failure-reason + click-flood-detection + bot-detection + post-attribution-fraud + retargeting-fraud + emulated-install + protection-rule-id + per-rule-effective-timestamp.

3. **AppsFlyer Incrementality evidence chain.** For every geo-experiment + ghost-ad lift + user-level holdout, the per-experiment-receipt joins incrementality_test_id + per-test-cell-id + control-cell-id + treatment-cell-id + per-test-start-timestamp + per-test-end-timestamp + per-incrementality-lift + per-confidence-interval.

4. **AppsFlyer Audiences + Audience-Sends evidence chain.** When a customer-audience is sent to Meta + Google + TikTok + Snap + Pinterest + Reddit + Liftoff + Moloco + ironSource + Unity + Apple Search Ads + Criteo + Yahoo + DOOH + CTV, the per-audience-send-receipt joins audience_segment_id + destination_platform + per-match-key + per-expiration + per-conversion-event-used-for-optimization + per-LAL-lookalike-feed-back.

5. **AppsFlyer CTV + household-graph + cross-device evidence chain.** When AppsFlyer CTV attributes a connected-TV impression to a downstream mobile install via household-graph + cross-device-merge, the per-CTV-rendered-impression + per-household-id + per-cross-device-merge-event + per-CTV-incrementality-test + per-MRC-CTV-measurement-guideline-version + per-IAB-Tech-Lab-CTV-Open-Measurement-version + per-cross-device-attribution-window joins the CTV row to the SKAdNetwork install + Protect360 fraud-flag + Audiences send + Incrementality test.

## 3 engagement options

- $500 / 48 hours — fixed-scope evidence-gap map: replay one AppsFlyer install, SKAdNetwork postback, Protect360 fraud-flag, Incrementality test, and CTV impression across the 18-column receipt and surface the 5 most expensive gaps with first-party remediation.
- $497 / month — quarterly mobile-attribution refresh: re-run the 18-column receipt per AppsFlyer release cycle + per-SKAN-postback-format-change + per-Protect360-rule-update + per-CTV-household-graph-merge-event.
- $497 / month × 5-client YanXbt pattern — Atlas-as-analyst for 5 concurrent mobile-attribution + fraud-prevention + incrementality + CTV-measurement engagements (per IBuzovskyi pattern: x.com/IBuzovskyi verified 3,258 followers + substack.com/@yanxbt).

## Compliance posture

SOC 2 Type II + ISO/IEC 27001:2022 + ISO/IEC 27018:2019 + ISO/IEC 27701:2019 + GDPR + UK GDPR + EU AI Act (Aug 2 2026 + Art. 50) + CCPA/CPRA + LGPD + APPI + PIPEDA + Australia Privacy Act + Singapore PDPA + COPPA + HIPAA + Apple ATT framework + Google Play Families Policy + EU DSA Art. 28 + EU DMA gatekeeper-obligations + IAB Tech Lab Open Measurement SDK + MRC measurement-standards (MRC mobile-attribution + MRC CTV-measurement + MRC cross-media-measurement) + WFA cross-media-measurement-standard.

## Prior sibling in this cohort

Triple Whale 820 OPENER #1/5 — AI-native DTC-ecommerce + Sonar AI-search + Moby AI + Compass MMM/MTA wedge. AppsFlyer 821 owns the mobile-attribution + SKAdNetwork + Protect360 fraud-prevention + Incrementality + CTV-household-graph wedge that Triple Whale does not ship.

## Planned next siblings

Rockerbox (Rockerbox multi-touch attribution + paid-social + paid-search + affiliate + influencer + podcast + TV + out-of-home measurement) + Measured (Measured incrementality + cross-channel experimentation + commerce-media measurement) + Northbeam (Northbeam multi-touch + AI-augmented attribution).
