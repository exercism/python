import unittest
import re

from simple_cipher import Cipher


# Tests adapted from `problem-specifications//canonical-data.json` @ v2.0.0

class SimpleCipherTest(unittest.TestCase):
    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


class RandomKeyCipherTest(SimpleCipherTest):
    def test_can_encode(self):
        cipher = Cipher()
        plaintext = 'aaaaaaaaaa'
        self.assertEqual(cipher.encode(plaintext), cipher.key[:len(plaintext)])

    def test_can_decode(self):
        cipher = Cipher()
        plaintext = 'aaaaaaaaaa'
        self.assertEqual(cipher.decode(cipher.key[:len(plaintext)]), plaintext)

    def test_is_reversible(self):
        cipher = Cipher()
        plaintext = 'abcdefghij'
        self.assertEqual(cipher.decode(cipher.encode(plaintext)), plaintext)

    def test_key_is_only_made_of_lowercase_letters(self):
        self.assertIsNotNone(re.match('^[a-z]+$', Cipher().key))


class SubstitutionCipherTest(SimpleCipherTest):
    def test_can_encode(self):
        cipher = Cipher('abcdefghij')
        self.assertEqual(cipher.encode('aaaaaaaaaa'), cipher.key)

    def test_can_decode(self):
        cipher = Cipher('abcdefghij')
        self.assertEqual(cipher.decode(cipher.key), 'aaaaaaaaaa')

    def test_is_reversible(self):
        cipher = Cipher('abcdefghij')
        plaintext = 'abcdefghij'
        self.assertEqual(cipher.decode(cipher.encode(plaintext)), plaintext)

    def test_can_double_shift_encode(self):
        plaintext = 'iamapandabear'
        cipher = Cipher(plaintext)
        self.assertEqual(cipher.encode(plaintext), 'qayaeaagaciai')

    def test_can_wrap_on_encode(self):
        cipher = Cipher('abcdefghij')
        self.assertEqual(cipher.encode('zzzzzzzzzz'), 'zabcdefghi')

    def test_can_wrap_on_decode(self):
        cipher = Cipher('abcdefghij')
        self.assertEqual(cipher.decode('zabcdefghi'), 'zzzzzzzzzz')

    def test_can_encode_messages_longer_than_key(self):
        cipher = Cipher('abc')
        self.assertEqual(cipher.encode('iamapandabear'), 'iboaqcnecbfcr')

    def test_can_decode_messages_longer_than_key(self):
        cipher = Cipher('abc')
        self.assertEqual(cipher.decode('iboaqcnecbfcr'), 'iamapandabear')


if __name__ == '__main__':
    unittest.main()
