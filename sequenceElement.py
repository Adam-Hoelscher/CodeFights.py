def sequenceElement(a, n):

    a = tuple(a)
    start = a

    for i in range(n):
        
        # check to see if we've run long enough to find a loop
        if a == start and i:
            steps_after_loop = n % i
            return sequenceElement(a, steps_after_loop)
        
        else:
            a = a[1:] + (sum(a) % 10, )
    
    return a[0]
