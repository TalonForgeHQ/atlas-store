#!/usr/bin/env python3
"""Append chunk-646 card to index.html before </html> closing tag.
Shape B variant (pitfall #82): rfind('</html>') instead of '</body>'."""
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
INDEX = REPO / "index.html"

NEW_CARD = """<section id="chunk-646" class="chunk-card" data-tick="2026-07-19-fast-exec-sprinto-650">
  <h3>Sprinto Compliance Automation 650 &mdash; SOC 2 + ISO 27001 + HIPAA + GDPR + PCI DSS + NIST CSF + CMMC + ISO 27701 + MDM Device Monitoring + Doctor Sprinto + Access Control + People Ops + Security Training + EU AI Act Art. 14 Evidence Map</h3>
  <p class="lede">Sprinto is an India-first compliance-automation platform (Bangalore HQ + 2,000+ customers) covering SOC 2 + ISO 27001 + HIPAA + GDPR + PCI DSS + NIST CSF + CMMC + ISO 27701 with Sprinto MDM (device monitoring) + Doctor Sprinto + Access Control + People Ops + Security Training modules. The official About page identifies Girish Redekar and Raghuveer Kancherla as Co-Founder CEOs (both ex-RecruiterBox), with Mohita Nagpal VP Marketing + Sandeepa Samuel VP People & Culture + Chaitanya Goyal Head of Product + Aayush Agarwal VP Strategy + Karthik V VP Solution Engineering and Audits leading the team; <a href="mailto:sales@sprinto.com">sales@sprinto.com</a> is verified live 2026-07-19 via Wayback archive 2024-06-01 of sprinto.com footer Reach Us At section as the canonical prospect/demo/start-trial inbox (tag icon).</p>
  <p>Tier-1 wedge: per-control + per-device-event + per-people-ops-event + per-access-event + per-training-completion + per-framework-version + per-mapping-rule + per-exception + per-remediation evidence schema + Sprinto-AI-output provenance + per-prompt + per-model + per-tool-version + per-incident + per-human-override logging, joined to per-device-timestamp + per-actor-attribute + per-policy-version + per-region attribute schema, mapped to EU AI Act Art. 9 risk-management + 10 data-governance + 11 technical-documentation + 12 logging + 14 human-oversight + 15 accuracy/robustness/cybersecurity + India DPDP Act 2023 dual-mandate. Differentiated from Drata 647 (US-first + 30+ frameworks + $328M Series C + 7,000+ customers) and Scrut 648 (India-first + BFSI focus + 3,000+ customers) and Secureframe 649 (YC-W15 OG-compliance + 100+ integrations + Notion + Atlassian + Quora) because Sprinto owns the DEVICE-MONITORING-DOCTOR + ACCESS-CONTROL-PEOPS-TRAINING-PACK + EX-RECruiterBOX-FOUNDER wedge specifically (the operational-coverage layer that goes beyond compliance-paperwork into device monitoring + people-ops + security training + access-control surface that auditors need to verify when they move from paperwork to people-and-devices). $500/48h evidence-gap map or $497/mo refresh.</p>
  <p class="links"><a href="chunks/chunk_646.html">Read the chunk &rarr;</a> | <a href="cold_email/templates/650_sprinto.md">Email template &rarr;</a> | <a href="mailto:sales@sprinto.com?subject=Atlas%20%E2%80%94%20Sprinto%20%E2%80%94%20Lead%20650">Reply to sales@sprinto.com &rarr;</a></p>
</section>
"""

text = INDEX.read_text(encoding="utf-8")

# Idempotency guard
assert 'id="chunk-646"' not in text, "chunk-646 card already in index.html"
# Shape B probe — find </html> closing tag (pitfall #82 — no </body>)
assert "</html>" in text and "</body>" not in text, "expected Shape B (no </body>, with </html>)"
close_idx = text.rfind("</html>")
assert close_idx > 0, "no </html> in index.html"

# Multi-DOCTYPE concatenation surface — rfind picks the VERY last </html>
# which is the canonical append anchor for this Shape-B atlas-store layout
last_html_close = text.rfind("</html>")
assert last_html_close > 0, f"no </html> in index.html (rfind={last_html_close})"

new_text = text[:last_html_close] + NEW_CARD + text[last_html_close:]

# Verify
assert new_text.count('id="chunk-646"') == 1, "expected exactly 1 chunk-646 anchor"
sales_count = new_text.count("sales@sprinto.com")
assert sales_count >= 2, f"expected >=2 sales@sprinto.com (lede + reply mailto), got {sales_count}"
assert new_text.count("data-tick=\"2026-07-19-fast-exec-sprinto-650\"") == 1, "data-tick anchor count != 1"

INDEX.write_text(new_text, encoding="utf-8")
print(f"[OK] index.html: chunk-646 card inserted before </html> (last_html_close={last_html_close})")
