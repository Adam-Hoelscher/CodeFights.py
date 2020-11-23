ROT_DIG = {
    '0': '0',
    '1': '1',
    '2': '2',
    '5': '5',
    '6': '9',
    '8': '8',
    '9': '6'
}


def add(x):
    return x + 1


def mult(x):
    return 2 * x


def rotate(x):
    try:
        return int(''.join(ROT_DIG[d] for d in str(x)[::-1]))
    except KeyError:
        return None


def kStepMaximization(n, k):

    def gen(n, k):

        if n is None:
            return
            
        elif k == 0:
            yield n

        else:
            yield from gen(add(n), k - 1)
            yield from gen(mult(n), k - 1)
            yield from gen(rotate(n), k - 1)

    return max(gen(n, k))
