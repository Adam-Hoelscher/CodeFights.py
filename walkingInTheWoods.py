from collections import defaultdict
from uuid import uuid4


def walkingInTheWoods(n, wmap):

    members = defaultdict(set)
    groups = defaultdict(uuid4)
    islands = set(range(n))
    
    for a, b in wmap:

        a_grp = groups[a]
        members[a_grp].add(a)
        islands.discard(a)
        
        b_grp = groups[b]
        members[b_grp].add(b)
        islands.discard(b)
        
        if a_grp != b_grp:
            members[a_grp].update(members[b_grp])
            for k in members[b_grp]:
                groups[k] = a_grp
            del members[b_grp]

    return len(members) + len(islands) - 1
