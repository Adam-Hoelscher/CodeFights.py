from collections import deque


def treeDiameter(n, tree):

    if len(tree) < 2:
        return len(tree)
    
    edges = {}

    def add_edges(x, y):
        if x in edges:
            edges[x].append(y)
        else:
            edges[x] = [y]
            
    for a, b in tree:
        add_edges(a, b)
        add_edges(b, a)
    
    def find_farthest(f):

        queue = deque([(f, 0)])
        seen = set()

        while queue:
            at, dist = queue.popleft()
            for t in edges.get(at):
                if t in seen:
                    continue
                else:
                    queue.append((t, dist+1))
                    seen.add(t)

        return at, dist
    
    point_1, _ = find_farthest(0)
    _, answer = find_farthest(point_1)

    return answer
