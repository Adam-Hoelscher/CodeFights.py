#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def kthSmallestInBST(t, k):

    stack = []
    values = []

    while(len(values) < k):
        while t is not None:
            stack.append(t)
            t = t.left
        top = stack.pop()
        values.append(top.value)
        t = top.right

    return(values[-1])
