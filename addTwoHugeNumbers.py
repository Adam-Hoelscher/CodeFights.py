# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

from itertools import zip_longest

def addTwoHugeNumbers(a, b):

    output = []
    carry = 0

    def convert(x):
        temp = []
        while x is not None:
            temp.append(x.value)
            x = x.next
        return(temp)

    la = convert(a)[::-1]
    lb = convert(b)[::-1]

    for x, y in zip_longest(la, lb, fillvalue=0):
        z = x + y + carry
        output.append(z % 10000)
        carry = z // 10000

    while carry:
        z = carry
        output.append(z % 10000)
        carry = z // 10000

    return(output[::-1])
