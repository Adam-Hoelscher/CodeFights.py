from itertools import combinations


def roadsBuilding(cities, roads):
    have = set(tuple(sorted(r)) for r in roads)
    def gen():
        for p in combinations(range(cities), 2):
            if p not in have:
                yield p

    return list(gen())