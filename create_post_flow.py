from playwright.sync_api import sync_playwright
import time, json

CDP_URL = "http://localhost:9222"

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(CDP_URL)
    context = browser.contexts[0]
    page = context.new_page()

    print("going to reddit home...")
    page.goto("https://www.reddit.com/", wait_until="domcontentloaded", timeout=30000)
    time.sleep(4)

    # Look for "Create post" button in nav
    print("looking for Create post button...")
    create_btn = page.query_selector('a[href*="/submit"], button:has-text("Create post"), [data-testid="create-post"]')
    if create_btn:
        print(f"found create btn: {create_btn.inner_text()[:50]}")
        create_btn.click()
        time.sleep(3)
    else:
        print("no create btn found, navigating directly to submit...")
        page.goto("https://www.reddit.com/submit", wait_until="domcontentloaded", timeout=30000)
        time.sleep(4)

    print(f"on: {page.url}")

    # Dump EVERYTHING on this page now
    state = page.evaluate("""() => {
        const all = document.querySelectorAll('*');
        const textboxes = document.querySelectorAll('[role="textbox"], textarea, [contenteditable="true"]');
        const buttons = document.querySelectorAll('button, [role="button"]');
        const inputs = document.querySelectorAll('input');
        return {
            url: window.location.href,
            title: document.title,
            textboxes: Array.from(textboxes).map(el => ({
                tag: el.tagName,
                role: el.getAttribute('role'),
                aria: el.getAttribute('aria-label'),
                placeholder: el.getAttribute('placeholder'),
                visible: el.offsetWidth > 0,
                text: (el.innerText || el.value || '').slice(0, 60),
            })),
            inputs: Array.from(inputs).map(el => ({
                type: el.type,
                name: el.name,
                placeholder: el.getAttribute('placeholder'),
                visible: el.offsetWidth > 0,
            })),
            buttons: Array.from(buttons).slice(0, 20).map(el => ({
                text: el.innerText.slice(0, 50),
                type: el.type,
                visible: el.offsetWidth > 0,
            })),
        };
    }""")

    print(f"URL: {state['url']}")
    print(f"TITLE: {state['title']}")
    print(f"\nTEXTBOXES ({len(state['textboxes'])}):")
    for tb in state['textboxes']:
        print(f"  {tb['tag']:8s} role={tb['role']:12s} aria={tb['aria']!r:25s} visible={tb['visible']} text={tb['text']!r}")
    print(f"\nINPUTS ({len(state['inputs'])}):")
    for inp in state['inputs']:
        print(f"  type={inp['type']} name={inp['name']} ph={inp['placeholder']!r} visible={inp['visible']}")
    print(f"\nBUTTONS ({len(state['buttons'])}):")
    for b in state['buttons']:
        print(f"  type={b['type']:7s} visible={b['visible']} text={b['text']!r}")

    page.screenshot(path="create_post_flow.png", full_page=True)
    print("\nscreenshot: create_post_flow.png")
