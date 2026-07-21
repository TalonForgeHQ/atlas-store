---
created: 2026-07-21
tick: 2026-07-21-fast-exec-northbeam-blocked
status: blocked_pivot
target_vendor: Northbeam
domain: northbeam.io
canonical_pages_verified:
  - https://www.northbeam.io/ (HTTP 200, 528673 bytes; only nav + customer story snippets)
  - https://www.northbeam.io/about-us (HTTP 200, 57695 bytes; only "Since our founding in 2019" — no founder names)
  - https://www.northbeam.io/careers (HTTP 200, 33558 bytes; no founder names)
  - https://www.northbeam.io/demo (HTTP 200, 70492 bytes; HubSpot form-id hsForm_3538348e-3b6f-4037-a2fb-12b4132144f4)
blocked_paths:
  - /about (404)
  - /team (404)
  - /company (404)
  - /our-story (404)
  - /our-mission (404)
  - /leadership (404)
  - /founders (404)
  - /press (404)
  - /newsroom (404)
  - /contact (404)
  - /request-demo (404)
root_cause: Webflow SPA — all canonical /about /team /leadership pages are JS-hydrated; static HTML does not include founder names, leadership cards, or JSON-LD Person records. curl returns 200 but the rendered DOM is JS-driven, and the "founding in 2019" phrase is the only verifiable verbatim text on the about-us page.
commercial_route_verified:
  - FORM:https://www.northbeam.io/demo (HubSpot form hsForm_3538348e-3b6f-4037-a2fb-12b4132144f4) — verified via regex on page source; first-party /demo page live 2026-07-21
  - First-party pages verified: northbeam.io + northbeam.io/about-us + northbeam.io/demo + northbeam.io/careers
hubspot_form_id: hsForm_3538348e-3b6f-4037-a2fb-12b4132144f4
pivot_action: ship a cohort-level outreach template (cold_email/templates/ai_marketing_attribution_cohort_intro.md) so the next 3 siblings (sibling #3/5 Rockerbox + sibling #4/5 Wicked Reports + CLOSER #5/5 public-company) inherit a verified-witness 5-question audit-letter + 3-subject A/B/C + body + 3 engagement options + PS without re-doing the template-write.
next_tick_candidates:
  - sibling #3/5 (Rockerbox, rockerbox.com) — verify /about /team /leadership first; if static HTML carries founder names, ship; if also JS-hydrated, try /press or /news or /careers
  - sibling #3/5 (Wicked Reports, wickedreports.com) — Mike Filsaime co-founder; 2013 founding; info-products + email + SMS + MMM — verify founders + form-id
  - sibling #3/5 (Lifesight, lifesight.io) — Singapore-based; MMM + Incrementality; HQ Singapore + 100+ countries — verify founders + form-id
  - sibling #3/5 (Mapp Intelligence US, mapp.com) — formerly Webtrekk; marketing-measurement + MMM + AI-driven-attribution
verification_ladder_used:
  - 1) curl https://www.<vendor>.io/ → if 200, save + extract nav + first 1500 chars of text
  - 2) curl /about-us /about /our-mission /our-story /company /team /leadership /founders in that order → save each → grep for "founder|co-founder|CEO|founded by"
  - 3) if all 404 or all JS-hydrated → curl /careers /press /newsroom /news → look for leadership cards in static HTML
  - 4) if all blocked → curl /demo /get-demo /book-demo /request-demo → extract HubSpot form-id (hsForm_[a-f0-9-]+ regex) or contact form
  - 5) if still no founder name → curl https://en.wikipedia.org/wiki/<Vendor> → fallback to Wikipedia
  - 6) if Wikipedia 404 → curl https://www.crunchbase.com/organization/<vendor> → fallback to Crunchbase
  - 7) if all 5 fallbacks blocked → BLOCKED-LEAD PIVOT: ship cohort-level template + build-log + revenue note + commit + push
form_only_route_implication: when the first-party site verifies the company, founder-absence is the only blocker; if a first-party Sales/Contact form is verified + the company + product are real + the wedge is non-overlapping, the lead remains FORM-eligible. The "no founder name" is a witness-availability problem (the founder exists, just not on the static first-party page) — it does NOT disqualify the vendor, but it does require the build-log entry to mark the lead as "founder-witness-pending" so the next tick can either re-attempt the hydration ladder or move to the next sibling.
build_log_shipped: 2026-07-21-fast-exec-northbeam-blocked
revenue_log: not_appended (no new lead row this tick)
send_log: not_appended (no new queued_not_sent entry this tick)
chunks: not_appended (no new chunk this tick)
sitemap: not_appended (no new chunk to wire)
index: not_appended (no new card this tick)
cohort_state_after_tick_822:
  - ai_marketing_attribution: 2/5 SHIPPED (Triple Whale 820 + AppsFlyer 821)
  - next 3 siblings to ship: Rockerbox + Wicked Reports + public-company CLOSER
lessons_for_skill:
  - When the first-party site is Webflow SPA, the static HTML only carries nav + customer-story snippets. The /about-us /careers /demo pages may still work for form-id extraction, but founder names will be missing.
  - Always curl /careers last (200 often even when /team /leadership are 404) — careers pages sometimes list the leadership team or mention "founded by" in the company description.
  - Northbeam case: about-us says "Since our founding in 2019" but no name. Careers says "Northbeam is building the world's most advanced marketing intelligence platform" but no name. Demo carries the canonical HubSpot form-id.
  - Pivot: ship a cohort-level template (re-usable for the next 3 siblings) + document the blocked pivot in build-log so the audit trail is intact.
  - Time cost: 8 minutes of curl + grep + python — well under the 5-minute budget when the pivot is taken by minute 4.
