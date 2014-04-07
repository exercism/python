from trinary import trinary

import unittest

class TrinaryTest(unittest.TestCase):
    def test_valid_trinary1(self):
        self.assertEqual(0, trinary('0'))

    def test_valid_trinary2(self):
        self.assertEqual(1, trinary('1'))

    def test_valid_trinary3(self):
        self.assertEqual(3, trinary('10'))

    def test_valid_trinary4(self):
        self.assertEqual(307, trinary('102101'))

    def test_valid_trinary5(self):
        self.assertEqual(242, trinary('22222'))

    def test_valid_trinary6(self):
        self.assertEqual(81, trinary('10000'))

    def test_invalid_trinary(self):
        self.assertEqual(0, trinary('13201'))


if __name__ == '__main__':
    unittest.main()
