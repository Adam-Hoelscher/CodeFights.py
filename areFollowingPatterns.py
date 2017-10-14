def areFollowingPatterns(strings, patterns):

    hash1 = dict()
    hash2 = dict()

    for i, (x, y) in enumerate(zip(strings, patterns)):
        try:
            p1 = hash1[x]
        except:
            p1 = i
            hash1[x] = i
        try:
            p2 = hash2[y]
        except:
            p2 = i
            hash2[y] = i
        if p1 != p2:
            return(False)

    return(True)

if __name__ == '__main__':
    strings= ["cat",
              "dog",
              "doggy"]
    patterns= ["a",
               "b",
               "b"]
    print(areFollowingPatterns(strings,patterns))
