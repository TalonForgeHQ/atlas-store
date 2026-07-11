from playwright.sync_api import sync_playwright
import time

CDP_URL = "http://localhost:9222"

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(CDP_URL)
    context = browser.contexts[0]
    page = context.new_page()

    print("step 1: going to reddit.com/submit...")
    page.goto("https://www.reddit.com/submit", wait_until="domcontentloaded", timeout=30000)
    time.sleep(4)

    print(f"on: {page.url}")

    # Step 2: Find and click the community picker
    print("step 2: clicking community picker...")
    # It's an r-post-composer-form's community-picker
    picker = page.query_selector('community-picker, [slot="community-picker"], button[aria-label*="community" i], [class*="community-picker"]')
    print(f"picker found: {picker is not None}")

    if not picker:
        # Try clicking the text "Choose a community" or similar
        picker_btns = page.query_selector_all('button, [role="button"]')
        print(f"total buttons: {len(picker_btns)}")
        for b in picker_btns:
            text = b.inner_text() if b.inner_text else ""
            if "community" in text.lower() or "subreddit" in text.lower() or "choose" in text.lower() or "select" in text.lower() or "r/" in text.lower():
                print(f"  candidate: {text!r}")
                picker = b
                break

    if picker:
        print(f"clicking picker: {picker.inner_text()[:80] if picker.inner_text else 'no text'}")
        picker.click()
        time.sleep(2)

        # Look for the community search input
        print("step 3: looking for community search input...")
        search_input = page.wait_for_selector('input[type="text"][placeholder*="community" i], input[placeholder*="r/" i], input[name="communityName"], faceplate-search input', timeout=5000)
        if search_input:
            print(f"search input found")
            search_input.fill("SideProject")
            time.sleep(1)

            # Wait for autocomplete results
            time.sleep(2)
            page.screenshot(path="picker_results.png", full_page=False)

            # Find the result for r/SideProject
            result = page.query_selector('text=r/SideProject, [id*="SideProject"], button:has-text("SideProject")')
            if result:
                print(f"found SideProject result")
                result.click()
                time.sleep(3)
            else:
                print("no SideProject in autocomplete, dumping options...")
                options = page.query_selector_all('[role="option"], [role="listbox"] button, [role="listbox"] a')
                for o in options[:10]:
                    print(f"  option: {o.inner_text()[:60] if o.inner_text else '?'}")

        time.sleep(2)
        page.screenshot(path="after_picker.png", full_page=True)

    # Now check if title field appeared
    print("\nstep 4: checking title field...")
    state = page.evaluate("""() => {
        const titleComp = document.query_selector('post-composer-title');
        const titleInput = titleComp ? (titleComp.shadowRoot ? titleComp.shadowRoot.query_selector('input, textarea, [contenteditable="true"]') : null) : null;
        return {
            url: window.location.href,
            hasTitleComp: !!titleComp,
            hasTitleInput: !!titleInput,
            subredditName: document.query_selector('input[name="subredditName"]')?.value || '',
        };
    }""") if False else page.evaluate("""() => {
        const titleComp = document.querySelector('post-composer-title');
        return {
            url: window.location.href,
            hasTitleComp: !!titleComp,
            subredditName: document.querySelector('input[name="subredditName"]')?.value || '',
        };
    }""")
    print(f"STATE: {state}")
