# 🚀 Quick Start Guide

Get AI Toolkit running in 5 minutes!

## Prerequisites

| Requirement | Minimum Version | Notes |
|-------------|-----------------|-------|
| Python | 3.8+ | Or Node.js 18+ for JS tools |
| Local LLM | Any OpenAI-compatible API | Ollama, LM Studio, vLLM, etc. |
| RAM | 8GB+ | More is better for larger models |

## Installation Steps

### Step 1: Clone the Repository

```bash
git clone https://github.com/NanYangLiHe/ai-toolkit.git
cd ai-toolkit
```

### Step 2: Install Dependencies

**Python tools:**
```bash
pip install -r requirements.txt
```

**Node.js tools (optional):**
```bash
npm install
```

### Step 3: Configure Your LLM Endpoint

Create a `.env` file:
```bash
cp .env.example .env
```

Edit `.env`:
```ini
# For LM Studio (default port)
LLM_API_URL=http://localhost:1234/v1/chat/completions

# For Ollama
LLM_API_URL=http://localhost:11434/v1/chat/completions

# For vLLM
LLM_API_URL=http://localhost:8000/v1/chat/completions
```

### Step 4: Test Your Setup

Run a quick test with Auto Writer:
```bash
python scripts/auto_writer.py --topic "Hello World" --language en-US
```

If you see output, you're good to go! 🎉

## Tool Overview

| Tool | Command Example | Use Case |
|------|-----------------|----------|
| **Auto Writer** | `--topic "AI Trends"` | Generate articles/docs |
| **Code Review** | `--file script.py` | Analyze code quality |
| **Data Parser** | `--input notes.txt --format json` | Extract structured data |
| **Web Scraper** | `--url https://example.com` | Scrape & parse websites |

## Troubleshooting

### "Connection refused"
- Make sure your LLM server is running
- Check the port in `.env` matches your server's settings

### "Out of memory" error
- Try a smaller model (7B parameters or less)
- Reduce `max_tokens` in tool configuration

### Slow responses
- Normal for local inference! Use quantized models for speed
- Consider using Ollama with faster backends (e.g., llama.cpp)

## Next Steps

1. Read the [Auto Writer Guide](writer_guide.md) to generate content
2. Check out the [Code Review Guide](review_guide.md) for code analysis
3. Explore advanced configurations in each tool's documentation

---

*Stuck? Open an issue on GitHub!*