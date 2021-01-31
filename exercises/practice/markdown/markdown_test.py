import unittest

from markdown import (
    parse,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class MarkdownTest(unittest.TestCase):
    def test_parses_normal_text_as_a_paragraph(self):
        self.assertEqual(
            parse("This will be a paragraph"), "<p>This will be a paragraph</p>"
        )

    def test_parsing_italics(self):
        self.assertEqual(
            parse("_This will be italic_"), "<p><em>This will be italic</em></p>"
        )

    def test_parsing_bold_text(self):
        self.assertEqual(
            parse("__This will be bold__"), "<p><strong>This will be bold</strong></p>"
        )

    def test_mixed_normal_italics_and_bold_text(self):
        self.assertEqual(
            parse("This will _be_ __mixed__"),
            "<p>This will <em>be</em> <strong>mixed</strong></p>",
        )

    def test_with_h1_header_level(self):
        self.assertEqual(parse("# This will be an h1"), "<h1>This will be an h1</h1>")

    def test_with_h2_header_level(self):
        self.assertEqual(parse("## This will be an h2"), "<h2>This will be an h2</h2>")

    def test_with_h6_header_level(self):
        self.assertEqual(
            parse("###### This will be an h6"), "<h6>This will be an h6</h6>"
        )

    def test_unordered_lists(self):
        self.assertEqual(
            parse("* Item 1\n* Item 2"), "<ul><li>Item 1</li><li>Item 2</li></ul>"
        )

    def test_with_a_little_bit_of_everything(self):
        self.assertEqual(
            parse("# Header!\n* __Bold Item__\n* _Italic Item_"),
            "<h1>Header!</h1><ul><li><strong>Bold Item</strong></li><li><em>Italic Item</em></li></ul>",
        )

    def test_with_markdown_symbols_in_the_header_text_that_should_not_be_interpreted(
        self,
    ):
        self.assertEqual(
            parse("# This is a header with # and * in the text"),
            "<h1>This is a header with # and * in the text</h1>",
        )

    def test_with_markdown_symbols_in_the_list_item_text_that_should_not_be_interpreted(
        self,
    ):
        self.assertEqual(
            parse("* Item 1 with a # in the text\n* Item 2 with * in the text"),
            "<ul><li>Item 1 with a # in the text</li><li>Item 2 with * in the text</li></ul>",
        )

    def test_with_markdown_symbols_in_the_paragraph_text_that_should_not_be_interpreted(
        self,
    ):
        self.assertEqual(
            parse("This is a paragraph with # and * in the text"),
            "<p>This is a paragraph with # and * in the text</p>",
        )

    def test_unordered_lists_close_properly_with_preceding_and_following_lines(self):
        self.assertEqual(
            parse("# Start a list\n* Item 1\n* Item 2\nEnd a list"),
            "<h1>Start a list</h1><ul><li>Item 1</li><li>Item 2</li></ul><p>End a list</p>",
        )


if __name__ == "__main__":
    unittest.main()
