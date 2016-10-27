import unittest

from crypto_square import encode


class CryptoSquareTest(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual('', encode(''))

    def test_perfect_square(self):
        self.assertEqual('ac bd', encode('ABCD'))

    def test_small_imperfect_square(self):
        self.assertEqual('tis hsy ie sa', encode('This is easy!'))

    def test_punctuation_and_numbers(self):
        msg = "1, 2, 3, Go! Go, for God's sake!"
        ciph = '1gga 2ook 3fde gos ors'
        self.assertEqual(ciph, encode(msg))

    def test_long_string(self):
        msg = ("If man was meant to stay on the ground, god would have given "
               "us roots.")
        ciph = "imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau"
        self.assertEqual(ciph, encode(msg))


if __name__ == '__main__':
    unittest.main()
