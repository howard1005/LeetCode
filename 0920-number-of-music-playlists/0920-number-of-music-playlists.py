from math import comb

class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 1000000007
        
        dp = [[[-1 for _ in range(n+1)] for _ in range(n+1)] for _ in range(goal)] # idx, remain N, avaliable N
        
        def dfs(i,j,a):
            if i >= goal:
                return 1 if j == 0 else 0
            
            if dp[i][j][a] != -1:
                return dp[i][j][a]
            dp[i][j][a] = 0
            
            if j:
                dp[i][j][a] += j * dfs(i+1,j-1,max(n-k,a-1,0))
                
            dp[i][j][a] += max(a-j,0) * dfs(i+1,j,max(n-k,a-1,0))
            
            dp[i][j][a] %= MOD
            
            # print(i,j,a,dp[i][j][a])
            
            return dp[i][j][a]
        
        
            
        return dfs(0,n,n)
            