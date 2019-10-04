import functools

def mergingVines(vines, n):
    def nTimes(n):
        return lambda x: functools.reduce(lambda f, g: lambda x: f(g(x)), [x] * n, lambda x: x)

    @nTimes(n)
    def sumOnce(vines):
        res = [vines[i] + vines[i + 1] for i in range(0, len(vines) - 1, 2)]
        if len(vines) % 2 == 1:
            res.append(vines[-1])
        return res

    return sumOnce(vines)
