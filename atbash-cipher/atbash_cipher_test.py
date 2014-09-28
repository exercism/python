import unittest

from atbash_cipher import decode, encode


class AtbashCipherTest(unittest.TestCase):

    def test_encode_no(self):
        self.assertEqual("ml", encode("no"))

    def test_encode_yes(self):
        self.assertEqual("bvh", encode("yes"))

    def test_encode_OMG(self):
        self.assertEqual("LNT", encode("OMG"))

    def test_encode_O_M_G(self):
        self.assertEqual("L N T", encode("O M G"))

    def test_encode_long_word(self):
        self.assertEqual("nrmwyoldrmtob", encode("mindblowingly"))

    def test_encode_numbers(self):
        self.assertEqual("Gvhgrmt, 1 2 3, gvhgrmt.",
                         encode("Testing, 1 2 3, testing."))

    def test_encode_sentence(self):
        self.assertEqual("Gifgs rh urxgrlm.",
                         encode("Truth is fiction."))

    def test_encode_all_things(self):
        plaintext = "The quick brown fox jumps over the lazy dog."
        ciphertext = "Gsv jfrxp yildm ulc qfnkh levi gsv ozab wlt."
        self.assertEqual(ciphertext, encode(plaintext))

    def test_decode_word(self):
        self.assertEqual("exercism", decode("vcvixrhn"))

    def test_decode_sentence(self):
        self.assertEqual("an obstacle is often a stepping stone",
                         decode("zm lyhgzxov rh lugvm z hgvkkrmt hglmv"))


if __name__ == '__main__':
    unittest.main()
