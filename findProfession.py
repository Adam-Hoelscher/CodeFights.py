def findProfession(level, pos):

    binary = str(bin(pos-1))[2:]
    prof = 0
    for i in reversed(binary):
        if int(i):
            prof = 1 - prof

    if prof:
        return('Doctor')
    else:
        return('Engineer')
