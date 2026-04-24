#!/usr/bin/env python3
"""
Content Publisher - Auto-publish articles to multiple platforms
Usage: python content_publisher.py --platform devto|medium|both [--api-key KEY]
"""
import argparse
import json
import time
from pathlib import Path

def load_article(filepath):
    """Load markdown article and format for platform"""
    content = Path(filepath).read_text(encoding="utf-8")
    
    # Extract metadata
    lines = content.split("\n")
    title = ""
    body_start = 1
    
    for i, line in enumerate(lines):
        if line.startswith("# "):
            title = line[2:].strip()
            body_start = i + 1
            break
    
    # Clean up for platform-specific formatting
    clean_content = "\n".join(lines[body_start:])
    
    return {
        "title": title,
        "content_markdown": content,
        "content_clean": clean_content,
        "tags": extract_tags(content),
        "word_count": len(content.split()),
    }

def extract_tags(content):
    """Extract relevant tags from content"""
    tag_keywords = {
        "AI": ["AI", "artificial intelligence", "machine learning"],
        "Python": ["python", "scripting"],
        "OpenSource": ["open source", "opensource", "GitHub"],
        "Automation": ["automation", "workflow"],
        "DevOps": ["devops", "deployment", "CI/CD"],
    }
    
    content_lower = content.lower()
    tags = []
    for tag, keywords in tag_keywords.items():
        if any(kw in content_lower for kw in keywords):
            tags.append(tag)
    
    # Ensure at least 4 tags (Dev.to requirement)
    while len(tags) < 4:
        tags.append(f"Tech{len(tags)+1}")
    
    return tags[:4]

def format_for_devto(article):
    """Format article for Dev.to"""
    return {
        "title": article["title"],
        "body_markdown": article["content_clean"],
        "tags": article["tags"],
        "published": True,
        "canonical_url": f"https://github.com/NanYangLiHe/ai-toolkit/blob/main/articles/{Path(article['file']).name}",
    }

def format_for_medium(article):
    """Format article for Medium (HTML)"""
    # Simple markdown to HTML conversion
    html = article["content_clean"].replace("# ", "<h1>").replace("## ", "<h2>")
    html += "</h1></h2>"  # Close tags
    
    return {
        "title": article["title"],
        "content_html": html,
        "tags": article["tags"],
        "publish_status": "public",
    }

def main():
    parser = argparse.ArgumentParser(description="Auto-publish articles to content platforms")
    parser.add_argument("--article", "-a", required=True, help="Article markdown file")
    parser.add_argument("--platform", "-p", choices=["devto", "medium", "both"], default="both",
                       help="Target platform(s)")
    parser.add_argument("--api-key-devto", help="Dev.to API key")
    parser.add_argument("--api-key-medium", help="Medium API key (MID token)")
    parser.add_argument("--dry-run", action="store_true", help="Preview without posting")
    
    args = parser.parse_args()
    
    article = load_article(args.article)
    
    print(f"📝 Article: {article['title']}")
    print(f"   Words: {article['word_count']}, Tags: {', '.join(article['tags'])}\n")
    
    # Dev.to
    if args.platform in ["devto", "both"]:
        devto_post = format_for_devto(article)
        print("🐦 Dev.to Post:")
        print(json.dumps(devto_post, indent=2))
        
        if not args.dry_run and args.api_key_devto:
            # TODO: Implement actual API call
            pass
    
    # Medium
    if args.platform in ["medium", "both"]:
        medium_post = format_for_medium(article)
        print("\n📖 Medium Post:")
        print(json.dumps(medium_post, indent=2))
        
        if not args.dry_run and args.api_key_medium:
            # TODO: Implement actual API call
            pass

if __name__ == "__main__":
    main()
