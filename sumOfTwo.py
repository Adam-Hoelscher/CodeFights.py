def sumOfTwo(a, b, v):

    if not len(a) * len(b):
        return False

    a.sort()
    b.sort()

    i = 0
    j = len(b)-1
    total = a[i] + b[j]

    while total != v:
        if total < v:
            i += 1
        else:
            j -= 1
        if i == len(a) or j == -1:
            return (False)
        else:
            total = a[i] + b[j]
    return True


if __name__=='__main__':
    a= [1, 2, 3]
    b= [10, 20, 30, 40]
    v= 42
    print(sumOfTwo(a,b,v))