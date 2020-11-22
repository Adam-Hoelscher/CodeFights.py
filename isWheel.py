def isWheel(adj):

    def search(pos, seen):

        connections = adj[pos]

        if sum(connections) != 3:
            return False

        next_pos = [i for i, c in enumerate(connections) if c and (i not in seen)]

        if not next_pos:
            return len(seen) == len(adj)
        else:
            return search(pos=next_pos[0], seen=seen+(next_pos[0],))

    for idx, vertex in enumerate(adj):        
        if sum(vertex) == len(adj) - 1:
            pos = 0 if idx else 1
            return search(pos, (idx, pos))

    return False