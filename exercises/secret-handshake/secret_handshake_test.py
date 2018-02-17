import unittest

from secret_handshake import handshake, secret_code


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0

class HandshakeTest(unittest.TestCase):
    def test_wink_for_1(self):
        self.assertEqual(handshake(1), ['wink'])

    def test_double_blink_for_10(self):
        self.assertEqual(handshake(2), ['double blink'])

    def test_close_your_eyes_for_100(self):
        self.assertEqual(handshake(4), ['close your eyes'])

    def test_jump_for_1000(self):
        self.assertEqual(handshake(8), ['jump'])

    def test_combine_two_actions(self):
        self.assertEqual(handshake(3), ['wink', 'double blink'])

    def test_reverse_two_actions(self):
        self.assertEqual(handshake(19), ['double blink', 'wink'])

    def test_reversing_one_action_gives_the_same_action(self):
        self.assertEqual(handshake(24), ['jump'])

    def test_reversing_no_actions_still_gives_no_actions(self):
        self.assertEqual(handshake(16), [])

    def test_all_possible_actions(self):
        self.assertEqual(handshake(15), ['wink',
                                         'double blink',
                                         'close your eyes',
                                         'jump'])

    def test_reverse_all_possible_actions(self):
        self.assertEqual(handshake(31), ['jump',
                                         'close your eyes',
                                         'double blink',
                                         'wink'])

    def test_do_nothing_for_zero(self):
        self.assertEqual(handshake(0), [])

    # Track-specific tests

    @unittest.skip('extra-credit')
    def test_code1(self):
        self.assertEqual(secret_code(['close your eyes', 'jump']), 12)

    @unittest.skip('extra-credit')
    def test_code2(self):
        self.assertEqual(secret_code(['wink', 'double blink']), 3)

    @unittest.skip('extra-credit')
    def test_code3(self):
        self.assertEqual(secret_code(['jump', 'double blink']), 26)

    @unittest.skip('extra-credit')
    def test_reversible1(self):
        self.assertEqual(secret_code(handshake(27)), 27)

    @unittest.skip('extra-credit')
    def test_reversible2(self):
        self.assertEqual(secret_code(handshake(1)), 1)

    @unittest.skip('extra-credit')
    def test_reversible3(self):
        self.assertEqual(secret_code(handshake(7)), 7)

    @unittest.skip('extra-credit')
    def test_reversible4(self):
        inp = ['wink', 'double blink', 'jump']
        self.assertEqual(handshake(secret_code(inp)), inp)


if __name__ == '__main__':
    unittest.main()
