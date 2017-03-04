def digitSumInverse(sum, numberLength):

    if 0 > sum or sum > numberLength*9:
        return 0
    elif numberLength == 1:
        return 1

    temp = 0
    for i in range(10):
        temp += digitSumInverse(sum - i, numberLength - 1)

    return temp


if __name__=='__main__':
    print(digitSumInverse(5, 2))
    # print(digitSumInverse(25, 4))
    # for s in range(100+1):
    #     for n in range(2,15+1):
    #         print(s, n, digitSumInverse(s,n))
