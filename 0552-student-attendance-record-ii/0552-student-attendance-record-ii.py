class Solution:
    def checkRecord(self, n: int) -> int:

        MOD = 1000000007

        dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n)]

        dp[-1][0][0] = 3
        dp[-1][0][1] = 3
        dp[-1][0][2] = 2
        dp[-1][1][0] = 2
        dp[-1][1][1] = 2
        dp[-1][1][2] = 1
        
        for i in range(n-2,-1,-1):
            for j in range(2):
                for k in range(3):
                    v = 0
                    if j == 0:
                        v = (v+dp[i+1][1][0])%MOD
                    if k < 2:
                        v = (v+dp[i+1][j][k+1])%MOD
                    v = (v+dp[i+1][j][0])%MOD
                    dp[i][j][k] = v

        return dp[0][0][0]