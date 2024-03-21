# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        h = head
        while h:
            l.append(h.val)
            h = h.next
        l.reverse()
        h = head
        i = 0
        while h:
            h.val = l[i]
            h = h.next
            i += 1
        return head