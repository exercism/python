def hamming(s1,s2):
    return sum(1 for a,b in map(None,s1,s2) if a != b)
