def nextLarger(a):

    seen = []
    temp = []
    for num in reversed(a):
        if not seen:
            temp = [-1] + temp
        else:
            for c in seen:
                if c > num:
                    temp = [c] + temp
                    break
            else:
                temp = [-1] + temp
        if num in seen: seen.rm(num)
        seen = [num] + seen

    return(temp)
