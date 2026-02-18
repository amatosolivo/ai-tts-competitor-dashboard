import sys
import os
import json
import httpx
from bs4 import BeautifulSoup
from typing import List, Dict, Optional
import time

class ScrapingEngine:
    def __init__(self, output_dir: str = "logs/scrapes"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }

    def htm_to_markdown(self, html_content: str) -> str:
        """
        Simplistic HTML to Markdown converter to reduce noise for AI processing.
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Remove script and style elements
        for script_or_style in soup(["script", "style", "nav", "footer", "header"]):
            script_or_style.decompose()

        # Get text
        text = soup.get_text(separator='\n')
        
        # Break into lines and remove leading and trailing whitespace
        lines = (line.strip() for line in text.splitlines())
        # Break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # Drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
        
        return text

    def scrape_url(self, url: str) -> Optional[str]:
        """
        Fetches and cleans a URL.
        """
        try:
            with httpx.Client(headers=self.headers, follow_redirects=True, timeout=15.0) as client:
                response = client.get(url)
                response.raise_for_status()
                
            markdown = self.htm_to_markdown(response.text)
            
            # Save to log for provenance
            filename = url.replace('https://', '').replace('/', '_').replace(':', '_') + ".md"
            filepath = os.path.join(self.output_dir, filename)
            with open(filepath, "w") as f:
                f.write(markdown)
                
            return markdown
        except Exception as e:
            print(f"Error scraping {url}: {e}", file=sys.stderr)
            return None

if __name__ == "__main__":
    if len(sys.argv) > 1:
        engine = ScrapingEngine()
        url = sys.argv[1]
        print(f"Scraping {url}...", file=sys.stderr)
        content = engine.scrape_url(url)
        if content:
            print(content[:500] + "...")
    else:
        print("Usage: python3 scraping_engine.py <url>")
