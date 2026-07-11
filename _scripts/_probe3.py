import asyncio, os, json, urllib.request
os.environ.pop('PYTHONPATH', None)
from browser_use.browser import BrowserSession
from browser_use.browser.events import SwitchTabEvent

async def main():
    # Discover tabs via the /json endpoint and pick the X one
    raw = urllib.request.urlopen('http://localhost:9222/json').read()
    tabs = json.loads(raw)
    x_tab = next((t for t in tabs if t['type'] == 'page' and 'x.com' in t.get('url','')), None)
    print('x tab found:', x_tab is not None)
    print('x tab url:', x_tab['url'] if x_tab else 'n/a')
    print('x tab targetId:', x_tab['id'] if x_tab else 'n/a')

    s = BrowserSession(cdp_url='http://localhost:9222')
    await s.start()
    try:
        # Switch to the X tab
        ev = s.event_bus.dispatch(SwitchTabEvent(target_id=x_tab['id']))
        # Wait for event resolution
        try:
            await ev.wait_until_complete(timeout=10)
        except Exception as e:
            print(f'switch wait warn: {e!r}')
        # confirm current url
        st = await s.get_browser_state_summary()
        print('after switch, url:', st.url)
        print('after switch, title:', st.title)

        # Now navigate X tab to compose
        await s.navigate_to('https://x.com/messages/compose?recipient_username=RentRedi')
        await asyncio.sleep(6)
        st = await s.get_browser_state_summary()
        print('after nav, url:', st.url)
        print('after nav, title:', st.title)
        smap = st.dom_state.selector_map
        print(f'selector_map size: {len(smap)}')

        # Dump likely textbox candidates + buttons
        for idx, n in smap.items():
            try:
                attrs = n.attributes or {}
            except Exception:
                attrs = {}
            tag = (n.tag_name or '').upper()
            t = ''
            try:
                t = (n.get_all_children_text() or '')[:80]
            except Exception:
                pass
            aria = attrs.get('aria-label','')
            testid = attrs.get('data-testid','')
            role = attrs.get('role','')
            ce = attrs.get('contenteditable','')
            if any([aria,testid,role,tag in ('BUTTON','A','TEXTAREA','INPUT'),ce]):
                print(f'  [{idx}] <{tag}> aria={aria!r} testid={testid!r} role={role!r} ce={ce!r} text={t!r}')

        # screenshot via event dispatch
        from browser_use.browser.events import ScreenshotEvent
        shot_ev = s.event_bus.dispatch(ScreenshotEvent(full_page=False))
        path = await shot_ev
        print(f'screenshot saved: {path}')
    finally:
        await s.stop()

asyncio.run(main())
