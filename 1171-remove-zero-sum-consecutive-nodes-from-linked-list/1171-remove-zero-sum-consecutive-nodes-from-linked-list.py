# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ansl = []
        
        l = []
        h = head
        while h:
            l.append(h)
            h = h.next
            
        i = 0
        while i < len(l):
            cum = 0
            flag = True
            for j in range(i,len(l)):
                cum += l[j].val
                if cum == 0:
                    i = j+1
                    flag = False
                    break
            if flag:
                ansl.append(l[i])
                i += 1
        
        if not ansl:
            return None
        
        for i in range(len(ansl)-1):
            ansl[i].next = ansl[i+1]
        ansl[-1].next = None
        
        return ansl[0]
            