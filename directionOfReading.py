def directionOfReading(numbers):

    size = len(numbers)
    square = [str(x).zfill(size) for x in numbers]
    return [int(''.join(x)) for x in zip(*square)]
