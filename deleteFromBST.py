def deleteFromBST(t, queries):

    def max_of_tree(t):
        if t is None: return(None)
        while t.right is not None:
            t = t.right
        return(t.value)

    def remove_right(t):
        if t.right is None:
            return(t.left)
        else:
            t.right = remove_right(t.right)
        return(t)

    def f1(t, q):
        if t is None: return(None)
        if q == t.value:
            if t.left:
                t.value = max_of_tree(t.left)
                t.left = remove_right(t.left)
            else:
                t = t.right
        elif q < t.value:
            t.left = f1(t.left, q)
        elif q > t.value:
            t.right = f1(t.right, q)
        return(t)

    for q in queries:
        t = f1(t, q)

    return(t)
