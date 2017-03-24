import unittest

from pig_latin import translate


class PigLatinTests(unittest.TestCase):
    def test_word_beginning_with_a(self):
        self.assertEqual(translate("apple"), "appleay")

    def test_word_beginning_with_e(self):
        self.assertEqual(translate("ear"), "earay")

    def test_word_beginning_with_p(self):
        self.assertEqual(translate("pig"), "igpay")

    def test_word_beginning_with_k(self):
        self.assertEqual(translate("koala"), "oalakay")

    def test_word_beginning_with_ch(self):
        self.assertEqual(translate("chair"), "airchay")

    def test_word_beginning_with_qu(self):
        self.assertEqual(translate("queen"), "eenquay")

    def test_word_beginning_with_squ(self):
        self.assertEqual(translate("square"), "aresquay")

    def test_word_beginning_with_th(self):
        self.assertEqual(translate("therapy"), "erapythay")

    def test_word_beginning_with_thr(self):
        self.assertEqual(translate("thrush"), "ushthray")

    def test_word_beginning_with_sch(self):
        self.assertEqual(translate("school"), "oolschay")

    def test_translates_phrase(self):
        self.assertEqual(translate("quick fast run"), "ickquay astfay unray")

    def test_word_beginning_with_ye(self):
        self.assertEqual(translate("yellow"), "ellowyay")

    def test_word_beginning_with_yt(self):
        self.assertEqual(translate("yttria"), "yttriaay")

    def test_word_beginning_with_xe(self):
        self.assertEqual(translate("xenon"), "enonxay")

    def test_word_beginning_with_xr(self):
        self.assertEqual(translate("xray"), "xrayay")


if __name__ == '__main__':
    unittest.main()
