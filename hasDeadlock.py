def hasDeadlock(connections):

    if min([len(c) for c in connections]):
        return(True)

    unchecked = set([x for x in range(len(connections))])

    def search(loc, path = set()):
        if loc not in unchecked: return False
        if loc in path: return True
        for conn in connections[loc]:
            next_path = set(path)
            next_path.add(loc)
            if search(conn, next_path):
                return True
        unchecked.remove(loc)
        return(False)

    while unchecked:
        for next_pos in unchecked: break
        if search(next_pos): return True

    return(False)

if __name__ == '__main__':
    connections= [[1,2,3],
     [2,3],
     [3],
     []]
    connections= [[1,2],
     [2],
     [],
     [4],
     [3]]
    print(hasDeadlock(connections))
