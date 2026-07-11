"""
Reddit Engagement Machine. CDP-attached to the user's logged-in Chrome (port 9222).
"""
from playwright.sync_api import sync_playwright
import time
import json
import sys
from pathlib import Path
from datetime import datetime

CDP_URL = "http://localhost:9222"
LOG_FILE = Path("reddit_engagement.log")


def log(msg):
    ts = datetime.now().strftime("%H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line, flush=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")


# Six posts, one per hour. Each post lives at distrib/reddit-final/<sub>.md as source of truth.
def load_posts():
    """Load posts from distrib/reddit-final/ markdown files."""
    import re
    posts = []
    base = Path("distrib/reddit-final")
    sub_map = {
        "sideproject.md": ("SideProject",),
        "ai-agents.md": ("AI_Agents",),
        "entrepreneur.md": ("Entrepreneur",),
        "automation.md": ("automation",),
        "saas.md": ("saas",),
        "indiehackers.md": ("IndieHackers",),
    }
    for fname, (sub,) in sub_map.items():
        fpath = base / fname
        if not fpath.exists():
            log(f"WARN: {fpath} not found")
            continue
        content = fpath.read_text(encoding="utf-8")
        # First line is title (# Title)
        m = re.match(r"^#\s+(.+)", content)
        if not m:
            log(f"WARN: no title in {fname}")
            continue
        title = m.group(1).strip()
        body = content[m.end():].strip()
        posts.append({"sub": sub, "title": title, "body": body, "src": str(fpath)})
    return posts


def find_reddit_page(context):
    """Find the user's logged-in Reddit tab."""
    for page in context.pages:
        if "reddit.com" in page.url:
            return page
    return None


def check_login(page):
    """Return dict describing Reddit login state."""
    state = page.evaluate("""() => {
        const logInLinks = document.querySelectorAll('a[href*="/login"]');
        const userLink = document.querySelector('a[href^="/user/"]');
        const faceplateUser = document.querySelector('faceplate-tracker[source="user_menu"]');
        const headerAvatar = document.querySelector('header img[alt*="avatar"], header [data-testid="user-avatar"]');
        return {
            hasLogIn: logInLinks.length > 0,
            hasUserLink: !!userLink,
            userHref: userLink ? userLink.getAttribute('href') : null,
            hasFaceplate: !!faceplateUser,
            hasHeaderAvatar: !!headerAvatar,
        };
    }""")
    return state


def browse_sub(page, sub, top_n=10):
    """Browse a subreddit's top posts of the day."""
    log(f"browsing r/{sub}...")
    page.goto(f"https://www.reddit.com/r/{sub}/top/?t=day", wait_until="domcontentloaded", timeout=30000)
    time.sleep(3)
    posts = page.evaluate("""(topN) => {
        const items = document.querySelectorAll('shreddit-post, [data-testid="post-container"]');
        return Array.from(items).slice(0, topN).map(p => ({
            title: (p.querySelector('[slot="title"]') || {}).innerText || '',
            permalink: p.getAttribute('permalink') || '',
            score: p.getAttribute('score') || '0',
            comments: p.getAttribute('comment-count') || '0',
        }));
    }""", top_n)
    log(f"  found {len(posts)} posts")
    for p in posts:
        log(f"    - [{p['score']}] {p['title'][:80]}")
    return posts


def post_to_subreddit(page, sub, title, body):
    """Post a text submission to a subreddit. Returns the new post URL or None."""
    log(f"posting to r/{sub}: {title[:60]}...")
    submit_url = f"https://www.reddit.com/r/{sub}/submit"
    page.goto(submit_url, wait_until="domcontentloaded", timeout=30000)
    time.sleep(2)

    # Click Text post tab if needed
    try:
        page.click(
            'button[aria-label*="Text"], [data-testid="post-type-selector"] button:nth-of-type(2)',
            timeout=3000,
        )
    except Exception:
        pass
    time.sleep(1)

    # Fill title
    page.fill(
        'textarea[name="title"], [data-testid="post-title-text-field"] textarea, textarea[placeholder*="Title"]',
        title,
    )
    time.sleep(0.5)

    # Fill body
    try:
        page.fill('div[contenteditable="true"], [data-testid="markdown-editor"] textarea', body)
    except Exception as e:
        log(f"  body fill warn: {e}")

    time.sleep(1)

    # Submit
    try:
        page.click(
            'button[type="submit"], [data-testid="submit-post-button"], button:has-text("Post")',
            timeout=5000,
        )
        time.sleep(5)
        url = page.url
        log(f"  ✓ posted → {url}")
        return url
    except Exception as e:
        log(f"  ✗ submit failed: {e}")
        page.screenshot(path=f"reddit_error_{sub}.png", full_page=True)
        return None


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "check"
    log(f"=== reddit_poster.py mode={mode} ===")

    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(CDP_URL)
        context = browser.contexts[0]
        log(f"connected. {len(context.pages)} tabs open")

        page = find_reddit_page(context)
        if not page:
            log("no reddit tab found. opening one...")
            page = context.new_page()
            page.goto("https://www.reddit.com", wait_until="domcontentloaded", timeout=30000)
            time.sleep(3)

        log(f"on: {page.url}")

        if mode == "check":
            state = check_login(page)
            log(f"login state: {json.dumps(state, indent=2)}")
            logged_in = (
                state.get("hasUserLink")
                or state.get("hasFaceplate")
                or state.get("hasHeaderAvatar")
            )
            log(f"LOGGED IN: {logged_in}")
            return logged_in

        elif mode == "browse":
            for sub in ["SideProject", "AI_Agents", "Entrepreneur", "automation"]:
                browse_sub(page, sub)
                time.sleep(2)

        elif mode == "post":
            posts = load_posts()
            log(f"loaded {len(posts)} posts from distrib/reddit-final/")
            start = int(sys.argv[2]) if len(sys.argv) > 2 else 0
            end = int(sys.argv[3]) if len(sys.argv) > 3 else len(posts)
            for post in posts[start:end]:
                post_to_subreddit(page, post["sub"], post["title"], post["body"])
                log("  waiting 60s before next post...")
                time.sleep(60)

        log("done.")


if __name__ == "__main__":
    main()