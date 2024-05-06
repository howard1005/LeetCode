# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        l = []
        h = head
        while h:
            l.append(h)
            h = h.next
        
        ll = []
        mx = 0
        for node in l[::-1]:
            if node.val >= mx:
                ll.append(node)
            mx = max(mx,node.val)
            
        for i in range(len(ll)-1,0,-1):
            ll[i].next = ll[i-1]
        ll[0].next = None
        
        return ll[-1]