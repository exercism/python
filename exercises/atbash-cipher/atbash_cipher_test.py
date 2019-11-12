import unittest

from atbash_cipher import decode, encode

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0


class AtbashCipherTest(unittest.TestCase):
    def test_encode_yes(self):
        value = "yes"
        expected = "bvh"
        self.assertEqual(encode(value), expected)

    def test_encode_no(self):
        value = "no"
        expected = "ml"
        self.assertEqual(encode(value), expected)

    def test_encode_omg(self):
        value = "OMG"
        expected = "lnt"
        self.assertEqual(encode(value), expected)

    def test_encode_spaces(self):
        value = "O M G"
        expected = "lnt"
        self.assertEqual(encode(value), expected)

    def test_encode_mindblowingly(self):
        value = "mindblowingly"
        expected = "nrmwy oldrm tob"
        self.assertEqual(encode(value), expected)

    def test_encode_numbers(self):
        value = "Testing,1 2 3, testing."
        expected = "gvhgr mt123 gvhgr mt"
        self.assertEqual(encode(value), expected)

    def test_encode_deep_thought(self):
        value = "Truth is fiction."
        expected = "gifgs rhurx grlm"
        self.assertEqual(encode(value), expected)

    def test_encode_all_the_letters(self):
        value = "The quick brown fox jumps over the lazy dog."
        expected = "gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt"
        self.assertEqual(encode(value), expected)

    def test_decode_exercism(self):
        value = "vcvix rhn"
        expected = "exercism"
        self.assertEqual(decode(value), expected)

    def test_decode_a_sentence(self):
        value = "zmlyh gzxov rhlug vmzhg vkkrm thglm v"
        expected = "anobstacleisoftenasteppingstone"
        self.assertEqual(decode(value), expected)

    def test_decode_numbers(self):
        value = "gvhgr mt123 gvhgr mt"
        expected = "testing123testing"
        self.assertEqual(decode(value), expected)

    def test_decode_all_the_letters(self):
        value = "gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt"
        expected = "thequickbrownfoxjumpsoverthelazydog"
        self.assertEqual(decode(value), expected)

    def test_decode_with_too_many_spaces(self):
        value = "vc vix    r hn"
        expected = "exercism"
        self.assertEqual(decode(value), expected)

    def test_decode_with_no_spaces(self):
        value = "zmlyhgzxovrhlugvmzhgvkkrmthglmv"
        expected = "anobstacleisoftenasteppingstone"
        self.assertEqual(decode(value), expected)


if __name__ == "__main__":
    unittest.main()
