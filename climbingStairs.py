# recursive with memoization
from functools import lru_cache


@lru_cache(None, False)
def climbingStairs(n):
    if n <= 2:
        return n
    else:
        return climbingStairs(n-2) + climbingStairs(n-1)


# iterative
def climbingStairs(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return b
