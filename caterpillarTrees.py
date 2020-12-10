from collections import Counter, defaultdict, deque
from heapq import heappop, heappush, heappushpop


def caterpillarTreesA(n, edges):

    full_graph = {i: set() for i in range(n)}

    def add_edge(x, y, graph):
        graph[x].add(y)
        graph[y].add(x)

    for a, b in edges:
        add_edge(a, b, full_graph)

    comps = []
    unseen = set(range(n))
    while unseen:
        
        connected = set([(unseen.pop(), None)])
        comp_graph = defaultdict(set)
        at = None
        tree = True
        
        while connected:

            at, prior = connected.pop()
                
            for n in list(full_graph[at]):
                
                unseen.discard(n)

                if n in comp_graph and n != prior:
                    tree = False

                if n not in comp_graph and len(full_graph[n]) > 1:                
                    connected.add((n, at))
                    add_edge(at, n, comp_graph)

                full_graph[n].discard(at)
                
        comps.append([comp_graph, tree])

    tree_count = 0
    cat_count = 0

    for c in comps:
        
        graph, tree = c
        
        if tree:
            tree_count += 1

            degree = (len(v) for v in graph.values())
            counts = Counter(degree)
            cat_count += not counts or counts[1] == 2

    return [tree_count, cat_count]


def caterpillarTreesB(n, edges):

    full_graph = {i: set() for i in range(n)}

    for a, b in edges:
        full_graph[a].add(b)
        full_graph[b].add(a)

    comps = []
    unseen = set(range(n))
    
    cache = {}
    def check(start):

        seen = set()
        queue = deque()

        queue.append(start)
        result = []

        while queue:
            at = queue.popleft()
            result.append(at)
            unseen.discard(at)

            seen.add(at)

            children = full_graph[at]
            for child in list(children):
                full_graph[child].discard(at)
                if child not in seen:
                    queue.append(child)

        print(full_graph)
        while result:

            at = result.pop()
            tree = cat = True
            kids_with_kids = 0

            children = full_graph[at]
            for child in list(children):
                child_tree, child_cat, child_kids = cache[child]
                print(at, child, child_tree, child_cat, child_kids)
                tree &= child_tree
                cat &= child_cat
                kids_with_kids += child_kids > 0

            cat &= kids_with_kids < 2
            kids = len(children)

            cache[at] = tree, cat, kids

        return cache[start]

    comps = []
    # unseen=set([20])
    while unseen:
        seed = max(unseen)
        comps.append(check(seed))
    print(comps)

    tree_count = cat_count = 0
    for t, c, _ in comps:
        tree_count += t
        cat_count += c
        
    return [tree_count, cat_count]

from random import randint, random
from itertools import combinations
import json

# k = 0
# while True:
#     # n = randint(1, 1e5)
#     n = randint(10, 5e1)
#     edges = [[a, b] for a, b in combinations(range(n), 2) if random() < .05]
    
#     k += 1
#     print(k, n)

#     a = caterpillarTreesA(n, edges)
#     b = caterpillarTreesB(n, edges)
#     if a != b:
#         json.dump(open(f'caterpillars/{k}.json'))
for item in json.load(open('caterpillar.json'))[-3:-2]:

    n, edges = item.values()

    a = caterpillarTreesA(n, edges)
    b = caterpillarTreesB(n, edges)
    print(a, b)