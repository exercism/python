import unittest

from pig_latin import (
    translate,
)

# Tests adapted from `problem-specifications//canonical-data.json`


class PigLatinTest(unittest.TestCase):
    def test_word_beginning_with_a(self):
        self.assertEqual(translate("apple"), "appleay")

    def test_word_beginning_with_e(self):
        self.assertEqual(translate("ear"), "earay")

    def test_word_beginning_with_i(self):
        self.assertEqual(translate("igloo"), "iglooay")

    def test_word_beginning_with_o(self):
        self.assertEqual(translate("object"), "objectay")

    def test_word_beginning_with_u(self):
        self.assertEqual(translate("under"), "underay")

    def test_word_beginning_with_a_vowel_and_followed_by_a_qu(self):
        self.assertEqual(translate("equal"), "equalay")

    def test_word_beginning_with_p(self):
        self.assertEqual(translate("pig"), "igpay")

    def test_word_beginning_with_k(self):
        self.assertEqual(translate("koala"), "oalakay")

    def test_word_beginning_with_x(self):
        self.assertEqual(translate("xenon"), "enonxay")

    def test_word_beginning_with_q_without_a_following_u(self):
        self.assertEqual(translate("qat"), "atqay")

    def test_word_beginning_with_ch(self):
        self.assertEqual(translate("chair"), "airchay")

    def test_word_beginning_with_qu(self):
        self.assertEqual(translate("queen"), "eenquay")

    def test_word_beginning_with_qu_and_a_preceding_consonant(self):
        self.assertEqual(translate("square"), "aresquay")

    def test_word_beginning_with_th(self):
        self.assertEqual(translate("therapy"), "erapythay")

    def test_word_beginning_with_thr(self):
        self.assertEqual(translate("thrush"), "ushthray")

    def test_word_beginning_with_sch(self):
        self.assertEqual(translate("school"), "oolschay")

    def test_word_beginning_with_yt(self):
        self.assertEqual(translate("yttria"), "yttriaay")

    def test_word_beginning_with_xr(self):
        self.assertEqual(translate("xray"), "xrayay")

    def test_y_is_treated_like_a_consonant_at_the_beginning_of_a_word(self):
        self.assertEqual(translate("yellow"), "ellowyay")

    def test_y_is_treated_like_a_vowel_at_the_end_of_a_consonant_cluster(self):
        self.assertEqual(translate("rhythm"), "ythmrhay")

    def test_y_as_second_letter_in_two_letter_word(self):
        self.assertEqual(translate("my"), "ymay")

    def test_a_whole_phrase(self):
        self.assertEqual(translate("quick fast run"), "ickquay astfay unray")


if __name__ == "__main__":
    unittest.main()
