def subsequence(dna):
    ld0 = len(dna[0]) + 1
    ld1 = len(dna[1]) + 1
    seq = [[None] * ld1 for i in range(ld0)]

    for i in range(ld0):
        seq[i][0] = ''
        
    for j in range(ld1):
        seq[0][j] = ''

    for i in range(1, ld0):
        for j in range(1, ld1):
            if dna[0][i - 1] == dna[1][j - 1]:
                seq[i][j] = seq[i-1][j-1] + dna[0][i-1]
            elif len(seq[i-1][j]) >= len(seq[i][j-1]): 
                seq[i][j] = seq[i-1][j]
            else:
                seq[i][j] = seq[i][j-1]

    return seq[ld0 - 1][ld1 - 1]
