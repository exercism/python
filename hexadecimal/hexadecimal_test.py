# To avoid trivial solutions, try to solve this problem without the
# function int(s, base=16)

import unittest

from hexadecimal import hexa


class HexadecimalTest(unittest.TestCase):
    def test_valid_hexa1(self):
        self.assertEqual(1, hexa('1'))

    @unittest.skip('not yet implemented')
    def test_valid_hexa2(self):
        self.assertEqual(12, hexa('c'))

    @unittest.skip('not yet implemented')
    def test_valid_hexa3(self):
        self.assertEqual(16, hexa('10'))

    @unittest.skip('not yet implemented')
    def test_valid_hexa4(self):
        self.assertEqual(175, hexa('af'))

    @unittest.skip('not yet implemented')
    def test_valid_hexa5(self):
        self.assertEqual(256, hexa('100'))

    @unittest.skip('not yet implemented')
    def test_valid_hexa6(self):
        self.assertEqual(105166, hexa('19ACE'))

    @unittest.skip('not yet implemented')
    def test_valid_hexa7(self):
        self.assertEqual(0, hexa('000000'))

    @unittest.skip('not yet implemented')
    def test_valid_hexa8(self):
        self.assertEqual(16776960, hexa('ffff00'))

    @unittest.skip('not yet implemented')
    def test_valid_hexa9(self):
        self.assertEqual(65520, hexa('00fff0'))

    @unittest.skip('not yet implemented')
    def test_invalid_hexa(self):
        with self.assertRaises(ValueError):
            hexa('carrot')


if __name__ == '__main__':
    unittest.main()
