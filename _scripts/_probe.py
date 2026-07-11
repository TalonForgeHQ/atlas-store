import asyncio, os
os.environ.pop('PYTHONPATH', None)
from browser_use.browser import BrowserSession

async def main():
    s = BrowserSession(cdp_url='http://localhost:9222')
    await s.start()
    try:
        await s.navigate_to('https://x.com/messages/compose?recipient_username=RentRedi')
        await asyncio.sleep(5)
        st = await s.get_browser_state_summary()
        print('PageInfo attrs exist:', [a for a in dir(st.page_info) if not a.startswith('_')])
        pi = st.page_info
        for attr in ('url', 'title', 'viewport', 'frame_url'):
            v = getattr(pi, attr, '<MISSING>')
            sv = str(v)[:100]
            print(f'  page_info.{attr} = {sv}')
        print('summary attrs:', [a for a in dir(st) if not a.startswith('_')])
        smap = st.dom_state.selector_map
        print('selector_map size:', len(smap))
        for idx, n in list(smap.items())[:400]:
            try:
                attrs = n.attributes or {}
            except Exception:
                attrs = {}
            aria = attrs.get('aria-label') or ''
            testid = attrs.get('data-testid') or ''
            role = attrs.get('role') or ''
            tag = (n.tag_name or '').upper()
            ce = attrs.get('contenteditable') or ''
            if any([aria, testid, role == 'textbox', ce == 'true']):
                t = ''
                try:
                    t = (n.get_all_children_text() or '')[:60]
                except Exception:
                    pass
                print(f'  [{idx}] <{tag}> aria={aria!r} testid={testid!r} role={role!r} ce={ce!r} text={t!r}')
    finally:
        await s.stop()

asyncio.run(main())
