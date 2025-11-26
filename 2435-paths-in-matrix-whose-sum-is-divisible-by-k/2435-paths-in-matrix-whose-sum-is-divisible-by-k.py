class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        ans = 0

        MOD = 1_000_000_007
        
        m,n = len(grid),len(grid[0])

        dp = [[[0 for _ in range(k)] for _ in range(n)] for _ in range(m)]

        dp[0][0][grid[0][0]%k] = 1

        for i in range(m):
            for j in range(n):
                v = grid[i][j]
                for kk in range(k):
                    t = (kk-(v%k)+k)%k
                    if i-1>=0:
                        dp[i][j][kk] += dp[i-1][j][t]
                    if j-1>=0:
                        dp[i][j][kk] += dp[i][j-1][t]
                    dp[i][j][kk] %= MOD
                        
        ans = dp[-1][-1][0]

        return ans