# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):

    temp = []

    while l1 is not None and l2 is not None:
        if l2.value < l1.value:
            temp.append(l2.value)
            l2 = l2.next
        else:
            temp.append(l1.value)
            l1 = l1.next

    while l1 is not None:
        temp.append(l1.value)
        l1 = l1.next

    while l2 is not None:
        temp.append(l2.value)
        l2 = l2.next

    return(temp)
