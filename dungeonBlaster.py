from string import ascii_lowercase, ascii_uppercase


def dungeonBlaster(m):

    h = len(m)
    w = len(m[0])
    map = {}

    seen = set()
    spaces = set()
    keys = set()
    doors = {}

    # located the start position
    for x, row in enumerate(m):
        for y, square in enumerate(row):
            pos = x, y
            if square == '*':
                spaces.add(pos)
            map[pos] = square

    # while there are spaces we have not explored
    while spaces:

        # take a step in each direction
            x, y = spaces.pop()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:

            pos = (x + dx) % h, (y + dy) % w
            
                if pos in seen:
                    continue

            square = map[pos]

                # if we've found the exit, stop
                if square == '^':
                    return True

                # if it's an open space we can expand it later
                elif square == ' ':
                    spaces.add(pos)

                # if we found a key, pick it up and now it's a regular space
                elif square in ascii_lowercase:
                    keys.add(square)
                    spaces.add(pos)

                # if we found a door, add it to the list of doors to check
                elif square in ascii_uppercase:
                    doors[square] = pos

                seen.add(pos)

        # open any doors for which we have found a key
        for k in keys:
            if (D := k.upper()) in doors:
                # if we've opened the door, it's now a space
                spaces.add(doors.pop(D))

    return False
