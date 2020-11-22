from collections import defaultdict

def namingRoads(roads):

    names = defaultdict(set)
    for a, b, r in roads:
        if any([
            b in names[r - 1],
            b in names[r + 1],
            a in names[r - 1],
            a in names[r + 1]
        ]) :
            return False
        else:
            names[r].add(a)
            names[r].add(b)
            
    return True

