def swapLexOrder(str, pairs):

    length = len(str)
    pairs.sort(key=lambda x: x[0]*length + x[1])

    pairs = [sorted([y - 1 for y in x]) for x in pairs]
    print(pairs)
    linked_to = [set([x]) for x in range(length)]

    for [low, high] in pairs:
        linked_to[low].add(high)
        linked_to[high].add(low)

    def prop_set(x):

        prop = set()

        def search(from_pos):
            for pos in linked_to[from_pos]:
                if pos not in prop:
                    prop.add(pos)
                    search(pos)

        [search(y) for y in x]
        return(prop)

    groups = set()
    for pos in linked_to:
        prop = prop_set(pos)
        groups.add(tuple(sorted(prop)))

    chars = ['' for x in range(length)]

    for group_numbers in groups:
        group_letters = [str[pos] for pos in group_numbers]
        group_letters.sort()
        for pos in group_numbers:
            chars[pos] = group_letters.pop()

    return(''.join(chars))
