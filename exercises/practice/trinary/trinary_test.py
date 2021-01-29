import unittest

from trinary import trinary


class TrinaryTest(unittest.TestCase):
    def test_valid_trinary1(self):
        self.assertEqual(trinary('0'), 0)

    def test_valid_trinary2(self):
        self.assertEqual(trinary('1'), 1)

    def test_valid_trinary3(self):
        self.assertEqual(trinary('10'), 3)

    def test_valid_trinary4(self):
        self.assertEqual(trinary('102101'), 307)

    def test_valid_trinary5(self):
        self.assertEqual(trinary('22222'), 242)

    def test_valid_trinary6(self):
        self.assertEqual(trinary('10000'), 81)

    def test_invalid_trinary(self):
        self.assertEqual(trinary('13201'), 0)


if __name__ == '__main__':
    unittest.main()
