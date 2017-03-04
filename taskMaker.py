def taskMaker(source, challengeId):

    chalString = '//DB ' + str(challengeId) + '//'

    out = []
    for ln in source:
        if ln.strip()[0:2]=='//':
            if ln.strip()[0:len(chalString)]==chalString:
                out.pop()
                out.append(ln.replace(chalString,''))
        else:
            out.append(ln)

    return(out)

if __name__=='__main__':
    source = ["abacaba  dabacaba",
              "//DB 5//abacaba  abacabadabacaba",
              "aaaaaaaa",
              "//DB 3//lalalala",
              "",
              "a",
              "         ",
              "      a     ",
              "codefights",
              "//DB 1//codefights is awesome",
              "//DB 2//    spaces! ! ! ! !  ",
              "//DB 999//reallybignumber"]
    challengeId = 999
    print(taskMaker(source, challengeId))