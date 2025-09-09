class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        ans = 0
        
        MOD = 1_000_000_007

        
        dp = [0 for _ in range(n)]
        dp[0] = 1

        cut = 0
        for i in range(n):
            for j in range(i+delay,i+forget):
                if j >= len(dp):
                    break
                dp[j] = (dp[j]+dp[i])%MOD
            if i+forget<len(dp):
                cut += dp[i]

        # print(dp)

        ans = (sum(dp)-cut+MOD)%MOD

        return ans