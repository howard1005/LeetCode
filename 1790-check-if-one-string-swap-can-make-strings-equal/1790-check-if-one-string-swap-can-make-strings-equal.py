class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        if s1 == s2:
            return True
        
        n = len(s2)
        l1,l2 = list(s1),list(s2)
        
        for i in range(n):
            for j in range(i+1,n):
                l2[i],l2[j] = l2[j],l2[i]
                if l1 == l2:
                    return True
                l2[i],l2[j] = l2[j],l2[i]
        
        return False
            