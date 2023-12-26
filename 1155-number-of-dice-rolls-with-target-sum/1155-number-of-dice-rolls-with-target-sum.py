class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 1000000007
        dp = [[0 for _ in range(target+1)] for _ in range(n+1)]
        for i in range(1,min(k+1,target+1)):
            dp[1][i] = 1
        for i in range(2,n+1):
            for j in range(1,target+1):
                for kk in range(1,k+1):
                    if j-kk >= 0:
                        dp[i][j] += dp[i-1][j-kk]
                        dp[i][j] %= MOD
        return dp[n][target]