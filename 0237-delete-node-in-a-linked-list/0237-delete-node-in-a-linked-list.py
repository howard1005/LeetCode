# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        l = []
        h = node
        while h:
            l.append(h)
            h = h.next
        for i in range(len(l)-1):
            l[i].val = l[i+1].val
        l[-2].next = None
    
        