# 🤝 Contributing to AI Toolkit

Thank you for your interest in contributing! Here's how to help:

## Ways to Contribute

### 🐛 Report Bugs
- Use the [GitHub Issues](https://github.com/NanYangLiHe/ai-toolkit/issues) template
- Include steps to reproduce and expected vs actual behavior

### ✨ Request Features
- Search existing issues first (might already be planned!)
- Explain your use case clearly with examples

### 💻 Submit Code
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes following our coding standards
4. Write tests for new functionality
5. Update documentation if needed
6. Submit a Pull Request!

## Coding Standards

### Python Scripts
- Type hints where helpful (not required everywhere)
- Docstrings for all functions
- Maximum line length: 100 characters
- Use f-strings over format() or % formatting

```python
def process_text(input_file: str, output_format: str = "json") -> dict:
    """Process input file and return structured data.
    
    Args:
        input_file: Path to the text file to process
        output_format: Desired output format (json/csv)
        
    Returns:
        Dictionary containing processed results
    """
```

### Documentation
- Use markdown with clear hierarchy (# → ## → ###)
- Include code examples for every feature
- Keep language simple and direct (no marketing fluff)
- Add screenshots/GIFs when helpful

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/ai-toolkit.git
cd ai-toolkit

# Install dependencies
pip install -r requirements.txt

# Run tests to verify setup
python tests/test_tools.py
```

## Pull Request Checklist

- [ ] Code follows project style guidelines
- [ ] Tests added and passing (if applicable)
- [ ] Documentation updated
- [ ] No breaking changes to existing APIs
- [ ] Commit messages are clear and descriptive

## Community Guidelines

- Be respectful and constructive
- Assume good intentions
- Focus on the problem, not the person
- Help others learn — this is a learning project!

---

Questions? Open an issue or chat in our community channels. 🌿