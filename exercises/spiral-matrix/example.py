def spiral(size):
    m = [[0] * size for i in range(size)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, c = 0, -1, 1
    for k in range(2*size - 1):
        for j in range((2*size - k) // 2):
            x += dx[k % 4]
            y += dy[k % 4]
            m[x][y] = c
            c += 1
    return m
