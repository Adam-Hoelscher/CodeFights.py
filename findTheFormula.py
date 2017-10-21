def findTheFormula(seq):
    y1 = seq[2]
    y0 = x1 = seq[1]
    x0 = seq[0]

    k = (y1 - y0) // (x1 - x0)
    b = y0 - k * x0

    if abs(k) == 1:
        if k < 0:
            k_out = '-'
        else:
            k_out = ''
    else:
        k_out = str(k)

    if b == 0:
        b_out = ''
    else:
        b_out = str(b)
        if b > 0:
            b_out = "+" + b_out

    return (k_out + 'n' + b_out)
