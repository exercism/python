import unittest

from cipher import Caesar, Cipher


class CipherTest(unittest.TestCase):

    def test_caesar_encode1(self):
        self.assertEqual('lwlvdzhvrphsurjudpplqjlqsbwkrq',
                         Caesar().encode('itisawesomeprogramminginpython'))

    def test_caesar_encode2(self):
        self.assertEqual('yhqlylglylfl', Caesar().encode('venividivici'))

    def test_caesar_encode3(self):
        self.assertEqual('wzdvwkhqljkwehiruhfkulvwpdv',
                         Caesar().encode('\'Twas the night before Christmas'))

    def test_caesar_encode_with_numbers(self):
        self.assertEqual('jr', Caesar().encode('1, 2, 3, Go!'))

    def test_caesar_decode(self):
        self.assertEqual('venividivici', Caesar().decode('yhqlylglylfl'))

    def test_cipher_encode1(self):
        c = Cipher('a')
        self.assertEqual('itisawesomeprogramminginpython',
                         c.encode('itisawesomeprogramminginpython'))

    def test_cipher_encode2(self):
        c = Cipher('aaaaaaaaaaaaaaaaaaaaaa')
        self.assertEqual('itisawesomeprogramminginpython',
                         c.encode('itisawesomeprogramminginpython'))

    def test_cipher_encode3(self):
        c = Cipher('dddddddddddddddddddddd')
        self.assertEqual('yhqlylglylfl', c.encode('venividivici'))

    def test_cipher_encode4(self):
        key = 'duxrceqyaimciuucnelkeoxjhdyduucpmrxmaivacmybmsdrzwqxvbxsygzsabdjmdjabeorttiwinfrpmpogvabiofqexnohrqu'
        c = Cipher(key)
        self.assertEqual('gccwkixcltycv', c.encode('diffiehellman'))

    def test_cipher_compositiion1(self):
        key = 'duxrceqyaimciuucnelkeoxjhdyduucpmrxmaivacmybmsdrzwqxvbxsygzsabdjmdjabeorttiwinfrpmpogvabiofqexnohrqu'
        plaintext = 'adaywithoutlaughterisadaywasted'
        c = Cipher(key)
        self.assertEqual(plaintext, c.decode(c.encode(plaintext)))

    def test_cipher_compositiion2(self):
        plaintext = 'adaywithoutlaughterisadaywasted'
        c = Cipher()
        self.assertEqual(plaintext, c.decode(c.encode(plaintext)))


if __name__ == '__main__':
    unittest.main()
