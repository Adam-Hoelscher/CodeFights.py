from itertools import chain


def parkingSpot(carDimensions, parkingLot, luckySpot):

    # extract the coordinates of the spot
    x1, y1, x2, y2 = luckySpot

    # increment the end coordinates for easier slicing
    x2 += 1; y2 += 1

    # if the spot is oriented vertically flip the coordinate system
    if x2 - x1 == carDimensions[0]:
        parkingLot = list(zip(*parkingLot))
        (x1, y1), (x2, y2) = (y1, x1), (y2, x2)

    # filter down to just the rows we're trying to park in
    rows = parkingLot[x1:x2]

    # generate the spots that have to be clear to enter from each side
    left = chain(*(r[:y2] for r in rows))
    rght = chain(*(r[y1:] for r in rows))

    # if all of the spots are clear from either side, we can park
    return not any(left) or not any(rght)
