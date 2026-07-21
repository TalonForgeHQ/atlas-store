import csv, json

# build-log
with open('build-log.html','r',encoding='utf-8') as f:
    txt = f.read()
entry = '''
<div class="tick-entry" data-tick="2026-07-21-fast-exec-dreamdata-823" data-cohort="ai_marketing_attribution" data-lead="823">

## Tick 823 — Dreamdata (ai_marketing_attribution sibling #4/5) + 822 catch-up card

**Time:** 2026-07-21 ~16:50 UTC
**Mode:** FULL SHIP (5 surfaces) — lead row + companion evidence + template + SEO chunk + build-log entry + sitemap + index card + revenue_log + send_log queued_not_sent entry.
**Tick id:** `2026-07-21-fast-exec-dreamdata-823`

**SHIP:** lead 823 Dreamdata (ai_marketing_attribution sibling #4/5 after Triple Whale 820 OPENER + AppsFlyer 821 sibling #2/5 + Wicked Reports 822 sibling #3/5) — dreamdata.com B2B revenue-attribution + buyer-journey + account-level MMM + per-source-ROI + Reveal account-level intent + Reveal buyer-journey playback + Act push to HubSpot/Salesforce/Slack + Dreamdata Lens content-velocity + 60+ ad-platform + CRM + CSP integrations. CEO Nick Turner + CPO &amp; Co-founder Lars Grønnegaard + CMO &amp; Co-founder Steffen Hedebrandt + COO Peter Egehoved + CTO James Dietrich (verbatim first-party dreamdata.com/about Squarespace 2026-07-21). HQ 39 Kalvebod Brygge 1560 Copenhagen Denmark + NY office 535 8th Avenue 12th Floor. CVR 39855224. $55M Series B. SOC 2 Type II + GDPR + UK GDPR + CCPA/CPRA + EU AI Act Art. 50 + ISO 27001 (in progress) + Danish Data Protection Act. Commercial route mailto:friends@dreamdata.io + FORM:https://www.dreamdata.com/demo + FORM:https://www.dreamdata.com/book-demo (all first-party, verified live 2026-07-21). 16-col B2B-revenue-attribution + buyer-journey + account-level MMM receipt (account_id + account_external_id + account_domain + buyer_journey_id + buyer_journey_touchpoint_id + touchpoint_timestamp + touchpoint_source + touchpoint_medium + touchpoint_campaign + touchpoint_ad_platform + touchpoint_ad_id + touchpoint_creative_id + touchpoint_user_id + touchpoint_user_email_hash + touchpoint_identified_at_timestamp + revenue_attributed_amount + revenue_attributed_currency + deal_id + deal_close_timestamp + ARR_recognized_period + ad_spend_amount + ad_spend_currency + per-source-ROI-score).

**DIFFERENTIATION vs prior siblings:** vs Triple Whale 820 (Triple Whale is DTC-ecommerce + Shopify + Moby AI ecommerce-trained + Sonar AI-search visibility — B2C-DTC-leaning; Dreamdata is B2B-SaaS + HubSpot/Salesforce/CRM-native + account-level + buyer-journey — B2B-leaning); vs AppsFlyer 821 (AppsFlyer is mobile + cross-device + post-IDFA + deep-linking + in-app — mobile-DTC + mobile-B2B gaming-leaning; Dreamdata is B2B-web + CRM-native + account-level + buyer-journey — B2B-web-leaning); vs Wicked Reports 822 (Wicked Reports is info-products + email-attribution + MMM + Halo + Time Machine + Signal Action — B2C-DTC-info-products-leaning; Dreamdata is B2B-SaaS + multi-touch + CRM-native — B2B-SaaS-leaning). Dreamdata is the only sibling in the cohort that ships the 16-column B2B-revenue-attribution + account-level buyer-journey + CRM-native cascade as first-party, integrated, per-account-journey-replayable, per-touchpoint-identification-confirmable, per-cross-tenant-no-bleed.

**CATCH-UP:** also added the chunk-822 Wicked Reports card to index.html (the previous tick 822 added the lead row + template + companion but not the index card, and not the SEO chunk); the chunk_822.html itself is still deferred (next-tick will write the SEO chunk for Wicked Reports 822 if cohort-fill continues). The sitemap.xml is now updated to 505 entries (added chunk_822 + chunk_823). The Dreamdata 823 surfaces are complete: lead row + companion evidence + template + SEO chunk + index card + sitemap + build-log + revenue log + send_log queued_not_sent.

**STATE:** `ai_marketing_attribution` cohort 4/5 SHIPPED (Triple Whale 820 OPENER + AppsFlyer 821 sibling #2/5 + Wicked Reports 822 sibling #3/5 + Dreamdata 823 sibling #4/5); 1 OPEN slot remaining: CLOSER #5/5 (public-company control surface — Nielsen Catalina Solutions or The Trade Desk or LiveRamp or DoubleVerify post-Rockerbox acquisition). $0 sent / $0 received (SMTP remains gated).

</div>
'''
if 'data-tick="2026-07-21-fast-exec-dreamdata-823"' not in txt:
    txt = txt.replace('</body>', entry + '</body>')
    with open('build-log.html','w',encoding='utf-8') as f:
        f.write(txt)
    print('build-log appended. new size:', len(txt))
else:
    print('already present')

# revenue_log
row = ['2026-07-21','823','823_dreamdata.md','chunk_823.html',
       'ai_marketing_attribution sibling #4/5 (after Triple Whale 820 OPENER + AppsFlyer 821 sibling #2/5 + Wicked Reports 822 sibling #3/5)','0',
       'Lead 823 — Dreamdata (dreamdata.com B2B revenue-attribution + buyer-journey + account-level MMM + per-source-ROI + Reveal + Dreamdata Lens + 60+ integrations. CEO Nick Turner + CPO/co-founder Lars Gronnegaard + CMO/co-founder Steffen Hedebrandt + COO Peter Egehoved + CTO James Dietrich verbatim first-party dreamdata.com/about 2026-07-21. HQ Copenhagen 39 Kalvebod Brygge + NY 535 8th Avenue. CVR 39855224 founded 2019. $55M Series B. SOC 2 Type II + GDPR + UK GDPR + CCPA/CPRA + EU AI Act Art. 50 + ISO 27001 + Danish DPA. Commercial route mailto:friends@dreamdata.io + FORM:dreamdata.com/demo + FORM:dreamdata.com/book-demo. 16-col B2B-revenue-attribution receipt. $500/48h evidence-gap map + $497/mo quarterly refresh + $497/mo x 5-client YanXbt. SMTP gated; no send, no revenue; sibling #4/5).']
with open('cold_email/revenue_log.csv','a',encoding='utf-8',newline='') as f:
    w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    w.writerow(row)
print('revenue_log appended')

# send_log
entry2 = {'ts':'2026-07-21T16:50:00Z','lead':'823','name':'Dreamdata','vertical':'ai_marketing_attribution',
         'route':'mailto:friends@dreamdata.io + FORM:https://www.dreamdata.com/demo + FORM:https://www.dreamdata.com/book-demo',
         'status':'queued_not_sent','reason':'SMTP gated; no send, no delivery, no payment, no revenue claimed'}
try:
    with open('cold_email/send_log.json','r',encoding='utf-8') as f:
        d = json.load(f)
    if not isinstance(d, list):
        d = [d]
except Exception:
    d = []
d.append(entry2)
with open('cold_email/send_log.json','w',encoding='utf-8') as f:
    json.dump(d, f, indent=2)
print('send_log appended, total entries:', len(d))
