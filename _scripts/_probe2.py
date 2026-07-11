import asyncio, os
os.environ.pop('PYTHONPATH', None)
from browser_use.browser import BrowserSession

async def main():
    s = BrowserSession(cdp_url='http://localhost:9222')
    await s.start()
    try:
        st = await s.get_browser_state_summary()
        print('CURRENT url:', st.url)
        print('CURRENT title:', st.title)
        print('cookies present, checking via eval:')
        # use eval-like approach: just navigate fresh and see what loads
        await s.navigate_to('https://x.com/messages/compose?recipient_username=RentRedi')
        await asyncio.sleep(6)
        st = await s.get_browser_state_summary()
        print('AFTER-NAV url:', st.url)
        print('AFTER-NAV title:', st.title)
        smap = st.dom_state.selector_map
        print(f'selector_map size: {len(smap)}')
        # Dump everything with any identifying info
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
            print(f'  [{idx}] <{tag}> aria={attrs.get("aria-label","")!r} testid={attrs.get("data-testid","")!r} role={attrs.get("role","")!r} href={attrs.get("href","")[:60]!r} text={t!r}')
        # screenshot for debugging
        await s.screenshot(path=r'C:\Users\Potts\projects\atlas-store\_screens\probe.png')
    finally:
        await s.stop()

asyncio.run(main())
