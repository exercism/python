import unittest

import rotational_cipher


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

class RotationalCipher(unittest.TestCase):
    def test_rotate_a_by_1(self):
        self.assertEqual(rotational_cipher.rotate('a', 1), 'b')

    def test_rotate_a_by_26(self):
        self.assertEqual(rotational_cipher.rotate('a', 26), 'a')

    def test_rotate_a_by_0(self):
        self.assertEqual(rotational_cipher.rotate('a', 0), 'a')

    def test_rotate_m_by_13(self):
        self.assertEqual(rotational_cipher.rotate('m', 13), 'z')

    def test_rotate_n_by_13_with_wrap_around_alphabet(self):
        self.assertEqual(rotational_cipher.rotate('n', 13), 'a')

    def test_rotate_capital_letters(self):
        self.assertEqual(rotational_cipher.rotate('OMG', 5), 'TRL')

    def test_rotate_spaces(self):
        self.assertEqual(rotational_cipher.rotate('O M G', 5), 'T R L')

    def test_rotate_numbers(self):
        self.assertEqual(
            rotational_cipher.rotate('Testing 1 2 3 testing', 4),
            'Xiwxmrk 1 2 3 xiwxmrk')

    def test_rotate_punctuation(self):
        self.assertEqual(
            rotational_cipher.rotate("Let's eat, Grandma!", 21),
            "Gzo'n zvo, Bmviyhv!")

    def test_rotate_all_letters(self):
        self.assertEqual(
            rotational_cipher.rotate("The quick brown fox jumps"
                                     " over the lazy dog.", 13),
            "Gur dhvpx oebja sbk whzcf bire gur ynml qbt.")


if __name__ == '__main__':
    unittest.main()
