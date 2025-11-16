import unittest
from extract_title import *

class TestExtractTitle(unittest.TestCase):
    def test_extract_title_success(self):
        markdown = """# This is the Title"""
        title = extract_title(markdown)
        self.assertEqual(title, "This is the Title")
    def test_extract_title_with_leading_spaces(self):
        markdown = """   # Leading Spaces Title"""
        title = extract_title(markdown)
        self.assertEqual(title, "Leading Spaces Title")
    def test_extract_title_multiple_headings(self):
        markdown = """# First Title"""
        title = extract_title(markdown)
        self.assertEqual(title, "First Title")
    def test_extract_title_no_heading(self):
        markdown = """This is some text without a heading."""
        with self.assertRaises(ValueError) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "no 1 heading aka title")
    def test_extract_title_empty_string(self):
        markdown = ""
        with self.assertRaises(ValueError) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "no 1 heading aka title")