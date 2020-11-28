def areFollowingPatterns(strings, patterns):

    hash1 = {}
    hash2 = {}

    for i, (x, y) in enumerate(zip(strings, patterns)):
        p1 = hash1[x] = hash1.get(x, i)
        p2 = hash2[y] = hash2.get(y, i)
        if p1 != p2:
            return False

    return True 
