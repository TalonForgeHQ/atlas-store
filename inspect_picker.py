from playwright.sync_api import sync_playwright
import time

CDP_URL = "http://localhost:9222"

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(CDP_URL)
    context = browser.contexts[0]
    page = context.new_page()

    page.goto("https://www.reddit.com/submit", wait_until="domcontentloaded", timeout=30000)
    time.sleep(4)

    # Get ALL interactive elements with class names + shadow DOM info
    print("=== ALL interactive elements ===")
    elements = page.evaluate("""() => {
        const results = [];
        document.querySelectorAll('community-picker, [class*="picker"], button, [role="combobox"]').forEach(el => {
            const rect = el.getBoundingClientRect();
            results.push({
                tag: el.tagName,
                class: (el.className || '').toString().slice(0, 80),
                aria: el.getAttribute('aria-label') || '',
                role: el.getAttribute('role') || '',
                text: (el.innerText || '').slice(0, 60),
                hasShadow: !!el.shadowRoot,
                visible: rect.width > 0,
                y: rect.y,
                id: el.id,
            });
        });
        return results;
    }""")
    for e in elements:
        if e['visible'] or 'community' in e['class'].lower() or 'picker' in e['class'].lower():
            print(f"  {e['tag']:20s} class={e['class'][:50]!r:55s} aria={e['aria']!r:25s} shadow={e['hasShadow']} visible={e['visible']} y={e['y']:.0f} text={e['text']!r}")

    # Try the direct URL to r/SideProject submit (might bypass picker)
    print("\n\n=== TRY DIRECT SUBREDDIT URL ===")
    page.goto("https://www.reddit.com/r/SideProject/submit", wait_until="domcontentloaded", timeout=30000)
    time.sleep(5)
    print(f"on: {page.url}")

    state = page.evaluate("""() => {
        const titleComp = document.querySelector('post-composer-title');
        const subredditName = document.querySelector('input[name="subredditName"]');
        const composer = document.querySelector('shreddit-composer');
        const composerRect = composer ? composer.getBoundingClientRect() : null;
        return {
            url: window.location.href,
            hasTitleComp: !!titleComp,
            hasShadowRoot: titleComp ? !!titleComp.shadowRoot : false,
            subredditNameValue: subredditName ? subredditName.value : '',
            composerVisible: composerRect ? composerRect.width > 0 : false,
            composerY: composerRect ? composerRect.y : 0,
        };
    }""")
    print(f"STATE: {state}")

    page.screenshot(path="direct_submit.png", full_page=True)
    print("\nscreenshot: direct_submit.png")

    # If title component exists, try to interact with its shadow DOM
    if state['hasTitleComp']:
        result = page.evaluate("""() => {
            const titleComp = document.querySelector('post-composer-title');
            if (!titleComp.shadowRoot) {
                return {error: 'no shadow root'};
            }
            const inner = titleComp.shadowRoot.innerHTML.slice(0, 2000);
            const inputs = titleComp.shadowRoot.querySelectorAll('input, textarea, [contenteditable]');
            return {
                innerHTML: inner,
                inputs: Array.from(inputs).map(el => ({
                    tag: el.tagName,
                    type: el.type,
                    placeholder: el.getAttribute('placeholder'),
                    ariaLabel: el.getAttribute('aria-label'),
                    visible: el.getBoundingClientRect().width > 0,
                })),
            };
        }""")
        print("\nTITLE COMP SHADOW:")
        if 'innerHTML' in result:
            print(result['innerHTML'][:1500])
            print(f"\nINPUTS: {result.get('inputs', [])}")
        else:
            print(result)
