# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans = 0
        
        l = []
        h = head
        while h:
            l.append(h.val)
            h = h.next
        
        for i in range(len(l)//2):
            ans = max(ans,l[i]+l[len(l)-1-i])
            
        return ans
        