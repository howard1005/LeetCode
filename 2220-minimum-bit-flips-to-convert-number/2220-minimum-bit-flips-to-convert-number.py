class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = 0

        n = start^goal
        while n:
            if n&1:
                ans += 1
            n >>= 1

        return ans 