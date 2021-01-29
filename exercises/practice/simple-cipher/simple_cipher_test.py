import re
import unittest

from simple_cipher import Cipher

# Tests adapted from `problem-specifications//canonical-data.json`


class RandomKeyCipherTest(unittest.TestCase):
    def test_can_encode(self):
        cipher = Cipher()
        plaintext = "aaaaaaaaaa"
        self.assertEqual(cipher.encode(plaintext), cipher.key[0 : len(plaintext)])

    def test_can_decode(self):
        cipher = Cipher()
        self.assertEqual(cipher.decode(cipher.key[0 : len("aaaaaaaaaa")]), "aaaaaaaaaa")

    def test_is_reversible(self):
        cipher = Cipher()
        plaintext = "abcdefghij"
        self.assertEqual(cipher.decode(cipher.encode(plaintext)), plaintext)

    def test_key_is_made_only_of_lowercase_letters(self):
        self.assertIsNotNone(re.match("^[a-z]+$", Cipher().key))


class SubstitutionCipherTest(unittest.TestCase):
    def test_can_encode(self):
        cipher = Cipher("abcdefghij")
        plaintext = "aaaaaaaaaa"
        self.assertEqual(cipher.encode(plaintext), cipher.key)

    def test_can_decode(self):
        cipher = Cipher("abcdefghij")
        self.assertEqual(cipher.decode(cipher.key), "aaaaaaaaaa")

    def test_is_reversible(self):
        cipher = Cipher("abcdefghij")
        plaintext = "abcdefghij"
        self.assertEqual(cipher.decode(cipher.encode(plaintext)), plaintext)

    def test_can_double_shift_encode(self):
        cipher = Cipher("iamapandabear")
        plaintext = "iamapandabear"
        self.assertEqual(cipher.encode(plaintext), "qayaeaagaciai")

    def test_can_wrap_on_encode(self):
        cipher = Cipher("abcdefghij")
        plaintext = "zzzzzzzzzz"
        self.assertEqual(cipher.encode(plaintext), "zabcdefghi")

    def test_can_wrap_on_decode(self):
        cipher = Cipher("abcdefghij")
        self.assertEqual(cipher.decode("zabcdefghi"), "zzzzzzzzzz")

    def test_can_encode_messages_longer_than_the_key(self):
        cipher = Cipher("abc")
        plaintext = "iamapandabear"
        self.assertEqual(cipher.encode(plaintext), "iboaqcnecbfcr")

    def test_can_decode_messages_longer_than_the_key(self):
        cipher = Cipher("abc")
        self.assertEqual(cipher.decode("iboaqcnecbfcr"), "iamapandabear")


if __name__ == "__main__":
    unittest.main()
