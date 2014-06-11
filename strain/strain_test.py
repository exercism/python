import unittest

from strain import keep, discard


class StrainTest(unittest.TestCase):
    def test_empty_sequence(self):
        self.assertEqual([], keep([], lambda x: x % 2 == 0))

    def test_empty_keep(self):
        inp = [2, 4, 6, 8, 10]
        out = []
        self.assertEqual(out, keep(inp, lambda x: x % 2 == 1))

    def test_empty_discard(self):
        inp = [2, 4, 6, 8, 10]
        out = []
        self.assertEqual(out, discard(inp, lambda x: x % 2 == 0))

    def test_keep_everything(self):
        inp = [2, 4, 6, 8, 10]
        self.assertEqual(inp, keep(inp, lambda x: x % 2 == 0))

    def test_discard_endswith(self):
        inp = ['dough', 'cash', 'plough', 'though', 'through', 'enough']
        out = ['cash']
        fn = lambda x: str.endswith(x, 'ough')
        self.assertEqual(out, discard(inp, fn))

    def test_keep_z(self):
        inp = ['zebra', 'arizona', 'apple', 'google', 'mozilla']
        out = ['zebra', 'arizona', 'mozilla']
        self.assertEqual(out, keep(inp, lambda x: 'z' in x))

    def test_keep_discard(self):
        inp = ['1,2,3', 'one', 'almost!', 'love']
        self.assertEqual([], discard(keep(inp, str.isalpha), str.isalpha))

    def test_keep_plus_discard(self):
        inp = ['1,2,3', 'one', 'almost!', 'love']
        out = ['one', 'love', '1,2,3', 'almost!']
        self.assertEqual(out, keep(inp, str.isalpha)+discard(inp, str.isalpha))


if __name__ == '__main__':
    unittest.main()
