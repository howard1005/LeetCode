class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 1000000007
        
        dp = [[-1 for _ in range(steps+1)] for _ in range(steps+1)]
        
        def dfs(i,s):
            if s == 0:
                return 1 if i == 0 else 0
            
            if dp[i][s] != -1:
                return dp[i][s]
            dp[i][s] = 0
            
            for j in range(-1,2):
                if i+j >= 0 and i+j < arrLen:
                    dp[i][s] += dfs(i+j,s-1)
                    dp[i][s] %= MOD
                    
            return dp[i][s]
        
        return dfs(0,steps)