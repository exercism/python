import unittest

from affine_cipher import decode, encode


# Tests adapted from `problem-specifications//canonical-data.json` @ v2.0.0

class AffineCipherTest(unittest.TestCase):
    def test_encode_yes(self):
        self.assertMultiLineEqual(encode("yes", 5, 7), "xbt")

    def test_encode_no(self):
        self.assertMultiLineEqual(encode("no", 15, 18), "fu")

    def test_encode_OMG(self):
        self.assertMultiLineEqual(encode("OMG", 21, 3), "lvz")

    def test_encode_O_M_G(self):
        self.assertMultiLineEqual(encode("O M G", 25, 47), "hjp")

    def test_encode_mindblowingly(self):
        self.assertMultiLineEqual(encode("mindblowingly", 11, 15),
                                  "rzcwa gnxzc dgt")

    def test_encode_numbers(self):
        self.assertMultiLineEqual(encode("Testing,1 2 3, testing.", 3, 4),
                                  "jqgjc rw123 jqgjc rw")

    def test_encode_deep_thought(self):
        self.assertMultiLineEqual(encode("Truth is fiction.", 5, 17),
                                  "iynia fdqfb ifje")

    def test_encode_all_the_letters(self):
        self.assertMultiLineEqual(
            encode("The quick brown fox jumps over the lazy dog.", 17, 33),
            "swxtj npvyk lruol iejdc blaxk swxmh qzglf")

    def test_encode_with_a_not_coprime_to_alphabet_size(self):
        self.assertRaises(ValueError, encode, "This is a test.", 6, 17)

    def test_decode_exercism(self):
        self.assertMultiLineEqual(decode("tytgn fjr", 3, 7), "exercism")

    def test_decode_sentence(self):
        self.assertMultiLineEqual(
        decode("qdwju nqcro muwhn odqun oppmd aunwd o", 19, 16),
            "anobstacleisoftenasteppingstone")

    def test_decode_numbers(self):
        self.assertMultiLineEqual(decode("odpoz ub123 odpoz ub", 25, 7),
                                  "testing123testing")

    def test_decode_all_the_letters(self):
        self.assertMultiLineEqual(
            decode("swxtj npvyk lruol iejdc blaxk swxmh qzglf", 17, 33),
            "thequickbrownfoxjumpsoverthelazydog")

    def test_decode_with_no_spaces(self):
        self.assertMultiLineEqual(
            decode("swxtjnpvyklruoliejdcblaxkswxmhqzglf", 17, 33),
            "thequickbrownfoxjumpsoverthelazydog")

    def test_decode_with_too_many_spaces(self):
        self.assertMultiLineEqual(decode("vszzm    cly   yd cg    qdp", 15, 16),
                                  "jollygreengiant")

    def test_decode_with_a_not_coprime_to_alphabet_size(self):
        self.assertRaises(ValueError, decode, "Test", 13, 5)
