#!/usr/bin/env python3
"""Insert chunk-304 summary card into index.html, anchored on unique end-of-file."""
INDEX = r"C:\Users\Potts\projects\atlas-store\index.html"
TICK_ID = "2026-07-17-fast-exec-synthesia-485"
LEAD = "485"
COHORT = "synthesia-ai-avatar-voice-clone-deepfake-defense-eu-ai-act-fcc-tcpa-bipa"

NEW_CARD = (
    '<section id="chunk-304" class="seo-chunk" data-vertical="synthetic_media" '
    f'data-lead="{LEAD}" data-tick="{TICK_ID}" data-cohort="{COHORT}">\n'
    '<article>\n'
    '<h2>Synthesia AI Avatar Voice Clone Vendor Audit 2026</h2>\n'
    '<p>Buyer checklist for Synthesia AI avatar and voice-clone platforms: '
    'per-render provenance (avatar_id + voice_clone_id + ai_script_id + ai_translation_id + '
    'render_job_id + tenant_id), voice-clone consent lineage (FCC TCPA + BIPA + GDPR Art. 9 + '
    'Illinois AI Video Interview Act), deepfake-misuse defense, cross-tenant render isolation, '
    'C2PA Content Credentials per-render watermark, and 12-state AI-presenter disclosure '
    '(CA SB 1001 + CO SB 24-205 + IL AI Video Interview Act + TX + NY + 7 others) + EU AI Act '
    'Art. 12/14/50/53 evidence. <a href="chunks/chunk_304.html">Read the full chunk 304 '
    'audit lane.</a></p>\n'
    '</article>\n'
    '</section>\n'
)


def main() -> None:
    with open(INDEX, encoding="utf-8") as f:
        text = f.read()

    # Insert before </html>; unique anchor in well-formed HTML
    anchor = "</html>"
    idx = text.rfind(anchor)
    assert idx > 0, "no </html> anchor"
    new_text = text[:idx] + NEW_CARD + text[idx:]

    with open(INDEX, "w", encoding="utf-8") as f:
        f.write(new_text)

    # parse-back verify
    with open(INDEX, encoding="utf-8") as f:
        again = f.read()
    assert again.count('id="chunk-304"') == 1, "chunk-304 anchor not unique"
    assert again.count('<section id="chunk-304"') == 1, "chunk-304 section count off"
    assert "synthetic_media" in again
    assert "Synthesia" in again
    assert "deepfake" in again.lower()
    print(f"OK: chunk-304 card inserted; index.html size {len(again):,} bytes")


if __name__ == "__main__":
    main()