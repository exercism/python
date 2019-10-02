import unittest

from crypto_square import ciphertext

# Tests adapted from `problem-specifications//canonical-data.json` @ v3.2.0


class CryptoSquareTest(unittest.TestCase):
    def test_empty_plaintext_results_in_an_empty_ciphertext(self):
        value = ""
        expected = ""
        self.assertEqual(ciphertext(value), expected)

    def test_lowercase(self):
        value = ""
        expected = "a"
        self.assertEqual(ciphertext(value), expected)

    def test_remove_spaces(self):
        value = ""
        expected = "b"
        self.assertEqual(ciphertext(value), expected)

    def test_remove_punctuation(self):
        value = ""
        expected = "1"
        self.assertEqual(ciphertext(value), expected)

    def test_9_character_plaintext_results_in_3_chunks_of_3_characters(self):
        value = ""
        expected = "tsf hiu isn"
        self.assertEqual(ciphertext(value), expected)

    def test_8_character_plaintext_results_in_3_chunks_the_last_one_with_a_trailing_space(
        self
    ):
        value = ""
        expected = "clu hlt io "
        self.assertEqual(ciphertext(value), expected)

    def test_54_character_plaintext_results_in_7_chunks_the_last_two_with_trailing_spaces(
        self
    ):
        value = ""
        expected = "imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn  sseoau "
        self.assertEqual(ciphertext(value), expected)


if __name__ == "__main__":
    unittest.main()
