import unittest

from run_length_encoding import encode, decode


class WordCountTests(unittest.TestCase):

    def test_encode_empty_string(self):
        self.assertMultiLineEqual('', encode(''))

    def test_encode_single_characters_only_are_encoded_without_count(self):
        self.assertMultiLineEqual('XYZ', encode('XYZ'))

    def test_encode_string_with_no_single_characters(self):
        self.assertMultiLineEqual('2A3B4C', encode('AABBBCCCC'))

    def test_encode_single_characters_mixed_with_repeated_characters(self):
        self.assertMultiLineEqual(
            '12WB12W3B24WB',
            encode('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB'))

    def test_encode_multiple_whitespace_mixed_in_string(self):
        self.assertMultiLineEqual('2 hs2q q2w2 ', encode('  hsqq qww  '))

    def test_encode_lowercase_characters(self):
        self.assertMultiLineEqual('2a3b4c', encode('aabbbcccc'))

    def test_decode_empty_string(self):
        self.assertMultiLineEqual('', decode(''))

    def test_decode_single_characters_only(self):
        self.assertMultiLineEqual('XYZ', decode('XYZ'))

    def test_decode_string_with_no_single_characters(self):
        self.assertMultiLineEqual('AABBBCCCC', decode('2A3B4C'))

    def test_decode_single_characters_with_repeated_characters(self):
        self.assertMultiLineEqual(
            'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB',
            decode('12WB12W3B24WB'))

    def test_decode_multiple_whitespace_mixed_in_string(self):
        self.assertMultiLineEqual('  hsqq qww  ', decode('2 hs2q q2w2 '))

    def test_decode_lower_case_string(self):
        self.assertMultiLineEqual('aabbbcccc', decode('2a3b4c'))

    def test_combination(self):
        self.assertMultiLineEqual('zzz ZZ  zZ', decode(encode('zzz ZZ  zZ')))


if __name__ == '__main__':
    unittest.main()
