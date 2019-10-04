def houseOfCats(legs):

    pairs = legs // 2
    
    return list(range(pairs % 2, pairs + 1, 2))
