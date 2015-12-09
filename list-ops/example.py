from functools import reduce

def map(function, xs):
    return (function(elem) for elem in xs)

def length(xs):
    len = 0
    for x in xs:
        len += 1
    return len

def filter(function, xs):
    return (x for x in xs if function(x))

def reverse(xs):
    if not xs:
        None
    else:
        return xs[::-1]

def append(xs, y):
    xs[len(xs):] = [y]
    return xs

def foldl(function, xs, acc):
    return acc if(len(xs) == 0) else foldl(function, xs[1:], function(acc, xs[0]))

def foldr(function, xs, acc):
    return acc if(len(xs) == 0) else function(xs[0], foldr(function, xs[1:], acc))

def flat(xs):
    out = []
    for item in xs:
        if isinstance(item, (list, tuple)):
            out.extend(flat(item))
        else:
            out.append(item)
    return out

    flat(["orange", "apple", "banana"])

def concat(xs, ys):
    if not ys:
        return xs
    else:
        for item in ys:
            xs.append(item)
        return xs
