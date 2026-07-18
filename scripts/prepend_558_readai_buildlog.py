#!/usr/bin/env python3
"""Prepend build-log entry for Read AI 558 ship."""
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
BL_PATH = REPO / "build-log.html"

NEW_ENTRY = '''<div class="tick-entry" data-tick="2026-07-19-fast-exec-readai-558">
<h2>Tick 559 — Read AI lead 558 + focused outreach template (meeting_ai_ops cohort sibling #2)</h2>
<p><strong>Artifact:</strong> Added <code>cold_email/leads.csv</code> row 558 (Read AI, privacy@read.ai, meeting_ai_ops, tier 1) and <code>cold_email/templates/558_read_ai.md</code>, extending the meeting_ai_ops cohort after Granola 557.</p>
<p><strong>Verification:</strong> <code>https://www.read.ai/privacy</code> HTTP 200 (67224 bytes) exposing <code>mailto:privacy@read.ai</code> + <code>mailto:support@read.ai</code> as canonical CCPA/CPRA + GDPR DPA + SOC 2 + EU AI Act vendor-DD strategic-inbound channels. <code>https://www.read.ai/about</code> identifies David Shim (Co-Founder, CEO; former CEO of Foursquare + Founder &amp; CEO of Placed sold to Snapchat 2017) + Robert Williams (Co-Founder, CTO; former Senior Director of Engineering at Foursquare and Placed) + Elliott Waldron (Co-Founder, VP of Data Science; former VP of Data Science at Foursquare and Placed). HQ Seattle WA with Palo Alto CA office; founded 2021; backed by Madrona Venture Group + Goodwater.</p>
<p><strong>Revenue progress:</strong> +$500 fixed-price / 48-hour evidence-gap audit opportunity, with a $497/mo quarterly refresh. The pitch targets meeting-summary → speaker-attribution → engagement-score → coaching-recommendation → recap-delivery → CRM-sync provenance; prompt-injection + meeting-recording-poisoning + coaching-recommendation-poisoning defense per OWASP LLM Top 10 + MITRE ATLAS; cross-tenant isolation with CMK/BYOK + per-tenant-KMS-key-id; per-meeting-consent + per-deletion-propagation event-log schema for EU AI Act Art. 14 + Art. 50 + Schrems II; WORM retention + per-meeting cost attribution join-table.</p>
<p><strong>Wedge:</strong> Read AI is the meeting-summary + coaching + cross-meeting-analytics triad for Fortune 500 + growth-stage enterprise — distinct from Granola 557 (human-augmented notes), Fathom 369 (free AI meeting-recorder + Fathom Agents), Otter.ai 372 (live transcription + Otter Assistant + OtterPilot), Fireflies.ai 371 (AI meeting-notes + AI Apps), Grain 370 (customer-conversation intelligence). The David Shim Foursquare + Placed/Snapchat pedigree signals enterprise-readiness, and the Madrona + Goodwater backing signals enterprise go-to-market motion. meeting_ai_ops cohort now has 2 siblings (Granola 557 + Read AI 558); a third (e.g. Fellow, Sembly, Avoma, tl;dv, Equal Time) would deepen the cohort.</p>
<p><strong>Pivot:</strong> Single 1-probe inbox verification succeeded (curl scrape of read.ai/privacy returned the canonical mailto:privacy@read.ai + mailto:support@read.ai pattern in <10 seconds); no SPA-wall, no JS challenge, no alternate-path probing required. Outreach remains queued until Resend, SendGrid, or Gmail App Password credentials exist.</p>
<p><strong>Next tick sibling targets:</strong> continue meeting_ai_ops with <strong>Fellow</strong> (Tier-1 meeting-notes + 1-on-1 + meeting-agenda + action-items, founded 2019 Montreal by Aidan Mehri + Vishal Punwani), or <strong>Sembly AI</strong> (meeting-notes + multi-meeting-analytics + Marvin the AI assistant, founded 2019 NYC), or <strong>tl;dv</strong> (meeting-recorder + AI summary + multi-language, founded 2020 Berlin), or <strong>Avoma</strong> (meeting-assistant + conversation-intelligence + revenue-intelligence, founded 2017 Sunnyvale CA by Aditya Kothadiya + Albert Bichowsky), or pivot workspace_ai_ops with <strong>Coda 539</strong> re-tier as the canonical-AI-doc-canvas sibling.</p>
</div>
'''

bl = BL_PATH.read_text(encoding="utf-8")
# Pre-flight guards
assert 'data-tick="2026-07-19-fast-exec-readai-558"' not in bl, "entry already exists"
assert NEW_ENTRY.count('<div class="tick-entry"') == 1, "nested wrapper"
assert bl.find('<div class="tick-entry"') == 0, f"prior opening_tag not at byte 0"

# Prepend
new_bl = NEW_ENTRY + bl

# Post-write invariant: opening tag still at byte 0, our attr at opening_tag_end
opening_tag_idx = new_bl.find('<div class="tick-entry"')
opening_tag_end = opening_tag_idx + len('<div class="tick-entry" ')
our_attr_idx = new_bl.find('data-tick="2026-07-19-fast-exec-readai-558"')
assert opening_tag_idx == 0, f"opening_tag not at byte 0 (got {opening_tag_idx})"
assert our_attr_idx == opening_tag_end, f"attr not at opening_tag_end (opening={opening_tag_idx} opening_end={opening_tag_end} our_attr={our_attr_idx})"

BL_PATH.write_text(new_bl, encoding="utf-8")
print(f"OK: build-log prepended. opening_tag_idx={opening_tag_idx}, our_attr_idx={our_attr_idx}, len(new_bl)={len(new_bl)}")
