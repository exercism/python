
def map_src(function, xs):
    return [function(elem) for elem in xs]


def reduce_src(function, xs, start=None):
    it = iter(xs)
    if start is None:
        try:
            start = next(it)
        except:
            raise TypeError("reduce_src() on empty sequence")
    accumulator = start
    for elem in it:
        accumulator = function(accumulator, elem)
    return accumulator


def length_src(xs):
    if not xs:
        return 0
    else:
        count = 0
        start = xs[0]
        for elem in xs:
            count += 1
        return count
