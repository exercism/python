import unittest
from ddt import ddt, data, unpack

from roman_numerals import numeral


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0

@ddt
class RomanTest(unittest.TestCase):
    @data(
        (1, 'I'),
        (2, 'II'),
        (3, 'III'),
        (4, 'IV'),
        (5, 'V'),
        (6, 'VI'),
        (9, 'IX'),
        (27, 'XXVII'),
        (48, 'XLVIII'),
        (49, 'XLIX'),
        (59, 'LIX'),
        (93, 'XCIII'),
        (141, 'CXLI'),
        (163, 'CLXIII'),
        (402, 'CDII'),
        (575, 'DLXXV'),
        (911, 'CMXI'),
        (1024, 'MXXIV'),
        (3000, 'MMM'),
    )
    @unpack
    def test_numeral(self, arabic, roman):
        self.assertEqual(numeral(arabic), roman)


if __name__ == '__main__':
    unittest.main()
