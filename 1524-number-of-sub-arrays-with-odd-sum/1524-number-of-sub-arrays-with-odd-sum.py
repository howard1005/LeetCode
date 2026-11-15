class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        ans = 0

        MOD = 10**9+7

        cum = 0
        o,e = 0,0
        for n in arr:
            cum += n
            if cum&1:
                ans += e+1
                o += 1
            else:
                ans += o
                e += 1
            ans %= MOD

        return ans