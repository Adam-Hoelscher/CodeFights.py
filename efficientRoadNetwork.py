from collections import defaultdict


def efficientRoadNetwork(n, roads):

    mapping = defaultdict(list)
    for l, r in roads:
        mapping[l].append(r)
        mapping[r].append(l)
        
    def cities_within_steps(src, steps):
        cities = set([src])
        for _ in range(steps):
            new = sum((mapping[c] for c in cities), [])
            cities.update(new)
        return cities
    
    return all(len(cities_within_steps(s, 2)) == n for s in range(n))