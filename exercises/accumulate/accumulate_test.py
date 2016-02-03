import unittest

from accumulate import accumulate


class AccumulateTest(unittest.TestCase):
    def test_empty_sequence(self):
        self.assertEqual([], accumulate([], lambda x: x / 2))

    def test_pow(self):
        self.assertEqual([1, 4, 9, 16, 25], accumulate([1, 2, 3, 4, 5],
                         lambda x: x * x))

    def test_divmod(self):
        inp = [10, 17, 23]
        out = [(1, 3), (2, 3), (3, 2)]
        self.assertEqual(out, accumulate(inp, lambda x: divmod(x, 7)))

    def test_composition(self):
        inp = [10, 17, 23]
        self.assertEqual(inp, accumulate(accumulate(inp, lambda x:
                         divmod(x, 7)), lambda x: 7 * x[0] + x[1]))

    def test_capitalize(self):
        inp = ['hello', 'world']
        out = ['HELLO', 'WORLD']
        self.assertEqual(out, accumulate(inp, str.upper))

    def test_recursive(self):
        inp = list('abc')
        out = [['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3']]
        self.assertEqual(out, accumulate(inp, lambda x: accumulate(list('123'),
                         lambda y: x + y)))


if __name__ == '__main__':
    unittest.main()
