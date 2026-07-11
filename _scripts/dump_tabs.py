import json, sys, os
fn = sys.argv[1]
try:
    d = json.load(open(fn))
except Exception as e:
    print('parse fail', repr(e)); sys.exit(1)
for p in d:
    if p.get('type') == 'page':
        u = (p.get('url') or '?')[:100]
        t = (p.get('title') or '?')[:60]
        print(f"{u:<100} | {t}")
