def spiral_matrix(size):
    matrix = [[0]*size for row in range(size)]
    idx = 0
    jdx = -1
    element = 1

    digital = [0, 1, 0, -1]
    disco = [1, 0, -1, 0]

    for edx in range(2*size - 1):
        for _ in range((2*size - edx) // 2):
            idx += digital[edx % 4]
            jdx += disco[edx % 4]
            matrix[idx][jdx] = element
            element += 1
    return matrix
