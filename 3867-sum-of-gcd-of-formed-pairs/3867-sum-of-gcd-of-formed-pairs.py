from math import gcd

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        ans = 0

        pl = [0 for _ in range(len(nums))]

        mx = 0
        for i,n in enumerate(nums):
            mx = max(mx,n)
            pl[i] = gcd(mx,n)
        pl.sort()

        for i in range(len(pl)//2):
            j = len(pl)-i-1
            ans += gcd(pl[i],pl[j])

        return ans