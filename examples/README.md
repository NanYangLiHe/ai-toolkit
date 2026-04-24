# 📚 Examples & Use Cases

Real-world examples showing how to use AI Toolkit effectively.

## Example 1: Technical Blog Post Generator

Generate a complete technical blog post with code examples:

```bash
# Step 1: Generate article outline
python scripts/auto_writer.py \
  --topic "Building Local AI Workflows" \
  --language en-US > draft.md

# Step 2: Translate to Chinese (if needed)
python scripts/auto_writer.py \
  --input draft.md \
  --action translate \
  --target-lang zh-CN
```

**Output:** Professional blog post ready for publication! 📝

---

## Example 2: Code Quality Pipeline

Automate code review before pushing to production:

```bash
# Review all Python files in your project
python scripts/code_review.py --target ./my_project/

# Focus on a specific file
python scripts/code_review.py --file critical_module.py
```

**What you get:**
- Bug detection with line numbers
- Performance optimization suggestions  
- Security vulnerability alerts
- Refactoring recommendations

---

## Example 3: Invoice Data Extraction

Turn messy invoice PDFs into clean JSON data:

```bash
# Extract structured data from invoice text
python scripts/data_parser.py \
  --input invoice_text.txt \
  --format json \
  --schema invoice > invoice_data.json
```

**Sample Output:**
```json
{
  "invoice_number": "INV-2024-1234",
  "date": "2024-06-15",
  "vendor": "Cloud Services Inc.",
  "amount": "$1,250.00",
  "items": [
    {
      "description": "Monthly cloud hosting",
      "quantity": 1,
      "unit_price": "$1,250.00"
    }
  ],
  "tax": "$75.00",
  "total": "$1,325.00"
}
```

---

## Example 4: Competitive Analysis Scraper

Gather competitor information automatically:

```bash
# Create URL list file
echo "https://competitor1.com/pricing" > competitors.txt
echo "https://competitor2.com/features" >> competitors.txt

# Scrape and analyze
python scripts/web_scraper.py \
  --urls competitors.txt \
  --prompt "Extract pricing tiers, features, and target audience" \
  --output analysis.json
```

**Perfect for:** Market research, competitive intelligence, content aggregation.

---

## Example 5: Prompt Engineering Workshop

Generate optimized prompts for specific tasks:

```bash
# Create a prompt for technical translation
python scripts/prompt_generator.py \
  --task "Translate API documentation from English to Chinese" \
  --style professional > api_doc_prompt.md
```

**Use case:** Building prompt templates for consistent AI output quality.

---

## Tips for Best Results

### Hardware Optimization
- **CPU-only:** Use quantized models (Q4_K_M or Q5_K_M)
- **GPU available:** Try FP16 or GGUF with higher precision
- **Memory constraints:** Start with 3B/7B parameter models

### Prompt Quality
- Be specific about desired output format
- Include examples when possible
- Specify tone and audience clearly
- Break complex tasks into smaller steps

### Automation Ideas
- Set up GitHub Actions for automatic code reviews
- Schedule weekly content generation scripts
- Create custom CLI wrappers for your workflow

---

*Have a cool use case? Share it in our [Discussions](https://github.com/NanYangLiHe/ai-toolkit/discussions)!* 🌿