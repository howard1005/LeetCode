class Solution:
    def distinctSubseqII(self, s: str) -> int:
        ans = 0

        MOD = 10**9+7

        dp = [0 for _ in range(len(s))]
        dp[-1] = 1

        d = defaultdict(int)
        sd = set()
        sd.add(s[-1])

        for i in range(len(s)-2,-1,-1):
            c = s[i]
            dp[i] = (2*dp[i+1] - d[c] + (0 if c in sd else 1) + MOD) % MOD
            d[c] = dp[i+1] 
            sd.add(c)

            # print(dp,d)

        ans = dp[0]

        return ans