
import os
import requests
import time
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urlunparse

# ✅ Setup Paths
PROJECT_ROOT = "/content/drive/MyDrive/super-bowl-ad-analysis"
DATA_DIR = os.path.join(PROJECT_ROOT, "data", "raw", "youtube_gemini")
os.makedirs(DATA_DIR, exist_ok=True)
OUTPUT_FILE = os.path.join(DATA_DIR, "homepage_youtube_links.txt")
BASE_URL = "https://www.superbowl-ads.com"

# ✅ Helper: Normalize URL
def normalize_url(url):
    url = url.strip().lower().rstrip('/')
    parsed = urlparse(url)
    return urlunparse((parsed.scheme, parsed.netloc, parsed.path.rstrip('/'), '', '', ''))

# ✅ Step 1: Scrape homepage links
homepage_url = BASE_URL
res = requests.get(homepage_url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(res.text, "html.parser")
homepage_links = [a['href'] for a in soup.find_all('a', href=True)]
print(f"🔗 Found {len(homepage_links)} homepage links")

# ✅ Step 2: Filter YouTube-embed pages (no duplicates)
full_links = []
seen_links = set()

for link in homepage_links:
    if link.startswith("http"):
        full_url = link
    elif link.startswith("/"):
        full_url = BASE_URL.rstrip("/") + link
    else:
        continue

    norm = normalize_url(full_url)
    if norm not in seen_links:
        full_links.append(full_url)
        seen_links.add(norm)

youtube_pages = set()

for url in full_links:
    try:
        res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        found = any("youtube.com" in iframe.get("src", "") for iframe in soup.find_all("iframe"))
        if not found:
            found = any("youtube.com/watch" in a.get("href", "") for a in soup.find_all("a", href=True))
        if found:
            youtube_pages.add(normalize_url(url))
            print(f"✅ YouTube found: {url}")
    except Exception as e:
        print(f"⚠️ Error processing {url}: {e}")
    time.sleep(0.5)

# ✅ Save results
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for link in sorted(youtube_pages):
        f.write(link + "\n")

print(f"🎯 Total unique pages with YouTube links: {len(youtube_pages)}")
