def networkWires(n, wires):

    wires.sort(key = lambda w: w[2])
    connected = {i: {i} for i in range(n)}
    dist = 0

    for f, t, l in wires:

        if not f in connected[t]:
            dist += l
            subnet = connected[t] | connected[f]
            for n in subnet:
                connected[n] = subnet
        
    return dist
