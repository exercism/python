def spiral(size):
    sm = [[0]*size for k in range(size)]
    i, j, el = 0, -1, 1
    di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
    for x in range(2*size - 1):
        for y in range((2*size - x) // 2):
            i += di[x % 4]
            j += dj[x % 4]
            sm[i][j] = el
            el += 1
    return sm
