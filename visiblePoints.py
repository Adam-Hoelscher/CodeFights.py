

def visiblePoints(points):

    from math import atan2, pi

    maxView = 0
    field_width = 2*pi*(45.0001/360)

    angles = [atan2(y, x) % (2*pi) for x, y in points]
    angles.sort()

    # angle_differences = [j - i for i, j in zip(angles[:-1], angles[1:])]
    # if max(angle_differences)

    for x in angles:
        if x < field_width:
            angles.append(x+(2*pi))
        else:
            break
    
    for i, start_angle in enumerate(angles):
        for j in range(i, len(angles)):
            if angles[j] - angles[i] >= field_width:
                break
        temp = range(i, j)
        if len(temp) > maxView:
            maxView = len(temp)

    return maxView

if __name__=='__main__':
    points = [
        [1,1],#
        [3,1],
        [3,2],
        [3,3],#
        [1,3],#
        [2,5],#
        [1,5],#
        [-1,-1],
        [-1,-2],
        [-2,-3],
        [-4,-4]]
    points = [[5,4]]
    print(visiblePoints(points))