from playwright.sync_api import sync_playwright
import time

CDP_URL = "http://localhost:9222"

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(CDP_URL)
    context = browser.contexts[0]
    page = context.new_page()

    page.goto("https://www.reddit.com/submit", wait_until="domcontentloaded", timeout=30000)
    time.sleep(5)

    # Get the FULL outer HTML of the submit form
    html = page.evaluate("""() => {
        // Find the main form area
        const main = document.querySelector('main, [role="main"], shreddit-compute-on-load, faceplate-form') || document.body;
        return main.innerHTML.slice(0, 8000);
    }""")
    print("MAIN HTML (first 8000 chars):")
    print(html)

    print("\n\n=== WIDE TITLE SEARCH ===")
    # Search for any input that could be title
    candidates = page.evaluate("""() => {
        const results = [];
        // All inputs/textareas/contenteditable
        document.querySelectorAll('input, textarea, [contenteditable="true"], [role="textbox"], shreddit-composer, [slot="title"]').forEach(el => {
            const rect = el.getBoundingClientRect();
            results.push({
                tag: el.tagName,
                type: el.type || '',
                role: el.getAttribute('role') || '',
                slot: el.getAttribute('slot') || '',
                placeholder: el.getAttribute('placeholder') || '',
                aria: el.getAttribute('aria-label') || '',
                name: el.getAttribute('name') || '',
                id: el.id || '',
                classes: el.className.toString().slice(0, 80),
                visible: rect.width > 0,
                x: rect.x,
                y: rect.y,
                w: rect.width,
                h: rect.height,
                text: (el.innerText || el.value || '').slice(0, 40),
            });
        });
        return results;
    }""")
    for c in candidates:
        print(f"  {c['tag']:10s} type={c['type']:10s} role={c['role']:12s} slot={c['slot']:8s} ph={c['placeholder']!r:25s} visible={c['visible']} y={c['y']:.0f} h={c['h']:.0f} text={c['text']!r}")
