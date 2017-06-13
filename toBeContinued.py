def toBeContinued(f):

    if f[1] == 0:
        return []

    temp = [f[0] // f[1]]
    temp += toBeContinued([f[1], f[0] % f[1]])
    return temp

if __name__ == '__main__':
    f = [1024, 2017]
    print(toBeContinued(f))