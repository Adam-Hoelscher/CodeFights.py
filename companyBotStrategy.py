def companyBotStrategy(trainingData):

    s = c = 0
    for t, a in trainingData:
        if a > 0:
            s += t
            c += 1
    return s / max(1, c)