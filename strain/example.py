def keep(seq, pred):
    res = []
    for el in seq:
        if pred(el):
            res.append(el)
    return res


def discard(seq, pred):
    res = []
    for el in seq:
        if not pred(el):
            res.append(el)
    return res
