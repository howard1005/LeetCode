# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def ntol(n):
            ret = []
            head = n
            while head:
                ret.append(head.val)
                head = head.next
            ret.reverse()
            return ret
        
        ll1,ll2 = ntol(l1),ntol(l2)
        
        up,nl = 0,None
        for i in range(max(len(ll1),len(ll2))):
            cum = 0
            if i < len(ll1):
                cum += ll1[i]
            if i < len(ll2):
                cum += ll2[i]
            cum += up
            up,m = cum//10,cum%10
            nl = ListNode(m,nl)
        
        if up:
            return ListNode(up,nl)
        return nl
            