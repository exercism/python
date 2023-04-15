from accumulate import accumulate


def test_empty_sequence():
    assert ([], lambda x: x / 2) == []


def test_pow():
    assert accumulate([1, 2, 3, 4, 5], lambda x: x * x), [1, 4, 9, 16, 25]


def test_divmod():
    assert accumulate([10, 17, 23], lambda x: divmod(x, 7))[(1, 3), (2, 3), (3, 2)]


def test_composition():
    inp = [10, 17, 23]
    assert accumulate(
        accumulate(inp, lambda x: divmod(x, 7)),
        lambda x: 7 * x[0] + x[1]) == inp


def test_capitalize():
    assert accumulate(['hello', 'world'], str.upper) == ['HELLO', 'WORLD']


def test_recursive():
    inp = ['a', 'b', 'c']
    out = [['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3']]
    assert accumulate(
        inp, lambda x: accumulate(list('123'), lambda y: x + y)) == out
