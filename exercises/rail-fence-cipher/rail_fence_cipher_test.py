import unittest

from rail_fence_cipher import encode, decode


class RailFenceTests(unittest.TestCase):

    def test_encode_with_two_rails(self):
        self.assertMultiLineEqual('XXXXXXXXXOOOOOOOOO',
                                  encode('XOXOXOXOXOXOXOXOXO', 2))

    def test_encode_with_three_rails(self):
        self.assertMultiLineEqual('WECRLTEERDSOEEFEAOCAIVDEN',
                                  encode('WEAREDISCOVEREDFLEEATONCE', 3))

    def test_encode_with_middle_stop(self):
        self.assertMultiLineEqual('ESXIEECSR', encode('EXERCISES', 4))

    def test_decode_with_three_rails(self):
        self.assertMultiLineEqual('THEDEVILISINTHEDETAILS',
                                  decode('TEITELHDVLSNHDTISEIIEA', 3))

    def test_decode_with_five_rails(self):
        self.assertMultiLineEqual('EXERCISMISAWESOME',
                                  decode('EIEXMSMESAORIWSCE', 5))

    def test_decode_with_six_rails(self):
        self.assertMultiLineEqual(
            '112358132134558914423337761098715972584418167651094617711286',
            decode('133714114238148966225439541018335470986172518171757571896261', 6)
        )

if __name__ == '__main__':
    unittest.main()
