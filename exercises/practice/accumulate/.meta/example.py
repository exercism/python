# [op(x) for x in seq] would be nice but trivial


def accumulate(seq, op):
    res = []
    for el in seq:
        res.append(op(el))
    return res
