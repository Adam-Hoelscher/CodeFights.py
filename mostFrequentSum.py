#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

from collections import Counter


def mostFrequentSum(t):

    sums = Counter()
    
    def rf(t):
        
        if t is None:
            return 0
        
        temp = t.value
        temp += rf(t.left)
        temp += rf(t.right)
        sums.update([temp])
        return temp
    
    rf(t)
    
    if not sums:
        return []
    else:
        freq = sums.most_common()[0][1]
        sum_val = sorted([k for k, v in sums.items() if v == freq])
        return sum_val
        