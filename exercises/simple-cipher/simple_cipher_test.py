import unittest

from simple_cipher import Caesar, Cipher


class CipherTest(unittest.TestCase):
    def test_caesar_encode1(self):
        self.assertEqual(Caesar().encode('itisawesomeprogramminginpython'),
                         'lwlvdzhvrphsurjudpplqjlqsbwkrq')

    def test_caesar_encode2(self):
        self.assertEqual(Caesar().encode('venividivici'), 'yhqlylglylfl')

    def test_caesar_encode3(self):
        self.assertEqual(Caesar().encode('\'Twas the night before Christmas'),
                         'wzdvwkhqljkwehiruhfkulvwpdv')

    def test_caesar_encode_with_numbers(self):
        self.assertEqual(Caesar().encode('1, 2, 3, Go!'), 'jr')

    def test_caesar_decode(self):
        self.assertEqual(Caesar().decode('yhqlylglylfl'), 'venividivici')

    def test_cipher_encode1(self):
        c = Cipher('a')
        self.assertEqual(
            c.encode('itisawesomeprogramminginpython'),
            'itisawesomeprogramminginpython')

    def test_cipher_encode2(self):
        c = Cipher('aaaaaaaaaaaaaaaaaaaaaa')
        self.assertEqual(
            c.encode('itisawesomeprogramminginpython'),
            'itisawesomeprogramminginpython')

    def test_cipher_encode3(self):
        c = Cipher('dddddddddddddddddddddd')
        self.assertEqual(c.encode('venividivici'), 'yhqlylglylfl')

    def test_cipher_encode4(self):
        key = ('duxrceqyaimciuucnelkeoxjhdyduucpmrxmaivacmybmsdrzwqxvbxsy'
               'gzsabdjmdjabeorttiwinfrpmpogvabiofqexnohrqu')
        c = Cipher(key)
        self.assertEqual(c.encode('diffiehellman'), 'gccwkixcltycv')

    def test_cipher_encode_short_key(self):
        c = Cipher('abcd')
        self.assertEqual(c.encode('aaaaaaaa'), 'abcdabcd')

    def test_cipher_compositiion1(self):
        key = ('duxrceqyaimciuucnelkeoxjhdyduucpmrxmaivacmybmsdrzwqxvbxsy'
               'gzsabdjmdjabeorttiwinfrpmpogvabiofqexnohrqu')
        plaintext = 'adaywithoutlaughterisadaywasted'
        c = Cipher(key)
        self.assertEqual(c.decode(c.encode(plaintext)), plaintext)

    def test_cipher_compositiion2(self):
        plaintext = 'adaywithoutlaughterisadaywasted'
        c = Cipher()
        self.assertEqual(c.decode(c.encode(plaintext)), plaintext)

    def test_cipher_random_key(self):
        c = Cipher()
        self.assertTrue(
            len(c.key) >= 100,
            'A random key must be generated when no key is given!')
        self.assertTrue(c.key.islower() and c.key.isalpha(),
                        'All items in the key must be chars and lowercase!')

    def test_cipher_wrong_key(self):
        self.assertRaises(ValueError, Cipher, 'a1cde')
        self.assertRaises(ValueError, Cipher, 'aBcde')


if __name__ == '__main__':
    unittest.main()
