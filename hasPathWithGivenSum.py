#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def hasPathWithGivenSum(t, s):

    if t is None: return(s == 0)

    def rec(t,s):
        if t is None: return(False)
        is_leaf = (t.left is None and t.right is None)

        target = s - t.value

        if is_leaf: return(target==0)

        l = rec(t.left,  target)
        r = rec(t.right, target)

        # print(t.value, l, r)

        return(l or r)

    return(rec(t,s))
