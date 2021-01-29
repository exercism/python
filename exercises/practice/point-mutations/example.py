def hamming_distance(strand1, strand2):
    return sum(x != y for (x, y) in zip(strand1, strand2))
