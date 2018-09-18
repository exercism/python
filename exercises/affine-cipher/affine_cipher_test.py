import unittest

from affine_cipher import decode, encode


# Tests adapted from `problem-specifications//canonical-data.json` @ v2.0.0

class AffineCipherTest(unittest.TestCase):
    def test_encode_yes(self):
        self.assertEqual(encode("yes", 5, 7), "xbt")

    def test_encode_no(self):
        self.assertEqual(encode("no", 15, 18), "fu")

    def test_encode_OMG(self):
        self.assertEqual(encode("OMG", 21, 3), "lvz")

    def test_encode_O_M_G(self):
        self.assertEqual(encode("O M G", 25, 47), "hjp")

    def test_encode_mindblowingly(self):
        self.assertEqual(encode("mindblowingly", 11, 15), "rzcwa gnxzc dgt")

    def test_encode_numbers(self):
        self.assertEqual(encode("Testing,1 2 3, testing.", 3, 4),
                         "jqgjc rw123 jqgjc rw")

    def test_encode_deep_thought(self):
        self.assertEqual(encode("Truth is fiction.", 5, 17),
                         "iynia fdqfb ifje")

    def test_encode_all_the_letters(self):
        self.assertEqual(
            encode("The quick brown fox jumps over the lazy dog.", 17, 33),
            "swxtj npvyk lruol iejdc blaxk swxmh qzglf")

    def test_encode_raises_meaningful_exception(self):
        with self.assertRaisesWithMessage(ValueError):
            encode("This is a test", 6, 17)

    def test_decode_exercism(self):
        self.assertEqual(decode("tytgn fjr", 3, 7), "exercism")

    def test_decode_sentence(self):
        self.assertEqual(
            decode("qdwju nqcro muwhn odqun oppmd aunwd o", 19, 16),
            "anobstacleisoftenasteppingstone")

    def test_decode_numbers(self):
        self.assertEqual(decode("odpoz ub123 odpoz ub", 25, 7),
                         "testing123testing")

    def test_decode_all_the_letters(self):
        self.assertEqual(
            decode("swxtj npvyk lruol iejdc blaxk swxmh qzglf", 17, 33),
            "thequickbrownfoxjumpsoverthelazydog")

    def test_decode_with_no_spaces(self):
        self.assertEqual(
            decode("swxtjnpvyklruoliejdcblaxkswxmhqzglf", 17, 33),
            "thequickbrownfoxjumpsoverthelazydog")

    def test_decode_with_too_many_spaces(self):
        self.assertEqual(
            decode("vszzm    cly   yd cg    qdp", 15, 16), "jollygreengiant")

    def test_decode_raises_meaningful_exception(self):
        with self.assertRaisesWithMessage(ValueError):
            decode("Test", 13, 5)

    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == '__main__':
    unittest.main()
