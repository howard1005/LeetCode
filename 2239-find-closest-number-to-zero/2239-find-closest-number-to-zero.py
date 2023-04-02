class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        mn = inf
        d = {}
        for n in nums:
            mn = min(abs(n),mn)
            d[n] = 1
        if mn in d:
            return mn
        return -mn
        