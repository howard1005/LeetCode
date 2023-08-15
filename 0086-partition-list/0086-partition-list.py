# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        p1,p2 = [],[]
        h = head
        while h:
            if h.val < x:
                p1.append(h)
            else:
                p2.append(h)
            h = h.next
        p = p1 + p2
        for i in range(len(p)-1):
            p[i].next = p[i+1]
        p[-1].next = None
        return p[0]