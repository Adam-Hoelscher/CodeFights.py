# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def reverseNodesInKGroups(l, k):

    def convert(x):
        temp = []
        while x is not None:
            temp.append(x.value)
            x = x.next
        return(temp)

    list_l = convert(l)

    temp = []
    for start in range(0, len(list_l), k):
        end = start + k
        sublist = list_l[start:end]
        if len(sublist) < k:
            temp += sublist[:]
        else:
            temp += sublist[::-1]

    return(temp)
