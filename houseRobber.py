from functools import lru_cache


def houseRobber(nums):

    @lru_cache(None, False)
    def rf(nums):

        if not nums:
            return 0

        # rob the first house, skip the second
        take = nums[0] + rf(nums[2:])
        
        # skip the first house, rob whatever is left
        skip = rf(nums[1:])

        return max([take, skip])
        
    return rf(tuple(nums))
