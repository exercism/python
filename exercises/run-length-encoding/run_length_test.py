# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

from run_length import encode, decode


class WordCountTests(unittest.TestCase):

    def test_encode(self):
        self.assertMultiLineEqual('2A3B4C', encode('AABBBCCCC'))

    def test_decode(self):
        self.assertMultiLineEqual('AABBBCCCC', decode('2A3B4C'))

    def test_encode_with_single(self):
        self.assertMultiLineEqual(
            '12WB12W3B24WB',
            encode('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB'))

    def test_decode_with_single(self):
        self.assertMultiLineEqual(
            'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB',
            decode('12WB12W3B24WB'))

    def test_combination(self):
        self.assertMultiLineEqual('zzz ZZ  zZ', decode(encode('zzz ZZ  zZ')))

    def test_encode_unicode_s(self):
        self.assertMultiLineEqual('⏰3⚽2⭐⏰', encode('⏰⚽⚽⚽⭐⭐⏰'))

    def test_decode_unicode(self):
        self.assertMultiLineEqual('⏰⚽⚽⚽⭐⭐⏰', decode('⏰3⚽2⭐⏰'))

if __name__ == '__main__':
    unittest.main()
