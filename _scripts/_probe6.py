import asyncio, os, json, urllib.request, base64
os.environ.pop('PYTHONPATH', None)
from browser_use.browser import BrowserSession
from browser_use.browser.events import SwitchTabEvent, ScreenshotEvent

async def main():
    raw = urllib.request.urlopen('http://localhost:9222/json').read()
    tabs = json.loads(raw)
    x_tab = next(t for t in tabs if t['type'] == 'page' and 'x.com' in t.get('url',''))
    print('ATTACH:', x_tab['id'], x_tab['url'])

    s = BrowserSession(cdp_url='http://localhost:9222')
    await s.start()
    try:
        s.event_bus.dispatch(SwitchTabEvent(target_id=x_tab['id']))
        await asyncio.sleep(2)

        await s.navigate_to('https://x.com/messages/compose?recipient_username=RentRedi')
        await asyncio.sleep(9)
        st = await s.get_browser_state_summary()
        smap = st.dom_state.selector_map
        print('selector_map size:', len(smap))

        # Save screenshot
        out_dir = r'C:\Users\Potts\projects\atlas-store\_screens'
        os.makedirs(out_dir, exist_ok=True)
        ev = s.event_bus.dispatch(ScreenshotEvent(full_page=False))
        b64 = await ev
        with open(os.path.join(out_dir, 'probe_compose_2.png'), 'wb') as f:
            f.write(base64.b64decode(b64))
        print('shot saved')

        # Look for textbox / compose candidates
        print('\n--- CANDIDATES with compose/dm/textbox/editor ---')
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
            placeholder = attrs.get('data-placeholder','') or attrs.get('placeholder','')
            if (ce == 'true' or 'compos' in testid.lower() or 'dm' in testid.lower() or
                'textbox' in role.lower() or 'text' in (aria or '').lower() or 'messag' in (aria or '').lower() or
                placeholder):
                print(f'  [{idx}] <{tag}> aria={aria!r} testid={testid!r} role={role!r} ce={ce!r} ph={placeholder!r} text={t!r}')
    finally:
        await s.stop()

asyncio.run(main())
