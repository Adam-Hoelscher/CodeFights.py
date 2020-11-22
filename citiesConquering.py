def citiesConquering(n, roads):

    ans = [-1 for _ in range(n)]

    free = {k: set() for k in range(n)}
    for a, b in roads:
        free[a].add(b)
        free[b].add(a)

    day = 0
    conquered = set([None])

    while conquered:

        day += 1
        next_conq = set()

        for city, neighbors in free.items():
            free[city] -= conquered
            if len(neighbors) <= 1:
                next_conq.add(city)
                ans[city] = day

        for city in next_conq:
            free.pop(city, None)
            
        conquered = next_conq

    return ans
