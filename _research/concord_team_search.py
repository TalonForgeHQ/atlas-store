"""Search for Concord CLM founder/CEO via first-party signals."""
import re, json, urllib.request

# Try Concord careers/about/leadership
urls = [
    "https://concord.app/leadership",
    "https://concord.app/our-team",
    "https://concord.app/about-us",
    "https://concord.app/blog",
    "https://concord.app/legal/privacy",
    "https://concord.app/legal/dpa",
    "https://concord.app/legal/security",
]
hdr = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
for u in urls:
    try:
        req = urllib.request.Request(u, headers=hdr)
        body = urllib.request.urlopen(req, timeout=8).read().decode("utf-8", errors="ignore")
        # search for founder/CEO text
        names = re.findall(r"(?:Matt|Jean|Marc|Chris|Nick|Hugo|Samuel|Thomas|David|Alex|Lhoumeau|Missoffi|Lambert|Smith|Wong|Wang|Kim|Patel|Sharma|Chen|Liu|Wang|Li)[A-Za-z\-']{2,30}", body)
        # pronouns
        ceo_block = re.findall(r"CEO|Chief Executive Officer|Founder|Co[\- ]Founder|Co[\- ]founder|Co Founder[\s\S]{0,400}", body)
        print(f"=={u}==")
        print("size:", len(body))
        print("names:", names[:8])
        print("ceo:", ceo_block[:1])
    except Exception as e:
        print(f"=={u}== error: {e}")
