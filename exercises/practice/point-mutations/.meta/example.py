def hamming_distance(strand1, strand2):
    return sum(idx != edx for (idx, edx) in zip(strand1, strand2))
