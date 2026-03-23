class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        ans = -1

        MOD = 10**9+7

        m,n = len(grid),len(grid[0])

        dp = [[[0]*2 for _ in range(n)] for _ in range(m)]

        dp[0][0] = [grid[0][0],grid[0][0]]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                k = grid[i][j]
                l = []
                if i-1>=0:
                    l.extend([v*k for v in dp[i-1][j]])
                if j-1>=0:
                    l.extend([v*k for v in dp[i][j-1]])
                dp[i][j] = [min(l),max(l)]

        # for r in dp:
        #     print(r)
        
        ans = dp[-1][-1][1] 
                    
        return ans%MOD if ans >= 0 else -1