def subtractionByRegrouping(minuend, subtrahend):

    digs = lambda x: (int(d) for d in str(x)[::-1])
    
    temp = []
    borrow = False
    for a, b in zip(digs(minuend), digs(subtrahend)):
        a -= borrow
        if b > a:
            borrow = True
            a += 10
        else:
            borrow = False
            
        temp.append(a)
        
    return temp
