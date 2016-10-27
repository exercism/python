import unittest

from pig_latin import translate


class PigLatinTests(unittest.TestCase):
    def test_word_beginning_with_a(self):
        self.assertEqual("appleay", translate("apple"))

    def test_word_beginning_with_e(self):
        self.assertEqual("earay", translate("ear"))

    def test_word_beginning_with_p(self):
        self.assertEqual("igpay", translate("pig"))

    def test_word_beginning_with_k(self):
        self.assertEqual("oalakay", translate("koala"))

    def test_word_beginning_with_ch(self):
        self.assertEqual("airchay", translate("chair"))

    def test_word_beginning_with_qu(self):
        self.assertEqual("eenquay", translate("queen"))

    def test_word_beginning_with_squ(self):
        self.assertEqual("aresquay", translate("square"))

    def test_word_beginning_with_th(self):
        self.assertEqual("erapythay", translate("therapy"))

    def test_word_beginning_with_thr(self):
        self.assertEqual("ushthray", translate("thrush"))

    def test_word_beginning_with_sch(self):
        self.assertEqual("oolschay", translate("school"))

    def test_translates_phrase(self):
        self.assertEqual("ickquay astfay unray", translate("quick fast run"))

    def test_word_beginning_with_ye(self):
        self.assertEqual("ellowyay", translate("yellow"))

    def test_word_beginning_with_yt(self):
        self.assertEqual("yttriaay", translate("yttria"))

    def test_word_beginning_with_xe(self):
        self.assertEqual("enonxay", translate("xenon"))

    def test_word_beginning_with_xr(self):
        self.assertEqual("xrayay", translate("xray"))

if __name__ == '__main__':
    unittest.main()
