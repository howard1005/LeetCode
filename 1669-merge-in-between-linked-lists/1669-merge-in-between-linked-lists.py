# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        l1,l2 = [],[]
        
        h = list1
        while h:
            l1.append(h)
            h = h.next
            
        h = list2
        while h:
            l2.append(h)
            h = h.next
        
        l1[a-1].next = l2[0]
        
        l2[-1].next = l1[b+1]
        
        return l1[0]
        