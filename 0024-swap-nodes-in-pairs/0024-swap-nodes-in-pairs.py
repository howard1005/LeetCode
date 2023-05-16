# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        l = []
        h = head
        while h:
            l.append(h)
            h = h.next
        for i in range(0,len(l),2):
            if i+1 < len(l):
                l[i],l[i+1] = l[i+1],l[i]
        for i in range(len(l)-1):
            l[i].next = l[i+1]
        l[-1].next = None
        return l[0]
        