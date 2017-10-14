# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def rearrangeLastN(l, n):

    def convert(x):
        temp = []
        while x is not None:
            temp.append(x.value)
            x = x.next
        return(temp)

    list_l = convert(l)

    return(list_l[-n:]+list_l[:-n])
