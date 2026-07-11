from playwright.sync_api import sync_playwright
import time, json
from pathlib import Path

CDP_URL = "http://localhost:9222"

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(CDP_URL)
    context = browser.contexts[0]
    page = context.new_page()

    print("navigating to r/SideProject submit...")
    page.goto("https://www.reddit.com/r/SideProject/submit", wait_until="domcontentloaded", timeout=30000)
    time.sleep(5)
    print(f"on: {page.url}")

    # Detailed DOM dump
    state = page.evaluate("""() => {
        // Look at all elements with role=textbox, role=button, etc
        const textboxes = document.querySelectorAll('[role="textbox"], textarea');
        const buttons = document.querySelectorAll('button');
        const tabs = document.querySelectorAll('[role="tab"]');

        const result = {
            url: window.location.href,
            title: document.title,
            textboxes: Array.from(textboxes).map(el => ({
                tag: el.tagName,
                role: el.getAttribute('role'),
                placeholder: el.getAttribute('aria-label') || el.getAttribute('placeholder'),
                name: el.getAttribute('name'),
                id: el.id,
                visible: el.offsetWidth > 0,
            })),
            tabs: Array.from(tabs).map(el => ({
                text: el.innerText,
                selected: el.getAttribute('aria-selected'),
                role: el.getAttribute('role'),
            })),
            buttons: Array.from(buttons).slice(0, 15).map(el => ({
                text: el.innerText.slice(0, 50),
                type: el.type,
                visible: el.offsetWidth > 0,
            })),
        };
        return result;
    }""")

    print(f"URL: {state['url']}")
    print(f"\nTEXTBOXES ({len(state['textboxes'])}):")
    for tb in state['textboxes']:
        print(f"  {tb['tag']} role={tb['role']} ph={tb['placeholder']!r} name={tb['name']} visible={tb['visible']}")

    print(f"\nTABS ({len(state['tabs'])}):")
    for t in state['tabs']:
        print(f"  [{t['selected']}] {t['text']!r}")

    print(f"\nBUTTONS ({len(state['buttons'])}):")
    for b in state['buttons']:
        print(f"  type={b['type']} visible={b['visible']} text={b['text']!r}")

    # Take a screenshot of the submit area only
    page.screenshot(path="submit_form.png", full_page=True)
    print("\nscreenshot: submit_form.png")
