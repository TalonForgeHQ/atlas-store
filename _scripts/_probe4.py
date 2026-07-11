import asyncio, os, json, urllib.request
os.environ.pop('PYTHONPATH', None)
from browser_use.browser import BrowserSession
from browser_use.browser.events import SwitchTabEvent, ScreenshotEvent

async def main():
    raw = urllib.request.urlopen('http://localhost:9222/json').read()
    tabs = json.loads(raw)
    x_tab = next(t for t in tabs if t['type'] == 'page' and 'x.com' in t.get('url',''))
    print('x tab targetId:', x_tab['id'])

    s = BrowserSession(cdp_url='http://localhost:9222')
    await s.start()
    try:
        s.event_bus.dispatch(SwitchTabEvent(target_id=x_tab['id']))
        await asyncio.sleep(1.5)
        # Try plain messages/compose
        await s.navigate_to('https://x.com/messages/compose')
        await asyncio.sleep(6)
        st = await s.get_browser_state_summary()
        print('after plain /messages/compose nav:')
        print('  url:', st.url)
        print('  title:', st.title)
        print('  selector_map size:', len(st.dom_state.selector_map))
        smap = st.dom_state.selector_map
        # Look for textbox candidates + close/discard buttons
        cands = []
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
            # textbox OR button-like
            if ce == 'true' or 'composer' in testid.lower() or 'dmcompos' in testid.lower() or 'messag' in aria.lower() or 'dm' in testid.lower() or 'dm' in (aria or '').lower():
                print(f'  CAND [{idx}] <{tag}> aria={aria!r} testid={testid!r} role={role!r} ce={ce!r} text={t!r}')
                cands.append(idx)
        print('cand count:', len(cands))
        # also dump any BUTTON whose text is X, Close, Discard, Send
        for idx, n in smap.items():
            try:
                attrs = n.attributes or {}
            except Exception:
                attrs = {}
            tag = (n.tag_name or '').upper()
            t = ''
            try:
                t = (n.get_all_children_text() or n.node_value or '').strip()
            except Exception:
                pass
            aria = attrs.get('aria-label','').strip()
            testid = attrs.get('data-testid','').strip()
            if tag in ('BUTTON','DIV','SPAN'):
                if t.lower() in ('x','close','discard','cancel','send') or 'close' in aria.lower() or 'dismiss' in aria.lower():
                    print(f'  CLOSE-CAND [{idx}] <{tag}> aria={aria!r} testid={testid!r} text={t[:40]!r}')
        shot_ev = s.event_bus.dispatch(ScreenshotEvent(full_page=False))
        path = await shot_ev
        print('shot:', path)
    finally:
        await s.stop()

asyncio.run(main())
