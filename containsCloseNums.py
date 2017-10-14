def containsCloseNums(nums, k):
    last_seen = dict()
    for pos, num in enumerate(nums):
        try:
            if pos - last_seen[num] <= k: return (True)
        except:
            pass
        last_seen[num] = pos

    return (False)


if __name__ == '__main__':
    nums = [0, 1, 2, 3, 5, 2]
    k = 3
    print(containsCloseNums(nums, k))
