#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def isSubtree(t1, t2):

    def check_equal(t1, t2):
        if t1 is None and t2 is None: return(True)
        if t1 is None or t2 is None: return(False)
        if t1.value != t2.value: return(False)
        if not check_equal(t1.left,  t2.left ): return(False)
        if not check_equal(t1.right, t2.right): return(False)
        return(True)

    if check_equal(t1, t2): return(True)
    if t1 is None: return(False)
    if isSubtree(t1.left,  t2): return(True)
    if isSubtree(t1.right, t2): return(True)
    return(False)
