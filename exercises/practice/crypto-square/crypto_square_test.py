import unittest

from crypto_square import (
    cipher_text,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class CryptoSquareTest(unittest.TestCase):
    def test_empty_plaintext_results_in_an_empty_ciphertext(self):
        value = ""
        expected = ""
        self.assertEqual(cipher_text(value), expected)

    def test_normalization_results_in_empty_plaintext(self):
        value = "... --- ..."
        expected = ""
        self.assertEqual(cipher_text(value), expected)

    def test_lowercase(self):
        value = "A"
        expected = "a"
        self.assertEqual(cipher_text(value), expected)

    def test_remove_spaces(self):
        value = "  b "
        expected = "b"
        self.assertEqual(cipher_text(value), expected)

    def test_remove_punctuation(self):
        value = "@1,%!"
        expected = "1"
        self.assertEqual(cipher_text(value), expected)

    def test_9_character_plaintext_results_in_3_chunks_of_3_characters(self):
        value = "This is fun!"
        expected = "tsf hiu isn"
        self.assertEqual(cipher_text(value), expected)

    def test_8_character_plaintext_results_in_3_chunks_the_last_one_with_a_trailing_space(
        self,
    ):
        value = "Chill out."
        expected = "clu hlt io "
        self.assertEqual(cipher_text(value), expected)

    def test_54_character_plaintext_results_in_7_chunks_the_last_two_with_trailing_spaces(
        self,
    ):
        value = "If man was meant to stay on the ground, god would have given us roots."
        expected = "imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn  sseoau "
        self.assertEqual(cipher_text(value), expected)


if __name__ == "__main__":
    unittest.main()
