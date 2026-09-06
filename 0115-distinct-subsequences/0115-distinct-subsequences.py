class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for _ in range(len(s))] for _ in range(len(t))]
        cnt = 0
        for si in range(len(s)):
            if s[si] == t[0]:
                cnt += 1
            dp[0][si] = cnt
        for ti in range(1,len(t)):
            for si in range(1,len(s)):
                if t[ti] == s[si]:
                    dp[ti][si] = dp[ti-1][si-1]
                dp[ti][si] += dp[ti][si-1]
        return dp[-1][-1]
                    