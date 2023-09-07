# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        h=head
        l=[]
        while h:
            l.append(h)
            h=h.next
        rl = l[:left-1] + l[left-1:right][::-1] + l[right:]
        for i in range(len(rl)-1):
            rl[i].next = rl[i+1]
        rl[-1].next=None
        return rl[0]