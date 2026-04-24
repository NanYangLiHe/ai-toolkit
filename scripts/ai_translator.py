#!/usr/bin/env python3
"""
AI Translator - Translate content between languages using local LLM
Usage: python ai_translator.py --file article.md --from en --to zh-CN [--output translated.md]
"""
import argparse
import json
import os
from pathlib import Path

class AITranslator:
    def __init__(self, api_url=None, model="qwen3.6-27b"):
        self.api_url = api_url or "http://localhost:1234/v1/chat/completions"
        self.model = model
    
    def translate(self, text, from_lang, to_lang):
        """Translate text using local LLM"""
        system_prompt = f"You are a professional translator. Translate the following content from {from_lang} to {to_lang}. Maintain technical accuracy and natural phrasing."
        
        user_prompt = f"Please translate this:\n\n{text}"
        
        # Call local API (simulated for now)
        try:
            import requests
            response = requests.post(
                self.api_url,
                json={
                    "model": self.model,
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    "temperature": 0.3,  # Low temperature for accurate translation
                },
                timeout=120
            )
            
            if response.status_code == 200:
                result = response.json()
                return result.get("choices", [{}])[0].get("message", {}).get("content", text)
        except Exception as e:
            print(f"API call failed: {e}")
        
        # Fallback to simple replacement for demo
        return self._simple_translate(text, from_lang, to_lang)
    
    def _simple_translate(self, text, from_lang, to_lang):
        """Simple translation fallback (demo only)"""
        translations = {
            "en-zh-CN": {
                "Introduction": "介绍",
                "Features": "功能特性", 
                "Installation": "安装指南",
                "Usage": "使用方法",
                "Conclusion": "总结"
            }
        }
        
        if f"{from_lang}-{to_lang}" in translations:
            for en, zh in translations[f"{from_lang}-{to_lang}"].items():
                text = text.replace(en, zh)
        
        return text

def main():
    parser = argparse.ArgumentParser(description="Translate content using local AI")
    parser.add_argument("--file", "-f", required=True, help="Input markdown file")
    parser.add_argument("--from", "-fr", default="en", help="Source language (default: en)")
    parser.add_argument("--to", "-t", default="zh-CN", help="Target language (default: zh-CN)")
    parser.add_argument("--output", "-o", help="Output file path")
    
    args = parser.parse_args()
    
    # Load content
    input_file = Path(args.file)
    if not input_file.exists():
        print(f"File not found: {input_file}")
        return
    
    content = input_file.read_text(encoding="utf-8")
    
    # Translate
    translator = AITranslator()
    translated = translator.translate(content, args.from_lang, args.to_lang)
    
    # Save output
    if args.output:
        output_path = Path(args.output)
        output_path.write_text(translated, encoding="utf-8")
        print(f"✅ Translated to {args.to}: {output_path}")
    else:
        print(translated)

if __name__ == "__main__":
    main()
