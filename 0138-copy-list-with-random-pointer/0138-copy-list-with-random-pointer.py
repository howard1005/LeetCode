"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        l = []
        h = head
        i = 0
        while h:
            l.append(Node(h.val))
            if i > 0:
                l[i-1].next = l[i]
            h.val = i
            i+=1
            h = h.next
        h = head
        i = 0
        while h:
            if h.random == None:
                l[i].random = None
            else:
                l[i].random = l[h.random.val]
            i+=1
            h = h.next
        
        return l[0]