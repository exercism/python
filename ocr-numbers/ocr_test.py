try:
    from ocr import number, grid
except ImportError:
    raise SystemExit('Could not find ocr.py. Does it exist?')

import unittest

class OcrTest(unittest.TestCase):
    def test_0(self):
        self.assertEqual('0', number([" _ ","| |","|_|","   "]))

#    @unittest.skip("Not implemented yet")
    def test_1(self):
        self.assertEqual('1', number(["   ","  |","  |","   "]))

#    @unittest.skip("Not implemented yet")
    def test_garbage(self):
        self.assertEqual('?', number([" _ "," _|","  |","   "]))

#    @unittest.skip("Not implemented yet")
    def test_last_line_nonblank(self):
        self.assertEqual('?', number(["   ","  |","  |","| |"]))

#    @unittest.skip("Not implemented yet")
    def test_unknown_char(self):
        self.assertEqual('?', number([" - "," _|"," X|","   "]))

#    @unittest.skip("Not implemented yet")
    def test_too_short_row(self):
        with self.assertRaises(ValueError) as context:
            number(["  "," _|"," X|","   "])
        self.assertEqual(context.exception.message, 'Unreadable grid')

#    @unittest.skip("Not implemented yet")
    def test_insufficient_rows(self):
        with self.assertRaises(ValueError) as context:
            number(["   "," _|"," X|"])
        self.assertEqual(context.exception.message, 'Unreadable grid')

#    @unittest.skip("Not implemented yet")
    def test_grid0(self):
        self.assertEqual([" _ ","| |","|_|","   "], grid('0'))

#    @unittest.skip("Not implemented yet")
    def test_grid1(self):
        self.assertEqual(["   ","  |","  |","   "], grid('1'))

#    @unittest.skip("Not implemented yet")
    def test_invalid_digit(self):
        with self.assertRaises(ValueError) as context:
            grid('2')
        self.assertEqual(context.exception.message, 'Unknown digit')


if __name__ == '__main__':
    unittest.main()
