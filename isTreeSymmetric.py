#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def isTreeSymmetric(t):

    if t is None: return(True)

    def val_left(x):
        if x is None:
            print('None')
            return([''])
        print(x.value)
        return([x.value] + val_left(x.left) + val_left(x.right))

    def val_right(x):
        if x is None:
            return([''])
        return([x.value] + val_right(x.right) + val_right(x.left))

    left_side = val_left(t.left)
    right_side = val_right(t.right)

    for l, r in zip(left_side, right_side):
        if l != r: return(False)

    return(True)
