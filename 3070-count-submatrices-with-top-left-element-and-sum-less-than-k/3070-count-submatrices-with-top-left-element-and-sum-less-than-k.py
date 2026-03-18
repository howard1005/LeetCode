class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        ans = 0

        m,n = len(grid),len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        def get_dp(i,j):
            if i>=0 and j>=0:
                return dp[i][j]
            return 0

        for i in range(m):
            for j in range(n):
                dp[i][j] = grid[i][j] + get_dp(i-1,j) + get_dp(i,j-1) - get_dp(i-1,j-1)
                if dp[i][j] <= k:
                    ans += 1

        return ans