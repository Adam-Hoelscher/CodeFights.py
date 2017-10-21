def copycatKeeper(books):

    col_count = max(map(len, books))

    transposed = []
    for c in range(col_count):
        temp = []
        for r in books:
            try:
                temp.append(r[c])
            except:
                pass
        temp.sort()
        transposed.append(temp)

    output = []
    for r in range(len(books)):
        temp = []
        for c in range(col_count):
            try:
                books[r][c]
                temp.append(transposed[c].pop(0))
            except:
                pass
        output.append(temp)

    return output

if __name__ == '__main__':
    books = [["Harry the Otter"],
 ["Of The English"],
 ["A PORTRAIT OF THE ARTIST AS A YOUNG MAN","The Slithering Elves","The Planet of the Night","Ship of Thorns","Devilish me"]]
    print(copycatKeeper(books))