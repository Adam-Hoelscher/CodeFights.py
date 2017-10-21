def theGunner(bullets, targets):

    from itertools import permutations
    options = permutations(bullets)

    steps = []
    for opt in options:
        result = [targets[i] - opt[i] for i in range(len(targets))]
        if max(result) <= 0:
            return 1
        else:
            steps.append(theGunner(bullets, result))

    return 1 + min(steps)


if __name__ == '__main__':
    bullets = [2, 5, 6]
    targets = [20, 38, 46]
    print(theGunner(bullets, targets))