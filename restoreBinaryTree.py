#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def restoreBinaryTree(inorder, preorder):

    root_val = preorder[0]
    root = Tree(root_val)
    pos = inorder.index(root_val)

    l_in = inorder[:pos]
    r_in = inorder[(1+pos):]

    l_pre = preorder[1:(pos+1)]
    r_pre = preorder[(1+pos):]

    if l_in: root.left  = restoreBinaryTree(l_in, l_pre)
    if r_in: root.right = restoreBinaryTree(r_in, r_pre)

    return(root)
