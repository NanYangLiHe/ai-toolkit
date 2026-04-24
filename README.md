# 🤖 AI Toolkit

<div align="center">
  <img src="https://img.shields.io/github/stars/NanYangLiHe/ai-toolkit?style=flat-square" alt="Stars">
  <img src="https://img.shields.io/github/forks/NanYangLiHe/ai-toolkit?style=flat-square" alt="Forks">
  <img src="https://img.shields.io/github/issues/NanYangLiHe/ai-toolkit?style=flat-square" alt="Issues">
  <img src="https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square" alt="MIT License">
  <img src="https://img.shields.io/badge/python-3.8%2B-green.svg?style=flat-square" alt="Python 3.8+">
  <br><br>
  <strong>Free & Open Source AI Automation Tools for Developers</strong>
</div>

A collection of practical, production-ready scripts and tools powered by local LLMs. No API keys required, no cloud dependencies — run everything on your own machine.

A collection of practical, production-ready scripts and tools powered by local LLMs. No API keys required, no cloud dependencies — run everything on your own machine.

## ✨ Features

| Tool | Description | Status |
|------|-------------|--------|
| 📝 Auto-Writer | AI-powered content generator (articles, docs, translations) | ✅ Ready |
| 🔧 Code Assistant | Local code review & refactoring automation | ✅ Ready |
| 📊 Data Parser | Extract structured JSON/CSV from messy text (invoices, contacts) | ✅ Ready |
| 🌐 Web Scraper | Intelligently scrape websites and extract key information | ✅ Ready |

## 🚀 Quick Start

### Prerequisites
- Python 3.8+ or Node.js 18+
- Local LLM (Ollama, LM Studio, or any OpenAI-compatible API)

### Installation

```bash
# Clone the repo
git clone https://github.com/NanYangLiHe/ai-toolkit.git
cd ai-toolkit

# Install dependencies
pip install -r requirements.txt
# OR for Node.js tools:
npm install

# Configure your local LLM endpoint
cp .env.example .env
# Edit .env with your settings
```

### Usage Examples

#### Generate Content
```bash
python scripts/auto_writer.py --topic "AI in 2025" --language zh-CN
```

#### Code Review
```bash
python scripts/code_review.py --target ./your_project/
```

#### Data Extraction (JSON/CSV)
```bash
# Parse a single file
python scripts/data_parser.py --input invoice.txt --format json --schema invoice

# Batch parse all files in directory
python scripts/data_parser.py --input ./documents/ --format csv
```

#### Intelligent Web Scraping
```bash
# Scrape a single URL
python scripts/web_scraper.py --url https://example.com

# Scrape multiple URLs from file
python scripts/web_scraper.py --urls targets.txt --output results.json
```

## 📖 Documentation

See [docs/](docs/) for detailed guides on each tool.

## 💰 Support This Project

If you find this toolkit useful, consider supporting:

- ⭐ Star this repo (helps more people discover it!)
- ☕ Buy me a coffee: https://buymeacoffee.com/lihuai
- 💬 Share with your network

**ETH Wallet:** `0x99F42Cf98e928785FC2484304Be368EFaD9787Af`

## 📄 License

MIT License — Free to use, modify, and distribute.

---

*Built with ❤️ by 李槐 (Li Huai)*