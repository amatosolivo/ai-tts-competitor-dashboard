import sys
import os
import json
import subprocess

with open("data/data.json", "r") as f:
    data = json.load(f)

scraped_count = 0
for competitor in data["competitors"]:
    name = competitor["metadata"]["name"]
    pages = competitor["discovery"].get("relevant_pages", [])
    
    # We only scrape up to 3 most relevant pages per competitor to save time/noise
    # Prioritizing 'pricing'
    pricing_pages = [p for p in pages if 'pricing' in p.lower()]
    other_pages = [p for p in pages if 'pricing' not in p.lower()]
    
    to_scrape = (pricing_pages + other_pages)[:3]
    
    print(f"Scraping for {name} ({len(to_scrape)} pages)...")
    
    for url in to_scrape:
        try:
            print(f"  - {url}")
            subprocess.run(
                ["python3", "src/scraping/scraping_engine.py", url],
                check=True,
                capture_output=True,
                timeout=20
            )
            scraped_count += 1
        except subprocess.TimeoutExpired:
            print(f"    ! Timeout scraping {url}")
        except Exception as e:
            print(f"    ! Failed to scrape {url}: {e}")

print(f"Scraping complete. Total pages scraped: {scraped_count}")
