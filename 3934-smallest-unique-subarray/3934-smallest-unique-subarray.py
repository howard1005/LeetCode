class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        ans = inf

        MOD = 10**9 + 7
        MOD2 = 10**9 + 9
        BASE = 100003
        n = len(nums)

        h1 = [0] * (n + 1)
        h2 = [0] * (n + 1)
        p1 = [1] * (n + 1)
        p2 = [1] * (n + 1)

        for i, v in enumerate(nums):
            h1[i+1] = (h1[i] * BASE + v) % MOD
            h2[i+1] = (h2[i] * BASE + v) % MOD2
            p1[i+1] = p1[i] * BASE % MOD
            p2[i+1] = p2[i] * BASE % MOD2

        def valid(le):
            vis = {}

            for i in range(n - le + 1):
                j = i + le

                # nums[i:j]의 해시: 뒤 누적값 - 앞 누적값
                a = (h1[j] - h1[i] * p1[le]) % MOD
                b = (h2[j] - h2[i] * p2[le]) % MOD2

                key = (a, b)
                vis[key] = vis.get(key, 0) + 1

            return any(cnt == 1 for cnt in vis.values())
                
                



        lo,hi = 1,len(nums)
        while lo<=hi:
            mi = (lo+hi)//2
            if valid(mi):
                ans = min(ans,mi)
                hi = mi - 1
            else:
                lo = mi + 1

        return ans