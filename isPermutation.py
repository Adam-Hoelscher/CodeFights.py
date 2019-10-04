def isPermutation(n, inputArray):

    return sorted(inputArray) == sorted(list(range(1, n+1)))
