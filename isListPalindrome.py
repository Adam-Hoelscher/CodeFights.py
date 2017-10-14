# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):

    temp = []
    i = 0
    while l is not None:
        temp.append(l.value)
        l = l.next

    return(temp == temp[::-1])
