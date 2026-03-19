class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        ans = 0

        m,n = len(grid),len(grid[0])

        dp = [[[0]*2 for _ in range(n)] for _ in range(m)]

        def get_dp(i,j):
            if i>=0 and j>=0:
                return dp[i][j]
            return [0,0]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'X':
                    dp[i][j][0] += 1
                if grid[i][j] == 'Y':
                    dp[i][j][1] += 1
                a = get_dp(i,j-1) 
                b = get_dp(i-1,j)
                c = get_dp(i-1,j-1)
                dp[i][j][0] += a[0]
                dp[i][j][0] += b[0]
                dp[i][j][0] -= c[0]  
                dp[i][j][1] += a[1]
                dp[i][j][1] += b[1]
                dp[i][j][1] -= c[1]  
                if dp[i][j][0] != 0 and dp[i][j][0] == dp[i][j][1]:
                    ans += 1

        return ans