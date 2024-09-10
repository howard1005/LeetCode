# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def gcd(a,b):
            while b:
                a,b = b,a%b
            return a

        l = []
        h = head
        while h:
            l.append(h)
            h = h.next

        gl = []
        for i in range(1,len(l)):
            a,b = l[i-1].val,l[i].val
            g = gcd(a,b)
            gl.append(ListNode(g))

        rl = []
        for i in range(len(gl)):
            rl.append(l[i])
            rl.append(gl[i])
        rl.append(l[-1])

        for i in range(1,len(rl)):
            rl[i-1].next = rl[i]
        rl[-1].next = None

        return rl[0]
        