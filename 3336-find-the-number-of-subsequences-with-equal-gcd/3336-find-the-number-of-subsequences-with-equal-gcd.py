from math import gcd

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        ans = 0

        MOD = 10**9+7

        @cache
        def dfs(i,a,b):
            if i >= len(nums):
                return 1 if a>0 and a==b else 0
            ret = 0
            n = nums[i]
            ret += dfs(i+1,a,b)
            ret += dfs(i+1,gcd(a,n) if a!=0 else n,b)
            ret += dfs(i+1,a,gcd(b,n) if b!=0 else n)
            ret %= MOD
            return ret

        ans = dfs(0,0,0)

        return ans