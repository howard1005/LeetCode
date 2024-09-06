# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        sd = set(nums)

        l = []
        h = head
        while h:
            if h.val not in sd:
                l.append(h)
            h = h.next

        if not l:
            return None

        for i in range(1,len(l)):
            l[i-1].next = l[i]
        l[-1].next = None

        return l[0]

        
        