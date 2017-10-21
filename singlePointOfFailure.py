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

    def remove_trivial_SPFs():
        num_del = 0
        for node_num, conn_set in enumerate(connections):
            if sum(conn_set) == 1:
                remove_node(node_num)
                num_del += 1
        return(num_del)

    trivial_SPFs = remove_trivial_SPFs()

    node_num = 0
    while node_num < len(connections):
        find_subnet(node_num)
        node_num += 1

    return(len(connections) - 1 + trivial_SPFs)


if __name__ == '__main__':

    from copy import deepcopy

    # test the algorithm using example 8
    connections= [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                  [0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    print(singlePointOfFailure(connections), True)

    # test the algorithm using example 9
    with open('./data/singlePointOfFailure.txt') as file:
        input = file.readlines()
    input = [str(x).strip('\n') for x in input]
    input = [[int(x) for x in line] for line in input]
    connections = deepcopy(input)
    print(singlePointOfFailure(connections))
