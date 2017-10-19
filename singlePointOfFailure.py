def singlePointOfFailure(connections):

    def remove_node(pos):

        # remove the nodes from the connections
        connections.pop(pos)

        # remove connections to the node
        for from_pos in range(len(connections)):
            connections[from_pos].pop(pos)

    def build_subnet(nodes):

        nodes.sort()
        new_pos = nodes[0]

        # add the connections of the later nodes to the first
        subnet_conn = list()
        for to_pos in range(len(connections)):
            conn = sum(connections[from_pos][to_pos] for from_pos in nodes)
            subnet_conn.append(conn)
        connections[new_pos] = subnet_conn

        # remove the later nodes
        for old_pos in reversed(nodes[1:]):
            remove_node(old_pos)

        # make sure the connections are symmetric
        for pos in range(len(connections)):
            connections[pos][new_pos] = subnet_conn[pos]

        test_subnet(new_pos)

        return()

    def test_subnet(address):

        new_nodes = list()
        for pos, conn in enumerate(connections[address]):
            if conn > 1 and pos != address:
                new_nodes.append(pos)

        if new_nodes:
            build_subnet([address] + new_nodes)

    def find_subnet(pos, path = list()):
        if pos in path:
            cycle_start = path.index(pos)
            build_subnet(path[cycle_start:])
            return(True)
        else:
            for next_pos, conn in enumerate(connections[pos]):
                # check if this node is connected
                if not conn:
                    continue
                # make sure we're not staying in the same place
                if next_pos is pos:
                    continue
                # make sure we're not going backwards
                if path and next_pos == path[-1]:
                    continue

                if find_subnet(next_pos, path + [pos]):
                    return(True)
            return(False)

    search_node = 0
    while search_node < len(connections):
        find_subnet(search_node)
        search_node += 1

    return(search_node - 1)


if __name__ == '__main__':

    from random import getrandbits, seed
    from copy import deepcopy

    seed(42)

    connections= [[0, 1],
                  [1, 0]]

    def grow():
        connections.append([])
        for row in connections[:-1]:
            thing = getrandbits(1)
            row.append(thing)
            connections[-1].append(thing)
        connections[-1].append(0)


    def test_big_o():
        for size in range(3, 301):
            grow()
            rows = len(connections)
            small = min(len(x) for x in connections)
            large = max(len(x) for x in connections)
            print(size, rows, small, large)
            input = deepcopy(connections)
            import cProfile
            cProfile.run('singlePointOfFailure(input)')


    def test_9():
        with open('singlePointOfFailure.txt') as file:
            connections = file.readlines()
        connections = [str(x).strip('\n') for x in connections]
        connections = [[int(x) for x in line] for line in connections]
        import cProfile
        print(singlePointOfFailure(connections))
        cProfile.run('print(singlePointOfFailure(connections))')


    test_9()
