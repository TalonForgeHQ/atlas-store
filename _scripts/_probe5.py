import asyncio, os, json, urllib.request, base64
os.environ.pop('PYTHONPATH', None)
from browser_use.browser import BrowserSession
from browser_use.browser.events import SwitchTabEvent, ScreenshotEvent, NavigateToUrlEvent

async def main():
    raw = urllib.request.urlopen('http://localhost:9222/json').read()
    tabs = json.loads(raw)
    print('All page targets:')
    for t in tabs:
        if t['type'] == 'page':
            print(f"  {t['id']}  {t['url'][:80]}")

    x_tab = next(t for t in tabs if t['type'] == 'page' and 'x.com' in t.get('url',''))
    print('\nATTACH to:', x_tab['id'], x_tab['url'])

    s = BrowserSession(cdp_url='http://localhost:9222')
    await s.start()
    try:
        s.event_bus.dispatch(SwitchTabEvent(target_id=x_tab['id']))
        await asyncio.sleep(2)
        st = await s.get_browser_state_summary()
        print('after switch url:', st.url)

        # First navigate to the compose URL with full wait
        print('\n--- navigate ---')
        await s.navigate_to('https://x.com/messages/compose?recipient_username=RentRedi')
        for i in range(8):
            await asyncio.sleep(1.5)
            st = await s.get_browser_state_summary()
            print(f'  +{(i+1)*1.5:.1f}s url={st.url[:60]} title={st.title[:30]} smap={len(st.dom_state.selector_map)}')

        # save screenshot
        ev = s.event_bus.dispatch(ScreenshotEvent(full_page=False))
        b64 = await ev
        out = r'C:\Users\Potts\projects\atlas-store\_screens\probe_compose.png'
        with open(out, 'wb') as f:
            f.write(base64.b64decode(b64))
        print(f'\nscreenshot bytes saved: {out}')
    finally:
        await s.stop()

asyncio.run(main())
