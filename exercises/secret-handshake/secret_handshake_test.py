import unittest

from secret_handshake import handshake, code


class HandshakeTest(unittest.TestCase):
    def test_shake_int(self):
        self.assertEqual(handshake(9), ['wink', 'jump'])

    def test_shake_bin1(self):
        self.assertEqual(
            handshake('10110'), ['close your eyes', 'double blink'])

    def test_shake_bin2(self):
        self.assertEqual(handshake('101'), ['wink', 'close your eyes'])

    def test_shake_negative_int(self):
        self.assertEqual(handshake(-9), [])

    def test_shake_bin_invalid(self):
        self.assertEqual(handshake('121'), [])

    def test_unknown_action(self):
        self.assertEqual(code(['wink', 'sneeze']), '0')

    def test_code1(self):
        self.assertEqual(code(['close your eyes', 'jump']), '1100')

    def test_code2(self):
        self.assertEqual(code(['wink', 'double blink']), '11')

    def test_code3(self):
        self.assertEqual(code(['jump', 'double blink']), '11010')

    def test_composition1(self):
        self.assertEqual(code(handshake(27)), '11011')

    def test_composition2(self):
        self.assertEqual(code(handshake(1)), '1')

    def test_composition3(self):
        self.assertEqual(code(handshake('111')), '111')

    def test_composition4(self):
        inp = ['wink', 'double blink', 'jump']
        self.assertEqual(handshake(code(inp)), inp)


if __name__ == '__main__':
    unittest.main()
