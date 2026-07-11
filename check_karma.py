from playwright.sync_api import sync_playwright
import time, json
from pathlib import Path

CDP_URL = "http://localhost:9222"

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(CDP_URL)
    context = browser.contexts[0]
    page = context.new_page()

    # Check your profile for total karma
    print("checking profile karma...")
    page.goto("https://www.reddit.com/user/Pearlharbortours1/", wait_until="domcontentloaded", timeout=30000)
    time.sleep(3)

    karma_data = page.evaluate("""() => {
        const items = document.querySelectorAll('faceplate-tracker, [id*="karma"], [class*="karma"]');
        const allText = document.body.innerText;
        const karmaMatch = allText.match(/([\d,]+)\s+karma/i);
        return {
            text_excerpt: allText.slice(0, 1500),
            karma_match: karmaMatch ? karmaMatch[0] : null,
        };
    }""")
    print(f"PROFILE PAGE EXCERPT:")
    print(karma_data["text_excerpt"])
    print(f"\nKARMA MATCH: {karma_data['karma_match']}")

    # Test posting ability on r/SideProject
    print("\n\n=== testing r/SideProject submit page ===")
    page.goto("https://www.reddit.com/r/SideProject/submit", wait_until="domcontentloaded", timeout=30000)
    time.sleep(4)

    submit_state = page.evaluate("""() => {
        return {
            url: window.location.href,
            title: document.title,
            body_excerpt: document.body.innerText.slice(0, 800),
            hasTitleField: !!document.querySelector('textarea[name="title"], textarea[placeholder*="Title"], [data-testid="post-title-text-field"] textarea'),
            hasBodyField: !!document.querySelector('div[contenteditable="true"], textarea[placeholder*="body"], [data-testid="markdown-editor"] textarea'),
            hasSubmitBtn: !!document.querySelector('button[type="submit"], [data-testid="submit-post-button"]'),
        };
    }""")
    print(f"URL: {submit_state['url']}")
    print(f"TITLE: {submit_state['title']}")
    print(f"EXCERPT:")
    print(submit_state['body_excerpt'])
    print(f"\nFIELDS:")
    print(f"  title field: {submit_state['hasTitleField']}")
    print(f"  body field: {submit_state['hasBodyField']}")
    print(f"  submit btn: {submit_state['hasSubmitBtn']}")

    page.screenshot(path="reddit_submit_test.png", full_page=False)
    print("\nscreenshot saved: reddit_submit_test.png")
