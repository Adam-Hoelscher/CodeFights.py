from heapq import heappush, heappop
from itertools import permutations


def shortestPathWithEdge(start, finish, weight, graph):

    start -= 1
    finish -= 1

    def dijkstra(source):

        visited = set()
        shortest = {source: 0}
        queue = [(0, source)]

        while queue:

            curr_dist, curr_loc = heappop(queue)

            if curr_loc in visited:
                continue

            for dest, dist in enumerate(graph[curr_loc]):

                if not dist:
                    continue

                new_dist = curr_dist + dist
                if new_dist < shortest.get(dest, new_dist + 1):
                    shortest[dest] = new_dist
                    heappush(queue, (new_dist, dest))

            visited.add(curr_loc)

        return shortest

    front = dijkstra(start)
    back = dijkstra(finish)

    temp = front[finish]
    for f, b in permutations(range(len(graph)), 2):
        if not graph[f][b]:
            bridge_dist = front[f] + back[b] + weight
            temp = min([temp, bridge_dist])

    return temp