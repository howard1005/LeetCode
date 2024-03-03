class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = [[[None for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)]
        
        
        def dfs(i,j,k):
            w = i&1
            if i >= n:
                return [0,0]
            if j >= n:
                return [0,0]
            
            if dp[i][j][k] != None:
                return dp[i][j][k]
            ret = [0,0]
            dp[i][j][k] = ret
            
            if n-j <= 2*k:
                ret[w] = sum(piles[j:])
                return ret
            
            cum = 0
            kk = 0
            for a in range(j,min(n,j+k*2)):
                cum += piles[a]
                kk += 1 
                _ret = dfs(i^1,a+1,max(k,kk))
                if (ret[w],-ret[w^1]) <= (_ret[w] + cum,-_ret[w^1]):
                    ret[w] = _ret[w] + cum
                    ret[w^1] = _ret[w^1]            
            
            return ret
                    
        
        return dfs(0,0,1)[0]