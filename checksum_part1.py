def checksum_part1(barcode):

    temp = 0
    for i, d in enumerate(str(barcode).zfill(11)):
        temp += (int(d) * (1+2*((i+1)%2)))
    return (10 - temp)%10

if __name__=='__main__':
    temp = 0
    for i in range(1, int(10e6)):
        temp += 1
    print(temp)
