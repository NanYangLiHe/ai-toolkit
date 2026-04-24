#!/usr/bin/env python3
"""
AI Data Parser - Extract structured data from unstructured text.

Convert messy text into clean JSON/CSV/tables using AI.

Usage:
    python data_parser.py --input notes.txt --format json
    python data_parser.py --input invoice.pdf.txt --schema "invoice"
"""

import argparse
import json
import os
from datetime import datetime


def parse_data(input_file, output_format="json", schema=None, model_url="http://localhost:1234/v1/chat/completions"):
    """Extract structured data from text using local LLM."""
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()[:10000]  # Limit input size
    
    schemas = {
        "invoice": {
            "fields": ["date", "vendor", "amount", "items[]", "tax", "total"]
        },
        "contact": {
            "fields": ["name", "email", "phone", "company", "address"]
        },
        "meeting_notes": {
            "fields": ["date", "attendees", "topics", "action_items[]", "decisions"]
        }
    }
    
    if schema and schema in schemas:
        schema_desc = f"Extract the following fields: {', '.join(schemas[schema]['fields'])}"
    else:
        schema_desc = "Identify all key entities, values, and relationships."
    
    prompt = f"""You are a data extraction expert. Extract structured information from the following text.

{schema_desc}

Output format: {output_format.upper()} (valid only)

Text to parse:
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
                "temperature": 0.2,
                "max_tokens": 4096
            },
            timeout=180
        )
        
        if response.status_code == 200:
            result = response.json()
            extracted = result['choices'][0]['message']['content']
            
            # Save output
            base, _ = os.path.splitext(input_file)
            ext = "json" if output_format == "json" else "csv"
            output_file = f"{base}_parsed.{ext}"
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(extracted)
            
            print(f"✅ Parsed data saved to: {output_file}")
            return extracted
            
    except Exception as e:
        print(f"❌ Parsing failed: {e}")
    
    return None


def batch_parse(input_dir, output_format="json", schema=None, model_url="http://localhost:1234/v1/chat/completions"):
    """Parse all text files in a directory."""
    
    results = {}
    count = 0
    
    for filename in os.listdir(input_dir):
        filepath = os.path.join(input_dir, filename)
        
        if not os.path.isfile(filepath):
            continue
        
        # Only process text-based files
        if any(filename.endswith(ext) for ext in ['.txt', '.md', '.csv']):
            print(f"🔍 Parsing: {filename}")
            result = parse_data(
                filepath, 
                output_format=output_format, 
                schema=schema,
                model_url=model_url
            )
            
            if result:
                results[filename] = result
                count += 1
    
    print(f"\n✅ Successfully parsed {count} files")
    return results


def main():
    parser = argparse.ArgumentParser(description="AI Data Parser - Extract structured data from text")
    parser.add_argument("--input", type=str, help="Input file or directory to parse")
    parser.add_argument("--format", type=str, choices=["json", "csv"], default="json", help="Output format")
    parser.add_argument("--schema", type=str, choices=["invoice", "contact", "meeting_notes", None], 
                       help="Predefined schema for extraction")
    parser.add_argument("--model-url", type=str, default=os.getenv("LLM_API_URL"))
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("📊 AI Data Parser")
    print("=" * 60)
    
    if not args.input:
        parser.error("--input is required")
    
    if os.path.isdir(args.input):
        batch_parse(args.input, args.format, args.schema, args.model_url)
    else:
        parse_data(args.input, args.format, args.schema, args.model_url)


if __name__ == "__main__":
    main()