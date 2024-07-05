# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        l = []

        h = head
        while h:
            l.append(h.val)
            h = h.next

        ll = []
        for i in range(1,len(l)-1):
            if l[i-1] < l[i] and l[i] > l[i+1]:
                ll.append(i)
            elif l[i-1] > l[i] and l[i] < l[i+1]:
                ll.append(i)

        if len(ll) < 2:
            return [-1,-1]
        
        mx = ll[-1]-ll[0]

        mn = inf
        for i in range(len(ll)-1):
            mn = min(mn,ll[i+1]-ll[i])

        return [mn,mx]