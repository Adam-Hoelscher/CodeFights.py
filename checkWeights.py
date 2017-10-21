def checkWeights(boxes, packageWeight):
    goal = sum([(b[1]+b[0])*(b[1]-b[0]+1)//2 for b in boxes])
    return packageWeight - goal

if __name__ == '__main__':
    boxes= [[1, 2],
            [3, 4]]
    packageWeight= 10
    print(checkWeights(boxes, packageWeight))