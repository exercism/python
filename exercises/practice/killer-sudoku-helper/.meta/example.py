import itertools

def combinations(target, size, exclude):
    result = []
    possible = [index for index in
                range(1, int((target ** 2 /size) ** 0.6))
                if index not in exclude]

    if size == 1:
        return [[target]]
    else:
        for index in range(len(possible), 0, -1):
            for seq in itertools.combinations(possible, index):
                if sum(seq) == target and len(seq) == size:
                    result.append(list(seq))
    return result
