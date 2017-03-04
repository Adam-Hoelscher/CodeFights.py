def tripletSum(x, a):

    a.sort()

    for i in range(len(a)):
        for j in range(i+1,len(a)):
            for k in range(j+1,len(a)):
                if a[i]+a[j]+a[k] == x:
                    return True
                elif a[i]+a[j]+a[k] > x:
                    break

    return False

