import sys
import json
import httpx
from bs4 import BeautifulSoup
from typing import List, Dict, Set
from urllib.parse import urljoin, urlparse
import time

class DiscoveryEngine:
    def __init__(self):
        self.priority_keywords = [
            'pricing', 'price', 'rates', 'plans',
            'features', 'capabilities', 'tech',
            'compare', 'vs', 'alternatives',
            'enterprise', 'pro', 'business', 'pricing-plans'
        ]
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }

    def _is_internal(self, base_url: str, link: str) -> bool:
        base_domain = urlparse(base_url).netloc
        link_domain = urlparse(link).netloc
        return link_domain == "" or link_domain == base_domain

    def discover_pages(self, homepage: str) -> List[str]:
        """
        Crawls the homepage and finds relevant internal links based on priority keywords.
        """
        try:
            with httpx.Client(headers=self.headers, follow_redirects=True, timeout=10.0) as client:
                response = client.get(homepage)
                response.raise_for_status()
                
            soup = BeautifulSoup(response.text, 'html.parser')
            links: Set[str] = set()
            
            for a in soup.find_all('a', href=True):
                href = a['href']
                full_url = urljoin(homepage, href)
                
                # Check if internal and contains keywords
                if self._is_internal(homepage, full_url):
                    path = urlparse(full_url).path.lower()
                    if any(keyword in path for keyword in self.priority_keywords):
                        # Clean fragments and trailing slashes
                        clean_url = full_url.split('#')[0].rstrip('/')
                        links.add(clean_url)
            
            return sorted(list(links))
        except Exception as e:
            print(f"Error crawling {homepage}: {e}", file=sys.stderr)
            return []

    def generate_competitor_stub(self, homepage: str) -> Dict:
        """
        Creates a discovery-based stub for a competitor.
        """
        name = urlparse(homepage).netloc.replace('www.', '').split('.')[0].capitalize()
        discovered = self.discover_pages(homepage)
        
        return {
            "metadata": {
                "name": name,
                "homepage": homepage,
                "last_crawl": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "status": "discovery_complete"
            },
            "discovery": {
                "relevant_pages": discovered
            },
            "pricing": {"plans": []},
            "capabilities": [],
            "scores": {}
        }

if __name__ == "__main__":
    engine = DiscoveryEngine()
    if len(sys.argv) > 1:
        homepage_url = sys.argv[1]
        print(f"Discovering relevant pages for: {homepage_url}...", file=sys.stderr)
        stub = engine.generate_competitor_stub(homepage_url)
        print(json.dumps(stub, indent=2))
    else:
        print("Usage: python3 discovery_engine.py <homepage_url>")
