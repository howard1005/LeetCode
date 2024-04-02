class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def enc(a):
            d = {}
            l = []
            n = 0
            for c in a:
                if c not in d:
                    d[c] = n
                    n += 1
                l.append(d[c])
            return l
        if enc(s) == enc(t):
            return True
        return False
                    
            