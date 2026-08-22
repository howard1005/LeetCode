class Solution:
    def checkDivisibility(self, n: int) -> bool:
        l = [int(c) for c in list(str(n))]
        
        t,p = 0,1

        for e in l:
            t += e
            p *= e

        if n%(t+p)==0:
            return True

        return False 