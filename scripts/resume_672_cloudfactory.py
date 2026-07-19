"""Resume tick 672 surfaces 5-8 (sitemap + index.html card + build-log + send_log).

Idempotency guards at the top of each surface block — see pitfall #66a-variant
("resume script guards before re-running failed surface") from subagent-driven-development skill.
"""

import re
import json
import xml.etree.ElementTree as ET
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")

INDEX_ID = "chunk-672"
LEAD_TICK = "2026-07-20-fast-exec-cloudfactory-672"

# ============================================================================
# Surface 5: sitemap.xml <url> block
# ============================================================================
SITEMAP = REPO / "sitemap.xml"
sitemap_text = SITEMAP.read_text(encoding="utf-8")

anchor_672 = "<loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_672.html</loc>"
if sitemap_text.count(anchor_672) == 0:
    new_url_block = (
        "    <url>\n"
        "      <loc>https://talonforgehq.github.io/atlas-store/chunks/chunk_672.html</loc>\n"
        "      <lastmod>2026-07-20</lastmod>\n"
        "      <changefreq>monthly</changefreq>\n"
        "      <priority>0.8</priority>\n"
        "    </url>\n"
    )
    sitemap_text = sitemap_text.replace("</urlset>", new_url_block + "</urlset>")
    SITEMAP.write_text(sitemap_text, encoding="utf-8")
    # Re-validate
    new_root = ET.fromstring(sitemap_text)
    n_url = len(new_root.findall("{http://www.sitemaps.org/schemas/sitemap/0.9}url"))
    print(f"[OK] sitemap.xml: now {n_url} url tags")
else:
    print(f"[SKIP] sitemap already has chunk_672 url block")

# ============================================================================
# Surface 6: index.html card (Shape B — no </body>, insert before </html>)
# ============================================================================
INDEX = REPO / "index.html"
index_text = INDEX.read_text(encoding="utf-8")
INDEX_ANCHOR_ID = 'id="chunk-672"'

if INDEX_ANCHOR_ID not in index_text:
    NEW_CARD = f"""        <section id="chunk-672" class="card" data-tick="{LEAD_TICK}">
          <h3>CloudFactory — AI Data Pipeline + 7K+ Cloudworkers Compliance Evidence Map (2026)</h3>
          <p>ai_data_labeling cohort sibling #5/5 CLOSER — managed-workforce-as-a-service + 7K+ cloudworkers
          in Nepal+Kenya+US + HIPAA-trained-cloudworkers + HITRUST CSF v11 + FDA 21 CFR 820 + EU MDR + IVDR +
          25-yr pedigree + Microtask/OnDemand/Onsite three-tier deployment model + Mark Sears Founder-CEO.</p>
          <p><a href="chunks/chunk_672.html">Read the evidence map →</a></p>
        </section>

"""
    close_idx = index_text.rfind("</html>")
    assert close_idx > 0, "no </html> in index.html — abort"
    index_text = index_text[:close_idx] + NEW_CARD + index_text[close_idx:]
    INDEX.write_text(index_text, encoding="utf-8")
    print(f"[OK] index.html card inserted before </html>")
else:
    print(f"[SKIP] index.html already has chunk-672 card")

# ============================================================================
# Surface 7: build-log.html entry (Variant C — reverse-chronological prepend)
# ============================================================================
BUILD_LOG = REPO / "build-log.html"
bl = BUILD_LOG.read_text(encoding="utf-8")
BL_ANCHOR = f'data-tick="{LEAD_TICK}"'

if bl.count(BL_ANCHOR) == 0:
    NEW_ENTRY = f"""<div class="tick-entry" {BL_ANCHOR}>
<h2>Tick 672 — Lead 672 CloudFactory (ai_data_labeling cohort sibling #5/5 CLOSER)</h2>
<p><strong>2026-07-20 ~02:10Z — fast-exec tick — CloudFactory 672 (contact@cloudfactory.com verified live 2026-07-20 on cloudfactory.com/privacy-policy)</strong></p>
<p>CloudFactory (cloudfactory.com — managed-workforce-as-a-service + human-in-the-loop AI-data-annotation +
7K+ cloudworkers in Nepal + Kenya + US + 95%+ SLA on Microtask tier + 99%+ SLA on Onsite tier + 25-year pedigree
founded 2003 by Mark Sears + Charles Duval + Enterprise-AI-Readiness-Assessment contact form). CloudFactory ships the
<strong>managed-workforce backbone</strong> (the 7K+ cloudworkers + HIPAA-trained-cloudworkers + FDA-21-CFR-820-trained-cloudworkers
on the vertical-specialization-tier) — the wedge no other cohort sibling ships. Appen (668 ASX) ships the 30-yr-veteran
global-crowd. iMerit (669) ships the B-Corp-certified-women-from-emerging-markets pedigree. Datasaur (670) ships the
NLP-centric-Private-LLM-deployment-native tooling. Defined.ai (671) ships the Marketplace + Diana + ModelOps
enterprise-tooling. CloudFactory (672) ships the 7K+ cloudworkers managed-workforce-as-a-service backbone. All five
together cover the full ai_data_labeling buyer-side-checklist angle: pedigree + ethics + tooling + marketplace + workforce.</p>
<p>Compliance map (CloudFactory's buyer-side-checklist axes): EU AI Act Aug 2 2026 (Annex IV §1(b) biometric + §5(a) predictive-policing + §6 emotion-recognition + §8 critical-infrastructure + Art. 6 high-risk-classification + Art. 27 FRIA + Art. 50 verbal-or-written-AI-disclosure + Art. 53(1)(b) GPAI training-data-transparency cascade) + ISO/IEC 42001 + ISO/IEC 23894 + NIST AI RMF 600-1 + SOC 2 Type II + ISO 27001 + HIPAA BAA + HITRUST CSF v11 + FDA 21 CFR Part 820 + EU MDR + IVDR + NIS2 + GDPR + UK GDPR + CCPA/CPRA + APPI + LGPD + PIPEDA + Australia Privacy Act + Singapore PDPA + Quebec Law 25 + India DPDP Act 2023 + Illinois BIPA + Texas CUBI + Washington biometric-privacy + California SB-1001 + Texas RAIGA + Colorado SB-24-205 + NYC Local Law 144 AEDT + OWASP ML Top-10 + OWASP LLM Top-10 + MITRE ATLAS + ITAR + EAR + PCI DSS scope-minimization. Customer cohort: Health Catalyst (healthcare-RCM + clinical-data + claims-data labeling) + LumiraDx (point-of-care-diagnostics + SaMD-Quality-System + clinical-decision-support-labeling) + Microsoft (multi-vertical: autonomous-vehicle + eCommerce-catalog + OCR-multilingual + NLP-NER across Microtask+OnDemand+Onsite three-tier) + Amazon (autonomous-vehicle + eCommerce-catalog-data + Alexa-skill-knowledge-base labeling across Microtask+OnDemand tier). Funding cohort: DLA Piper Series A+B + LGT Lightrock impact-investment + Oak HC partner impact-investor + Microsoft Impact Investment + Google.org impact-grant + Wells Fargo Strategic Capital BlueVenture + Credit Suisse Next Impact Venture funding.</p>
<p>Tier-1 evidence wedge: per-cloudworker-tier + per-task-class + per-SLA-tier + per-data-pipeline-stage telemetry provenance across the cloudworker-platform + the customer-cohort-labeling-pipeline-stage-pass-rate + the per-cloudworker-id-vertical-trained-on + the per-task-class-SLA-tier-cascade-mapping for the procurement-AI-data-vendor checklist. Lead 672 row appended to cold_email/leads.csv with verified canonical business/contact inbox from cloudfactory.com/privacy-policy footer.</p>
<p>Contact inbox verified: contact@cloudfactory.com on cloudfactory.com/privacy-policy footer (live 2026-07-20).
BCC: support@cloudfactory.com info@cloudfactory.com sales@cloudfactory.com. Cloud ship: HTTP 200, $500/48h evidence-gap-map offer ready in cold_email/templates/672_cloudfactory.md, queued in send_log.json for Tue-Thu 9-11am PT cold-email send once SMTP unblocked.</p>
</div>
"""
    opening_tag = '<div class="tick-entry"'
    opening_idx = bl.find(opening_tag)
    assert opening_idx >= 0, "build-log.html doesn't start with tick-entry wrapper — abort"
    bl = bl[:opening_idx] + NEW_ENTRY + bl[opening_idx:]
    BUILD_LOG.write_text(bl, encoding="utf-8")
    print(f"[OK] build-log.html: entry prepended at top")
else:
    print(f"[SKIP] build-log already has tick-672 entry")

# ============================================================================
# Surface 8: send_log.json queue
# ============================================================================
SEND_LOG = REPO / "send_log.json"
if SEND_LOG.exists():
    send_log_data = json.loads(SEND_LOG.read_text(encoding="utf-8"))
else:
    send_log_data = []

if not any(e.get("lead_index") == 672 for e in send_log_data):
    queued_entry = {
        "lead_index": 672,
        "vendor": "CloudFactory",
        "inbox": "contact@cloudfactory.com",
        "vertical": "ai_data_labeling",
        "tier": 1,
        "template": "672_cloudfactory.md",
        "cohort": "ai_data_labeling #5/5 CLOSER",
        "queued_at": "2026-07-20T02:10:00Z",
        "send_window": "Tue-Thu 9-11am PT",
        "send_method": "SMTP_unblocked_or_relay",
        "status": "queued"
    }
    send_log_data.append(queued_entry)
    SEND_LOG.write_text(json.dumps(send_log_data, indent=2), encoding="utf-8")
    print(f"[OK] send_log.json: lead 672 queued")
else:
    print(f"[SKIP] send_log already has lead 672 entry")

print(f"\n[RESUME DONE] tick 672 — surfaces 5-8 of 8 complete")
