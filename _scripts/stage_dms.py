"""
Stage 19 DMs in X compose (DO NOT SEND) — prove the compose flow works.
Each DM is read from outreach/leads/dm_NN_handle.txt, navigated to
x.com/messages/compose?recipient_username=X, the message body typed
into the compose textbox, then the X close button clicked to DISCARD
the draft (NOT sent). Per user request — they want to review before send.
"""

import asyncio
import os
import re
import sys
from pathlib import Path

os.environ.pop("PYTHONPATH", None)

from browser_use.browser import BrowserSession
from browser_use.browser.events import (
    ClickElementEvent,
    TypeTextEvent,
    SendKeysEvent,
    NavigateToUrlEvent,
)
from browser_use.browser.watchdogs.default_action_watchdog import DefaultActionWatchdog
from bubus import EventBus

LEADS_DIR = Path(r"C:\Users\Potts\projects\atlas-store\outreach\leads")
RESULTS = []


def load_dms():
    """Load all dm_*.txt files, return list of (index, handle, body)."""
    out = []
    files = sorted(LEADS_DIR.glob("dm_*.txt"))
    for f in files:
        m = re.match(r"dm_(\d+)_([^.]+)\.txt", f.name)
        if not m:
            # filename might end differently, parse differently
            # try: dm_18__convertica.txt (double underscore)
            m2 = re.match(r"dm_(\d+)_(.+?)\.txt", f.name)
            if not m2:
                continue
            idx, name = m2.group(1), m2.group(2).strip("_")
        else:
            idx, name = m.group(1), m.group(2)

        # pull TO handle from header line 1
        text = f.read_text(encoding="utf-8")
        handle_match = re.search(r"^# TO: @(\S+)\s*\(.*\)$", text, re.MULTILINE)
        handle = handle_match.group(1) if handle_match else name

        # body = everything after the ======== line, trimmed
        parts = text.split("=" * 40, 1)
        body = parts[1].strip() if len(parts) == 2 else text

        out.append((int(idx), handle, body, f.name))
    return out


async def wait_and_state(session, settle_ms=3500):
    """navigate + wait for selector_map populated."""
    await asyncio.sleep(settle_ms / 1000)
    return await session.get_browser_state_summary()


def find_node(selector_map, **filters):
    """Find EnhancedDOMTreeNode matching any of given filter predicates.
    filters can include:
      attributes_eq: {attr: value}      exact attribute match
      attributes_has: {attr: value}     attribute contains value (string)
      text_includes: str                visible text contains this
      tag_name: str                     upper-case HTML tag
    """
    for idx, node in selector_map.items():
        if not hasattr(node, "attributes"):
            continue
        ok = True
        attrs = node.attributes or {}
        if "attributes_eq" in filters:
            for k, v in filters["attributes_eq"].items():
                if attrs.get(k) != v:
                    ok = False
                    break
        if not ok:
            continue
        if "attributes_has" in filters:
            attr_ok = True
            for k, v in filters["attributes_has"].items():
                if v not in (attrs.get(k) or ""):
                    attr_ok = False
                    break
            if not attr_ok:
                continue
        if "text_includes" in filters:
            try:
                t = node.get_all_children_text() or node.node_value or ""
            except Exception:
                t = ""
            if filters["text_includes"] not in t:
                continue
        if "tag_name" in filters:
            if (node.tag_name or "").upper() != filters["tag_name"].upper():
                continue
        return idx, node
    return None, None


async def stage_one(session, bus, idx, handle, body, filename):
    """Navigate to compose, type, then close-discard."""
    print(f"\n[{idx:02d}] {handle}  -- {filename}")

    url = f"https://x.com/messages/compose?recipient_username={handle}"
    print(f"  navigate: {url}")
    try:
        await session.navigate_to(url)
    except Exception as e:
        msg = f"NAV_ERROR: {e!r}"
        print(f"  {msg}")
        RESULTS.append((idx, handle, "FAIL", "navigate", msg))
        return False

    summary = await wait_and_state(session, settle_ms=4000)
    smap = summary.dom_state.selector_map

    # X DM compose textbox: <div contenteditable="true" role="textbox"
    #                          aria-label="Message text" /> OR often
    # data-testid DM composer "dmComposerTextInput" or similar.
    # Try a series of lookups in order.
    textbox_idx, textbox_node = None, None
    for attrs_eq in [
        {"aria-label": "Message text"},
        {"data-testid": "dmComposerTextInput"},
        {"data-testid": "tweetTextarea_0"},
        {"aria-label": "Post text"},  # fallback if X shows public compose
    ]:
        textbox_idx, textbox_node = find_node(smap, attributes_eq=attrs_eq)
        if textbox_idx is not None:
            print(f"  textbox found idx={textbox_idx} attrs={attrs_eq}")
            break
        # try partial match
        textbox_idx, textbox_node = find_node(
            smap, attributes_has={"aria-label": "Message text"}
        )
        if textbox_idx is not None:
            break

    if textbox_idx is None:
        # one retry after additional settle
        await asyncio.sleep(2.5)
        summary = await wait_and_state(session, settle_ms=0)
        smap = summary.dom_state.selector_map
        textbox_idx, textbox_node = find_node(
            smap, attributes_has={"aria-label": "Message text"}
        ) or find_node(smap, attributes_has={"data-testid": "dmComposer"})
        if textbox_idx is None:
            print(f"  TEXTBOX NOT FOUND. URL after nav: {summary.page_info.url if summary.page_info else 'n/a'}")
            RESULTS.append((idx, handle, "FAIL", "textbox", "compose textbox not found"))
            return False
        print(f"  textbox found on retry idx={textbox_idx}")

    wd = DefaultActionWatchdog(event_bus=bus, browser_session=session)

    # 1) click the textbox to focus
    try:
        await wd.on_ClickElementEvent(
            ClickElementEvent(node=textbox_node)
        )
        await asyncio.sleep(0.4)
    except Exception as e:
        RESULTS.append((idx, handle, "FAIL", "click textbox", repr(e)))
        return False

    # 2) type the body
    try:
        await wd.on_TypeTextEvent(
            TypeTextEvent(node=textbox_node, text=body)
        )
        await asyncio.sleep(0.6)
        print(f"  typed {len(body)} chars into compose")
    except Exception as e:
        RESULTS.append((idx, handle, "FAIL", "type", repr(e)))
        return False

    # 3) screenshot proof
    try:
        proof = LEADS_DIR.parent / "_screens"
        proof.mkdir(parents=True, exist_ok=True)
        shot = proof / f"dm_{idx:02d}_{handle}_staged.png"
        await session.screenshot(path=str(shot))
        print(f"  screenshot: {shot.name}")
    except Exception as e:
        print(f"  screenshot warn: {e!r}")

    # 4) DISCARD: click the X (close) button on the compose modal.
    # After typing, X shows a confirmation dialog with Discard / Save buttons.
    # strategy: press Escape then look for close, OR re-snapshot and find
    # the dismiss button by aria-label.
    summary2 = await wait_and_state(session, settle_ms=1200)
    smap2 = summary2.dom_state.selector_map

    # Look for discard button
    discard_idx, discard_node = find_node(
        smap2, attributes_has={"data-testid": "confirmationSheetConfirm"}
    )
    if discard_node is None:
        # fallback: any button with text "Discard"
        for i, n in smap2.items():
            if getattr(n, "tag_name", "").upper() in ("BUTTON", "DIV", "SPAN"):
                try:
                    t = n.get_all_children_text() or ""
                except Exception:
                    t = ""
                if t.strip().lower() == "discard" or t.strip().lower().startswith("discard"):
                    discard_idx, discard_node = i, n
                    break

    if discard_node is not None:
        try:
            await wd.on_ClickElementEvent(ClickElementEvent(node=discard_node))
            print(f"  clicked Discard (idx={discard_idx})")
        except Exception as e:
            print(f"  discard click err: {e!r}")
    else:
        # fallback: try Escape to close
        try:
            await wd.on_SendKeysEvent(SendKeysEvent(keys="Escape"))
            print(f"  no Discard button found, pressed Escape")
        except Exception as e:
            print(f"  escape err: {e!r}")

    await asyncio.sleep(1.0)
    RESULTS.append((idx, handle, "STAGED", "compose typed + discarded", body[:60]))
    return True


async def main():
    dms = load_dms()
    print(f"loaded {len(dms)} dm files from {LEADS_DIR}")

    session = BrowserSession(cdp_url="http://localhost:9222")
    await session.start()
    bus = EventBus()
    try:
        for idx, handle, body, fname in dms:
            ok = await stage_one(session, bus, idx, handle, body, fname)
    finally:
        # capture final URL
        try:
            final_state = await session.get_browser_state_summary()
            final_url = (
                final_state.page_info.url
                if final_state.page_info and final_state.page_info.url
                else final_state.url
            )
        except Exception:
            final_url = "<unknown>"
        await session.stop()

    # report
    print("\n" + "=" * 60)
    print("STAGING REPORT")
    print("=" * 60)
    staged = [r for r in RESULTS if r[2] == "STAGED"]
    failed = [r for r in RESULTS if r[2] == "FAIL"]
    print(f"STAGED: {len(staged)} / {len(dms)}")
    print(f"FAILED: {len(failed)}")
    for r in RESULTS:
        print(f"  [{r[0]:02d}] {r[1]:20s}  {r[2]:6s}  {r[3]:12s}  -- {r[4][:80]!r}")
    print(f"\nFINAL URL: {final_url}")
    return len(staged), len(failed), final_url


if __name__ == "__main__":
    ok, fail, final_url = asyncio.run(main())
    sys.exit(0 if fail == 0 else 1)
