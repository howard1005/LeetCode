class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
        dp[1][0] = 1
        e = [1 for _ in range(k+1)]
        for i in range(2,n+1):
            for j in range(k+1):
                l = max(0,j-(i-1))
                r = j
                dp[i][j] = (e[j] - e[l] + dp[i-1][l]) % 1000000007
            e[0] = dp[i][0]
            for j in range(1,k+1):
                e[j] = (dp[i][j] + e[j-1]) % 1000000007
        return dp[n][k]