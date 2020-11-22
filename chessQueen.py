from itertools import product


def chessQueen(q):

    files = 'abcdefgh'

    q_file = files.find(q[0])
    q_rank = int(q[-1]) - 1
    
    safe_locs = set(product(range(8), range(8)))

    for file in range(8):
        file_diff = q_file - file
        if not file_diff:
            for rank in range(8):
                safe_locs.discard((file, rank))
        else:
            for direction in range(-1, 2):
                threatened_rank = q_rank + file_diff * direction
                safe_locs.discard((file, threatened_rank))
        
    safe = [f'{files[f]}{r+1}' for f, r in safe_locs]
    return sorted(safe)