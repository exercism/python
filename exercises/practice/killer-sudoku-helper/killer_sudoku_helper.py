import itertools

def combinations(target, size, exclude):
    result = []
    possible = [i for i in range(1, target) if i not in exclude]
    if size == 1:
        return [[target]]
    else:
        for i in range(len(possible), 0, -1):
            for seq in itertools.combinations(possible, i):
                if sum(seq) == target and len(seq) == size:
                    result.append(list(seq))
    return result
