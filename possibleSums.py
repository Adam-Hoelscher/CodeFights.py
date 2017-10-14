def possibleSums(coins, quantity):

    sums = set([0])

    for coin_value, number in zip(coins, quantity):
        new_sums = set([0])
        for q in range(number + 1):
            for base in sums:
                new_sums.add(base + q * coin_value)
        sums = new_sums

    sums.remove(0)

    return(len(sums))
