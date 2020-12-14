from collections import deque
from itertools import chain, permutations, product

import numpy

HORIZONTAL = 0
VERTICAL = 1


def rodInLabyrinth(labyrinth):

    height = len(labyrinth)
    width = len(labyrinth[0])
    goals = set([
        (height - 2, width - 1, VERTICAL),
        (height - 1, width - 2, HORIZONTAL)
    ])

    def check(r, c, shape):

        r0 = r - shape[0] // 2
        r1 = r + shape[0] // 2 + 1
        if not 0 <= r0 < r1 <= height:
            return False

        c0 = c - shape[1] // 2
        c1 = c + shape[1] // 2 + 1
        if not 0 <= c0 < c1 <= width:
            return False

        spaces = chain(*(labyrinth[i][c0:c1] for i in range(r0, r1)))
        return all(s == '.' for s in spaces)

    can_occupy = set()
    can_rotate = set()

    for i, j in product(range(height), range(width)):

        if check(i, j, (1, 3)):
            can_occupy.add((i, j, HORIZONTAL))
        if check(i, j, (3, 1)):
            can_occupy.add((i, j, VERTICAL))

        if check(i, j, (3, 3)):
            can_rotate.add((i, j))

    start_loc = (0, 1, HORIZONTAL)
    start_dist = 0
    queue = deque([(start_loc, start_dist)])
    seen = set()

    while queue:

        at, dist = queue.popleft()

        if at in seen or at not in can_occupy:
            continue
        elif at in goals:
            return dist

        seen.add(at)

        r, c, rotation = at
        for (dr, dc), sign in product(permutations([0, 1]), [-1, 1]):
            next_pos = r + sign * dr, c + sign * dc, rotation
            next_state = next_pos, dist + 1
            queue.append(next_state)

        if (r, c) in can_rotate:
            next_pos = r, c, 1 - rotation
            next_state = next_pos, dist + 1
            queue.append(next_state)

    return -1
