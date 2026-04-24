#!/usr/bin/env python3
"""
SEO Optimizer - Analyze and improve content for search engines
Usage: python seo_optimizer.py --file article.md [--output report.json]
"""
import json
import argparse
from pathlib import Path
from collections import Counter

def analyze_content(text):
    """Analyze text for SEO metrics"""
    words = text.lower().split()
    word_count = len(words)
    
    # Keyword density analysis
    stop_words = {"the", "a", "an", "is", "are", "was", "were", "be", "been", 
                  "being", "have", "has", "had", "do", "does", "did", "will",
                  "would", "could", "should", "may", "might", "must", "shall",
                  "can", "need", "dare", "ought", "used", "to", "of", "in", 
                  "for", "on", "with", "at", "by", "from", "as", "into", 
                  "through", "during", "before", "after", "above", "below",
                  "between", "out", "off", "over", "under", "again", "further",
                  "then", "once", "here", "there", "when", "where", "why", 
                  "how", "all", "both", "each", "few", "more", "most", "other",
                  "some", "such", "no", "nor", "not", "only", "own", "same",
                  "so", "than", "too", "very", "just", "because", "but", 
                  "and", "or"}
    
    meaningful_words = [w for w in words if w not in stop_words]
    word_freq = Counter(meaningful_words)
    top_keywords = word_freq.most_common(10)
    
    # Calculate keyword density
    keyword_density = []
    for word, count in top_keywords:
        density = (count / len(meaningful_words)) * 100 if meaningful_words else 0
        keyword_density.append({"keyword": word, "count": count, "density": f"{density:.2f}%"})
    
    # Readability metrics
    sentences = text.split(".")
    avg_sentence_length = word_count / len(sentences) if sentences else 0
    
    # Character counts
    char_count = len(text.replace(" ", "").replace("\n", ""))
    
    return {
        "word_count": word_count,
        "character_count": char_count,
        "sentence_count": len(sentences),
        "avg_sentence_length": f"{avg_sentence_length:.1f} words",
        "top_keywords": keyword_density[:5],
        "seo_score": calculate_seo_score(word_count, avg_sentence_length, top_keywords)
    }

def calculate_seo_score(word_count, avg_sentence_len, keywords):
    """Calculate SEO score (0-100)"""
    score = 0
    
    # Word count scoring
    if word_count >= 300:
        score += 20
    elif word_count >= 200:
        score += 15
    elif word_count >= 100:
        score += 10
    
    # Sentence length scoring (ideal: 15-20 words)
    if 15 <= avg_sentence_len <= 20:
        score += 20
    elif 10 <= avg_sentence_len <= 25:
        score += 15
    
    # Keyword diversity
    unique_keywords = len(set([k["keyword"] for k in keywords]))
    if unique_keywords >= 8:
        score += 30
    elif unique_keywords >= 5:
        score += 20
    
    # Bonus points
    score += min(word_count // 100 * 10, 30)
    
    return min(score, 100)

def main():
    parser = argparse.ArgumentParser(description="Analyze and optimize content for SEO")
    parser.add_argument("--file", "-f", required=True, help="Markdown file to analyze")
    parser.add_argument("--output", "-o", help="Output JSON report file")
    
    args = parser.parse_args()
    
    file_path = Path(args.file)
    if not file_path.exists():
        print(f"File not found: {file_path}")
        return
    
    content = file_path.read_text(encoding="utf-8")
    analysis = analyze_content(content)
    
    # Print report
    print("\n📊 SEO Analysis Report")
    print("="*50)
    print(f"Words: {analysis['word_count']}")
    print(f"Characters: {analysis['character_count']}")
    print(f"Sentence Count: {analysis['sentence_count']}")
    print(f"Avg Sentence Length: {analysis['avg_sentence_length']}")
    print(f"\nTop Keywords:")
    for kw in analysis['top_keywords']:
        print(f"  • {kw['keyword']}: {kw['count']} ({kw['density']})")
    
    print(f"\n🎯 SEO Score: {analysis['seo_score']}/100")
    
    # Recommendations
    if analysis['word_count'] < 300:
        print("\n⚠️  Recommendation: Increase content length to at least 300 words for better ranking")
    if analysis['avg_sentence_length'].endswith('words') and float(analysis['avg_sentence_length'].split()[0]) > 25:
        print("⚠️  Recommendation: Break up long sentences for better readability")
    
    # Save report if output specified
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(analysis, f, indent=2)

if __name__ == "__main__":
    main()
