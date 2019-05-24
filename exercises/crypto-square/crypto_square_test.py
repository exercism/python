import unittest

from crypto_square import cipher_text


# Tests adapted from `problem-specifications//canonical-data.json` @ v3.2.0

class CryptoSquareTest(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(cipher_text(''), '')

    def test_lowercase(self):
        self.assertEqual(cipher_text('A'), 'a')

    def test_remove_spaces(self):
        self.assertEqual(cipher_text('  b '), 'b')

    def test_remove_punctuation(self):
        self.assertEqual(cipher_text('@1,%!'), '1')

    def test_9chars_results_3chunks(self):
        self.assertEqual(cipher_text('This is fun!'), 'tsf hiu isn')

    def test_8chars_results_3chunks_ending_space(self):
        self.assertEqual(cipher_text('Chill out.'), 'clu hlt io ')

    def test_54chars_results_7chunks_2ending_space(self):
        self.assertEqual(
            cipher_text('If man was meant to stay on the ground, '
                        'god would have given us roots.'),
            'imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn  sseoau '
        )


if __name__ == '__main__':
    unittest.main()
