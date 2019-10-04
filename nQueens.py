def nQueens(n):

    solutions = []

    def check_pos(ranks):

        for step in (-1, 0, 1):
            test = [(x - step * y + 1) for y, x in enumerate(ranks)]
            if not len(set(test)) == len(test):
                return False

        return True

    def search(ranks=[]):

        if check_pos(ranks):

            if len(ranks) == n:
                solutions.append([x + 1 for x in ranks])

            else:
                available = [x for x in range(n) if x not in ranks]
                for y in available:
                    search(ranks + [y])

    search()

    return solutions
