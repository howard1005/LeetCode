class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        ans = 0

        nums.sort(reverse=True)

        d = {}
        for n in nums:
            if n*n in d:
                d[n] = d[n*n] + 1
            else:
                d[n] = 1
            ans = max(ans,d[n])

        return ans if ans > 1 else -1