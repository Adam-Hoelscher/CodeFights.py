BUDGET = 20
TYPES = ["UberX", "UberXL", "UberPlus", "UberBlack", "UberSUV"]

def fancyRide(l, fares):
    
    for i, f in enumerate(fares):
        if l * f > BUDGET:
            return TYPES[i - 1]

    return TYPES[-1]