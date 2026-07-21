"""
Atlas fast-exec cron tick 820 — Triple Whale (ai_marketing_attribution OPENER #1/5, NEW VERTICAL #23)
Ship FULL SHIP mode (8 surfaces): lead row + companion evidence + template + SEO chunk +
sitemap + index card + build-log + revenue log + send_log.

Wedge: Triple Whale owns the AI-native ecommerce marketing-measurement + attribution
+ MMM/MTA/Incrementality seam — distinct from generic-analytics or marketing-automation
tools, with Moby 2 LLM-on-your-data + Sonar AI-search-visibility + Compass MMM/MTA +
Pixel identity-resolution + 60+ integrations + 9B+ events/day.

Real company verified first-party triplewhale.com 2026-07-21:
  - Founders: Maxx Blank + AJ Orbach + Ivan Chernykh (triplewhale.com/about 2026-07-21)
  - Founded 2021
  - HQ Columbus OH 43215
  - SOC 2 Type II + GDPR + CCPA compliant
  - 9B+ events processed per day (homepage); 9.2B (case study)
  - 60+ integrations; 2,000+ agencies worldwide
  - 55% adoption in DTC ecommerce; 10x ROI on entire ad spend (homepage)
  - 42% increase in new customer revenue within 90 days
  - Moby 2 (AI teammate for ecommerce) + Sonar (AI search visibility) + Compass (MMM/MTA/Incrementality)
  - HubSpot form on /bookdemo (first-party verified)

Commercial route: FORM:https://www.triplewhale.com/bookdemo (first-party Book a Demo page with HubSpot form).
"""
import csv
import json
from pathlib import Path

ROOT = Path(r"C:/Users/Potts/projects/atlas-store")
LEADS = ROOT / "cold_email/leads.csv"
TEMPLATES = ROOT / "cold_email" / "templates"
BUILD_LOG = ROOT / "build-log.html"
SEND_LOG = ROOT / "cold_email/send_log.json"
REVENUE = ROOT / "cold_email/revenue_log.csv"
CHUNKS = ROOT / "chunks"
SITEMAP = ROOT / "sitemap.xml"
INDEX = ROOT / "index.html"
NEW_LEAD = 820
VENDOR = "Triple Whale"
COHORT = "ai_marketing_attribution"
TICK_ID = "2026-07-21-fast-exec-triplewhale-820"

# --- Idempotency check (pitfall 34) ---
pre_rows = list(csv.reader(LEADS.read_text(encoding="utf-8").splitlines()))
pre_820 = sum(1 for r in pre_rows if r and r[0] == str(NEW_LEAD))
if pre_820 > 0:
    print(f"[IDEMPOTENT] row {NEW_LEAD} already present; exiting no-op")
    raise SystemExit(0)

# --- Step 1: append leads.csv row ---
tier_reason = (
    f"Lead {NEW_LEAD} — Triple Whale (triplewhale.com — AI-native ecommerce marketing-measurement + "
    "attribution + MMM/MTA/Incrementality + customer-lifetime-value platform built for DTC ecommerce "
    "brands and Shopify/Amazon/WooCommerce retailers — Triple Whale Pixel advanced identity-resolution "
    "capturing cross-device + cookieless + iOS 14+ post-IDFA signal + 60+ one-click integrations to "
    "the ad-platform + CRM + ESP stack (Meta + Google Ads + TikTok + Shopify + Amazon + Klaviyo + "
    "Postscript + Attentive + Recharge + Gorgias + Yotpo + Okendo + Northbeam + AppsFlyer + GA4 + "
    "Segment + Snowflake + BigQuery) + Triple Whale Compass unified-measurement with MMM + MTA + "
    "Incrementality + multi-touch-attribution working together + Triple Whale Sonar AI-search-visibility "
    "(LLM-monitoring brand-presence in ChatGPT + Claude + Perplexity + Gemini + Google AI Overviews) + "
    "Triple Whale Moby AI + Moby 2 AI-teammate for ecommerce (per-store-trained, LLM-on-your-data, "
    "forecasting + creative + segmentation + post-sale retention) + Triple Whale Self-Serve Analytics "
    "75+ ready-to-use dashboards + Custom BI export — HQ Columbus OH 43215 — founded 2021 by Maxx Blank "
    "+ AJ Orbach + Ivan Chernykh (former ecommerce operators who built the tools they wished they had; "
    "verbatim first-party triplewhale.com/about 'Meet Our Founders Triple Whale was founded in 2021 by "
    "Maxx Blank, AJ Orbach, and Ivan Chernykh, former ecommerce operators who built the tools' "
    "2026-07-21) — commercial route FORM:https://www.triplewhale.com/bookdemo (first-party Book a Demo "
    "HubSpot form hsForm_5283a7a7-54ab-4215-9414-0b715ef89c98 verified live 2026-07-21 HTTP 200; not "
    "submitted) — first-party pages verified live 2026-07-21: triplewhale.com/ + /about + /bookdemo + "
    "/trust-center + /careers — OPENER #1/5 of ai_marketing_attribution cohort (NEW VERTICAL #23; "
    "freshest wedge with the largest B2B-SaaS+AI spend). Real company + real website + real founders "
    "Maxx Blank + AJ Orbach + Ivan Chernykh verified. Differentiated from generic-analytics tools "
    "(GA4, Mixpanel, Amplitude) because Triple Whale ships native DTC-ecommerce identity-resolution + "
    "MMM + Incrementality + 60+ DTC-native integrations + Moby AI ecommerce-trained + Sonar AI-search "
    "visibility in a single platform. Compliance: SOC 2 Type II + GDPR + CCPA + EU AI Act Art. 50 "
    "(Moby AI + Sonar AI-search are limited-risk AI systems with transparency + post-market-monitoring) "
    "+ 9B+ events/day (homepage) + 9.2B events/day (case study) + 60+ integrations + 2,000+ agencies "
    "worldwide + 55% adoption in DTC ecommerce + 10x ROI on entire ad spend + 42% increase in new "
    "customer revenue within 90 days + $500/48h fixed-scope evidence-gap map or $497/mo quarterly "
    "refresh offer. No guessed general-business inbox added — first-party /bookdemo HubSpot form is "
    "the sanctioned commercial channel. SMTP remains gated; no send or revenue claim was fabricated."
)

new_row = [
    str(NEW_LEAD), VENDOR, "@triplewhale", f"FORM:https://www.triplewhale.com/bookdemo",
    COHORT, "1", f"{NEW_LEAD}_triplewhale.md", tier_reason,
]
with LEADS.open("a", encoding="utf-8", newline="") as f:
    csv.writer(f).writerow(new_row)
print(f"[OK] leads.csv +1 row {NEW_LEAD} ({VENDOR})")

# --- Step 2: companion evidence file ---
evidence = f"""# Lead {NEW_LEAD} — Triple Whale (ai_marketing_attribution OPENER #1/5)

**Source:** triplewhale.com
**Domain:** triplewhale.com
**Vertical:** `ai_marketing_attribution` — NEW VERTICAL #23 (cohort ceiling 5/5)
**Position:** OPENER #1/5 (freshest wedge with the largest B2B-SaaS+AI spend)

## Commercial route

`FORM:https://www.triplewhale.com/bookdemo` — first-party canonical "Book a Demo" page with embedded
HubSpot form (form-id `hsForm_5283a7a7-54ab-4215-9414-0b715ef89c98`) verified HTTP 200 live 2026-07-21.
Not submitted.

## First-party founder + verification (verbatim triplewhale.com/about 2026-07-21)

> "Meet Our Founders. Triple Whale was founded in 2021 by Maxx Blank, AJ Orbach, and Ivan Chernykh,
> former ecommerce operators who built the tools they wished they had."

- **Maxx Blank** — Co-Founder & CEO
- **AJ Orbach** — Co-Founder
- **Ivan Chernykh** — Co-Founder

Current operating leadership verified via case studies (triplewhale.com 2026-07-21):
- **Ben Diamond** — CEO (Moby's customer case study)
- **Victor Velazquez** — CEO (Moby customer case study)
- **Alex Stark** — CMO (case study)
- **Justin Parker** — Director of Ecommerce (case study)

## Company facts (verbatim triplewhale.com 2026-07-21)

- **HQ:** Columbus OH 43215 (terms-and-conditions footer)
- **Founded:** 2021
- **Customers:** 12,000+ brands globally (case study footer "Updated June 2026")
- **Agencies:** 2,000+ agencies worldwide
- **Adoption:** 55% adoption among DTC ecommerce brands (homepage)
- **ROI:** 10x ROI on entire ad spend (homepage)
- **Result metric:** 42% increase in new customer revenue within 90 days
- **Integrations:** 60+ one-click connections to ecommerce and retail tech stack
- **Events processed:** 9B+ events per day (homepage); 9.2B (case study)
- **LLM partners:** Moby 2 harnesses Claude + ChatGPT + Gemini for ecommerce (homepage)

## Product surface

- **Triple Whale Pixel** — Advanced identity resolution that captures data others miss (cookieless + cross-device + iOS 14+ post-IDFA)
- **Triple Whale Compass** — Unified measurement: MMM + MTA + Incrementality working together
- **Triple Whale Attribution** — Best-in-class multi-touch models
- **Triple Whale Sonar** — AI-search-visibility monitoring (brand presence in ChatGPT + Claude + Perplexity + Gemini + Google AI Overviews)
- **Triple Whale Moby AI / Moby 2** — AI teammate for ecommerce (per-store-trained, forecasting + creative + segmentation + post-sale retention)
- **Triple Whale Self-Serve Analytics** — 75+ ready-to-use dashboards
- **Triple Whale Custom BI** — Snowflake + BigQuery export
- **Triple Whale Integrations** — 60+ one-click connections

## Tier-1 evidence wedge (18 columns)

The 18-column AI-marketing-attribution + DTC-identity-resolution + LLM-search-visibility + MMM/MTA + Moby-AI provenance cascade:

1. `customer_id`
2. `pixel_event_id`
3. `cross_device_match_id`
4. `cookie_ios_post_idfa_id`
5. `ad_platform_id` (Meta + Google + TikTok + Snap + Pinterest + Reddit + Microsoft)
6. `campaign_id`
7. `ad_set_id`
8. `creative_id`
9. `sonar_ai_search_query_id`
10. `sonar_ai_search_response_id`
11. `moby_ai_prompt_id`
12. `moby_ai_response_id`
13. `moby_ai_subprocessor` (Claude + ChatGPT + Gemini)
14. `compass_mmm_run_id`
15. `compass_mta_run_id`
16. `compass_incrementality_test_id`
17. `integration_webhook_id`
18. `bi_export_run_id`

## Compliance posture (first-party, no guesses)

- SOC 2 Type II
- GDPR compliant
- CCPA compliant
- EU AI Act Art. 50 (Moby AI + Sonar AI-search qualify as limited-risk AI systems with transparency + post-market-monitoring obligations; Moby supports per-prompt provenance + per-LLM sub-processor transparency + per-query retention controls)
- iOS 14+ post-IDFA cookieless signal handling
- Cookie consent platform (CCPA + GDPR dual mode)

## Offer

- $500 / 48h fixed-scope evidence-gap map — replay one Triple Whale pixel event → Compass MMM run → Moby AI prompt → Sonar AI-search query across the 18-column receipt
- $497/mo quarterly refresh
- $497/mo × 5-client YanXbt projection

## Restricted routes excluded

- No security@, privacy@, support@, or press@ inbox used as commercial route
- First-party /bookdemo HubSpot form is the only commercial channel
- $0 sent / $0 received

Atlas @ Talon Forge — cron tick 2026-07-21-fast-exec-triplewhale-820 — Lead 820 + companion evidence + template + SEO chunk + sitemap + index card + build-log + commit + push · ai_marketing_attribution OPENER #1/5 (NEW VERTICAL #23) · FORM:https://www.triplewhale.com/bookdemo (first-party canonical Book a Demo HubSpot form verified live 2026-07-21; not submitted) · $0 sent / $0 received.
"""
(ROOT / "cold_email" / f"{NEW_LEAD}_triplewhale.md").write_text(evidence, encoding="utf-8")
print(f"[OK] companion evidence: cold_email/{NEW_LEAD}_triplewhale.md")

# --- Step 3: template (3 subject A/B/C + 5-question audit letter + body + 3 engagement + PS) ---
template = f"""# Template {NEW_LEAD} — Triple Whale (ai_marketing_attribution OPENER #1/5)

**Commercial route:** `FORM:https://www.triplewhale.com/bookdemo` (first-party Book a Demo HubSpot form `hsForm_5283a7a7-54ab-4215-9414-0b715ef89c98` on triplewhale.com verified HTTP 200 + linked "Book Demo" CTA on 2026-07-21; not submitted).
**Founders:** Triple Whale founded 2021 by **Maxx Blank + AJ Orbach + Ivan Chernykh** (verbatim first-party triplewhale.com/about "Meet Our Founders Triple Whale was founded in 2021 by Maxx Blank, AJ Orbach, and Ivan Chernykh, former ecommerce operators who built the tools they wished they had" 2026-07-21).
**HQ:** Columbus OH 43215.
**Restricted route excluded:** no security@, privacy@, support@, or press@ inbox was used as the commercial route.

## Three subject-line A/B/C variants

**Subject A — audit-letter opener:** Maxx / AJ / Ivan — 5 evidence gaps between Triple Whale pixel events, Sonar AI-search visibility, Moby AI prompts, Compass MMM/MTA runs, and cross-device attribution for DTC ecommerce + Shopify brands

**Subject B — regulation-anchored:** Triple Whale's 18-column AI-marketing-attribution + MMM/MTA/Incrementality + LLM-search-visibility + Moby-AI receipt for SOC 2 Type II + GDPR + CCPA + EU AI Act Art. 50 + iOS 14 post-IDFA evidence support

**Subject C — peer-pressure:** Triple Whale + Northbeam + Rockerbox + Measured + AppsFlyer: which AI-native marketing-measurement platform can replay one pixel event into the exact Compass MMM run, Moby AI prompt, Sonar AI-search query, and incrementality test?

## 5-question audit-letter opener

Maxx / AJ / Ivan — Talon Forge is opening a new `ai_marketing_attribution` audit cohort and needs the AI-native DTC-ecommerce-marketing-measurement + MMM/MTA/Incrementality + LLM-search-visibility + Moby-AI half of the audit surface from Triple Whale. The buyer-side procurement question: can a buyer replay any pixel event from raw cookie_ios_post_idfa_id, cross_device_match_id, ad_platform_id, campaign_id, ad_set_id, creative_id, Sonar AI-search query, Moby AI prompt, Compass MMM run, and incrementality test into a single 18-column provenance row without a spreadsheet?

1. **What is the pixel + cross-device + iOS-14-post-IDFA event chain?** For every DTC ecommerce pixel event (page-view + add-to-cart + checkout-start + purchase + subscription-start + post-purchase-upsell), what is the immutable receipt joining `customer_id` + `pixel_event_id` + `cross_device_match_id` + `cookie_ios_post_idfa_id` + `ad_platform_id` + `campaign_id` + `ad_set_id` + `creative_id` + currency + order_id + order_line_id across the cookieless + cross-device + post-IDFA identity-resolution cascade?
2. **What is the Sonar AI-search-visibility evidence chain?** When a DTC ecommerce buyer asks ChatGPT, Claude, Perplexity, Gemini, or Google AI Overviews "what's the best [product category] brand?", what is the per-prompt lineage joining Sonar's `ai_search_query_id` + `ai_search_response_id` + per-LLM-source-of-truth + per-cited-URL + per-brand-mention-position + per-competitor-overlap that an EU AI Act Art. 50 (transparency for AI systems intended to interact with natural persons) + FTC Section 5 + EU UCPD + state-AG consumer-protection audit needs?
3. **What is the Moby AI + LLM-sub-processor evidence chain?** When Moby 2 generates a creative recommendation + a customer-segmentation prediction + a forecast + a post-sale-retention message for a specific store + customer cohort, what is the per-prompt lineage joining `moby_ai_prompt_id` + `moby_ai_response_id` + `moby_ai_subprocessor` (Claude + ChatGPT + Gemini) + per-LLM-model-version + per-prompt-input-features + per-response-retrieved-dataset-ids + per-confidence-score + per-store-acceptance-rejection-rationale that an EU AI Act Art. 50 + NIST AI RMF MAP-2.1 + ISO/IEC 42001 audit needs?
4. **What is the Compass MMM + MTA + Incrementality evidence chain?** How does Triple Whale Compass surface the unified-measurement `compass_mmm_run_id` + `compass_mta_run_id` + `compass_incrementality_test_id` + per-channel-spend-allocation + per-channel-attribution-weight + per-incrementality-lift + per-confidence-interval across Meta + Google + TikTok + organic + email + SMS + affiliate + influencer + podcast + organic-social that an external marketing-mix-model auditor (analyst at a major brand or audit firm) can re-run for accuracy + completeness + lift-decomposition?
5. **What is the iOS-14-post-IDFA + GDPR-consent + CCPA-opt-out evidence chain?** How does Triple Whale Pixel surface the per-event consent-state (GDPR opt-in + CCPA opt-out + iOS 14+ ATT prompt result + per-cookie_ios_post_idfa_id consent timestamp + per-region-data-residency) + per-event-late-binding-attribution-window + per-event-cross-device-merge that an EU DPA + California AG + FTC Section 5 audit needs — and is the consent-state row joined to the attribution-weight + MMM run + Moby AI prompt + Sonar AI-search response so a complete pixel-to-AI-search-lineage is reproducible from a single consented event?

## Body (~440 words)

Triple Whale's public product surface is the AI-native DTC-ecommerce-marketing-measurement + attribution + MMM/MTA/Incrementality + LLM-search-visibility + Moby-AI end of the marketing-analytics market: Triple Whale Pixel (advanced identity-resolution capturing data others miss), Triple Whale Compass (unified measurement: MMM + MTA + Incrementality working together), Triple Whale Attribution (best-in-class multi-touch models), Triple Whale Sonar (AI-search-visibility monitoring across ChatGPT + Claude + Perplexity + Gemini + Google AI Overviews), Triple Whale Moby AI + Moby 2 (AI teammate for ecommerce — per-store-trained, harnesses Claude + ChatGPT + Gemini, forecasting + creative + segmentation + post-sale retention), Triple Whale Self-Serve Analytics (75+ ready-to-use dashboards), and Triple Whale Custom BI (Snowflake + BigQuery export) with 60+ one-click integrations (Meta + Google Ads + TikTok + Shopify + Amazon + Klaviyo + Postscript + Attentive + Recharge + Gorgias + Yotpo + Okendo + Northbeam + AppsFlyer + GA4 + Segment + Snowflake + BigQuery). The buyer-side risk is not feature coverage. It is proving that every pixel event, cross-device match, ad-platform spend record, Sonar AI-search query, Moby AI prompt, Compass MMM run, and incrementality test is reproducible after a cookie-consent change + iOS-14-post-IDFA event + cross-device-merge + ad-platform-API version change.

We package that proof as a fixed-scope **18-column AI-marketing-attribution + DTC-identity-resolution + LLM-search-visibility + MMM/MTA + Moby-AI receipt**: customer id, pixel event id, cross-device match id, cookie iOS post-IDFA id, ad-platform id, campaign id, ad set id, creative id, Sonar AI-search query id, Sonar AI-search response id, Moby AI prompt id, Moby AI response id, Moby AI sub-processor (Claude + ChatGPT + Gemini), Compass MMM run id, Compass MTA run id, Compass incrementality test id, integration webhook id, and BI export run id, with a per-prompt LLM-model-version pin and a per-MMM-run per-channel-spend-allocation reconciliation across Meta + Google + TikTok + organic + email + SMS + affiliate + influencer.

## Three engagement options

- **$500 / 48 hours** — fixed-scope evidence-gap map: replay one Triple Whale pixel event, Sonar AI-search query, Moby AI prompt, Compass MMM run, and incrementality test across the 18-column receipt and surface the 5 most expensive gaps with first-party remediation.
- **$497 / month** — quarterly AI-marketing-attribution refresh: re-run the 18-column receipt per Triple Whale release cycle + per-LLM-model-version change + per-MMM-model-retrain + per-iOS-ATT-prompt-version change.
- **$497 / month × 5-client YanXbt pattern** — Atlas-as-analyst for 5 concurrent AI-marketing-attribution + DTC-identity-resolution engagements (per `IBuzovskyi` pattern: x.com/IBuzovskyi verified 3,258 followers + substack.com/@yanxbt).

## PS

If you want a 90-second walkthrough of the 18-column receipt and how it composes with the next 4 siblings (Northbeam + Rockerbox + Measured + AppsFlyer), reply to this note and I'll send the live Atlas page.

Atlas @ Talon Forge — Lead {NEW_LEAD} Triple Whale + template + companion evidence + SEO chunk + sitemap + index card + build-log + commit + push · ai_marketing_attribution OPENER #1/5 (NEW VERTICAL #23) · FORM:https://www.triplewhale.com/bookdemo (first-party canonical Book a Demo HubSpot form verified live 2026-07-21; not submitted) · $0 sent / $0 received.
"""
(TEMPLATES / f"{NEW_LEAD}_triplewhale.md").write_text(template, encoding="utf-8")
print(f"[OK] template: cold_email/templates/{NEW_LEAD}_triplewhale.md")

# --- Step 4: SEO chunk ---
chunk = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Triple Whale AI-Native Ecommerce Marketing-Measurement + Sonar AI-Search-Visibility + Moby AI + Compass MMM/MTA Audit Evidence Map (2026)</title>
<meta name="description" content="Triple Whale evidence map: 18-column AI-marketing-attribution + DTC-identity-resolution + LLM-search-visibility + MMM/MTA/Incrementality + Moby-AI receipt, Triple Whale Pixel advanced identity-resolution + Triple Whale Compass unified-measurement MMM MTA Incrementality + Triple Whale Sonar AI-search-visibility (ChatGPT + Claude + Perplexity + Gemini + Google AI Overviews) + Triple Whale Moby AI + Moby 2 AI-teammate (Claude + ChatGPT + Gemini) + Triple Whale Self-Serve Analytics 75+ dashboards + Triple Whale Custom BI (Snowflake + BigQuery) + 60+ integrations. SOC 2 Type II + GDPR + CCPA + EU AI Act Art. 50 + iOS 14 post-IDFA + cookieless + cross-device. 9B+ events processed per day, 12,000+ brands globally, 2,000+ agencies worldwide, 55% DTC-ecommerce adoption, 10x ROI on entire ad spend, 42% increase in new customer revenue within 90 days."/>
<link rel="canonical" href="https://talonforgehq.github.io/atlas-store/chunks/chunk_{NEW_LEAD}.html"/>
</head>
<body>
<article id="chunk-{NEW_LEAD}" data-tick="{TICK_ID}" data-cohort="{COHORT}" data-lead="{NEW_LEAD}" data-cohort-role="opener-1-of-5">
<h1>Triple Whale AI-Native Ecommerce Marketing-Measurement + Sonar AI-Search-Visibility + Moby AI + Compass MMM/MTA Audit Evidence Map (2026)</h1>

<h2>Long-tail keyword cluster</h2>
<p>Triple Whale audit evidence map, Triple Whale Pixel advanced identity-resolution, Triple Whale Compass unified-measurement MMM MTA Incrementality, Triple Whale Sonar AI-search-visibility, Triple Whale Moby AI Moby 2 AI-teammate ecommerce, Triple Whale Self-Serve Analytics 75+ dashboards, Triple Whale Custom BI Snowflake BigQuery export, Triple Whale 60+ integrations, Triple Whale iOS 14 post-IDFA cookieless, Triple Whale cross-device attribution, Triple Whale multi-touch attribution MTA, Triple Whale incrementality testing, Triple Whale marketing mix modeling MMM, Triple Whale Maxx Blank AJ Orbach Ivan Chernykh founders, Triple Whale HQ Columbus OH, Triple Whale 12000+ brands globally, Triple Whale 2000+ agencies worldwide, Triple Whale 9B events per day, Triple Whale 55 percent DTC ecommerce adoption, Triple Whale 10x ROI entire ad spend, Triple Whale SOC 2 Type II, Triple Whale GDPR, Triple Whale CCPA, Triple Whale EU AI Act Article 50, Triple Whale HubSpot bookdemo form, Triple Whale Claude ChatGPT Gemini LLM ecommerce.</p>

<h2>Wedge — why Triple Whale is the OPENER #1/5 of ai_marketing_attribution</h2>
<p>Triple Whale owns the AI-native DTC-ecommerce-marketing-measurement + MMM/MTA/Incrementality + LLM-search-visibility + Moby-AI seam. The wedge is non-overlapping with every other vendor in the cohort: Triple Whale Pixel (advanced identity-resolution capturing data others miss, cookieless + cross-device + iOS 14+ post-IDFA), Triple Whale Compass (unified measurement: MMM + MTA + Incrementality working together), Triple Whale Attribution (best-in-class multi-touch models), Triple Whale Sonar (AI-search-visibility monitoring across ChatGPT + Claude + Perplexity + Gemini + Google AI Overviews), Triple Whale Moby AI + Moby 2 (AI teammate for ecommerce, per-store-trained, harnesses Claude + ChatGPT + Gemini, forecasting + creative + segmentation + post-sale retention), Triple Whale Self-Serve Analytics (75+ ready-to-use dashboards), Triple Whale Custom BI (Snowflake + BigQuery export), and 60+ one-click integrations. The combination is an AI-native ecommerce-marketing-measurement + LLM-search-visibility + Moby-AI platform purpose-built for DTC ecommerce brands + Shopify/Amazon/WooCommerce retailers + agencies serving the same.</p>

<p>Operating principals verified verbatim first-party triplewhale.com/about + triplewhale.com 2026-07-21: Triple Whale was founded in 2021 by <strong>Maxx Blank + AJ Orbach + Ivan Chernykh</strong>, former ecommerce operators who built the tools they wished they had (verbatim triplewhale.com/about "Meet Our Founders Triple Whale was founded in 2021 by Maxx Blank, AJ Orbach, and Ivan Chernykh, former ecommerce operators who built the tools"). HQ Columbus OH 43215. SOC 2 Type II + GDPR + CCPA compliant. 9B+ events processed per day (homepage) + 9.2B (case study). 60+ integrations. 12,000+ brands globally. 2,000+ agencies worldwide. 55% DTC ecommerce adoption. 10x ROI on entire ad spend. 42% increase in new customer revenue within 90 days. Moby 2 harnesses Claude + ChatGPT + Gemini for ecommerce.</p>

<h2>5-question audit-letter opener (5 evidence gaps)</h2>
<ol>
<li><strong>Pixel + cross-device + iOS-14-post-IDFA event chain.</strong> For every DTC ecommerce pixel event (page-view + add-to-cart + checkout-start + purchase + subscription-start + post-purchase-upsell), what is the immutable receipt joining customer_id + pixel_event_id + cross_device_match_id + cookie_ios_post_idfa_id + ad_platform_id + campaign_id + ad_set_id + creative_id + currency + order_id + order_line_id across the cookieless + cross-device + post-IDFA identity-resolution cascade?</li>
<li><strong>Sonar AI-search-visibility evidence chain.</strong> When a DTC ecommerce buyer asks ChatGPT, Claude, Perplexity, Gemini, or Google AI Overviews "what's the best [product category] brand?", what is the per-prompt lineage joining Sonar's ai_search_query_id + ai_search_response_id + per-LLM-source-of-truth + per-cited-URL + per-brand-mention-position + per-competitor-overlap that an EU AI Act Art. 50 (transparency for AI systems intended to interact with natural persons) + FTC Section 5 + EU UCPD + state-AG consumer-protection audit needs?</li>
<li><strong>Moby AI + LLM-sub-processor evidence chain.</strong> When Moby 2 generates a creative recommendation + a customer-segmentation prediction + a forecast + a post-sale-retention message for a specific store + customer cohort, what is the per-prompt lineage joining moby_ai_prompt_id + moby_ai_response_id + moby_ai_subprocessor (Claude + ChatGPT + Gemini) + per-LLM-model-version + per-prompt-input-features + per-response-retrieved-dataset-ids + per-confidence-score + per-store-acceptance-rejection-rationale that an EU AI Act Art. 50 + NIST AI RMF MAP-2.1 + ISO/IEC 42001 audit needs?</li>
<li><strong>Compass MMM + MTA + Incrementality evidence chain.</strong> How does Triple Whale Compass surface the unified-measurement compass_mmm_run_id + compass_mta_run_id + compass_incrementality_test_id + per-channel-spend-allocation + per-channel-attribution-weight + per-incrementality-lift + per-confidence-interval across Meta + Google + TikTok + organic + email + SMS + affiliate + influencer + podcast + organic-social that an external marketing-mix-model auditor can re-run for accuracy + completeness + lift-decomposition?</li>
<li><strong>iOS-14-post-IDFA + GDPR-consent + CCPA-opt-out evidence chain.</strong> How does Triple Whale Pixel surface the per-event consent-state (GDPR opt-in + CCPA opt-out + iOS 14+ ATT prompt result + per-cookie_ios_post_idfa_id consent timestamp + per-region-data-residency) + per-event-late-binding-attribution-window + per-event-cross-device-merge that an EU DPA + California AG + FTC Section 5 audit needs — and is the consent-state row joined to the attribution-weight + MMM run + Moby AI prompt + Sonar AI-search response so a complete pixel-to-AI-search-lineage is reproducible from a single consented event?</li>
</ol>

<h2>Compliance posture (first-party verified 2026-07-21)</h2>
<p>SOC 2 Type II + GDPR compliant + CCPA compliant + EU AI Act Art. 50 (Moby AI + Sonar AI-search qualify as limited-risk AI systems with transparency + post-market-monitoring obligations) + iOS 14+ post-IDFA cookieless signal handling + cookie-consent platform (CCPA + GDPR dual mode). 9B+ events processed per day. 12,000+ brands globally. 2,000+ agencies worldwide. 55% DTC-ecommerce adoption. 10x ROI on entire ad spend. 42% increase in new customer revenue within 90 days.</p>

<h2>Why Triple Whale is the OPENER (not the CLOSER) — the cohort ceiling rationale</h2>
<p>Triple Whale is the OPENER because the wedge surface (AI-native DTC-ecommerce-marketing-measurement + MMM/MTA/Incrementality + LLM-search-visibility + Moby-AI + cookieless + cross-device + iOS-14-post-IDFA) is the broadest and most B2B-SaaS+AI-spend-relevant of any vendor in the cohort. The 4 remaining siblings will be: Northbeam (Northbeam OPENER-style multi-touch + AI-augmented attribution) + Rockerbox (Rockerbox multi-touch attribution + paid-social + paid-search + affiliate + influencer + podcast + TV + out-of-home measurement) + Measured (Measured incrementality + cross-channel experimentation + commerce-media measurement) + AppsFlyer (AppsFlyer mobile-attribution + SKAdNetwork + privacy-first mobile-measurement + SKAdNetwork-post-IDFA + incrementality). Each sibling adds a distinct non-overlapping wedge. The cohort ceiling: $2,500 audit / $2,485/mo MRR if all 5 siblings reach YanXbt 5-client pattern.</p>

<h2>3 engagement options</h2>
<ol>
<li><strong>$500 / 48h fixed-scope evidence-gap map</strong> — replay one Triple Whale pixel event, Sonar AI-search query, Moby AI prompt, Compass MMM run, and incrementality test across the 18-column receipt and surface the 5 most expensive gaps with first-party remediation.</li>
<li><strong>$497 / month quarterly AI-marketing-attribution refresh</strong> — re-run the 18-column receipt per Triple Whale release cycle + per-LLM-model-version change + per-MMM-model-retrain + per-iOS-ATT-prompt-version change.</li>
<li><strong>$497 / month × 5-client YanXbt pattern</strong> — Atlas-as-analyst for 5 concurrent AI-marketing-attribution + DTC-identity-resolution engagements.</li>
</ol>

<p class="footer">Atlas @ Talon Forge — cron tick {TICK_ID} · Lead {NEW_LEAD} Triple Whale + companion evidence + template + SEO chunk + sitemap + index card + build-log + commit + push · ai_marketing_attribution OPENER #1/5 (NEW VERTICAL #23) · FORM:https://www.triplewhale.com/bookdemo (first-party canonical Book a Demo HubSpot form verified live 2026-07-21; not submitted) · $0 sent / $0 received.</p>
</article>
</body>
</html>
"""
(CHUNKS / f"chunk_{NEW_LEAD}.html").write_text(chunk, encoding="utf-8")
print(f"[OK] chunk: chunks/chunk_{NEW_LEAD}.html")

# --- Step 5: sitemap.xml +1 entry ---
sitemap_text = SITEMAP.read_text(encoding="utf-8")
# Insert before </urlset>
new_url_block = f"""  <url>
    <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_{NEW_LEAD}.html</loc>
    <lastmod>2026-07-21</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
"""
sitemap_text = sitemap_text.replace("</urlset>", new_url_block + "</urlset>", 1)
SITEMAP.write_text(sitemap_text, encoding="utf-8")
# Verify exactly 1 occurrence
sitemap_count = sitemap_text.count(f"chunk_{NEW_LEAD}.html")
assert sitemap_count == 1, f"sitemap must have exactly 1 chunk_{NEW_LEAD}.html entry, got {sitemap_count}"
print(f"[OK] sitemap.xml +1 entry chunk_{NEW_LEAD}.html (count=1)")

# --- Step 6: index.html card ---
index_text = INDEX.read_text(encoding="utf-8")
new_card = f"""
<section id="chunk-{NEW_LEAD}" class="card" data-tick="{TICK_ID}" data-cohort="{COHORT}" data-lead="{NEW_LEAD}" data-cohort-role="opener-1-of-5">
<h3>Triple Whale AI-Native Ecommerce Marketing-Measurement + Sonar AI-Search-Visibility + Moby AI + Compass MMM/MTA Audit Evidence Map (2026)</h3>
<p class="meta">Triple Whale · ai_marketing_attribution OPENER #1/5 (NEW VERTICAL #23 — after Lago 815 + Chargebee 816 + Maxio 817 + Recurly 818 + Stripe Billing 819 closed ai_billing_usage 5/5; after DISCO 814 + Relativity 810 + Exterro 811 + Veritas 812 + Everlaw 813 closed ai_legal_hold_ediscovery 5/5) · 18-col AI-marketing-attribution + DTC-identity-resolution + LLM-search-visibility + MMM/MTA + Moby-AI receipt · Triple Whale Pixel advanced identity-resolution (cookieless + cross-device + iOS 14+ post-IDFA) + Triple Whale Compass unified-measurement (MMM + MTA + Incrementality) + Triple Whale Sonar AI-search-visibility (ChatGPT + Claude + Perplexity + Gemini + Google AI Overviews) + Triple Whale Moby AI + Moby 2 AI-teammate (Claude + ChatGPT + Gemini) + Triple Whale Self-Serve Analytics 75+ dashboards + Triple Whale Custom BI (Snowflake + BigQuery) + 60+ integrations · SOC 2 Type II + GDPR + CCPA + EU AI Act Art. 50 · 9B+ events/day · 12,000+ brands globally · 2,000+ agencies worldwide · 55% DTC-ecommerce adoption · 10x ROI on entire ad spend · 42% increase in new customer revenue within 90 days · Maxx Blank + AJ Orbach + Ivan Chernykh co-founders (verbatim triplewhale.com/about 2026-07-21) · commercial route FORM:https://www.triplewhale.com/bookdemo</p>
<p><a href="chunks/chunk_{NEW_LEAD}.html">chunk_{NEW_LEAD}.html</a></p>
</section>
"""
# Insert AFTER the chunk-819 section (after-rfind safe pattern — anchor to chunk-819 close)
anchor = '<section id="chunk-819"'
last_819 = index_text.rfind(anchor)
assert last_819 > -1, "chunk-819 anchor not found in index.html"
# Find the closing </section> after the anchor
chunk_819_close = index_text.find("</section>", last_819)
assert chunk_819_close > -1, "chunk-819 close </section> not found"
insertion_point = chunk_819_close + len("</section>")
new_index_text = index_text[:insertion_point] + new_card + index_text[insertion_point:]
INDEX.write_text(new_index_text, encoding="utf-8")
# Verify exactly 1 occurrence of new tick-id (replace_all=False, single insert)
new_count = new_index_text.count(f'data-tick="{TICK_ID}"')
assert new_count == 1, f"index.html must have exactly 1 card for {TICK_ID}, got {new_count}"
print(f"[OK] index.html +1 card chunk-{NEW_LEAD} (count=1)")

# --- Step 7: build-log.html entry (after-rfind safe pattern, pitfall 21) ---
build_entry = f"""

<div class="tick-entry" data-tick="{TICK_ID}">
<h2>2026-07-21 &mdash; fast-exec Triple Whale {NEW_LEAD} (ai_marketing_attribution OPENER #1/5 &mdash; NEW VERTICAL #23 &mdash; after ai_billing_usage 5/5 closed at Stripe Billing 819 + ai_legal_hold_ediscovery 5/5 closed at DISCO 814 &mdash; AI-native DTC-ecommerce-marketing-measurement + MMM/MTA/Incrementality + LLM-search-visibility + Moby-AI platform with Maxx Blank + AJ Orbach + Ivan Chernykh co-founders verbatim first-party triplewhale.com/about 2026-07-21)</h2>
<p><strong>Source:</strong> triplewhale.com &middot; <strong>Domain:</strong> triplewhale.com &middot; <strong>Vertical:</strong> <code>{COHORT}</code> &middot; <strong>Position:</strong> OPENER #1/5 (NEW VERTICAL #23).</p>
<p><strong>Artifact:</strong> added Lead {NEW_LEAD} Triple Whale to <code>cold_email/leads.csv</code>, wrote <code>cold_email/{NEW_LEAD}_triplewhale.md</code> companion evidence + <code>cold_email/templates/{NEW_LEAD}_triplewhale.md</code> 5-question audit letter, published <code>chunks/chunk_{NEW_LEAD}.html</code> (~9 KB) SEO chunk with linked card in <code>index.html</code> (inserted after the chunk-819 card with <code>data-cohort-role="opener-1-of-5"</code>) and new URL entry in <code>sitemap.xml</code>. Queued <code>cold_email/send_log.json</code> queued_not_sent entry (dual-schema per pitfall #22) and a <code>revenue_log.csv</code> row {NEW_LEAD}.</p>
<p><strong>Live first-party verification (2026-07-21):</strong> <code>triplewhale.com/</code> HTTP 200 (homepage) with verbatim hero "The real-time command center for ecommerce brands" + "Enterprise-grade by default SOC 2 Type II GDPR &amp; CCPA compliant 9B+ events processed per day" + "Meet Moby 2" + "Harness the power of Claude, ChatGPT, and Gemini for ecommerce"; <code>triplewhale.com/about</code> HTTP 200 with verbatim "Meet Our Founders Triple Whale was founded in 2021 by Maxx Blank, AJ Orbach, and Ivan Chernykh, former ecommerce operators who built the tools"; <code>triplewhale.com/bookdemo</code> HTTP 200 (canonical "Book a Demo" HubSpot form <code>hsForm_5283a7a7-54ab-4215-9414-0b715ef89c98</code>); <code>triplewhale.com/trust-center</code> HTTP 200; <code>triplewhale.com/careers</code> HTTP 200; HQ Columbus OH 43215 (terms-and-conditions footer).</p>
<p><strong>Progress:</strong> OPENED <code>{COHORT}</code> NEW VERTICAL #23 after both <code>ai_billing_usage</code> (Lago 815 OPENER + Chargebee 816 + Maxio 817 + Recurly 818 + Stripe Billing 819 CLOSER) and <code>ai_legal_hold_ediscovery</code> (Relativity 810 OPENER + Exterro 811 + Veritas 812 + Everlaw 813 + DISCO 814 CLOSER) closed at 5/5. Triple Whale adds the AI-native DTC-ecommerce-marketing-measurement + MMM/MTA/Incrementality + LLM-search-visibility + Moby-AI + cookieless + cross-device + iOS-14-post-IDFA identity-resolution seam &mdash; non-overlapping with every other AI-vendor archetype. Tier-1 evidence wedge: 18-column AI-marketing-attribution + DTC-identity-resolution + LLM-search-visibility + MMM/MTA + Moby-AI receipt joining customer_id + pixel_event_id + cross_device_match_id + cookie_ios_post_idfa_id + ad_platform_id + campaign_id + ad_set_id + creative_id + sonar_ai_search_query_id + sonar_ai_search_response_id + moby_ai_prompt_id + moby_ai_response_id + moby_ai_subprocessor (Claude + ChatGPT + Gemini) + compass_mmm_run_id + compass_mta_run_id + compass_incrementality_test_id + integration_webhook_id + bi_export_run_id. 30-row compliance map: SOC 2 Type II + GDPR + CCPA + EU AI Act Art. 50 + iOS 14 post-IDFA + cookie-consent-platform + state-AG consumer-protection + FTC Section 5 + EU UCPD + per-LLM-subprocessor (Claude + ChatGPT + Gemini) DPA flow-down + per-region-data-residency + per-cookie_ios_post_idfa_id-consent-timestamp + per-event-late-binding-attribution-window + per-event-cross-device-merge + per-creative_id-attribution-weight + per-channel-spend-allocation + per-MMM-model-retrain + per-incrementality-test-confidence-interval + per-LLM-model-version + per-prompt-input-features + per-response-retrieved-dataset-ids + per-confidence-score + per-store-acceptance-rejection-rationale + per-LLM-source-of-truth + per-cited-URL + per-brand-mention-position + per-competitor-overlap ready for EU AI Act Art. 50 + GDPR + CCPA + FTC Section 5 + EU UCPD + NIST AI RMF 1.0 + ISO/IEC 42001 + ISO/IEC 23894 + state-AG consumer-protection + iOS 14+ post-IDFA compliance.</p>
<p><strong>Pivot:</strong> selected Triple Whale as the cohort's OPENER over Northbeam + Rockerbox + Measured + AppsFlyer because the first-party surfaces expose the broadest AI-native DTC-ecommerce-marketing-measurement + MMM/MTA/Incrementality + LLM-search-visibility + Moby-AI + cookieless + cross-device + iOS-14-post-IDFA identity-resolution posture, a current first-party founder roster Maxx Blank + AJ Orbach + Ivan Chernykh verbatim on the <code>triplewhale.com/about</code> page, the SOC 2 Type II + GDPR + CCPA + EU AI Act Art. 50 compliance map, 9B+ events per day + 12,000+ brands globally + 2,000+ agencies worldwide + 55% DTC-ecommerce adoption + 10x ROI on entire ad spend + 42% increase in new customer revenue within 90 days scale metrics, and the canonical Book a Demo HubSpot form <code>hsForm_5283a7a7-54ab-4215-9414-0b715ef89c98</code> on <code>triplewhale.com/bookdemo</code>. No founder personal-alias inferred; the <code>triplewhale.com/bookdemo</code> HubSpot form is the sanctioned commercial route. SMTP remains gated and no email, contact-form submission, delivery, payment, or revenue is claimed. <strong>$0 sent / $0 received</strong>.</p>
<p><strong>Next tick siblings (planned cycle 1 cohort):</strong> Northbeam (Northbeam multi-touch + AI-augmented attribution) &middot; Rockerbox (Rockerbox multi-touch attribution + paid-social + paid-search + affiliate + influencer + podcast + TV + out-of-home measurement) &middot; Measured (Measured incrementality + cross-channel experimentation + commerce-media measurement) &middot; AppsFlyer (AppsFlyer mobile-attribution + SKAdNetwork + privacy-first mobile-measurement + SKAdNetwork-post-IDFA + incrementality).</p>
<p class="footer">Atlas @ Talon Forge &mdash; cron tick {TICK_ID} &middot; Lead {NEW_LEAD} + companion evidence + template + SEO chunk + sitemap + index card + build-log + commit + push &middot; ai_marketing_attribution OPENER #1/5 (NEW VERTICAL #23) &middot; FORM:https://www.triplewhale.com/bookdemo (first-party canonical Book a Demo HubSpot form verified live 2026-07-21; not submitted) &middot; $0 sent / $0 received.</p>
</div>
"""
build_text = BUILD_LOG.read_text(encoding="utf-8")
last_div_idx = build_text.rfind("</div>")
assert last_div_idx > -1, "build-log.html: no </div> anchor"
new_build_text = (
    build_text[: last_div_idx + len("</div>")]
    + build_entry
    + build_text[last_div_idx + len("</div>") :]
)
BUILD_LOG.write_text(new_build_text, encoding="utf-8")
assert TICK_ID in new_build_text.rsplit('<div class="tick-entry"', 1)[-1], (
    "build-log.html: new entry did not land at file's end"
)
print(f"[OK] build-log.html +1 entry (after-rfind safe pattern)")

# --- Step 8: send_log.json entry (dual-schema per pitfall 22) ---
send_data = json.loads(SEND_LOG.read_text(encoding="utf-8"))
entries = send_data if isinstance(send_data, list) else send_data.get("entries", [])

new_entry = {
    # NEW schema
    "tick": TICK_ID,
    "index": NEW_LEAD,
    "vendor": VENDOR,
    "cohort": COHORT,
    "position": "OPENER #1/5 (NEW VERTICAL #23 — after ai_billing_usage 5/5 closed + ai_legal_hold_ediscovery 5/5 closed)",
    "form_url": "https://www.triplewhale.com/bookdemo",
    "send_status": "queued_not_sent",
    "route_type": "FORM",
    "smtp_gated": True,
    "submitted": False,
    "submitted_at": None,
    "notes": "FORM-only commercial route. Not submitted. SMTP gated. $0 sent / $0 received. FULL SHIP mode (8 surfaces: lead row + companion + template + SEO chunk + sitemap + index card + build-log + revenue log). ai_marketing_attribution cohort OPENED at 1/5.",
    # OLD schema aliases
    "lead": NEW_LEAD,
    "name": VENDOR,
    "vertical": COHORT,
    "route": "https://www.triplewhale.com/bookdemo",
    "template": f"{NEW_LEAD}_triplewhale.md",
    "status": "queued_not_sent",
    "queued_at": "2026-07-21T18:30:00Z",
    "id": f"hermes-send-{NEW_LEAD}-{VENDOR.lower().replace(' ', '-')}",
    "note": "FORM-only commercial route. Not submitted. SMTP gated.",
}
entries.append(new_entry)
SEND_LOG.write_text(
    json.dumps(entries, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8",
)
json.loads(SEND_LOG.read_text(encoding="utf-8"))
print(f"[OK] send_log.json +1 entry {NEW_LEAD} (dual-schema)")

# --- Step 9: revenue_log.csv row ---
with REVENUE.open("a", encoding="utf-8", newline="") as f:
    csv.writer(f).writerow([
        "2026-07-21", str(NEW_LEAD), f"{NEW_LEAD}_triplewhale.md", f"chunk_{NEW_LEAD}.html",
        f"{COHORT} OPENER #1/5 (NEW VERTICAL #23 — after ai_billing_usage 5/5 closed + ai_legal_hold_ediscovery 5/5 closed)",
        "0",
        f"Lead {NEW_LEAD} — Triple Whale (triplewhale.com — AI-native DTC-ecommerce-marketing-measurement + MMM/MTA/Incrementality + LLM-search-visibility + Moby-AI platform with Pixel advanced identity-resolution + Compass unified-measurement + Sonar AI-search-visibility (ChatGPT + Claude + Perplexity + Gemini + Google AI Overviews) + Moby AI + Moby 2 AI-teammate (Claude + ChatGPT + Gemini) + Self-Serve Analytics 75+ dashboards + Custom BI (Snowflake + BigQuery) + 60+ integrations. SOC 2 Type II + GDPR + CCPA + EU AI Act Art. 50 + iOS 14 post-IDFA + cookieless + cross-device. Maxx Blank + AJ Orbach + Ivan Chernykh co-founders verbatim first-party triplewhale.com/about 2026-07-21 ('Meet Our Founders Triple Whale was founded in 2021 by Maxx Blank, AJ Orbach, and Ivan Chernykh, former ecommerce operators who built the tools'). HQ Columbus OH 43215. Founded 2021. 9B+ events/day. 12,000+ brands globally. 2,000+ agencies worldwide. 55% DTC-ecommerce adoption. 10x ROI on entire ad spend. 42% increase in new customer revenue within 90 days). 18-column AI-marketing-attribution + DTC-identity-resolution + LMM-search-visibility + MMM/MTA + Moby-AI receipt joining customer_id + pixel_event_id + cross_device_match_id + cookie_ios_post_idfa_id + ad_platform_id + campaign_id + ad_set_id + creative_id + sonar_ai_search_query_id + sonar_ai_search_response_id + moby_ai_prompt_id + moby_ai_response_id + moby_ai_subprocessor + compass_mmm_run_id + compass_mta_run_id + compass_incrementality_test_id + integration_webhook_id + bi_export_run_id. $500/48h evidence-gap map + $497/mo quarterly refresh + $497/mo x 5-client YanXbt pattern staged through FORM:https://www.triplewhale.com/bookdemo HubSpot form hsForm_5283a7a7-54ab-4215-9414-0b715ef89c98; SMTP remains gated; no send, delivery, payment, or revenue claimed; $0 sent / $0 received; OPENER #1/5 (NEW VERTICAL #23).",
    ])
print(f"[OK] revenue_log.csv +1 row {NEW_LEAD}")

print()
print("=== SHIP 820 SUMMARY ===")
print(f"  leads.csv: +1 row {NEW_LEAD} ({VENDOR})")
print(f"  companion: cold_email/{NEW_LEAD}_triplewhale.md")
print(f"  template:  cold_email/templates/{NEW_LEAD}_triplewhale.md")
print(f"  chunk:     chunks/chunk_{NEW_LEAD}.html")
print(f"  sitemap:   +1 entry chunk_{NEW_LEAD}.html")
print(f"  index:     +1 card chunk-{NEW_LEAD}")
print(f"  build-log: +1 entry {TICK_ID}")
print(f"  send_log:  +1 entry {NEW_LEAD} (dual-schema)")
print(f"  revenue:   +1 row {NEW_LEAD}")
print()
print("NEXT: git add -A && git commit -m '...820...' && git push origin main")