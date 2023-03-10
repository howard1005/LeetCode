import random

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.l = self._init(head)
        
    def _init(self, head):
        l = []
        h = head
        while h:
            l.append(h.val)
            h = h.next
        return l
    
    
    def getRandom(self) -> int:
        return random.sample(self.l,1)[0]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()