import bisect


def countSmallerToTheRight(nums):

    seen = []
    temp = 0

    for n in nums:
        idx = bisect.bisect(seen, n)
        temp += len(seen) - idx
        seen.insert(idx, n)
    
    return temp
