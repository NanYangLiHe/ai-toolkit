#!/usr/bin/env python3
"""
Basic unit tests for AI Toolkit scripts.

Run: python -m pytest tests/ or python tests/test_tools.py
"""

import os
import sys
import unittest
from pathlib import Path


class TestAutoWriter(unittest.TestCase):
    """Test Auto Writer script imports and basic structure."""
    
    def test_script_exists(self):
        self.assertTrue(os.path.exists("../scripts/auto_writer.py"))
    
    def test_script_importable(self):
        # Add scripts directory to path for testing
        sys.path.insert(0, "../scripts")
        import auto_writer
        self.assertTrue(hasattr(auto_writer, 'generate_content'))


class TestDataParser(unittest.TestCase):
    """Test Data Parser script structure."""
    
    def test_script_exists(self):
        self.assertTrue(os.path.exists("../scripts/data_parser.py"))
    
    def test_schema_definitions(self):
        sys.path.insert(0, "../scripts")
        import data_parser
        # Test that schema definitions exist and have expected fields
        schemas = {
            "invoice": ["date", "vendor", "amount"],
            "contact": ["name", "email", "phone"]
        }
        for schema_name, expected_fields in schemas.items():
            self.assertIn(schema_name, data_parser.schemas)
            for field in expected_fields:
                self.assertIn(field, data_parser.schemas[schema_name]["fields"])


class TestCodeReview(unittest.TestCase):
    """Test Code Review script structure."""
    
    def test_script_exists(self):
        self.assertTrue(os.path.exists("../scripts/code_review.py"))
    
    def test_scan_function_exists(self):
        sys.path.insert(0, "../scripts")
        import code_review
        self.assertTrue(hasattr(code_review, 'scan_directory'))


class TestWebScraper(unittest.TestCase):
    """Test Web Scraper script structure."""
    
    def test_script_exists(self):
        self.assertTrue(os.path.exists("../scripts/web_scraper.py"))
    
    def test_fetch_page_function_exists(self):
        sys.path.insert(0, "../scripts")
        import web_scraper
        self.assertTrue(hasattr(web_scraper, 'fetch_page'))


class TestDocumentation(unittest.TestCase):
    """Test documentation completeness."""
    
    def test_readme_exists_and_not_empty(self):
        with open("README.md", "r", encoding="utf-8") as f:
            readme = f.read()
        self.assertGreater(len(readme), 1000)  # At least 1KB of content
    
    def test_env_example_exists(self):
        self.assertTrue(os.path.exists(".env.example"))
    
    def test_requirements_txt_not_empty(self):
        with open("requirements.txt", "r", encoding="utf-8") as f:
            requirements = f.read()
        # Should have at least 2 packages listed
        lines = [l.strip() for l in requirements.split('\n') if l.strip() and not l.startswith('#')]
        self.assertGreaterEqual(len(lines), 2)


if __name__ == "__main__":
    unittest.main()