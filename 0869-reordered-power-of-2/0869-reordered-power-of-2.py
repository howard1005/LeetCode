from itertools import permutations

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        l = []
        while n:
            l.append(str(n%10))
            n //= 10
        
        pl = list(permutations(l))
        for t in pl:
            if t[0] != '0':
                n = int(''.join(t))
                if (n&(n-1))==0:
                    return True
            
        return False