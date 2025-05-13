class Solution:
    dp = []
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 1_000_000_007

        if not self.dp:
            dp = self.dp
            for _ in range(26):
                dp.append([1 for _ in range(100001)])

            for j in range(100001):
                for i in range(25,-1,-1):
                    if i == 25:
                        if j-1 >= 0:
                            dp[i][j] = dp[0][j-1] + dp[1][j-1]
                    else:
                        if j-1 >= 0:
                            dp[i][j] = dp[i+1][j-1]
                    dp[i][j] %= MOD

        dp = self.dp

        ans = 0

        for c in s:
            i = ord(c)-ord('a')
            ans += dp[i][t]

        return ans % MOD