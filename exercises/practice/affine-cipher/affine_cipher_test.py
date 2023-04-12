import unittest
from affine_cipher import decode, encode


class AffineCipherTest(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(encode("yes", 5, 7), "xbt")
        self.assertEqual(encode("no", 15, 18), "fu")
        self.assertEqual(encode("OMG", 21, 3), "lvz")
        self.assertEqual(encode("O M G", 25, 47), "hjp")
        self.assertEqual(encode("mindblowingly", 11, 15), "rzcwa gnxzc dgt")
        self.assertEqual(encode("Testing,1 2 3, testing.", 3, 4), "jqgjc rw123 jqgjc rw")
        self.assertEqual(encode("Truth is fiction.", 5, 17), "iynia fdqfb ifje")
        self.assertEqual(encode("The quick brown fox jumps over the lazy dog.", 17, 33), "swxtj npvyk lruol iejdc blaxk swxmh qzglf")
        
    def test_encode_invalid(self):
        with self.assertRaises(ValueError) as err:
            encode("This is a test.", 6, 17)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "a and m must be coprime.")
        
    def test_decode(self):
        self.assertEqual(decode("tytgn fjr", 3, 7), "exercism")
        self.assertEqual(decode("qdwju nqcro muwhn odqun oppmd aunwd o", 19, 16), "anobstacleisoftenasteppingstone")
        self.assertEqual(decode("odpoz ub123 odpoz ub", 25, 7), "testing123testing")
        self.assertEqual(decode("swxtj npvyk lruol iejdc blaxk swxmh qzglf", 17, 33), "thequickbrownfoxjumpsoverthelazydog")
        self.assertEqual(decode("swxtjnpvyklruoliejdcblaxkswxmhqzglf", 17, 33), "thequickbrownfoxjumpsoverthelazydog")
        self.assertEqual(decode("vszzm    cly   yd cg    qdp", 15, 16), "jollygreengiant")
        
    def test_decode_invalid(self):
        with self.assertRaises(ValueError) as err:
            decode("Test", 13, 5)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "a and m must be coprime.")
