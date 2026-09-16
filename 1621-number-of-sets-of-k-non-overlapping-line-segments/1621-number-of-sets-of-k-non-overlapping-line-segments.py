class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        ans = 0

        MOD = 10**9+7

        dp = [[[0 for _ in range(2)] for _ in range(k+1)] for _ in range(n+1)]
        dp[-1][0][0] = 1

        for i in range(n-1,-1,-1):
            for r in range(k+1):
                for m in range(2):
                    ret = 0
                    if m == 0:
                        ret += dp[i+1][r][0]
                        ret += dp[i+1][r][1]
                    else:
                        ret += dp[i+1][r][1]
                        if r-1>=0:
                            ret += dp[i+1][r-1][0]
                        if r-1 > 0:
                            ret += dp[i+1][r-1][1]
                    # print(i,r,m,dp[i][r][m])
                    dp[i][r][m] = ret%MOD

        ans = dp[0][k][0]
        # print(dp)

        return ans