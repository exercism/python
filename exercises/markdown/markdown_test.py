import unittest
from markdown import parse_markdown


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0

class TestMarkdown(unittest.TestCase):

    def test_paragraph(self):
        self.assertEqual(parse_markdown('This will be a paragraph'),
                         '<p>This will be a paragraph</p>')

    def test_italics(self):
        self.assertEqual(parse_markdown('_This will be italic_'),
                         '<p><em>This will be italic</em></p>')

    def test_bold(self):
        self.assertEqual(parse_markdown('__This will be bold__'),
                         '<p><strong>This will be bold</strong></p>')

    def test_mixed_normal_italics_and_bold(self):
        self.assertEqual(parse_markdown('This will _be_ __mixed__'),
                         '<p>This will <em>be</em> <strong>mixed</strong></p>')

    def test_h1(self):
        self.assertEqual(parse_markdown('# This will be an h1'),
                         '<h1>This will be an h1</h1>')

    def test_h2(self):
        self.assertEqual(parse_markdown('## This will be an h2'),
                         '<h2>This will be an h2</h2>')

    def test_h6(self):
        self.assertEqual(parse_markdown(
            '###### This will be an h6'), '<h6>This will be an h6</h6>')

    def test_unordered_lists(self):
        self.assertEqual(parse_markdown('* Item 1\n* Item 2'),
                         '<ul><li>Item 1</li>'
                         '<li>Item 2</li></ul>')

    def test_little_bit_of_everything(self):
        self.assertEqual(parse_markdown(
            '# Header!\n* __Bold Item__\n* _Italic Item_'),
            '<h1>Header!</h1><ul><li><strong>Bold Item</strong></li>'
            '<li><em>Italic Item</em></li></ul>')


if __name__ == '__main__':
    unittest.main()
