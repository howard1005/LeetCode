class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        ans = 0

        m,n = len(grid),len(grid[0])

        dp = [[[0 for _ in range(1024)] for _ in range(n)] for _ in range(m)]

        dp[0][0][grid[0][0]] = 1
        for i in range(1,m):
            v = grid[i][0]
            for x in range(1024):
                dp[i][0][x] = dp[i-1][0][x^v]
        for j in range(1,n):
            v = grid[0][j]
            for x in range(1024):
                dp[0][j][x] = dp[0][j-1][x^v]
            
        
        for i in range(1,m):
            for j in range(1,n):
                v = grid[i][j]
                for x in range(1024):
                    dp[i][j][x] = dp[i-1][j][x^v] | dp[i][j-1][x^v]

        for x in range(1024):
            if dp[-1][-1][x]:
                ans = x
                break            

        return ans