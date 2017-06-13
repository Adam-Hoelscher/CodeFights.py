def studentsAge(students):

    temp = 0
    hash = dict()

    for x in students:
        temp += hash.get(x, 0)
        hash[x+1] = hash.get(x+1, 0) + 1

    return temp

if __name__=='__main__':
    s = [2, 4, 3, 4, 6]
    print(studentsAge(s))