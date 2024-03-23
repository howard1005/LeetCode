# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return head
        l = []
        h = head
        while h:
            l.append(h)
            h = h.next
        
        ll = []
        i,j = 0,len(l)-1
        while 1:
            ll.append(l[i])
            if i<j:
                ll.append(l[j])
            else:
                break
            i += 1
            j -= 1
        for i in range(len(ll)-1):
            ll[i].next = ll[i+1]
        ll[-1].next = None
        
        return ll[0]
            
        