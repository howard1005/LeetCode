class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        ans = 0
        
        MOD = 1000000007
        
        dp = [[[-1 for _ in range(k+1)] for _ in range(m+1)] for _ in range(n)]
        
        def dfs(i,mx,kk):
            if i >= n:
                return 1 if kk == 0 else 0
            
            if dp[i][mx][kk] != -1:
                return dp[i][mx][kk]
            dp[i][mx][kk] = 0
            ret = 0
            
            ret += mx*dfs(i+1,mx,kk)
            ret %= MOD

            if kk:
                for j in range(mx+1,m+1):
                    ret += dfs(i+1,j,kk-1)
                    ret %= MOD
            
            dp[i][mx][kk] = ret
            return ret
        
        ans = dfs(0,0,k)
            
        return ans