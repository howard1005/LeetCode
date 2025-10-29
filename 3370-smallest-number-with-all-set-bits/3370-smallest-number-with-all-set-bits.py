class Solution:
    def smallestNumber(self, n: int) -> int:
        ans = 1
        while n:
            ans <<= 1
            n >>= 1
        return ans-1