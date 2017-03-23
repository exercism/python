import unittest

from diamond import make_diamond


class DiamondTests(unittest.TestCase):
    def test_letter_A(self):
        self.assertMultiLineEqual(make_diamond('A'), 'A\n')

    def test_letter_C(self):
        result = ['  A  ',
                  ' B B ',
                  'C   C',
                  ' B B ',
                  '  A  ']
        self.assertMultiLineEqual(make_diamond('C'), '\n'.join(result) + '\n')

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
        self.assertMultiLineEqual(make_diamond('E'), '\n'.join(result) + '\n')


if __name__ == '__main__':
    unittest.main()
