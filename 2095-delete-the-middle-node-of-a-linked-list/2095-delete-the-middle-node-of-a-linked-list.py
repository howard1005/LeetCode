# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        h = head
        while h:
            l.append(h)
            h = h.next
        i = len(l)//2
        if i:
            l[i-1].next = l[i].next
        else:
            return l[i].next
        return head