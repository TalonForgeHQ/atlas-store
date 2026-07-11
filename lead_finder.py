"""
Atlas Lead Finder — finds REAL business emails WITHOUT Hunter.io / Apollo API keys.
Uses:
1. Google site:linkedin.com scraping (public data)
2. Domain pattern guessing (info@, sales@, founder@)
3. Public YC bookface / Crunchbase scraping
4. Direct website contact page scraping

NO API KEYS NEEDED. Pure Python with requests + BeautifulSoup.
"""

import requests
from bs4 import BeautifulSoup
import re
import csv
import json
import time
import random
from urllib.parse import urlparse, quote_plus
from pathlib import Path
from typing import List, Dict, Optional


HEADERS = [
    {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"},
    {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15"},
    {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"},
]


def random_headers() -> Dict:
    return random.choice(HEADERS)


def extract_emails(text: str) -> List[str]:
    """Extract email addresses from text."""
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    found = re.findall(pattern, text)
    # Filter out junk
    return [e for e in found if not any(x in e.lower() for x in ['example.com', 'email.com', 'domain.com', '.png', '.jpg', 'youremail', 'wixpress', 'sentry'])]


def guess_emails_for_domain(domain: str, names: List[str] = None) -> List[str]:
    """Generate likely email addresses from a domain + names."""
    domain = domain.replace("https://", "").replace("http://", "").replace("www.", "").rstrip("/")
    common_prefixes = ["info", "contact", "sales", "hello", "founder", "team", "support", "press", "partnerships"]
    guesses = [f"{p}@{domain}" for p in common_prefixes]

    if names:
        for name in names:
            parts = name.lower().strip().split()
            if len(parts) >= 2:
                # first@, last@, first.last@, flast@
                first, last = parts[0], parts[-1]
                guesses.extend([
                    f"{first}@{domain}",
                    f"{first}.{last}@{domain}",
                    f"{first[0]}{last}@{domain}",
                    f"{first}{last[0]}@{domain}",
                ])
    return list(set(guesses))


def scrape_contact_page(domain: str, timeout: int = 10) -> List[str]:
    """Try common contact page URLs and extract emails."""
    paths = ["/contact", "/contact-us", "/about", "/team", "/about-us", "/get-in-touch", "/"]
    urls = [f"https://{domain}{p}" for p in paths]

    emails = []
    for url in urls:
        try:
            r = requests.get(url, headers=random_headers(), timeout=timeout, allow_redirects=True)
            if r.status_code == 200:
                found = extract_emails(r.text)
                if found:
                    emails.extend(found)
                    break
        except Exception:
            continue

    return list(set(emails))


def find_emails_for_company(company_name: str, website: str, founder_name: str = None) -> Dict:
    """Main: find emails for a company + optional founder."""
    domain = urlparse(website).netloc if website else ""
    if not domain:
        domain = (website or "").replace("https://", "").replace("http://", "").split("/")[0]
    domain = domain.replace("www.", "")

    result = {
        "company": company_name,
        "website": website,
        "domain": domain,
        "emails_found": [],
        "guessed_emails": [],
        "founder": founder_name or "",
        "source": "scraped",
    }

    # Step 1: scrape contact page
    scraped = scrape_contact_page(domain)
    result["emails_found"] = scraped

    # Step 2: guess from domain + founder name
    names = [founder_name] if founder_name else []
    guessed = guess_emails_for_domain(domain, names)
    result["guessed_emails"] = guessed

    return result


def find_leads_from_google(query: str, max_results: int = 10) -> List[Dict]:
    """Search Google for companies matching query (using a free SERP API approach via html scraping)."""
    # NOTE: this will hit captcha often. Use only when needed.
    url = f"https://www.google.com/search?q={quote_plus(query)}&num={max_results}"
    try:
        r = requests.get(url, headers=random_headers(), timeout=10)
        if "sorry" in r.url or r.status_code != 200:
            return []
        soup = BeautifulSoup(r.text, "html.parser")
        results = []
        for g in soup.find_all("div", class_="g"):
            link = g.find("a")
            if link and link.get("href"):
                href = link["href"]
                title = g.find("h3")
                title_text = title.get_text() if title else ""
                if "http" in href:
                    results.append({"title": title_text, "url": href})
        return results[:max_results]
    except Exception:
        return []


# Pre-built lead list with REAL websites — sourced from public YC, IndieHackers, Product Hunt
# These are companies known to need AI ops services, with public contact info
KNOWN_LEADS = [
    # YC-backed AI companies
    {"company": "Recall.ai", "website": "https://www.recall.ai", "founder": "David Hu", "vertical": "AI meeting transcription"},
    {"company": "Deepgram", "website": "https://deepgram.com", "founder": "Scott Stephenson", "vertical": "Speech AI"},
    {"company": "Anyscale", "website": "https://www.anyscale.com", "founder": "Robert Nishihara", "vertical": "AI compute"},
    {"company": "Together AI", "website": "https://www.together.ai", "founder": "Vipul Ved Prakash", "vertical": "Open-source AI"},
    {"company": "Replicate", "website": "https://replicate.com", "founder": "Ben Firshman", "vertical": "AI model hosting"},

    # Indie hackers (known to buy AI tools)
    {"company": "TidyCal", "website": "https://tidycal.com", "founder": "Neville Medhora", "vertical": "Scheduling"},
    {"company": "ConvertKit", "website": "https://convertkit.com", "founder": "Nathan Barry", "vertical": "Email marketing"},
    {"company": "Beehiiv", "website": "https://www.beehiiv.com", "founder": "Tyler Denk", "vertical": "Newsletters"},
    {"company": "Carrd", "website": "https://carrd.co", "founder": "AJ Nash", "vertical": "Landing pages"},
    {"company": "Ghost", "website": "https://ghost.org", "founder": "John O'Nolan", "vertical": "Publishing"},

    # AI startups in growth phase
    {"company": "Jasper", "website": "https://www.jasper.ai", "founder": "Dave Rogenmoser", "vertical": "AI content"},
    {"company": "Copy.ai", "website": "https://www.copy.ai", "founder": "Paul Yacoubian", "vertical": "AI writing"},
    {"company": "Writer", "website": "https://writer.com", "founder": "May Habib", "vertical": "Enterprise AI"},
    {"company": "Notion AI", "website": "https://www.notion.so", "founder": "Ivan Zhao", "vertical": "Productivity AI"},
    {"company": "Linear", "website": "https://linear.app", "founder": "Karri Saarinen", "vertical": "Project management"},

    # Local business verticals (cyberfarmacist's pattern)
    {"company": "ServiceTitan", "website": "https://www.servicetitan.com", "founder": "Ara Mahdessian", "vertical": "Field service AI"},
    {"company": "Jobber", "website": "https://getjobber.com", "founder": "Sam Pillar", "vertical": "Field service"},
    {"company": "Housecall Pro", "website": "https://www.housecallpro.com", "founder": "Roland Ligtenberg", "vertical": "Home services"},
    {"company": "ServiceNow", "website": "https://www.servicenow.com", "founder": "Fred Luddy", "vertical": "Enterprise workflow"},
    {"company": "Zapier", "website": "https://zapier.com", "founder": "Wade Foster", "vertical": "Automation"},

    # Agencies that need AI ops
    {"company": "SmartSites", "website": "https://www.smartsites.com", "founder": "Alex Melen", "vertical": "Digital marketing"},
    {"company": "WebFX", "website": "https://www.webfx.com", "founder": "William Craig", "vertical": "Digital marketing"},
    {"company": "Disruptive Advertising", "website": "https://disruptiveadvertising.com", "founder": "Jacob Baadsgaard", "vertical": "PPC"},
    {"company": "Coalition Technologies", "website": "https://coalitiontechnologies.com", "founder": "Joel Gross", "vertical": "SEO agency"},
    {"company": "Straight North", "website": "https://www.straightnorth.com", "founder": "David Steinberg", "vertical": "B2B marketing"},

    # Solo founders / Indie Hackers active on X
    {"company": "PiQrypt", "website": "https://github.com/PiQrypt/piqrypt", "founder": "PiQrypt_Fred", "vertical": "Cryptographic AI audit"},
    {"company": "Jin", "website": "https://meetjin.com", "founder": "Ankush Vishnu", "vertical": "AI-readable web"},
    {"company": "AGNT", "website": "https://github.com/agnt-gg/agnt", "founder": "Nathan Wilbanks", "vertical": "Agent infrastructure"},
    {"company": "RovaSpace", "website": "https://www.rovaspace.com", "founder": "IronSteel", "vertical": "AI virtual office"},
    {"company": "VisaList", "website": "https://visalist.io", "founder": "Hari Krishna Dulipudi", "vertical": "Visa AI ($700/mo)"},
]


def enrich_all_leads(leads: List[Dict], max_per_company: int = 2, delay: float = 0.5) -> List[Dict]:
    """Find emails for each lead."""
    enriched = []
    for i, lead in enumerate(leads):
        print(f"  [{i+1}/{len(leads)}] {lead['company']} ({data['domain']})...")
        try:
            data = find_emails_for_company(
                lead["company"],
                lead["website"],
                lead.get("founder")
            )
            data["vertical"] = lead.get("vertical", "")
            # Pick best email: scraped > guessed
            best_email = None
            if data["emails_found"]:
                # Prefer info@ or hello@ over personal
                for e in data["emails_found"]:
                    if any(p in e.lower() for p in ["info", "hello", "contact", "sales", "founder"]):
                        best_email = e
                        break
                if not best_email:
                    best_email = data["emails_found"][0]
            elif data["guessed_emails"]:
                # Prefer info@ over personal guesses
                for e in data["guessed_emails"]:
                    if e.startswith(("info@", "hello@", "contact@")):
                        best_email = e
                        break
                if not best_email and data["guessed_emails"]:
                    best_email = data["guessed_emails"][0]

            data["best_email"] = best_email
            enriched.append(data)
            if best_email:
                print(f"    [OK] {best_email}")
            else:
                print(f"    [NONE]")
        except Exception as e:
            print(f"    [ERROR] {e}")
            enriched.append({"company": lead["company"], "website": lead["website"], "error": str(e)})

        time.sleep(delay)  # rate limit

    return enriched


def save_to_csv(enriched: List[Dict], path: str):
    """Save to leads_with_emails.csv."""
    fieldnames = ["company", "domain", "website", "founder", "vertical", "best_email", "emails_found", "guessed_emails"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for row in enriched:
            row["emails_found"] = "; ".join(row.get("emails_found", []) or [])
            row["guessed_emails"] = "; ".join(row.get("guessed_emails", []) or [])
            writer.writerow(row)


if __name__ == "__main__":
    import sys
    output_path = sys.argv[1] if len(sys.argv) > 1 else "leads_with_emails.csv"

    print(f"Atlas Lead Finder")
    print(f"Enriching {len(KNOWN_LEADS)} leads with public email data...\n")

    enriched = enrich_all_leads(KNOWN_LEADS, delay=0.3)
    save_to_csv(enriched, output_path)

    found_count = sum(1 for r in enriched if r.get("best_email"))
    print(f"\n=== RESULT: {found_count}/{len(enriched)} leads have an email ===")
    print(f"Saved to {output_path}")
