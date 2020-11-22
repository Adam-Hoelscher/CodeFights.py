def productExceptSelf(nums, m):
    sum, prod = 0, 1
    for n in nums:
        sum, prod = (prod + sum * n), prod * n
    return sum % m
