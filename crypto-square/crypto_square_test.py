import unittest

from crypto_square import encode, decode


class CryptoSquareTest(unittest.TestCase):
    def test_empty_plain(self):
        self.assertEqual('', encode(''))

    def test_perfect_square(self):
        self.assertEqual('wliod drwe', encode('WorldWide'))

    def test_almost_perfect_square(self):
        self.assertEqual('oasny selde', encode('One day less'))

    def test_punctuation(self):
        msg = "1, 2, 3, Go! Go, for God's sake!"
        ciph = '1gga2 ook3f degos ors'
        self.assertEqual(ciph, encode(msg))

    def test_long_string(self):
        msg = "Be who you are and say what you feel, because those who mind "\
              "don't matter and those who matter don't mind."
        ciph = 'betcw tttne ayahm htdwn ouoao ehdus mtsro sfeit edyae tnewo '\
               'oyehd rhnuw lodao tahbs onmmr aeend ai'
        self.assertEqual(ciph, encode(msg))

    def test_decode(self):
        ciph = 'woree iorhu ssmtp eefei aiafn ildjs ulenf eotse vdoor iecey '\
               'nfima trott tenyu hhytd'
        msg = 'wheneveryoufindyourselfonthesideofthemajorityitistimetopausea'\
              'ndreflect'
        self.assertEqual(msg, decode(ciph))

    def test_encode_decode(self):
        msg = 'tensioniswhoyouthinkyoushouldberelaxationiswhoyouare'
        self.assertEqual(msg, decode(encode(msg)))


if __name__ == '__main__':
    unittest.main()
