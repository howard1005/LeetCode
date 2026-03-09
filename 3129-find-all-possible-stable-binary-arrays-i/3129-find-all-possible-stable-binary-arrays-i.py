class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        ans = 0

        MOD = 1000000007

        dp = [[[0]*2 for _ in range(one+1)] for _ in range(zero+1)]
        zdp = [[[0]*2 for _ in range(one+1)] for _ in range(zero+1)]
        odp = [[[0]*2 for _ in range(one+1)] for _ in range(zero+1)]
        dp[0][0][0] = 1
        dp[0][0][1] = 1
        zdp[0][0][0] = 1
        zdp[0][0][1] = 1
        odp[0][0][0] = 1
        odp[0][0][1] = 1

        for i in range(zero+1):
            for j in range(one+1):
                if i == 0 and j == 0:
                    continue
                dp[i][j][0] = (zdp[i-1][j][1] if i else 0) - (zdp[i-limit-1][j][1] if i-limit-1>=0 else 0)
                dp[i][j][0] %= MOD
                zdp[i][j][0] = (zdp[i-1][j][0] if i else 0) + dp[i][j][0]
                zdp[i][j][0] %= MOD
                odp[i][j][0] = (odp[i][j-1][0] if j else 0) + dp[i][j][0]
                odp[i][j][0] %= MOD

                dp[i][j][1] = (odp[i][j-1][0] if j else 0) - (odp[i][j-limit-1][0] if j-limit-1>=0 else 0)
                dp[i][j][1] %= MOD
                zdp[i][j][1] = (zdp[i-1][j][1] if i else 0) + dp[i][j][1]
                zdp[i][j][1] %= MOD
                odp[i][j][1] = (odp[i][j-1][1] if j else 0) + dp[i][j][1]
                odp[i][j][1] %= MOD    

        # print(dp)
        # print(zdp)
        # print(odp)
        
        ans = sum(dp[zero][one])%MOD

        return ans