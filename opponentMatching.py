def opponentMatching(xp):

    queue = sorted(enumerate(xp), key=lambda x: x[1])
    matches = []

    while len(queue) >= 2:
        min_dist = float('Inf')
        for (id0, x0), (id1, x1) in zip(queue, queue[1:]):
            if x1 - x0 < min_dist:
                min_dist = x1 - x0
                pair = (id0, x0), (id1, x1)

        matches.append(sorted(player[0] for player in pair))
        for p in pair:
            queue.remove(p)

    return matches