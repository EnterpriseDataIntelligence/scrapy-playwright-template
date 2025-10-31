import requests, csv
from bs4 import BeautifulSoup
from datetime import datetime
from pathlib import Path

OUT = Path("data/processed"); OUT.mkdir(parents=True, exist_ok=True)
fname = OUT / f"news_{datetime.utcnow():%Y%m%d_%H%M%S}.csv"

url = "https://news.ycombinator.com/"
r = requests.get(url, timeout=20); r.raise_for_status()
soup = BeautifulSoup(r.text, "html.parser")
rows = [(a.text, a["href"]) for a in soup.select(".titleline a")]

with open(fname, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["title","url","scraped_at_utc"])
    for t,u in rows:
        w.writerow([t, u, datetime.utcnow().isoformat(timespec="seconds")])

print(f"✅ Saved {len(rows)} headlines → {fname}")
