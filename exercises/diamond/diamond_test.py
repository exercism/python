import unittest

from diamond import make_diamond


class DiamondTests(unittest.TestCase):

    def test_letter_A(self):
        self.assertMultiLineEqual('A\n', make_diamond('A'))

    def test_letter_C(self):
        result = ['  A  ',
                  ' B B ',
                  'C   C',
                  ' B B ',
                  '  A  ']
        self.assertMultiLineEqual('\n'.join(result) + '\n', make_diamond('C'))

    def test_letter_E(self):
        result = ['    A    ',
                  '   B B   ',
                  '  C   C  ',
                  ' D     D ',
                  'E       E',
                  ' D     D ',
                  '  C   C  ',
                  '   B B   ',
                  '    A    ']
        self.assertMultiLineEqual('\n'.join(result) + '\n', make_diamond('E'))


if __name__ == '__main__':
    unittest.main()
