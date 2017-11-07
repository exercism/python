def append(xs, ys):
    return concat([xs, ys])


def concat(lists):
    return [elem for lst in lists for elem in lst]


def filter_clone(function, xs):
    return [x for x in xs if function(x)]


def length(xs):
    return sum(1 for _ in xs)


def map_clone(function, xs):
    return [function(elem) for elem in xs]


def foldl(function, xs, acc):
    if len(xs) == 0:
        return acc
    else:
        return foldl(function, xs[1:], function(acc, xs[0]))


def foldr(function, xs, acc):
    if len(xs) == 0:
        return acc
    else:
        return function(xs[0], foldr(function, xs[1:], acc))


def reverse(xs):
    return xs[::-1]
