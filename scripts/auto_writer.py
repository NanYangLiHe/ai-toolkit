#!/usr/bin/env python3
"""
AI Auto-Writer - Content generation powered by local LLMs.

Generate articles, documentation, translations, and more
using your own local language model. No API costs!

Usage:
    python auto_writer.py --topic "Your topic here" --language en-US
    python auto_writer.py --input file.md --action translate --target-lang zh-CN
"""

import argparse
import json
import os
from datetime import datetime


def generate_content(topic, language="en-US", model_url="http://localhost:1234/v1/chat/completions"):
    """Generate content using local LLM."""
    
    prompt = f"""You are a professional technical writer. Write a comprehensive article about: {topic}

Requirements:
- Language: {language}
- Length: 800-1200 words
- Include practical examples and actionable insights
- Use markdown formatting with headers, lists, and code blocks where appropriate
- Make it engaging and easy to read
- End with a summary section

Write the article now:"""

    try:
        import requests
        
        response = requests.post(
            model_url,
            json={
                "model": "local",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7,
                "max_tokens": 4096
            },
            timeout=120
        )
        
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content']
        else:
            print(f"❌ Error: {response.status_code}")
            print(response.text)
            return None
            
    except ImportError:
        print("⚠️  requests library not installed. Run: pip install requests")
        return None
    except Exception as e:
        print(f"❌ Failed to generate content: {e}")
        print("\n💡 Tip: Make sure your local LLM server is running!")
        return None


def translate_text(input_file, target_lang="zh-CN", model_url="http://localhost:1234/v1/chat/completions"):
    """Translate document using local LLM."""
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    prompt = f"""You are a professional translator. Translate the following text to {target_lang}.

Requirements:
- Maintain technical accuracy
- Preserve formatting (markdown, code blocks)
- Use natural language appropriate for the target audience
- Do not add explanations or notes

Text to translate:
---
{content}
---"""

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
            timeout=120
        )
        
        if response.status_code == 200:
            result = response.json()
            translated = result['choices'][0]['message']['content']
            
            # Save to new file
            base, ext = os.path.splitext(input_file)
            output_file = f"{base}_translated_{target_lang.replace('-', '')}{ext}"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(translated)
            
            print(f"✅ Translation saved to: {output_file}")
            return translated
            
    except Exception as e:
        print(f"❌ Translation failed: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(description="AI Auto-Writer - Local LLM content generator")
    parser.add_argument("--topic", type=str, help="Topic for content generation")
    parser.add_argument("--input", type=str, help="Input file for translation")
    parser.add_argument("--action", type=str, choices=["generate", "translate"], default="generate")
    parser.add_argument("--language", type=str, default="en-US", help="Target language code")
    parser.add_argument("--target-lang", type=str, default="zh-CN", help="Translation target language")
    parser.add_argument("--model-url", type=str, default=os.getenv("LLM_API_URL", "http://localhost:1234/v1/chat/completions"))
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("🤖 AI Auto-Writer")
    print(f"   Powered by local LLM at: {args.model_url}")
    print("=" * 60)
    
    if args.action == "generate":
        if not args.topic:
            parser.error("--topic is required for generate action")
        
        print(f"\n📝 Generating content about: {args.topic}")
        result = generate_content(args.topic, args.language, args.model_url)
        
        if result:
            # Save to file
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"generated_{timestamp}.md"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(result)
            print(f"\n✅ Content saved to: {filename}")
    
    elif args.action == "translate":
        if not args.input:
            parser.error("--input is required for translate action")
        
        print(f"\n🔄 Translating: {args.input} → {args.target_lang}")
        result = translate_text(args.input, args.target_lang, args.model_url)


if __name__ == "__main__":
    main()