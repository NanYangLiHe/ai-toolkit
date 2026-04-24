#!/usr/bin/env python3
"""
AI Prompt Generator - Create optimized prompts for any task.

Usage:
    python prompt_generator.py --task "Translate technical documentation" --style professional
    python prompt_generator.py --template code_review --language zh-CN
"""

import argparse
import json
import os


def generate_prompt(task, style="professional", language="en-US", model_url="http://localhost:1234/v1/chat/completions"):
    """Generate optimized prompts using meta-prompting."""
    
    templates = {
        "code_review": (
            "You are a senior software engineer with 10+ years experience. "
            "Review the following code and provide:\n"
            "1. Critical bugs and security vulnerabilities\n"
            "2. Performance bottlenecks\n"
            "3. Code style improvements\n"
            "4. Suggested refactoring\n\n"
            "Rate quality: ⭐⭐⭐⭐⭐ | Be specific with line numbers."
        ),
        "content_writer": (
            "You are a professional technical writer for [AUDIENCE].\n"
            "Write about: {topic}\n"
            "- Tone: {tone}\n"
            "- Length: 800-1200 words\n"
            "- Include practical examples and code snippets\n"
            "- Use markdown formatting with clear headers\n"
            "- End with actionable takeaways"
        ),
        "data_analyst": (
            "Analyze the following data and extract:\n"
            "- Key metrics and trends\n"
            "- Anomalies or outliers\n"
            "- Actionable insights\n"
            "- Recommended next steps\n\n"
            "Format output as JSON with clear structure."
        ),
        "translator": (
            "Translate the following text to {target_language}:\n"
            "- Maintain technical accuracy\n"
            "- Preserve all formatting and code blocks\n"
            "- Use natural language appropriate for {audience}\n"
            "- Do not add explanations or notes outside translation"
        )
    }

    prompt = f"""Create an optimized prompt for: "{task}"

Requirements:
- Style: {style}
- Target language: {language}
- Include clear instructions and examples
- Optimize for local LLM inference (7B parameters)

Available templates you can adapt:
{json.dumps(templates, indent=2)}

Generate the best possible prompt:"""

    try:
        import requests
        
        response = requests.post(
            model_url,
            json={
                "model": "local",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7,
                "max_tokens": 2048
            },
            timeout=120
        )
        
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content']
            
    except Exception as e:
        print(f"❌ Prompt generation failed: {e}")
    
    return None


def main():
    parser = argparse.ArgumentParser(description="AI Prompt Generator")
    parser.add_argument("--task", type=str, help="Describe what you want the prompt to do")
    parser.add_argument("--style", type=str, choices=["professional", "casual", "academic"], default="professional")
    parser.add_argument("--language", type=str, default="en-US")
    parser.add_argument("--model-url", type=str, default=os.getenv("LLM_API_URL"))
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("✨ AI Prompt Generator")
    print("=" * 60)
    
    if not args.task:
        parser.error("--task is required")
    
    result = generate_prompt(args.task, args.style, args.language, args.model_url)
    
    if result:
        # Save to file
        timestamp = __import__('datetime').datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"prompt_{timestamp}.md"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(result)
        print(f"\n✅ Prompt saved to: {filename}")


if __name__ == "__main__":
    main()