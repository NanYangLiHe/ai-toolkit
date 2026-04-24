#!/usr/bin/env python3
"""
Twitter/X Bot - Auto post tech content to drive traffic
Usage: python twitter_bot.py --api-key KEY --api-secret SECRET --bearer-token TOKEN
"""
import argparse
import json
import time
from pathlib import Path

def load_articles():
    """Load articles from the articles directory"""
    articles_dir = Path(__file__).parent.parent / "articles"
    if not articles_dir.exists():
        print("No articles found. Create markdown files in articles/ first.")
        return []
    
    articles = []
    for md_file in articles_dir.glob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        # Extract title (first line starting with #)
        lines = content.split("\n")
        title = ""
        for line in lines:
            if line.startswith("# "):
                title = line[2:].strip()
                break
        
        # Get first 100 chars as preview
        body_lines = [l.strip() for l in lines[1:] if l.strip()]
        preview = " ".join(body_lines[:3])[:250] + "..."
        
        articles.append({
            "title": title,
            "preview": preview,
            "content": content,
            "file": md_file.name,
        })
    
    return articles

def format_tweet(article):
    """Format article as a tweet thread"""
    tweets = []
    
    # Main tweet with link
    main_tweet = f"📝 New: {article['title']}\n\n{article['preview'][:150]}\n\nGitHub: https://github.com/NanYangLiHe/ai-toolkit\n\n#AI #OpenSource #Python"
    tweets.append(main_tweet)
    
    # Thread continuation (split into chunks of 280 chars)
    content = article["content"]
    chunk_size = 260
    for i in range(0, min(len(content), 1500), chunk_size):
        tweets.append(content[i:i+chunk_size])
    
    return tweets

def main():
    parser = argparse.ArgumentParser(description="Auto-post articles to Twitter/X")
    parser.add_argument("--api-key", help="Twitter API Key")
    parser.add_argument("--api-secret", help="Twitter API Secret") 
    parser.add_argument("--bearer-token", help="Twitter Bearer Token")
    parser.add_argument("--dry-run", action="store_true", help="Preview tweets without posting")
    
    args = parser.parse_args()
    
    articles = load_articles()
    if not articles:
        return
    
    print(f"Found {len(articles)} articles to post\n")
    
    for article in articles:
        print(f"📌 {article['title']}")
        
        tweets = format_tweet(article)
        for i, tweet in enumerate(tweets):
            print(f"\n--- Tweet {i+1} ---")
            print(tweet[:280])
            if not args.dry_run:
                # TODO: Implement actual Twitter API posting
                pass
        
        print("\n" + "="*60)
        time.sleep(5)  # Rate limiting

if __name__ == "__main__":
    main()
