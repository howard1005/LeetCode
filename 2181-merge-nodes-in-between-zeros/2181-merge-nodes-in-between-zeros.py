# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []

        cum = 0
        h = head
        while h:
            if h.val == 0:
                l.append(cum)
                cum = 0
            else:
                cum += h.val
            h = h.next

        nl = []
        for v in l[1:]:
            nl.append(ListNode(v))
        for i in range(len(nl)-1):
            nl[i].next = nl[i+1]
        
        return nl[0]
        

