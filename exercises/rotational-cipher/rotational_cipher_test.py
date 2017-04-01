import unittest

import rotational_cipher


class RotationalCipher(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(rotational_cipher.rotational_cipher('hello', 0),
                         'hello')

    def test_space(self):
        self.assertEqual(
            rotational_cipher.rotational_cipher(
                                                'from the other side',
                                                0),
            'from the other side')

    def test_ciphered(self):
        self.assertEqual(
            rotational_cipher.rotational_cipher(
                                                'i must have called',
                                                13),
            'v zhfg unir pnyyrq')

    def test_mixed(self):
        self.assertEqual(
            rotational_cipher.rotational_cipher(
                                                '... a 1000 TIMES',
                                                13),
            '... n 1000 GVZRF')

    def test_emptystring(self):
        self.assertEqual(rotational_cipher.rotational_cipher('', 13), '')

    def test_numbers(self):
        self.assertEqual(rotational_cipher.rotational_cipher('07041776!!%$$', 13),
                         '07041776!!%$$')

    def test_mixed(self):
        self.assertEqual(
            rotational_cipher.rotational_cipher(
                                                "Doesn't tear you apart;",
                                                27),
            "Epfto'u ufbs zpv bqbsu;")

    def test_mixed(self):
        self.assertEqual(
            rotational_cipher.rotational_cipher(
                                                "Anymoreeee :'(",
                                                -26),
            "Anymoreeee :'(")


if __name__ == '__main__':
    unittest.main()
