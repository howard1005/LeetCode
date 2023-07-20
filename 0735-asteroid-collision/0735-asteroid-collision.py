class LL:
    def __init__(self,v,p=None,n=None):
        self.v = v
        self.p = p
        self.n = n

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        
        h = LL(0)
        p = h
        for v in asteroids:
            n = LL(v,p)
            p.n = n
            p = n
        
        def remove(node):
            node.p.n = node.n
            if node.n:
                node.n.p = node.p
            
        node = h.n
        while node.n:
            v1,v2 = node.v,node.n.v
            if v1 > 0 and v2 < 0:
                if abs(v1) > abs(v2):
                    remove(node.n)
                elif abs(v1) < abs(v2):
                    remove(node)
                    node = node.p
                else:
                    remove(node)
                    remove(node.n)
                    node = node.p
            else:
                node = node.n
        
        node = h.n
        while node:
            ans.append(node.v)
            node = node.n 
        
        return ans