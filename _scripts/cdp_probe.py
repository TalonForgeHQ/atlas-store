"""Direct CDP probe of the Brave browser via the WebSocket on port 9224.
Attach to the new-tab page, navigate to x.com/i/chat/compose, then capture
the final URL after redirects and any errors. Tells us whether X sees us
as authenticated or not.
"""
import json, sys, time
import websocket

# The Python sandbox has its own /tmp; write outputs to project folder.
import os
os.chdir(r"C:\Users\Potts\projects\atlas-store\\_scripts")
sys.path.insert(0, r"C:\Users\Potts\projects\atlas-store\\_scripts")

PORT = "9224"
HOST = "localhost"

import urllib.request
def list_pages():
    with urllib.request.urlopen(f"http://{HOST}:{PORT}/json/list", timeout=5) as r:
        return json.loads(r.read().decode())

pages = list_pages()
target = None
for p in pages:
    if p.get("type") == "page":
        target = p
        break
if not target:
    print("NO PAGE TAB FOUND")
    sys.exit(1)

ws_url = target["webSocketDebuggerUrl"]
tab_title = target.get("title", "?")
print(f"ATTACHING to tab title={tab_title!r} url={target.get('url','?')}")
print(f"WS URL: {ws_url}")

def make_caller(ws):
    next_id = [1]
    pending = {}
    def call(method, params=None, timeout=15):
        i = next_id[0]; next_id[0] += 1
        msg = {"id": i, "method": method, "params": params or {}}
        ws.send(json.dumps(msg))
        deadline = time.time() + timeout
        while time.time() < deadline:
            ws.settimeout(0.5)
            try:
                raw = ws.recv()
            except Exception:
                continue
            try:
                resp = json.loads(raw)
            except Exception:
                continue
            if resp.get("id") == i:
                if "error" in resp:
                    raise RuntimeError(f"CDP error: {resp['error']}")
                return resp.get("result", {})
        raise TimeoutError(f"CDP call {method} timed out")
    return call

ws = websocket.create_connection(ws_url, timeout=10)
ws.settimeout(0.5)
# drain initial events
deadline = time.time() + 1.0
while time.time() < deadline:
    try:
        ws.recv()
    except Exception:
        break

call = make_caller(ws)

call("Page.enable")
call("Network.enable")

# Now navigate to x.com/i/chat/compose (the DM compose page)
print("\n>> Navigating to https://x.com/i/chat/compose ...")
call("Page.navigate", {"url": "https://x.com/i/chat/compose", "transitionType": "typed"}, timeout=20)

# Wait for load + collect network events
start = time.time()
final_url = None
status_code = None
top_responses = []
while time.time() - start < 25:
    ws.settimeout(0.5)
    try:
        raw = ws.recv()
    except Exception:
        continue
    try:
        ev = json.loads(raw)
    except Exception:
        continue
    m = ev.get("method", "")
    if m == "Network.responseReceived":
        params = ev["params"]
        url = params.get("response", {}).get("url", "?")
        if "x.com" in url and "doubleclick" not in url:
            top_responses.append((params["response"].get("status"), url[:80]))
            if url.startswith("https://x.com/i/chat/compose") or url.startswith("https://x.com/messages") or url.startswith("https://x.com/"):
                status_code = params["response"].get("status")
    if m == "Page.frameNavigated":
        u = ev["params"].get("frame", {}).get("url", "")
        if u.startswith("https://x.com/"):
            final_url = u[:120]

# Wait 8 seconds for Cloudflare to settle and X DOM to hydrate
time.sleep(8)

# Evaluate current state via JS, including cookies and full URL
result = call("Runtime.evaluate", {"expression": "(()=>{ try { return { url: location.href, readyState: document.readyState, title: document.title, hasBody: !!document.body, textStart: (document.body && document.body.innerText || '').substring(0,300) }; } catch(e) { return { error: String(e) }; } })()"})
print("\n>> Runtime result:")
print(json.dumps(result.get("result", {}).get("value", {}), indent=2)[:1500])

# Pull all cookies via Network
ck = call("Network.getAllCookies")
print("\n>> Cookies (count=" + str(len(ck.get("cookies", []))) + ")")
for c in ck.get("cookies", []):
    name = c.get("name")
    dom = c.get("domain", "")
    if dom.endswith("x.com") or dom.endswith("twitter.com"):
        print(f"  {name:<25} domain={dom:<25} expires={c.get('expires')} httpOnly={c.get('httpOnly')} secure={c.get('secure')}")

print("\n>> Network top responses captured (top 10):")
for s, u in top_responses[:10]:
    print(f"  {s} {u}")

ws.close()
print("\nDONE")
