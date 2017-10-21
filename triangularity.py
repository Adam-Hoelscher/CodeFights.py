def triangularity(segmentsLength):

    l = sorted(segmentsLength)
    for k  in range(len(segmentsLength) - 2):
        if l[-1-k] < l[-2-k] + l[-3-k]:
            return True
    return False
