# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = []
        h = head
        while h:
            l.append(h)
            h = h.next
        prev,next = None,None
        if n < len(l):
            prev = l[-n-1]
        if n > 1:
            next = l[-n+1]
        if prev:
            prev.next = next
            return head
        else:
            return head.next