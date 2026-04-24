# 📖 AI Toolkit Examples

Real-world usage examples for each tool. Copy-paste ready!

---

## 📝 Auto Writer

### Generate a technical article
```bash
python scripts/auto_writer.py --topic "Python async programming" --length 800 --output articles/async-guide.md
```

### Batch generate content (daily workflow)
```bash
# Create multiple articles in one command
for topic in AI automation devops python scripting machine learning; do
    python scripts/auto_writer.py --topic "$topic" --output "articles/$topic.md"
done
echo "✅ Generated 6 articles!"
```

---

## 🔧 Code Review

### Quick code analysis
```bash
# Review a single file
python scripts/code_review.py my_script.py

# Output includes:
# - Potential bugs detected
# - Performance optimization suggestions  
# - Best practices recommendations
```

### Full project review
```bash
# Review all Python files in directory
find . -name "*.py" -exec python scripts/code_review.py {} \; > code-review-report.txt
```

---

## 📊 Data Parser

### Extract invoice data from text
```bash
python scripts/data_parser.py --input invoices.txt --format json --schema invoice

# Output: structured JSON with fields like {date, amount, vendor, items...}
```

### Clean contact list
```bash
python scripts/data_parser.py --input contacts.csv --format json --schema person

# Normalizes names, emails, phone numbers into consistent format
```

---

## 🌐 Web Scraper

### Extract key insights from webpage
```bash
python scripts/web_scraper.py --url "https://example.com/article" --extract "key points"

# Returns: markdown summary of the page content
```

### Competitive analysis
```bash
# Scrape multiple competitor sites
for url in "site1.com" "site2.com" "site3.com"; do
    python scripts/web_scraper.py --url "$url" --extract "features, pricing" --output "competitors/$url.json"
done
```

---

## 🔍 SEO Optimizer

### Analyze content for search engines
```bash
python scripts/seo_optimizer.py --file article.md --output seo-report.json

# Report includes:
# - Word count & readability score
# - Keyword density analysis  
# - SEO recommendations (0-100 score)
```

---

## 🐦 Twitter Bot

### Post articles automatically
```bash
python scripts/twitter_bot.py --article articles/my-post.md --dry-run

# Preview tweets → remove --dry-run to actually post
```

---

## 🌍 AI Translator

### Translate content between languages
```bash
# English → Chinese (Simplified)
python scripts/ai_translator.py --file article.md --from en --to zh-CN --output article-zh.md

# Supports: en, zh-CN, ja, ko, fr, de, es...
```

---

## 🚀 Complete Workflow Example

```bash
#!/bin/bash
# daily-content.sh - Full content creation pipeline

TOPIC="Local AI deployment"

echo "📝 Generating article..."
python scripts/auto_writer.py --topic "$TOPIC" --output articles/$TOPIC.md

echo "🔍 Optimizing for SEO..."  
python scripts/seo_optimizer.py --file articles/$TOPIC.md --output reports/$TOPIC-seo.json

echo "🌍 Translating to Chinese..."
python scripts/ai_translator.py --file articles/$TOPIC.md --from en --to zh-CN --output articles/$TOPIC-zh.md

echo "✅ Content ready! Review and publish manually or with content_publisher.py"
```

---

💡 **Tip:** Combine these tools into automated workflows for maximum efficiency!

🌿 *Need help? Open an issue on [GitHub](https://github.com/NanYangLiHe/ai-toolkit/issues)*
