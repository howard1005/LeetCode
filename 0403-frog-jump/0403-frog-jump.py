class Solution:
    def canCross(self, stones: List[int]) -> bool:
        d = {}
        for stone in stones:
            d[stone] = 0
        d[stones[-1]] = 1
        dp = {}
        
        def dfs(n,k):
            if d[n]:
                return True
            
            if (n,k) in dp:
                return dp[(n,k)]
            dp[(n,k)] = False
            
            for kk in range(k-1,k+2):
                if kk <= 0:
                    continue
                if n+kk in d:
                    dp[(n,k)] |= dfs(n+kk,kk)
            
            return dp[(n,k)]
        
        ans = dfs(0,0)
        
        return ans