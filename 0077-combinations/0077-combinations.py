class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def comb(i,l):
            if len(l) == k:
                ans.append(l[:])
                return
            for j in range(i,n+1):
                l.append(j)
                comb(j+1,l)
                l.pop()
        comb(1,[])
        
        return ans