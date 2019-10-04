from math import log

def currencyArbitrage(exchange):
    
    all_weights = [[-log(rate) for rate in row] for row in exchange]
    start_cost = all_weights[0]
    costs = start_cost[::]

    for _ in exchange:

        # take a note of current state
        temp = tuple(costs)

        # loop through source nodes
        for curr, node_weights in enumerate(all_weights):

            # loop through destination nodes
            for target, weight in enumerate(node_weights):

                # figure out cost to get to dest from source
                from_curr = costs[curr] + weight

                # if this path is shorter, use it instead
                if from_curr < costs[target]:
                    costs[target] = from_curr

        # check if we found a negative weight cycle
        if costs[0] < start_cost[0]:
            return True

        # if there are no neg weight cycles and we're stationary
        elif tuple(costs) == temp:
            return False

    # we're not stationary, but if the graph had no negative weight cycles,
    # we would be. therefore, there is a negative weight cycle.
    return True
