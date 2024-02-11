class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(m)]
        
        for j in range(n):
            for k in range(n):
                if j == k:
                    dp[-1][j][k] = grid[-1][j]
                else:
                    dp[-1][j][k] = grid[-1][j] + grid[-1][k]
                    
        for i in range(m-2,-1,-1):
            for j in range(n):
                for k in range(n):
                
                    for a in range(j-1,j+2):
                        for b in range(k-1,k+2):
                            if a<0 or b<0 or a>=n or b>=n:
                                continue
                            dp[i][j][k] = max(dp[i][j][k], dp[i+1][a][b])
                            
                    if j == k:
                        dp[i][j][k] += grid[i][j]
                    else:
                        dp[i][j][k] += grid[i][j] + grid[i][k]
                        
        return dp[0][0][n-1]