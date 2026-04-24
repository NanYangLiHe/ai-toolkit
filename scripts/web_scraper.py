#!/usr/bin/env python3
"""
AI Web Scraper - Intelligent web scraping with AI-powered parsing.

Extract meaningful information from websites using local LLMs.

Usage:
    python web_scraper.py --url https://example.com --output data.json
    python web_scraper.py --urls list.txt --format csv
"""

import argparse
import json
import os
import time


def fetch_page(url, timeout=30):
    """Fetch webpage content."""
    
    try:
        import requests
        
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; AI-Toolkit/1.0)"
        }
        
        response = requests.get(
            url, 
            headers=headers, 
            timeout=timeout
        )
        
        if response.status_code == 200:
            return extract_text(response.text)
            
    except ImportError:
        print("⚠️  requests library required. Run: pip install beautifulsoup4")
    except Exception as e:
        print(f"❌ Failed to fetch {url}: {e}")
    
    return None


def extract_text(html):
    """Extract readable text from HTML."""
    
    try:
        from bs4 import BeautifulSoup
        
        soup = BeautifulSoup(html, 'html.parser')
        
        # Remove script and style elements
        for element in soup(['script', 'style']):
            element.decompose()
        
        return soup.get_text(separator='\n', strip=True)[:10000]
            
    except ImportError:
        # Fallback: basic regex extraction
        import re
        text = re.sub('<[^<]+>', '', html)
        return '\n'.join(line.strip() for line in text.split('\n') if line.strip())[:10000]


def parse_content(text, prompt=None, model_url="http://localhost:1234/v1/chat/completions"):
    """Use AI to extract structured data from web content."""
    
    if not prompt:
        prompt = """Extract the key information from this webpage as JSON.
Include: title, main_topics[], key_points[], links[]"""
    
    ai_prompt = f"{prompt}\n\nWebpage content:\n---\n{text[:8000]}\n---"
    
    try:
        import requests
        
        response = requests.post(
            model_url,
            json={
                "model": "local",
                "messages": [{"role": "user", "content": ai_prompt}],
                "temperature": 0.3,
                "max_tokens": 4096
            },
            timeout=180
        )
        
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content']
            
    except Exception as e:
        print(f"❌ AI parsing failed: {e}")
    
    return None


def scrape_urls(url_list, output_format="json", prompt=None, model_url="http://localhost:1234/v1/chat/completions"):
    """Scrape multiple URLs and compile results."""
    
    results = []
    
    for i, url in enumerate(url_list):
        print(f"\n📄 [{i+1}/{len(url_list)}] Scraping: {url}")
        
        text = fetch_page(url)
        
        if text:
            parsed = parse_content(text, prompt=prompt, model_url=model_url)
            
            results.append({
                "url": url,
                "raw_text": text[:2000],  # Keep first 2K chars
                "parsed": parsed or "Parsing failed"
            })
        
        time.sleep(1)  # Be polite to servers
    
    return results


def main():
    parser = argparse.ArgumentParser(description="AI Web Scraper")
    parser.add_argument("--url", type=str, help="Single URL to scrape")
    parser.add_argument("--urls", type=str, help="File containing list of URLs")
    parser.add_argument("--prompt", type=str, help="Custom parsing prompt for AI")
    parser.add_argument("--output", type=str, default="scraped_data.json", help="Output file path")
    parser.add_argument("--model-url", type=str, default=os.getenv("LLM_API_URL"))
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("🌐 AI Web Scraper")
    print("=" * 60)
    
    # Get URLs to scrape
    urls = []
    
    if args.url:
        urls.append(args.url)
    
    if args.urls:
        with open(args.urls, 'r', encoding='utf-8') as f:
            urls.extend(line.strip() for line in f if line.strip())
    
    if not urls:
        parser.error("Provide --url or --urls file")
    
    # Scrape and save results
    results = scrape_urls(urls, model_url=args.model_url)
    
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Results saved to: {args.output}")


if __name__ == "__main__":
    main()