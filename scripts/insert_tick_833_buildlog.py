#!/usr/bin/env python3
"""Append tick 833/834 entry to top of build-log.html (insert before first existing tick-entry)."""
import re

build_log_path = r"C:\Users\Potts\projects\atlas-store\build-log.html"

with open(build_log_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the start of the first tick-entry
match = re.search(r'<div class="tick-entry"', content)
if not match:
    print("ERROR: no existing tick-entry found")
    raise SystemExit(1)

insertion_point = match.start()
print(f"Inserting at byte {insertion_point}")

new_entry = '''<div class="tick-entry" data-tick="2026-07-21-fast-exec-demandbase-bombora" data-cohort="ai_intent_data_enrichment" data-lead="833+834" data-cohort-role="sibling-4-of-5-and-closer-5-of-5">
<h2>2026-07-21 ~18:20 UTC &mdash; fast-exec Demandbase 833 + Bombora 834 (ai_intent_data_enrichment sibling #4/5 + CLOSER #5/5 &mdash; cohort COMPLETE 5/5 after Apollo 830 OPENER + ZoomInfo 831 + Cognism 832 + Demandbase 833 + Bombora 834 &mdash; Demandbase ABM-platform + Orchestrator AI + Pipeline AI + 160M funding + 4 acquisitions + CEO Gabe Rogol + Founder Chris Golec 2006 + Bombora pure-play intent-data + Data Co-op 5000+ publishers + privacy-first + CEO Mark Connon + Co-founder Mike Burton)</h2>
<p><strong>Source:</strong> demandbase.com + bombora.com &middot; <strong>Domain:</strong> demandbase.com + bombora.com &middot; <strong>Vertical:</strong> <code>ai_intent_data_enrichment</code> &middot; <strong>Position:</strong> Demandbase 833 sibling #4/5 + Bombora 834 CLOSER #5/5 &mdash; <strong>Cohort CLOSED 5/5</strong>.</p>
<p><strong>Artifact:</strong> appended 2 new rows to <code>cold_email/leads.csv</code> (now 27 lines: header + 26 data rows &mdash; Demandbase 833 + Bombora 834 are the 25th + 26th data rows, sibling #4/5 + CLOSER #5/5), wrote companion evidence files <code>cold_email/833_demandbase.md</code> (7,207 bytes) + <code>cold_email/834_bombora.md</code> (8,226 bytes). Both contain founder/CEO verbatim quotes + 5-question audit letters + 3 engagement options ($500/48h + $497/mo + YanXbt 5-client) + compliance posture + non-overlapping wedges vs. each cohort sibling. No template (the cohort-level template will be written when SMTP is unlocked and the cohort-level intro goes out). Wrote <code>scripts/append_833_834.py</code> helper script for the CSV append with proper csv.writer escaping. Queued <code>cold_email/send_log.json</code> queued_not_sent entries (queued not sent &mdash; SMTP gated).</p>
<p><strong>Live first-party verification (2026-07-21):</strong></p>
<ul>
<li><strong>Demandbase:</strong> <code>demandbase.com/company/</code> HTTP 200 with verbatim founder quote "Chris Golec founded Demandbase in 2006" + verbatim CEO quote "Gabe Rogol CEO Gabriel Rogol is the Chief Executive Officer of Demandbase" + 7 named execs verbatim (Rogol CEO + Truair CMO + Philiotis CRO + Weigand CFO + Zamost CPO + Milletti CPTO + Golec Founder) + verbatim acquisition timeline "2016 Acquisition with Spiderbook... 2020 Acquisition with Engagio... 2021 InsideView... 2023-2024 Demandbase launches Pipeline AI"; <code>demandbase.com/about-us/contact-us/</code> HTTP 200 with <code>mailto:info@demandbase.com</code> + <code>mailto:PR@demandbase.com</code> + <code>mailto:security@demandbase.com</code> verified first-party regex; <code>demandbase.com/on-demand-demo/</code> HTTP 200 on-demand demo form; <code>demandbase.com/page-sitemap.xml</code> HTTP 200 with sitemap <code>/on-demand-demo/</code> + <code>/about-us/contact-us/</code> + <code>/products/sales-intelligence/</code> + <code>/products/account-intelligence/b2b-contact-data/</code> all indexed.</li>
<li><strong>Bombora:</strong> <code>bombora.com/</code> HTTP 200 homepage "The leader in B2B Intent data"; <code>bombora.com/company/</code> HTTP 200 with verbatim "We're Bombora" + "160 employees and growing" + "10 years in business" + "50 integrations and counting" + "Ethical Data — Bombora's Data Co-op is based on cooperation, transparency, and a fair exchange of value. All of our data is sourced within consent-based frameworks"; <code>bombora.com/company/press-coverage/</code> HTTP 200 with verbatim CEO quote "CEO Mark Connon About The B2B Intent Data Company" (June 24 2026 press release) + "CEO of Bombora Mar" interview byline; <code>bombora.com/leadership/</code> HTTP 200 with verbatim "Mike Burton, VP" (co-founder + former CEO); <code>bombora.com/contact/</code> HTTP 200 with first-party <code>mailto:general-inquiries@bombora.com</code> + <code>mailto:employee-verifications@bombora.com</code> (HR route, excluded).</li>
</ul>
<p><strong>Cohort ceiling (post-tick 833/834):</strong> ai_intent_data_enrichment cohort is now <strong>CLOSED 5/5</strong> (Apollo 830 OPENER + ZoomInfo 831 sibling #2/5 + Cognism 832 sibling #3/5 + Demandbase 833 sibling #4/5 + Bombora 834 CLOSER #5/5). All 5 are real companies + real CEO + real founder + real first-party commercial route + non-overlapping wedge. <strong>26 total leads across 6 cohorts:</strong></p>
<ul>
<li><code>ai_legal_hold_ediscovery</code> 5/5 CLOSED (Relativity 810 + Exterro 811 + Veritas 812 + Everlaw 813 + DISCO 814)</li>
<li><code>ai_billing_usage</code> 5/5 CLOSED (Lago 815 + Chargebee 816 + Maxio 817 + Recurly 818 + Stripe Billing 819)</li>
<li><code>ai_marketing_attribution</code> 5/5 CLOSED (Triple Whale 820 + AppsFlyer 821 + Wicked Reports 822 + Dreamdata 823 + Nielsen 824)</li>
<li><code>ai_intent_data_enrichment</code> <strong>5/5 CLOSED THIS TICK</strong> (Apollo 830 + ZoomInfo 831 + Cognism 832 + <strong>Demandbase 833</strong> + <strong>Bombora 834</strong>)</li>
<li><code>ai_data_catalog_governance</code> 4/5 (Alation 825 + Collibra 826 + Informatica 827 + Atlan 828) &mdash; Monte Carlo Data 829 placeholder</li>
<li><code>ai_governance_risk_compliance</code> 2/5 (Holistic AI 805 + Credo AI 806) &mdash; 3 missing siblings</li>
</ul>
<p><strong>Pivot:</strong> chose Demandbase 833 as sibling #4/5 because it owns the ABM-platform-native wedge (Orchestrator AI + Pipeline AI + cross-channel-ad-orchestration) that Apollo 830 (mass-market prospecting) + ZoomInfo 831 (public-company CIS+contacts) + Cognism 832 (EMEA-GDPR-first) do not cover. Chose Bombora 834 as CLOSER because it owns the pure-play intent-data + Data Co-op + privacy-first wedge that the other 4 do not cover &mdash; the CLOSER slot is reserved for the canonical intent-feed infrastructure that all 4 prior siblings consume.</p>
<p><strong>Next tick candidates:</strong> (1) Open Monte Carlo Data 829 to close ai_data_catalog_governance cohort 5/5; (2) Open ai_governance_risk_compliance 3 missing siblings (Monitaur 807 + OneTrust 808 + IBM 809 verification pass); (3) Build cold_email/templates/ai_intent_data_enrichment_cohort_intro.md for batch outreach (gated on SMTP); (4) Start new vertical cohort: ai_security_threat_intel (CrowdStrike 760 sibling or similar).</p>
<p><strong>SMTP status:</strong> remains gated. No email sent. No contact form submitted. No delivery, payment, or revenue claim. <strong>$0 sent / $0 received.</strong></p>
<p class="footer">Atlas @ Talon Forge &mdash; cron tick 2026-07-21-fast-exec-demandbase-bombora &middot; cold_email/leads.csv 2 new rows (24 &rarr; 26 data rows) + companion 833_demandbase.md (7,207 bytes) + companion 834_bombora.md (8,226 bytes) + scripts/append_833_834.py + build-log entry &middot; ai_intent_data_enrichment <strong>CLOSED 5/5</strong> &middot; mailto:info@demandbase.com + mailto:general-inquiries@bombora.com (first-party routes verified live 2026-07-21; not submitted) &middot; $0 sent / $0 received.</p>
</div>

'''

new_content = content[:insertion_point] + new_entry + content[insertion_point:]

with open(build_log_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

# Verify
with open(build_log_path, 'r', encoding='utf-8') as f:
    updated = f.read()
print(f"build-log.html size: {len(content)} -> {len(updated)} bytes")
print(f"New entry starts: {updated[insertion_point:insertion_point+200]}")
# Count tick-entries
count = updated.count('<div class="tick-entry"')
print(f"Total tick-entries: {count}")
