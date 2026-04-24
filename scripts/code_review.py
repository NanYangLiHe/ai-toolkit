#!/usr/bin/env python3
"""
AI Code Review - Automated code analysis and improvement suggestions.

Review your code locally using AI without sending anything to the cloud.

Usage:
    python code_review.py --target ./your_project/
    python code_review.py --file specific_file.py
"""

import argparse
import os
import glob


def review_code(file_path, model_url="http://localhost:1234/v1/chat/completions"):
    """Review a single file using local LLM."""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()
    
    # Limit to first 500 lines for review context
    lines = code.split('\n')[:500]
    code_snippet = '\n'.join(lines)
    
    prompt = f"""You are a senior software engineer doing a code review.

Review the following code and provide:
1. 🐛 Bugs or potential issues (critical first)
2. ⚡ Performance improvements
3. 📝 Code style and best practices
4. 🔒 Security concerns (if any)
5. 💡 Suggestions for refactoring

Be specific with line numbers where possible.
Rate the overall quality: ⭐⭐⭐⭐⭐

Code to review ({os.path.basename(file_path)}):
```python
{code_snippet}
```"""

    try:
        import requests
        
        response = requests.post(
            model_url,
            json={
                "model": "local",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.3,
                "max_tokens": 4096
            },
            timeout=180
        )
        
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content']
            
    except Exception as e:
        print(f"❌ Review failed: {e}")
    
    return None


def scan_directory(target_dir, extensions=['*.py', '*.js', '*.ts'], model_url="http://localhost:1234/v1/chat/completions"):
    """Scan a directory and review all matching files."""
    
    results = {}
    file_count = 0
    
    for ext in extensions:
        pattern = os.path.join(target_dir, f'**/{ext}')
        files = glob.glob(pattern, recursive=True)
        
        for filepath in files[:10]:  # Limit to first 10 files per extension
            if 'node_modules' in filepath or '.git' in filepath:
                continue
            
            print(f"🔍 Reviewing: {filepath}")
            review = review_code(filepath, model_url)
            
            if review:
                results[filepath] = review
                file_count += 1
    
    return results, file_count


def main():
    parser = argparse.ArgumentParser(description="AI Code Review - Local LLM code analysis")
    parser.add_argument("--target", type=str, help="Directory to scan")
    parser.add_argument("--file", type=str, help="Specific file to review")
    parser.add_argument("--model-url", type=str, default=os.getenv("LLM_API_URL"))
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("🔍 AI Code Reviewer")
    print("=" * 60)
    
    if args.file:
        result = review_code(args.file, args.model_url)
        if result:
            print("\n" + result)
    
    elif args.target:
        results, count = scan_directory(args.target, model_url=args.model_url)
        print(f"\n✅ Reviewed {count} files")


if __name__ == "__main__":
    main()