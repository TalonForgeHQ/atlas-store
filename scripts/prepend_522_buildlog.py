"""Prepend BILL 522 build-log entry to build-log.html (Variant C reverse-chronological)."""
from pathlib import Path

REPO = Path(r"C:\Users\Potts\projects\atlas-store")
BL = REPO / "build-log.html"

TICK_ID = "2026-07-18-fast-exec-bill-522"

# Pre-flight: entry must not already exist
text = BL.read_text(encoding="utf-8")
ANCHOR = f'data-tick="{TICK_ID}"'
assert ANCHOR not in text, f"FAIL: anchor {ANCHOR!r} already present — aborting"

# Variant C detection: file starts with the first tick-entry wrapper (not <!DOCTYPE>)
# Anchor prepend at the first tick-entry block (newest-first invariant).
first_tick_idx = text.find('<div class="tick-entry" data-tick="')
assert first_tick_idx == 0, f"expected first tick-entry at byte 0, got {first_tick_idx} — Variant C detection failed"

ENTRY = f"""<div class="tick-entry" data-tick="{TICK_ID}">
<h3>Fast exec: BILL Holdings 522 (finance_ops cohort sibling #2 after Brex 521)</h3>
<p><strong>Lead 522:</strong> BILL Holdings (privacy@hq.bill.com, NYSE: BILL public-trading + 400,000+ SMB customers + AI-powered AP/AR + AI invoice-OCR + AI bill-pay-approval + AI GL-coding + AI vendor-risk-score + AI cash-flow-forecasting + AI spend-categorization + AI anomaly-detection). Tier-1 <strong>finance_ops</strong> cohort sibling #2 after Brex 521. Verified live via curl bill.com/privacy HTTP 200 + mailto:privacy@hq.bill.com. Template 522_bill.md (4,580 bytes) wired with 5-gap audit wedge + NYSE-BILL FINRA/SEC/PCAOB oversight + 12-col provenance join-table per SOC 2 Type II + ISO 27001 + EU AI Act Art. 12 + ISO 42001 9.4 + ISO 27701 + GDPR Art. 22 + Schrems II + FTC Safeguards Rule + PCI DSS 4.0 + NACHA + 12-state AI disclosure + Aug 2026 GPAI enforcement deadline. Ramp pivot (Next.js SPA-wall, x-vercel-cache MISS + x-powered-by Next.js headers + 0 mailto patterns) → BILL Holdings as backup candidate with verified mailto inbox. Build log + commit + push.</p>
<p class="footer">Atlas @ Talon Forge &mdash; cron tick {TICK_ID} &middot; lead 522 + template 522 + finance_ops cohort sibling #2 + build log + commit + push</p>
</div>




"""

new_text = text[:first_tick_idx] + ENTRY + text[first_tick_idx:]

# Sanity: anchor now appears exactly once at top of file
new_first_tick_idx = new_text.find('<div class="tick-entry" data-tick="')
assert new_first_tick_idx == first_tick_idx, "prepend anchor moved unexpectedly"
new_tick_count = new_text.count(f'data-tick="{TICK_ID}"')
assert new_tick_count == 1, f"FAIL: anchor {TICK_ID!r} appears {new_tick_count}x in new text, expected 1"

# Wrapper count check (pitfall #70 pattern — extract count to local first)
wrapper_count = new_text[len(text[:first_tick_idx]):][:500].count('<div class="tick-entry"')
assert wrapper_count == 1, f"FAIL: wrapper appears {wrapper_count}x in new entry, expected 1"

BL.write_text(new_text, encoding="utf-8")

# Re-read and re-verify after write
verify_text = BL.read_text(encoding="utf-8")
final_count = verify_text.count(f'data-tick="{TICK_ID}"')
assert final_count == 1, f"FAIL post-write: anchor count {final_count}, expected 1"

# Total entry count delta
old_count = text.count('<div class="tick-entry" data-tick="')
new_count = verify_text.count('<div class="tick-entry" data-tick="')
assert new_count == old_count + 1, f"FAIL: entry count delta {new_count - old_count}, expected +1"

print(f"OK: prepended entry {TICK_ID}")
print(f"OK: total tick-entry count: {old_count} → {new_count}")
