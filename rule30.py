def rule30(n):

    v = 1
    for _ in range(n):
        v ^= 2 * v | 4 * v

    return bin(v).count('1')
