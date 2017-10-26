import unittest

from crypto_square import encode

# Tests adapted from `problem-specifications//canonical-data.json` @ v3.1.0
class CryptoSquareTest(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual('', encode(''))

    def test_lowercase(self):
        self.assertEqual('a', encode('A'))

    def test_remove_spaces(self):
        self.assertEqual('b', encode('  b '))

    def test_remove_punctuation(self):
        self.assertEqual('1', encode('@1,%!'))

    def test_9chars_results_3chunks(self):
        self.assertEqual('tsf hiu isn', encode('This is fun!'))

    def test_8chars_results_3chunks_ending_space(self):
        self.assertEqual('clu hlt io ', encode('Chill out.'))

    def test_54chars_results_7chunks_2ending_space(self):
        self.assertEqual(
            'imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn  sseoau ',
            encode('If man was meant to stay on the ground, '
                   'god would have given us roots.')
        )

    # Additional tests for this track

    def test_perfect_square(self):
        self.assertEqual('ac bd', encode('ABCD'))

    def test_small_imperfect_square(self):
        self.assertEqual(encode('This is easy!'), 'tis hsy ie sa')

    def test_punctuation_and_numbers(self):
        msg = '1, 2, 3, Go! Go, for God\'s sake!'
        ciph = '1gga 2ook 3fde gos ors'
        self.assertEqual(ciph, encode(msg))

    def test_long_string(self):
        msg = ('If man was meant to stay on the ground, god would have given '
               'us roots.')
        ciph = 'imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau'
        self.assertEqual(ciph, encode(msg))


if __name__ == '__main__':
    unittest.main()
